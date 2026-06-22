from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def code_block(code: str, output: str, caption: str) -> str:
    return (
        f'<pre><code class="language-python">{code.strip()}</code></pre>\n'
        f'<div class="code-output">\n{output.strip()}\n</div>\n'
        f'<div class="code-caption"><strong>Code Fragment 1:</strong> {caption}</div>'
    )


def figure(module: Path, section: str, title: str, image: str | None) -> str:
    if not image:
        return ""
    if not (module / "images" / image).exists():
        return ""
    alt = (
        f"Educational illustration for Section {section}, showing {title.lower()} as a robot "
        "reasoning problem that connects measurements, state estimates, decisions, and replayable evidence."
    )
    return (
        '<figure class="illustration">\n'
        f'<img alt="{alt}" loading="lazy" src="images/{image}"/>\n'
        f'<figcaption><strong>Figure {section}.1</strong>: {title} becomes useful when the visual idea is tied to a state variable, an uncertainty model, and the next robot action.</figcaption>\n'
        '</figure>\n'
    )


def fallback_diagram(section: str, title: str, mode: str) -> str:
    if mode == "slam":
        nodes = [
            ("Measurements", 35, 50, "#e3f2fd", "#1565c0"),
            ("Residuals", 250, 50, "#e8f5e9", "#2e7d32"),
            ("Optimizer", 465, 50, "#fff3e0", "#e65100"),
            ("Action Map", 680, 50, "#f3e5f5", "#6a1b9a"),
        ]
        caption = f'<strong>Figure {section}.1</strong>: The SLAM pipeline is useful only when measurements become residuals, residuals become an uncertainty-aware estimate, and the estimate changes the action map.'
    else:
        nodes = [
            ("Goal", 35, 50, "#e3f2fd", "#1565c0"),
            ("Candidates", 250, 50, "#e8f5e9", "#2e7d32"),
            ("Constraints", 465, 50, "#fff3e0", "#e65100"),
            ("Command", 680, 50, "#f3e5f5", "#6a1b9a"),
        ]
        caption = f'<strong>Figure {section}.1</strong>: The navigation loop turns goals into candidate motions, filters them through constraints, and publishes only commands the robot can execute.'
    rects = []
    for label, x, y, fill, stroke in nodes:
        rects.append(f'<rect x="{x}" y="{y}" width="150" height="70" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
        rects.append(f'<text x="{x + 75}" y="{y + 42}" text-anchor="middle" font-size="18" fill="#1a1a2e">{label}</text>')
    arrows = []
    for x in [190, 405, 620]:
        arrows.append(f'<path d="M{x} 85 L{x + 50} 85" stroke="#333" stroke-width="3" marker-end="url(#arrow-{section.replace(".", "-")})"/>')
    return (
        '<div class="diagram-container">\n'
        f'<svg aria-label="Block diagram for {title}" role="img" viewBox="0 0 870 170" xmlns="http://www.w3.org/2000/svg">\n'
        '<defs>\n'
        f'<marker id="arrow-{section.replace(".", "-")}" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#333"/></marker>\n'
        '</defs>\n'
        + "\n".join(rects + arrows) +
        '\n</svg>\n'
        f'<div class="diagram-caption">{caption}</div>\n'
        '</div>\n'
    )


def visual(module: Path, section: str, title: str, image: str | None, mode: str) -> str:
    drawn = figure(module, section, title, image)
    return drawn if drawn else fallback_diagram(section, title, mode)


def body_29(module: Path, section: str, title: str, desc: str, core: str, formula: str,
            algorithm: list[str], code: str, output: str, caption: str, tools: str, frontier: str,
            img: str | None, bibs: list[tuple[str, str, str]], next_href: str, next_title: str) -> str:
    items = "\n".join(f"<li>{item}</li>" for item in algorithm)
    bib_html = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref} <a href="{url}" rel="noopener" target="_blank">{url}</a></p><p class="bib-annotation">{ann}</p></div>'
        for ref, url, ann in bibs
    )
    return f'''<blockquote class="epigraph"><p>"A map is a promise that every future footstep will ask you to keep."</p><cite>A Loop Closure That Came Back With Receipts</cite></blockquote>
{visual(module, section, title, img, "slam")}<div class="callout big-picture"><div class="callout-title">Big Picture</div><p><strong>{title}</strong> is the state-estimation half of embodied autonomy. The robot has partial, noisy, time-stamped evidence; it must turn that evidence into a pose, a map, and an uncertainty statement that a planner can actually trust.</p></div>
<div class="callout pathway"><div class="callout-title">Reader Pathway</div><p>This section moves from the physical failure that motivates the method, to the mathematical object being estimated, to a small runnable diagnostic, then to the production tools that make the method deployable.</p></div>
<h2>Problem First</h2>
<p>{desc}</p>
<p>{core}</p>
<div class="callout key-insight"><div class="callout-title">Action Contract</div><p>A localization or mapping result is incomplete until it names the frame, timestamp, covariance or confidence, map layer, and downstream consumer. A beautiful trajectory plot with no uncertainty is not a robot interface; it is a picture.</p></div>
<h2>Formal Model</h2>
<p>The common estimator shape is a posterior over robot trajectory and map variables conditioned on controls and observations:</p>
<p>$$ {formula} $$</p>
<p>The important part is not the notation alone. The posterior says that motion increments, landmark observations, scan matches, visual features, and loop closures are all evidence terms. The estimate is strongest when each term carries a residual, a covariance model, and a replayable source record.</p>
<div class="callout algorithm"><div class="callout-title">Algorithm: Section {section} Evidence Loop</div><ol>
{items}
</ol></div>
<h2>Worked Diagnostic</h2>
<p>Code Fragment 1 makes the section concrete with a small numeric check. It is intentionally small, because the first debugging question is whether the estimate behaves correctly before it is hidden inside a large ROS graph or optimizer.</p>
{code_block(code, output, caption)}
<h2>Tool Workflow</h2>
<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>{tools}</p></div>
<p>Use the hand calculation as the unit test and the library stack as the maintained implementation. The right workflow is not from-scratch forever; it is from-scratch until the invariants are visible, then production tools for scale, logging, visualization, and integration.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Replay the same bag or log with one perturbation at a time: delayed timestamps, wrong frame transform, biased wheel radius, feature dropout, repeated corridor texture, moving people, or stale map cells. If the failure label cannot distinguish sensing, association, optimization, mapping, and planning, the section is not yet debug-ready.</p></div>
<div class="callout practical-example"><div class="callout-title">Practical Example</div><p>A warehouse robot should record odometry, IMU packets, scan or feature tracks, estimated pose, covariance, active map layer, planner cost, and recovery behavior in one replay. That single artifact lets the team ask whether a route failed because the robot was lost, the map was wrong, the planner was overconfident, or the controller could not execute the command.</p></div>
<div class="callout research-frontier"><div class="callout-title">Research Frontier</div><p>{frontier}</p></div>
<div class="callout fun-note"><div class="callout-title">Memory Hook</div><p>SLAM is the robot version of walking into a room and saying, "I remember this place," then checking whether the memory improves the next step instead of merely sounding confident.</p></div>
<div class="callout self-check"><div class="callout-title">Self Check</div><p>Can you state the state variables, observation residual, uncertainty representation, replay artifact, and most likely field failure for {title.lower()}? If one field is vague, the estimator is not ready for embodied use.</p></div>
<div class="callout key-takeaway"><div class="callout-title">Key Takeaway</div><p>{title} is production-ready only when geometry, uncertainty, timing, and action consequences are tested together.</p></div>
<div class="callout exercise"><div class="callout-title">Exercise {section}.1</div><p>Design a two-run replay test for this section. One run should be nominal. The other should perturb exactly one assumption, such as feature dropout, wheel slip, map aging, or delayed transforms. Report the metric, the failure label, and the action that should change.</p></div>
<div class="whats-next"><h3>What's Next?</h3><p>Continue to <a href="{next_href}">{next_title}</a>, where this state-estimation contract becomes the input to the next embodied capability.</p></div>
<section class="bibliography"><h2>Section References</h2>
{bib_html}
</section>
'''


