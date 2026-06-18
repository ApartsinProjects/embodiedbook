from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART9 = ROOT / "part-9-manipulation-locomotion-and-embodied-skills"


def page(chapter, section, title, chapter_title, module_href, prev_href, prev_label, next_href, next_label, body, sources):
    num = f"{chapter}.{section}"
    source_cards = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{name}. <a href="{url}" rel="noopener" target="_blank">{url}</a></p><p class="bib-annotation">{note}</p></div>'
        for name, url, note in sources
    )
    return f'''<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Section {num} of Building Embodied AI: From Perception to Autonomous Action: {title}." name="description"/>
<title>Section {num}: {title} | Building Embodied AI: From Perception to Autonomous Action</title>
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
<div class="part-label"><a href="../index.html">Part IX: Manipulation, Locomotion, and Embodied Skills</a></div>
<div class="chapter-label"><a href="index.html">Chapter {chapter}: {chapter_title}</a></div>
<h1>Section {num}: {title}</h1>
</header>
<main class="content" id="main-content">
<blockquote class="epigraph"><p>"A robot earns trust one recovered disturbance at a time."</p><cite>A Field-Tested Control Loop</cite></blockquote>
{body}
<section class="bibliography">
<h2>Section References</h2>
{source_cards}
</section>
<nav class="chapter-nav">
<a class="prev" href="{prev_href}">{prev_label}</a>
<a class="up" href="{module_href}">Chapter {chapter}: {chapter_title}</a>
<a class="next" href="{next_href}">{next_label}</a>
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


def humanoid_48_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>Boston Dynamics-class humanoids are not walking chatbots. They are underactuated, contact-rich, human-scale machines that must coordinate balance, momentum, manipulation, perception, force limits, thermal limits, timing, and safety in one closed loop.</p>
</div>
<h2>Why The Specialist Layer Matters</h2>
<p>Earlier sections introduced platforms, teleoperation, whole-body control, and foundation models. This section adds the mechanical depth required for a serious humanoid researcher: reduced-order models for planning, full multibody dynamics for execution, contact mode reasoning, and controllers that remain stable when hands, feet, hips, and torso all matter.</p>
<p>The key abstraction is a hierarchy of models. A planner may reason over center of mass, centroidal momentum, footstep locations, and hand contact targets. A whole-body controller then maps those targets into joint torques or position commands while satisfying contact, friction, joint, actuator, and balance constraints.</p>
<div class="callout key-insight">
<div class="callout-title">Reduced Models Are Interfaces</div>
<p>A centroidal model is not a toy replacement for full dynamics. It is an interface between high-level task planning and whole-body execution: simple enough to optimize quickly, but physical enough to expose balance, angular momentum, and contact feasibility.</p>
</div>
<h2>Centroidal Dynamics And Balance</h2>
<p>For a humanoid of mass $m$, center of mass position $c$, total linear momentum $l$, and angular momentum $k$, the centroidal dynamics summarize the whole robot as:</p>
<p>$$\\dot c = \\frac{1}{m}l, \\qquad \\dot l = mg + \\sum_i f_i, \\qquad \\dot k = \\sum_i (p_i - c) \\times f_i + \\tau_i.$$</p>
<p>The contact point $p_i$, contact force $f_i$, and contact torque $\\tau_i$ are the bridge from geometry to behavior. If the required force exits the friction cone, the plan is not merely suboptimal. It asks the robot to push on the world in a direction the world will not support.</p>
<div class="callout algorithm">
<div class="callout-title">Algorithm: Whole-Body QP Control Loop</div>
<ol>
<li>Estimate base pose, joint state, contact state, object state, and human-zone constraints.</li>
<li>Choose task targets: center of mass, torso, feet, hands, gaze, and object pose.</li>
<li>Build equality constraints for rigid contacts and task accelerations.</li>
<li>Build inequality constraints for friction cones, joint limits, torque limits, velocity limits, and safety zones.</li>
<li>Solve a quadratic program for joint accelerations, contact forces, and torques.</li>
<li>Send commands through the low-level controller, then log solver status, tracking error, contact slip, and recovery actions.</li>
</ol>
</div>
<h2>Contact-Rich Loco-Manipulation</h2>
<p>Loco-manipulation begins when walking and manipulation stop being separable. Carrying a heavy object changes the support polygon, the feasible torso motion, the footstep plan, and the hand force budget. Opening a door may require one hand to pull, one foot to reposition, the torso to rotate, and the controller to maintain balance while the door hinge imposes a moving constraint.</p>
<p>A serious system therefore treats limbs as resources. A hand may be an end-effector, a brace, a sensor, or a temporary support. A foot may be a locomotion contact, a push contact, or a stabilizing anchor. Interlimb coordination is the policy that assigns these roles over time.</p>
<div class="comparison-table">
<div class="comparison-table-title">Humanoid Research Stack</div>
<table>
<thead><tr><th>Layer</th><th>Technical Content</th><th>Evidence Artifact</th></tr></thead>
<tbody>
<tr><td>Reduced model</td><td>CoM, centroidal momentum, ZMP, capture region, footstep timing</td><td>Feasible contact and momentum plan</td></tr>
<tr><td>Whole-body controller</td><td>Operational-space control, inverse dynamics, constrained QP, torque limits</td><td>Solver trace, torque trace, contact wrench trace</td></tr>
<tr><td>Learning policy</td><td>RL, imitation, motion priors, domain randomization, sim-to-real</td><td>Scenario panel with perturbations and recovery labels</td></tr>
<tr><td>Contact perception</td><td>Tactile hands, force feedback, object state estimation, slip detection</td><td>Contact event log and manipulation outcome</td></tr>
<tr><td>Deployment layer</td><td>Runtime supervision, human-zone limits, task validation, fleet metrics</td><td>Safety case and field reliability dashboard</td></tr>
</tbody>
</table>
</div>
<h2>Practical Recipe</h2>
<ol>
<li>Start with a constrained task, such as pick, carry, place, or door traversal.</li>
<li>Write the contact schedule and identify which contacts are required, optional, or forbidden.</li>
<li>Plan footsteps, hand contacts, and object motion with centroidal feasibility checks.</li>
<li>Use Drake, MuJoCo, MJX, Isaac Lab, or Pinocchio to verify dynamics and constraints.</li>
<li>Train or adapt a policy only after the model-based baseline exposes the physical limits.</li>
<li>Evaluate with pushes, payload changes, object pose shifts, friction changes, and perception latency.</li>
</ol>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>A hand-built centroidal controller can teach the mechanism, but production work should use Drake, Pinocchio, MuJoCo, MJX, Isaac Lab, and ROS 2 control to keep multibody dynamics, solver status, contact constraints, and logs inspectable.</p>
</div>
<pre><code class="language-python"># Minimal evidence schema for whole-body humanoid research.
from dataclasses import dataclass, asdict

@dataclass
class HumanoidTrial:
    task: str
    contact_schedule: list[str]
    controller: str
    perturbation: str
    metrics: dict[str, float]

trial = HumanoidTrial(
    task="carry object while stepping over a low obstacle",
    contact_schedule=["left_foot", "right_foot", "left_hand_object", "right_hand_object"],
    controller="centroidal planner plus whole-body QP",
    perturbation="payload shifted by 8 cm during mid-step",
    metrics={"com_error_cm": 3.4, "max_foot_slip_cm": 0.7, "recovery_time_s": 0.42},
)
print(asdict(trial))</code></pre>
<div class="code-caption">Code Fragment 46.8.1 records the task, contact schedule, controller, perturbation, and construct-matched metrics for a humanoid whole-body trial.</div>
<div class="callout warning">
<div class="callout-title">Common Failure Mode</div>
<p>A humanoid demo can look successful while hiding an impossible control budget. Always inspect contact forces, torque saturation, solver failures, emergency stops, and recovery events, not only final task completion.</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise 46.8.1</div>
<p>Design a same-panel comparison between a pure learned policy and a centroidal-planner plus whole-body-QP stack for a heavy-object carry task. Specify contacts, perturbations, metrics, and the failure taxonomy.</p>
</div>'''


