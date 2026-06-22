# Manual Reading Batch

Sections 1-4 of 379



========================================================================================


## [001] part-1-foundations-of-embodied-ai\module-01-from-static-ai-to-embodied-ai\section-1.1.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 1: From Static AI to Embodied AI


# Section 1.1: Static prediction vs. embodied interaction


"A classifier answers a question once. An embodied agent answers, then inherits the consequences."


**FIGURE:** Figure 1.1A: Section 1.1: Static prediction vs. embodied interaction becomes easier to reason about when the reader can see the perception, decision, action, and feedback loop as one physical situation.


A Patient Control Loop


**CALLOUT:** Big Picture


Static prediction vs. embodied interaction is the first split that matters in embodied AI. A static model maps an input to an output. An embodied agent maps a stream of observations to actions that change the next stream of observations. A prediction is a statement; an embodied decision is an intervention inside a coupled system.


**CALLOUT:** Reader Pathway


Use this section to make static prediction vs. embodied interaction operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


Concept map for Section 1.1
A local diagram showing how prediction errors flow into state changes and recovery costs.


-

-

-


Evidence
what the agent receives
Decision
what the system changes
Consequence
what the next step inherits
Closed-loop feedback makes the next input depend on the last action.


**FIGURE:** Figure 1.1. Static prediction vs. embodied interaction is easiest to reason about as a closed-loop evidence, decision, consequence pattern: prediction errors flow into state changes and recovery costs.


## From Answering To Intervening


A static model is evaluated on examples sampled from a fixed distribution: images, prompts, tabular rows, point clouds, or short video clips. Its world does not push back. If an image classifier mistakes a mug for a bowl, the mistake ends at the output. The benchmark records an error and moves to the next example.


An embodied system acts on the mistake. A mobile manipulator may grasp the wrong object, move it into a new pose, block the actual target, and create a harder problem for its next observation. The same numerical error is now a state change, a recovery burden, and possibly a safety event. This is why embodied AI starts with trajectories rather than isolated examples.


**CALLOUT:** Action Changes The Dataset


A static benchmark hides the cost of being wrong. In an embodied benchmark, the agent's output becomes part of the next input distribution. Ordinary prediction error can compound into state error, recovery cost, and unsafe behavior.


## The Formal Difference


A static predictor learns a function $f(x)=y$. The input $x$ is given, the output $y$ is scored, and the example ends. An embodied agent receives an observation $o_t$, updates an internal belief $b_t$, chooses an action $a_t$, and receives a new observation $o_{t+1}$ from transition dynamics that depend on $a_t$. The score is a property of a rollout, not a single prediction.


The useful unit is a trajectory, $\tau=(o_0,a_0,o_1,a_1,\ldots,o_T)$. A static loss might score one pair as $\ell(f(x),y)$, while an embodied evaluation scores a policy over time: $J(\pi)=\mathbb{E}_{\tau \sim \pi}\left[\sum_t r_t-\lambda\sum_t c_t\right]$. Here $r_t$ is task progress, $c_t$ is a cost such as collision risk or recovery effort, and $\lambda$ states how much the evaluator penalizes unsafe or expensive behavior. The formula matters because two policies with the same first prediction can separate sharply once their actions reshape later observations.


This changes the scientific question. Static prediction asks, "Did the model label this example correctly?" Embodied interaction asks, "Did the sequence of observations, beliefs, actions, constraints, and recoveries produce reliable task progress?" The second question includes the first, but it also includes timing, dynamics, control authority, safety margins, and the ability to recover from surprises.


Static Prediction And Embodied Interaction


Design questionStatic modelEmbodied agent

InputFixed exampleObservation chosen by prior actions
OutputLabel, score, token, or boxAction, trajectory, skill, or tool call
Evaluation unitExampleEpisode or rollout
Main riskWrong answerWrong state transition plus recovery cost


## Worked Example: Episode Accounting


The compact implementation below turns the distinction into bookkeeping. A static score would count independent mistakes. The embodied log carries state forward, so an early mistake can change whether later actions are safe, useful, or recoverable.


```text
# Section 1.1: runnable checkpoint for Static prediction vs. embodied interaction.
# Keep the output small so the evidence record can be inspected directly.
from dataclasses import dataclass

@dataclass
class EpisodeLog:
    successes: int = 0
    interventions: int = 0
    recoveries: int = 0
    unsafe_actions: int = 0

def run_pick_episode(predictions, safety_flags):
    log = EpisodeLog()
    block_pose_known = False
    gripper_clear = True
    for prediction, safe in zip(predictions, safety_flags):
        log.interventions += 1
        if not safe:
            log.unsafe_actions += 1
            gripper_clear = False
            continue
        if prediction == "target_visible":
            block_pose_known = True
        elif prediction == "target_grasped" and block_pose_known and gripper_clear:
            log.successes += 1
        else:
            log.recoveries += 1
            gripper_clear = True
    return log

rollout = run_pick_episode(
    predictions=["target_visible", "wrong_object", "target_grasped"],
    safety_flags=[True, True, True],
)
print(rollout)
```


**CODE CAPTION:** Code Fragment 1.1.1 records how one wrong embodied decision changes later episode state.


**CALLOUT:** Library Shortcut: Gymnasium Episode Semantics


The hand-built example is about 30 lines because it exposes state carryover. Gymnasium reduces the environment side to reset and step, while handling observation spaces, action spaces, termination, truncation, wrappers, and reproducible seeds. The shortcut is the move from hand-coded episode accounting to comparable environment logs. Keep the hand-built version for learning and debugging; use Gymnasium when experiments need repeatability.


## Practical Recipe


- Write the static task first: what would the model predict if no action followed?


- Write the embodied task second: what action consumes that prediction, and what state changes if it is wrong?


- Log observations, actions, safety flags, success, recovery, latency, and termination reason in one episode artifact.


- Compare metrics only when they are co-computed on the same environment, policy, split, seed set, and evaluation script.


- Inspect early rollout failures for compounding effects before changing the model architecture.


**CALLOUT:** Warning: Point Accuracy Can Mislead


A grasp detector with excellent image-level accuracy can still fail inside a robot loop if rare errors occur near collisions, occlusions, or irreversible state changes. Closed-loop evaluation must weight where errors happen, not only how often they happen.


