export const meta = {
  name: 'wave-5-catchup',
  description: 'Wave 5 catch-up: cross-reference links for sections missed by compaction',
  phases: [{ title: 'Cross-refs catchup', detail: 'Remaining sections get 3-6 inline cross-ref links' }],
}

const SHORT_MAP = `1.1|Static prediction vs. embodied interaction|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.1.html
1.2|Why intelligence needs a world; the perception-action loop|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.2.html
1.3|Agents, environments, observations, actions, rewards, constraints|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.3.html
1.4|Physical vs. simulated embodiment|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.4.html
1.5|The "Physical AI" framing and why 2023-2026 changed the field|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.5.html
1.6|Examples: vacuum, drone, autonomous vehicle, manipulator, humanoid, ga|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.6.html
1.7|Why embodied AI is hard (partial observability, long horizons, safety,|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.7.html
1.8|Map of the book|part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.8.html
2.1|Agents and environments formally|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.1.html
2.2|State, observation, hidden variables, partial observability|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.2.html
2.3|Action types: discrete, continuous, symbolic, motor-level, chunked|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.3.html
2.4|Rewards, goals, costs, constraints|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.4.html
2.5|Episodes, horizons, trajectories, discounting|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.5.html
2.6|Markov decision processes; Bellman equations|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.6.html
2.7|Partially observable MDPs; belief states|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.7.html
2.8|Why embodiment is usually partially observable|part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.8.html
3.1|The canonical stack: sense, perceive, estimate, predict, plan, control|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.1.html
3.2|Classical modular robotics pipeline|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.2.html
3.3|End-to-end learned policy pipeline|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.3.html
3.4|Hybrid and hierarchical architectures|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.4.html
3.5|Reactive vs. deliberative agents|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.5.html
3.6|Dual-system (System 1 / System 2) designs and where they come from|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.6.html
3.7|Where LLMs, VLMs, and VLAs sit in the stack|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.7.html
3.8|Failure modes of each architecture|part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.8.html
49.1|One agent vs. many|part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.1.html
49.2|Cooperation, competition, communication|part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.2.html
49.3|Shared perception and task allocation|part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.3.html
49.4|Multi-agent RL (with PettingZoo)|part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.4.html
49.5|Swarms and emergent behavior; evaluating teams|part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.5.html
50.1|Robots among humans|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.1.html
50.2|Natural-language interaction and social navigation|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.2.html
50.3|Intent recognition and trust calibration|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.3.html
50.4|Explainable robot behavior|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.4.html
50.5|Human feedback and shared autonomy|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.5.html
50.6|Ethical concerns|part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.6.html
51.1|Closed- vs. open-world tasks|part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.1.html
51.2|Novel objects and instructions; changing environments|part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.2.html
51.3|Long-horizon tasks|part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.3.html
51.4|Distribution shift triggers and open-world adaptation|part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.4.html
51.5|Novelty detection and retraining triggers; open-world evaluation|part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.5.html
52.1|Why accuracy is not enough|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.1.html
52.2|Success rate, path efficiency, time and energy cost|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.2.html
52.3|Safety violations and constraint satisfaction|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.3.html
52.4|Robustness and generalization metrics|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.4.html
52.5|Reproducible evaluation: SIMPLER and sim-as-proxy|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.5.html
52.6|Real-world evaluation hygiene; benchmark design|part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.6.html
53.1|What goes wrong: sensor noise, distribution shift|part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.1.html
53.2|Model uncertainty and calibration|part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.2.html
53.3|Out-of-distribution detection|part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.3.html
53.4|Runtime monitoring and fail-safe behavior|part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.4.html
54.1|Why embodied safety is different (physical harm)|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.1.html
54.2|Constraint violations and safe exploration|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.2.html
54.3|Control barrier functions and Hamilton-Jacobi reachability|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.3.html
54.4|Shielded policies and safety filters|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.4.html
54.5|Human override and safety testing|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.5.html
54.6|Deployment approval and safety cases|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.6.html
54.7|Safety Cases And Assurance Arguments For Embodied AI|part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.7.html
55.1|From notebook to robot|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.1.html
55.2|Real-time inference and control rates|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.2.html
55.3|Edge vs. cloud-robot computation; asynchronous inference|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.3.html
55.4|Logging, monitoring, model updates|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.4.html
55.5|Failure recovery, security, maintenance|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.5.html
55.6|Industrial Fleets, Open-RMF, AMR Interoperability, And Operations|part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.6.html
56.1|Why memory matters; short- vs. long-term|part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.1.html
56.2|Spatial, episodic, and semantic memory|part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.2.html
56.3|Memory retrieval for planning|part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.3.html
56.4|Memory errors|part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.4.html
57.1|Learning after deployment|part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.1.html
57.2|Catastrophic forgetting and mitigation|part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.2.html
57.3|Online adaptation; human correction as data|part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.3.html
57.4|Safe continual learning; evaluation over time|part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.4.html
58.1|Scaling laws and data engines for robots|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.1.html
58.2|Generalist vs. specialist policies|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.2.html
58.3|World models in the robot loop|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.3.html
58.4|The open-vs-closed model divide|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.4.html
58.5|What is still unsolved (long-horizon reasoning, reliability, real-worl|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.5.html
58.99|Frontier Watch|part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.99.html
59.1|Object search in a simulated home|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.1.html
59.10|Multi-agent search and rescue|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.10.html
59.11|Open-ended research project|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.11.html
59.12|Application Track Capstone Templates|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.12.html
59.2|Language-guided navigation with replanning|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.2.html
59.3|Vision-based robotic pick-and-place (IL + RL)|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.3.html
59.4|Fine-tune an open VLA on a custom task (LeRobot)|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.4.html
59.5|Learned locomotion with sim-to-real analysis|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.5.html
59.6|World-model-based planning agent|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.6.html
59.7|Safety-shielded embodied agent|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.7.html
59.8|LLM-based household task planner|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.8.html
59.9|Drone inspection planner|part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.9.html
60.1|One-semester graduate course (14 weeks)|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.1.html
60.2|One-semester advanced undergraduate course (lighter theory, more labs)|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.2.html
60.3|Two-semester sequence|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.3.html
60.4|Research-seminar track|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.4.html
60.5|Lab infrastructure and compute budgeting for instructors|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.5.html
60.6|Assessment, rubrics, and academic-integrity notes for code assignments|part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.6.html
4.1|Why space is the substrate of embodiment|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.1.html
4.2|Points, vectors, poses, frames|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.2.html
4.3|Rotations: matrices, Euler angles, axis-angle, quaternions; pitfalls|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.3.html
4.4|Rigid transforms, homogeneous coordinates, SE(3)|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.4.html
4.5|2D and 3D transformations; transform trees (tf in ROS)|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.5.html
4.6|Camera, body, and world frames|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.6.html
4.7|Common frame mistakes and how to debug them|part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/section-4.7.html
5.1|Position, velocity, acceleration; twists|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.1.html
5.2|Holonomic vs. non-holonomic motion|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.2.html
5.3|Differential-drive and car-like robots|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.3.html
5.4|Robot arms, joints, the kinematic chain|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.4.html
5.5|Forward kinematics|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.5.html
5.6|Inverse kinematics: analytic, numerical (Jacobian), and learned|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.6.html
5.7|Jacobians, singularities, manipulability|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.7.html
5.8|Motion constraints|part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/section-5.8.html
6.1|From kinematics to dynamics: forces, torques, inertia|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.1.html
6.2|Rigid-body dynamics; the manipulator equation|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.2.html
6.3|Contact, friction, and why contact-rich sim is hard|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.3.html
6.4|Numerical integration and stability|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.4.html
6.5|Differentiable physics: what it buys you|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.5.html
6.6|Why GPU-parallel simulation changed robot learning|part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.6.html
7.1|Open-loop vs. closed-loop control|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.1.html
7.2|Feedback, error, stability, overshoot, oscillation|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.2.html
7.3|PID control, intuition and tuning|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.3.html
7.4|State-space control, LQR|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.4.html
7.5|Model predictive control (MPC) as receding-horizon optimization|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.5.html
7.6|Operational-space and whole-body control (preview for humanoids)|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.6.html
7.7|Controllers vs. policies; when learning helps and when it makes contro|part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/section-7.7.html
8.1|What sensors provide and what they cost|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.1.html
8.2|Cameras, depth (stereo/structured light/ToF), LiDAR|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.2.html
8.3|IMU, wheel odometry, joint encoders, proprioception|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.3.html
8.4|Tactile and force/torque sensing (GelSight, DIGIT): preview|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.4.html
8.5|Sensor noise and uncertainty models|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.5.html
8.6|Bayesian filtering: Kalman, EKF, particle filters|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.6.html
8.7|Sensor fusion intuition and practice|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.7.html
8.8|Perception as an imperfect window into the world|part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/section-8.8.html
9.1|Why real-world learning is slow, costly, and risky|part-3-simulation-tooling-and-the-modern-stack/module-09-why-simulation-is-central/section-9.1.html
9.2|Simulation as data generator, testbed, and curriculum|part-3-simulation-tooling-and-the-modern-stack/module-09-why-simulation-is-central/section-9.2.html
9.3|Fidelity: physical, visual, behavioral|part-3-simulation-tooling-and-the-modern-stack/module-09-why-simulation-is-central/section-9.3.html
9.4|The reality gap as a measurable quantity|part-3-simulation-tooling-and-the-modern-stack/module-09-why-simulation-is-central/section-9.4.html
9.5|Benchmark environment map|part-3-simulation-tooling-and-the-modern-stack/module-09-why-simulation-is-central/section-9.5.html
10.1|Gym is dead; Gymnasium is the standard|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.1.html
10.2|Observation and action spaces|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.2.html
10.3|Reward design and termination|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.3.html
10.4|Vectorized environments; wrappers|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.4.html
10.5|Rendering, logging, and debugging|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.5.html
10.6|Evaluation protocol and seeding|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.6.html
10.7|PettingZoo for multi-agent|part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.7.html
11.1|What Physics Simulators Model|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.1.html
11.2|MuJoCo and the MJCF or URDF Model Formats|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.2.html
11.3|MuJoCo MJX and MuJoCo Warp|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.3.html
11.4|NVIDIA Isaac Sim and Isaac Lab|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.4.html
11.5|The Newton Physics Engine and OpenUSD|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.5.html
11.6|Genesis and Generative Multi-Physics|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.6.html
11.7|Drake, SAPIEN, ROS 2, and Gazebo|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.7.html
11.8|Choosing a Simulator|part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.8.html
12.1|Why standardized benchmarks matter|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.1.html
12.2|Manipulation: ManiSkill3, robosuite, RoboCasa, robomimic, RLBench|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.2.html
12.3|Lifelong and language-conditioned: LIBERO, CALVIN, Meta-World|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.3.html
12.4|Household and long-horizon: BEHAVIOR-1K / OmniGibson|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.4.html
12.5|Navigation and social: Habitat 3.0, AI2-THOR / ProcTHOR|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.5.html
12.6|Reading a leaderboard without fooling yourself|part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/section-12.6.html
13.1|Why synthetic variation matters|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.1.html
13.2|Visual, physics, sensor, and task randomization|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.2.html
13.3|Curriculum and automatic randomization|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.3.html
13.4|Photoreal rendering and tiled cameras|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.4.html
13.5|real2sim2real and asset/scene reconstruction|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.5.html
13.6|Randomization vs. realism; measuring transfer readiness|part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/section-13.6.html
14.1|Learning from interaction; return and discounting|part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.1.html
14.2|Policies and value functions|part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.2.html
14.3|Exploration vs. exploitation|part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.3.html
14.4|Model-free vs. model-based; on- vs. off-policy|part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.4.html
14.5|Why RL is hard in embodied systems (sample cost, reward, safety)|part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.5.html
15.1|Direct policy optimization; stochastic policies|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.1.html
15.2|The policy gradient theorem; REINFORCE|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.2.html
15.3|Actor-critic and advantage estimation (GAE)|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.3.html
15.4|Trust regions; TRPO to PPO|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.4.html
15.5|PPO in practice: the implementation details that matter|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.5.html
15.6|Reward shaping and its hazards|part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/section-15.6.html
16.1|Q-learning; deep Q-networks|part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/section-16.1.html
16.2|Replay buffers and target networks|part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/section-16.2.html
16.3|Continuous control: DDPG, TD3, SAC|part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/section-16.3.html
16.4|Maximum-entropy RL|part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/section-16.4.html
16.5|Sample efficiency and off-policy failure modes|part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/section-16.5.html
17.1|Why thousands of parallel envs changed the field|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.1.html
17.2|Learning to walk in minutes: the parallel-RL recipe|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.2.html
17.3|Isaac Lab with SKRL / rl_games / RSL-RL|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.3.html
17.4|MJX/Brax-training and JAX RL|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.4.html
17.5|Teacher-student and privileged-information distillation|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.5.html
17.6|Throughput, wall-clock, and cost engineering|part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/section-17.6.html
18.1|Why rewards are dangerous|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.1.html
18.2|Sparse vs. dense; shaping done right|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.2.html
18.3|Goal-conditioned policies; hindsight experience replay|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.3.html
18.4|Reward hacking, with case studies|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.4.html
18.5|Human preferences and learned reward models (RLHF for control)|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.5.html
18.6|Safety-aware and constrained rewards|part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/section-18.6.html
19.1|Why embodied exploration is expensive and risky|part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.1.html
19.2|Intrinsic motivation, curiosity, count-based and novelty methods|part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.2.html
19.3|Safe exploration|part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.3.html
19.4|Exploration under partial observability|part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.4.html
20.1|The reality gap revisited|part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/section-20.1.html
20.2|What transfers and what does not|part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/section-20.2.html
20.3|Domain randomization, system identification, adaptation (RMA)|part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/section-20.3.html
20.4|Fine-tuning on hardware; safe real-world RL|part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/section-20.4.html
20.5|Measuring transfer performance|part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/section-20.5.html
21.1|Why learning from demonstration matters for robots|part-5-learning-from-demonstration-and-robot-data/module-21-imitation-learning/section-21.1.html
21.2|Behavior cloning; the distribution-shift problem|part-5-learning-from-demonstration-and-robot-data/module-21-imitation-learning/section-21.2.html
21.3|DAgger and dataset aggregation|part-5-learning-from-demonstration-and-robot-data/module-21-imitation-learning/section-21.3.html
21.4|Inverse reinforcement learning|part-5-learning-from-demonstration-and-robot-data/module-21-imitation-learning/section-21.4.html
21.5|Sources of demonstrations: humans, planners, foundation models|part-5-learning-from-demonstration-and-robot-data/module-21-imitation-learning/section-21.5.html
22.1|Why single-step prediction fails on real manipulation|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.1.html
22.2|ACT (Action Chunking Transformer) and the cVAE formulation|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.2.html
22.3|ALOHA, ALOHA 2, and Mobile ALOHA|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.3.html
22.4|Diffusion Policy: action generation by denoising|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.4.html
22.5|Flow matching for actions|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.5.html
22.6|VQ-BeT and discretized behavior modeling|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.6.html
22.7|Choosing an action representation: a decision guide|part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/section-22.7.html
23.1|Why data is the bottleneck|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.1.html
23.2|Leader-follower teleoperation (ALOHA, GELLO)|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.2.html
23.3|Handheld and in-the-wild collection (UMI)|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.3.html
23.4|Immersive/VR teleoperation (Open-TeleVision)|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.4.html
23.5|Data quality, diversity, and labeling|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.5.html
23.6|The LeRobotDataset format and pipeline|part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/section-23.6.html
24.1|The major datasets: Open X-Embodiment, DROID, BridgeData V2, RH20T, Ro|part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/section-24.1.html
24.2|Dataset structure, embodiment metadata, and licensing|part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/section-24.2.html
24.3|Cross-embodiment pooling|part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/section-24.3.html
24.4|Empirical data scaling laws in imitation learning|part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/section-24.4.html
24.5|Curating and mixing data|part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/section-24.5.html
25.1|Learning without online interaction|part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/section-25.1.html
25.2|Distribution shift and extrapolation error|part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/section-25.2.html
25.3|Conservative methods (CQL, IQL) and their intuition|part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/section-25.3.html
25.4|Offline-to-online fine-tuning|part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/section-25.4.html
25.5|Evaluating offline policies rigorously|part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/section-25.5.html
26.1|What a skill is; low- vs. high-level actions|part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/section-26.1.html
26.2|The options framework|part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/section-26.2.html
26.3|Skill discovery and hierarchical RL|part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/section-26.3.html
26.4|Language as a high-level controller|part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/section-26.4.html
26.5|Skill libraries for embodied agents|part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/section-26.5.html
27.1|Seeing to classify vs. seeing to act|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.1.html
27.2|Detection, segmentation, and the Segment Anything family|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.2.html
27.3|Depth estimation and metric scale|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.3.html
27.4|Optical flow and motion cues|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.4.html
27.5|Affordances and graspable regions|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.5.html
27.6|Active and embodied perception|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.6.html
27.7|When perception failures become action failures|part-6-embodied-perception/module-27-visual-perception-for-action/section-27.7.html
28.1|Why 3D matters for manipulation and navigation|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.1.html
28.2|Point clouds and depth maps|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.2.html
28.3|3D detection and scene reconstruction|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.3.html
28.4|Occupancy grids and voxel maps|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.4.html
28.5|NeRF: implicit radiance fields|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.5.html
28.6|3D Gaussian Splatting: explicit, editable, real-time|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.6.html
28.7|Scene representations for robotics: SLAM, real2sim, manipulation|part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.7.html
29.1|Where am I and what does the world look like|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.1.html
29.2|Odometry and dead reckoning|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.2.html
29.3|Localization (Monte Carlo / particle filters)|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.3.html
29.4|Mapping and occupancy grids|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.4.html
29.5|SLAM: graph-based and visual SLAM|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.5.html
29.6|Neural and Gaussian-splat SLAM|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.6.html
29.7|Map uncertainty|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.7.html
29.8|Modern SLAM Systems And Failure Modes|part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.8.html
30.1|Navigation as embodied intelligence|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.1.html
30.2|Graph search: BFS, Dijkstra, A*|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.2.html
30.3|Sampling-based planning: RRT, RRT*, PRM|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.3.html
30.4|Local planning and obstacle avoidance (DWA, potential fields)|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.4.html
30.5|Learned navigation policies|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.5.html
30.6|Language- and image-goal navigation|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.6.html
30.7|Field Navigation Under Degraded Sensing|part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.7.html
31.1|Why language matters in embodied AI|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.1.html
31.2|Instructions, goals, constraints|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.2.html
31.3|Grounding language in perception; referring expressions|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.3.html
31.4|Object- and region-centric grounding|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.4.html
31.5|Task planning from language; ambiguity and clarification|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.5.html
31.6|Human-agent interaction|part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.6.html
32.1|From image-text models to embodied perception|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.1.html
32.2|CLIP, SigLIP, DINOv2 representations|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.2.html
32.3|Vision-language encoders and open-vocabulary detection|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.3.html
32.4|Visual question answering and scene description in environments|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.4.html
32.5|Multimodal memory|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.5.html
32.6|Limits of static VLMs in dynamic worlds|part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.6.html
33.1|What LLMs can and cannot do in embodied tasks|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.1.html
33.2|SayCan: affordance-grounded planning|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.2.html
33.3|Code as Policies: LLMs that write robot code|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.3.html
33.4|VoxPoser: composing 3D value maps|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.4.html
33.5|ReKep: relational keypoint constraints|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.5.html
33.6|Tool use, action APIs, plan verification, replanning|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.6.html
33.7|Memory, state tracking, and hallucination in physical tasks|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.7.html
33.8|Safe LLM-agent interfaces|part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.8.html
34.1|From VLMs to VLAs: the core idea|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.1.html
34.2|The lineage: RT-1, RT-2, RT-X / Open X-Embodiment|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.2.html
34.3|Open generalist policies: Octo, OpenVLA|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.3.html
34.4|Diffusion and flow VLAs: RDT-1B, pi-zero, pi-zero FAST, pi-zero point |part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.4.html
34.5|Action tokenization vs. continuous heads; the FAST tokenizer|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.5.html
34.6|Co-training with web data for semantic generalization|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.6.html
34.7|Prompting and conditioning embodied policies|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.7.html
34.8|Evaluating VLA behavior; limitations and open problems|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.8.html
34.9|Action Representations In VLA Systems|part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.9.html
35.1|Why foundation models matter for robotics|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.1.html
35.2|Cross-embodiment training and transfer|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.2.html
35.3|Dual-system architectures: GR00T N1.5, Helix, Gemini Robotics (with Fr|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.3.html
35.4|Large behavior models and rigorous evaluation|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.4.html
35.5|Adapting to new robots; prompting and conditioning|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.5.html
35.6|Data scale, compute, and the open-vs-closed divide|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.6.html
35.7|Limitations and open questions|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.7.html
35.8|Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models|part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.8.html
36.1|Why agents need to predict|part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/section-36.1.html
36.2|Forward/dynamics models; state vs. observation prediction|part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/section-36.2.html
36.3|Error accumulation and horizon|part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/section-36.3.html
36.4|Uncertainty in prediction|part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/section-36.4.html
36.5|Planning with predicted futures|part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/section-36.5.html
37.1|Model-free vs. model-based trade-offs|part-8-world-models-and-model-based-embodied-ai/module-37-model-based-rl-and-mpc/section-37.1.html
37.2|Learning dynamics models; ensembles and uncertainty|part-8-world-models-and-model-based-embodied-ai/module-37-model-based-rl-and-mpc/section-37.2.html
37.3|Planning with learned models; MPC and CEM/MPPI|part-8-world-models-and-model-based-embodied-ai/module-37-model-based-rl-and-mpc/section-37.3.html
37.4|Imagination rollouts|part-8-world-models-and-model-based-embodied-ai/module-37-model-based-rl-and-mpc/section-37.4.html
37.5|Sample-efficiency advantages and failure modes|part-8-world-models-and-model-based-embodied-ai/module-37-model-based-rl-and-mpc/section-37.5.html
38.1|Why predict in latent space|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.1.html
38.2|Autoencoders and recurrent state-space models (RSSM)|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.2.html
38.3|Dreamer to DreamerV3|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.3.html
38.4|Transformer world models (IRIS)|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.4.html
38.5|TD-MPC2: latent MPC at scale|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.5.html
38.6|World models for visual control|part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.6.html
39.1|Generative models as learned simulators|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.1.html
39.2|Genie 1-3: interactive, playable world models|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.2.html
39.3|Video generation as world simulation: Sora and successors|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.3.html
39.4|NVIDIA Cosmos: world foundation models for physical AI|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.4.html
39.5|GameNGen and Oasis: neural game engines|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.5.html
39.6|Using generative world models for data and evaluation (e.g., humanoid |part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.6.html
39.7|Evaluating consistency, controllability, and horizon|part-8-world-models-and-model-based-embodied-ai/module-39-generative-and-video-world-models/section-39.7.html
40.1|Predict in representation space, not pixels: the JEPA idea|part-8-world-models-and-model-based-embodied-ai/module-40-predictive-representations-and-self-supervised-world-models/section-40.1.html
40.2|I-JEPA and V-JEPA|part-8-world-models-and-model-based-embodied-ai/module-40-predictive-representations-and-self-supervised-world-models/section-40.2.html
40.3|V-JEPA 2 and action-conditioned latent planning|part-8-world-models-and-model-based-embodied-ai/module-40-predictive-representations-and-self-supervised-world-models/section-40.3.html
40.4|Self-supervised pretraining for control|part-8-world-models-and-model-based-embodied-ai/module-40-predictive-representations-and-self-supervised-world-models/section-40.4.html
41.1|Diffusion models as planners|part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.1.html
41.2|Diffuser and Decision Diffuser|part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.2.html
41.3|Generative trajectory planning and scoring|part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.3.html
41.4|Generating scenes and synthetic experience|part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.4.html
41.5|Risks of generated experience|part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.5.html
42.1|What manipulation is; reaching and pushing|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.1.html
42.2|Pick-and-place pipelines|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.2.html
42.3|Contact-rich interaction|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.3.html
42.4|Perception for manipulation|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.4.html
42.5|Learning manipulation policies (IL, RL, VLA)|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.5.html
42.6|Failure detection and recovery|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.6.html
42.7|Mobile Manipulation: Base, Arm, Perception, And Recovery|part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.7.html
43.1|Grasp synthesis: analytic and learned (Dex-Net lineage)|part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.1.html
43.2|Parallel-jaw vs. multi-finger hands|part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.2.html
43.3|In-hand manipulation and reorientation|part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.3.html
43.4|Dexterous RL with demonstrations|part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.4.html
43.5|Sim-to-real for dexterity|part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.5.html
44.1|Why touch matters for contact-rich tasks|part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.1.html
44.2|Vision-based tactile sensors (GelSight, DIGIT)|part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.2.html
44.3|Simulating touch (e.g., tactile sim in Isaac)|part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.3.html
44.4|Visuo-tactile pretraining and policies|part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.4.html
44.5|Combining vision and touch|part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.5.html
45.1|Wheeled, legged, and hybrid robots|part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.1.html
45.2|Balance, stability, and gait|part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.2.html
45.3|Learning locomotion with massively parallel RL|part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.3.html
45.4|Terrain adaptation, parkour, and rapid motor adaptation|part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.4.html
45.5|Energy efficiency; sim-to-real and safety in locomotion|part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.5.html
46.1|Why humanoids became the focus (data, morphology, hardware cost)|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.1.html
46.2|Platforms: Unitree G1/H1, Figure, Optimus, 1X, electric Atlas, Apptron|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.2.html
46.3|Whole-body and operational-space control|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.3.html
46.4|Learning from humans: HumanPlus, OmniH2O/HOVER, motion retargeting|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.4.html
46.5|Teleoperation for humanoids|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.5.html
46.6|Dual-system humanoid foundation models (tie-back to Ch. 35)|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.6.html
46.7|Safety for human-scale robots|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.7.html
46.8|Advanced humanoid dynamics and contact mechanics|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html
46.9|Boston Dynamics-style loco-manipulation research track|part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.9.html
47.1|Why aerial agents are special|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.1.html
47.2|Flight dynamics intuition|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.2.html
47.3|Perception, navigation, and obstacle avoidance|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.3.html
47.4|Coverage and inspection; multi-drone coordination|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.4.html
47.5|Safety, regulation, and simulation for aerial agents|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.5.html
47.6|Quadrotor dynamics and flight control|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.6.html
47.7|Trajectory generation and GPS-denied missions|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.7.html
47.8|PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence|part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.8.html
48.1|Driving as perception, prediction, planning, control|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.1.html
48.2|Sensors and sensor fusion in AVs|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.2.html
48.3|Detection, lane and behavior prediction|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.3.html
48.4|Route and local planning|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.4.html
48.5|End-to-end and world-model driving|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.5.html
48.6|Scenario testing and safety cases|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.6.html
48.7|Vehicle kinematics, dynamics, and control|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.7.html
48.8|Route, behavior, and scenario-based planning|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.8.html
48.9|Closed-Loop Driving Evaluation And Safety Assurance|part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.9.html`

