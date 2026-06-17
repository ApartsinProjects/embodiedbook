# Building Embodied AI

## From Perception to Autonomous Action

### Master Book Plan, Concept, and Table of Contents (2026 Edition)

> This is the comprehensive, modernized plan. The original 48-chapter outline (archived at `archive/building_embodied_ai_book_plan_v1_ARCHIVED.md`) had the right skeleton but predated the 2023-2026 shift to vision-language-action models, GPU-parallel simulation, diffusion/flow-matching policies, generative world models, humanoid learning, and the LeRobot-centric open toolchain. This version folds all of that in, deepens the theory, and adds a concrete tools-and-recipes spine plus full course-design material.

---

## 1. Title and Positioning

**Building Embodied AI: From Perception to Autonomous Action**

Recommended subtitle alternatives, in priority order:

1. *From Perception to Autonomous Action* (broad, default)
2. *Robots, World Models, and Vision-Language-Action Systems*
3. *Foundations, Foundation Models, and Physical Intelligence*

The title deliberately spans classical robotics, reinforcement and imitation learning, simulation, world models, multimodal foundation models, and safe real-world deployment. It is positioned as the fifth volume in the series (after Language AI, Vision AI, Temporal AI, Scalable AI) and as the bridge volume into Physical AI.

---

## 2. What This Edition Adds Over a 2022-Era Book

A textbook written before 2023 cannot teach how embodied systems are actually built today. This edition treats the following as first-class material, each verified against current sources during planning:

- **Vision-Language-Action (VLA) models** as a category: RT-1/RT-2, RT-X, Octo, OpenVLA, RDT-1B, π0 / π0-FAST / π0.5, GR00T N1.5, Gemini Robotics, SmolVLA, TRI Large Behavior Models.
- **Action representation theory**: discrete action tokenization vs. action chunking (ACT) vs. diffusion and flow-matching action heads; the FAST frequency-space tokenizer.
- **Dual-system (System 1 / System 2) architectures** for humanoids and reasoning-plus-control.
- **Cross-embodiment learning and robot data scaling laws** (Open X-Embodiment, empirical imitation-learning scaling laws).
- **The modern open toolchain**: LeRobot, Gymnasium (not Gym), Isaac Lab (not Isaac Gym), MuJoCo + MJX + MuJoCo Warp, the Newton physics engine, Genesis, ManiSkill3, robosuite/RoboCasa, BEHAVIOR-1K/OmniGibson.
- **Diffusion for planning and control**: Diffuser, Decision Diffuser, Diffusion Policy.
- **Generative and predictive world models**: DreamerV3, TD-MPC2, IRIS; Genie 1-3, Sora-as-simulator, NVIDIA Cosmos, GameNGen/Oasis; the JEPA family up to V-JEPA 2.
- **Neural scene representations for robotics**: NeRF and 3D Gaussian Splatting for SLAM, real2sim2real, and synthetic data.
- **Low-cost teleoperation and data collection**: ALOHA / ALOHA 2 / Mobile ALOHA, GELLO, UMI, Open-TeleVision.
- **Humanoids and whole-body control**: platforms (Unitree G1/H1, Figure, Optimus, 1X, electric Atlas, Apptronik) and methods (HumanPlus, OmniH2O/HOVER, massively parallel locomotion, parkour, RMA).
- **Reproducible evaluation**: SIMPLER for sim evaluation of real-world policies; benchmark hygiene at scale.

Every named model, dataset, and tool in the book ships with a "verify before citing" pass using the `bibtest` workflow, because several of the most important artifacts (Helix, Gemini Robotics 1.5, the newest world models) have only vendor releases rather than peer-reviewed papers.

---

## 3. Book Vision and Core Thesis

> An embodied AI system is one whose intelligence is expressed through a closed loop of perception and action inside a world, physical or simulated.

The book develops a single recurring loop and returns to it in every chapter:

```text
sense -> represent -> predict -> decide -> act -> observe consequences -> learn
```

It starts from first principles (agents, environments, coordinate frames, control) and builds without gaps to the frontier (robot foundation models, generative world models, safe deployment). The unifying claim is that modern embodied intelligence is not "deep learning replacing robotics" but the disciplined integration of learned components with geometry, dynamics, planning, and safety constraints.

---

## 4. Design Principles

1. **Interaction first.** Prediction is in service of action and its consequences.
2. **One loop, many instantiations.** Every method is located on the sense-predict-act loop.
3. **Simulation before reality, but reality is the judge.** Train in sim; evaluate for transfer; treat the reality gap as a measurable quantity.
4. **Learning plus structure.** Geometry, kinematics, controllers, maps, and constraints are scaffolding that learning fills in, not obstacles to remove.
5. **Self-contained.** Every prerequisite (linear algebra, probability, deep learning, RL, control) has a refresher in-line or in an appendix, so a motivated reader needs no second book open.
6. **Buildable.** Every major concept has a runnable artifact and names the specific, currently-maintained library to use, with version and recency caveats.
7. **Honest about the frontier.** Where results are vendor-reported or unreplicated, the text says so.

---

## 5. Target Audience and Prerequisites

**Audience:** advanced undergraduates, graduate students, and working engineers/researchers entering embodied AI from machine learning, computer vision, NLP, RL, or classical robotics; instructors designing a one- or two-semester course.

**Assumed:** Python; basic linear algebra, probability, and machine learning; exposure to neural networks (CNNs, transformers).

