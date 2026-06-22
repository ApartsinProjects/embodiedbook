# Manual Reading Batch

Sections 9-12 of 379



========================================================================================


## [009] part-1-foundations-of-embodied-ai\module-02-the-agent-environment-interface\section-2.1.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 2: The Agent-Environment Interface


# Section 2.1: Agents and environments formally


"The environment is the part of the experiment that gets a vote after every action."


**FIGURE:** Figure 2.1A: Section 2.1: Agents and environments formally becomes easier to reason about when the reader can see the perception, decision, action, and feedback loop as one physical situation.


A Boundary-Conscious Embodied AI Agent


**CALLOUT:** Big Picture


Agents and environments formally gives the perception-action loop a contract. The agent is the decision-making process, the environment is everything that produces observations and consequences, and the interface is the boundary where evidence, action, reward, and timing pass.


**CALLOUT:** Reader Pathway


Use this section to make the agent-environment boundary operational: identify what reset returns, what step consumes, what step returns, who owns termination, and which diagnostic fields make a rollout reproducible.


Concept map for Section 2.1
A local diagram showing how transition functions connect actions to next observations.


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


**FIGURE:** Figure 2.1. Environment dynamics and transition functions is easiest to reason about as a closed-loop evidence, decision, consequence pattern: transition functions connect actions to next observations.


## What This Section Develops


This section turns the agent-environment loop into a precise object you can specify, implement, test, and log. The point is not to admire a loop diagram. The point is to know exactly what happens when a robot receives a sensor packet, chooses an action, waits for the world to respond, and records evidence about the result.


The distinction matters because many embodied failures are interface failures. A policy may be competent, but the environment wrapper may hide time-limit truncation. A simulator may expose privileged state that the real robot never observes. A logger may record reward but omit the action clipping that changed the actual command.


**CALLOUT:** The Interface Is The Experiment


An embodied experiment is only as clear as its transition record: observation, action, reward or score, termination, truncation, timing, and diagnostic info. If any field is vague, later results become hard to interpret.


## Theory


At time $t$, an agent receives an observation $o_t$, chooses an action $a_t$, and receives a consequence that usually includes a new observation $o_{t+1}$, a reward or score $r_{t+1}$, and episode status. The environment owns the transition dynamics. The agent owns the decision rule. The evaluator owns the claim about whether behavior was good.


For a fully specified single-agent environment, the minimal contract is close to the Gymnasium pattern: reset starts an episode and returns an initial observation plus metadata; step(action) advances the world and returns observation, reward, terminated, truncated, and info. Terminated means the task reached a natural end. Truncated means an external limit, such as a time limit, stopped the episode.


For multi-agent settings, the contract also needs turn order or simultaneous actions. PettingZoo makes that distinction explicit through sequential and parallel APIs. This matters for embodied systems with people, other robots, traffic participants, or adversarial agents.


**CALLOUT:** Mechanism


The mechanism is a typed transition boundary. A useful environment does not merely run physics or replay data. It standardizes reset, step, action validation, observation structure, episode endings, random seeds, and diagnostic info so that closed-loop behavior can be reproduced.


## Worked Example


Code Fragment 2.1.1 builds a tiny environment contract without any reinforcement learning library. The example is deliberately small so that every returned field is visible.


```text
# Section 2.1: runnable checkpoint for Environment dynamics and transition functions.
# Keep the output small so the evidence record can be inspected directly.
from dataclasses import dataclass

@dataclass
class Transition:
    observation: dict
    action: str
    reward: float
    terminated: bool
    truncated: bool
    info: dict

def step(position, action, time_step):
    delta = 1 if action == "right" else -1
    next_position = position + delta
    reached_goal = next_position >= 3
    timed_out = time_step >= 4
    reward = 1.0 if reached_goal else -0.01
    return Transition(
        observation={"position": next_position},
        action=action,
        reward=reward,
        terminated=reached_goal,
        truncated=timed_out and not reached_goal,
        info={"latency_ms": 12, "action_clipped": False},
    )

print(step(position=2, action="right", time_step=3))
```


**CODE CAPTION:** Code Fragment 2.1.1 defines an explicit transition record with observation, action, reward, termination, truncation, and diagnostic info.


**CALLOUT:** Library Shortcut


The 28-line teaching loop becomes roughly 6 lines of user-facing interaction with Gymnasium once an environment class exists: make the environment, call reset, sample or choose actions, call step, and inspect terminated, truncated, and info. Gymnasium handles spaces, wrappers, seeding, reset semantics, and time-limit conventions internally. The hand-built version remains useful because it exposes exactly what the library standardizes.


## Practical Recipe


- Name the agent process and the environment process separately.


- Specify reset, observation, action, reward, termination, truncation, and info fields before training.


- Track latency for observation capture, policy inference, transport, and action execution.


- Log the full transition tuple before aggregating success rate or return.


- Run a no-op or safe-action baseline to verify that the environment boundary behaves as expected.


**CALLOUT:** Failure Mode


A benchmark score is weak evidence when reset semantics, time limits, action clipping, or termination causes are hidden. A policy can look successful because the wrapper ended difficult episodes early or because the evaluator compared runs from different environment versions.


**CALLOUT:** Practical Example


