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


Use this section to make agents and environments formally operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


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


Environment dynamics and transition functions becomes useful when it is tied to a closed-loop contract for the contract between policy, world, evaluator, and safety constraints. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For Agents and environments formally, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 2.1

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumkeeps reset, step, termination, truncation, and spaces explicitUse it when the hand-built contract is clear and the experiment needs repeatable runs.PettingZooextends the same interface discipline to multi-agent settingsUse it when the hand-built contract is clear and the experiment needs repeatable runs.ROS 2carries observations, commands, clocks, and diagnostics across real robot processesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Agents and environments formally, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 2.1: Environment dynamics and transition functions.
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
    section="2.1",
    observation="state or observation before an action",
    action="action passed to the transition function",
    metric="prediction error for next state and task progress",
    perturbation="slippery transition or delayed effect",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 2.1.2 records a construct-matched evidence schema for Environment dynamics and transition functions.


**CALLOUT:** Teaching Move


Ask readers to fill the Agents and environments formally evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When Environment dynamics and transition functions fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


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


Use this section to make state, observation, hidden variables, partial observability operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


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


Expected output: the printed trace for State, observation, hidden variables, partial observability should expose the method configuration, the measured evidence field, and the failure label. If one of those fields is missing or unchanged under the perturbation, the example is not yet an evaluation artifact.


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


State vs. observation becomes useful when it is tied to a closed-loop contract for the contract between policy, world, evaluator, and safety constraints. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For State, observation, hidden variables, partial observability, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 2.2

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumkeeps reset, step, termination, truncation, and spaces explicitUse it when the hand-built contract is clear and the experiment needs repeatable runs.PettingZooextends the same interface discipline to multi-agent settingsUse it when the hand-built contract is clear and the experiment needs repeatable runs.ROS 2carries observations, commands, clocks, and diagnostics across real robot processesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For State, observation, hidden variables, partial observability, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 2.2: State vs. observation.
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
    section="2.2",
    observation="noisy observation of a hidden state",
    action="query, move, or wait",
    metric="belief accuracy and task outcome",
    perturbation="occluded object or missing sensor",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 2.2.2 records a construct-matched evidence schema for State vs. observation.


**CALLOUT:** Teaching Move


Ask readers to fill the State, observation, hidden variables, partial observability evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When State vs. observation fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


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


Use this section to make action types: discrete, continuous, symbolic, motor-level, chunked operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


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


Action types: discrete, continuous, symbolic, motor-level, chunked becomes useful when it is tied to a closed-loop contract for the contract between policy, world, evaluator, and safety constraints. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For Action types: discrete, continuous, symbolic, motor-level, chunked, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 2.3

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumkeeps reset, step, termination, truncation, and spaces explicitUse it when the hand-built contract is clear and the experiment needs repeatable runs.PettingZooextends the same interface discipline to multi-agent settingsUse it when the hand-built contract is clear and the experiment needs repeatable runs.ROS 2carries observations, commands, clocks, and diagnostics across real robot processesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Action types: discrete, continuous, symbolic, motor-level, chunked, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 2.3: Action types: discrete, continuous, symbolic,
# motor-level, chunked.
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
    section="2.3",
    observation="policy context and actuator limits",
    action="discrete, continuous, symbolic, motor-level, or chunked command",
    metric="task success plus control smoothness",
    perturbation="actuator saturation or command quantization",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 2.3.2 records a construct-matched evidence schema for Action types: discrete, continuous, symbolic, motor-level, chunked.


**CALLOUT:** Teaching Move


Ask readers to fill the Action types: discrete, continuous, symbolic, motor-level, chunked evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When Action types: discrete, continuous, symbolic, motor-level, chunked fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


## Hands-On Lab: Build a Section Evidence Trace

Duration: ~65 minutesDifficulty: Intermediate


### Objective


Turn Action types: discrete, continuous, symbolic, motor-level, chunked into a small artifact that compares a hand-built baseline with a maintained-tool shortcut under one perturbation.


### What You'll Practice

- Define an observation, action, metric, and perturbation contract

- Build a minimal baseline trace

- Preserve the same schema for the library shortcut

- Write a failure postmortem from the evidence record


### Setup


```text
pip install numpy pandas
```


**CODE CAPTION:** Code Fragment 2.3.L1 installs NumPy and pandas for the section lab trace.


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


**CODE CAPTION:** Code Fragment 2.3.L1.1 records Step 1, Define the contract, and reports that the evidence fields are concrete and ready for comparison.

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


**CODE CAPTION:** Code Fragment 2.3.L1.2 records Step 2, Record the baseline, and reports that the evidence fields are concrete and ready for comparison.

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


**CODE CAPTION:** Code Fragment 2.3.L1.3 records Step 3, Add the shortcut, and reports that the evidence fields are concrete and ready for comparison.

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


**CODE CAPTION:** Code Fragment 2.3.L1.4 records Step 4, Apply one perturbation, and reports that the evidence fields are concrete and ready for comparison.

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


**CODE CAPTION:** Code Fragment 2.3.L2 creates a complete same-schema evidence table for the section lab.


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


Use this section to make rewards, goals, costs, constraints operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign.


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


Expected output: the printed trace for Rewards, goals, costs, constraints should expose the method configuration, the measured evidence field, and the failure label. If one of those fields is missing or unchanged under the perturbation, the example is not yet an evaluation artifact.


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


Reward functions, task specifications, and constraints becomes useful when it is tied to a closed-loop contract for the contract between policy, world, evaluator, and safety constraints. The contract names the observation stream, the action representation, the timing budget, the safety boundary, and the result artifact. That is the bridge between a readable concept and a system a skeptical builder can test.


For Rewards, goals, costs, constraints, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.


Practical Tool Choices For Section 2.4

Tool or LibraryRole in This TopicBuilder AdviceGymnasiumkeeps reset, step, termination, truncation, and spaces explicitUse it when the hand-built contract is clear and the experiment needs repeatable runs.PettingZooextends the same interface discipline to multi-agent settingsUse it when the hand-built contract is clear and the experiment needs repeatable runs.ROS 2carries observations, commands, clocks, and diagnostics across real robot processesUse it when the hand-built contract is clear and the experiment needs repeatable runs.


## Implementation Recipe


For Rewards, goals, costs, constraints, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.


- Write a one-paragraph task contract with observation, action, success, failure, and safety fields.

- Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully.

- Run one deterministic smoke test and one perturbation test before scaling.

- Save one artifact containing configuration, seed, metrics, traces, and failure labels.

- Compare methods only when the same script evaluates the same panel, split, seed set, and metric.


```text
# Build one evidence record for Section 2.4: Reward functions, task specifications, and constraints.
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
    section="2.4",
    observation="task state and safety context",
    action="candidate action with reward and constraint checks",
    metric="return, violations, and recovery cost",
    perturbation="reward hacking opportunity",
)
print(record.as_row())
```


**CODE CAPTION:** Code Fragment 2.4.2 records a construct-matched evidence schema for Reward functions, task specifications, and constraints.


**CALLOUT:** Teaching Move


Ask readers to fill the Rewards, goals, costs, constraints evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.


## Failure Analysis Pattern


When Reward functions, task specifications, and constraints fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.


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
