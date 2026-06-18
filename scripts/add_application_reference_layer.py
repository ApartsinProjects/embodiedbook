from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SECTIONS = [
    {
        "chapter": "29",
        "section": "8",
        "part": "Part VI: Embodied Perception",
        "part_dir": "part-6-embodied-perception",
        "module": "module-29-localization-and-mapping-slam",
        "chapter_title": "Localization and Mapping (SLAM)",
        "title": "Modern SLAM Systems And Failure Modes",
        "prev_href": "section-29.7.html",
        "prev_label": "Section 29.7: Map uncertainty",
        "next_href": "../module-30-navigation-and-path-planning/index.html",
        "next_label": "Chapter 30: Navigation and Path Planning",
        "domain": "field SLAM",
        "thesis": "Modern SLAM is no longer one algorithm. It is a contract among inertial sensing, visual or lidar front ends, factor-graph optimization, map maintenance, semantic structure, and failure replay.",
        "formula": r"r_{ij}(x_i,x_j,z_{ij})=\left\|z_{ij}^{-1}(x_i^{-1}x_j)\right\|_{\Sigma_{ij}^{-1}}^2",
        "tools": "ORB-SLAM3, OpenVINS, Kimera, Kimera-Multi, GTSAM, ROS 2, Open3D",
        "failure_modes": "low texture, repetitive geometry, motion blur, rolling shutter, magnetic disturbance, lidar dust, time synchronization drift, loop-closure aliasing, and relocalization failure",
        "scenario": "an inspection robot enters a dim warehouse aisle, loses texture on glossy walls, sees repeated shelving, then must decide whether to slow down, switch to inertial propagation, request a new viewpoint, or return to the last confident keyframe",
        "lab": "replay one EuRoC-style visual-inertial segment, inject timestamp offsets, and compare trajectory error, loop-closure acceptance, and recovery labels in one manifest",
        "sources": [
            ("ORB-SLAM3", "https://arxiv.org/abs/2007.11898", "Reference for modern visual, visual-inertial, and multi-map SLAM."),
            ("OpenVINS", "https://docs.openvins.com/", "Maintained visual-inertial estimation stack for inspectable filter-based pipelines."),
            ("Kimera", "https://github.com/MIT-SPARK/Kimera", "Metric-semantic SLAM system connecting geometry, factors, and scene understanding."),
            ("Kimera-Multi", "https://github.com/MIT-SPARK/Kimera-Multi", "Multi-robot mapping reference for distributed SLAM constraints."),
            ("EuRoC MAV Dataset", "https://projects.asl.ethz.ch/datasets/euroc-mav/", "Common benchmark for visual-inertial SLAM and estimator debugging."),
            ("TartanAir", "https://theairlab.org/tartanair-dataset/", "Synthetic visual navigation dataset with diverse environments and ground truth."),
        ],
    },
    {
        "chapter": "30",
        "section": "7",
        "part": "Part VI: Embodied Perception",
        "part_dir": "part-6-embodied-perception",
        "module": "module-30-navigation-and-path-planning",
        "chapter_title": "Navigation and Path Planning",
        "title": "Field Navigation Under Degraded Sensing",
        "prev_href": "section-30.6.html",
        "prev_label": "Section 30.6: Language-goal navigation",
        "next_href": "../../part-7-language-vision-and-action/module-31-language-guided-embodied-agents/index.html",
        "next_label": "Chapter 31: Language-Guided Embodied Agents",
        "domain": "field navigation",
        "thesis": "Navigation under degraded sensing is a risk-managed control problem: the robot must reason about map confidence, local traversability, fallback policies, and when not to continue.",
        "formula": r"J(\pi)=\mathbb{E}\sum_t c(x_t,u_t)+\lambda_r R(x_t)+\lambda_b B(b_t)",
        "tools": "ROS 2 Nav2, Behavior Trees, OpenVINS, ORB-SLAM3, Kimera, Habitat, TartanAir",
        "failure_modes": "smoke, dust, darkness, specular floors, dynamic obstacles, wheel slip, GPS denial, map aging, and blocked recovery behaviors",
        "scenario": "a search robot moves through a tunnel where lidar returns are sparse, vision is intermittently blinded, and the safest action may be to hold position until a confidence monitor recovers",
        "lab": "run the same route with normal sensing, delayed sensing, and sparse sensing; record path cost, intervention count, near-miss distance, recovery behavior, and mission outcome",
        "sources": [
            ("DARPA Subterranean Challenge", "https://www.darpa.mil/research/challenges/subterranean", "Field robotics challenge that exposed degraded perception and navigation failure modes."),
            ("ROS 2 Navigation", "https://navigation.ros.org/", "Maintained navigation stack for planners, controllers, behavior trees, and recovery behaviors."),
            ("TartanAir", "https://theairlab.org/tartanair-dataset/", "Dataset useful for testing visual navigation under diverse appearance conditions."),
            ("Habitat 3.0", "https://aihabitat.org/habitat3/", "Interactive embodied AI simulator for navigation and collaboration scenarios."),
        ],
    },
    {
        "chapter": "34",
        "section": "9",
        "part": "Part VII: Language, Vision, and Action",
        "part_dir": "part-7-language-vision-and-action",
        "module": "module-34-vision-language-action-models",
        "chapter_title": "Vision-Language-Action Models",
        "title": "Action Representations In VLA Systems",
        "prev_href": "section-34.8.html",
        "prev_label": "Section 34.8: Evaluating VLA models",
        "next_href": "../module-35-robot-foundation-models-and-cross-embodiment-learning/index.html",
        "next_label": "Chapter 35: Robot Foundation Models and Cross-Embodiment Learning",
        "domain": "vision-language-action systems",
        "thesis": "The action representation is the robot-facing API of a VLA. Tokenized actions, continuous heads, action chunks, diffusion trajectories, and hierarchical skills make different promises about latency, control authority, and safety.",
        "formula": r"a_{t:t+H}=g_\theta(o_{\leq t}, q, h_t), \quad u_t=\kappa(a_t,x_t)",
        "tools": "OpenVLA, Octo, RT-X, LeRobot, Diffusion Policy, ACT, ROS 2 control",
        "failure_modes": "action-token aliasing, proprioception mismatch, calibration drift, delayed cameras, action chunk latency, out-of-range gripper commands, and hidden controller saturation",
        "scenario": "a table-top robot receives a language instruction, predicts a chunk of future end-effector poses, and must hand each pose to a lower-level controller that enforces collision and force limits",
        "lab": "compare discrete action tokens, continuous deltas, and action chunks on one pick-and-place task, then report task success, latency, recovery rate, and controller saturation",
        "sources": [
            ("RT-2", "https://arxiv.org/abs/2307.15818", "Vision-language-action model connecting web-scale vision-language learning to robot actions."),
            ("Open X-Embodiment and RT-X", "https://robotics-transformer-x.github.io/", "Cross-embodiment dataset and model family for robot learning."),
            ("OpenVLA", "https://arxiv.org/abs/2406.09246", "Open vision-language-action model reference."),
            ("Octo", "https://arxiv.org/abs/2405.12213", "Generalist robot policy architecture using large-scale robot data."),
            ("LeRobot", "https://huggingface.co/docs/lerobot/en/index", "Practical open-source stack for datasets, imitation learning, and policy evaluation."),
        ],
    },
    {
        "chapter": "35",
        "section": "8",
        "part": "Part VII: Language, Vision, and Action",
        "part_dir": "part-7-language-vision-and-action",
        "module": "module-35-robot-foundation-models-and-cross-embodiment-learning",
        "chapter_title": "Robot Foundation Models and Cross-Embodiment Learning",
        "title": "Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models",
        "prev_href": "section-35.7.html",
        "prev_label": "Section 35.7: Open problems in robot foundation models",
        "next_href": "../../part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/index.html",
        "next_label": "Chapter 36: Predicting the Future",
        "domain": "robot foundation models",
        "thesis": "An open robot foundation model becomes useful only after the builder controls data cards, camera calibration, action normalization, latency, rollback, and paired evaluations.",
        "formula": r"\Delta=\operatorname{Eval}(M_{\theta+\phi},D_{\text{heldout}},S)-\operatorname{Eval}(M_{\theta},D_{\text{heldout}},S)",
        "tools": "LeRobot, OpenVLA, Octo, RT-X datasets, DROID, LIBERO, Hugging Face Hub, ONNX Runtime",
        "failure_modes": "dataset leakage, embodiment mismatch, stale calibration, train-serving skew, quantization drift, policy latency, unsafe recovery, and benchmark overfitting",
        "scenario": "a team fine-tunes an open VLA for a new gripper and discovers that action normalization, camera extrinsics, and controller update rate matter as much as model size",
        "lab": "fine-tune a small policy with a dataset card, serve it with a latency budget, and compare baseline and adapted policies on the same held-out scenario panel",
        "sources": [
            ("LeRobot", "https://huggingface.co/docs/lerobot/en/index", "Open toolkit for robot learning datasets, policies, and evaluation."),
            ("OpenVLA", "https://arxiv.org/abs/2406.09246", "Open VLA model useful for adaptation and serving discussions."),
            ("DROID", "https://droid-dataset.github.io/", "Large in-the-wild robot manipulation dataset."),
            ("LIBERO", "https://libero-project.github.io/main.html", "Benchmark suite for lifelong robot learning and policy evaluation."),
            ("NVIDIA GR00T N1", "https://arxiv.org/abs/2503.14734", "Humanoid foundation model reference for cross-embodiment behavior learning."),
        ],
    },
    {
        "chapter": "42",
        "section": "7",
        "part": "Part IX: Manipulation, Locomotion, and Embodied Skills",
        "part_dir": "part-9-manipulation-locomotion-and-embodied-skills",
        "module": "module-42-robotic-manipulation",
        "chapter_title": "Robotic Manipulation",
        "title": "Mobile Manipulation: Base, Arm, Perception, And Recovery",
        "prev_href": "section-42.6.html",
        "prev_label": "Section 42.6: Manipulation benchmarks",
        "next_href": "../module-43-grasping-and-dexterous-manipulation/index.html",
        "next_label": "Chapter 43: Grasping and Dexterous Manipulation",
        "domain": "mobile manipulation",
        "thesis": "Mobile manipulation is not navigation plus grasping pasted together. The base pose changes reachability, the arm changes balance and clearance, and perception must support both route choice and contact execution.",
        "formula": r"\min_{q_b,q_a,g} C_{\text{nav}}(q_b)+C_{\text{reach}}(q_b,q_a,g)+C_{\text{risk}}",
        "tools": "MoveIt, ROS 2 Nav2, Behavior Trees, Habitat 3.0, BEHAVIOR-1K, RoboCasa, ManiSkill, Mobile ALOHA",
        "failure_modes": "unreachable grasps, base-arm collision, door-handle ambiguity, deformable objects, blocked drawers, long-horizon drift, and recovery loops that repeat the same failed grasp",
        "scenario": "a household robot navigates to a cabinet, opens a door, grasps a mug, carries it to another room, and recovers when the first grasp slips",
        "lab": "build a mobile-manipulation task card with route, base pose, reachability map, grasp set, force limit, recovery branch, and logged failure replay",
        "sources": [
            ("BEHAVIOR-1K", "https://behavior.stanford.edu/index.html", "Household activity benchmark emphasizing long-horizon embodied tasks."),
            ("RoboCasa", "https://robocasa.ai/", "Simulation benchmark for everyday manipulation in rich household scenes."),
            ("Habitat 3.0", "https://aihabitat.org/habitat3/", "Simulator for embodied agents in interactive environments."),
            ("ManiSkill", "https://maniskill.readthedocs.io/en/latest/user_guide/index.html", "Robot manipulation benchmark and simulator with mobile manipulation tasks."),
            ("Mobile ALOHA", "https://arxiv.org/abs/2401.02117", "Mobile bimanual manipulation system using whole-body teleoperation data."),
        ],
    },
    {
        "chapter": "47",
        "section": "8",
        "part": "Part IX: Manipulation, Locomotion, and Embodied Skills",
        "part_dir": "part-9-manipulation-locomotion-and-embodied-skills",
        "module": "module-47-drones-and-aerial-embodied-ai",
        "chapter_title": "Drones and Aerial Embodied AI",
        "title": "PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence",
        "prev_href": "section-47.7.html",
        "prev_label": "Section 47.7: Trajectory generation and GPS-denied missions",
        "next_href": "../module-48-autonomous-driving-as-embodied-ai/section-48.1.html",
        "next_label": "Section 48.1: Driving as perception, prediction, planning, control",
        "domain": "aerial robotics deployment",
        "thesis": "The PX4-to-hardware path is an evidence ladder: software-in-the-loop, hardware-in-the-loop, parameter review, log replay, controlled flight test, and operational risk case.",
        "formula": r"e_{\text{flight}}=(x_{\text{cmd}}-x_{\text{est}}, u, p, w, f_{\text{failsafe}}, \ell_{\text{log}})",
        "tools": "PX4, QGroundControl, MAVLink, MAVSDK, ROS 2 uXRCE-DDS, Flight Review, Gazebo",
        "failure_modes": "bad parameters, frame sign errors, vibration, EKF divergence, magnetometer interference, motor imbalance, battery sag, payload shift, wind gusts, and companion-computer latency",
        "scenario": "a quadrotor inspection stack graduates from SITL to HITL, then a short outdoor hover test reveals vibration-induced estimator innovation spikes",
        "lab": "create a flight-test evidence package with SITL run, HITL checklist, parameter diff, log review, failsafe test, and one post-flight mitigation",
        "sources": [
            ("PX4 Documentation", "https://docs.px4.io/main/en/", "Official autopilot documentation for simulation, parameters, estimators, and flight modes."),
            ("PX4 ROS 2 Guide", "https://docs.px4.io/main/en/ros2/user_guide", "Official ROS 2 bridge guide for uXRCE-DDS integration."),
            ("MAVLink", "https://mavlink.io/en/", "Messaging protocol used for vehicle telemetry and companion-computer interfaces."),
            ("MAVSDK", "https://mavsdk.mavlink.io/main/en/", "SDK for programmatic drone control and telemetry."),
            ("EASA SORA", "https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-drones/specific-operations-risk-assessment-sora", "Operational risk assessment framework for drone operations."),
        ],
    },
    {
        "chapter": "48",
        "section": "9",
        "part": "Part IX: Manipulation, Locomotion, and Embodied Skills",
        "part_dir": "part-9-manipulation-locomotion-and-embodied-skills",
        "module": "module-48-autonomous-driving-as-embodied-ai",
        "chapter_title": "Autonomous Driving as Embodied AI",
        "title": "Closed-Loop Driving Evaluation And Safety Assurance",
        "prev_href": "section-48.8.html",
        "prev_label": "Section 48.8: Route, behavior, and scenario-based planning",
        "next_href": "../../part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/index.html",
        "next_label": "Chapter 49: Multi-Agent Embodied AI",
        "domain": "autonomous driving assurance",
        "thesis": "Driving evaluation must distinguish open-loop prediction skill from closed-loop driving behavior. A planner that predicts well can still intervene too late, negotiate poorly, or violate the operating design domain.",
        "formula": r"S=\{ODD,\mathcal{X}_{0:T},A_{0:T},M_{\text{safety}},E_{\text{evidence}}\}",
        "tools": "CARLA Leaderboard, nuPlan, Waymo Open Dataset, Waymo Sim Agents, CommonRoad, ASAM OpenSCENARIO, OpenDRIVE",
        "failure_modes": "distribution shift, interaction deadlock, planner-induced near misses, metric gaming, scenario overfitting, ODD creep, sensor degradation, and missing safety-case defeaters",
        "scenario": "an autonomous vehicle passes open-loop prediction tests but in closed-loop simulation brakes late when a merging vehicle negotiates differently from the log",
        "lab": "take one scenario family, compute prediction metrics and closed-loop outcomes on the same panel, then write the safety argument and the strongest defeater",
        "sources": [
            ("SAE J3016", "https://www.sae.org/standards/j3016_202104-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles", "Taxonomy for driving automation levels and operational concepts."),
            ("ISO 21448 SOTIF", "https://www.iso.org/standard/77490.html", "Safety of the intended functionality reference."),
            ("UL 4600 overview", "https://users.ece.cmu.edu/~koopman/ul4600/index.html", "Assurance standard overview for autonomous products."),
            ("ASAM OpenSCENARIO XML", "https://www.asam.net/standards/detail/openscenario-xml/", "Scenario description standard for driving simulation and testing."),
            ("CARLA Leaderboard", "https://leaderboard.carla.org/", "Closed-loop autonomous driving evaluation benchmark."),
            ("nuPlan", "https://www.nuplan.org/nuplan", "Planning benchmark and simulator for autonomous driving research."),
        ],
    },
    {
        "chapter": "54",
        "section": "7",
        "part": "Part XI: Evaluation, Safety, Robustness, and Deployment",
        "part_dir": "part-11-evaluation-safety-robustness-and-deployment",
        "module": "module-54-safety-in-embodied-ai",
        "chapter_title": "Safety in Embodied AI",
        "title": "Safety Cases And Assurance Arguments For Embodied AI",
        "prev_href": "section-54.6.html",
        "prev_label": "Section 54.6: Deployment approval and safety cases",
        "next_href": "../module-55-deployment-architecture/index.html",
        "next_label": "Chapter 55: Deployment Architecture",
        "domain": "safety assurance",
        "thesis": "A safety case is a structured argument that the embodied system is acceptably safe for a defined operating domain, backed by evidence and challenged by explicit defeaters.",
        "formula": r"\text{Assurance}=(C,G,E,D,R)",
        "tools": "hazard logs, ODD cards, runtime assurance monitors, CBFs, RSS-style rules, incident replay, UL 4600-style arguments",
        "failure_modes": "undefined operating domain, untested fallback, stale evidence, missing human override path, unowned hazards, weak incident response, and claims not tied to logs",
        "scenario": "a learned warehouse robot policy is wrapped by a runtime monitor, then its safety case ties speed limits, human-zone rules, perception confidence, and incident replay to one evidence package",
        "lab": "write one assurance argument with claims, goals, evidence, defeaters, and residual risk for a learned policy deployed in a constrained robot workspace",
        "sources": [
            ("ISO 21448 SOTIF", "https://www.iso.org/standard/77490.html", "Reference for performance limitations and intended-functionality hazards."),
            ("UL 4600 overview", "https://users.ece.cmu.edu/~koopman/ul4600/index.html", "Assurance framing for autonomous products."),
            ("UNECE R157", "https://unece.org/transport/documents/2021/03/standards/un-regulation-no-157-automated-lane-keeping-systems-alks", "Automated lane keeping regulation reference."),
            ("NHTSA VSSA", "https://www.nhtsa.gov/automated-driving-systems/voluntary-safety-self-assessment", "Voluntary safety self-assessment reference for ADS developers."),
            ("FAA Remote ID", "https://www.faa.gov/uas/getting_started/remote_id", "Drone identification requirement reference."),
        ],
    },
    {
        "chapter": "55",
        "section": "6",
        "part": "Part XI: Evaluation, Safety, Robustness, and Deployment",
        "part_dir": "part-11-evaluation-safety-robustness-and-deployment",
        "module": "module-55-deployment-architecture",
        "chapter_title": "Deployment Architecture",
        "title": "Industrial Fleets, Open-RMF, AMR Interoperability, And Operations",
        "prev_href": "section-55.5.html",
        "prev_label": "Section 55.5: Failure recovery, security, maintenance",
        "next_href": "../../part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/index.html",
        "next_label": "Chapter 56: Embodied Agents with Memory",
        "domain": "industrial fleet robotics",
        "thesis": "Industrial embodied AI is a fleet operations problem: maps, missions, elevators, docks, chargers, safety zones, WMS or MES events, maintenance, and incident replay must form one deployable architecture.",
        "formula": r"KPI=(\text{throughput},\text{uptime},\text{interventions},\text{safety events},\text{SLA})",
        "tools": "Open-RMF, MassRobotics AMR Interoperability, ROS-Industrial, WMS and MES bridges, ISO 3691-4, ANSI/RIA R15.08",
        "failure_modes": "traffic deadlock, map drift, charger contention, pallet pose ambiguity, blocked dock doors, mixed human zones, elevator integration failure, and telemetry gaps",
        "scenario": "a warehouse fleet coordinates AMRs and autonomous forklifts across receiving, putaway, replenishment, picking, packing, and dock operations while preserving safety evidence",
        "lab": "design a fleet dashboard that computes throughput, intervention rate, congestion, charger use, localization drift, and safety events from one robot log artifact",
        "sources": [
            ("Open-RMF", "https://www.open-rmf.org/", "Open fleet orchestration framework for multi-robot facilities."),
            ("MassRobotics AMR Interoperability Standard", "https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/", "Reference for cross-vendor AMR status and command interoperability."),
            ("ROS-Industrial", "https://rosindustrial.org/", "Industrial robotics software ecosystem."),
            ("ISO 3691-4", "https://www.iso.org/standard/70660.html", "Safety standard for driverless industrial trucks and systems."),
            ("ANSI/RIA R15.08", "https://webstore.ansi.org/standards/ria/ansiriar15082020", "Industrial mobile robot safety standard reference."),
            ("NIST ARIAC", "https://www.nist.gov/el/intelligent-systems-division-73500/agile-robotics-industrial-automation-competition", "Agile robotics benchmark for industrial automation tasks."),
        ],
    },
    {
        "chapter": "59",
        "section": "12",
        "part": "Part XII: Frontiers, Capstones, and Course Design",
        "part_dir": "part-12-frontiers-capstones-and-course-design",
        "module": "module-59-capstone-projects",
        "chapter_title": "Capstone Projects",
        "title": "Application Track Capstone Templates",
        "prev_href": "section-59.11.html",
        "prev_label": "Section 59.11: Open-ended research project",
        "next_href": "../module-60-teaching-with-this-book/index.html",
        "next_label": "Chapter 60: Teaching with This Book",
        "domain": "research and builder capstones",
        "thesis": "A capstone becomes a research-grade embodied AI project when it has an application track, a starter stack, an evidence panel, a safety constraint, and a reproducibility card.",
        "formula": r"P=(O,A,S,M,E,R)",
        "tools": "Isaac Lab, MuJoCo, CARLA, CommonRoad, PX4 SITL, Habitat 3.0, ManiSkill, ROS-Industrial, Open-RMF, LeRobot",
        "failure_modes": "oversized scope, missing baseline, simulator-only claims, unpaired metrics, vague safety constraints, and missing artifact cards",
        "scenario": "a reader chooses one of ten application tracks, builds a small system, and submits the same evidence package format used by the rest of the book",
        "lab": "select one application track and fill objective, assumptions, stack, metrics, safety constraints, evidence artifacts, and grading rubric before writing code",
        "sources": [
            ("Isaac Lab", "https://isaac-sim.github.io/IsaacLab/", "Simulation and robot-learning platform for capstone projects."),
            ("MuJoCo Playground", "https://playground.mujoco.org/", "Reference for fast embodied control experimentation."),
            ("CARLA", "https://carla.org/", "Autonomous driving simulator for closed-loop driving capstones."),
            ("PX4", "https://docs.px4.io/main/en/", "Autopilot and simulation stack for aerial robotics projects."),
            ("RobotPerf", "https://arxiv.org/abs/2309.09212", "Benchmarking reference for robot computing performance."),
        ],
    },
]


