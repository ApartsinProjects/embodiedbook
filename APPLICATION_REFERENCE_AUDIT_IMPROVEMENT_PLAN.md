# Application Reference Audit And Improvement Plan

Prepared: 2026-06-18

Status: read-only audit. Do not apply yet.

## Executive Judgment

The book is already broad enough to serve as a strong embodied AI reference. It covers foundations, spatial math, kinematics, dynamics, control, simulation, reinforcement learning, imitation learning, robot data, perception, SLAM, navigation, VLA models, world models, manipulation, locomotion, humanoids, drones, autonomous driving, safety, deployment, capstones, and course design.

The gap is not breadth. The gap is application-grade depth for teams that need the book as a main reference while building production or frontier systems. The strongest current areas are robot learning, VLA systems, simulation, humanoids, drones, autonomous driving, and safety foundations. The weakest areas, relative to leading researcher and developer needs, are production fleet robotics, industrial logistics, deployable safety cases, data engineering, simulator-to-hardware lab workflows, and application-specific evaluation panels.

## Priority Scale

- Tier 1: needed for the book to credibly serve as a main reference for leading researchers or developers in that application.
- Tier 2: important depth that would make the book more distinctive and practically useful.
- Tier 3: valuable enrichment, examples, diagrams, labs, and appendices.

## Top 10 Application Audit

### 1. Humanoid Robots And Whole-Body Autonomy

Current coverage:
- Strong and recently improved. Chapters 45 and 46 now cover locomotion, humanoid platforms, whole-body control, teleoperation, safety, advanced humanoid dynamics, contact mechanics, and a Boston Dynamics-style loco-manipulation research track.

Researcher-grade missing material:
- Unified treatment of learned policies with model-based whole-body control.
- More on floating-base dynamics, impacts, compliance, friction cones, spatial momentum, and hierarchical QP/MPC.
- More detailed humanoid data engineering: teleoperation rigs, retargeting pipelines, embodiment normalization, dataset licensing, failure replay.
- More explicit safety cases for human-scale robots outside fenced industrial settings.

Improvement plan:
- Tier 1: add a new section to Chapter 46: `Humanoid Data Engines, Retargeting, And Failure Replay`.
- Tier 1: expand Section 46.8 with hierarchical QP, contact complementarity, friction cones, impact handling, and compliance.
- Tier 2: add a humanoid evaluation panel table covering HumanoidBench, GR00T-style policies, Mobile ALOHA-style teleoperation, Isaac Lab, MuJoCo Playground, Drake, and Pinocchio.
- Tier 3: add a diagram showing the full humanoid loop: task planner, behavior model, centroidal planner, whole-body controller, safety monitor, telemetry, replay.

Key sources:
- NVIDIA GR00T N1: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- HumanoidBench: https://humanoid-bench.github.io/
- MIT Underactuated humanoids: https://underactuated.mit.edu/humanoids.html
- Drake: https://drake.mit.edu/
- Pinocchio: https://stack-of-tasks.github.io/pinocchio/

### 2. Drone And Aerial Robotics

Current coverage:
- Good after the advanced domain layer. Chapter 47 now covers quadrotor dynamics, cascaded control, geometric control, MPC, PX4, ROS 2, MAVLink, VIO, GPS-denied missions, inspection planning, and Remote ID.

Researcher-grade missing material:
- Fixed-wing and hybrid VTOL coverage is thin.
- Fault-tolerant control, system identification, vibration, motor failure, battery aging, payload shift, and wind modeling need deeper treatment.
- Full PX4-to-hardware lab workflow is missing: SITL, HITL, parameter tuning, logs, flight review, companion computer deployment.
- Regulatory engineering should include BVLOS, UTM, SORA, U-space, and cybersecurity.

Improvement plan:
- Tier 1: add a Chapter 47 section: `PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence`.
- Tier 1: expand drone safety section with BVLOS, SORA, U-space, detect-and-avoid, and operational risk cases.
- Tier 2: add an aerial state-estimation comparison: EKF2, OpenVINS, ORB-SLAM3, Kimera, lidar odometry, and degraded visual environments.
- Tier 3: add a multi-drone lab using Crazyswarm2 or PX4 multi-vehicle simulation.