**Introduced from scratch (no prior assumed):** coordinate frames and rigid transforms, kinematics and dynamics, feedback control, sensors and state estimation, reinforcement learning, imitation learning, simulation, world models, and safety.

**Refreshers provided** (Appendices): linear algebra and 3D geometry; probability and estimation; PyTorch and JAX essentials; the math of optimization used in RL and control.

---

## 6. Pedagogical Apparatus (every chapter)

Each chapter follows a fixed, didactic rhythm so the book works as a course text:

1. **Motivation** in plain language, anchored to a real system.
2. **Intuition** with a diagram of where the topic sits on the perception-action loop.
3. **Theory**: formal definitions, derivations, and the key equations, at graduate depth.
4. **Worked example**: a minimal, fully-explained instance.
5. **Practical recipe**: the concrete "how you actually do this in 2026" with named tools, default hyperparameters, and known pitfalls.
6. **Code demo**: a runnable notebook/script using a current library.
7. **Common mistakes and failure modes**, including how they show up on real hardware.
8. **Exercises** (conceptual + derivation).
9. **Programming assignment** (graded, with a rubric).
10. **Project / research extension** and **further reading** (curated, dated, with arXiv ids).

Recurring sidebars: **Theory Deep-Dive**, **Recipe Card** (one-page actionable checklist), **Tooling Note** (library + version + maintenance status), **Reality Gap** (what breaks moving sim to real), and **Frontier Watch** (unreplicated/vendor results, flagged).

---

## 7. Software, Tools, and Compute (taught throughout, cataloged in Appendix C)

The book commits to a current, maintained stack and is explicit about what is deprecated.

### Core numerical / DL
Python 3.11+, NumPy, SciPy, Matplotlib, OpenCV, PyTorch, JAX (for parallel/differentiable sim), Hugging Face Transformers and Diffusers, scikit-learn.

### Simulation and physics
- **MuJoCo** (DeepMind, Apache-2.0, actively released) and **MuJoCo MJX** (JAX, GPU/differentiable) with **MuJoCo Playground**; **MuJoCo Warp**.
- **NVIDIA Isaac Sim + Isaac Lab** (the supported successor to the deprecated Isaac Gym / IsaacGymEnvs / OmniIsaacGymEnvs / Orbit).
- **Newton** physics engine (NVIDIA + DeepMind + Disney, Linux Foundation, on Warp) as the emerging GPU-differentiable standard.
- **Genesis** (generative multi-physics, fast-growing) as a forward-looking option.
- **Drake** (model-based design, MPC, verification), **SAPIEN** (under ManiSkill), **ROS 2 + modern Gazebo** (systems integration; note Gazebo Classic reached end of life).
- Legacy/teaching-only: **PyBullet** (covered for accessibility, flagged as maintenance-mode).

### Benchmarks / task suites
ManiSkill3, robosuite + RoboCasa, robomimic, LIBERO, Meta-World, CALVIN, RLBench, BEHAVIOR-1K / OmniGibson, Habitat 3.0, AI2-THOR / ProcTHOR.

### RL / IL libraries
Gymnasium and PettingZoo (Farama); Stable-Baselines3, CleanRL, Tianshou; the Isaac Lab-native GPU libraries SKRL, rl_games, RSL-RL; offline-RL tooling.

### Robot learning, data, and teleoperation
**LeRobot** (Hugging Face) as the unifying hub (LeRobotDataset format; ACT, Diffusion Policy, VQ-BeT, π0, GR00T N1.5, SmolVLA; low-cost hardware support); **openpi** (π0/π0.5); OpenVLA and Octo codebases; teleoperation hardware ALOHA 2, Mobile ALOHA, GELLO, UMI, Open-TeleVision.

### Perception / multimodal
Detectron2 / Ultralytics YOLO, Segment Anything-family, CLIP / SigLIP / DINOv2, depth-estimation models, 3D Gaussian Splatting toolkits, open VLMs.

### Compute guidance
A standing **Compute Recipe** appendix: what runs on a single 6-8 GB consumer GPU (toy MuJoCo, small SB3/CleanRL, LeRobot ACT fine-tunes), what needs a workstation or one cloud GPU (PPO at scale in Isaac Lab, diffusion policies, OpenVLA fine-tuning), and what needs multi-GPU/cloud (VLA pretraining, world-model training). Cloud-offload patterns and cost framing are given explicitly.

---

## 8. Full Table of Contents

The book is organized into 12 parts and a front-matter "how to use this book" plus appendices. Chapter count grows from 48 to 60 to absorb the modern material without overloading individual chapters.

---

### Front Matter

- **How to Use This Book** — reading paths (undergraduate, graduate, research, self-study); notation; the perception-action loop as a map of the book.
- **0. Setting Up Your Embodied AI Lab** — environment setup (Python, CUDA, the encoding/locale gotchas on Windows), installing the simulator stack, a 30-minute "hello, embodiment" that runs an agent in MuJoCo and in Gymnasium and renders it.

---

# Part I — Foundations of Embodied AI

## Chapter 1 — From Static AI to Embodied AI
1.1 Static prediction vs. embodied interaction
1.2 Why intelligence needs a world; the perception-action loop
1.3 Agents, environments, observations, actions, rewards, constraints
1.4 Physical vs. simulated embodiment
1.5 The "Physical AI" framing and why 2023-2026 changed the field
1.6 Examples: vacuum, drone, autonomous vehicle, manipulator, humanoid, game agent
1.7 Why embodied AI is hard (partial observability, long horizons, safety, data cost)
1.8 Map of the book
- **Demo:** a minimal grid-world agent. **Assignment:** 2D grid agent with rewards.