def humanoid_49_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>A Boston Dynamics-style research track asks whether a humanoid can turn dynamic mobility into useful work. The target is not a single acrobatic clip. The target is reliable mobile manipulation under contact, payload, uncertainty, and human-scale safety constraints.</p>
</div>
<h2>The Research Contract</h2>
<p>The research contract for enterprise humanoids is stricter than a benchmark score: the robot must perform useful material-handling or workstation tasks, recover from ordinary disturbances, expose failures in logs, and improve through simulation, teleoperation, reinforcement learning, and field feedback.</p>
<p>Recent public signals from Boston Dynamics, the Robotics and AI Institute, Toyota Research Institute, Google DeepMind, and NVIDIA all point in the same direction: humanoids need whole-body manipulation, simulation-trained behaviors, foundation-model reasoning, tactile feedback, and runtime safety supervision.</p>
<div class="callout research-frontier">
<div class="callout-title">Frontier Watch</div>
<p>Large Behavior Models and robotics foundation models are best understood as task-level and behavior-level priors. They do not remove the need for contact mechanics, controller verification, sensor timing, or safety cases.</p>
</div>
<h2>What A Leading Researcher Needs</h2>
<ul>
<li>Underactuated dynamics, hybrid contact systems, impacts, and contact mode transitions.</li>
<li>Centroidal planning, footstep planning, spatial momentum, capture regions, and push recovery.</li>
<li>Whole-body QP or MPC control with equality and inequality constraints.</li>
<li>Teleoperation, retargeting, motion priors, human demonstration pipelines, and data curation.</li>
<li>Reinforcement learning with domain randomization, curriculum design, actuator models, and failure replay.</li>
<li>Tactile and force-aware manipulation for rigid, deformable, articulated, heavy, and delicate objects.</li>
<li>Runtime supervision, human-zone safety, fleet telemetry, reliability metrics, and task-level safety cases.</li>
</ul>
<h2>Pipeline Pattern</h2>
<p>A robust research loop is simulation-first but not simulation-only. Simulation proposes behaviors, hardware reveals the missing dynamics, logs define the next perturbation set, and the training panel expands. The key is to keep the scenario panel stable enough to compare methods while adding targeted disturbances that expose failure causes.</p>
<div class="comparison-table">
<div class="comparison-table-title">Boston Dynamics-Style Research Loop</div>
<table>
<thead><tr><th>Stage</th><th>Question</th><th>Representative Tools</th></tr></thead>
<tbody>
<tr><td>Task design</td><td>What useful work must the robot perform?</td><td>Workcell analysis, safety case templates, ROS 2 logs</td></tr>
<tr><td>Simulation</td><td>Can the behavior survive dynamics and contact perturbations?</td><td>Isaac Lab, MuJoCo, MJX, Drake, Genesis</td></tr>
<tr><td>Learning</td><td>Which skills improve through data?</td><td>RL, imitation learning, teleoperation, LeRobot-style data tools</td></tr>
<tr><td>Controller integration</td><td>Can the policy respect real-time constraints?</td><td>Whole-body QP, MPC, ROS 2 control, safety filters</td></tr>
<tr><td>Field evaluation</td><td>Does the robot recover and keep working?</td><td>Scenario panels, fleet telemetry, failure taxonomies</td></tr>
</tbody>
</table>
</div>
<h2>Evaluation Panel</h2>
<p>A credible evaluation panel includes static manipulation, dynamic manipulation, locomotion under terrain variation, payload handling, bimanual coordination, human-zone slowdowns, sensor dropout, and recovery after contact surprises. Each result should include success, recovery, safety intervention, contact slip, energy, latency, and hardware stress metrics.</p>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>For a factory tote-moving task, compare three policies on the same workcell: a scripted baseline, a motion-prior policy, and a foundation-model-guided behavior stack. Use the same tote poses, payloads, lighting, floor friction, and human-zone interruptions for all three.</p>
</div>
<pre><code class="language-python"># Same-panel metric skeleton for a humanoid research track.
methods = ["scripted_baseline", "motion_prior_policy", "foundation_model_stack"]
scenarios = ["nominal_tote", "shifted_payload", "human_zone_pause", "low_friction_floor"]
metrics = ["task_success", "recovery_success", "contact_slip", "torque_saturation", "safety_stop"]