def body_30(module: Path, section: str, title: str, desc: str, core: str, formula: str,
            algorithm: list[str], code: str, output: str, caption: str, tools: str, frontier: str,
            img: str | None, bibs: list[tuple[str, str, str]], next_href: str, next_title: str) -> str:
    items = "\n".join(f"<li>{item}</li>" for item in algorithm)
    bib_html = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref} <a href="{url}" rel="noopener" target="_blank">{url}</a></p><p class="bib-annotation">{ann}</p></div>'
        for ref, url, ann in bibs
    )
    return f'''<blockquote class="epigraph"><p>"A plan is only smart if the wheels, floor, people, and clock all agree to it."</p><cite>A Local Planner With Commitment Issues</cite></blockquote>
{visual(module, section, title, img, "nav")}<div class="callout big-picture"><div class="callout-title">Big Picture</div><p><strong>{title}</strong> turns maps and goals into constrained motion. The planner is not searching for a pretty line; it is choosing a feasible commitment under geometry, dynamics, uncertainty, moving obstacles, and recovery rules.</p></div>
<div class="callout pathway"><div class="callout-title">Reader Pathway</div><p>This section starts with the planning failure that motivates the method, then gives the mathematical object, an algorithmic recipe, a runnable diagnostic, a tool shortcut, and field tests that reveal whether the plan survives contact with the robot.</p></div>
<h2>Problem First</h2>
<p>{desc}</p>
<p>{core}</p>
<div class="callout key-insight"><div class="callout-title">Feasibility Before Beauty</div><p>The best-looking route is not the best robot plan unless the controller can track it, the costmap reflects current hazards, and replanning has a defined trigger. Navigation quality is measured by executed motion, not only by path length.</p></div>
<h2>Formal Model</h2>
<p>Most navigation methods can be read as constrained search or optimization:</p>
<p>$$ {formula} $$</p>
<p>The cost term names what the robot wants. The constraints name what reality permits: collision clearance, velocity and acceleration limits, curvature bounds, kinodynamic feasibility, perception confidence, and safety monitors.</p>
<div class="callout algorithm"><div class="callout-title">Algorithm: Section {section} Planning Loop</div><ol>
{items}
</ol></div>
<h2>Worked Diagnostic</h2>
<p>Code Fragment 1 isolates the planning idea in a tiny runnable example. The goal is not to replace Nav2 or OMPL; the goal is to make the invariant visible before the full stack absorbs it.</p>
{code_block(code, output, caption)}
<h2>Tool Workflow</h2>
<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>{tools}</p></div>
<p>Keep the small implementation as a regression test. Use the maintained stack for maps, costmaps, behavior trees, controllers, plugins, simulation replay, and deployment telemetry.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Every planner in this chapter should be replayed with blocked corridors, moving obstacles, localization jumps, stale costmaps, actuator saturation, and recovery failure. A plan that only works in a clean static grid is a sketch, not an embodied system.</p></div>
<div class="callout practical-example"><div class="callout-title">Practical Example</div><p>A delivery robot should log global path, local command, costmap snapshot, controller error, nearest obstacle distance, replan count, and recovery action. Those fields separate a weak route planner from a bad local controller or an outdated perception layer.</p></div>
<div class="callout note"><div class="callout-title">Integration Checklist</div><p>Before comparing planners, freeze the robot footprint, inflation radius, controller frequency, maximum velocity, acceleration limits, map resolution, and localization source. Otherwise the comparison silently mixes planner quality with robot configuration. A serious navigation report should also include a route replay, a costmap snapshot at the decision point, the exact recovery behavior that was enabled, and whether the final command respected the same kinodynamic limits used during planning.</p></div>
<div class="callout research-frontier"><div class="callout-title">Research Frontier</div><p>{frontier}</p></div>
<div class="callout fun-note"><div class="callout-title">Memory Hook</div><p>A planner that ignores dynamics is a cartographer with excellent handwriting and no driver license.</p></div>
<div class="callout self-check"><div class="callout-title">Self Check</div><p>Can you state the search space, cost function, constraints, replanning trigger, controller interface, and failure metric for {title.lower()}? If not, the planner is not specified enough to deploy.</p></div>
<div class="callout key-takeaway"><div class="callout-title">Key Takeaway</div><p>{title} is ready for embodied use when route quality, dynamic feasibility, local control, and recovery behavior are measured in the same replay.</p></div>
<div class="callout exercise"><div class="callout-title">Exercise {section}.1</div><p>Create a three-scenario planning panel: clear route, blocked route, and dynamic obstacle. Report path cost, minimum clearance, replan count, controller saturation, and final mission outcome for the same robot model.</p></div>
<div class="whats-next"><h3>What's Next?</h3><p>Continue to <a href="{next_href}">{next_title}</a>, where this planning contract connects to the next embodied capability.</p></div>
<section class="bibliography"><h2>Section References</h2>
{bib_html}
</section>
'''