## Chapter 2 — The Agent-Environment Interface
2.1 Agents and environments formally
2.2 State, observation, hidden variables, partial observability
2.3 Action types: discrete, continuous, symbolic, motor-level, chunked
2.4 Rewards, goals, costs, constraints
2.5 Episodes, horizons, trajectories, discounting
2.6 Markov decision processes; Bellman equations
2.7 Partially observable MDPs; belief states
2.8 Why embodiment is usually partially observable
- **Demo:** a custom Gymnasium environment. **Assignment:** an embodied task env with obs/action/reward.

## Chapter 3 — Embodied System Architectures
3.1 The canonical stack: sense, perceive, estimate, predict, plan, control, act
3.2 Classical modular robotics pipeline
3.3 End-to-end learned policy pipeline
3.4 Hybrid and hierarchical architectures
3.5 Reactive vs. deliberative agents
3.6 Dual-system (System 1 / System 2) designs and where they come from
3.7 Where LLMs, VLMs, and VLAs sit in the stack
3.8 Failure modes of each architecture
- **Demo:** build a modular perception-planner-controller agent. **Assignment:** compare rule-based vs. learned agent in one env.

---

# Part II — Mathematical, Robotics, and Control Foundations

## Chapter 4 — Spatial Representation and Coordinate Frames
4.1 Why space is the substrate of embodiment
4.2 Points, vectors, poses, frames
4.3 Rotations: matrices, Euler angles, axis-angle, quaternions; pitfalls
4.4 Rigid transforms, homogeneous coordinates, SE(3)
4.5 2D and 3D transformations; transform trees (tf in ROS)
4.6 Camera, body, and world frames
4.7 Common frame mistakes and how to debug them
- **Demo:** transform points across frames; quaternion vs. Euler. **Assignment:** track a moving robot's pose.

## Chapter 5 — Kinematics and Robot Motion
5.1 Position, velocity, acceleration; twists
5.2 Holonomic vs. non-holonomic motion
5.3 Differential-drive and car-like robots
5.4 Robot arms, joints, the kinematic chain
5.5 Forward kinematics
5.6 Inverse kinematics: analytic, numerical (Jacobian), and learned
5.7 Jacobians, singularities, manipulability
5.8 Motion constraints
- **Demo:** differential-drive sim; arm FK/IK. **Assignment:** motion model + trajectory visualization.

## Chapter 6 — Dynamics and Simulation Math
6.1 From kinematics to dynamics: forces, torques, inertia
6.2 Rigid-body dynamics; the manipulator equation
6.3 Contact, friction, and why contact-rich sim is hard
6.4 Numerical integration and stability
6.5 Differentiable physics: what it buys you
6.6 Why GPU-parallel simulation changed robot learning
- **Demo:** simulate a pendulum/cart-pole from the equations, then in MuJoCo. **Assignment:** reproduce a contact behavior and diagnose instability.

## Chapter 7 — Control for AI Practitioners
7.1 Open-loop vs. closed-loop control
7.2 Feedback, error, stability, overshoot, oscillation
7.3 PID control, intuition and tuning
7.4 State-space control, LQR
7.5 Model predictive control (MPC) as receding-horizon optimization
7.6 Operational-space and whole-body control (preview for humanoids)
7.7 Controllers vs. policies; when learning helps and when it makes control unsafe
- **Demo:** PID then LQR on cart-pole; a short MPC loop. **Assignment:** tune and break a controller; analyze failure.

## Chapter 8 — Sensors, Perception Hardware, and State Estimation
8.1 What sensors provide and what they cost
8.2 Cameras, depth (stereo/structured light/ToF), LiDAR
8.3 IMU, wheel odometry, joint encoders, proprioception
8.4 Tactile and force/torque sensing (GelSight, DIGIT) — preview
8.5 Sensor noise and uncertainty models
8.6 Bayesian filtering: Kalman, EKF, particle filters
8.7 Sensor fusion intuition and practice
8.8 Perception as an imperfect window into the world
- **Demo:** add noise to sensors; implement a Kalman filter. **Assignment:** fuse two noisy position estimates.

---

# Part III — Simulation, Tooling, and the Modern Stack

## Chapter 9 — Why Simulation Is Central
9.1 Why real-world learning is slow, costly, and risky
9.2 Simulation as data generator, testbed, and curriculum
9.3 Fidelity: physical, visual, behavioral
9.4 The reality gap as a measurable quantity
9.5 The landscape of benchmark environments
- **Demo:** toy env vs. physics env side by side. **Assignment:** specify what a simulator must model for a chosen task.

## Chapter 10 — Environments with Gymnasium (and PettingZoo)
10.1 Gym is dead; Gymnasium is the standard
10.2 Observation and action spaces
10.3 Reward design and termination
10.4 Vectorized environments; wrappers
10.5 Rendering, logging, and debugging
10.6 Evaluation protocol and seeding
10.7 PettingZoo for multi-agent
- **Demo:** build a navigation env. **Assignment:** a task with sparse and dense reward variants.