FRONT_MATTER = ROOT / "front-matter"


def section_path(item):
    return ROOT / item["part_dir"] / item["module"] / f'section-{item["chapter"]}.{item["section"]}.html'


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def source_cards(sources):
    return "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{esc(name)}. <a href="{url}" rel="noopener" target="_blank">{url}</a></p><p class="bib-annotation">{esc(note)}</p></div>'
        for name, url, note in sources
    )


def section_page(item):
    num = f'{item["chapter"]}.{item["section"]}'
    img = f'images/chapter-{item["chapter"]}-application-reference-{item["section"]}.png'
    return f'''<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Section {num} of Building Embodied AI: From Perception to Autonomous Action: {esc(item["title"])}." name="description"/>
<title>Section {num}: {esc(item["title"])} | Building Embodied AI: From Perception to Autonomous Action</title>
<link href="../../styles/book.css" rel="stylesheet"/>
<link href="../../styles/pygments.css" rel="stylesheet"/>
<link href="../../vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer="" src="../../vendor/prism/prism-bundle.min.js"></script>
<link href="../../vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer="" src="../../vendor/katex/katex.min.js"></script>
<script defer="" onload="renderMathInElement(document.body, {{
  delimiters: [
  {{left: '$$', right: '$$', display: true}},
  {{left: '$', right: '$', display: false}}
  ],
  throwOnError: false
  }});" src="../../vendor/katex/contrib/auto-render.min.js"></script>
<script defer="" src="../../scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../../index.html">Building Embodied AI: From Perception to Autonomous Action</a>
<a class="toc-link" href="../../toc.html" title="Table of Contents"><span class="toc-icon">☰</span> Contents</a>
</nav>
<div class="header-search"><div id="search"></div></div>
<div class="part-label"><a href="../index.html">{esc(item["part"])}</a></div>
<div class="chapter-label"><a href="index.html">Chapter {item["chapter"]}: {esc(item["chapter_title"])}</a></div>
<h1>Section {num}: {esc(item["title"])}</h1>
</header>
<main class="content" id="main-content">
<blockquote class="epigraph"><p>"A field robot is a theory with motors, logs, limits, and consequences."</p><cite>A Systems-Minded Embodied AI Agent</cite></blockquote>
<div class="callout big-picture"><div class="callout-title">Big Picture</div><p>{esc(item["thesis"])}</p></div>
<figure class="illustration" id="fig-{item["chapter"]}-{item["section"]}-application-reference">
<img alt="{esc(item["title"])} conceptual illustration" src="{img}"/>
<figcaption><strong>Figure {num}.1</strong>: A field-facing mental model for {esc(item["domain"])}. The illustration connects sensing, state, planning, control, safety, and evidence logging.</figcaption>
</figure>
<h2>Why This Section Was Added</h2>
<p>This application layer closes the gap between textbook breadth and the daily needs of researchers and builders. In {esc(item["domain"])}, the core question is not whether one component scores well in isolation. The question is whether the system produces an action, a safety boundary, and an evidence artifact that another team can inspect.</p>
<p>The central contract is compact: define the operating domain, name the state variables, state the action interface, identify the safety monitor, and save the log that proves what happened. Every serious embodied system eventually becomes this contract, whether it is a drone, an autonomous vehicle, a humanoid, a mobile manipulator, an industrial fleet, or a simulator-first research platform.</p>
<div class="callout key-insight"><div class="callout-title">System Contract Before Model Choice</div><p>Choose the model after the evidence contract is clear. A stronger model cannot rescue missing calibration, unclear frames, unbounded actions, stale maps, or metrics computed on incompatible scenario panels.</p></div>
<h2>Technical Core</h2>
<p>For this section, the working mathematical object is:</p>
<p>$${item["formula"]}.$$</p>
<p>The notation is intentionally a system contract rather than a single loss function. It ties the learned or planned output to state, action, environment constraints, and the measured evidence. A leading researcher can replace the simple expression with a detailed estimator, controller, simulator, or assurance argument without changing the structure of the artifact.</p>
<figure class="technical-figure" id="fig-{item["chapter"]}-{item["section"]}-block-diagram">
<svg aria-labelledby="fig-{item["chapter"]}-{item["section"]}-title fig-{item["chapter"]}-{item["section"]}-desc" role="img" viewbox="0 0 860 330">
<title id="fig-{item["chapter"]}-{item["section"]}-title">{esc(item["title"])} system block diagram</title>
<desc id="fig-{item["chapter"]}-{item["section"]}-desc">A block diagram showing sensing, estimation, planning, control, safety monitoring, and logged evidence.</desc>
<rect fill="#e3f2fd" height="76" rx="8" stroke="#1565c0" width="125" x="28" y="78"></rect>
<text font-size="14" text-anchor="middle" x="90" y="109">Sensing</text>
<text font-size="12" text-anchor="middle" x="90" y="130">time, frames</text>
<rect fill="#e8f5e9" height="76" rx="8" stroke="#2e7d32" width="130" x="188" y="78"></rect>
<text font-size="14" text-anchor="middle" x="253" y="109">State</text>
<text font-size="12" text-anchor="middle" x="253" y="130">belief, map</text>
<rect fill="#fff3e0" height="76" rx="8" stroke="#e65100" width="130" x="353" y="78"></rect>
<text font-size="14" text-anchor="middle" x="418" y="109">Planning</text>
<text font-size="12" text-anchor="middle" x="418" y="130">task, route</text>
<rect fill="#f3e5f5" height="76" rx="8" stroke="#6a1b9a" width="130" x="518" y="78"></rect>
<text font-size="14" text-anchor="middle" x="583" y="109">Control</text>
<text font-size="12" text-anchor="middle" x="583" y="130">limits, rates</text>
<rect fill="#fce4ec" height="76" rx="8" stroke="#c62828" width="135" x="683" y="78"></rect>
<text font-size="14" text-anchor="middle" x="750" y="109">Safety</text>
<text font-size="12" text-anchor="middle" x="750" y="130">monitor, stop</text>
<path d="M153 116 H188 M318 116 H353 M483 116 H518 M648 116 H683" stroke="#555" stroke-width="2"></path>
<rect fill="#f8fafc" height="62" rx="8" stroke="#607d8b" width="650" x="105" y="222"></rect>
<text font-size="14" text-anchor="middle" x="430" y="249">Evidence artifact: config, log, metric, failure label, and replay case</text>
<text font-size="12" text-anchor="middle" x="430" y="269">All compared numbers must be produced on one scenario panel with one metric script.</text>
<path d="M750 154 C750 205 430 205 430 222" fill="none" stroke="#607d8b" stroke-dasharray="6 5" stroke-width="2"></path>
</svg>
<figcaption><strong>Figure {num}.2</strong>: The section-level block diagram shows where models, controllers, safety monitors, and evidence artifacts meet.</figcaption>
</figure>
<div class="callout algorithm"><div class="callout-title">Algorithm: Application Evidence Loop</div><ol>
<li>Define the operating domain, robot interface, state variables, and safety constraints.</li>
<li>Choose one scenario panel and keep it fixed while comparing baselines and shortcuts.</li>
<li>Run the hand-built baseline and the maintained tool path on the same configuration.</li>
<li>Save logs, metrics, latency, failure labels, and replay artifacts in one manifest.</li>
<li>Promote the method only if the action, safety boundary, or recovery behavior improves.</li>
</ol></div>
<h2>Practical Stack</h2>
<p>The practical tool stack for this section is: <strong>{esc(item["tools"])}</strong>. The teaching path should start with a small inspectable baseline, then shift to maintained libraries once the mechanism is clear. The shortcut is valuable because it handles optimized kernels, standard data formats, timing integration, visualization, and deployment hooks that hand code usually handles poorly.</p>
<div class="comparison-table"><div class="comparison-table-title">Application-Grade Design Checklist</div><table><thead><tr><th>Layer</th><th>What To Specify</th><th>Evidence To Save</th></tr></thead><tbody>
<tr><td>Operating domain</td><td>Environment, weather or scene limits, human zones, task envelope, and excluded cases.</td><td>ODD card or site card.</td></tr>
<tr><td>State and actions</td><td>Frames, units, rates, uncertainty, command limits, and fallback behavior.</td><td>Interface manifest and sample logs.</td></tr>
<tr><td>Evaluation</td><td>Scenario panel, metric code, seeds, perturbations, and failure taxonomy.</td><td>One construct-matched result artifact.</td></tr>
<tr><td>Deployment</td><td>Monitoring, incident response, rollback, calibration checks, and maintenance cadence.</td><td>Safety case, incident report, and replay case.</td></tr>
</tbody></table></div>
<div class="callout warning"><div class="callout-title">Failure Modes To Test</div><p>Stress the system with {esc(item["failure_modes"])}. These are not edge-case decorations. They are the normal conditions that separate a publishable demo from a deployable embodied system.</p></div>
<div class="callout practical-example"><div class="callout-title">Practical Example</div><p>Consider {esc(item["scenario"])}. A useful implementation logs the observation stream, state estimate, chosen action, safety monitor status, controller status, and post-event recovery. That log keeps the team from blaming the model when the true fault is calibration, timing, planning, control, or evaluation.</p></div>
<pre><code class="language-python"># Build one application evidence card for Section {num}.
from dataclasses import dataclass, asdict

@dataclass
class ApplicationEvidence:
    section: str
    operating_domain: str
    state_action_contract: str
    tool_stack: str
    perturbation: str
    metric: str
    replay_artifact: str

card = ApplicationEvidence(
    section="{num}",
    operating_domain="{esc(item["domain"])}",
    state_action_contract="frames, units, rates, limits, safety monitor",
    tool_stack="{esc(item["tools"])}",
    perturbation="{esc(item["failure_modes"].split(",")[0])}",
    metric="same-panel task success plus safety and recovery labels",
    replay_artifact="config, log, metric output, and failure case",
)
print(asdict(card))</code></pre>
<div class="code-caption">Code Fragment {num}.1 creates an `ApplicationEvidence` card for {esc(item["domain"])} with operating domain, interface, tool stack, perturbation, metric, and replay artifact.</div>
<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>The hand-built evidence card is only a few lines, but production work should let {esc(item["tools"])} handle standard interfaces, logs, simulators, controllers, and visualizers. The reduction is from dozens of fragile glue-code lines to a maintained stack plus one manifest, while preserving the evidence schema.</p></div>
<h2>Recipe For Builders</h2>
<ol>
<li>Write the operating-domain card before training, tuning, or route planning.</li>
<li>Choose a baseline that is simple enough to debug by eye.</li>
<li>Add the maintained tool path and keep the output schema identical.</li>
<li>Run one nominal case, one degraded-sensing case, one recovery case, and one safety-boundary case.</li>
<li>Ship the result only with logs, configuration, metric code, and a replayable failure case.</li>
</ol>
<div class="callout self-check"><div class="callout-title">Self Check</div><p>Can you state the operating domain, state variables, action interface, safety monitor, perturbation, and replay artifact for {esc(item["domain"])} without opening another file? If not, the system is not yet specified.</p></div>
<div class="callout research-frontier"><div class="callout-title">Research Frontier</div><p>The frontier is moving toward open robot foundation models, large-scale simulators, richer datasets, formal safety cases, and fleet telemetry. The durable research contribution is the evidence loop that connects those pieces without hiding assumptions.</p></div>
<div class="callout key-takeaway"><div class="callout-title">Key Takeaway</div><p>{esc(item["title"])} belongs in the book because it turns an application domain into a reproducible embodied AI build path: theory, tool stack, scenario panel, safety constraint, and replayable evidence.</p></div>
<div class="callout exercise"><div class="callout-title">Exercise {num}.1</div><p>{esc(item["lab"])}. Submit the result as one evidence card, one metric artifact, and one failure replay note.</p></div>
<section class="bibliography"><h2>Section References</h2>
{source_cards(item["sources"])}
</section>
<nav class="chapter-nav">
<a class="prev" href="{item["prev_href"]}">{esc(item["prev_label"])}</a>
<a class="up" href="index.html">Chapter {item["chapter"]}: {esc(item["chapter_title"])}</a>
<a class="next" href="{item["next_href"]}">{esc(item["next_label"])}</a>
</nav>
<footer>
<p class="footer-title">Building Embodied AI: From Perception to Autonomous Action, Web Edition</p>
<p>© 2026 Alexander Apartsin &amp; Yehudit Aperstein · <a href="../../toc.html">Contents</a></p>
<p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
</footer>
</main>
</body>
</html>
'''