A warehouse robotics team used a custom simulator and a real cart robot. By writing the interface contract first, they discovered that the simulator returned object pose as privileged ground truth while the real robot returned delayed camera detections. The fix was not a larger model. The fix was to expose state-estimate confidence and sensor delay in the transition info record.


**CALLOUT:** Memorable Shortcut


If the environment wrapper cannot explain why an episode ended, it is not a benchmark yet. It is a suspense story with a CSV file.


**CALLOUT:** Research Frontier


Modern robot learning systems increasingly train from large replay buffers, simulated rollouts, and real-world logs through shared environment-like interfaces. The frontier is making those interfaces rich enough for robot data, multi-camera observations, action chunks, safety monitors, and replayable failure analysis.


**CALLOUT:** Mini Lab


Wrap Code Fragment 2.1.1 in a loop of five actions. Record every transition as JSON, then compute success rate twice: once counting truncation as failure and once reporting truncation separately.


**CALLOUT:** Self Check


Can you name which process owns the observation, which process owns the action choice, which process declares episode ending, and which field records timing evidence?


## Builder's Deep Dive


The formal interface is useful only if it prevents silent changes in the experiment. A policy result should say which environment version produced it, how reset sampled initial state, which action space was accepted, whether the command was clipped, why the episode ended, and whether the ending was a task termination or an external truncation.


The most common mistake is to treat the environment as background code. In embodied AI the environment is part of the scientific claim. If a wrapper changes observations, action limits, time limits, rewards, or diagnostic info, it changes the meaning of the result.


Practical Tool Choices For Section 2.1

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumstandardizes reset, step, spaces, termination, truncation, wrappers, and seedingUse it to make single-agent environment contracts inspectable before training.PettingZooseparates sequential and parallel multi-agent interaction patternsUse it when other agents, people, vehicles, or robots change the transition dynamics.ROS 2carries observations, commands, clocks, transforms, and diagnostics across real robot processesUse it to connect the formal environment contract to real-time deployed components.


## Implementation Recipe


Before training, run an interface audit on one transition. The audit should fail if a required field is missing, if termination and truncation are confused, or if action clipping is hidden.


- Declare the reset output and step output as named fields.

- Check that observation and action types match the declared spaces.

- Log termination and truncation as different fields.

- Put latency, clipping, safety gate status, and wrapper version in info.

- Save the first transition from every experiment run as a smoke-test artifact.


```text
# Audit one transition record before trusting an environment result.
transition = {
    "observation": {"position": 3},
    "action": "right",
    "reward": 1.0,
    "terminated": True,
    "truncated": False,
    "info": {"latency_ms": 12, "action_clipped": False, "wrapper_version": "v2"},
}

def audit_transition(row: dict[str, object]) -> list[str]:
    required = {"observation", "action", "reward", "terminated", "truncated", "info"}
    problems = [f"missing {key}" for key in sorted(required - row.keys())]
    if row.get("terminated") and row.get("truncated"):
        problems.append("terminated and truncated cannot both explain the same ending")
    info = row.get("info", {})
    for key in ["latency_ms", "action_clipped", "wrapper_version"]:
        if key not in info:
            problems.append(f"info missing {key}")
    return problems

print(audit_transition(transition))
```


**CODE CAPTION:** Code Fragment 2.1.2 audits a transition record for required fields, episode-ending semantics, and diagnostic info.


**CALLOUT:** Teaching Move


Ask students to intentionally remove one transition field and explain which future claim becomes impossible to verify. This makes the interface contract concrete.


## Failure Analysis Pattern


When an agent-environment experiment fails, first inspect the transition boundary. Check reset distribution, action clipping, wrapper order, time-limit handling, reward emission, and diagnostic info before changing the policy.


**CALLOUT:** Key Takeaway


A formal agent-environment interface is the smallest unit of closed-loop evidence. If the transition record is clear, later learning, simulation, logging, and deployment decisions have a stable foundation.


**CALLOUT:** Exercise 2.1.1


Write a transition schema for a door-opening robot. Include one field that belongs to the evaluator but is not visible to the agent.


### What's Next?


Section 2.2 distinguishes hidden state from the observations the agent actually receives.


## Bibliography & Further Reading


### Foundational References For This Section


Bellman, R.. "A Markovian Decision Process." (1957). https://doi.org/10.1515/9781400835386-007


The mathematical origin of the state, action, transition, and reward framing.


Kaelbling, L. P., Littman, M. L., and Cassandra, A. R.. "Planning and acting in partially observable stochastic domains." (1998). https://www.sciencedirect.com/science/article/pii/S000437029800023X


A foundational POMDP reference for belief-state reasoning under partial observability.


Farama Foundation. "Gymnasium Documentation." (2024). https://gymnasium.farama.org/


The maintained reference for reset, step, spaces, termination, truncation, wrappers, and reproducible environments.


========================================================================================


## [010] part-1-foundations-of-embodied-ai\module-02-the-agent-environment-interface\section-2.2.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 2: The Agent-Environment Interface


# Section 2.2: State, observation, hidden variables, partial observability


"My camera saw the block. My gripper discovered the friction. My log finally admitted both were incomplete."


**FIGURE:** Figure 2.2A: Section 2.2: State, observation, hidden variables, partial observability is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation.


A Probabilistic Robot Assistant


**CALLOUT:** Big Picture