Key sources:
- PX4: https://docs.px4.io/main/en/
- PX4 ROS 2 guide: https://docs.px4.io/main/en/ros2/user_guide
- MAVLink: https://mavlink.io/en/
- OpenVINS: https://docs.openvins.com/
- EuRoC MAV Dataset: https://projects.asl.ethz.ch/datasets/euroc-mav/
- EASA SORA: https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-drones/specific-operations-risk-assessment-sora

### 3. Autonomous Vehicles And Driving Agents

Current coverage:
- Strong and recently improved. Chapter 48 covers vehicle models, route and behavior planning, scenario-based planning, CARLA, CommonRoad, OpenSCENARIO, SOTIF-style reasoning, nuScenes, and Waymo Open Dataset.

Researcher-grade missing material:
- Closed-loop planning evaluation needs more depth: nuPlan, CARLA Leaderboard, Waymo Sim Agents, open-loop vs closed-loop metric failures.
- Standards and assurance coverage should include SAE J3016, UL 4600, UNECE R157, NHTSA VSSA, ISO 26262 boundary, and safety-case defeaters.
- Prediction and interaction should include occupancy flow, multimodal forecasting, game-theoretic planning, learned interaction models, and planning-oriented end-to-end stacks such as UniAD.

Improvement plan:
- Tier 1: add a Chapter 48 section: `Closed-Loop Driving Evaluation And Safety Assurance`.
- Tier 1: expand Section 48.8 with ODD, functional/logical/concrete scenarios, OpenSCENARIO XML and DSL, OpenDRIVE, scenario mining, and coverage arguments.
- Tier 2: add a comparison table for CARLA Leaderboard, nuPlan, Waymo Sim Agents, CommonRoad, nuScenes, and Waymo Open Dataset.
- Tier 3: add a lab that compares open-loop prediction metrics against closed-loop planner outcomes on the same scenario family.

Key sources:
- SAE J3016: https://www.sae.org/standards/j3016_202104-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles
- ISO 21448 SOTIF: https://www.iso.org/standard/77490.html
- UL 4600 overview: https://users.ece.cmu.edu/~koopman/ul4600/index.html
- ASAM OpenSCENARIO XML: https://www.asam.net/standards/detail/openscenario-xml/
- CARLA Leaderboard: https://leaderboard.carla.org/
- nuPlan: https://www.nuplan.org/nuplan

### 4. Mobile Manipulation Robots

Current coverage:
- Covered across Chapters 30, 42, 43, 44, 46, 50, and 59. The book has navigation, manipulation, tactile learning, mobile manipulation adjacency, HRI, and capstones.

Researcher-grade missing material:
- Mobile manipulation should be more explicitly unified: base-arm coordination, navigation plus manipulation coupling, bimanual mobile manipulation, household workflows, deformables, doors, drawers, kitchens, and long-horizon recovery.
- More benchmarks and environments should be surfaced: BEHAVIOR-1K, RoboCasa, Habitat 3.0, ManiSkill mobile manipulation, Mobile ALOHA, DROID.

Improvement plan:
- Tier 1: add a Chapter 42 or new Chapter 42.7 section: `Mobile Manipulation: Base, Arm, Perception, And Recovery`.
- Tier 1: add a worked lab: mobile robot navigates to a cabinet, opens it, grasps an object, carries it, and recovers from a failed grasp.
- Tier 2: add a benchmark table covering BEHAVIOR-1K, RoboCasa, Habitat 3.0, ManiSkill, AI2-THOR, DROID, and Mobile ALOHA.
- Tier 3: add a diagram showing the coupled planner: global route, local navigation, reachability map, grasp planner, whole-body or base-arm controller.

Key sources:
- BEHAVIOR-1K: https://behavior.stanford.edu/index.html
- RoboCasa: https://robocasa.ai/
- Habitat 3.0: https://aihabitat.org/habitat3/
- ManiSkill mobile manipulation: https://maniskill.readthedocs.io/en/v3.0.0b20/tasks/mobile_manipulation/
- Mobile ALOHA: https://arxiv.org/abs/2401.02117
- DROID: https://droid-dataset.github.io/

### 5. Industrial And Logistics Robotics

Current coverage:
- Present but underdeveloped. The book covers deployment architecture, safety, manipulation, navigation, multi-agent systems, and capstones, but it does not yet feel like a main reference for warehouse automation, autonomous forklifts, AMR fleets, WMS/MES integration, or production robotics operations.