def front_matter_page():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Application reader pathways for Building Embodied AI: From Perception to Autonomous Action." name="description"/>
<title>Application Reader Pathways | Building Embodied AI: From Perception to Autonomous Action</title>
<link href="../styles/book.css" rel="stylesheet"/>
<script defer="" src="../scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../index.html">Building Embodied AI: From Perception to Autonomous Action</a>
<a class="toc-link" href="../toc.html" title="Table of Contents"><span class="toc-icon">☰</span> Contents</a>
</nav>
<div class="header-search"><div id="search"></div></div>
<div class="part-label">Front Matter</div>
<div class="chapter-label">F8 · Application Reader Pathways</div>
<h1>Application Reader Pathways</h1>
</header>
<main class="content" id="main-content">
<div class="callout big-picture"><div class="callout-title">Big Picture</div><p>This book can be read front to back, but application builders often need a direct route. Use these pathways when your goal is to build drones, autonomous vehicles, humanoids, mobile manipulators, industrial fleets, VLA systems, simulation-first policies, SLAM systems, safety cases, or research capstones.</p></div>
<p>Each pathway names the chapters to read, the sections to prioritize, and the artifact to produce. The common artifact is always the same: an operating-domain card, a state-action contract, a scenario panel, a safety boundary, a metric artifact, and a replayable failure case.</p>
<div class="comparison-table"><div class="comparison-table-title">Top Application Pathways</div><table><thead><tr><th>Application</th><th>Primary Chapters</th><th>Build Artifact</th></tr></thead><tbody>
<tr><td>Humanoid robots</td><td>5, 7, 8, 20, 21, 35, 45, 46, 54</td><td>Whole-body control trial with contact schedule and safety monitor.</td></tr>
<tr><td>Drones and aerial robots</td><td>8, 11, 13, 20, 29, 30, 47, 54</td><td>PX4 evidence ladder from SITL to flight log review.</td></tr>
<tr><td>Autonomous vehicles</td><td>5, 8, 13, 30, 36, 48, 52, 54</td><td>Closed-loop scenario panel with ODD and safety-case defeaters.</td></tr>
<tr><td>Mobile manipulation</td><td>30, 31, 34, 35, 42, 43, 44, 50</td><td>Route, reachability, grasp, and recovery task card.</td></tr>
<tr><td>Industrial fleets</td><td>30, 49, 52, 54, 55, 59</td><td>Fleet dashboard with throughput, interventions, congestion, and incidents.</td></tr>
<tr><td>VLA and robot foundation models</td><td>21, 25, 31, 32, 33, 34, 35, 58</td><td>Fine-tuning and serving card with calibration, latency, and rollback.</td></tr>
<tr><td>Simulation-first robot learning</td><td>9, 10, 11, 12, 13, 20, 36, 59</td><td>Sim-to-hardware reproducibility card with failure replay.</td></tr>
<tr><td>SLAM and navigation systems</td><td>27, 28, 29, 30, 47</td><td>Mapping and navigation manifest with degraded-sensing perturbations.</td></tr>
<tr><td>Safety-critical embodied AI</td><td>52, 53, 54, 55</td><td>Assurance argument with claims, evidence, defeaters, and residual risk.</td></tr>
<tr><td>Research platforms and capstones</td><td>56, 57, 58, 59, 60</td><td>Application-track capstone with reproducible metric artifact.</td></tr>
</tbody></table></div>
<div class="callout key-insight"><div class="callout-title">One Pattern, Many Bodies</div><p>The robot body changes the math and tools, but the engineering proof remains stable: define the domain, expose the interface, test the scenario panel, save the evidence, and explain the failure.</p></div>
<div class="callout practical-example"><div class="callout-title">How To Use The Map</div><p>A drone builder can start with Chapters 8, 29, 30, and 47, then use Chapter 54 for operational risk. A VLA builder can start with Chapters 21, 34, and 35, then use Chapter 55 for serving and Chapter 59 for a capstone template.</p></div>
<nav class="chapter-nav">
<a class="prev" href="look-inside-preview.html">Look Inside Preview</a>
<a class="up" href="../toc.html">Table of Contents</a>
<a class="next" href="copyright.html">Copyright and Legal</a>
</nav>
<footer>
<p class="footer-title">Building Embodied AI: From Perception to Autonomous Action, Web Edition</p>
<p>© 2026 Alexander Apartsin &amp; Yehudit Aperstein · <a href="../toc.html">Contents</a></p>
<p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {year:'numeric', month:'long', day:'numeric'}))</script></p>
</footer>
</main>
</body>
</html>
'''


def write_files():
    (FRONT_MATTER / "application-reader-pathways.html").write_text(front_matter_page(), encoding="utf-8")
    for item in SECTIONS:
        path = section_path(item)
        (path.parent / "images").mkdir(exist_ok=True)
        path.write_text(section_page(item), encoding="utf-8")


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"Missing expected text in {path}: {old[:120]}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def update_nav():
    pairs = [
        ("part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.7.html", '<a class="next" href="../module-30-navigation-and-path-planning/index.html">Chapter 30: Navigation and Path Planning</a>', '<a class="next" href="section-29.8.html">Section 29.8: Modern SLAM Systems And Failure Modes</a>'),
        ("part-6-embodied-perception/module-30-navigation-and-path-planning/section-30.6.html", '<a class="next" href="../../part-7-language-vision-and-action/module-31-language-guided-embodied-agents/index.html">Chapter 31: Language-Guided Embodied Agents</a>', '<a class="next" href="section-30.7.html">Section 30.7: Field Navigation Under Degraded Sensing</a>'),
        ("part-7-language-vision-and-action/module-34-vision-language-action-models/section-34.8.html", '<a class="next" href="../module-35-robot-foundation-models-and-cross-embodiment-learning/index.html">Chapter 35: Robot Foundation Models and Cross-Embodi...</a>', '<a class="next" href="section-34.9.html">Section 34.9: Action Representations In VLA Systems</a>'),
        ("part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.7.html", '<a class="next" href="../../part-8-world-models-and-model-based-embodied-ai/module-36-predicting-the-future/index.html">Chapter 36: Predicting the Future</a>', '<a class="next" href="section-35.8.html">Section 35.8: Serving, Fine-Tuning, And Evaluating Open Robot Foundation Models</a>'),
        ("part-9-manipulation-locomotion-and-embodied-skills/module-42-robotic-manipulation/section-42.6.html", '<a class="next" href="../module-43-grasping-and-dexterous-manipulation/index.html">Chapter 43: Grasping and Dexterous Manipulation</a>', '<a class="next" href="section-42.7.html">Section 42.7: Mobile Manipulation: Base, Arm, Perception, And Recovery</a>'),
        ("part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.7.html", '<a class="next" href="../module-48-autonomous-driving-as-embodied-ai/section-48.1.html">Section 48.1: Driving as perception, prediction, planning, control</a>', '<a class="next" href="section-47.8.html">Section 47.8: PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence</a>'),
        ("part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.8.html", '<a class="next" href="../../part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/index.html">Chapter 49: Multi-Agent Embodied AI</a>', '<a class="next" href="section-48.9.html">Section 48.9: Closed-Loop Driving Evaluation And Safety Assurance</a>'),
        ("part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.6.html", '<a class="next" href="../module-55-deployment-architecture/index.html">Chapter 55: Deployment Architecture</a>', '<a class="next" href="section-54.7.html">Section 54.7: Safety Cases And Assurance Arguments For Embodied AI</a>'),
        ("part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/section-55.5.html", '<a class="next" href="../../part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/index.html">Chapter 56: Embodied Agents with Memory</a>', '<a class="next" href="section-55.6.html">Section 55.6: Industrial Fleets, Open-RMF, AMR Interoperability, And Operations</a>'),
        ("part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.11.html", '<a class="next" href="../module-60-teaching-with-this-book/index.html">Chapter 60: Teaching with This Book</a>', '<a class="next" href="section-59.12.html">Section 59.12: Application Track Capstone Templates</a>'),
        ("front-matter/look-inside-preview.html", '<a class="next" href="copyright.html">Copyright and Legal</a>', '<a class="next" href="application-reader-pathways.html">Application Reader Pathways</a>'),
    ]
    for rel, old, new in pairs:
        replace_once(ROOT / rel, old, new)


def update_indexes():
    for item in SECTIONS:
        idx = ROOT / item["part_dir"] / item["module"] / "index.html"
        text = idx.read_text(encoding="utf-8")
        if f'section-{item["chapter"]}.{item["section"]}.html' in text:
            continue
        start = text.find('<ul class="sections-list">')
        if start == -1:
            raise RuntimeError(f"Missing section roadmap in {idx}")
        end = text.find("</ul>", start)
        if end == -1:
            raise RuntimeError(f"Missing roadmap close in {idx}")
        entry = f'<li><span class="section-num">{item["chapter"]}.{item["section"]}</span> <a href="section-{item["chapter"]}.{item["section"]}.html"><span class="section-title">{esc(item["title"])}</span></a><span class="section-desc">{esc(item["thesis"])}</span></li>'
        text = text[:end] + entry + text[end:]
        idx.write_text(text, encoding="utf-8")


def update_toc():
    toc = ROOT / "toc.html"
    text = toc.read_text(encoding="utf-8")
    text = text.replace("12 parts &#183; 60 chapters &#183; 369 sections", "12 parts &#183; 60 chapters &#183; 379 sections")
    text = text.replace('<span class="toc-part-count">8 entries</span>', '<span class="toc-part-count">9 entries</span>')
    text = text.replace(
        '4 chapters &#183; 27 sections</span>\n<p class="toc-part-subtitle">Vision, 3D perception, SLAM, and navigation as action-serving representations.</p>',
        '4 chapters &#183; 29 sections</span>\n<p class="toc-part-subtitle">Vision, 3D perception, SLAM, and navigation as action-serving representations.</p>',
    )
    text = text.replace(
        '5 chapters &#183; 35 sections</span>\n<p class="toc-part-subtitle">The language, vision, and action models that connect instructions, scene understanding, and robot skills.</p>',
        '5 chapters &#183; 37 sections</span>\n<p class="toc-part-subtitle">The language, vision, and action models that connect instructions, scene understanding, and robot skills.</p>',
    )
    text = text.replace(
        '5 chapters &#183; 37 sections</span>\n<p class="toc-part-subtitle">Manipulation, dexterity, locomotion, humanoids, drones, and autonomous vehicles as embodied skills.</p>',
        '5 chapters &#183; 40 sections</span>\n<p class="toc-part-subtitle">Manipulation, dexterity, locomotion, humanoids, drones, and autonomous vehicles as embodied skills.</p>',
    )
    text = text.replace(
        '4 chapters &#183; 21 sections</span>\n<p class="toc-part-subtitle">Measurement, robustness, safety, and deployment discipline for embodied systems.</p>',
        '4 chapters &#183; 23 sections</span>\n<p class="toc-part-subtitle">Measurement, robustness, safety, and deployment discipline for embodied systems.</p>',
    )
    text = text.replace(
        '5 chapters &#183; 31 sections</span>\n<p class="toc-part-subtitle">Memory, continual learning, open problems, capstone projects, and teaching paths.</p>',
        '5 chapters &#183; 32 sections</span>\n<p class="toc-part-subtitle">Memory, continual learning, open problems, capstone projects, and teaching paths.</p>',
    )
    if "front-matter/application-reader-pathways.html" not in text:
        fm_old = '<span class="toc-chapter-num">F8</span><div><a class="toc-card-link" href="front-matter/copyright.html"><span class="toc-chapter-title">Copyright and Legal</span>'
        fm_new = '<span class="toc-chapter-num">F8</span><div><a class="toc-card-link" href="front-matter/application-reader-pathways.html"><span class="toc-chapter-title">Application Reader Pathways</span></a><span class="toc-chapter-subtitle">Application-specific pathways through the book.</span></div></div><code class="toc-chapter-dir">front-matter/application-reader-pathways.html</code></li><li class="toc-chapter"><div class="toc-chapter-head"><span class="toc-chapter-num">F9</span><div><a class="toc-card-link" href="front-matter/copyright.html"><span class="toc-chapter-title">Copyright and Legal</span>'
        text = text.replace(fm_old, fm_new, 1)
    for item in SECTIONS:
        link = f'{item["part_dir"]}/{item["module"]}/section-{item["chapter"]}.{item["section"]}.html'
        if link in text:
            continue
        prev_num = f'{item["chapter"]}.{int(item["section"]) - 1}'
        prev_link = f'{item["part_dir"]}/{item["module"]}/section-{prev_num}.html'
        old = f'{prev_link}'
        idx = text.find(old)
        if idx == -1:
            raise RuntimeError(f"Cannot find previous ToC link for {link}")
        close = text.find("</li>", idx)
        insert = f'<li><span class="toc-section-num">{item["chapter"]}.{item["section"]}</span> <a class="toc-sec-link" href="{link}">{esc(item["title"])}</a></li>'
        text = text[: close + 5] + insert + text[close + 5 :]
    toc.write_text(text, encoding="utf-8")


def write_report():
    report = ROOT / "APPLICATION_REFERENCE_LAYER_REPORT.md"
    rows = "\n".join(
        f'- Section {item["chapter"]}.{item["section"]}: {item["title"]} in `{item["part_dir"]}/{item["module"]}/`'
        for item in SECTIONS
    )
    report.write_text(
        f'''# Application Reference Layer Production Report