panel = [(method, scenario, metric) for method in methods for scenario in scenarios for metric in metrics]
print(f"logged_cells={len(panel)}")</code></pre>
<div class="code-caption">Code Fragment 46.9.1 enumerates a same-panel evaluation grid so every method is tested on the same scenarios and metrics.</div>
<div class="callout key-takeaway">
<div class="callout-title">Key Takeaway</div>
<p>The research bar is recoverable autonomy: useful work, physical feasibility, contact-aware control, reproducible evaluation, and visible safety margins in the same artifact.</p>
</div>'''


def drone_46_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>Drone autonomy begins with a harsh fact: the vehicle is underactuated, fast, energy-limited, and usually unable to stop safely in mid-failure. A serious drone chapter must therefore connect AI decisions to flight dynamics and flight-control interfaces.</p>
</div>
<h2>Quadrotor State And Forces</h2>
<p>A quadrotor state can be written as position $p$, velocity $v$, attitude $R$, body angular velocity $\\omega$, and rotor speeds $\\Omega_i$. The translational and rotational dynamics are commonly summarized as:</p>
<p>$$m\\dot v = mg e_3 - f R e_3 + d, \\qquad J\\dot\\omega = \\tau - \\omega \\times J\\omega.$$</p>
<p>The total thrust $f$ and body torque $\\tau$ come from rotor thrusts. That mapping is the control allocation problem. If the planner asks for a force or moment outside the rotor envelope, the mission is already infeasible.</p>
<div class="callout key-insight">
<div class="callout-title">Autonomy Rides On Inner Loops</div>
<p>A learned planner may choose waypoints or velocities, but the vehicle survives because fast attitude and rate loops stabilize the body. High-level AI should respect the timing and authority of the low-level flight controller.</p>
</div>
<h2>Cascaded Flight Control</h2>
<p>Most practical quadrotor stacks use cascaded control: position control produces velocity or acceleration targets, velocity control produces attitude and thrust targets, attitude control produces body-rate targets, and rate control produces motor commands. The outer loops can be slower. The inner loops must be fast, stable, and well tuned.</p>
<div class="comparison-table">
<div class="comparison-table-title">Drone Control Stack</div>
<table>
<thead><tr><th>Loop</th><th>Typical Input</th><th>Typical Output</th><th>Failure To Log</th></tr></thead>
<tbody>
<tr><td>Mission</td><td>inspection goal, geofence, battery budget</td><td>waypoints or coverage path</td><td>route infeasible</td></tr>
<tr><td>Position</td><td>pose estimate, waypoint</td><td>desired velocity or acceleration</td><td>tracking drift</td></tr>
<tr><td>Attitude</td><td>desired thrust direction</td><td>body-rate target</td><td>tilt or saturation</td></tr>
<tr><td>Rate</td><td>body-rate target</td><td>motor commands</td><td>oscillation or actuator limit</td></tr>
<tr><td>Safety</td><td>geofence, failsafe, health state</td><td>land, hold, return, abort</td><td>late intervention</td></tr>
</tbody>
</table>
</div>
<h2>Geometric Control And MPC</h2>
<p>Geometric control treats attitude directly on $SO(3)$, avoiding Euler-angle singularities. Nonlinear MPC adds constraints for thrust, tilt, obstacle clearance, geofences, and energy. The practical question is not which controller sounds more advanced, but which one meets the update deadline while keeping enough safety margin.</p>
<div class="callout algorithm">
<div class="callout-title">Algorithm: Flight-Ready Evaluation</div>
<ol>
<li>Define mission goals, geofence, wind envelope, sensing mode, and emergency behaviors.</li>
<li>Run a transparent cascaded PID or LQR baseline.</li>
<li>Add a geometric or MPC controller on the same waypoint panel.</li>
<li>Inject wind, latency, battery drop, sensor dropout, and obstacle perturbations.</li>
<li>Compare tracking error, control saturation, near-collision margin, energy, and failsafe events.</li>
</ol>
</div>
<pre><code class="language-python"># Drone control evidence record.
from dataclasses import dataclass

@dataclass
class DroneMissionMetric:
    controller: str
    wind_mps: float
    mean_tracking_error_m: float
    max_tilt_deg: float
    failsafe_events: int

metric = DroneMissionMetric("geometric_controller", 6.0, 0.21, 24.0, 0)
print(metric)</code></pre>
<div class="code-caption">Code Fragment 47.6.1 records wind, tracking error, tilt, and failsafe events for a drone controller comparison.</div>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>Use PX4 for the flight stack, ROS 2 and MAVLink for companion-computer integration, gym-pybullet-drones and safe-control-gym for controlled learning tests, and Aerial Gym or Isaac Sim when parallel aerial simulation matters.</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise 47.6.1</div>
<p>Compare cascaded PID, geometric control, and MPC on the same square inspection route with wind, latency, and thrust saturation. Report tracking error, energy, saturation, and failsafe interventions.</p>
</div>'''