**CALLOUT:** Practical Example: Warehouse Picking


A warehouse team first measured object detection quality for a bin-picking robot. The score looked strong, but false positives near transparent packaging caused bad grasps and costly recoveries. The team added episode logs with target visibility, chosen grasp pose, contact outcome, recovery count, and time to clear the bin. Those logs showed that a lower-confidence detector with a reject option achieved higher completed picks per hour because it avoided compounding mistakes.


**CALLOUT:** Fun Note


A static benchmark lets each mistake leave quietly. A robot loop asks the mistake to help clean up before the next timestep.


**CALLOUT:** Research Frontier


OpenVLA-style vision-language-action systems blur the line between predictor and controller by emitting robot actions from image and language context. The frontier question is not whether a large model can choose plausible actions. It is whether the closed loop remains calibrated under distribution shift, latency, contact, and recovery pressure.


**CALLOUT:** Self Check


For a task you know, name one static metric and one trajectory metric. Then describe a case where the static metric improves while the trajectory metric gets worse.


## Builder's Deep Dive


The practical difference between a predictor and an embodied policy is not philosophical. It appears in the error ledger. A static model pays once for a wrong label. A robot pays again if the wrong action occludes the target, changes frictional contact, consumes time, triggers a recovery routine, or moves the system outside the training distribution. A useful closed-loop experiment therefore logs where the error occurred in the episode, what state it changed, and which later measurements inherited that change.


For this reason, the first build artifact should be an episode table, not a leaderboard row. Each row should contain the observation hash, action command, action precondition, safety gate output, controller result, next observation hash, reward, cost, and termination reason. Once those fields exist, a builder can distinguish a harmless perception miss from a compounding embodied failure.


Practical Tool Choices For Section 1.1

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumturns independent examples into reset, step, termination, truncation, and wrapper-managed episode tracesUse it to prove that the observation, action, reward, and termination contract is explicit before moving to heavier simulation.MuJoCoexposes whether a prediction error becomes a contact, timing, or recovery problemUse it when the next observation depends on contact dynamics, actuator limits, or failed grasps.LeRobotconnects policy logs to real robot datasets, action chunks, and deployment tracesUse it when the distinction between offline prediction quality and rollout quality must be tested on robot trajectories.


## Implementation Recipe


Start with an isolated predictor, wrap it in the smallest action loop that consumes its output, and compare the two error ledgers. The goal is to show exactly when a wrong prediction becomes a changed state.


- Name the static output and its ordinary per-example metric.

- Name the action that consumes that output and the precondition that makes the action legal.

- Record whether the action changed the next observation, required recovery, or violated a constraint.

- Report first-error location, downstream recovery count, and final episode result together.

- Compare static and embodied variants only on the same object set, seed set, controller, and reset distribution.


```text
# Diagnose whether a classifier error stays local or compounds through a rollout.
events = [
    {"t": 0, "prediction": "target_visible", "action": "approach", "safe": True, "state_delta": "target_closer"},
    {"t": 1, "prediction": "wrong_object", "action": "grasp", "safe": True, "state_delta": "target_occluded"},
    {"t": 2, "prediction": "target_visible", "action": "grasp", "safe": False, "state_delta": "recovery_required"},
]

def embodied_error_ledger(events: list[dict[str, object]]) -> dict[str, object]:
    first_bad_step = None
    recovery_steps = 0
    inherited_errors = []
    for event in events:
        bad_prediction = event["prediction"] == "wrong_object"
        changed_future = event["state_delta"] in {"target_occluded", "recovery_required"}
        if bad_prediction and first_bad_step is None:
            first_bad_step = event["t"]
        if event["state_delta"] == "recovery_required":
            recovery_steps += 1
        if first_bad_step is not None and changed_future:
            inherited_errors.append((event["t"], event["state_delta"]))
    return {
        "first_bad_step": first_bad_step,
        "recovery_steps": recovery_steps,
        "compounded": bool(inherited_errors),
        "inherited_errors": inherited_errors,
    }

print(embodied_error_ledger(events))
```


**CODE CAPTION:** Code Fragment 1.1.2 turns prediction mistakes into an embodied error ledger that records first bad step, recovery load, and inherited state changes.


**CALLOUT:** Teaching Move


Give students a static confusion matrix and an episode log from the same task. Ask them to identify which static mistakes matter most once action consequences are included. The useful discussion is usually about error location, not aggregate accuracy.


## Failure Analysis Pattern


When closed-loop performance falls below static performance, classify the first nonlocal error. Did the output trigger an illegal action, create an occlusion, exhaust a timing budget, push the controller outside its stable region, or cause a recovery policy to enter a loop? Repair the earliest causal link before changing the model family.


## Hands-On Lab: Build a Section Evidence Trace

Duration: ~65 minutesDifficulty: Intermediate


### Objective


Turn Static prediction vs. embodied interaction into a small artifact that compares a hand-built baseline with a maintained-tool shortcut under one perturbation.


### What You'll Practice

- Define an observation, action, metric, and perturbation contract

- Build a minimal baseline trace

- Preserve the same schema for the library shortcut

- Write a failure postmortem from the evidence record


### Setup


```text
pip install numpy pandas
```


**CODE CAPTION:** Code Fragment 1.1.L1 installs NumPy and pandas for the section lab trace.


### Steps


#### Step 1: Define the contract


Write the fields that make two runs comparable.


```text
contract = {
    "observation": "timestamped RGB-D frame plus robot joint state",
    "action": "bounded end-effector delta pose",
    "metric": "task success, collision count, and recovery latency",
    "perturbation": "120 ms observation delay with unchanged task reset seed",
}

def missing_contract_fields(payload: dict[str, str]) -> dict[str, object]:
    missing = [key for key, value in payload.items() if value == ""]
    return {"contract": payload, "missing_fields": missing}

print(missing_contract_fields(contract))
```


**CODE CAPTION:** Code Fragment 1.1.L1.1 records Step 1, Define the contract, and reports that the evidence fields are concrete and ready for comparison.

Hint


Start with the smallest deterministic trace. Add the perturbation only after the baseline and shortcut share the same artifact schema.