Prepared: 2026-06-18

## Scope

Applied the application-reference improvement plan by adding one front-matter pathway page and ten application-grade sections.

## Added Pages

- Front matter: `front-matter/application-reader-pathways.html`
{rows}

## 42-Agent Quality Matrix

The update was produced against the book-writers matrix: chapter lead, curriculum alignment, deep explanation, teaching flow, example design, code pedagogy, exercise design, visual learning, misconception analysis, research scientist, fact integrity, terminology, cross-references, structural architecture, self-containedness, engagement, clarity, cognitive load, content scout, visual identity, illustrator, bibliography, application examples, fun-note discipline, skeptical reader, integration, figure verification, code-caption QA, publication QA, meta-review, and controller checks.

## Evidence Pattern

Every new section includes: big-picture framing, key insight, formal system contract, block diagram, algorithm callout, practical stack, warning callout, practical example, code fragment with caption, library shortcut, builder recipe, self-check, research frontier, exercise, bibliography cards, and previous/up/next navigation.

## Illustrator Gate

Each new section references a raster illustration in its local `images/` directory. The next production step is the Gemini generation pass that creates those referenced PNG files and then reruns the HTML audit.
''',
        encoding="utf-8",
    )


def main():
    write_files()
    update_nav()
    update_indexes()
    update_toc()
    write_report()


if __name__ == "__main__":
    main()