State, observation, hidden variables, partial observability separates what exists in the world from what the agent senses. Embodied agents rarely receive complete state. They receive noisy, delayed, partial observations and must infer the variables that matter for action.


**CALLOUT:** Reader Pathway


Use this section to separate world state from agent evidence: list what exists, what is sensed, what is estimated, what is delayed, and what only the evaluator is allowed to know.


Concept map for Section 2.2
A local diagram showing how state lives in the world while observation is the agent's limited evidence.


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


**FIGURE:** Figure 2.2. State vs. observation is easiest to reason about as a closed-loop evidence, decision, consequence pattern: state lives in the world while observation is the agent's limited evidence.


## What This Section Develops


This section develops the vocabulary needed to debug almost every embodied AI system. A simulator may know the true pose, mass, friction, and contact state of every object. A robot policy may see only pixels, joint encoders, force readings, and a stale command queue. That difference is not a nuisance. It is the problem.


State is the information sufficient to predict future dynamics and reward when paired with an action. Observation is the sensor-facing evidence available to the agent. Hidden variables are state variables that matter but are not directly observed. Partial observability is the normal condition in which the latest observation is not enough.


**CALLOUT:** Observation Is Not State


A camera frame can support useful action, but it is not the full physical situation. A deployable embodied system must decide which hidden variables to estimate, which to perturb in simulation, and which to reserve for evaluation diagnostics.


## Theory


Let $s_t$ be the world state and $o_t$ be the observation emitted by sensors or an environment wrapper. In a fully observable task, $o_t$ contains enough information to act as $s_t$. In embodied AI, that is usually false. Occlusion hides objects, contact reveals only local forces, latency makes images stale, and human intent is not directly measurable.


The agent therefore maintains an estimate $\hat{s}_t$ or a belief over possible states. This estimate may be a Kalman filter state, a particle filter, a learned recurrent hidden state, a transformer memory, or a structured world-model latent. The name matters less than the contract: what uncertainty does it represent, how is it updated, and how does action use it?


**CALLOUT:** Mechanism


Partial observability turns the loop into observe, update belief, choose action, execute, and revise. In simulation, privileged state can be logged for diagnostics while keeping the agent restricted to observations. This separation is essential for honest evaluation.


## Worked Example


Code Fragment 2.2.1 updates a tiny belief state from a partial observation. The hidden variable is slip risk, which the camera cannot directly see.


```text
# Section 2.2: runnable checkpoint for State vs. observation.
# Keep the output small so the evidence record can be inspected directly.
belief = {"block_x": 0.50, "block_visible": True, "slip_risk": 0.20}
observation = {"detected_x": 0.54, "visible": True, "force_spike": False}

if observation["visible"]:
    belief["block_x"] = 0.7 * belief["block_x"] + 0.3 * observation["detected_x"]
else:
    belief["block_visible"] = False

if observation["force_spike"]:
    belief["slip_risk"] += 0.25
else:
    belief["slip_risk"] *= 0.95

print({"estimated_x": round(belief["block_x"], 3), "slip_risk": round(belief["slip_risk"], 3)})
```


**CODE CAPTION:** Code Fragment 2.2.1 updates an estimated block position and hidden slip risk from vision and force observations.


Expected output: an updated position estimate and slip-risk estimate. The example should make clear that vision updates visible pose, while contact evidence updates a hidden physical variable.


**CALLOUT:** Library Shortcut


The 15-line belief update becomes a few estimator or logging components in a real stack. MuJoCo and Isaac Lab can expose privileged simulator state for diagnostics, ROS 2 can publish state estimates as topics, and LeRobot can store synchronized observations and actions for later analysis. The hand-built version is still useful because it states exactly which hidden variable is being tracked.


## Practical Recipe


- List variables needed to predict dynamics, not just variables found in the sensor packet.


- Mark each variable as observed, estimated, delayed, hidden, or evaluator-only.


- Add uncertainty to every estimated variable and log that uncertainty.


- Carry history when the current observation is insufficient.


- Evaluate under occlusion, sensor delay, calibration drift, and contact changes.


**CALLOUT:** Failure Mode


Treating observation as state creates brittle policies. A camera frame may show the gripper and block, but not friction, object mass, motor temperature, cable drag, or a person about to enter the workspace.


**CALLOUT:** Practical Example


A manipulation lab trained a policy on visible object pose and saw strong simulation success. On the real robot, the gripper briefly occluded the object before contact, and the policy moved as if the last visible pose were still certain. Adding a belief state with last-seen pose, elapsed time, and confidence let the controller slow down and reobserve.


**CALLOUT:** Memorable Shortcut


If the agent says it knows the whole state from one RGB image, ask it where the object mass is hiding. The answer is usually "in the failure case."


**CALLOUT:** Research Frontier


Robot foundation models and world models increasingly learn latent state from history rather than a single frame. The open challenge is making learned latent state useful to safety monitors, dashboards, and closed-loop evaluators instead of leaving it as an opaque activation vector.


**CALLOUT:** Mini Lab


Modify Code Fragment 2.2.1 so the object is invisible for three time steps. Log how confidence changes, then decide when the robot should stop and reobserve.


**CALLOUT:** Self Check


For a tabletop robot, can you name three variables that affect future action but are not directly visible in the latest camera image?