## Chapter 11 — Physics Simulators: MuJoCo, MJX, Isaac Lab, Genesis
11.1 What physics simulators model (bodies, joints, contacts, friction)
11.2 MuJoCo and the MJCF/URDF model formats
11.3 MuJoCo MJX and MuJoCo Warp: massively parallel and differentiable
11.4 NVIDIA Isaac Sim + Isaac Lab; the Isaac Gym -> Isaac Lab migration
11.5 The Newton physics engine and OpenUSD scene interchange
11.6 Genesis and generative multi-physics
11.7 Drake, SAPIEN, ROS 2 + Gazebo; where each fits
11.8 Choosing a simulator: a decision guide and recency table
- **Demo:** the same reaching task in MuJoCo and Isaac Lab. **Assignment:** load a URDF and script a behavior; benchmark parallel envs.

## Chapter 12 — Benchmarks and Task Suites
12.1 Why standardized benchmarks matter
12.2 Manipulation: ManiSkill3, robosuite, RoboCasa, robomimic, RLBench
12.3 Lifelong and language-conditioned: LIBERO, CALVIN, Meta-World
12.4 Household and long-horizon: BEHAVIOR-1K / OmniGibson
12.5 Navigation and social: Habitat 3.0, AI2-THOR / ProcTHOR
12.6 Reading a leaderboard without fooling yourself
- **Demo:** run a baseline on LIBERO via LeRobot. **Assignment:** profile two benchmarks and report what each actually measures.

## Chapter 13 — Domain Randomization and Synthetic Data
13.1 Why synthetic variation matters
13.2 Visual, physics, sensor, and task randomization
13.3 Curriculum and automatic randomization
13.4 Photoreal rendering and tiled cameras
13.5 real2sim2real and asset/scene reconstruction
13.6 Randomization vs. realism; measuring transfer readiness
- **Demo:** train perception under randomized lighting/textures. **Assignment:** robustness under shifting simulator conditions.

---

# Part IV — Reinforcement Learning for Embodied Agents

## Chapter 14 — Reinforcement Learning Refresher
14.1 Learning from interaction; return and discounting
14.2 Policies and value functions
14.3 Exploration vs. exploitation
14.4 Model-free vs. model-based; on- vs. off-policy
14.5 Why RL is hard in embodied systems (sample cost, reward, safety)
- **Demo:** train a simple agent with Stable-Baselines3. **Assignment:** random vs. rule-based vs. RL.

## Chapter 15 — Policy Gradient Methods and PPO
15.1 Direct policy optimization; stochastic policies
15.2 The policy gradient theorem; REINFORCE
15.3 Actor-critic and advantage estimation (GAE)
15.4 Trust regions; TRPO to PPO
15.5 PPO in practice: the implementation details that matter
15.6 Reward shaping and its hazards
- **Demo:** PPO on a continuous-control task (CleanRL). **Assignment:** measure how shaping changes learning.

## Chapter 16 — Value-Based and Off-Policy Methods
16.1 Q-learning; deep Q-networks
16.2 Replay buffers and target networks
16.3 Continuous control: DDPG, TD3, SAC
16.4 Maximum-entropy RL
16.5 Sample efficiency and off-policy failure modes
- **Demo:** SAC on a manipulation task. **Assignment:** PPO vs. SAC on the same task.

## Chapter 17 — Massively Parallel and GPU RL
17.1 Why thousands of parallel envs changed the field
17.2 Learning to walk in minutes: the parallel-RL recipe
17.3 Isaac Lab with SKRL / rl_games / RSL-RL
17.4 MJX/Brax-training and JAX RL
17.5 Teacher-student and privileged-information distillation
17.6 Throughput, wall-clock, and cost engineering
- **Demo:** parallel PPO locomotion in Isaac Lab or MJX. **Assignment:** scale env count and report the throughput/quality curve.

## Chapter 18 — Reward Design and Goal Specification
18.1 Why rewards are dangerous
18.2 Sparse vs. dense; shaping done right
18.3 Goal-conditioned policies; hindsight experience replay
18.4 Reward hacking, with case studies
18.5 Human preferences and learned reward models (RLHF for control)
18.6 Safety-aware and constrained rewards
- **Demo:** three reward functions for one task. **Assignment:** find and fix a reward-hacking behavior.

## Chapter 19 — Exploration in Embodied Worlds
19.1 Why embodied exploration is expensive and risky
19.2 Intrinsic motivation, curiosity, count-based and novelty methods
19.3 Safe exploration
19.4 Exploration under partial observability
- **Demo:** add a curiosity reward. **Assignment:** external-only vs. curiosity-augmented reward.

## Chapter 20 — Sim-to-Real Transfer (RL focus)
20.1 The reality gap revisited
20.2 What transfers and what does not
20.3 Domain randomization, system identification, adaptation (RMA)
20.4 Fine-tuning on hardware; safe real-world RL
20.5 Measuring transfer performance
- **Demo:** train randomized, test shifted. **Assignment:** propose and justify a sim-to-real protocol.

---

# Part V — Learning from Demonstration and Robot Data

## Chapter 21 — Imitation Learning
21.1 Why learning from demonstration matters for robots
21.2 Behavior cloning; the distribution-shift problem
21.3 DAgger and dataset aggregation
21.4 Inverse reinforcement learning
21.5 Sources of demonstrations: humans, planners, foundation models
- **Demo:** behavior cloning from expert trajectories. **Assignment:** expert vs. cloned vs. RL-refined.

