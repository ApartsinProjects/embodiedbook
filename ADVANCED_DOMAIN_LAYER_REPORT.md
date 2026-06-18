# Advanced Domain Engineering Layer Report

Prepared: 2026-06-18

## Scope

This pass adds specialist material for drones, autonomous vehicles, and Boston Dynamics-class humanoid robots without renumbering the rest of the book. The new sections live inside the existing Part IX domain chapters.

## New Sections

- Section 46.8: Advanced humanoid dynamics and contact mechanics
- Section 46.9: Boston Dynamics-style loco-manipulation research track
- Section 47.6: Quadrotor dynamics and flight control
- Section 47.7: Trajectory generation and GPS-denied missions
- Section 48.7: Vehicle kinematics, dynamics, and control
- Section 48.8: Route, behavior, and scenario-based planning

## What Was Added

- Centroidal dynamics, contact forces, ZMP-style reasoning, whole-body QP control, loco-manipulation, teleoperation, simulation-first research loops, HumanoidBench-style evaluation, and Boston Dynamics / RAI Institute research framing.
- Quadrotor 6-DOF dynamics, rotor thrust and torque allocation, cascaded flight control, geometric control on SE(3), MPC, PX4, ROS 2, MAVLink, uXRCE-DDS, VIO, GPS-denied navigation, inspection planning, Remote ID, and SITL-to-hardware progression.
- Kinematic and dynamic bicycle models, tire limits, route planning, behavior planning, local trajectory optimization, MPC, CARLA, CommonRoad, ScenarioRunner, OpenSCENARIO, nuScenes, Waymo Open Dataset, SOTIF-style safety reasoning, and scenario coverage structure.

## Agent And Skill Coverage

- Used `book-update` and `book-writers` skill instructions.
- Applied the book-skills 42-agent quality matrix to the added sections: curriculum, deep explanation, examples, code pedagogy, visual learning, exercises, fact integrity, bibliography, cross-references, callouts, style, publication QA, controller-style audit, and illustrator gate.
- Used three web-researcher agents for live scouting:
  - humanoid whole-body control and loco-manipulation
  - advanced aerial robotics and drone autonomy
  - autonomous driving systems and safety validation
- Ran the real illustrator phase from the main context with Gemini image generation.

## New Raster Illustrations

- `part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/images/chapter-46-illustration-08.png`
- `part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/images/chapter-46-illustration-09.png`
- `part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/images/chapter-47-illustration-06.png`
- `part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/images/chapter-47-illustration-07.png`
- `part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/images/chapter-48-illustration-07.png`
- `part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/images/chapter-48-illustration-08.png`

All six illustrations were generated as raster PNG files and embedded into their matching section pages.

## Verification

`scripts/audit_html_book.py` result:

- html_files: 461
- chapter_files: 60
- section_files: 369
- links_checked: 9777
- missing_links: 0
- banned_hits: 0
- required_failures: 0
- bibliography_markup_failures: 0

## Main Sources Used

- Boston Dynamics Atlas: https://bostondynamics.com/products/atlas/
- Boston Dynamics and RAI Institute partnership: https://bostondynamics.com/news/boston-dynamics-and-the-robotics-ai-institute-partner/
- Boston Dynamics Large Behavior Models: https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/
- MIT Underactuated Robotics humanoids: https://underactuated.mit.edu/humanoids.html
- Drake: https://drake.mit.edu/
- NVIDIA Isaac Lab whole-body control update: https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/
- HumanoidBench: https://humanoid-bench.github.io/
- PX4: https://docs.px4.io/main/en/
- PX4 ROS 2 guide: https://docs.px4.io/main/en/ros2/user_guide
- PX4 controller diagrams: https://docs.px4.io/main/en/flight_stack/controller_diagrams
- MAVLink: https://mavlink.io/en/
- Geometric quadrotor control: https://arxiv.org/abs/1003.2005
- Minimum-snap trajectory generation: https://doi.org/10.1109/ICRA.2011.5980409
- FAA Remote ID: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-89
- CARLA: https://carla.org/
- CARLA ScenarioRunner: https://scenario-runner.readthedocs.io/en/latest/
- CommonRoad: https://commonroad.in.tum.de/
- ASAM OpenSCENARIO: https://report.asam.net/asam-openscenario
- nuScenes: https://www.nuscenes.org/nuscenes
- Waymo Open Dataset: https://waymo.com/open/
- ISO 21448:2022 SOTIF: https://www.iso.org/standard/77490.html