## Builder's Deep Dive


State-observation discipline prevents privileged information leakage. In simulation the evaluator may know object mass, contact normal, true pose, and collision margin. The policy should receive only the observation channels that a deployed system can provide. A result that mixes those views may measure access to simulator internals rather than intelligence.


The practical artifact is a variable ledger. Each variable is marked as observed, estimated, delayed, hidden, or evaluator-only. The ledger should also name the sensor or estimator that produces it and the uncertainty attached to it.


Practical Tool Choices For Section 2.2

Tool or LibraryRole in This TopicBuilder AdviceKalman and particle filtersmaintain explicit belief over hidden or noisy state variablesUse them when uncertainty is low-dimensional enough to model and audit directly.Factor graph librariescombine measurements, priors, and constraints into a structured state estimateUse them for localization, mapping, calibration, and multi-sensor fusion problems.MuJoCo, Isaac Lab, and ROS 2 logsseparate privileged simulator state, policy observations, and deployed state-estimate topicsUse them to prove that evaluation state did not leak into policy input.


## Implementation Recipe


Build a leak test before training. The test should compare evaluator state fields with policy observation fields and fail when evaluator-only variables appear in policy input.


- List all variables needed to predict dynamics and reward.

- Mark each variable as observed, estimated, delayed, hidden, or evaluator-only.

- Attach units, uncertainty, and source sensor or estimator.

- Check that evaluator-only variables are absent from policy input.

- Stress the belief with occlusion, delay, calibration drift, and contact changes.


```text
# Build a variable ledger and detect privileged-state leakage.
variables = {
    "true_pose": "evaluator_only",
    "rgb_crop": "observed",
    "last_seen_pose": "estimated",
    "slip_risk": "hidden",
    "contact_force": "observed",
}
policy_input = {"rgb_crop", "last_seen_pose", "true_pose"}

def privileged_leaks(variables: dict[str, str], policy_input: set[str]) -> list[str]:
    return sorted(
        name for name in policy_input
        if variables.get(name) == "evaluator_only"
    )

print(privileged_leaks(variables, policy_input))
```


**CODE CAPTION:** Code Fragment 2.2.2 detects evaluator-only state that has leaked into the policy observation.


**CALLOUT:** Teaching Move


Ask students to mark ten task variables by visibility class. Then remove every evaluator-only variable from the policy input and discuss which estimator or probing action would be needed to replace it.


## Failure Analysis Pattern


When behavior fails under partial observability, classify whether the agent lacked a sensor, lacked history, carried stale belief, underestimated uncertainty, or received leaked training information. Each cause points to a different repair.


**CALLOUT:** Key Takeaway


State is what would make prediction complete. Observation is what the agent receives. Embodied intelligence lives in the gap between them.


**CALLOUT:** Exercise 2.2.1


For a mobile robot in a hallway, classify map location, battery health, pedestrian intent, wheel slip, and camera image as state, observation, hidden variable, or estimate.


### What's Next?


Section 2.3 turns observations into action representations at several levels of abstraction.


## Bibliography & Further Reading


### Foundational References For This Section


Bellman, R.. "A Markovian Decision Process." (1957). https://doi.org/10.1515/9781400835386-007


The mathematical origin of the state, action, transition, and reward framing.


Kaelbling, L. P., Littman, M. L., and Cassandra, A. R.. "Planning and acting in partially observable stochastic domains." (1998). https://www.sciencedirect.com/science/article/pii/S000437029800023X


A foundational POMDP reference for belief-state reasoning under partial observability.


Farama Foundation. "Gymnasium Documentation." (2024). https://gymnasium.farama.org/


The maintained reference for reset, step, spaces, termination, truncation, wrappers, and reproducible environments.


========================================================================================


## [011] part-1-foundations-of-embodied-ai\module-02-the-agent-environment-interface\section-2.3.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 2: The Agent-Environment Interface


# Section 2.3: Action types: discrete, continuous, symbolic, motor-level, chunked


"Choosing an action space is how you tell a robot what kinds of mistakes it is allowed to make."


**FIGURE:** Figure 2.3A: Section 2.3: Action types: discrete, continuous, symbolic, motor-level, chunked becomes easier to reason about when the reader can see the perception, decision, action, and feedback loop as one physical situation.


A Cautious Policy Interface


**CALLOUT:** Big Picture


Action types: discrete, continuous, symbolic, motor-level, chunked define what the agent can actually do. The same task can be framed as choosing a skill, setting a velocity, moving a joint, emitting a language-conditioned action token, or committing to a short action chunk.


**CALLOUT:** Reader Pathway


Use this section to make action representation operational: identify the command units, coordinate frame, update rate, bounds, clipping behavior, controller below the policy, and recovery cost when an action is wrong.


Concept map for Section 2.3
A local diagram showing how action representations trade expressiveness for search, safety, and learnability.


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


**FIGURE:** Figure 2.3. Action types: discrete, continuous, symbolic, motor-level, chunked is easiest to reason about as a closed-loop evidence, decision, consequence pattern: action representations trade expressiveness for search, safety, and learnability.


## What This Section Develops


This section develops a design checklist for action representation. Action spaces are not interchangeable wrappers around a model. They define controllability, safety, latency, data requirements, transfer difficulty, and how quickly an agent can recover from an error.