Researcher-grade missing material:
- Warehouse workflows: receiving, putaway, replenishment, picking, sortation, packing, dock operations, returns.
- AMRs and autonomous forklifts: pallet handling, docking, charging, traffic, elevators, doors, mixed human zones.
- Fleet orchestration: Open-RMF, multi-vendor interoperability, MassRobotics AMR standard, traffic negotiation, maps, WMS and MES integration.
- Operational metrics: throughput, cycle time, intervention rate, uptime, safety events, congestion, battery, localization drift, labor ergonomics, SLA performance.
- Safety: ISO 3691-4, ANSI/RIA R15.08, risk assessment, specified operating environments.

Improvement plan:
- Tier 1: add a new chapter in Part X or Part XI: `Industrial And Logistics Embodied AI`.
- Tier 1: add labs for AMR dispatch, autonomous forklift pallet movement, fleet traffic, WMS bridge, charging policy, and incident replay.
- Tier 2: add a deployment chapter section on site surveys, commissioning, map lifecycle, calibration drift, recovery procedures, and fleet telemetry.
- Tier 3: add a production dashboard example with robot KPIs and business KPIs computed from one log artifact.

Key sources:
- Amazon Robotics: https://www.aboutamazon.com/news/operations/amazon-robotics-robots-fulfillment-center
- DHL warehouse robotics: https://www.dhl.com/global-en/delivered/innovation/warehouse-robotics-and-automation.html
- MassRobotics AMR standard: https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/
- Open-RMF: https://www.open-rmf.org/
- ISO 3691-4: https://www.iso.org/standard/70660.html
- ANSI/RIA R15.08: https://webstore.ansi.org/standards/ria/ansiriar15082020

### 6. Embodied Foundation Models And VLA Systems

Current coverage:
- Strong. Chapters 31 to 35 cover language-guided agents, VLMs, LLM planners, VLAs, robot foundation models, and cross-embodiment learning. Chapters 21 to 25 cover imitation and robot data.

Researcher-grade missing material:
- Action representation taxonomy needs to be sharper: text-token actions, continuous action heads, action chunking, ACT, diffusion heads, flow matching, hierarchical planners.
- More practical model adaptation: LoRA, quantized serving, policy latency, action normalization, proprioception alignment, camera calibration, time synchronization.
- More explicit comparison among RT-2, RT-X, OpenVLA, Octo, GR00T N1, pi0, SmolVLA, and LeRobot implementations.

Improvement plan:
- Tier 1: add a section to Chapter 34: `Action Representations In VLA Systems`.
- Tier 1: add a section to Chapter 35: `Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models`.
- Tier 2: add an implementation recipe for LeRobot fine-tuning with dataset cards, calibration checks, action normalization, latency budget, and rollback.
- Tier 3: add a matrix comparing VLA architectures, datasets, action heads, policy frequency, robot embodiments, and evaluation limits.

Key sources:
- RT-2: https://arxiv.org/abs/2307.15818
- Open X-Embodiment and RT-X: https://robotics-transformer-x.github.io/
- OpenVLA: https://arxiv.org/abs/2406.09246
- Octo: https://arxiv.org/abs/2405.12213
- LeRobot: https://huggingface.co/docs/lerobot/en/index
- GR00T N1: https://arxiv.org/abs/2503.14734

### 7. Simulation-First Robot Learning

Current coverage:
- Strong in Parts III, IV, VIII, and appendices. The book covers MuJoCo, MJX, Isaac Lab, Genesis, domain randomization, parallel RL, sim-to-real, world models, and compute recipes.

Researcher-grade missing material:
- Need clearer simulator selection criteria by application: humanoid, manipulation, drone, driving, household, industrial fleet.
- Need stronger treatment of what simulation cannot replace: contact mismatch, deformables, visual realism, latency, controller mismatch, human demonstration gaps, actuator and thermal behavior.
- Need a reproducible simulator-to-hardware pattern: scenario panel, randomization budget, model identification, log replay, hardware perturbation, failure triage.

Improvement plan:
- Tier 1: add an appendix or Chapter 11 section: `Simulator Selection And Reality Gap Failure Modes`.
- Tier 1: add a lab template for sim-to-real evidence: one scenario panel, one model ID artifact, one real log, one replayed failure, one mitigation.
- Tier 2: add official 2026 snapshots for Genesis World and NVIDIA Newton as moving-target tools.
- Tier 3: add diagrams showing simulator roles: dynamics engine, renderer, data generator, policy trainer, evaluator, replay environment, and safety sandbox.