const TARGETS = [{"sec": "11.8", "title": "Choosing a Simulator", "path": "part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/section-11.8.html"}, {"sec": "14.1", "title": "Learning from interaction; return and discounting", "path": "part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.1.html"}, {"sec": "14.5", "title": "Why RL is hard in embodied systems (sample cost, reward, safety)", "path": "part-4-reinforcement-learning-for-embodied-agents/module-14-reinforcement-learning-refresher/section-14.5.html"}, {"sec": "19.1", "title": "Why embodied exploration is expensive and risky", "path": "part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.1.html"}, {"sec": "19.4", "title": "Exploration under partial observability", "path": "part-4-reinforcement-learning-for-embodied-agents/module-19-exploration-in-embodied-worlds/section-19.4.html"}, {"sec": "35.4", "title": "Large behavior models and rigorous evaluation", "path": "part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.4.html"}, {"sec": "35.5", "title": "Adapting to new robots; prompting and conditioning", "path": "part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.5.html"}, {"sec": "35.6", "title": "Data scale, compute, and the open-vs-closed divide", "path": "part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.6.html"}, {"sec": "35.7", "title": "Limitations and open questions", "path": "part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.7.html"}, {"sec": "35.8", "title": "Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models", "path": "part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.8.html"}, {"sec": "38.1", "title": "Why predict in latent space", "path": "part-8-world-models-and-model-based-embodied-ai/module-38-latent-world-models/section-38.1.html"}, {"sec": "41.1", "title": "Diffusion models as planners", "path": "part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.1.html"}, {"sec": "41.2", "title": "Diffuser and Decision Diffuser", "path": "part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.2.html"}, {"sec": "41.3", "title": "Generative trajectory planning and scoring", "path": "part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.3.html"}, {"sec": "41.4", "title": "Generating scenes and synthetic experience", "path": "part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.4.html"}, {"sec": "41.5", "title": "Risks of generated experience", "path": "part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.5.html"}, {"sec": "42.1", "title": "What manipulation is; reaching and pushing", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.1.html"}, {"sec": "42.2", "title": "Pick-and-place pipelines", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.2.html"}, {"sec": "42.3", "title": "Contact-rich interaction", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.3.html"}, {"sec": "42.4", "title": "Perception for manipulation", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.4.html"}, {"sec": "42.5", "title": "Learning manipulation policies (IL, RL, VLA)", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.5.html"}, {"sec": "42.6", "title": "Failure detection and recovery", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.6.html"}, {"sec": "42.7", "title": "Mobile Manipulation: Base, Arm, Perception, And Recovery", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.7.html"}, {"sec": "43.1", "title": "Grasp synthesis: analytic and learned (Dex-Net lineage)", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.1.html"}, {"sec": "43.2", "title": "Parallel-jaw vs. multi-finger hands", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.2.html"}, {"sec": "43.3", "title": "In-hand manipulation and reorientation", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.3.html"}, {"sec": "43.4", "title": "Dexterous RL with demonstrations", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.4.html"}, {"sec": "43.5", "title": "Sim-to-real for dexterity", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-43-grasping-and-dexterous-manipulation/section-43.5.html"}, {"sec": "44.1", "title": "Why touch matters for contact-rich tasks", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.1.html"}, {"sec": "44.2", "title": "Vision-based tactile sensors (GelSight, DIGIT)", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.2.html"}, {"sec": "44.3", "title": "Simulating touch (e.g., tactile sim in Isaac)", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.3.html"}, {"sec": "44.4", "title": "Visuo-tactile pretraining and policies", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.4.html"}, {"sec": "44.5", "title": "Combining vision and touch", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-44-tactile-and-visuo-tactile-learning/section-44.5.html"}, {"sec": "46.8", "title": "Advanced humanoid dynamics and contact mechanics", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html"}, {"sec": "46.9", "title": "Boston Dynamics-style loco-manipulation research track", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.9.html"}, {"sec": "47.1", "title": "Why aerial agents are special", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.1.html"}, {"sec": "47.2", "title": "Flight dynamics intuition", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.2.html"}, {"sec": "47.3", "title": "Perception, navigation, and obstacle avoidance", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.3.html"}, {"sec": "47.4", "title": "Coverage and inspection; multi-drone coordination", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.4.html"}, {"sec": "47.5", "title": "Safety, regulation, and simulation for aerial agents", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.5.html"}, {"sec": "47.6", "title": "Quadrotor dynamics and flight control", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.6.html"}, {"sec": "47.7", "title": "Trajectory generation and GPS-denied missions", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.7.html"}, {"sec": "47.8", "title": "PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.8.html"}, {"sec": "48.1", "title": "Driving as perception, prediction, planning, control", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.1.html"}, {"sec": "48.2", "title": "Sensors and sensor fusion in AVs", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.2.html"}, {"sec": "48.3", "title": "Detection, lane and behavior prediction", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.3.html"}, {"sec": "48.4", "title": "Route and local planning", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.4.html"}, {"sec": "48.5", "title": "End-to-end and world-model driving", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.5.html"}, {"sec": "48.6", "title": "Scenario testing and safety cases", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.6.html"}, {"sec": "48.7", "title": "Vehicle kinematics, dynamics, and control", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.7.html"}, {"sec": "48.8", "title": "Route, behavior, and scenario-based planning", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.8.html"}, {"sec": "48.9", "title": "Closed-Loop Driving Evaluation And Safety Assurance", "path": "part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.9.html"}]