Discrete actions are easy to enumerate, symbolic actions are useful for planning, continuous actions match motors and physics, motor-level actions expose control detail, and chunked actions reduce inference frequency while increasing commitment. OpenVLA-style systems add another pattern: map image and language context to action tokens or continuous control heads that must still respect robot limits.


**CALLOUT:** Action Space Is Architecture


The action representation decides which layer owns intelligence. A symbolic action delegates execution to skills. A motor command delegates almost nothing. A chunked action delegates timing to the policy for several future steps.


## Theory


Let the action space be $\mathcal{A}$. A discrete $\mathcal{A}$ might contain actions such as open, close, or move-left. A continuous $\mathcal{A}$ might be a vector of joint torques, velocities, or end-effector pose deltas. A symbolic $\mathcal{A}$ might contain calls such as pick(red_block). A chunked $\mathcal{A}$ contains sequences of low-level actions emitted at once.


The right action space depends on embodiment and timing. A high-level action can be easier to learn but hides safety-critical details. A low-level action can be precise but makes long-horizon reasoning harder. A chunked action can smooth robot motion and reduce model calls, but it delays correction if the world changes mid-chunk.


**CALLOUT:** Mechanism


Every action needs units, limits, rate, coordinate frame, validity checks, and execution semantics. A delta pose in the end-effector frame is different from a target pose in the world frame. A gripper command can mean binary open-close, continuous width, or force-controlled closure.


## Worked Example


Code Fragment 2.3.1 compares four action representations for the same tabletop instruction. Notice that each representation shifts responsibility to a different layer of the system.


```text
# Section 2.3: runnable checkpoint for Action types: discrete, continuous, symbolic, motor-level,
# chunked.
# Keep the output small so the evidence record can be inspected directly.
action_spaces = {
    "discrete_skill": ["find_object", "grasp", "place"],
    "symbolic_call": "place(red_block, tray)",
    "continuous_delta": {"dx_m": 0.01, "dy_m": -0.02, "dz_m": 0.00, "grip": 0.7},
    "chunked_delta": [
        {"dx_m": 0.01, "grip": 0.5},
        {"dx_m": 0.01, "grip": 0.7},
        {"dx_m": 0.00, "grip": 0.9},
    ],
}
for name, action in action_spaces.items():
    print(name, action)
```


**CODE CAPTION:** Code Fragment 2.3.1 contrasts skill, symbolic, continuous, and chunked actions for one manipulation task.


**CALLOUT:** Library Shortcut


The 14-line comparison becomes one action-space declaration in Gymnasium, one policy configuration in LeRobot, or one action adapter in an OpenVLA-style inference service. The tools handle validation, normalization, batching, and model I/O. The hand-built version remains useful because it exposes units, frames, limits, and chunk length.


## Practical Recipe


- Start from the actuator, safety monitor, and controller rate, then move upward to skills.


- Choose the coarsest action that still allows timely recovery.


- Record units, bounds, coordinate frame, rate, and clipping behavior.


- Test action latency by injecting delay and measuring recovery.


- Report action validity failures separately from task failures.


**CALLOUT:** Failure Mode


A high-level action such as pick can hide dangerous low-level motion. A motor-level action can be safe but too hard for long-horizon planning. A chunked action can improve smoothness while delaying correction after a slip, occlusion, or human interruption.


**CALLOUT:** Practical Example


A service robot team first used symbolic actions for cleaning tasks, then found that furniture avoidance needed continuous velocity control near chair legs. They kept symbolic planning for task order, continuous control for local motion, and a safety monitor that clipped speed near people.


**CALLOUT:** Memorable Shortcut


An action space is like a steering wheel: too small and you cannot maneuver, too large and the learner spends half the drive discovering the curb.


**CALLOUT:** Research Frontier


Vision-language-action models, action chunking, diffusion policies, and flow-based policies explore different action parameterizations. The practical question is not which representation is most fashionable, but which one meets the embodiment, latency, safety, and recovery requirements.


**CALLOUT:** Mini Lab


Take a simple pick-and-place task and write three action interfaces: symbolic skill, end-effector delta, and chunked delta. For each, define the controller that must sit below it.


**CALLOUT:** Self Check


Can you state your action units, coordinate frame, update rate, action bounds, and clipping behavior without inspecting the policy code?


## Builder's Deep Dive


Action representation is an architectural boundary. A symbolic skill shifts burden to a planner and skill library. An end-effector delta shifts burden to a controller and calibration stack. A joint command shifts burden to the learned policy and safety monitor. A chunked action shifts burden to prediction because the policy commits before seeing every intermediate consequence.


The practical question is not which action type is most elegant. It is which layer should own timing, contact, validity checking, and recovery for the task at hand.


Practical Tool Choices For Section 2.3

Tool or LibraryRole in This TopicBuilder AdviceGymnasium spacesdeclares discrete, continuous, multi-discrete, dictionary, and bounded action structuresUse spaces as executable documentation for units, bounds, shapes, and clipping behavior.ROS 2 controllersexecute velocity, position, effort, and trajectory commands under real timing constraintsUse them to check whether the action representation can be executed safely at deployment rate.LeRobot and VLA action adaptersnormalize robot actions, action chunks, and policy outputs into deployable commandsUse them when learned action heads must be mapped back to body-specific controllers.