def drone_47_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>A drone mission is a route-planning problem, a trajectory-generation problem, a perception problem, and a safety problem at the same time. The right abstraction depends on whether the drone is choosing where to inspect, how to fly there, or how to recover when the state estimate degrades.</p>
</div>
<h2>Routes, Trajectories, And Commands</h2>
<p>A route is an ordered set of mission goals. A trajectory is a time-parameterized path with position, velocity, acceleration, yaw, and sometimes snap. A command is what the flight stack can actually accept at the current interface: position setpoint, velocity setpoint, attitude target, body rate, or actuator command.</p>
<p>Minimum-snap trajectory generation is useful because quadrotors can track smooth high-order trajectories. For polynomial segment $p(t)$, the optimizer often minimizes an integral such as $\\int \\lVert p^{(4)}(t) \\rVert^2 dt$ subject to waypoint, velocity, acceleration, and continuity constraints.</p>
<div class="callout key-insight">
<div class="callout-title">The Interface Chooses The Risk</div>
<p>Sending waypoints to PX4 is safer and less expressive than sending body-rate commands. Sending body-rate commands gives the autonomy stack more authority, but also more ways to violate assumptions.</p>
</div>
<h2>GPS-Denied Autonomy</h2>
<p>Indoor inspection, tunnels, warehouses, forests, and disaster sites often require autonomy without reliable GPS. The stack then depends on visual-inertial odometry, lidar odometry, SLAM, loop closure, obstacle avoidance, and health monitoring. The mission planner must know when localization confidence is too weak for continued flight.</p>
<div class="comparison-table">
<div class="comparison-table-title">Drone Autonomy Interfaces</div>
<table>
<thead><tr><th>Interface</th><th>Use When</th><th>Main Risk</th></tr></thead>
<tbody>
<tr><td>Mission waypoints</td><td>The environment is known and safety envelope is simple</td><td>Poor local obstacle response</td></tr>
<tr><td>Offboard velocity</td><td>The companion computer handles local planning</td><td>Latency and estimator drift</td></tr>
<tr><td>Trajectory setpoints</td><td>The route requires smooth aggressive motion</td><td>Infeasible timing or thrust</td></tr>
<tr><td>Body-rate targets</td><td>Research needs direct agile control</td><td>Thin safety margin</td></tr>
</tbody>
</table>
</div>
<h2>Inspection And Coverage Planning</h2>
<p>Inspection planning adds coverage constraints: each surface, asset, or viewpoint should be observed with sufficient angle, distance, resolution, and overlap. Multi-drone planning adds communication, collision avoidance, task allocation, and battery-aware return-to-home constraints.</p>
<pre><code class="language-python"># Inspection route scoring sketch.
viewpoints = [
    {"id": "roof_edge", "coverage": 0.22, "risk": 0.10, "energy": 0.18},
    {"id": "north_wall", "coverage": 0.31, "risk": 0.18, "energy": 0.25},
    {"id": "antenna", "coverage": 0.19, "risk": 0.32, "energy": 0.22},
]
score = sum(v["coverage"] - 0.5 * v["risk"] - 0.2 * v["energy"] for v in viewpoints)
print(round(score, 3))</code></pre>
<div class="code-caption">Code Fragment 47.7.1 scores an inspection route by balancing coverage, risk, and energy in one inspectable expression.</div>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>For bridge inspection, require each candidate path to specify camera distance, viewing angle, overlap, battery reserve, wind limit, geofence margin, and emergency landing zones.</p>
</div>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>Use PX4 offboard mode, ROS 2, MAVLink, QGroundControl, VIO or lidar SLAM packages, and simulation-first evaluation. Avoid deprecated trajectory interfaces and verify current flight-stack support before teaching an API.</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise 47.7.1</div>
<p>Design a GPS-denied warehouse inspection mission. Specify localization, map representation, trajectory interface, geofence, battery reserve, emergency behaviors, and the scenario panel used before hardware flight.</p>
</div>'''


def av_47_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>An autonomous vehicle is a robot whose controller acts through tires, not abstract actions. Route decisions become steering, throttle, and braking through vehicle kinematics, tire forces, road friction, actuator limits, and comfort constraints.</p>
</div>
<h2>Kinematic Bicycle Model</h2>
<p>The kinematic bicycle model is the first useful model for route following and local planning. With position $(x,y)$, heading $\\psi$, speed $v$, wheelbase $L$, and steering angle $\\delta$:</p>
<p>$$\\dot x = v\\cos\\psi, \\qquad \\dot y = v\\sin\\psi, \\qquad \\dot\\psi = \\frac{v}{L}\\tan\\delta, \\qquad \\dot v = a.$$</p>
<p>This model exposes non-holonomic motion and curvature limits. It is not enough for high-speed handling, but it is the right bridge between geometric planning and controller design.</p>
<div class="callout key-insight">
<div class="callout-title">Planning Must Respect Curvature</div>
<p>A route polyline is not a drivable trajectory. The vehicle needs curvature, speed, acceleration, jerk, tire friction, and actuator limits that match the road and the platform.</p>
</div>
<h2>Dynamic Bicycle Model</h2>
<p>The dynamic bicycle model adds lateral velocity, yaw rate, tire slip, and lateral tire forces. It matters when speed, friction, braking, and evasive maneuvers dominate. A planner that ignores these effects can choose trajectories that are geometrically collision-free but dynamically unsafe.</p>
<div class="comparison-table">
<div class="comparison-table-title">Vehicle Models For Embodied AI</div>
<table>
<thead><tr><th>Model</th><th>Best Use</th><th>Failure If Misused</th></tr></thead>
<tbody>
<tr><td>Point mass</td><td>Coarse route timing and search</td><td>Ignores heading and steering</td></tr>
<tr><td>Kinematic bicycle</td><td>Lane following, parking, local paths</td><td>Misses tire saturation</td></tr>
<tr><td>Dynamic bicycle</td><td>Higher-speed maneuvers and stability</td><td>Requires tire and friction parameters</td></tr>
<tr><td>Full vehicle model</td><td>Validation and control calibration</td><td>Harder real-time optimization</td></tr>
</tbody>
</table>
</div>
<h2>Control Choices</h2>
<p>Pure pursuit and Stanley control are useful geometric baselines. LQR and MPC expose the state-space and constrained-optimization view. MPC becomes especially important when the controller must trade route progress, comfort, lane keeping, collision margins, and actuator limits in one horizon.</p>
<pre><code class="language-python"># Kinematic bicycle rollout for a local planner sanity check.
import math

x, y, psi, v = 0.0, 0.0, 0.0, 8.0
L, dt = 2.8, 0.1
for _ in range(20):
    delta = math.radians(5.0)
    x += v * math.cos(psi) * dt
    y += v * math.sin(psi) * dt
    psi += (v / L) * math.tan(delta) * dt
print(round(x, 2), round(y, 2), round(math.degrees(psi), 2))</code></pre>
<div class="code-caption">Code Fragment 48.7.1 rolls out a kinematic bicycle model so a local planner can verify curvature and heading change before entering a simulator.</div>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>Use CommonRoad for motion-planning scenarios, CARLA for closed-loop simulation, ROS 2 for stack integration, and vehicle-dynamics libraries or simulator models when tire forces and stability matter.</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise 48.7.1</div>
<p>Implement pure pursuit and MPC for the same lane-change path. Compare lateral error, curvature, jerk, actuator saturation, and time-to-collision margin under dry and low-friction conditions.</p>
</div>'''