## Chapter 22 — Action Chunking and Diffusion Policies
22.1 Why single-step prediction fails on real manipulation
22.2 ACT (Action Chunking Transformer) and the cVAE formulation
22.3 ALOHA, ALOHA 2, and Mobile ALOHA
22.4 Diffusion Policy: action generation by denoising
22.5 Flow matching for actions
22.6 VQ-BeT and discretized behavior modeling
22.7 Choosing an action representation: a decision guide
- **Demo:** train ACT and a Diffusion Policy in LeRobot. **Assignment:** compare chunk sizes and action heads on one task.

## Chapter 23 — Teleoperation and Data Collection
23.1 Why data is the bottleneck
23.2 Leader-follower teleoperation (ALOHA, GELLO)
23.3 Handheld and in-the-wild collection (UMI)
23.4 Immersive/VR teleoperation (Open-TeleVision)
23.5 Data quality, diversity, and labeling
23.6 The LeRobotDataset format and pipeline
- **Demo:** record and replay a demonstration set in LeRobot. **Assignment:** design a data-collection protocol for a chosen skill.

## Chapter 24 — Robot Datasets and Data Scaling Laws
24.1 The major datasets: Open X-Embodiment, DROID, BridgeData V2, RH20T, RoboMIND, AgiBot World
24.2 Dataset structure, embodiment metadata, and licensing
24.3 Cross-embodiment pooling
24.4 Empirical data scaling laws in imitation learning
24.5 Curating and mixing data
- **Demo:** load and inspect an Open X-Embodiment shard. **Assignment:** analyze how dataset size/diversity affects a cloned policy.

## Chapter 25 — Offline RL and Dataset-Based Robot Learning
25.1 Learning without online interaction
25.2 Distribution shift and extrapolation error
25.3 Conservative methods (CQL, IQL) and their intuition
25.4 Offline-to-online fine-tuning
25.5 Evaluating offline policies honestly
- **Demo:** train a policy from a fixed dataset (robomimic). **Assignment:** dataset quality vs. policy performance.

## Chapter 26 — Skills, Hierarchy, and Task Decomposition
26.1 What a skill is; low- vs. high-level actions
26.2 The options framework
26.3 Skill discovery and hierarchical RL
26.4 Language as a high-level controller
26.5 Skill libraries for embodied agents
- **Demo:** an agent with reusable nav + manipulation skills. **Assignment:** decompose a household task into skills.

---

# Part VI — Embodied Perception

## Chapter 27 — Visual Perception for Action
27.1 Seeing to classify vs. seeing to act
27.2 Detection, segmentation, and the Segment Anything family
27.3 Depth estimation and metric scale
27.4 Optical flow and motion cues
27.5 Affordances and graspable regions
27.6 Active and embodied perception
27.7 When perception failures become action failures
- **Demo:** detect objects and estimate navigable regions. **Assignment:** a perception module for object search.

## Chapter 28 — 3D Perception and Neural Scene Representations
28.1 Why 3D matters for manipulation and navigation
28.2 Point clouds and depth maps
28.3 3D detection and scene reconstruction
28.4 Occupancy grids and voxel maps
28.5 NeRF: implicit radiance fields
28.6 3D Gaussian Splatting: explicit, editable, real-time
28.7 Scene representations for robotics: SLAM, real2sim, manipulation
- **Demo:** depth to point cloud; a small Gaussian-splat reconstruction. **Assignment:** build a 3D occupancy map.

## Chapter 29 — Localization and Mapping (SLAM)
29.1 Where am I and what does the world look like
29.2 Odometry and dead reckoning
29.3 Localization (Monte Carlo / particle filters)
29.4 Mapping and occupancy grids
29.5 SLAM: graph-based and visual SLAM
29.6 Neural and Gaussian-splat SLAM
29.7 Map uncertainty
- **Demo:** 2D occupancy-grid mapping. **Assignment:** noisy odometry corrected by observations.

## Chapter 30 — Navigation and Path Planning
30.1 Navigation as embodied intelligence
30.2 Graph search: BFS, Dijkstra, A*
30.3 Sampling-based planning: RRT, RRT*, PRM
30.4 Local planning and obstacle avoidance (DWA, potential fields)
30.5 Learned navigation policies
30.6 Language- and image-goal navigation
- **Demo:** A* on an occupancy grid; an RRT. **Assignment:** classical vs. learned navigation.

---

# Part VII — Language, Vision, and Action

## Chapter 31 — Language-Guided Embodied Agents
31.1 Why language matters in embodied AI
31.2 Instructions, goals, constraints
31.3 Grounding language in perception; referring expressions
31.4 Object- and region-centric grounding
31.5 Task planning from language; ambiguity and clarification
31.6 Human-agent interaction
- **Demo:** natural-language commands to symbolic goals. **Assignment:** a language-guided navigation agent.

## Chapter 32 — Vision-Language Models for Embodiment
32.1 From image-text models to embodied perception
32.2 CLIP, SigLIP, DINOv2 representations
32.3 Vision-language encoders and open-vocabulary detection
32.4 Visual question answering and scene description in environments
32.5 Multimodal memory
32.6 Limits of static VLMs in dynamic worlds
- **Demo:** rank target objects with a VLM. **Assignment:** visual-language similarity for object search.

## Chapter 33 — LLMs as Planners and Controllers
33.1 What LLMs can and cannot do in embodied tasks
33.2 SayCan: affordance-grounded planning
33.3 Code as Policies: LLMs that write robot code
33.4 VoxPoser: composing 3D value maps
33.5 ReKep: relational keypoint constraints
33.6 Tool use, action APIs, plan verification, replanning
33.7 Memory, state tracking, and hallucination in physical tasks
33.8 Safe LLM-agent interfaces
- **Demo:** connect an LLM planner to a simulated action API. **Assignment:** decompose household instructions into executable skills.