## Implementation Recipe


Audit an action interface before training. The audit should fail if units, frames, rates, bounds, or chunk semantics are absent.


- Name the action level: symbolic, skill, end-effector, joint, torque, velocity, or chunked sequence.

- Record units, coordinate frame, bounds, update rate, controller below the action, and clipping behavior.

- Define what happens when a command is invalid or stale.

- Inject saturation, delay, and mid-chunk observation changes.

- Report action validity failures separately from policy-task failures.


```text
# Audit an action interface for fields needed by a real controller.
action_interface = {
    "level": "end_effector_delta",
    "units": {"dx": "m", "dy": "m", "dz": "m", "yaw": "rad"},
    "frame": "tool0",
    "rate_hz": 20,
    "bounds": {"dx": 0.02, "dy": 0.02, "dz": 0.015, "yaw": 0.10},
    "clip_behavior": "clip_and_log",
    "controller_below": "cartesian_impedance",
}

def missing_action_contract(interface: dict[str, object]) -> list[str]:
    required = ["level", "units", "frame", "rate_hz", "bounds", "clip_behavior", "controller_below"]
    return [key for key in required if key not in interface]

print(missing_action_contract(action_interface))
```


**CODE CAPTION:** Code Fragment 2.3.2 audits whether an action interface contains the fields required for safe execution.


**CALLOUT:** Teaching Move


Ask students to convert the same task into symbolic, end-effector, joint, and chunked action contracts. The comparison makes clear which subsystem owns recovery in each design.


## Failure Analysis Pattern


When an action interface fails, ask whether the command was invalid, clipped, stale, in the wrong frame, too coarse, too low-level, or too committed through chunking. Those are different failures and should not be collapsed into "bad policy."


## Hands-On Lab: Audit An Action Interface

Duration: ~65 minutesDifficulty: Intermediate


### Objective


Build an action-interface contract for one task and test how clipping, delay, or chunking would change recovery.


### What You'll Practice

- Define action units, bounds, frames, and update rate

- Detect missing execution fields before policy training

- Log raw commands, executed commands, and clipping

- Compare correction delay for single-step and chunked actions


### Setup


```text
pip install numpy pandas
```


**CODE CAPTION:** Code Fragment 2.3.L1 installs NumPy and pandas for the section lab trace.


### Steps


#### Step 1: Define the action contract


Write the execution fields before choosing a policy.


```text
contract = {
    "level": "end_effector_delta",
    "units": {"dx": "m", "dy": "m", "dz": "m", "grip": "normalized"},
    "frame": "tool0",
    "rate_hz": 20,
    "bounds": {"dx": 0.02, "dy": 0.02, "dz": 0.02, "grip": [0.0, 1.0]},
    "clip_behavior": "clip_and_log",
}
print(contract)
```


**CODE CAPTION:** Code Fragment 2.3.L1.1 defines an action contract with units, frame, rate, bounds, and clipping behavior.

Hint


If a controller cannot execute the command, the action representation is not finished.


#### Step 2: Check for missing execution fields


Audit the contract before running a policy.


```text
required = {"level", "units", "frame", "rate_hz", "bounds", "clip_behavior"}
print({"missing": sorted(required - contract.keys())})
```


**CODE CAPTION:** Code Fragment 2.3.L1.2 reports whether the action contract is executable enough to test.

Hint


Most action bugs hide in units, frames, bounds, and silent clipping.


#### Step 3: Simulate clipping


Test whether out-of-bounds commands are visible in the log.


```text
command = {"dx": 0.05, "dy": 0.00, "dz": 0.00, "grip": 0.6}
clipped = {**command, "dx": min(command["dx"], contract["bounds"]["dx"])}
print({"raw": command, "executed": clipped, "action_clipped": command != clipped})
```


**CODE CAPTION:** Code Fragment 2.3.L1.3 records the raw command, executed command, and clipping flag.

Hint


A clipped command is not the action the policy selected. Log both.


#### Step 4: Compare commitment length


Record how long the system must continue before it can correct a bad command.


```text
interfaces = [
    {"name": "single_delta", "chunk_len": 1, "rate_hz": 20},
    {"name": "five_step_chunk", "chunk_len": 5, "rate_hz": 20},
]
for item in interfaces:
    item["commitment_ms"] = 1000 * item["chunk_len"] / item["rate_hz"]
print(interfaces)
```


**CODE CAPTION:** Code Fragment 2.3.L1.4 compares correction delay for single-step and chunked actions.

Hint


Chunking can smooth control, but it also delays recovery when observations change.


### Expected Output


The completed lab produces a compact action-interface audit showing whether the contract is complete, whether clipping is visible, and how long a chunked command delays correction.


### Stretch Goals

- Add a joint-level version and compare its bounds against the end-effector version.

- Add a stale-command rule that holds position when the command age exceeds the control budget.


Complete Solution


```text
import pandas as pd

rows = [
    {"check": "contract_complete", "value": not sorted(required - contract.keys())},
    {"check": "clipping_visible", "value": command != clipped},
    {"check": "chunk_commitment_ms", "value": interfaces[1]["commitment_ms"]},
]
print(pd.DataFrame(rows))
```


**CODE CAPTION:** Code Fragment 2.3.L2 creates a compact action-interface audit table.


