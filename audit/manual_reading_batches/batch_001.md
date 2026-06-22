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


Static prediction vs. embodied interaction becomes useful when it is tied to a closed-loop contract for why closed-loop action changes what intelligence means. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For Static prediction vs. embodied interaction, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 1.1

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumstandardizes episodes so static examples can become stepwise interaction testsUse it when the hand-built contract is clear and the experiment needs repeatable runs.MuJoComakes contact, timing, and recovery visible before hardware is involvedUse it when the hand-built contract is clear and the experiment needs repeatable runs.LeRobotconnects early action-loop ideas to real robot datasets and policiesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Static prediction vs. embodied interaction, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 1.1: Static prediction vs. embodied interaction.
# Use the same schema for the hand-built baseline and the library shortcut.
from dataclasses import dataclass, asdict

@dataclass
class EvidenceRecord:
    section: str
    observation: str
    action: str
    metric: str
    perturbation: str

    def as_row(self) -> dict[str, object]:
        return asdict(self)

record = EvidenceRecord(
    section="1.1",
    observation="camera frame plus last action outcome",
    action="accept, reject, or recover",
    metric="episode success with recovery cost",
    perturbation="late false positive near contact",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 1.1.2 records a construct-matched evidence schema for Static prediction vs. embodied interaction.


**CALLOUT:** Teaching Move


Ask readers to fill the Static prediction vs. embodied interaction evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When Static prediction vs. embodied interaction fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


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


Why intelligence needs a world; the perception-action loop becomes useful when it is tied to a closed-loop contract for why closed-loop action changes what intelligence means. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For Why intelligence needs a world; the perception-action loop, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 1.2

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumstandardizes episodes so static examples can become stepwise interaction testsUse it when the hand-built contract is clear and the experiment needs repeatable runs.MuJoComakes contact, timing, and recovery visible before hardware is involvedUse it when the hand-built contract is clear and the experiment needs repeatable runs.LeRobotconnects early action-loop ideas to real robot datasets and policiesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Why intelligence needs a world; the perception-action loop, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 1.2: Why intelligence needs a world; the perception-action
# loop.
# Use the same schema for the hand-built baseline and the library shortcut.
from dataclasses import dataclass, asdict

@dataclass
class EvidenceRecord:
    section: str
    observation: str
    action: str
    metric: str
    perturbation: str

    def as_row(self) -> dict[str, object]:
        return asdict(self)

record = EvidenceRecord(
    section="1.2",
    observation="egocentric observation and short history",
    action="move, inspect, or pause",
    metric="loop closure rate under perturbation",
    perturbation="sensor dropout during a correction",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 1.2.2 records a construct-matched evidence schema for Why intelligence needs a world; the perception-action loop.


**CALLOUT:** Teaching Move


Ask readers to fill the Why intelligence needs a world; the perception-action loop evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When Why intelligence needs a world; the perception-action loop fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


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


The graduate-level habit is to ask which variable moved. If success rises because the observation included ground-truth pose, that is not the same claim as success rising because the policy learned better visual grounding. Keeping those claims separate prevents leakage and makes construct-matched comparison possible.


Practical Tool Choices For Section 1.3

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumstandardizes episodes so static examples can become stepwise interaction testsUse it when the hand-built contract is clear and the experiment needs repeatable runs.MuJoComakes contact, timing, and recovery visible before hardware is involvedUse it when the hand-built contract is clear and the experiment needs repeatable runs.LeRobotconnects early action-loop ideas to real robot datasets and policiesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Agents, environments, observations, actions, rewards, constraints, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 1.3: Agents, environments, observations, actions, rewards,
# constraints.
# Use the same schema for the hand-built baseline and the library shortcut.
from dataclasses import dataclass, asdict

@dataclass
class EvidenceRecord:
    section: str
    observation: str
    action: str
    metric: str
    perturbation: str

    def as_row(self) -> dict[str, object]:
        return asdict(self)

record = EvidenceRecord(
    section="1.3",
    observation="state estimate from noisy sensors",
    action="discrete option or continuous command",
    metric="reward with constraint violation count",
    perturbation="changed friction or delayed observation",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 1.3.2 records a construct-matched evidence schema for Agents, environments, observations, actions, rewards, constraints.


**CALLOUT:** Teaching Move


Ask readers to fill the Agents, environments, observations, actions, rewards, constraints evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


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


The graduate-level habit is to avoid saying "validated in simulation" as if it were one category. Specify validated for what: perception robustness, controller stability, contact recovery, safety margin, or task sequencing. Each claim has a different sim-real risk.


Practical Tool Choices For Section 1.4

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumstandardizes episodes so static examples can become stepwise interaction testsUse it when the hand-built contract is clear and the experiment needs repeatable runs.MuJoComakes contact, timing, and recovery visible before hardware is involvedUse it when the hand-built contract is clear and the experiment needs repeatable runs.LeRobotconnects early action-loop ideas to real robot datasets and policiesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Physical vs. simulated embodiment, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 1.4: Physical vs. simulated embodiment.
# Use the same schema for the hand-built baseline and the library shortcut.
from dataclasses import dataclass, asdict

@dataclass
class EvidenceRecord:
    section: str
    observation: str
    action: str
    metric: str
    perturbation: str

    def as_row(self) -> dict[str, object]:
        return asdict(self)

record = EvidenceRecord(
    section="1.4",
    observation="simulated state or real sensor packet",
    action="sim action or hardware command",
    metric="sim-real agreement on success and failure labels",
    perturbation="contact parameter mismatch",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 1.4.2 records a construct-matched evidence schema for Physical vs. simulated embodiment.


**CALLOUT:** Teaching Move


Ask readers to fill the Physical vs. simulated embodiment evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


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