def av_48_body():
    return '''<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>Autonomous driving planning is layered because the problem has layered commitments: where to go, how to interact, which lane or gap to choose, and which trajectory the vehicle can safely execute.</p>
</div>
<h2>Route, Behavior, And Local Planning</h2>
<p>Route planning chooses a coarse path through a road graph. Behavior planning chooses maneuvers such as follow, yield, merge, stop, nudge, overtake, or pull over. Local planning turns that decision into a dynamically feasible trajectory with speed, curvature, comfort, and collision constraints.</p>
<div class="callout key-insight">
<div class="callout-title">Prediction And Planning Are Coupled</div>
<p>The planner does not react to one fixed future. It plans against uncertain futures from other agents, then updates as those agents respond. That makes driving an interactive embodied system, not a static path search.</p>
</div>
<h2>Scenario-Based Validation</h2>
<p>Scenario testing is the bridge from impressive driving clips to engineering evidence. A scenario names the road layout, actors, initial states, behavior scripts, weather, sensor configuration, success criteria, and termination rules. OpenSCENARIO, ScenarioRunner, CommonRoad, and CARLA-style tooling make those assumptions explicit.</p>
<div class="comparison-table">
<div class="comparison-table-title">Driving Planning Layers</div>
<table>
<thead><tr><th>Layer</th><th>Question</th><th>Evidence Metric</th></tr></thead>
<tbody>
<tr><td>Route planning</td><td>Which road sequence reaches the goal?</td><td>Route completion and map validity</td></tr>
<tr><td>Behavior planning</td><td>Which maneuver is socially and legally appropriate?</td><td>Rule violations and interaction safety</td></tr>
<tr><td>Prediction</td><td>What might other agents do?</td><td>Calibration, miss rate, interaction coverage</td></tr>
<tr><td>Trajectory optimization</td><td>Which path and speed are feasible now?</td><td>TTC, comfort, jerk, curvature, collision margin</td></tr>
<tr><td>Control</td><td>Can the vehicle track it?</td><td>Lateral error, actuator saturation, stability margin</td></tr>
</tbody>
</table>
</div>
<h2>Safety Case Thinking</h2>
<p>A safety case connects hazards, mitigations, tests, and residual risk. For driving, this means the evidence should be organized by operational design domain: road type, weather, speed range, traffic density, lighting, map quality, sensor availability, and fallback behavior.</p>
<pre><code class="language-python"># Scenario card for an AV planning test.
scenario = {
    "name": "occluded pedestrian after parked van",
    "odd": ["urban", "daylight", "dry road", "25 mph"],
    "actors": ["ego_vehicle", "parked_van", "pedestrian"],
    "metrics": ["min_ttc", "max_deceleration", "rule_violation", "route_completion"],
    "fallback": "controlled stop if pedestrian uncertainty exceeds threshold",
}
print(scenario["name"], len(scenario["metrics"]))</code></pre>
<div class="code-caption">Code Fragment 48.8.1 defines a scenario card with operational design domain, actors, metrics, and fallback behavior for a driving planner test.</div>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>Use CARLA and ScenarioRunner for closed-loop scenario execution, CommonRoad for planning benchmarks, OpenSCENARIO for portable scenario descriptions, and nuScenes or Waymo Open Dataset for perception and prediction grounding.</p>
</div>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>For an unprotected left turn, evaluate route completion only after checking gap selection, prediction uncertainty, acceleration comfort, time-to-collision, rule compliance, and controller tracking. A completed route with an unsafe gap is not a planning success.</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise 48.8.1</div>
<p>Build a scenario suite with cut-in, unprotected left turn, occluded pedestrian, emergency vehicle, low-friction curve, and construction detour. Define one metric and one expected failure for each layer of the planning stack.</p>
</div>'''