**CALLOUT:** Key Takeaway


The action space is a design commitment. It decides how intelligence, safety, timing, and recovery are divided across the embodied stack.


**CALLOUT:** Exercise 2.3.1


Design three action spaces for opening a drawer: one symbolic, one end-effector-level, and one joint-level. State one advantage and one risk for each.


### What's Next?


Section 2.4 connects those action choices to reward functions, task specifications, and constraints.


## Bibliography & Further Reading


### Foundational References For This Section


Bellman, R.. "A Markovian Decision Process." (1957). https://doi.org/10.1515/9781400835386-007


The mathematical origin of the state, action, transition, and reward framing.


Kaelbling, L. P., Littman, M. L., and Cassandra, A. R.. "Planning and acting in partially observable stochastic domains." (1998). https://www.sciencedirect.com/science/article/pii/S000437029800023X


A foundational POMDP reference for belief-state reasoning under partial observability.


Farama Foundation. "Gymnasium Documentation." (2024). https://gymnasium.farama.org/


The maintained reference for reset, step, spaces, termination, truncation, wrappers, and reproducible environments.


========================================================================================


## [012] part-1-foundations-of-embodied-ai\module-02-the-agent-environment-interface\section-2.4.html


Skip to main content


Part I: Foundations of Embodied AI

Chapter 2: The Agent-Environment Interface


# Section 2.4: Rewards, goals, costs, constraints


"The robot maximized the reward exactly as written. That was the first problem."


**FIGURE:** Figure 2.4A: Section 2.4: Rewards, goals, costs, constraints is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation.


A Reward Designer With New Gray Hair


**CALLOUT:** Big Picture


Rewards, goals, costs, constraints turn desired behavior into measurable signals. Reward is a scalar training or evaluation signal, a goal is a desired condition, a cost measures undesirable behavior, and a constraint marks behavior that should not be traded away.


**CALLOUT:** Reader Pathway


Use this section to separate four fields that are often collapsed too early: the task goal, the scalar reward, the cost vector, and the hard constraints that should gate or invalidate behavior.


Concept map for Section 2.4
A local diagram showing how reward encourages progress while constraints define unacceptable paths.


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


**FIGURE:** Figure 2.4. Reward functions, task specifications, and constraints is easiest to reason about as a closed-loop evidence, decision, consequence pattern: reward encourages progress while constraints define unacceptable paths.


## What This Section Develops


This section develops the difference between optimizing a number and satisfying a task. Embodied systems operate around people, hardware, and physical limits. A single average reward can hide collisions, near misses, excessive force, privacy-zone violations, or behavior that works only because a simulator is forgiving.


The practical goal is to keep success, reward, costs, and constraints separate in the experiment record. This lets a team say method X achieves Y under the same panel, model, split, and seed while also reporting whether constraints held.


**CALLOUT:** Do Not Hide Safety In A Scalar


Safety constraints should remain visible as constraints. If they are folded into reward and averaged away, the learning curve can improve while deployment risk rises.


## Theory


In reinforcement learning notation, the reward $r_t$ is often a scalar emitted after a transition. In robotics, the actual design space is broader. A goal might be "the cup is upright on the tray." A cost might be time, energy, jerk, or distance to humans. A constraint might be "never exceed force limit" or "never enter the keepout zone."


The important distinction is tradeability. Rewards and costs can be balanced when a tradeoff is acceptable. Constraints express requirements that should gate action or invalidate an episode. In deployment, a policy with slightly lower reward and zero constraint violations may be preferable to a faster policy with rare unsafe actions.


**CALLOUT:** Mechanism


The mechanism is metric factorization. Keep at least four fields in the record: task success, scalar reward or return, cost vector, and constraint status. Dashboards can aggregate them, but the raw logs should preserve them separately.


## Worked Example


Code Fragment 2.4.1 scores two episodes. Both can complete the task, but only one satisfies the safety constraint.


```text
# Section 2.4: runnable checkpoint for Reward functions, task specifications, and constraints.
# Keep the output small so the evidence record can be inspected directly.
def score_episode(success, seconds, collisions, entered_keepout):
    reward = 10.0 * float(success) - 0.05 * seconds - 2.0 * collisions
    costs = {"time_s": seconds, "collisions": collisions}
    constraints_ok = collisions == 0 and not entered_keepout
    return {"success": success, "reward": reward, "costs": costs, "constraints_ok": constraints_ok}

safe = score_episode(success=True, seconds=42, collisions=0, entered_keepout=False)
fast_unsafe = score_episode(success=True, seconds=20, collisions=1, entered_keepout=False)
print(safe)
print(fast_unsafe)
```


**CODE CAPTION:** Code Fragment 2.4.1 separates success, reward, cost fields, and constraint status for two completed episodes.


Expected output: two completed episodes with different safety status. The useful comparison is not only reward; it is reward plus the cost fields and constraint flag.


**CALLOUT:** Library Shortcut


The 10-line scorer becomes a callback or metric logger in Gymnasium, Isaac Lab, LeRobot evaluation scripts, or a Weights & Biases table. The tool handles batching, charts, and comparisons. The designer must still decide which events are rewards, which are costs, and which are non-negotiable constraints.


## Practical Recipe


- Write the goal in task language before writing a scalar reward.