def replace_main(path: Path, new_body: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.index('<main class="content" id="main-content">') + len('<main class="content" id="main-content">')
    nav_match = re.search(r'\n<nav class="chapter-nav">', text)
    if not nav_match:
        raise RuntimeError(f"nav not found in {path}")
    updated = text[:start] + "\n" + new_body.rstrip() + text[nav_match.start():]
    path.write_text(updated, encoding="utf-8", newline="\n")


M29 = ROOT / "part-6-embodied-perception" / "module-29-localization-and-mapping-slam"
M30 = ROOT / "part-6-embodied-perception" / "module-30-navigation-and-path-planning"

slam_bibs = [
    ("Durrant-Whyte, H. and Bailey, T. \"Simultaneous Localization and Mapping.\" IEEE Robotics and Automation Magazine, 2006.", "https://ieeexplore.ieee.org/document/1638022", "Classic SLAM tutorial that frames the estimation problem and the role of uncertainty."),
    ("GTSAM Project. \"Factor Graphs and GTSAM.\" Official documentation.", "https://gtsam.org/", "Primary tool reference for factor graphs, smoothing, pose graphs, and robotics estimation examples."),
    ("ROS 2 Navigation Project. \"Nav2 documentation.\" Official documentation.", "https://navigation.ros.org/", "Primary documentation for integrating localization, maps, planners, controllers, behavior trees, and recoveries."),
]

nav_bibs = [
    ("LaValle, S. M. \"Planning Algorithms.\" Cambridge University Press, 2006.", "http://lavalle.pl/planning/", "Open textbook reference for graph search, sampling-based planning, configuration spaces, and kinodynamic planning."),
    ("OMPL Project. \"Open Motion Planning Library.\" Official documentation.", "https://ompl.kavrakilab.org/", "Primary tool reference for sampling-based planners such as RRT, RRTstar, PRM, and kinodynamic variants."),
    ("ROS 2 Navigation Project. \"Nav2 documentation.\" Official documentation.", "https://navigation.ros.org/", "Primary documentation for global planners, controllers, costmaps, behavior trees, and recovery behaviors."),
]

sections_29 = {
    "29.1": ("Where am I and what does the world look like", "A robot cannot make a reliable plan if pose and map are treated as separate chores. The map is built from poses, while pose estimates depend on the map. This circular dependency is why SLAM is an estimation problem rather than a drawing problem.", "The state usually contains a trajectory $x_{0:T}$ and map variables $m$. Controls $u_{1:T}$ predict motion, while observations $z_{1:T}$ correct that prediction. A localization-only system estimates $x_t$ against a known map; a mapping-only system assumes poses are good enough; SLAM estimates both and exposes the remaining uncertainty.", r"p(x_{0:T},m\mid z_{1:T},u_{1:T}) \propto p(x_0)\prod_t p(x_t\mid x_{t-1},u_t)\prod_t p(z_t\mid x_t,m)", ["Define the state variables: pose, velocity if needed, landmarks or grid cells, and map frame.", "Attach every measurement to a frame, timestamp, residual, and covariance.", "Update the belief, then publish only the estimate fields the planner is allowed to consume.", "Replay the same evidence after perturbing one sensor or transform assumption."], """# Compare a pose prior with one landmark observation.
# The innovation shows whether the new range evidence agrees with the map.
import numpy as np

prior_xy = np.array([2.0, 1.0])
landmark_xy = np.array([5.0, 1.0])
measured_range_m = 2.7
predicted_range_m = np.linalg.norm(landmark_xy - prior_xy)
innovation_m = measured_range_m - predicted_range_m
print(f"predicted={predicted_range_m:.2f} m")
print(f"innovation={innovation_m:.2f} m")""", "predicted=3.00 m\ninnovation=-0.30 m", "The diagnostic computes a range residual from one landmark and one pose prior. The negative innovation says the observation is closer than the current map-pose prediction, which should pull the pose or landmark estimate during correction.", "In production, ROS 2 tf2 handles frame transforms, Nav2 consumes map and localization topics, and GTSAM or Ceres solves larger nonlinear least-squares problems. That is the reduction from hand-checking residuals to configuring maintained graph and middleware components.", "Current SLAM research increasingly connects geometry with semantics, neural scene representations, and open-vocabulary perception. The open problem is not only dense reconstruction; it is making dense maps reliable enough for planning, manipulation, and safety cases.", "chapter-29-illustration-01.png"),
    "29.2": ("Odometry and dead reckoning", "Odometry is tempting because it is always available. Wheel ticks, IMU integration, and visual motion increments keep producing estimates even when no map feature is visible. The danger is that small bias accumulates without an external correction.", "For a differential-drive base, wheel angular increments become a forward displacement and heading change. The covariance must grow with each integration step because uncertainty compounds. Dead reckoning is useful as a short-horizon prediction, not as a long-term truth source.", r"x_{t+1}=x_t+\Delta s\cos(\theta_t+\Delta\theta/2),\quad y_{t+1}=y_t+\Delta s\sin(\theta_t+\Delta\theta/2),\quad \theta_{t+1}=\theta_t+\Delta\theta", ["Calibrate wheel radius, baseline, IMU bias, and timestamp synchronization.", "Integrate small increments in the correct body or odom frame.", "Propagate covariance with motion noise after every step.", "Bound drift by fusing map, visual, GNSS, beacon, or loop-closure evidence."], """# Integrate a differential-drive odometry increment.
# A small wheel mismatch creates a heading change that will compound.
import math

r = 0.05
baseline = 0.32
d_left = 1.00
d_right = 1.06
delta_s = r * (d_right + d_left) / 2.0
delta_theta = r * (d_right - d_left) / baseline
print(f"forward={delta_s:.3f} m")
print(f"heading_change={math.degrees(delta_theta):.2f} deg")""", "forward=0.052 m\nheading_change=0.54 deg", "The calculation turns wheel increments into forward motion and heading drift. The heading change looks tiny for one update, but repeated bias bends the whole trajectory unless a later correction constrains it.", "ROS 2 odometry messages, robot_localization, OpenVINS, and visual odometry modules absorb message formats, timestamp handling, and sensor fusion plumbing. Keep the two-line kinematic calculation as a unit test for frame direction and sign conventions.", "Visual-inertial odometry remains active because low-cost cameras and IMUs are sensitive to rolling shutter, vibration, bias drift, and degraded lighting. Recent work combines learned features with classical filtering, but hardware timing and calibration still decide field performance.", "chapter-29-illustration-02.png"),
    "29.3": ("Localization with particle filters", "A single Gaussian pose estimate can be misleading when the robot starts uncertain or sees repeated structure. A corridor with identical doors can support several plausible locations. Particle filters solve this by representing belief as many weighted hypotheses.", "Monte Carlo localization alternates prediction, measurement weighting, and resampling. Particles spread under motion noise, then measurements increase the weight of poses whose expected observations match the sensor data. Resampling focuses compute on likely poses while preserving enough diversity to recover from ambiguity.", r"w_t^{(i)} \propto w_{t-1}^{(i)}p(z_t\mid x_t^{(i)},m),\quad \hat{x}_t=\sum_i w_t^{(i)}x_t^{(i)}", ["Sample particle motion from the control model and injected noise.", "Compute each particle weight from laser, landmark, or visual likelihood.", "Normalize weights and monitor effective sample size.", "Resample only when degeneracy is high, then publish mean, covariance, and multimodality diagnostics."], """# Weight three pose hypotheses from range residuals.
# Smaller residuals receive larger likelihood before normalization.
import numpy as np

residuals_m = np.array([0.10, 0.60, 1.20])
sigma_m = 0.35
weights = np.exp(-0.5 * (residuals_m / sigma_m) ** 2)
weights = weights / weights.sum()
print(np.round(weights, 3))
print(f"effective_particles={1.0 / np.sum(weights ** 2):.2f}")""", "[0.803 0.197 0.   ]\neffective_particles=1.47", "The snippet converts range residuals into normalized particle weights and an effective-particle count. The low count warns that resampling may be needed because most probability mass has collapsed onto one hypothesis.", "Nav2 AMCL provides a maintained particle-filter localization path for 2D maps, while Python prototypes with NumPy are useful for understanding weight collapse and resampling. The shortcut saves dozens of lines of sensor-model, transform, and map-query code.", "Research frontiers include robust global localization under visual aliasing, semantic particle filters, and localization that reasons over language or object-level map cues. The hard case is not the clean hallway; it is the repeated, changing, partially occluded one.", "chapter-29-illustration-03.png"),
    "29.4": ("Mapping and occupancy grids", "A robot map is a probabilistic memory of what sensor rays have implied. Free space, occupied space, and unknown space must stay distinct because a planner should treat unseen cells differently from cells observed as empty.", "Occupancy grids update each cell through inverse sensor models, often using log odds for numerical stability. A range ray decreases occupancy probability along free cells and increases it near the measured endpoint. The map is therefore a belief field, not a bitmap.", r"L_t(c)=L_{t-1}(c)+\log\frac{p(c\mid z_t,x_t)}{1-p(c\mid z_t,x_t)}-L_0(c)", ["Transform each sensor ray into the map frame.", "Mark traversed cells as free evidence and endpoint cells as occupied evidence.", "Update log odds, then clamp values to avoid irreversible certainty.", "Publish costmap layers that keep unknown, lethal, inflated, and traversable cells separate."], """# Apply log-odds updates for free and occupied evidence.
# The probabilities show how repeated rays change a grid cell belief.
import math

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

log_odds = 0.0
for update in [-0.4, -0.4, 0.9]:
    log_odds += update
    print(f"log_odds={log_odds:.1f}, p_occ={sigmoid(log_odds):.2f}")""", "log_odds=-0.4, p_occ=0.40\nlog_odds=-0.8, p_occ=0.31\nlog_odds=0.1, p_occ=0.52", "The log-odds trace shows two free-space updates followed by one occupied endpoint update. The cell moves gradually because mapping should accumulate evidence rather than flip certainty after a single ray.", "Nav2 costmaps, OctoMap, Voxblox-style volumetric maps, and Open3D point-cloud processing turn this update idea into maintained map layers and visualization workflows. The library path handles ray tracing, inflation, serialization, and map publication.", "Mapping research is moving toward hybrid metric, semantic, and neural maps. The key embodied question is how those richer maps expose conservative, inspectable costs to planners rather than only attractive reconstructions.", "chapter-29-illustration-04.png"),
    "29.5": ("Graph-based and visual SLAM", "Frame-by-frame correction is too local when the robot revisits a place after a long loop. A loop closure says that two far-apart timestamps are actually nearby in space, which can bend the entire trajectory into consistency.", "Graph SLAM represents poses and landmarks as variables and measurements as factors. Visual SLAM adds feature tracking, keyframes, bundle adjustment, and relocalization. The optimizer minimizes residuals weighted by measurement covariance, so a bad association can pull the whole graph into a convincing but false solution.", r"x^*=\arg\min_x \sum_k \|r_k(x)\|_{\Omega_k}^{2},\quad \|r\|_{\Omega}^{2}=r^\top\Omega r", ["Select keyframes or pose nodes that summarize the trajectory.", "Create odometry, landmark, scan-match, visual feature, and loop-closure factors.", "Reject weak data associations with geometric and appearance checks.", "Optimize the pose graph, then inspect residual histograms and loop-closure influence."], """# Compare two residuals with different information weights.
# High-confidence loop closures should matter more only when association is correct.
import numpy as np

residuals = np.array([0.20, 1.00])
information = np.array([25.0, 4.0])
weighted_cost = np.sum(information * residuals ** 2)
print(f"weighted_cost={weighted_cost:.2f}")
print(f"largest_term={np.argmax(information * residuals ** 2)}")""", "weighted_cost=5.00\nlargest_term=1", "The example computes a tiny weighted least-squares cost. Even though the first factor has higher confidence, the larger residual dominates the objective, which is exactly why outlier loop closures need robust checking.", "GTSAM and Ceres provide the nonlinear optimization machinery, while ORB-SLAM3, RTAB-Map, Kimera, and related systems package front ends, loop closure, and map maintenance. The shortcut replaces a full optimizer and visual pipeline with maintained APIs and configuration.", "The frontier is robust data association at scale: visual place recognition, semantic loop closure, dynamic-scene rejection, and uncertainty-aware graph optimization. Graph SLAM succeeds when it distrusts attractive false matches.", "chapter-29-illustration-05.png"),
    "29.6": ("Neural and Gaussian-splat SLAM", "Classical maps are excellent for geometry, but robots increasingly need dense appearance, object affordances, and view synthesis. Neural and Gaussian-splat SLAM try to build maps that are both localizable and visually rich.", "The state can include camera poses plus a continuous scene representation. Gaussian splats store position, covariance, color, opacity, and sometimes semantic features; neural maps encode geometry and appearance in learned fields. The risk is that photorealistic quality can hide metric or temporal inconsistency.", r"\min_{\theta,\,x_{0:T}}\sum_{t,p}\rho\big(I_t(p)-\hat I(p;x_t,\theta)\big)+\lambda R(\theta)", ["Track camera motion with geometric or photometric residuals.", "Update the dense scene representation only from well-conditioned views.", "Separate reconstruction metrics from planning metrics.", "Export collision, traversability, and uncertainty layers before using the map for action."], """# Score whether a dense reconstruction is useful for action.
# Visual quality and metric consistency are kept as separate gates.
psnr_db = 29.0
pose_rmse_cm = 4.5
unknown_fraction = 0.18
passes_action_gate = psnr_db > 25 and pose_rmse_cm < 5 and unknown_fraction < 0.25
print(f"visual_quality={psnr_db} dB")
print(f"action_ready={passes_action_gate}")""", "visual_quality=29.0 dB\naction_ready=True", "The gate keeps appearance quality, pose accuracy, and unknown space separate. A dense map should not enter a planner only because it looks good; it must also have metric and coverage evidence.", "Gaussian-splat SLAM repositories, Open3D, PyTorch, and ROS export bridges handle dense rendering, point-cloud checks, and integration. For production, pair the learned map with a conservative costmap or mesh validation layer.", "Recent dense SLAM work is racing to combine real-time 3D Gaussian maps, semantics, dynamic object handling, and robot-safe geometry. The unsolved research gap is certifying what the dense representation does not know.", None),
    "29.7": ("Map uncertainty", "Uncertainty is not a final error bar; it is an input to action. A planner should slow down, explore, or refuse a route when the map is stale, sparse, or contradicted by fresh observations.", "Map uncertainty appears as covariance over landmarks, entropy over occupancy cells, confidence over semantic labels, and disagreement among map layers. The planner should consume these quantities explicitly instead of treating every map cell as equally trustworthy.", r"H(c)=-p(c)\log p(c)-(1-p(c))\log(1-p(c)),\quad J(\pi)=C(\pi)+\beta\sum_{c\in\pi}H(c)", ["Store uncertainty with the map layer, not in a separate notebook.", "Convert uncertainty into cost only after deciding the robot's risk policy.", "Recompute confidence when maps age, lighting changes, shelves move, or sensors degrade.", "Log whether uncertainty changed the selected route or recovery behavior."], """# Convert occupancy probabilities into entropy costs.
# Cells near 0.5 are most uncertain and should influence route choice.
import math

probs = [0.05, 0.50, 0.90]
for p in probs:
    h = -p * math.log(p) - (1 - p) * math.log(1 - p)
    print(f"p_occ={p:.2f}, entropy={h:.3f}")""", "p_occ=0.05, entropy=0.199\np_occ=0.50, entropy=0.693\np_occ=0.90, entropy=0.325", "The entropy calculation identifies the ambiguous cell as highest risk for planning. This is why unknown and uncertain map regions should not be silently collapsed into free space.", "Nav2 costmap layers can encode unknown space, inflation, keepout zones, and speed filters, while custom map servers can attach age and confidence metadata. The shortcut is to use maintained layers, then add a small policy that defines how uncertainty changes motion.", "Frontier work links uncertainty-aware mapping with active perception, information gain planning, and safety assurance. The important open question is when a robot should gather more evidence instead of pushing forward.", None),
    "29.8": ("Modern SLAM systems and failure modes", "A modern SLAM system is not one algorithm. It is a contract among sensors, calibration, front-end tracking, back-end optimization, map storage, localization consumers, and replay tools.", "The systems view matters because field failures often arise at interfaces: a visual-inertial front end tracks well but publishes stale transforms, a loop closure is geometrically plausible but semantically wrong, or the map is correct but too old for the current route.", r"\text{SLAM system}=(\text{sensors},\text{calibration},\text{front end},\text{back end},\text{map},\text{consumer},\text{replay})", ["Write a sensor and calibration manifest before running SLAM.", "Record front-end health: feature count, IMU residuals, scan-match score, and dropped frames.", "Record back-end health: factor residuals, loop closures, optimization time, and marginal covariance.", "Replay failures with all consumers attached: localization, planner, controller, and recovery behavior."], """# Classify a SLAM failure from health signals.
# The labels separate front-end tracking from back-end graph trouble.
feature_count = 38
loop_residual_m = 2.4
optimization_ms = 180
if feature_count < 50:
    label = "front_end_tracking_risk"
elif loop_residual_m > 1.0:
    label = "loop_closure_outlier_risk"
elif optimization_ms > 100:
    label = "back_end_latency_risk"
else:
    label = "nominal"
print(label)""", "front_end_tracking_risk", "The classifier turns health signals into a failure label before the robot reaches for a generic recovery. The point is not the thresholds; the point is separating tracking, association, and optimization failures.", "ORB-SLAM3, RTAB-Map, OpenVINS, Kimera, Cartographer-style pipelines, GTSAM, Ceres, and Nav2 cover different parts of the system. A serious build chooses tools by sensor suite, map type, latency budget, license, deployment platform, and replay needs.", "The strongest current systems blend classical estimation with learned features, semantics, and dense representations. The research challenge is not replacing all geometry with learning; it is deciding which learned signal can be audited when the robot fails.", "chapter-29-application-reference-8.png"),
}

sections_30 = {
    "30.1": ("Navigation as embodied intelligence", "Navigation is where the agent's world model becomes a physical commitment. A route that ignores localization uncertainty, moving people, controller limits, or recovery policy is not a plan; it is a wish drawn on a map.", "A navigation stack has layers: global route, local trajectory, costmap, controller, safety monitor, and recovery behavior. Each layer can be correct locally and still fail globally if the interfaces are underspecified.", r"\pi^*=\arg\min_{\pi}\sum_t c(x_t,u_t)\quad\text{s.t.}\quad x_{t+1}=f(x_t,u_t),\; x_t\in X_{\mathrm{free}}", ["Convert the goal into a map frame and validate localization confidence.", "Plan a global path through known traversable space.", "Generate local velocity commands that respect dynamics and current obstacles.", "Trigger replanning or recovery when the state estimate, costmap, or controller error violates its bound."], """# Score a navigation run with execution-aware fields.
# A short path loses if it creates low clearance and many recoveries.
runs = [
    {"name": "short", "meters": 12.0, "clearance": 0.18, "recoveries": 2},
    {"name": "safe", "meters": 14.0, "clearance": 0.42, "recoveries": 0},
]
for run in runs:
    cost = run["meters"] + 8 / run["clearance"] + 5 * run["recoveries"]
    print(run["name"], round(cost, 1))""", "short 66.4\nsafe 33.0", "The scoring rule makes execution risk visible. The longer route wins because clearance and recovery count dominate the apparent path-length advantage of the short route.", "Nav2 provides the deployed pattern: planner server, controller server, behavior tree navigator, costmaps, lifecycle nodes, and recovery behaviors. Habitat and Isaac-style simulators help test policies before field deployment.", "Navigation research is converging on classical planning plus learned perception, foundation-model goal interpretation, and explicit safety monitors. The field is rediscovering that end-to-end policies still need replayable failures and comparable baselines.", "chapter-30-illustration-01.png"),
    "30.2": ("Graph search: BFS, Dijkstra, A*", "Grid maps and roadmaps become actionable only after the robot defines nodes, edges, and costs. Breadth-first search assumes equal edge cost, Dijkstra handles positive costs, and A* adds a heuristic that focuses expansion toward the goal.", "A* is correct when the heuristic is admissible, meaning it never overestimates the true remaining cost. Consistency gives an even stronger property: once a node is expanded, its best cost is known. Those guarantees matter when the graph stands in for physical space.", r"f(n)=g(n)+h(n),\quad 0\le h(n)\le h^*(n)", ["Build nodes from grid cells, topological places, or lattice states.", "Assign edge costs for distance, clearance, slope, turn penalty, and risk.", "Choose a heuristic whose units match the edge cost.", "Audit the found path against collision checks and controller feasibility."], """# Compute A* priorities for three frontier nodes.
# The admissible heuristic focuses search without changing cost units.
frontier = [
    {"node": "A", "g": 4.0, "h": 6.0},
    {"node": "B", "g": 7.0, "h": 2.0},
    {"node": "C", "g": 5.0, "h": 5.0},
]
ranked = sorted((n["g"] + n["h"], n["node"]) for n in frontier)
print(ranked)
print(f"expand={ranked[0][1]}")""", "[(9.0, 'B'), (10.0, 'A'), (10.0, 'C')]\nexpand=B", "The frontier ranking shows how A* combines traveled cost and heuristic cost. Node B expands first because its total priority is lowest, not because it is nearest in Euclidean distance alone.", "NetworkX can teach graph search in a few lines, while Nav2 global planner plugins apply the same idea to costmaps and robot goals. The shortcut saves manual priority queues, path reconstruction, and middleware integration.", "The frontier includes dynamic graph search, learned heuristics with admissibility checks, and multi-resolution planners that combine topological maps with local geometric grids.", "chapter-30-illustration-02.png"),
    "30.3": ("Sampling-based planning: RRT, RRT*, PRM", "High-dimensional robot motion rarely fits neatly into a grid. A manipulator, drone, or car-like robot may need to search continuous configuration space, where discretizing everything becomes expensive or misleading.", "Sampling-based planners trade exhaustive enumeration for random coverage. RRT grows a tree toward random samples, RRTstar rewires toward asymptotic optimality, and PRM builds a reusable roadmap. Collision checking is the core cost center.", r"q_{\mathrm{new}}=\mathrm{steer}(q_{\mathrm{near}},q_{\mathrm{rand}},\eta),\quad q_{\mathrm{new}}\in C_{\mathrm{free}}", ["Define configuration variables and bounds, including orientation when it affects collision.", "Sample states, find nearest neighbors, and steer with a step size or local planner.", "Reject edges that collide or violate dynamics.", "For RRTstar or PRM, rewire or connect neighbors to improve path quality."], """# One RRT steering step in a 2D configuration space.
# The step-size limit prevents the tree from jumping through obstacles.
import numpy as np

q_near = np.array([1.0, 1.0])
q_rand = np.array([4.0, 5.0])
eta = 1.5
direction = q_rand - q_near
q_new = q_near + eta * direction / np.linalg.norm(direction)
print(np.round(q_new, 2))""", "[1.9 2.2]", "The steering step moves from the nearest tree node toward the random sample by a bounded distance. Real planners add collision checking and kinodynamic feasibility before accepting the new node.", "OMPL provides maintained implementations of RRT, RRTstar, PRM, KPIECE, and kinodynamic planners, while MoveIt and Nav2 integrations connect planners to robots. The shortcut replaces custom nearest-neighbor, sampling, and collision-check plumbing.", "Current research focuses on learned sampling distributions, neural collision checking, kinodynamic planning for agile systems, and combining sampling planners with trajectory optimization for smoother execution.", "chapter-30-illustration-03.png"),
    "30.4": ("Local planning and obstacle avoidance", "A global path is too coarse for the next second of motion. The robot still has to choose velocities that avoid nearby obstacles, respect acceleration limits, and remain trackable by its controller.", "Dynamic Window Approach samples feasible velocity commands and scores their short rollouts. Potential fields define attractive and repulsive forces but can get trapped in local minima. Modern local planning combines costmap scoring, trajectory rollout, and controller constraints.", r"u^*=\arg\min_{u\in\mathcal U_{\mathrm{dyn}}}\alpha d_{\mathrm{goal}}+\beta c_{\mathrm{obstacle}}+\gamma e_{\mathrm{path}}", ["Build a local costmap from recent sensor data.", "Sample velocity commands allowed by current speed and acceleration limits.", "Roll each command forward over a short horizon.", "Reject collisions and choose the lowest scored command with enough clearance."], """# Score three local velocity commands.
# The selected command balances goal progress and obstacle clearance.
candidates = [
    {"v": 0.6, "goal": 2.0, "clearance": 0.20},
    {"v": 0.4, "goal": 2.4, "clearance": 0.55},
    {"v": 0.2, "goal": 3.0, "clearance": 0.80},
]
scores = []
for c in candidates:
    score = c["goal"] + 1.5 / c["clearance"] - 0.3 * c["v"]
    scores.append((round(score, 2), c["v"]))
print(scores)
print(f"command_v={min(scores)[1]}")""", "[(9.32, 0.6), (4.97, 0.4), (4.82, 0.2)]\ncommand_v=0.2", "The local scorer penalizes low clearance strongly enough to choose the slower command. This is the behavior a field robot needs when the global route passes near a hazard.", "Nav2 controller plugins, MPPI controllers, Regulated Pure Pursuit, and DWB controllers package local rollout and tracking behavior. The maintained path handles costmap integration, velocity limits, plugin loading, and behavior-tree coordination.", "Frontier work is pushing local planning toward risk-aware MPC, social navigation, learned traversability, and fast GPU rollout for dynamic scenes.", "chapter-30-illustration-04.png"),
    "30.5": ("Learned navigation policies", "Learned policies can map observations directly to actions, but a policy that beats a weak baseline in one simulator may still fail under sensor shift, new layouts, or a different robot body.", "A learned navigation policy should be evaluated against classical baselines, not in isolation. The input contract must name observation modalities, memory state, action space, training distribution, and the recovery layer that catches unsafe outputs.", r"\pi_\theta(a_t\mid o_{\le t},g),\quad J(\theta)=\mathbb E\left[\sum_t r(s_t,a_t)\right]", ["Define observation and action spaces in robot units.", "Train or fine-tune under scenario panels that include failures, not only success cases.", "Compare against graph search, local planning, and oracle-map baselines.", "Deploy with shields, confidence monitors, and fallback planners."], """# Compare a learned policy against a classical baseline panel.
# Success alone is not enough, intervention count changes the verdict.
panel = [
    {"method": "A_star_plus_DWB", "success": 0.86, "interventions": 0.08},
    {"method": "learned_policy", "success": 0.90, "interventions": 0.22},
]
for row in panel:
    score = row["success"] - 0.5 * row["interventions"]
    print(row["method"], round(score, 3))""", "A_star_plus_DWB 0.82\nlearned_policy 0.79", "The comparison penalizes interventions, so the higher raw success rate does not automatically win. Learned navigation needs construct-matched metrics with safety and recovery fields.", "Habitat, RoboTHOR, AI2-THOR, Isaac Lab, and PyTorch provide training and evaluation infrastructure, while Nav2 remains the practical baseline for deployed mobile robots. The shortcut is to run learned policies beside a classical stack, not instead of one by default.", "Research directions include vision-language navigation, foundation-model affordance maps, offline robot navigation datasets, and policy distillation into safety-monitored controllers.", "chapter-30-illustration-05.png"),
    "30.6": ("Language- and image-goal navigation", "A command such as find the red mug is not a coordinate. The robot must ground a linguistic or visual goal into possible regions, objects, viewpoints, and stopping conditions.", "Goal grounding adds an interpretation layer before planning. Language, image, and object detections produce candidate goals with confidence. The navigation stack then plans to viewpoints that can verify the goal rather than blindly driving to the nearest semantic guess.", r"g^*=\arg\max_g p(g\mid \text{language},\text{image},m),\quad \pi^*=\arg\min_\pi C(\pi,g^*)", ["Parse or embed the goal into object, room, relation, or image-match constraints.", "Generate candidate map targets with confidence and observability requirements.", "Plan to a viewpoint that can verify the goal.", "Stop only when perception evidence satisfies the goal predicate."], """# Choose a semantic goal candidate with confidence and travel cost.
# The best target balances semantic match with route cost.
candidates = [
    {"place": "kitchen_counter", "match": 0.82, "cost": 9.0},
    {"place": "desk", "match": 0.76, "cost": 4.0},
    {"place": "shelf", "match": 0.91, "cost": 15.0},
]
ranked = sorted(((c["match"] - 0.03 * c["cost"], c["place"]) for c in candidates), reverse=True)
print(ranked[0])""", "(0.64, 'kitchen_counter')", "The scoring rule chooses a goal candidate by combining semantic confidence and route cost. Real systems also include viewpoint quality, uncertainty, and a stopping verifier.", "CLIP-style embeddings, open-vocabulary detectors, semantic maps, Habitat simulators, and Nav2 planners can be joined into a language-goal navigation pipeline. The library shortcut handles perception embeddings and navigation execution while the book's evidence contract preserves auditability.", "The frontier is reliable grounding: open-vocabulary object search, embodied question answering, memory maps, and stopping rules that do not confuse a plausible detection with task completion.", None),
    "30.7": ("Field navigation under degraded sensing", "Field navigation starts when the assumptions break. Dust, darkness, wheel slip, GPS denial, glass, crowds, and map aging make the planner reason about confidence and fallback behavior.", "The field stack must define degraded-mode policies before deployment. It should know when to slow down, switch sensors, request teleoperation, hold position, or retreat. Continuing without a confidence bound is not autonomy; it is unmanaged risk.", r"u_t\in\mathcal U_{\mathrm{safe}}(b_t),\quad b_t=p(x_t,m,\text{hazards}\mid z_{\le t},u_{<t})", ["Monitor localization confidence, costmap freshness, controller error, and obstacle disagreement.", "Enter degraded mode when any monitored signal crosses its bound.", "Select a fallback policy: slow, stop, replan, retreat, ask for help, or switch sensor mode.", "Replay the event with synchronized sensors, transforms, commands, and recovery logs."], """# Select a degraded-mode response from confidence signals.
# The policy chooses the least risky action before full failure.
signals = {"localization": 0.42, "costmap_age_s": 3.8, "clearance_m": 0.31}
if signals["localization"] < 0.5:
    action = "hold_and_relocalize"
elif signals["costmap_age_s"] > 2.0:
    action = "slow_and_refresh_map"
elif signals["clearance_m"] < 0.35:
    action = "stop_and_replan"
else:
    action = "continue"
print(action)""", "hold_and_relocalize", "The degraded-mode policy acts before the robot has fully failed. Localization confidence is the first violated bound, so the system holds and relocalizes instead of trusting a stale route.", "Nav2 behavior trees, lifecycle management, costmap filters, OpenVINS or RTAB-Map localization, and ROS bag replay give the practical backbone for degraded sensing tests. The shortcut is a maintained safety and replay stack plus a project-specific risk policy.", "Frontier systems combine multimodal sensing, active perception, formal runtime monitors, and fleet-level failure mining. The hard research problem is making degraded-mode decisions explainable enough for safety review.", "chapter-30-application-reference-7.png"),
}

nexts_29 = {
    "29.1": ("section-29.2.html", "Section 29.2: Odometry and dead reckoning"),
    "29.2": ("section-29.3.html", "Section 29.3: Localization with particle filters"),
    "29.3": ("section-29.4.html", "Section 29.4: Mapping and occupancy grids"),
    "29.4": ("section-29.5.html", "Section 29.5: Graph-based and visual SLAM"),
    "29.5": ("section-29.6.html", "Section 29.6: Neural and Gaussian-splat SLAM"),
    "29.6": ("section-29.7.html", "Section 29.7: Map uncertainty"),
    "29.7": ("section-29.8.html", "Section 29.8: Modern SLAM systems and failure modes"),
    "29.8": ("../../part-6-embodied-perception/module-30-navigation-and-path-planning/index.html", "Chapter 30: Navigation and Path Planning"),
}
nexts_30 = {
    "30.1": ("section-30.2.html", "Section 30.2: Graph search"),
    "30.2": ("section-30.3.html", "Section 30.3: Sampling-based planning"),
    "30.3": ("section-30.4.html", "Section 30.4: Local planning"),
    "30.4": ("section-30.5.html", "Section 30.5: Learned navigation policies"),
    "30.5": ("section-30.6.html", "Section 30.6: Language- and image-goal navigation"),
    "30.6": ("section-30.7.html", "Section 30.7: Field navigation under degraded sensing"),
    "30.7": ("../../part-7-language-vision-and-action/module-31-language-guided-embodied-agents/index.html", "Chapter 31: Language-Guided Embodied Agents"),
}

for sec, values in sections_29.items():
    next_href, next_title = nexts_29[sec]
    replace_main(M29 / f"section-{sec}.html", body_29(M29, sec, *values, slam_bibs, next_href, next_title))

for sec, values in sections_30.items():
    next_href, next_title = nexts_30[sec]
    replace_main(M30 / f"section-{sec}.html", body_30(M30, sec, *values, nav_bibs, next_href, next_title))