SECTIONS = [
    {
        "dir": PART9 / "module-46-humanoid-robots-and-whole-body-control",
        "file": "section-46.8.html",
        "chapter": 46,
        "section": 8,
        "title": "Advanced humanoid dynamics and contact mechanics",
        "chapter_title": "Humanoid Robots and Whole-Body Control",
        "prev_href": "section-46.7.html",
        "prev_label": "Section 46.7: Safety for human-scale robots",
        "next_href": "section-46.9.html",
        "next_label": "Section 46.9: Boston Dynamics-style loco-manipulation research track",
        "body": humanoid_48_body(),
        "sources": [
            ("MIT Underactuated Robotics humanoids chapter", "https://underactuated.mit.edu/humanoids.html", "Reference for underactuated legged robots, ZMP, footstep planning, and humanoid control concepts."),
            ("Drake robotics toolbox", "https://drake.mit.edu/", "Model-based robotics tooling for multibody dynamics, optimization, and control."),
            ("NVIDIA Isaac Lab whole-body control update", "https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/", "Current tool reference for whole-body control and teleoperation workflows."),
        ],
    },
    {
        "dir": PART9 / "module-46-humanoid-robots-and-whole-body-control",
        "file": "section-46.9.html",
        "chapter": 46,
        "section": 9,
        "title": "Boston Dynamics-style loco-manipulation research track",
        "chapter_title": "Humanoid Robots and Whole-Body Control",
        "prev_href": "section-46.8.html",
        "prev_label": "Section 46.8: Advanced humanoid dynamics and contact mechanics",
        "next_href": "../module-47-drones-and-aerial-embodied-ai/section-47.1.html",
        "next_label": "Section 47.1: Why aerial agents are special",
        "body": humanoid_49_body(),
        "sources": [
            ("Boston Dynamics Atlas", "https://bostondynamics.com/products/atlas/", "Official product framing for industrial humanoid automation."),
            ("Boston Dynamics and RAI Institute humanoid RL partnership", "https://bostondynamics.com/news/boston-dynamics-and-the-robotics-ai-institute-partner/", "Official partnership announcement focused on reinforcement learning for dynamic mobile manipulation on electric Atlas."),
            ("Boston Dynamics Large Behavior Models", "https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/", "Public technical framing for large behavior models, whole-body coordination, and humanoid manipulation."),
            ("HumanoidBench", "https://humanoid-bench.github.io/", "Benchmark reference for humanoid locomotion and manipulation tasks."),
        ],
    },
    {
        "dir": PART9 / "module-47-drones-and-aerial-embodied-ai",
        "file": "section-47.6.html",
        "chapter": 47,
        "section": 6,
        "title": "Quadrotor dynamics and flight control",
        "chapter_title": "Drones and Aerial Embodied AI",
        "prev_href": "section-47.5.html",
        "prev_label": "Section 47.5: Safety, regulation, and simulation for aerial agents",
        "next_href": "section-47.7.html",
        "next_label": "Section 47.7: Trajectory generation and GPS-denied missions",
        "body": drone_46_body(),
        "sources": [
            ("PX4 Autopilot documentation", "https://docs.px4.io/main/en/", "Official open flight-stack documentation."),
            ("PX4 ROS 2 guide", "https://docs.px4.io/main/en/ros2/", "Official guide for ROS 2 integration with PX4."),
            ("gym-pybullet-drones", "https://github.com/utiasDSL/gym-pybullet-drones", "Gymnasium-style quadrotor learning environment."),
        ],
    },
    {
        "dir": PART9 / "module-47-drones-and-aerial-embodied-ai",
        "file": "section-47.7.html",
        "chapter": 47,
        "section": 7,
        "title": "Trajectory generation and GPS-denied missions",
        "chapter_title": "Drones and Aerial Embodied AI",
        "prev_href": "section-47.6.html",
        "prev_label": "Section 47.6: Quadrotor dynamics and flight control",
        "next_href": "../module-48-autonomous-driving-as-embodied-ai/section-48.1.html",
        "next_label": "Section 48.1: Driving as perception, prediction, planning, control",
        "body": drone_47_body(),
        "sources": [
            ("MAVLink developer guide", "https://mavlink.io/en/", "Protocol reference for drone messaging and companion-computer integration."),
            ("MAVLink trajectory interface", "https://mavlink.io/en/services/trajectory.html", "Reference that notes older trajectory interface deprecation and reinforces current API verification."),
            ("Aerial Gym Simulator", "https://ntnu-arl.github.io/aerial_gym_simulator/", "Parallel aerial robot simulation reference."),
        ],
    },
    {
        "dir": PART9 / "module-48-autonomous-driving-as-embodied-ai",
        "file": "section-48.7.html",
        "chapter": 48,
        "section": 7,
        "title": "Vehicle kinematics, dynamics, and control",
        "chapter_title": "Autonomous Driving as Embodied AI",
        "prev_href": "section-48.6.html",
        "prev_label": "Section 48.6: Scenario testing and safety cases",
        "next_href": "section-48.8.html",
        "next_label": "Section 48.8: Route, behavior, and scenario-based planning",
        "body": av_47_body(),
        "sources": [
            ("CommonRoad", "https://commonroad.in.tum.de/", "Motion-planning scenario and benchmark framework."),
            ("CARLA Simulator", "https://carla.org/", "Open autonomous driving simulator for development, training, and validation."),
            ("TUM autonomous vehicles motion planning course", "https://www.mos.ed.tum.de/en/avs/teaching/autonomous-vehicles-motion-planning-decision-making/", "Course reference for graph-based planning, game-theoretic approaches, and RL in AV decision making."),
        ],
    },
    {
        "dir": PART9 / "module-48-autonomous-driving-as-embodied-ai",
        "file": "section-48.8.html",
        "chapter": 48,
        "section": 8,
        "title": "Route, behavior, and scenario-based planning",
        "chapter_title": "Autonomous Driving as Embodied AI",
        "prev_href": "section-48.7.html",
        "prev_label": "Section 48.7: Vehicle kinematics, dynamics, and control",
        "next_href": "../../part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/index.html",
        "next_label": "Chapter 49: Multi-Agent Embodied AI",
        "body": av_48_body(),
        "sources": [
            ("CARLA ScenarioRunner", "https://github.com/carla-simulator/scenario_runner", "Scenario execution engine for CARLA with OpenSCENARIO support."),
            ("nuScenes", "https://www.nuscenes.org/", "Multimodal autonomous driving dataset for perception and prediction."),
            ("Waymo Open Dataset", "https://waymo.com/open/", "Large-scale autonomous driving dataset for perception and behavior research."),
        ],
    },
]