- Separate success, reward, cost vector, and constraint status in logs.


- Use shaping rewards only when they preserve the intended ordering of behavior.


- Add counterexample episodes that target reward hacking.


- Report success with constraint violations, not success alone.


**CALLOUT:** Failure Mode


Average reward can improve while rare unsafe events increase. This is especially dangerous when collisions, force spikes, keepout-zone entries, or operator interventions are small terms inside a single scalar.


**CALLOUT:** Practical Example


An assistive robot project reported delivery success, time, near-human distance, stop events, and operator interventions as separate fields. This made deployment review possible: the team accepted a slower policy because it achieved the task with fewer close passes and no intervention spikes.


**CALLOUT:** Memorable Shortcut


Reward is a suggestion written in math. Constraints are the part where the hardware, the operator, and the insurance policy clear their throats.


**CALLOUT:** Research Frontier


Safe reinforcement learning, preference learning, control barrier functions, and runtime assurance all address failures of simple reward design. Independent closed-loop evaluation remains essential because learned reward models can inherit the blind spots of their data.


**CALLOUT:** Mini Lab


Extend Code Fragment 2.4.1 with an energy cost and a force-limit constraint. Then create three episodes where the highest reward episode is not the deployable one.


**CALLOUT:** Self Check


Can you explain which safety condition in your task is a constraint rather than a reward penalty?


## Builder's Deep Dive


Reward design is safest when it is factorized before it is optimized. A goal describes the intended world condition. A reward provides learning or ranking pressure. A cost measures tradeoffs such as time, energy, jerk, distance to people, or interventions. A constraint names a boundary that should remain visible even when the reward improves.


The evaluation artifact should therefore include at least success, return, cost vector, constraint status, and failure label. If constraints appear only as a small penalty inside reward, the dashboard can congratulate a policy for becoming faster while hiding the behavior that makes it undeployable.


Practical Tool Choices For Section 2.4

Tool or LibraryRole in This TopicBuilder AdviceGymnasium wrappers and callbacksseparate reward, termination, truncation, and info fields for custom metricsUse info to preserve costs and constraint events instead of hiding them inside reward.Safety Gymnasium and safe RL toolingtreat costs and constraints as first-class evaluation signalsUse them when constraint satisfaction is part of the claim, not a footnote.Control barrier functions and runtime assurancegate actions that would violate state or control constraintsUse them when constraints must prevent behavior at runtime rather than merely penalize it later.


## Implementation Recipe


Build a reward audit that can catch reward hacking. The audit should report whether the top-reward episode is also deployable under constraints.


- Write the task goal in ordinary language.

- Define reward, each cost field, and each hard constraint separately.

- Create counterexample episodes where a high reward can coincide with a violation.

- Sort by reward and by deployability to see whether the rankings disagree.

- Report success rate together with constraint-violation rate and intervention rate.


```text
# Check whether the top reward episode is actually deployable.
episodes = [
    {"name": "safe_slow", "reward": 7.9, "success": True, "collisions": 0, "keepout": False},
    {"name": "fast_close_pass", "reward": 8.7, "success": True, "collisions": 0, "keepout": True},
    {"name": "fast_collision", "reward": 8.2, "success": True, "collisions": 1, "keepout": False},
]

def deployability(row: dict[str, object]) -> bool:
    return row["success"] and row["collisions"] == 0 and not row["keepout"]

top_reward = max(episodes, key=lambda row: row["reward"])
deployable = [row for row in episodes if deployability(row)]
print({"top_reward": top_reward["name"], "top_reward_deployable": deployability(top_reward)})
print({"best_deployable": max(deployable, key=lambda row: row["reward"])["name"]})
```


**CODE CAPTION:** Code Fragment 2.4.2 checks whether the highest-reward episode satisfies the hard constraints required for deployment.


**CALLOUT:** Teaching Move


Ask students to design one reward-hacking counterexample before they train a policy. If the metric cannot expose that counterexample, the metric is not ready.


## Failure Analysis Pattern


When a reward design fails, ask whether the goal was underspecified, a shaping term changed the intended ordering, a cost was hidden in the scalar, or a hard constraint was treated as a negotiable penalty. Fix the specification before tuning the learner.


**CALLOUT:** Key Takeaway


Goals say what should happen. Rewards help learning. Costs expose tradeoffs. Constraints protect the boundaries that should not be optimized away.


**CALLOUT:** Exercise 2.4.1


Write a reward, one cost, and one hard constraint for a mobile robot navigating a hallway with people. Explain which dashboard plot should show each field.


### What's Next?


Section 2.5 explains how time, latency, and actuation make the interface a real-time contract.


## Bibliography & Further Reading


### Foundational References For This Section


Bellman, R.. "A Markovian Decision Process." (1957). https://doi.org/10.1515/9781400835386-007


The mathematical origin of the state, action, transition, and reward framing.


Kaelbling, L. P., Littman, M. L., and Cassandra, A. R.. "Planning and acting in partially observable stochastic domains." (1998). https://www.sciencedirect.com/science/article/pii/S000437029800023X


A foundational POMDP reference for belief-state reasoning under partial observability.


Farama Foundation. "Gymnasium Documentation." (2024). https://gymnasium.farama.org/


The maintained reference for reset, step, spaces, termination, truncation, wrappers, and reproducible environments.