#### Step 2: Record the baseline


Save one deterministic result before adding noise or latency.


```text
baseline = {"run": "baseline", "seed": 0, "success": 0.82, "failure_label": "none"}

def summarize_baseline(payload: dict[str, object]) -> dict[str, object]:
    missing = sorted(key for key, value in payload.items() if value in (0.0, "", None))
    return {"record": payload, "missing_fields": missing}

print(summarize_baseline(baseline))
```


**CODE CAPTION:** Code Fragment 1.1.L1.2 records Step 2, Record the baseline, and reports that the evidence fields are concrete and ready for comparison.

Hint


Start with the smallest deterministic trace. Add the perturbation only after the baseline and shortcut share the same artifact schema.


#### Step 3: Add the shortcut


Run or sketch the maintained-tool version while keeping the artifact schema fixed.


```text
shortcut = {"run": "library_shortcut", "seed": 0, "success": 0.86, "failure_label": "none"}

def summarize_shortcut(payload: dict[str, object]) -> dict[str, object]:
    missing = sorted(key for key, value in payload.items() if value in (0.0, "", None))
    return {"record": payload, "missing_fields": missing}

print(summarize_shortcut(shortcut))
```


**CODE CAPTION:** Code Fragment 1.1.L1.3 records Step 3, Add the shortcut, and reports that the evidence fields are concrete and ready for comparison.

Hint


Start with the smallest deterministic trace. Add the perturbation only after the baseline and shortcut share the same artifact schema.


#### Step 4: Apply one perturbation


Change exactly one condition and preserve the same logging fields.


```text
perturbed = {**baseline, "run": "baseline_perturbed", "success": 0.61, "failure_label": "latency_induced_miss"}

def summarize_perturbed(payload: dict[str, object]) -> dict[str, object]:
    missing = sorted(key for key, value in payload.items() if value in (0.0, "", None))
    return {"record": payload, "missing_fields": missing}

print(summarize_perturbed(perturbed))
```


**CODE CAPTION:** Code Fragment 1.1.L1.4 records Step 4, Apply one perturbation, and reports that the evidence fields are concrete and ready for comparison.

Hint


Start with the smallest deterministic trace. Add the perturbation only after the baseline and shortcut share the same artifact schema.


### Expected Output


The completed lab produces one table with baseline, shortcut, and perturbed rows, plus a short note explaining which comparison is valid because all metrics were co-computed under one schema.


### Stretch Goals

- Add a second seed and report mean and spread.

- Write a one-paragraph postmortem that separates root cause from symptom.


Complete Solution


```text
# Complete compact evidence trace for the section lab.
# Extend these records with values produced by your actual environment or simulator.
import pandas as pd

records = [
    {"run": "baseline", "seed": 0, "success": 0.72, "failure_label": "none"},
    {"run": "library_shortcut", "seed": 0, "success": 0.78, "failure_label": "none"},
    {"run": "baseline_perturbed", "seed": 0, "success": 0.54, "failure_label": "latency"},
]
print(pd.DataFrame(records))
```


**CODE CAPTION:** Code Fragment 1.1.L2 creates a complete same-schema evidence table for the section lab.


**CALLOUT:** Key Takeaway


Embodied AI starts when output quality is no longer enough. The decisive object is the closed-loop trajectory created by predictions, actions, dynamics, constraints, and recovery.


**CALLOUT:** Exercise 1.1.1


Wrap a familiar classifier in a hypothetical action loop. Define the observation, action, transition consequence, safety constraint, episode metric, and one error that would compound over time.


### What's Next?


Section 1.2 expands this into the perception-action loop, where sensing and acting become one coupled process.


## Bibliography & Further Reading


### Foundational References For This Section


Sutton, R. S., and Barto, A. G.. "Reinforcement Learning: An Introduction." (2018). http://incompleteideas.net/book/the-book-2nd.html


The durable reference for interaction, return, policies, and episode-level evaluation.


Brohan, A. et al.. "RT-1: Robotics Transformer for real-world control at scale." (2022). https://arxiv.org/abs/2212.06817


A useful anchor for large-scale robot policy learning from real interaction data.


Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." (2023). https://arxiv.org/abs/2310.08864


Shows why cross-embodiment data matters for the Physical AI framing.


========================================================================================


## [002] part-1-foundations-of-embodied-ai\module-01-from-static-ai-to-embodied-ai\section-1.2.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 1: From Static AI to Embodied AI


# Section 1.2: Why intelligence needs a world; the perception-action loop


"I sensed, therefore I acted. Then I had to sense what acting had done."


**FIGURE:** Figure 1.2A: Section 1.2: Why intelligence needs a world; the perception-action loop is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation.


A Reflective Mobile Robot


**CALLOUT:** Big Picture


The perception-action loop is the central abstraction of embodied AI. Intelligence is not a detached computation over a finished dataset. It is a recurring cycle in which sensing, state estimation, prediction, decision, control, and learning continually reshape one another.


**CALLOUT:** Reader Pathway


Use this section to make why intelligence needs a world; the perception-action loop operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


Concept map for Section 1.2
A local diagram showing how the world closes the loop between perception and action.


-

-

-


Evidence
what the agent receives
Decision
what the system changes
Consequence
what the next step inherits
Closed-loop feedback makes the next input depend on the last action.


**FIGURE:** Figure 1.2. Why intelligence needs a world; the perception-action loop is easiest to reason about as a closed-loop evidence, decision, consequence pattern: the world closes the loop between perception and action.


## Why A World Is Not Optional


A world supplies consequences. Without consequences, an AI system can describe, classify, retrieve, or plan, but it cannot test whether its plan survives timing, friction, occlusion, other agents, or actuator limits. Embodied intelligence uses the world as both problem and teacher.


The loop has six recurring roles. Sensors produce observations. Representation turns observations into a compact working state. Prediction estimates what may happen next. Decision selects an action under goals and constraints. Control executes the action through hardware or simulation. Learning updates future behavior from the observed result.


**CALLOUT:** The Loop Is The Unit


No single component owns intelligence in an embodied system. Good behavior comes from the fit among perception, memory, prediction, policy, controller, safety layer, and evaluation. A weak interface can erase the value of a strong model.


