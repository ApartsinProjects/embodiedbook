# Depth Remediation Queue

This queue converts the Round 2 depth audit into production work. It uses the same book-writers rubrics: deep explanation, code pedagogy, research grounding, self-containment, and publication QA.

## Gate Definition

A section is graduate-ready only when it has:

- A topic-native mechanism, not only an action-loop restatement.
- The core equation, algorithm, data schema, controller contract, or tool interface demanded by the title.
- One runnable or inspectable evidence artifact with expected-output interpretation.
- Concrete libraries or datasets that match the section topic.
- Failure analysis specific to the method, including assumptions and scope.
- Local reference support or a clear pointer to the chapter bibliography with named sources.

## Priority 1, Replace Template Cores

These sections should be rewritten first because the title promises algorithmic or system depth, but the current body leans heavily on generic scaffolding.

| Area | Sections | Required Upgrade |
|---|---|---|
| Robotics math and control | Modules 5 through 8 | Add IK solvers, Jacobian velocity maps, manipulator equations, contact models, PID and LQR derivations, MPC examples, Kalman filtering, sensor fusion equations, tactile uncertainty, and tool-specific checks for Drake, Pinocchio, CasADi, python-control, GTSAM, ROS 2, and MuJoCo. |
| RL algorithms | Modules 14 through 20 | Replace random-rollout examples with method-matched objectives and diagnostics: returns, advantages, log probabilities, PPO clipping, KL checks, Q-learning targets, SAC entropy temperature, replay bias, domain randomization, and sim-to-real evaluation. |
| Perception for action | Modules 27 through 30 | Add camera geometry, metric depth, optical flow, affordance scoring, active perception information gain, point-cloud lifting, SLAM graphs, occupancy updates, A*, RRT, DWA, learned navigation policies, and language-goal navigation benchmarks. |
| Manipulation and AV systems | Sections 42.3 and 48.2 | Add contact-rich hybrid dynamics, friction cones, impedance control, tactile feedback, AV sensor models, Kalman tracking, association, latency compensation, calibration drift, and CARLA or nuScenes style evaluation. |
| Capstone and teaching sections | Sections 59.4 and 60.1 | Turn these into real implementation and course artifacts: LeRobot dataset conversion, policy config, compute budget, rollout logs, grading rubric, weekly schedule, labs, readings, and milestones. |

## Priority 2, De-Template Repeated Prose

Remove or localize these repeated patterns:

- `reader fill in`, 607 occurrences in current HTML.
- `This section turns the idea of`, 179 occurrences.
- `Design a minimal experiment`, 246 occurrences.
- `See the chapter bibliography for primary papers`, 27 occurrences, all in Part VI.
- Generic epigraphs, generic perception-action-loop captions, and generic tool tables where the tools do not match the method.

Keep the same-artifact comparison principle, but move it into chapter labs or make each use section-specific.

## Priority 3, Add Expected-Output Pedagogy

The most common code-pedagogy issue is that snippets print a dictionary or trace without explaining what the output should mean. Fix by adding a sentence after each nontrivial code block:

- What output pattern indicates success.
- What value range or field should change under perturbation.
- What mismatch points to a convention, timing, units, or model error.

## Priority 4, Add Research And Tool Anchors

Use named sources and tools where they matter:

- Robotics foundations: Modern Robotics, Murray Li Sastry, Siciliano, LaValle, ROS tf2, Drake, Pinocchio, CasADi, GTSAM, MuJoCo, Isaac Sim, python-control.
- RL: Sutton and Barto, Williams REINFORCE, TRPO, PPO, DQN, SAC, TD3, Dreamer, TD-MPC2, CleanRL, Stable-Baselines3, RLlib.
- Robot data: DAgger, ACT, Diffusion Policy, ALOHA, Open X-Embodiment, robomimic, LeRobot.
- Perception and planning: OpenCV, Open3D, SAM, DINOv2, GTSAM, ORB-SLAM, COLMAP, Nav2, OMPL, Habitat, Gibson, AI2-THOR.
- AV and safety: CARLA, nuScenes, Waymo Open Dataset, RSS, CBF, Hamilton-Jacobi reachability, runtime monitoring, conformal prediction.

## Priority 5, Visual And Figure Depth

Replace generic loop figures where the section demands a specific concept:

- PPO: clipped surrogate curve, KL drift, advantage estimate flow.
- ALOHA and ACT: bimanual teleoperation, action chunks, temporal ensembling.
- SLAM: factor graph with odometry, loop closure, and landmark factors.
- RRT and A*: sampled tree or grid cost map with tie-breaking and heuristic admissibility.
- CBF and HJ reachability: safe set boundary, barrier condition, reachable set over time.

## Completion Criteria

After remediation, rerun:

```powershell
C:\Python314\python.exe scripts\audit_scientific_depth.py
C:\Python314\python.exe scripts\audit_html_book.py
C:\Python314\python.exe scripts\audit_book_depth.py
```

Target for the next gate:

- No `DEPTH-GAP` sections in `audit/scientific_depth_round_2.csv`.
- Fewer than 60 `REVIEW` sections.
- No generic placeholder phrase used as a section core.
- Every capstone and course-design section has real deliverables, rubrics, and expected artifacts.