## Chapter 34 — Vision-Language-Action Models
34.1 From VLMs to VLAs: the core idea
34.2 The lineage: RT-1, RT-2, RT-X / Open X-Embodiment
34.3 Open generalist policies: Octo, OpenVLA
34.4 Diffusion/flow VLAs: RDT-1B, π0, π0-FAST, π0.5
34.5 Action tokenization vs. continuous heads; the FAST tokenizer
34.6 Co-training with web data for semantic generalization
34.7 Prompting and conditioning embodied policies
34.8 Evaluating VLA behavior; limitations and open problems
- **Demo:** fine-tune a small open VLA (SmolVLA/OpenVLA) in LeRobot. **Assignment:** design a dataset schema for VLA training.

## Chapter 35 — Robot Foundation Models and Cross-Embodiment Learning
35.1 Why foundation models matter for robotics
35.2 Cross-embodiment training and transfer
35.3 Dual-system architectures: GR00T N1.5, Helix, Gemini Robotics (with Frontier-Watch caveats)
35.4 Large behavior models and rigorous evaluation
35.5 Adapting to new robots; prompting and conditioning
35.6 Data scale, compute, and the open-vs-closed divide
35.7 Limitations and open questions
- **Demo:** a small cross-task policy interface. **Assignment:** a critical analysis of robot-foundation-model evaluation.

---

# Part VIII — World Models and Model-Based Embodied AI

## Chapter 36 — Predicting the Future
36.1 Why agents need to predict
36.2 Forward/dynamics models; state vs. observation prediction
36.3 Error accumulation and horizon
36.4 Uncertainty in prediction
36.5 Planning with predicted futures
- **Demo:** train a next-state predictor. **Assignment:** planning with true vs. learned dynamics.

## Chapter 37 — Model-Based RL and MPC
37.1 Model-free vs. model-based trade-offs
37.2 Learning dynamics models; ensembles and uncertainty
37.3 Planning with learned models; MPC and CEM/MPPI
37.4 Imagination rollouts
37.5 Sample-efficiency advantages and failure modes
- **Demo:** short-horizon planning with a learned model. **Assignment:** implement MPC in a toy environment.

## Chapter 38 — Latent World Models
38.1 Why predict in latent space
38.2 Autoencoders and recurrent state-space models (RSSM)
38.3 Dreamer to DreamerV3
38.4 Transformer world models (IRIS)
38.5 TD-MPC2: latent MPC at scale
38.6 World models for visual control
- **Demo:** train a small latent dynamics model. **Assignment:** a visual prediction model for an embodied task.

## Chapter 39 — Generative and Video World Models
39.1 Generative models as learned simulators
39.2 Genie 1-3: interactive, playable world models
39.3 Video generation as world simulation: Sora and successors
39.4 NVIDIA Cosmos: world foundation models for physical AI
39.5 GameNGen and Oasis: neural game engines
39.6 Using generative world models for data and evaluation (e.g., humanoid pipelines)
39.7 Evaluating consistency, controllability, and horizon
- **Demo:** roll out a generative world model and probe its consistency. **Assignment:** assess a video world model as a data source.

## Chapter 40 — Predictive Representations and Self-Supervised World Models
40.1 Predict in representation space, not pixels: the JEPA idea
40.2 I-JEPA and V-JEPA
40.3 V-JEPA 2 and action-conditioned latent planning
40.4 Self-supervised pretraining for control
- **Demo:** use a pretrained predictive encoder for a control task. **Assignment:** compare pixel vs. latent prediction.

## Chapter 41 — Diffusion and Generative Planning
41.1 Diffusion models as planners
41.2 Diffuser and Decision Diffuser
41.3 Generative trajectory planning and scoring
41.4 Generating scenes and synthetic experience
41.5 Risks of generated experience
- **Demo:** generate and score candidate trajectories. **Assignment:** direct policy vs. trajectory generation.

---

# Part IX — Manipulation, Locomotion, and Embodied Skills

## Chapter 42 — Robotic Manipulation
42.1 What manipulation is; reaching and pushing
42.2 Pick-and-place pipelines
42.3 Contact-rich interaction
42.4 Perception for manipulation
42.5 Learning manipulation policies (IL, RL, VLA)
42.6 Failure detection and recovery
- **Demo:** a reaching/grasping task in ManiSkill or robosuite. **Assignment:** a pick-and-place pipeline.

## Chapter 43 — Grasping and Dexterous Manipulation
43.1 Grasp synthesis: analytic and learned (Dex-Net lineage)
43.2 Parallel-jaw vs. multi-finger hands
43.3 In-hand manipulation and reorientation
43.4 Dexterous RL with demonstrations
43.5 Sim-to-real for dexterity
- **Demo:** a grasp-quality model or a dexterous reorientation task. **Assignment:** evaluate grasp success across objects.

## Chapter 44 — Tactile and Visuo-Tactile Learning
44.1 Why touch matters for contact-rich tasks
44.2 Vision-based tactile sensors (GelSight, DIGIT)
44.3 Simulating touch (e.g., tactile sim in Isaac)
44.4 Visuo-tactile pretraining and policies
44.5 Combining vision and touch
- **Demo:** a tactile-conditioned grasp policy in sim. **Assignment:** analyze the value of touch on a contact task.