def write_sections():
    for s in SECTIONS:
        html = page(
            s["chapter"],
            s["section"],
            s["title"],
            s["chapter_title"],
            "index.html",
            s["prev_href"],
            s["prev_label"],
            s["next_href"],
            s["next_label"],
            s["body"],
            s["sources"],
        )
        (s["dir"] / s["file"]).write_text(html, encoding="utf-8")


def replace_text(path, old, new):
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Missing expected text in {path}: {old[:80]}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def update_navigation():
    replace_text(
        PART9 / "module-46-humanoid-robots-and-whole-body-control" / "section-46.7.html",
        '<a class="next" href="../module-47-drones-and-aerial-embodied-ai/index.html">Chapter 47: Drones and Aerial Embodied AI</a>',
        '<a class="next" href="section-46.8.html">Section 46.8: Advanced humanoid dynamics and contact mechanics</a>',
    )
    replace_text(
        PART9 / "module-47-drones-and-aerial-embodied-ai" / "section-47.5.html",
        '<a class="next" href="../module-48-autonomous-driving-as-embodied-ai/index.html">Chapter 48: Autonomous Driving as Embodied AI</a>',
        '<a class="next" href="section-47.6.html">Section 47.6: Quadrotor dynamics and flight control</a>',
    )
    replace_text(
        PART9 / "module-48-autonomous-driving-as-embodied-ai" / "section-48.6.html",
        '<a class="next" href="../../part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/index.html">Chapter 49: Multi-Agent Embodied AI</a>',
        '<a class="next" href="section-48.7.html">Section 48.7: Vehicle kinematics, dynamics, and control</a>',
    )