Key sources:
- Isaac Lab: https://isaac-sim.github.io/IsaacLab/
- MuJoCo MJX: https://mujoco.readthedocs.io/en/stable/mjx.html
- MuJoCo Playground: https://playground.mujoco.org/
- Genesis World: https://genesis-world.readthedocs.io/
- NVIDIA Newton: https://developer.nvidia.com/newton-physics
- Cosmos world models: https://arxiv.org/abs/2501.03575

### 8. Autonomous Navigation And SLAM Systems

Current coverage:
- Good in Chapters 27 to 30 and the drone additions. The book covers visual perception, 3D perception, SLAM, neural and Gaussian-splat SLAM, navigation, planning, language-goal navigation, and GPS-denied drone contexts.

Researcher-grade missing material:
- Modern SLAM comparison needs more depth: ORB-SLAM3, OpenVINS, Kimera, Kimera-Multi, lidar-inertial odometry, neural implicit mapping, lifelong maps, semantic maps, scene graphs.
- More field failure modes: low texture, smoke, dust, lighting shifts, repetitive structures, motion blur, magnetic disturbance, time sync failures, map drift, relocalization failure.
- More multi-robot SLAM: distributed mapping, map merge, bandwidth limits, time synchronization, shared semantic maps.

Improvement plan:
- Tier 1: add a Chapter 29 section: `Modern SLAM Systems And Failure Modes`.
- Tier 1: add a Chapter 30 section: `Field Navigation Under Degraded Sensing`.
- Tier 2: add a benchmark table for EuRoC, TartanAir, SubT, Habitat, Gibson, AI2-THOR, and real robot logs.
- Tier 3: add a lab that compares ORB-SLAM3 or OpenVINS-style assumptions against a learned or neural mapping approach on a degraded scenario.

Key sources:
- OpenVINS: https://docs.openvins.com/
- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- Kimera: https://github.com/MIT-SPARK/Kimera
- Kimera-Multi: https://github.com/MIT-SPARK/Kimera-Multi
- EuRoC MAV Dataset: https://projects.asl.ethz.ch/datasets/euroc-mav/
- TartanAir: https://theairlab.org/tartanair-dataset/
- DARPA Subterranean Challenge: https://www.darpa.mil/research/challenges/subterranean

### 9. Safety-Critical Embodied AI

Current coverage:
- Solid foundation in Chapters 52 to 55, and reinforced in drones, autonomous driving, humanoids, and deployment. The book covers evaluation, robustness, control barrier functions, Hamilton-Jacobi reachability, safety filters, deployment approval, runtime monitoring, and fail-safe behavior.

Researcher-grade missing material:
- Safety assurance needs a cross-application unifying chapter: safety cases, ODD or operating-domain boundaries, assurance arguments, defeaters, monitor architectures, rollback, incident response, and post-deployment evidence.
- Need stronger standards coverage: SAE J3016, ISO 21448, ISO 26262 boundary, UL 4600, UNECE R157, ISO 3691-4, ANSI/RIA R15.08, aviation Remote ID and SORA.
- Need runtime assurance, CBFs, RSS, fallback controllers, and safety monitors treated as one design pattern.

Improvement plan:
- Tier 1: add a new Chapter 54 section: `Safety Cases And Assurance Arguments For Embodied AI`.
- Tier 1: add a comparative standards map across AVs, drones, industrial robots, AMRs, and humanoids.
- Tier 2: add a lab where a learned policy is wrapped by a runtime assurance monitor, with a safety-case artifact and incident replay.
- Tier 3: add templates: hazard log, ODD card, safety monitor interface, incident report, rollback plan.

Key sources:
- ISO 21448 SOTIF: https://www.iso.org/standard/77490.html
- UL 4600 overview: https://users.ece.cmu.edu/~koopman/ul4600/index.html
- UNECE R157: https://unece.org/transport/documents/2021/03/standards/un-regulation-no-157-automated-lane-keeping-systems-alks
- NHTSA VSSA: https://www.nhtsa.gov/automated-driving-systems/voluntary-safety-self-assessment
- FAA Remote ID: https://www.faa.gov/uas/getting_started/remote_id
- CBF survey: https://arxiv.org/html/2408.13271v1

### 10. Research And Course-Grade Embodied AI Platforms