## Chapter 45 — Locomotion and Mobility
45.1 Wheeled, legged, and hybrid robots
45.2 Balance, stability, and gait
45.3 Learning locomotion with massively parallel RL
45.4 Terrain adaptation, parkour, and rapid motor adaptation
45.5 Energy efficiency; sim-to-real and safety in locomotion
- **Demo:** a learned locomotion controller in Isaac Lab/MJX. **Assignment:** robustness to terrain changes.

## Chapter 46 — Humanoid Robots and Whole-Body Control
46.1 Why humanoids became the focus (data, morphology, hardware cost)
46.2 Platforms: Unitree G1/H1, Figure, Optimus, 1X, electric Atlas, Apptronik
46.3 Whole-body and operational-space control
46.4 Learning from humans: HumanPlus, OmniH2O/HOVER, motion retargeting
46.5 Teleoperation for humanoids
46.6 Dual-system humanoid foundation models (tie-back to Ch. 35)
46.7 Safety for human-scale robots
- **Demo:** a whole-body control or retargeting example in sim. **Assignment:** a teleoperation-to-imitation pipeline design.

## Chapter 47 — Drones and Aerial Embodied AI
47.1 Why aerial agents are special
47.2 Flight dynamics intuition
47.3 Perception, navigation, and obstacle avoidance
47.4 Coverage and inspection; multi-drone coordination
47.5 Safety, regulation, and simulation for aerial agents
- **Demo:** 2D/3D drone navigation. **Assignment:** an inspection mission planner.

## Chapter 48 — Autonomous Driving as Embodied AI
48.1 Driving as perception, prediction, planning, control
48.2 Sensors and sensor fusion in AVs
48.3 Detection, lane and behavior prediction
48.4 Route and local planning
48.5 End-to-end and world-model driving
48.6 Scenario testing and safety cases
- **Demo:** a toy lane-following controller. **Assignment:** evaluate failure cases in driving scenarios.

---

# Part X — Multi-Agent and Human-Centered Embodiment

## Chapter 49 — Multi-Agent Embodied AI
49.1 One agent vs. many
49.2 Cooperation, competition, communication
49.3 Shared perception and task allocation
49.4 Multi-agent RL (with PettingZoo)
49.5 Swarms and emergent behavior; evaluating teams
- **Demo:** multi-agent grid-world coordination. **Assignment:** agents that divide a search region.

## Chapter 50 — Human-Robot Interaction
50.1 Robots among humans
50.2 Natural-language interaction and social navigation
50.3 Intent recognition and trust calibration
50.4 Explainable robot behavior
50.5 Human feedback and shared autonomy
50.6 Ethical concerns
- **Demo:** a human-in-the-loop correction interface. **Assignment:** an interaction protocol for a household assistant.

## Chapter 51 — Open-World and Lifelong Embodiment
51.1 Closed- vs. open-world tasks
51.2 Novel objects and instructions; changing environments
51.3 Long-horizon tasks
51.4 Continual learning and catastrophic forgetting
51.5 Memory and experience replay; open-world evaluation
- **Demo:** add unknown objects to an existing task. **Assignment:** evaluate an agent under environment change.

---

# Part XI — Evaluation, Safety, Robustness, and Deployment

## Chapter 52 — Evaluating Embodied Systems
52.1 Why accuracy is not enough
52.2 Success rate, path efficiency, time and energy cost
52.3 Safety violations and constraint satisfaction
52.4 Robustness and generalization metrics
52.5 Reproducible evaluation: SIMPLER and sim-as-proxy
52.6 Real-world evaluation hygiene; benchmark design
- **Demo:** an evaluation dashboard for navigation/manipulation. **Assignment:** define a metric suite for a complete task.

## Chapter 53 — Robustness and Uncertainty
53.1 What goes wrong: sensor noise, distribution shift
53.2 Model uncertainty and calibration
53.3 Out-of-distribution detection
53.4 Runtime monitoring and fail-safe behavior
- **Demo:** uncertainty-aware action selection. **Assignment:** a fallback policy for uncertain situations.

## Chapter 54 — Safety in Embodied AI
54.1 Why embodied safety is different (physical harm)
54.2 Constraint violations and safe exploration
54.3 Control barrier functions and Hamilton-Jacobi reachability
54.4 Shielded policies and safety filters
54.5 Human override and safety testing
54.6 Deployment approval and safety cases
- **Demo:** a safety shield that blocks unsafe actions. **Assignment:** a safety case for a mobile or human-scale robot.

## Chapter 55 — Deployment Architecture
55.1 From notebook to robot
55.2 Real-time inference and control rates
55.3 Edge vs. cloud-robot computation; asynchronous inference
55.4 Logging, monitoring, model updates
55.5 Failure recovery, security, maintenance
- **Demo:** package an embodied agent as modular real-time services. **Assignment:** design an end-to-end deployment architecture.

---

# Part XII — Frontiers, Capstones, and Course Design

## Chapter 56 — Embodied Agents with Memory
56.1 Why memory matters; short- vs. long-term
56.2 Spatial, episodic, and semantic memory
56.3 Memory retrieval for planning
56.4 Memory errors
- **Demo:** map-based memory for object search. **Assignment:** memoryless vs. memory-based agents.