## The Loop As A Dynamical System


At time $t$, an agent receives observation $o_t$, maintains belief $b_t$, chooses action $a_t$, and receives a reward, cost, or other feedback after the environment transitions. In a fully observed problem, $o_t$ may contain the state. In most embodied settings, the true state is hidden, so the agent acts from belief rather than certainty.


A compact belief update is $b_{t+1}(s') \propto O(o_{t+1}\mid s')\sum_s T(s'\mid s,a_t)b_t(s)$. The transition model $T$ predicts where the world could move after the action, and the observation model $O$ reweights those possibilities using the new sensor data. This is the mathematical reason probing actions matter: an action can be useful even before it reaches the goal if it makes the next belief sharper.


Partial observability is not an edge case. Cameras miss what is behind an object. Lidars miss reflective surfaces. Tactile sensors only report contact after contact occurs. Language instructions omit operational details. A capable embodied agent must infer, probe, remember, and recover.


**CALLOUT:** Mechanism: Six Contracts


The practical loop is six measurable contracts: sensor contract, representation contract, prediction contract, decision contract, control contract, and evaluation contract. If one contract is implicit, debugging collapses into guessing which subsystem failed.


## Worked Example: A Belief-Carrying Loop


The code below names the loop elements explicitly. It is not a complete robot stack. It is the control-flow skeleton that later reappears inside Gymnasium, PettingZoo, MuJoCo, Isaac Lab, ROS 2 deployments, and OpenVLA-style rollout evaluators.


```text
# Section 1.2: runnable checkpoint for Why intelligence needs a world; the perception-action loop.
# Keep the output small so the evidence record can be inspected directly.
def embodied_loop(agent, env, horizon):
    observation, info = env.reset(seed=7)
    belief = agent.initial_belief(info)
    episode = []

    for step in range(horizon):
        action = agent.act(observation, belief)
        next_observation, reward, terminated, truncated, info = env.step(action)
        next_belief = agent.update_belief(belief, action, next_observation, info)
        episode.append({
            "step": step,
            "action": action,
            "reward": reward,
            "terminated": terminated,
            "truncated": truncated,
            "belief_quality": info.get("belief_quality"),
        })
        observation, belief = next_observation, next_belief
        if terminated or truncated:
            break
    return episode
```


**CODE CAPTION:** Code Fragment 1.2.1 states the perception-action loop as executable control flow with belief updates and termination logs.


Expected output: the printed trace for Why intelligence needs a world; the perception-action loop should expose the method configuration, the measured evidence field, and the failure label. If one of those fields is missing or unchanged under the perturbation, the example is not yet an evaluation artifact.


**CALLOUT:** Library Shortcut: Gymnasium And PettingZoo


The hand-written loop is about 25 lines because it exposes every moving part. Gymnasium compresses the environment side to reset and step, with standardized observations, rewards, termination, truncation, and spaces. PettingZoo extends the same discipline to multi-agent loops through AEC and parallel APIs. The libraries do not solve intelligence, but they make the loop comparable and auditable.


## Practical Recipe


- Start every design document with a loop diagram: observe, estimate, predict, decide, act, learn.


- Define the time scale for each component. Vision may run at 10 Hz, control at 200 Hz, and planning only when the task changes.


- Record belief updates separately from raw observations so state-estimation errors remain visible.


- Use Gymnasium for single-agent prototypes and PettingZoo when another agent can change the transition dynamics.


- Carry the same logging fields into MuJoCo, Isaac Lab, ROS 2, and real robot tests.


**CALLOUT:** Warning: Hidden State Is Still State


If a variable affects success but is missing from the observation, the agent must infer it, probe for it, or remain robust to it. Pretending the system is fully observed usually produces policies that work in demos and fail under small changes.


**CALLOUT:** Practical Example: Drone Inspection


A drone inspecting roof damage cannot treat each image as an independent classification problem. Wind changes camera pose, battery reserve changes the feasible path, glare changes visibility, and earlier viewpoints determine what remains unseen. The useful log includes pose estimate, image frame, chosen waypoint, collision margin, battery reserve, and inspection coverage.


**CALLOUT:** Fun Note


The perception-action loop is a group project where the world insists on doing the peer review immediately.


**CALLOUT:** Research Frontier


Modern embodied research increasingly asks agents to choose observations, not only actions. Active perception, latent world models, and video-prediction systems let an agent ask which motion would reduce uncertainty before committing to a high-cost action.


**CALLOUT:** Self Check


In Code Fragment 1.2.1, which variables are observed, which are estimated, and which are chosen? If you cannot separate them, your implementation will be difficult to debug.


## Builder's Deep Dive


The perception-action loop becomes engineering reality when every module has a rate, latency budget, input contract, and output contract. A camera may run at 30 Hz, state estimation at 100 Hz, a learned policy at 5 to 20 Hz, and a low-level controller at 250 to 1000 Hz. A loop that looks clean in a diagram can fail because the policy consumes stale state, the planner replans slower than the disturbance, or the safety layer receives commands after the controller has already moved.


A useful design review therefore asks whether the loop is synchronous, event-driven, or hierarchical. Reactive collision checks belong near the controller. Belief updates may be slower but must expose uncertainty. High-level language or task planning can be slower still, but it must not be allowed to issue commands whose preconditions have expired.


Practical Tool Choices For Section 1.2

Tool or LibraryRole in This TopicBuilder AdviceROS 2makes perception, estimation, planning, and control interfaces explicit through topics, services, actions, clocks, and QoSUse it when the loop must survive real sensor rates, message drops, and distributed timing.MuJoColets the same perception-action loop be stepped under controlled dynamics and latency perturbationsUse it to test whether a loop is stable before exposing hardware to contact or speed.BehaviorTree.CPPkeeps high-level task control separate from fast feedback loopsUse it when the agent must switch among inspect, act, recover, and abort behaviors without hiding preconditions.


## Implementation Recipe


Build a loop timing table before selecting a policy architecture. The table should state producer, consumer, message, nominal rate, maximum tolerated age, and failure action. This catches many failures that model-centric prototypes miss.


- List every loop edge from sensor measurement to actuator command.

- Assign a rate and maximum message age to each edge.

- Define the behavior when a message is late, missing, or inconsistent with the current belief.

- Inject one delay and one dropout into a replayed trace.

- Accept the loop only if the failure action is explicit and observable in the log.


```text
# Check whether a perception-action loop is consuming stale information.
loop_edges = [
    {"edge": "camera_to_state_estimator", "rate_hz": 30, "max_age_ms": 80, "age_ms": 42},
    {"edge": "state_to_policy", "rate_hz": 10, "max_age_ms": 120, "age_ms": 135},
    {"edge": "policy_to_controller", "rate_hz": 20, "max_age_ms": 60, "age_ms": 35},
    {"edge": "controller_to_actuator", "rate_hz": 500, "max_age_ms": 10, "age_ms": 7},
]

def stale_edges(edges: list[dict[str, object]]) -> list[dict[str, object]]:
    failures = []
    for edge in edges:
        stale = edge["age_ms"] > edge["max_age_ms"]
        if stale:
            failures.append({
                "edge": edge["edge"],
                "age_ms": edge["age_ms"],
                "max_age_ms": edge["max_age_ms"],
                "required_action": "hold_position_and_request_fresh_state",
            })
    return failures

print(stale_edges(loop_edges))
```


**CODE CAPTION:** Code Fragment 1.2.2 audits loop timing and identifies the exact edge where perception has become too stale for action.


**CALLOUT:** Teaching Move


Ask students to draw the same robot loop twice: once as information flow and once as timing constraints. The second drawing usually reveals whether a proposed intelligence story can run on a physical system.


## Failure Analysis Pattern


When the loop fails, locate the first broken edge rather than blaming the whole agent. Common causes are stale observations, belief updates that ignore action effects, policies that command outside controller limits, recovery routines that erase useful state, and safety gates that arrive too late. Rerun the smallest replay that reproduces the broken edge.


**CALLOUT:** Key Takeaway


The perception-action loop is the backbone of this book. Every later tool, from MuJoCo to OpenVLA-style policies, is useful only insofar as it clarifies or improves part of this loop.


**CALLOUT:** Exercise 1.2.1


Draw the loop for a household robot that must set a table. Mark which components run continuously, which run on demand, and which variables are hidden from direct sensing.


### What's Next?


Section 1.3 names the pieces of the loop: agents, environments, observations, actions, rewards, and constraints.


## Bibliography & Further Reading


### Foundational References For This Section


Sutton, R. S., and Barto, A. G.. "Reinforcement Learning: An Introduction." (2018). http://incompleteideas.net/book/the-book-2nd.html


The durable reference for interaction, return, policies, and episode-level evaluation.


Brohan, A. et al.. "RT-1: Robotics Transformer for real-world control at scale." (2022). https://arxiv.org/abs/2212.06817


A useful anchor for large-scale robot policy learning from real interaction data.


Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." (2023). https://arxiv.org/abs/2310.08864


Shows why cross-embodiment data matters for the Physical AI framing.


========================================================================================


## [003] part-1-foundations-of-embodied-ai\module-01-from-static-ai-to-embodied-ai\section-1.3.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 1: From Static AI to Embodied AI


# Section 1.3: Agents, environments, observations, actions, rewards, constraints


"Agents, environments, observations, actions, rewards, constraints matters when the next action changes the evidence you thought you had."


**FIGURE:** Figure 1.3A: Section 1.3: Agents, environments, observations, actions, rewards, constraints is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation.


A Careful Control Loop


**CALLOUT:** Big Picture


Agents, environments, observations, actions, rewards, constraints are the interface words that keep embodied AI experiments honest. They separate what the agent can see, what it can change, what the evaluator rewards, and what the system is not allowed to violate.


**CALLOUT:** Reader Pathway


Read this section as an interface manifest. First separate state from observation, then separate action authority from reward, then add constraints that remain visible even when the reward looks good.


Concept map for Section 1.3
A local diagram showing how interface terms separate what the agent sees from what the evaluator knows.


-

-

-


Evidence
what the agent receives
Decision
what the system changes
Consequence
what the next step inherits
Closed-loop feedback makes the next input depend on the last action.


**FIGURE:** Figure 1.3. Agents, environments, observations, actions, rewards, constraints is easiest to reason about as a closed-loop evidence, decision, consequence pattern: interface terms separate what the agent sees from what the evaluator knows.


## What This Section Develops


This section turns six familiar reinforcement-learning terms into a practical contract for embodied systems. The contract prevents a common mistake: treating the reward as the whole task while leaving observations, action limits, and safety constraints implicit.


The key question is practical: what does the evaluator know, what does the agent actually observe, what actions are physically available, and which constraints must remain separate from reward?


**CALLOUT:** Action Is The Test


A reward names preference. A constraint names a boundary. If those are merged into one scalar too early, a policy can appear strong while learning to trade safety, recoverability, or hardware limits for short-term score.


## Theory


A useful formal model is the constrained partially observed decision process $\mathcal{M}=(\mathcal{S},\mathcal{O},\mathcal{A},T,O,r,c,\gamma)$. The environment state $s_t$ lives in $\mathcal{S}$, the agent receives observation $o_t$ from $\mathcal{O}$, chooses action $a_t$ from $\mathcal{A}$, and the transition model $T$ determines what can happen next. The reward $r$ measures task progress, while the cost or constraint signal $c$ records violations such as collision, force, workspace, energy, or latency limits.


The important separation is epistemic. The evaluator may know the simulator state, the full object pose, or the collision margin. The agent often sees only an image, a proprioceptive vector, a tactile event, or a language instruction. A reproducible experiment states both views instead of pretending they are the same.


**CALLOUT:** Mechanism


The mechanism is an interface boundary. Observations constrain belief, actions constrain authority, rewards shape optimization, and constraints bound acceptable behavior. Debugging becomes possible when each boundary has a logged field and unit.


## Worked Example


Code Fragment 1.3.1 makes the boundary explicit for a tabletop pick. The agent sees a noisy pose estimate and a short action menu, while the evaluator records reward and constraint status from the same transition.


```text
# Separate the agent's local view from the evaluator's full transition record.
# Keep reward and constraint labels distinct so success cannot hide a violation.
transition = {
    "true_block_pose": (0.42, 0.18),
    "observed_block_pose": (0.40, 0.21),
    "available_actions": ["approach", "grasp", "relocalize"],
    "chosen_action": "grasp",
    "reward": 1.0,
    "constraint_violation": "force_limit",
}
def split_views(payload: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    agent_view = {
        "observation": payload["observed_block_pose"],
        "actions": payload["available_actions"],
    }
    evaluator_view = {
        "state": payload["true_block_pose"],
        "action": payload["chosen_action"],
        "reward": payload["reward"],
        "constraint": payload["constraint_violation"],
    }
    return agent_view, evaluator_view

agent_view, evaluator_view = split_views(transition)
print("agent_view:", agent_view)
print("evaluator_view:", evaluator_view)
```


**CODE OUTPUT:** agent_view: {'observation': (0.4, 0.21), 'actions': ['approach', 'grasp', 'relocalize']}
evaluator_view: {'state': (0.42, 0.18), 'action': 'grasp', 'reward': 1.0, 'constraint': 'force_limit'}


**CODE CAPTION:** Code Fragment 1.3.1 separates the noisy observation available to the policy from the fuller transition record used by the evaluator. The example also keeps reward and constraint_violation as different fields, which prevents a successful grasp from hiding an unsafe force event.


Expected output: the two printed views should differ. If the agent view and evaluator view are identical, the experiment is probably leaking state information into the policy.


**CALLOUT:** Library Shortcut: Spaces And Wrappers


Gymnasium turns the same contract into declared observation spaces, action spaces, rewards, termination flags, truncation flags, and wrapper-managed logs. PettingZoo extends the contract when multiple agents alter the transition dynamics. These tools do not choose the right abstraction for you, but they make the chosen abstraction inspectable.


## Practical Recipe


- Write the hidden state fields the evaluator may use, then write the smaller observation fields the agent receives.


- Declare the action space with units, rate limits, and invalid-action handling.


- Keep reward and constraint logs separate until final reporting.


- Record termination, truncation, recovery, and safety fields in every episode artifact.


- Run one ablation where reward is unchanged but a constraint changes, then inspect whether the policy behavior changes.


**CALLOUT:** Common Failure Mode


Reward hacking often begins as interface ambiguity. If collision, time, energy, and intervention are folded into one opaque score, a policy can improve the score by exploiting the measurement rather than solving the task.


**CALLOUT:** Practical Example: Bin Picking Contract


For a bin-picking arm, the environment state may include every object pose and contact force, but the agent may see only an RGB-D crop and gripper opening. The action might be a 6D grasp pose plus gripper command. Reward can credit a successful pick, while constraints separately record table collision, excessive force, dropped objects, and human intervention.


**CALLOUT:** Fun Note


Rewards are the applause, constraints are the building inspector, and both arrive after the agent has already touched the world.


**CALLOUT:** Research Frontier


A major open problem is how much structure to keep around learned policies. End-to-end policies can absorb observation and action conventions, but explicit constraints, safety filters, and calibrated uncertainty remain easier to audit when they are represented outside the policy head.


**CALLOUT:** Self Check


For a robot crossing a cluttered room, list one hidden state variable, one observation, one action, one reward, and one constraint. Which of those may the evaluator know even when the agent does not?


## Builder's Deep Dive


An interface manifest is the compact artifact that makes this section teachable. It states $\mathcal{S}$ for evaluator-only state, $\mathcal{O}$ for policy-visible observations, $\mathcal{A}$ for allowed actions, $r$ for preferences, and $c$ for constraints. When those fields are explicit, a reader can tell whether a method improved perception, changed the action space, relaxed a constraint, or benefited from privileged information.


The serious habit is to ask which variable moved. If success rises because the observation included ground-truth pose, that is not the same claim as success rising because the policy learned better visual grounding. Keeping those claims separate prevents leakage and makes construct-matched comparison possible.


Practical Tool Choices For Section 1.3

Tool or LibraryRole in This TopicBuilder AdviceGymnasium spacesdeclares observation and action bounds, dtypes, shapes, and invalid-action behaviorUse spaces as executable documentation for what the policy can see and do.PettingZooextends the contract to multi-agent environments where each agent has a distinct observation and action authorityUse it when another robot, person, or traffic participant changes the transition dynamics.Safety Gymnasiumkeeps reward and cost signals separate in constrained-control experimentsUse it when success must not be allowed to hide collisions, energy overuse, or rule violations.


## Implementation Recipe


Turn the interface vocabulary into a leak test. A leak test checks whether the policy-visible observation contains evaluator-only state, whether the action exposes impossible authority, and whether reward has silently absorbed a constraint.


- Write separate dictionaries for evaluator state, policy observation, allowed action, reward, and cost.

- Check that no evaluator-only key appears in the policy observation unless the deployment sensor can provide it.

- Check that every action has units, bounds, and invalid-action handling.

- Check that each safety constraint remains a separate field until the final report.

- Store the manifest next to every result table so readers can interpret what changed.


```text
# Detect privileged-state leakage and reward-cost mixing in an embodied interface.
manifest = {
    "evaluator_state": {"true_pose", "contact_force", "object_id", "collision_margin"},
    "policy_observation": {"rgbd_crop", "gripper_width", "true_pose"},
    "action_fields": {"dx_m", "dy_m", "dz_m", "yaw_rad", "gripper_command"},
    "reward_fields": {"picked_target"},
    "cost_fields": {"collision_margin", "force_limit_violation"},
}

def interface_warnings(manifest: dict[str, set[str]]) -> list[str]:
    warnings = []
    privileged = manifest["evaluator_state"] & manifest["policy_observation"]
    if privileged:
        warnings.append(f"privileged observation fields: {sorted(privileged)}")
    mixed = manifest["reward_fields"] & manifest["cost_fields"]
    if mixed:
        warnings.append(f"reward-cost mixing: {sorted(mixed)}")
    if not {"dx_m", "dy_m", "dz_m"} <= manifest["action_fields"]:
        warnings.append("cartesian action lacks complete translational units")
    return warnings

print(interface_warnings(manifest))
```


**CODE CAPTION:** Code Fragment 1.3.2 checks for privileged observation leakage and reward-cost mixing before a policy result is trusted.


**CALLOUT:** Teaching Move


Give students a published result table and ask them to reconstruct the manifest that would make the result interpretable. Missing observation, action, or cost fields are usually where comparison claims become fragile.


## Failure Analysis Pattern


When this interface fails, first ask whether the agent lacked information, lacked authority, pursued the wrong reward, or violated a constraint. Then rerun one controlled perturbation that changes only that field. This turns a disappointing rollout into evidence about the boundary that failed.


**CALLOUT:** Key Takeaway


The agent-environment vocabulary is useful because it prevents hidden state, action authority, reward, and constraint from being confused. Strong embodied evaluations make each one visible in the same artifact.


**CALLOUT:** Exercise 1.3.1


Design a method-matched experiment for Agents, environments, observations, actions, rewards, constraints. Specify the environment, observation schema, action interface, metric, and one perturbation that targets the section's core assumption.


### What's Next?


Section 1.4 separates physical embodiment from simulated embodiment and explains why both matter.


## Bibliography & Further Reading


### Foundational References For This Section


Sutton, R. S., and Barto, A. G.. "Reinforcement Learning: An Introduction." (2018). http://incompleteideas.net/book/the-book-2nd.html


The durable reference for interaction, return, policies, and episode-level evaluation.


Brohan, A. et al.. "RT-1: Robotics Transformer for real-world control at scale." (2022). https://arxiv.org/abs/2212.06817


A useful anchor for large-scale robot policy learning from real interaction data.


Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." (2023). https://arxiv.org/abs/2310.08864


Shows why cross-embodiment data matters for the Physical AI framing.


========================================================================================


## [004] part-1-foundations-of-embodied-ai\module-01-from-static-ai-to-embodied-ai\section-1.4.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 1: From Static AI to Embodied AI


# Section 1.4: Physical vs. simulated embodiment


"Physical vs. simulated embodiment matters when the next action changes the evidence you thought you had."


**FIGURE:** Figure 1.4A: Section 1.4: Physical vs. simulated embodiment is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation.


A Careful Control Loop


**CALLOUT:** Big Picture


Physical vs. simulated embodiment is a question about what kind of evidence a result can support. Simulation gives repeatability, controllable perturbations, and cheap failures. Hardware gives contact, latency, calibration drift, wear, and the final test of whether the modeled assumptions were strong enough.


**CALLOUT:** Reader Pathway


Read this section as a validation ladder. First ask what the simulator can control, then ask what the hardware can reveal, then require one shared artifact that records the gap between them.


Concept map for Section 1.4
A local diagram showing how simulation provides repeatability while hardware supplies final accountability.


-

-

-


Evidence
what the agent receives
Decision
what the system changes
Consequence
what the next step inherits
Closed-loop feedback makes the next input depend on the last action.


**FIGURE:** Figure 1.4. Physical vs. simulated embodiment is easiest to reason about as a closed-loop evidence, decision, consequence pattern: simulation provides repeatability while hardware supplies final accountability.


## What This Section Develops


This section develops the contract between simulated evidence and physical evidence. A simulator is not a lesser world; it is a world with declared equations, controllable initial conditions, and missing nuisance factors. A robot is not automatically more scientific; it is a test bed with richer nuisance factors and fewer opportunities for perfect replay.


The key question is practical: which claims can the simulator support, which claims require hardware, and how do we measure the sim-real gap without changing the task definition?


**CALLOUT:** Action Is The Test


Simulation validates counterfactuals. Hardware validates accountability. A serious embodied result normally needs both: simulation to isolate causes and hardware to check whether the isolated causes still matter under contact, latency, and calibration error.


## Theory


Let $T_{\text{sim}}(s'\mid s,a)$ be the simulator transition model and $T_{\text{real}}(s'\mid s,a)$ be the physical transition process. Sim-to-real work is the attempt to make policy conclusions robust when $T_{\text{sim}} \neq T_{\text{real}}$. The difference may come from friction, compliance, sensor noise, actuator delay, lighting, surface geometry, or unmodeled contacts.


The practical design rule is to name the validity envelope. If a simulator claim depends on rigid objects, fixed lighting, perfect calibration, or zero network delay, those assumptions belong next to the metric. Hardware trials then test the exact assumptions most likely to break.


**CALLOUT:** Mechanism


The mechanism is model mismatch management. Domain randomization widens simulated variation, system identification narrows the model around measured hardware, and residual logging records where neither strategy explained the rollout.


## Worked Example


Code Fragment 1.4.1 compares the same grasp claim in simulation and hardware. The point is not that one number is better, but that both rows share the same task, action, metric, and failure label.


```text
# Compare simulation and hardware using the same task fields.
# The gap column makes model mismatch explicit instead of hiding it in prose.
sim_trial = {"surface": "rubber_mat", "success": 0.92, "failure": "none"}
real_trial = {"surface": "rubber_mat", "success": 0.74, "failure": "slip"}

def compare_trials(sim_trial: dict[str, object], real_trial: dict[str, object]) -> dict[str, object]:
    gap = sim_trial["success"] - real_trial["success"]
    return {
        "task": "top_grasp_cup",
        "action": "cartesian_grasp_pose",
        "sim_success": sim_trial["success"],
        "real_success": real_trial["success"],
        "sim_real_gap": round(gap, 2),
        "real_failure": real_trial["failure"],
    }

evidence = compare_trials(sim_trial, real_trial)
print(evidence)
```


**CODE OUTPUT:** {'task': 'top_grasp_cup', 'action': 'cartesian_grasp_pose', 'sim_success': 0.92, 'real_success': 0.74, 'sim_real_gap': 0.18, 'real_failure': 'slip'}


**CODE CAPTION:** Code Fragment 1.4.1 records the sim-real gap for a top-grasp task using matched fields. The real_failure field makes the 0.18 success gap actionable by pointing to slip rather than leaving the mismatch as an abstract performance drop.


Expected output: the evidence record should include the matched task, the shared action representation, the two success rates, the gap, and the physical failure label.


**CALLOUT:** Library Shortcut: MuJoCo, Isaac Lab, And Real Logs


MuJoCo and Isaac Lab make repeated simulated perturbations cheap, while ROS 2 and robot data tools keep hardware logs tied to timestamps, frames, and actuator commands. The shortcut is not skipping validation. It is using standard simulators and logging stacks so the same task contract survives the move from replayable worlds to accountable hardware.


## Practical Recipe


- State the simulator assumptions: contact model, friction range, sensor noise, actuation delay, and reset distribution.


- Choose one hardware-facing metric that uses the same task definition as simulation.


- Run simulation sweeps to isolate likely failure causes before risking hardware.


- Run a small hardware panel that targets those causes, not a disconnected demo set.


- Report the sim-real gap with matched seeds, object sets, controller settings, and failure labels where possible.


**CALLOUT:** Common Failure Mode


The common mistake is treating a simulator as either proof or decoration. It is neither. It is an instrument for controlled claims, and every claim needs a stated validity envelope.


**CALLOUT:** Practical Example: Slippery Cup Transfer


A manipulator policy may reach 95 percent success in simulation when friction is sampled from a narrow range. On hardware, glossy cups slip during lift. The fix is not merely more real trials; first widen the simulated friction and compliance range, then run a hardware panel that measures slip, lift height, grip force, and recovery action under the same grasp task.


**CALLOUT:** Fun Note


Simulation is a generous rehearsal room. Hardware is the stage manager who notices every loose cable.


**CALLOUT:** Research Frontier


One frontier is automatic sim-real diagnosis: using real rollout logs to infer which simulated parameters, assets, or sensors need adjustment. The scientific challenge is causal, not cosmetic. A better-looking scene is not enough unless it predicts the same failures that matter on the robot.


**CALLOUT:** Self Check


Name one claim that simulation can test better than hardware, and one claim that hardware must test. What field would you log to connect the two?


## Builder's Deep Dive


A simulator supports counterfactual teaching because it can replay the same initial state while changing one variable. Hardware supports accountability because it contains nuisance factors the modeler did not enumerate. A strong validation plan uses simulation to propose a causal story and hardware to test whether that story survives contact with the physical system.


The disciplined habit is to avoid saying "validated in simulation" as if it were one category. Specify validated for what: perception robustness, controller stability, contact recovery, safety margin, or task sequencing. Each claim has a different sim-real risk.


Practical Tool Choices For Section 1.4

Tool or LibraryRole in This TopicBuilder AdviceMuJoCosupports fast contact experiments with explicit bodies, joints, actuators, constraints, and sensor tracesUse it when the suspected gap is contact, actuation, or controller stability.Isaac Labsupports large-scale randomized simulation for manipulation and locomotion policiesUse it when robustness must be measured across many appearances, object placements, or physical parameters.ROS 2 bag filespreserve hardware evidence as timestamped sensor, command, transform, and diagnostic streamsUse logs as the bridge between simulation hypotheses and hardware failures.


## Implementation Recipe


Build sim-real comparison around failure labels, not only success rates. A simulator gap becomes actionable when the same action fails in hardware with a named cause such as slip, missed contact, delayed braking, bad calibration, object pose drift, or sensor saturation.


- Keep the task, object set, controller, and success criterion identical across simulation and hardware.

- Log the simulator assumptions next to the metric: friction range, mass, compliance, latency, lighting, and reset distribution.

- Replay hardware failures in simulation by changing one assumption at a time.

- Report the smallest simulated perturbation that reproduces the hardware failure label.

- Do not change the policy and the simulator at the same time during gap diagnosis.


```text
# Decompose a sim-real gap by matching hardware failures to simulator perturbations.
hardware_failures = [
    {"trial": 4, "failure": "slip", "surface": "matte_cup", "real_success": False},
    {"trial": 9, "failure": "late_stop", "surface": "glossy_cup", "real_success": False},
]
sim_sweeps = [
    {"perturbation": "lower_friction", "reproduces": {"slip"}},
    {"perturbation": "add_120ms_actuator_delay", "reproduces": {"late_stop"}},
    {"perturbation": "increase_camera_noise", "reproduces": set()},
]

def matched_gap_explanations(failures, sweeps):
    labels = {failure["failure"] for failure in failures}
    return [
        {
            "failure_label": label,
            "candidate_sim_perturbations": [
                sweep["perturbation"] for sweep in sweeps if label in sweep["reproduces"]
            ],
        }
        for label in sorted(labels)
    ]

print(matched_gap_explanations(hardware_failures, sim_sweeps))
```


**CODE CAPTION:** Code Fragment 1.4.2 turns a sim-real gap into matched hardware failure labels and simulator perturbations.


**CALLOUT:** Teaching Move


Ask students to defend one claim that simulation can support and one claim that hardware must support. Then require the same task contract for both. The exercise prevents simulation from becoming either a toy world or a rhetorical checkbox.


## Failure Analysis Pattern


When sim and hardware disagree, classify the gap before changing the policy. Common causes are visual mismatch, contact mismatch, actuator delay, calibration drift, reset mismatch, and logging mismatch. Then rerun the smallest simulated perturbation that reproduces the hardware failure label.


**CALLOUT:** Key Takeaway


Simulation and hardware answer different evidence questions. The practical skill is preserving one task contract while using simulation for controlled causes and hardware for final accountability.


**CALLOUT:** Exercise 1.4.1


Design a method-matched experiment for Physical vs. simulated embodiment. Specify the environment, observation schema, action interface, metric, and one perturbation that targets the section's core assumption.


### What's Next?


Section 1.5 explains why the 2023 to 2026 Physical AI framing changed the field's center of gravity.


## Bibliography & Further Reading


### Foundational References For This Section


Sutton, R. S., and Barto, A. G.. "Reinforcement Learning: An Introduction." (2018). http://incompleteideas.net/book/the-book-2nd.html


The durable reference for interaction, return, policies, and episode-level evaluation.


Brohan, A. et al.. "RT-1: Robotics Transformer for real-world control at scale." (2022). https://arxiv.org/abs/2212.06817


A useful anchor for large-scale robot policy learning from real interaction data.


Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." (2023). https://arxiv.org/abs/2310.08864


Shows why cross-embodiment data matters for the Physical AI framing.