phase('Cross-refs catchup')
log(`Inserting cross-refs into ${TARGETS.length} remaining sections...`)

await pipeline(TARGETS, async (t) => agent(
  `You are the Cross-Reference Architect (#13) for an embodied AI textbook.

TASK: Insert 3 to 6 inline cross-reference links into section ${t.sec}.
File: ${t.path}

SECTION MAP (number: short title):
${SHORT_MAP}

INSTRUCTIONS:
1. Read file "${t.path}"
2. Count any existing <a href="../../ links — if already 3 or more, return "SKIP: already has links" and stop.
3. Identify 3-6 concepts that are covered in OTHER sections.
4. For each, wrap a natural phrase in: <a href="../../{target_path}">{phrase}</a>
   Path format: ../../part-N-name/module-MM-name/section-X.Y.html
5. Spread links across different paragraphs (max 2 per paragraph).
6. Skip: code blocks, headings, nav footer, epigraph, figure captions.
7. Edit the file directly with the Edit tool.
8. NEVER use em dashes or double dashes.

Return: "Added N links to: [list of target sections]" or "SKIP: [reason]"`,
  { label: `xref-catchup-${t.sec}`, phase: 'Cross-refs catchup' }
))

log('Wave 5 catch-up complete!')
return { wave: '5-catchup', sections_processed: TARGETS.length }