## Chapter 57 — Continual and Lifelong Learning
57.1 Learning after deployment
57.2 Catastrophic forgetting and mitigation
57.3 Online adaptation; human correction as data
57.4 Safe continual learning; evaluation over time
- **Demo:** fine-tune on new tasks while preserving old skills. **Assignment:** design a lifelong-learning benchmark.

## Chapter 58 — Frontier and Open Problems
58.1 Scaling laws and data engines for robots
58.2 Generalist vs. specialist policies
58.3 World models in the robot loop
58.4 The open-vs-closed model divide
58.5 What is still unsolved (long-horizon reasoning, reliability, real-world RL)
- **Frontier Watch:** a curated, dated list of claims to revisit.

## Chapter 59 — Capstone Projects
A bank of full project specs, each with problem definition, simulator/dataset, baselines, required implementation, evaluation metrics, report structure, and extensions:
59.1 Object search in a simulated home
59.2 Language-guided navigation with replanning
59.3 Vision-based robotic pick-and-place (IL + RL)
59.4 Fine-tune an open VLA on a custom task (LeRobot)
59.5 Learned locomotion with sim-to-real analysis
59.6 World-model-based planning agent
59.7 Safety-shielded embodied agent
59.8 LLM-based household task planner
59.9 Drone inspection planner
59.10 Multi-agent search and rescue
59.11 Open-ended research project

## Chapter 60 — Teaching with This Book
60.1 One-semester graduate course (14 weeks)
60.2 One-semester advanced undergraduate course (lighter theory, more labs)
60.3 Two-semester sequence
60.4 Research-seminar track
60.5 Lab infrastructure and compute budgeting for instructors
60.6 Assessment, rubrics, and academic-integrity notes for code assignments

---

### Appendices

- **A. Linear Algebra and 3D Geometry Refresher**
- **B. Probability, Estimation, and Optimization Refresher**
- **C. The Embodied AI Toolbox** — install guides, version/maintenance status, and decision tables for every library named in the book (simulators, RL/IL libs, LeRobot, datasets), with the deprecation map (Gym->Gymnasium, Isaac Gym->Isaac Lab, Gazebo Classic EOL).
- **D. PyTorch and JAX for Embodied AI**
- **E. Compute Recipes** — what runs on consumer GPU vs. workstation vs. cloud; cloud-offload patterns; cost framing.
- **F. Datasets and Benchmarks Catalog** — scale, license, format, and access for each.
- **G. Reproducibility and Experiment Hygiene** — seeding, logging, evaluation protocols, reporting.
- **H. Notation and Glossary.**
- **I. Citing the Frontier** — how the book verifies vendor vs. peer-reviewed claims; the standing "verify before citing" list.

---

## 9. Course Mappings

### 9.1 One-Semester Graduate Course (14 weeks)

| Week | Topic | Chapters |
|---|---|---|
| 1 | Foundations and the perception-action loop | 1-3 |
| 2 | Spatial math, kinematics, dynamics | 4-6 |
| 3 | Control and sensing/estimation | 7-8 |
| 4 | Simulation and the modern stack | 9-11 |
| 5 | Benchmarks and domain randomization | 12-13 |
| 6 | RL foundations and PPO | 14-16 |
| 7 | Parallel RL, reward, exploration, sim-to-real | 17-20 |
| 8 | Imitation, action chunking, diffusion policies | 21-22 |
| 9 | Data, teleoperation, scaling laws, offline RL | 23-26 |
| 10 | Embodied perception, 3D, SLAM, navigation | 27-30 |
| 11 | Language, VLMs, LLM planners, VLAs | 31-35 |
| 12 | World models (latent, generative, JEPA, diffusion) | 36-41 |
| 13 | Manipulation, locomotion, humanoids, domains | 42-48 |
| 14 | Multi-agent, HRI, evaluation, safety, deployment + projects | 49-55, 59 |

### 9.2 Advanced Undergraduate Variant
Compress Parts II, VIII, and the foundation-model theory; expand labs in Parts III, IV, V; require one capstone from Chapter 59.

### 9.3 Two-Semester Sequence
Semester A: Parts I-VI (foundations, simulation, RL, imitation/data, perception). Semester B: Parts VII-XII (language/VLA, world models, skills/humanoids, multi-agent, safety/deployment, research project).

### 9.4 Research-Seminar Track
Chapters 34-41, 46, 52, 58 with paper readings keyed to the Frontier-Watch lists.

---

## 10. Distinctive Features

1. Treats embodied AI as a unifying field, not only robotics.
2. Integrates classical robotics, control, and estimation with modern deep learning and foundation models in one framework.
3. Current to 2026: VLAs, generative world models, humanoids, the LeRobot toolchain, GPU-parallel simulation.
4. Deep theory and runnable practice in every chapter, with Recipe Cards and Tooling Notes.
5. Self-contained, with refreshers and appendices so no second book is required.
6. Honest about the frontier: vendor vs. peer-reviewed claims are marked, and citations are verified.
7. Course-ready: full week-by-week mappings, rubrics, compute budgeting, and a capstone bank.

---

## 11. Series Position and Companion Volumes

Fifth volume in the series: Language AI, Vision AI, Temporal AI, Scalable AI, then **Embodied AI**. Natural companions afterward: Trustworthy AI, Scientific AI, Reasoning AI, Edge AI, Multimodal AI.

---

## 12. Core Message

> Intelligence becomes embodied when an agent must act, observe the consequences, and adapt inside a changing world. This book teaches both the enduring theory of that loop and the specific, current tools for building systems that close it.