Current coverage:
- Good in Chapter 59 and Chapter 60, with capstones, teaching paths, compute budgeting, and appendices. The book already has course-ready shape.

Researcher-grade missing material:
- Capstones need stronger application tracks that map directly to the top 10 application areas.
- Reproducibility should include pinned simulator versions, seeded scenario suites, standard logs, replayable failures, grading rubrics, artifact cards, and compute-budget tiers.
- Course platforms should be explicitly grouped: Gazebo, Isaac Sim, Isaac Lab, MuJoCo, AI2-THOR, Habitat 3.0, ManiSkill, ROS-Industrial, CARLA, CommonRoad, PX4 SITL.

Improvement plan:
- Tier 1: add an application-track capstone map with 10 tracks matching this audit.
- Tier 1: add project templates for each track: objective, assumptions, starter stack, dataset or simulator, metrics, safety constraints, artifact checklist, and grading rubric.
- Tier 2: add a reproducibility appendix card format for every lab.
- Tier 3: add instructor notes for compute-light, workstation, and cloud-GPU versions of each capstone.

Key sources:
- ROS-Industrial: https://rosindustrial.org/
- NIST ARIAC: https://www.nist.gov/el/intelligent-systems-division-73500/agile-robotics-industrial-automation-competition
- RobotPerf: https://arxiv.org/abs/2309.09212
- Habitat 3.0: https://aihabitat.org/habitat3/
- AI2-THOR: https://ai2thor.allenai.org/
- ManiSkill: https://maniskill.readthedocs.io/en/latest/user_guide/index.html

## Cross-Cutting Additions Recommended

### Tier 1

1. Add an application reference map after the front matter or in Chapter 1 that tells each application reader which chapters to study and which labs to run.
2. Add a safety assurance chapter section with cross-domain standards and evidence artifacts.
3. Add an industrial and logistics robotics chapter or major section.
4. Add a robot data engineering section covering schemas, calibration, sync, filtering, licensing, failure data, and replay.
5. Add a simulator-to-hardware reproducibility template used by humanoid, drone, AV, and mobile manipulation labs.

### Tier 2

1. Add benchmark tables for humanoids, mobile manipulation, drones, AVs, SLAM, VLA systems, industrial robotics, and course platforms.
2. Add closed-loop evaluation warnings wherever open-loop metrics can mislead.
3. Add diagrams for each application stack: perception, state estimation, planning, control, safety, logs, deployment.
4. Add application-specific capstone templates and grading rubrics.
5. Add a deployment telemetry pattern: logs, metrics, incident replay, rollback, drift detection, human override.

### Tier 3

1. Add Gemini illustrations for new application-track maps after content approval.
2. Add glossary entries for ODD, SOTIF, UL 4600, OpenSCENARIO, uXRCE-DDS, VIO, LIO, WMS, MES, Open-RMF, RT-X, action chunking, and behavior foundation model.
3. Add a source-curation appendix grouping official docs, papers, benchmarks, and standards by application.
4. Add reading pathways for researchers, developers, instructors, and product teams.

## Proposed Structural Placement

Preferred structure with minimal disruption:

- Front matter: add `Application Reader Pathways`.
- Chapter 29: add `Modern SLAM Systems And Failure Modes`.
- Chapter 30: add `Field Navigation Under Degraded Sensing`.
- Chapter 34: add `Action Representations In VLA Systems`.
- Chapter 35: add `Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models`.
- Chapter 42: add `Mobile Manipulation: Base, Arm, Perception, And Recovery`.
- Chapter 47: add `PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence`.
- Chapter 48: add `Closed-Loop Driving Evaluation And Safety Assurance`.
- Chapter 54: add `Safety Cases And Assurance Arguments For Embodied AI`.
- Chapter 55 or new Chapter 55.6: add `Industrial Fleets, Open-RMF, AMR Interoperability, And Operations`.
- Chapter 59: add `Application Track Capstone Templates`.
- Appendix C: add application tool matrices.
- Appendix F: add application benchmark matrices.
- Appendix G: add application reproducibility cards.

## Scout Agent Coverage

Five scouting agents reviewed recent developments and sources for:

1. Humanoids and mobile manipulation.
2. Drones, navigation, and SLAM.
3. Autonomous vehicles and safety-critical embodied AI.
4. Embodied foundation models and simulation-first robot learning.
5. Industrial logistics robotics and course-grade platforms.

No book content was changed in this audit pass.