def update_indexes():
    idx46 = PART9 / "module-46-humanoid-robots-and-whole-body-control" / "index.html"
    replace_text(
        idx46,
        '</li></ul>\n<div class="callout library-shortcut">',
        '</li><li><span class="section-num">46.8</span> <a href="section-46.8.html"><span class="section-title">Advanced humanoid dynamics and contact mechanics</span></a><span class="section-desc">Deepens humanoid whole-body control with centroidal dynamics, contact constraints, and whole-body QP reasoning.</span></li><li><span class="section-num">46.9</span> <a href="section-46.9.html"><span class="section-title">Boston Dynamics-style loco-manipulation research track</span></a><span class="section-desc">Frames enterprise humanoid research around loco-manipulation, behavior models, sim-to-real, telemetry, and safety evidence.</span></li></ul>\n<div class="callout library-shortcut">',
    )
    idx47 = PART9 / "module-47-drones-and-aerial-embodied-ai" / "index.html"
    replace_text(
        idx47,
        '</li></ul>\n<div class="callout library-shortcut">',
        '</li><li><span class="section-num">47.6</span> <a href="section-47.6.html"><span class="section-title">Quadrotor dynamics and flight control</span></a><span class="section-desc">Adds 6-DOF quadrotor dynamics, cascaded control, geometric control, MPC, and flight-stack evidence metrics.</span></li><li><span class="section-num">47.7</span> <a href="section-47.7.html"><span class="section-title">Trajectory generation and GPS-denied missions</span></a><span class="section-desc">Adds minimum-snap trajectories, PX4 offboard interfaces, VIO, coverage planning, and inspection mission design.</span></li></ul>\n<div class="callout library-shortcut">',
    )
    idx48 = PART9 / "module-48-autonomous-driving-as-embodied-ai" / "index.html"
    replace_text(
        idx48,
        '</li></ul>\n<div class="callout library-shortcut">',
        '</li><li><span class="section-num">48.7</span> <a href="section-48.7.html"><span class="section-title">Vehicle kinematics, dynamics, and control</span></a><span class="section-desc">Adds bicycle models, tire-aware dynamics, pure pursuit, Stanley, LQR, MPC, and construct-matched control metrics.</span></li><li><span class="section-num">48.8</span> <a href="section-48.8.html"><span class="section-title">Route, behavior, and scenario-based planning</span></a><span class="section-desc">Adds route planning, behavior planning, trajectory optimization, scenario cards, ODDs, and safety-case evidence.</span></li></ul>\n<div class="callout library-shortcut">',
    )


def update_toc():
    toc = ROOT / "toc.html"
    text = toc.read_text(encoding="utf-8")
    text = text.replace('12 parts &#183; 60 chapters &#183; 363 sections', '12 parts &#183; 60 chapters &#183; 369 sections')
    text = text.replace('5 chapters &#183; 31 sections</span>\n<p class="toc-part-subtitle">Manipulation, dexterity, locomotion, humanoids, drones, and autonomous vehicles as embodied skills.</p>', '5 chapters &#183; 37 sections</span>\n<p class="toc-part-subtitle">Manipulation, dexterity, locomotion, humanoids, drones, and autonomous vehicles as embodied skills.</p>')
    text = text.replace('46.7</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.7.html">Safety for human-scale robots</a></li></ol>', '46.7</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.7.html">Safety for human-scale robots</a></li><li><span class="toc-section-num">46.8</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html">Advanced humanoid dynamics and contact mechanics</a></li><li><span class="toc-section-num">46.9</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.9.html">Boston Dynamics-style loco-manipulation research track</a></li></ol>')
    text = text.replace('47.5</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.5.html">Safety, regulation, and simulation for aerial agents</a></li></ol>', '47.5</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.5.html">Safety, regulation, and simulation for aerial agents</a></li><li><span class="toc-section-num">47.6</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.6.html">Quadrotor dynamics and flight control</a></li><li><span class="toc-section-num">47.7</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-47-drones-and-aerial-embodied-ai/section-47.7.html">Trajectory generation and GPS-denied missions</a></li></ol>')
    text = text.replace('48.6</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.6.html">Scenario testing and safety cases</a></li></ol>', '48.6</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.6.html">Scenario testing and safety cases</a></li><li><span class="toc-section-num">48.7</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.7.html">Vehicle kinematics, dynamics, and control</a></li><li><span class="toc-section-num">48.8</span> <a class="toc-sec-link" href="part-9-manipulation-locomotion-and-embodied-skills/module-48-autonomous-driving-as-embodied-ai/section-48.8.html">Route, behavior, and scenario-based planning</a></li></ol>')
    toc.write_text(text, encoding="utf-8")


def main():
    write_sections()
    update_navigation()
    update_indexes()
    update_toc()


if __name__ == "__main__":
    main()
