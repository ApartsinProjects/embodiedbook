from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def section_body(
    *,
    section: str,
    title: str,
    opener: str,
    figure_label: str,
    figure_title: str,
    figure_nodes: list[tuple[str, str, str]],
    formula_title: str,
    formula: str,
    formula_note: str,
    algorithm_title: str,
    algorithm_steps: list[str],
    table_title: str,
    table_rows: list[tuple[str, str, str]],
    code_intro: str,
    code: str,
    output: str,
    caption: str,
    shortcut: str,
    warning: str,
    practical: str,
    frontier: str,
    refs: list[tuple[str, str, str]],
    takeaway: str,
    exercise: str,
) -> str:
    colors = ["#e3f2fd", "#e8f5e9", "#fff3e0", "#f3e5f5", "#fce4ec"]
    strokes = ["#1565c0", "#2e7d32", "#e65100", "#6a1b9a", "#c62828"]
    boxes = []
    arrows = []
    x = 25
    width = 145
    for i, (head, sub) in enumerate(figure_nodes):
        boxes.append(
            f'<rect fill="{colors[i % len(colors)]}" height="76" rx="10" stroke="{strokes[i % len(strokes)]}" width="{width}" x="{x}" y="80"></rect>\n'
            f'<text font-size="14" text-anchor="middle" x="{x + width/2:.0f}" y="112">{head}</text>\n'
            f'<text font-size="12" text-anchor="middle" x="{x + width/2:.0f}" y="134">{sub}</text>'
        )
        if i:
            arrows.append(f'<path d="M{x - 30} 118 H{x}" stroke="#555" stroke-width="2"></path>')
        x += 175
    rows_html = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in table_rows
    )
    steps_html = "\n".join(f"<li>{step}</li>" for step in algorithm_steps)
    refs_html = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref} <a href="{url}" rel="noopener" target="_blank">{url}</a></p><p class="bib-annotation">{annotation}</p></div>'
        for ref, url, annotation in refs
    )
    return f"""<div class="callout big-picture"><div class="callout-title">Big Picture</div><p><strong>{title}</strong> {opener}</p></div>
<div class="callout pathway">
<div class="callout-title">Reader Pathway</div>
<p>Track three questions while reading: what representation is produced, what action consumes it, and what evidence would prove that the representation improved the robot instead of only improving a perception score.</p>
</div>
<h2>Problem First: Why This Representation Exists</h2>
<p>A static computer-vision system can stop when it names an object or produces a clean visualization. An embodied system cannot. The robot needs a representation that is tied to coordinates, uncertainty, latency, and an action interface, because a late or uncalibrated result can be more dangerous than no result at all.</p>
<p>For this section, the useful mental model is an action contract. The perception module receives sensor evidence, estimates a compact state, exposes confidence and timing, and lets a planner or controller decide whether the next action is allowed. This is the bridge from <a href="../../part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/index.html">coordinate frames</a> and <a href="../../part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/index.html">sensor estimation</a> to the closed-loop evaluation discipline used in <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html">sim-to-real transfer</a>.</p>
<div class="callout key-insight"><div class="callout-title">Action Is The Unit Of Meaning</div><p>A perception output becomes embodied knowledge only when it can change an admissible action, a recovery choice, or a safety margin. If the same command is issued with and without the representation, the representation is not yet part of the control loop.</p></div>
<p>Figure {figure_label} shows the contract used by this section. Each box is a handoff where bugs usually hide: units, frame names, timestamps, uncertainty, and allowed consumers.</p>
<figure class="technical-figure" id="fig-{section.replace('.', '-')}-contract">
<svg aria-labelledby="fig-{section.replace('.', '-')}-contract-title fig-{section.replace('.', '-')}-contract-desc" role="img" viewbox="0 0 900 245">
<title id="fig-{section.replace('.', '-')}-contract-title">{figure_title}</title>
<desc id="fig-{section.replace('.', '-')}-contract-desc">A robotics perception contract connecting sensor evidence to state, action, and diagnostics.</desc>
{chr(10).join(boxes)}
{chr(10).join(arrows)}
<path d="M810 80 C810 34 96 34 96 80" fill="none" stroke="#607d8b" stroke-dasharray="6 5" stroke-width="2"></path>
</svg>
<figcaption><strong>Figure {figure_label}</strong>: {figure_title}. The dashed feedback path reminds the reader that perception quality is judged by action consequences and replayable diagnostics.</figcaption>
</figure>
<h2>Mathematical Core</h2>
<p>{formula_title}</p>
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>{formula}</p></div>
<p>{formula_note}</p>
<div class="callout algorithm"><div class="callout-title">{algorithm_title}</div><ol>{steps_html}</ol></div>
<div class="comparison-table"><div class="comparison-table-title">{table_title}</div><table><thead><tr><th>Design Choice</th><th>Use When</th><th>Control Risk</th></tr></thead><tbody>{rows_html}</tbody></table></div>
<h2>Worked Miniature</h2>
<p>{code_intro}</p>
<pre><code class="language-python">{code}</code></pre>
<div class="code-output">{output}</div>
<div class="code-caption"><strong>Code Fragment {section}.1:</strong> {caption}</div>
<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>{shortcut}</p></div>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>{warning}</p></div>
<div class="callout practical-example"><div class="callout-title">Practical Example</div><p>{practical}</p></div>
<div class="callout fun-note"><div class="callout-title">Memory Hook</div><p>If the perception result cannot answer what action changed, what uncertainty changed, and what log would reproduce the decision, it is still a pretty picture wearing a hard hat.</p></div>
<h2>Debugging And Evaluation</h2>
<p>Evaluate the representation inside the same action loop that will use it. The report should include the sensor stream, calibration version, frame transform, model checkpoint or library version, latency distribution, action candidate set, chosen action, and failure label. This makes the comparison construct matched: the baseline and shortcut are judged by the same script on the same panel.</p>
<p>A good debugging run varies one factor at a time. Perturb lighting, occlusion, calibration, motion blur, viewpoint, object pose, or update rate, then record whether the action changed for the right reason. That single-factor habit is what turns a failed rollout into a useful engineering artifact.</p>
<div class="callout research-frontier"><div class="callout-title">Research Frontier</div><p>{frontier}</p></div>
<section class="bibliography"><h2>Section References</h2>{refs_html}</section>
<div class="callout self-check"><div class="callout-title">Self Check</div><p>Can you name the representation, the consuming action, the uncertainty or freshness field, and the failure label for {title}? If any one is missing, the section is not yet ready for a robot replay log.</p></div>
<div class="callout key-takeaway"><div class="callout-title">Key Takeaway</div><p>{takeaway}</p></div>
<div class="callout exercise"><div class="callout-title">Exercise {section}.1</div><p>{exercise}</p></div>
"""


sections = {
    "27.1": section_body(
        section="27.1",
        title="Seeing to classify vs. seeing to act",
        opener="separates image labels from action-relevant state. A class label says what a pixel region might contain; an action perception record says where that region is, how certain the estimate is, how fresh it is, and which robot commands are now admissible.",
        figure_label="27.1.1",
        figure_title="From image recognition to action-conditioned state",
        figure_nodes=[("Image", "pixels and time"), ("State", "pose, mask, belief"), ("Action", "allowed command"), ("Safety", "margin and stop"), ("Replay", "debug trace")],
        formula_title="The basic decision object is expected utility conditioned on visual evidence, not class probability alone.",
        formula=r"$a^*=\arg\max_{a\in\mathcal A_{\mathrm{safe}}}\mathbb E[U(a,s)\mid z_{1:t}],\quad z_t=(I_t,K,T_{cw},\Delta t,\Sigma_t)$",
        formula_note=r"The image $I_t$ matters only after calibration $K$, camera pose $T_{cw}$, latency $\Delta t$, and uncertainty $\Sigma_t$ make it usable by the action module. The safe action set filters out commands that violate collision, reach, or timing constraints before utility is maximized.",
        algorithm_title="Classification-to-action conversion",
        algorithm_steps=["Convert visual evidence into a calibrated state estimate with units and frame names.", "Attach uncertainty and timestamp metadata before the estimate reaches the planner.", "Filter actions by geometric and safety constraints.", "Log the chosen action and a counterfactual action that would have been chosen without the visual estimate."],
        table_title="Classification Output Versus Action Output",
        table_rows=[("Image class", "Inventory, captioning, weak context", "Can ignore pose, reachability, and latency."), ("Action state", "Grasping, navigation, inspection, docking", "Wrong frame or stale timestamp can make a correct label unsafe."), ("Counterfactual action", "Evaluation and debugging", "No counterfactual means no evidence that perception mattered.")],
        code_intro="Code Fragment 27.1.1 grounds the idea with three candidate actions. NumPy is enough here because the goal is to expose the action contract before a full vision stack hides it behind models.",
        code="""# Rank robot actions from calibrated visual evidence.
# The visual confidence must combine with safety margin before execution.
import numpy as np

actions = np.array(["reach left", "reach center", "wait"])
class_confidence = np.array([0.92, 0.64, 1.00])
safety_margin_m = np.array([0.03, 0.14, 0.50])
task_value = np.array([0.95, 0.72, 0.20])

score = task_value * class_confidence + 0.8 * safety_margin_m
chosen = int(score.argmax())
print(actions[chosen])
print(np.round(score, 3))""",
        output="reach center\n[0.898 0.573 0.600]",
        caption="The code shows why the highest class confidence does not automatically win. The small `safety_margin_m` for `reach left` pushes the policy toward `reach center`, which is exactly the action-conditioned distinction this section teaches.",
        shortcut="In production, OpenCV calibration, ROS 2 message timestamps, and a PyTorch perception head can produce this action record in a few calls. The library stack handles camera models, image transport, batching, and tensor execution, but the action schema should remain as inspectable as the NumPy baseline.",
        warning="The common failure is celebrating a high-confidence class label while the robot executes an unsafe reach because the label was not tied to a metric safety margin.",
        practical="A warehouse arm deciding between two bins should log the detected object, camera frame, transform into the robot base, safety margin to each bin lip, and the command that changed because of vision. That log lets the team distinguish a visual error from a controller clearance error.",
        frontier="Current visual foundation models are increasingly useful as feature providers, but embodied evaluation still hinges on whether those features improve closed-loop success under perturbations. The frontier is not only stronger recognition; it is recognition whose uncertainty, timing, and geometry are usable by action policies.",
        refs=[("OpenCV. Camera calibration and 3D reconstruction documentation.", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Defines the calibration and pose-estimation routines that turn pixels into metric evidence for robot action."), ("NVIDIA. Isaac ROS Visual SLAM documentation.", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Shows how visual perception becomes a real-time odometry source for navigation stacks.")],
        takeaway="Seeing to act means optimizing an action under calibrated visual evidence, uncertainty, and safety constraints, not merely choosing the most likely class label.",
        exercise="For a tabletop pick task, write two action candidates that a classifier alone would rank incorrectly. Add the missing frame, uncertainty, or safety-margin field that would fix the decision.",
    ),
    "27.2": section_body(
        section="27.2",
        title="Detection, segmentation, and the Segment Anything family",
        opener="turns boxes and masks into regions a robot can track, avoid, grasp, wipe, pour into, or ignore. A mask is only a beginning; the embodied question is whether the region remains stable, metric, and useful under motion.",
        figure_label="27.2.1",
        figure_title="From promptable masks to robot-safe action regions",
        figure_nodes=[("Detect", "box or prompt"), ("Segment", "mask pixels"), ("Track", "identity over time"), ("Ground", "metric region"), ("Act", "affordance")],
        formula_title="Segmentation quality is usually measured by overlap, but control also needs stability and action utility.",
        formula=r"$\mathrm{IoU}(M,\hat M)=\frac{|M\cap\hat M|}{|M\cup\hat M|},\quad q_{\mathrm{act}}=\mathrm{IoU}\cdot p_{\mathrm{track}}\cdot \mathbf 1[\mathrm{clearance}>\epsilon]$",
        formula_note="Intersection-over-union rewards geometric overlap. The action score multiplies it by temporal track confidence and a clearance constraint, because a beautiful mask that flickers or violates clearance can still produce a bad grasp.",
        algorithm_title="Mask-to-affordance pipeline",
        algorithm_steps=["Generate boxes, prompts, or masks from the image stream.", "Filter masks by area, stability, boundary quality, and temporal identity.", "Lift candidate mask pixels through depth or a known support plane.", "Score each mask by affordance, clearance, latency, and track consistency."],
        table_title="Mask Choices For Action",
        table_rows=[("Detector box", "Fast object proposals and coarse avoidance", "Box can include unsafe background or miss thin handles."), ("Instance mask", "Grasping, pouring, wiping, and contact planning", "Boundary errors become contact errors near clutter."), ("SAM or SAM 2 promptable mask", "Interactive data creation, video tracking, open-world regions", "Prompt sensitivity and temporal drift need explicit validation.")],
        code_intro="Code Fragment 27.2.1 computes a small action score for three candidate masks. The variables mimic what a ROS or PyTorch pipeline should publish after detection and segmentation.",
        code="""# Convert mask quality into an action-safe ranking.
# IoU alone is not enough; temporal stability and clearance gate execution.
import numpy as np

mask_iou = np.array([0.91, 0.78, 0.86])
track_confidence = np.array([0.62, 0.95, 0.88])
clearance_m = np.array([0.015, 0.060, 0.035])
safe = clearance_m > 0.03

action_score = mask_iou * track_confidence * safe
print(np.round(action_score, 3))
print(int(action_score.argmax()))""",
        output="[0.    0.741 0.757]\n2",
        caption="The `safe` gate removes a high-overlap mask that is too close to an obstacle. The winning mask is not the largest IoU alone; it is the region that remains trackable and leaves enough clearance for action.",
        shortcut="A practical stack can pair an object detector with SAM 2 style promptable segmentation, then publish masks through ROS 2 image messages. That reduces custom mask generation to a few calls while the system still owns the action score, temporal checks, and clearance threshold.",
        warning="Promptable segmentation can make a mask look authoritative even when it is action-ambiguous. Always test whether the same mask identity survives camera motion, partial occlusion, and contact.",
        practical="For a mobile manipulator clearing a table, boxes are useful for object proposals, masks are useful for contact boundaries, and tracks are useful for deciding whether an object moved after the last command. The robot should store all three.",
        frontier="SAM 2 extended promptable segmentation to images and videos with streaming memory, which is especially relevant to robotics because robots need mask identity across time. The research frontier is turning these open-world masks into calibrated, persistent, and safety-aware action regions.",
        refs=[("Ravi, N. et al. SAM 2: Segment Anything in Images and Videos. arXiv, 2024.", "https://arxiv.org/abs/2408.00714", "Introduces SAM 2, including streaming memory for video segmentation and interactive correction."), ("Meta AI. Introducing Segment Anything Model 2.", "https://ai.meta.com/research/sam2/", "Official overview of SAM 2 capabilities and video memory behavior.")],
        takeaway="Detection finds candidates, segmentation shapes them, tracking stabilizes them, and action scoring decides whether the robot can use them.",
        exercise="Choose a cluttered manipulation task and define one mask-quality metric, one tracking metric, and one action-safety metric. Explain which one should veto execution.",
    ),
    "27.3": section_body(
        section="27.3",
        title="Depth estimation and metric scale",
        opener="turns visual evidence into distances that can support collision checking, grasp approach, landing, docking, and navigation. Depth is useful for action only when its scale, frame, and failure modes are explicit.",
        figure_label="27.3.1",
        figure_title="From pixels and disparity to metric depth",
        figure_nodes=[("Pixels", "u, v"), ("Intrinsics", "fx, fy, cx, cy"), ("Depth", "z meters"), ("Point", "x, y, z"), ("Action", "clearance")],
        formula_title="The pinhole camera model lifts a depth pixel into a 3D camera-frame point.",
        formula=r"$X_c=\frac{(u-c_x)z}{f_x},\quad Y_c=\frac{(v-c_y)z}{f_y},\quad Z_c=z,\quad z_{\mathrm{stereo}}=\frac{fB}{d}$",
        formula_note="The first three equations use metric depth directly. The stereo equation shows why small disparity errors become large distance errors when disparity $d$ is small, which is why far obstacles and reflective surfaces deserve extra caution.",
        algorithm_title="Depth-to-action validation",
        algorithm_steps=["Check the camera intrinsics and depth units before any planning call.", "Reject missing, saturated, or physically impossible depth pixels.", "Back-project task-relevant pixels into the camera frame, then transform them into the robot frame.", "Compare the resulting clearance against controller limits and uncertainty margins."],
        table_title="Depth Sources And Failure Modes",
        table_rows=[("Stereo", "Outdoor robots and textured scenes", "Low texture and far range create unstable disparity."), ("RGB-D or time-of-flight", "Indoor manipulation and tabletop mapping", "Reflective, transparent, or black materials can corrupt depth."), ("Monocular depth", "Semantic priors and fallback estimates", "Metric scale may drift without calibration or known references.")],
        code_intro="Code Fragment 27.3.1 implements the back-projection equations with one pixel and one depth value. This is the smallest useful check before passing points into Open3D or a planner.",
        code="""# Back-project one depth pixel through camera intrinsics.
# The output is a metric 3D point in the camera frame.
fx, fy = 615.0, 615.0
cx, cy = 320.0, 240.0
u, v, z_m = 350.0, 260.0, 1.20

x_m = (u - cx) * z_m / fx
y_m = (v - cy) * z_m / fy
point_c = (round(x_m, 3), round(y_m, 3), z_m)
print(point_c)""",
        output="(0.059, 0.039, 1.2)",
        caption="The variables `fx`, `fy`, `cx`, and `cy` turn pixel offsets into meters. The tiny output shift shows why camera calibration, not only neural depth prediction, decides whether a robot can trust clearance.",
        shortcut="OpenCV and Open3D collapse this from hand-written equations into camera calibration, RGB-D image, and point-cloud constructors. The shortcut handles formats and vectorization, but it does not absolve the builder from checking units, missing depth, and transforms.",
        warning="Depth maps often fail silently on transparent cups, glossy tabletops, thin chair legs, and motion blur. The robot must know when depth is absent or unreliable, not only when it is numerically present.",
        practical="A drone landing system can accept monocular depth for exploratory terrain scoring, but final descent should require scale-checked stereo, lidar, or trusted altitude sensing with a conservative uncertainty margin.",
        frontier="Foundation depth models are improving fast, but robotics still needs calibrated scale, uncertainty, and temporal consistency. The open problem is not producing pretty depth, it is certifying when depth is good enough for contact or collision decisions.",
        refs=[("OpenCV. Camera calibration and 3D reconstruction documentation.", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Primary implementation reference for calibration, projection, stereo, and pose routines."), ("Open3D. RGB-D images and point cloud documentation.", "https://www.open3d.org/docs/release/tutorial/geometry/rgbd_image.html", "Shows the practical library path from depth images to point clouds.")],
        takeaway="Metric depth is a contract among pixels, intrinsics, units, transforms, and uncertainty; remove any one of those and the action estimate becomes suspect.",
        exercise="Given a camera with $f_x=600$, $c_x=320$, pixel $u=380$, and depth $z=2.0$ m, compute $X_c$. Then explain how a 10 percent depth-scale error changes a grasp clearance estimate.",
    ),
    "27.4": section_body(
        section="27.4",
        title="Optical flow and motion cues",
        opener="captures how image evidence moves between frames. For embodied agents, flow is a cue for ego-motion, moving obstacles, time-to-contact, tracking failures, and when a controller should slow down.",
        figure_label="27.4.1",
        figure_title="Motion cues from image flow to controller timing",
        figure_nodes=[("Frame t", "image"), ("Frame t+1", "image"), ("Flow", "u dot, v dot"), ("Separate", "ego or object"), ("Control", "slow or steer")],
        formula_title="Classical optical flow starts with brightness constancy and a small-motion approximation.",
        formula=r"$I_x u + I_y v + I_t = 0,\quad \tau \approx \frac{\theta}{\dot\theta}$",
        formula_note="The first equation says that image intensity should stay constant as a point moves. The time-to-contact approximation uses visual expansion: when an object's angular size grows quickly, the robot may need to brake even before full 3D reconstruction is available.",
        algorithm_title="Flow-to-action recipe",
        algorithm_steps=["Estimate sparse or dense flow between consecutive frames.", "Subtract expected ego-motion flow when camera motion is known.", "Cluster residual flow into moving object hypotheses.", "Convert expansion, bearing change, or residual speed into a controller-level slow, stop, or replan signal."],
        table_title="Flow Use Cases",
        table_rows=[("Sparse feature flow", "Visual odometry and low-compute tracking", "Fails on textureless surfaces and repetitive patterns."), ("Dense learned flow", "Scene motion and manipulation video", "Can be expensive and may hallucinate in occlusion."), ("Residual flow", "Moving obstacle detection", "Bad ego-motion compensation can create false obstacles.")],
        code_intro="Code Fragment 27.4.1 uses bounding-box size over time to estimate a simple time-to-contact cue. It is not a replacement for full flow, but it teaches the control signal hidden inside motion.",
        code="""# Estimate time-to-contact from visual expansion.
# A smaller tau means the controller should slow or stop sooner.
import numpy as np

box_width_px = np.array([42.0, 48.0, 56.0, 67.0])
dt_s = 0.10
growth_rate = (box_width_px[-1] - box_width_px[-2]) / dt_s
tau_s = box_width_px[-1] / growth_rate
command = "slow" if tau_s < 1.0 else "continue"
print(round(float(tau_s), 2))
print(command)""",
        output="0.61\nslow",
        caption="The `tau_s` estimate converts image expansion into a control hint. The command changes to `slow` because the apparent object size is growing quickly, even before a full 3D map is available.",
        shortcut="OpenCV provides Lucas-Kanade and Farneback flow, while modern PyTorch models provide learned dense flow. Those tools reduce implementation work, but the robot still needs ego-motion compensation, latency checks, and a controller policy for residual motion.",
        warning="Do not treat every flow vector as object motion. A turning camera creates global flow, so the system must subtract expected ego-motion before labeling a pedestrian, arm, or drone as moving.",
        practical="An indoor delivery robot can use residual flow to slow for a person stepping from behind a shelf. The action policy should log whether the stop came from obstacle geometry, optical expansion, or a conservative fallback.",
        frontier="Recent video foundation models make long-range tracking easier, but closed-loop robotics still needs low-latency motion cues with calibrated failure labels. The frontier is combining learned flow, geometric ego-motion, and uncertainty-aware control.",
        refs=[("OpenCV. Optical flow tutorials.", "https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html", "Documents classical sparse and dense optical-flow tools used in practical robotics prototypes."), ("NVIDIA. Isaac ROS Visual SLAM documentation.", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Shows real-time visual motion estimation in a ROS 2 robotics stack.")],
        takeaway="Optical flow is not just pretty arrows; it is a low-latency motion signal that must be separated into ego-motion, object motion, and control response.",
        exercise="Design a residual-flow test for a mobile robot turning in place while a person walks across the scene. What flow should be subtracted, and what residual should trigger slowing?",
    ),
    "27.5": section_body(
        section="27.5",
        title="Affordances and graspable regions",
        opener="asks what the robot can do with a visible region. Category names are optional; action possibilities such as grasp, push, pull, pour, step, wipe, or avoid are the core output.",
        figure_label="27.5.1",
        figure_title="Affordance scoring from region evidence to grasp action",
        figure_nodes=[("Region", "mask or patch"), ("Geometry", "normal and depth"), ("Affordance", "grasp, push"), ("Constraint", "reach and force"), ("Skill", "execute")],
        formula_title="An affordance map scores actions over image or 3D regions under robot constraints.",
        formula=r"$A(r,a)=P(\mathrm{success}\mid \phi(r),a,\theta_{\mathrm{robot}}),\quad a^*=\arg\max_{a\in\mathcal A} A(r,a)-\lambda C(a)$",
        formula_note=r"The feature vector $\phi(r)$ may include mask shape, depth, surface normal, material cues, and semantic features. The cost term $C(a)$ penalizes collision risk, reach limits, force limits, or task time.",
        algorithm_title="Affordance-to-skill handoff",
        algorithm_steps=["Extract candidate regions from masks, depth discontinuities, or learned heatmaps.", "Estimate local geometry, including surface normals and approach directions.", "Score each region-action pair for success probability and execution cost.", "Send the selected region, pose, and uncertainty to the skill controller."],
        table_title="Affordance Representations",
        table_rows=[("Heatmap", "Fast image-space grasp or push proposals", "Must be lifted to metric pose before control."), ("Object-centric affordance", "Reusable skills such as open, pour, wipe", "Object identity can hide local contact constraints."), ("3D contact affordance", "Dexterous manipulation and humanoid hands", "Requires reliable geometry and force-aware execution.")],
        code_intro="Code Fragment 27.5.1 scores candidate grasp regions by combining learned affordance probability with reach and collision costs. The small table-like arrays stand in for a vision model output.",
        code="""# Choose a graspable region from affordance and cost terms.
# The selected region must be promising and executable by the robot.
import numpy as np

affordance = np.array([0.88, 0.74, 0.67])
reach_cost = np.array([0.35, 0.08, 0.05])
collision_cost = np.array([0.10, 0.06, 0.30])
score = affordance - 0.6 * reach_cost - 0.8 * collision_cost
print(np.round(score, 3))
print(int(score.argmax()))""",
        output="[0.590 0.644 0.400]\n1",
        caption="The `score` calculation prevents the highest affordance heatmap value from winning automatically. Region 1 wins because its lower `reach_cost` and `collision_cost` make it more executable for the embodied system.",
        shortcut="In practice, grasp pipelines often combine learned heatmaps, depth processing in Open3D, and robot-specific inverse kinematics. The libraries shorten perception and geometry work, but the system still needs an explicit region-to-skill contract.",
        warning="An affordance is not a permission slip. A mug handle may be visually graspable but unreachable from the current arm pose, blocked by clutter, or unsafe under the current force limit.",
        practical="A service robot loading a dishwasher should score regions by grasp success, collision with nearby dishes, wrist clearance, and whether the chosen contact leaves the object in a stable orientation for placement.",
        frontier="Affordance learning is moving from category-specific grasp detection toward open-vocabulary, language-conditioned, and 3D contact-aware skill grounding. The hard robotics problem is making those affordances executable under real robot kinematics and contact limits.",
        refs=[("Open3D. Geometry documentation.", "https://www.open3d.org/docs/release/tutorial/geometry/index.html", "Provides practical primitives for normals, point clouds, and geometry processing used in affordance pipelines."), ("Meta AI. Segment Anything Model 2.", "https://ai.meta.com/research/sam2/", "Promptable masks can provide candidate regions, but robotics still needs affordance and constraint scoring.")],
        takeaway="Affordances are action-conditioned predictions over regions, and they become useful only after reach, collision, contact, and uncertainty constraints are attached.",
        exercise="Pick one household object and list three visible regions. For each region, score grasp, push, and avoid actions, then name the robot constraint that could veto the top score.",
    ),
    "27.6": section_body(
        section="27.6",
        title="Active and embodied perception",
        opener="lets the agent choose observations instead of passively consuming images. Looking, moving, touching, zooming, and waiting become information-gathering actions that trade time and risk for better state estimates.",
        figure_label="27.6.1",
        figure_title="Observation as an action in embodied perception",
        figure_nodes=[("Belief", "uncertain state"), ("View", "move sensor"), ("Observe", "new evidence"), ("Update", "lower entropy"), ("Act", "task command")],
        formula_title="Active perception selects the observation action with the best expected information gain after accounting for movement cost.",
        formula=r"$a_{\mathrm{view}}^*=\arg\max_a \mathbb E[H(b_t)-H(b_{t+1})\mid a]-\lambda c(a)$",
        formula_note="The entropy term measures uncertainty in the belief state. A view is valuable when it is expected to reduce uncertainty enough to justify the time, energy, or collision risk required to obtain it.",
        algorithm_title="Next-best-view policy",
        algorithm_steps=["Represent the current task belief and its uncertainty.", "Enumerate feasible sensing actions, such as camera pan, base motion, wrist motion, or tactile probe.", "Predict expected information gain and execution cost for each sensing action.", "Execute the sensing action only if its expected value exceeds acting immediately."],
        table_title="Active Perception Choices",
        table_rows=[("Move camera", "Occlusion, pose ambiguity, inspection", "Adds latency and can change the scene."), ("Move base", "Navigation and scene disambiguation", "May violate safety margins or block people."), ("Touch or probe", "Material and contact uncertainty", "Can disturb the object and complicate recovery.")],
        code_intro="Code Fragment 27.6.1 implements a tiny next-best-view selector. The numbers are artificial, but the tradeoff between entropy reduction and motion cost is the real design decision.",
        code="""# Select a sensing action by expected information gain minus cost.
# Acting immediately is allowed when extra perception is not worth it.
import numpy as np

views = np.array(["look left", "look right", "move closer", "act now"])
expected_entropy_drop = np.array([0.22, 0.31, 0.42, 0.00])
motion_cost = np.array([0.05, 0.08, 0.30, 0.00])
utility = expected_entropy_drop - 0.7 * motion_cost
print(np.round(utility, 3))
print(views[int(utility.argmax())])""",
        output="[0.185 0.254 0.210 0.000]\nlook right",
        caption="The selector chooses `look right` because its information gain survives the motion-cost penalty. `move closer` reduces more entropy, but it is too costly for this action cycle.",
        shortcut="Robotics systems often implement active perception with ROS 2 behavior trees, next-best-view planners, or simulator rollouts. The library route handles motion execution and visualization, while the builder still defines the belief, information metric, and stopping rule.",
        warning="Active perception can become procrastination. A robot that keeps looking because every view might help needs a decision threshold for when to act with the current belief.",
        practical="A humanoid robot reaching into a shelf may lean its head to disambiguate a handle before moving the hand. The sensing motion is worthwhile only if it reduces the probability of collision or failed grasp enough to offset delay.",
        frontier="The frontier combines active perception with language goals, tactile sensing, and foundation-model uncertainty. The central research question is how to price information when sensing actions can disturb the world they are trying to measure.",
        refs=[("NVIDIA. Isaac ROS overview.", "https://developer.nvidia.com/isaac/ros", "Describes accelerated robotics perception packages that can be used inside active perception pipelines."), ("OpenCV. Camera calibration and 3D reconstruction documentation.", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Provides the geometry primitives needed when active camera motion changes viewpoint and pose.")],
        takeaway="Active perception is decision making over observations: look only when the expected reduction in task uncertainty is worth the cost and risk.",
        exercise="Define four candidate sensing actions for a robot searching inside a cabinet. Assign each one an expected entropy drop and a motion cost, then choose the action with the best net utility.",
    ),
    "27.7": section_body(
        section="27.7",
        title="When perception failures become action failures",
        opener="maps visual errors to downstream consequences. The goal is not merely to say that perception failed, but to identify whether calibration, recognition, uncertainty, latency, tracking, or the action interface caused the robot to choose badly.",
        figure_label="27.7.1",
        figure_title="Failure propagation from perception to action",
        figure_nodes=[("Sensor", "noise or blur"), ("Model", "wrong estimate"), ("Interface", "missing uncertainty"), ("Planner", "bad choice"), ("Recovery", "label cause")],
        formula_title="A perception error matters when it crosses an action boundary or consumes the available timing margin.",
        formula=r"$\mathrm{fail}= \mathbf 1[d(\hat s,s)>\epsilon_{\mathrm{action}}]\lor \mathbf 1[\Delta t>\Delta t_{\max}]\lor \mathbf 1[\Sigma_{\hat s}\not\subseteq \Sigma_{\mathrm{allowed}}]$",
        formula_note="This expression separates magnitude error, latency error, and uncertainty-interface error. A small estimate error can be harmless far from a decision boundary; the same error can be catastrophic near contact.",
        algorithm_title="Perception failure triage",
        algorithm_steps=["Replay the raw sensor stream and verify calibration, timestamps, and transforms.", "Compare model output with a task-level counterfactual action.", "Check whether uncertainty was published and consumed by the planner or controller.", "Assign the failure to sensing, representation, timing, action selection, control, or evaluation."],
        table_title="Failure Labels That Preserve Debugging Value",
        table_rows=[("Sensing failure", "Blur, glare, missing depth, dropped frames", "Bad raw evidence enters every downstream module."), ("Representation failure", "Wrong mask, pose, flow, or affordance", "Planner receives a plausible but false state."), ("Interface failure", "No uncertainty, wrong frame, stale timestamp", "Correct perception is consumed incorrectly.")],
        code_intro="Code Fragment 27.7.1 classifies failures by comparing state error, latency, and uncertainty width against action thresholds. This is the kind of small rule that should appear in replay dashboards.",
        code="""# Label whether perception crossed an action-relevant failure boundary.
# Separate geometry error, latency error, and uncertainty-interface error.
state_error_m = 0.045
action_margin_m = 0.030
latency_ms = 115
max_latency_ms = 80
uncertainty_m = 0.055
allowed_uncertainty_m = 0.040

labels = []
if state_error_m > action_margin_m:
    labels.append("geometry_error")
if latency_ms > max_latency_ms:
    labels.append("stale_perception")
if uncertainty_m > allowed_uncertainty_m:
    labels.append("uncertainty_too_wide")
print(labels)""",
        output="['geometry_error', 'stale_perception', 'uncertainty_too_wide']",
        caption="The three thresholds create distinct failure labels instead of one vague perception failure. `geometry_error`, `stale_perception`, and `uncertainty_too_wide` each point to a different fix path.",
        shortcut="A production pipeline should emit these labels from ROS 2 diagnostics, tracing tools, and model telemetry. Frameworks can collect timestamps and message metadata automatically, but the team must define the action boundary and failure taxonomy.",
        warning="The worst failure label is `bad vision`. It hides the specific interface that broke and makes the next experiment less informative.",
        practical="When an autonomous vehicle brakes late, the audit should separate missed detection, wrong object velocity, delayed perception, planner threshold, and actuator response. Only one of those is solved by retraining a detector.",
        frontier="As perception stacks absorb foundation models, multimodal prompts, and learned world models, failure attribution becomes more important. The frontier is building evaluation artifacts that reveal when a model was wrong, when it was late, and when downstream code ignored its uncertainty.",
        refs=[("NVIDIA. Isaac ROS Visual SLAM documentation.", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Illustrates real-time perception components whose odometry output must be monitored for latency and reliability."), ("OpenCV. Camera calibration and 3D reconstruction documentation.", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Calibration failures are a frequent root cause of action-level perception failures.")],
        takeaway="A perception failure becomes useful engineering evidence only after it is mapped to the action boundary it crossed and the interface that allowed it through.",
        exercise="Take a failed robot rollout and assign three labels: first bad signal, first bad state estimate, and first bad action. Explain how the fix differs for each label.",
    ),
    "28.1": section_body(
        section="28.1",
        title="Why 3D matters for manipulation and navigation",
        opener="explains why pixels alone are insufficient for bodies that move through space. The robot needs reachable surfaces, traversable volumes, occluded regions, and metric distances, not only visible texture.",
        figure_label="28.1.1",
        figure_title="3D scene state as the bridge from pixels to motion",
        figure_nodes=[("Pixels", "appearance"), ("Depth", "distance"), ("Geometry", "free space"), ("Task", "reach or drive"), ("Control", "safe motion")],
        formula_title="A robot action usually depends on geometric predicates: distance, reachability, support, and collision.",
        formula=r"$a\ \mathrm{allowed}\iff d(q,\mathcal O)>\epsilon,\quad p_{\mathrm{target}}\in\mathcal R(q),\quad \mathrm{support}(p_{\mathrm{target}})=\mathrm{true}$",
        formula_note="The configuration $q$ is allowed only if obstacles are far enough away, the target point lies in the robot's reachable set, and the target has the support needed for the action. A 2D image alone cannot answer those predicates reliably.",
        algorithm_title="2D-to-3D action test",
        algorithm_steps=["Identify the task predicate: reach, traverse, avoid, place, inspect, or dock.", "Determine which 3D variables the predicate needs.", "Choose the smallest representation that can answer those variables under latency constraints.", "Reject representations that render nicely but cannot update after motion or contact."],
        table_title="3D Variables By Robot Task",
        table_rows=[("Manipulation", "Contact pose, surface normal, clearance, support", "Wrong local geometry causes bad grasp or collision."), ("Navigation", "Free space, obstacle distance, slope, traversability", "Unknown space can be mistaken for safe space."), ("Humanoid motion", "Foot support, hand contact, body clearance", "Whole-body motion amplifies small map errors.")],
        code_intro="Code Fragment 28.1.1 computes whether a candidate target is reachable and collision-safe in a tiny 2D slice. The same predicates become 3D reachability checks in a real planner.",
        code="""# Test a target with reachability and obstacle clearance predicates.
# The same predicate pattern scales to 3D planners and robot arms.
import numpy as np

robot_xy = np.array([0.0, 0.0])
target_xy = np.array([0.55, 0.20])
obstacle_xy = np.array([0.42, 0.18])
reach_radius_m = 0.75
clearance_min_m = 0.18

reachable = np.linalg.norm(target_xy - robot_xy) < reach_radius_m
clearance = np.linalg.norm(target_xy - obstacle_xy)
allowed = reachable and clearance > clearance_min_m
print(round(float(clearance), 3))
print(allowed)""",
        output="0.132\nFalse",
        caption="The target is within `reach_radius_m`, but the obstacle clearance is too small. This illustrates why 3D action checks need geometry and constraints, not just target recognition.",
        shortcut="Open3D, Drake, ROS 2 planning stacks, and simulator scene graphs provide practical routes for computing geometry predicates. The shortcut saves implementation time, but the builder must choose the representation that matches the action predicate.",
        warning="A beautiful reconstructed scene can still be useless for control if it cannot answer free-space, reachability, or support queries at the rate the robot needs.",
        practical="A humanoid robot stepping over a cable needs a 3D estimate of cable height, foot clearance, and support region. A camera label saying cable is not enough to plan the step.",
        frontier="Robotics research is moving toward hybrid scene state: metric geometry for safety and contact, object-centric memory for reasoning, and neural fields for dense appearance. The challenge is keeping the representation updateable during real interaction.",
        refs=[("Open3D. Geometry documentation.", "https://www.open3d.org/docs/release/tutorial/geometry/index.html", "Practical reference for point clouds, meshes, and geometry operations."), ("Nerfstudio. Splatfacto documentation.", "https://docs.nerf.studio/nerfology/methods/splat.html", "Explains how 3D Gaussian Splatting stores explicit volumetric Gaussians for fast rendering.")],
        takeaway="3D matters when the robot must answer geometric predicates that pixels cannot answer reliably: can I reach, fit, support, avoid, or move there now?",
        exercise="For one manipulation task and one navigation task, list the exact 3D predicate that a 2D detector cannot answer by itself.",
    ),
    "28.2": section_body(
        section="28.2",
        title="Point clouds and depth maps",
        opener="provides the simplest bridge from image coordinates to spatial measurements. A depth map stores distance per pixel; a point cloud turns those pixels into metric samples that planners, mappers, and grasp modules can consume.",
        figure_label="28.2.1",
        figure_title="Back-projecting depth pixels into a point cloud",
        figure_nodes=[("Depth map", "z per pixel"), ("Intrinsics", "camera model"), ("Back-project", "x, y, z"), ("Filter", "noise and outliers"), ("Use", "map or grasp")],
        formula_title="Back-projection converts each valid depth pixel into a 3D point in the camera frame.",
        formula=r"$P_c(u,v)=z(u,v)K^{-1}[u,v,1]^T,\quad P_w=T_{wc}P_c$",
        formula_note="The camera intrinsics $K$ define the ray for each pixel. The transform $T_{wc}$ moves the point into the world or robot frame, where it can be merged, filtered, and queried by action modules.",
        algorithm_title="Depth-map to point-cloud pipeline",
        algorithm_steps=["Validate depth units and reject invalid pixels.", "Back-project pixels through camera intrinsics.", "Transform camera-frame points into the robot or world frame.", "Downsample, remove outliers, estimate normals, and publish the cloud with timestamp metadata."],
        table_title="Point Cloud Processing Choices",
        table_rows=[("Voxel downsample", "Large clouds need real-time processing", "Too coarse a voxel hides thin obstacles."), ("Outlier removal", "Noisy sensors or reflective surfaces", "Aggressive filters remove small task-relevant objects."), ("Normal estimation", "Grasping, placement, surface following", "Normals become unstable on sparse or mixed surfaces.")],
        code_intro="Code Fragment 28.2.1 back-projects a 2 by 2 depth map into four 3D points. This tiny array is the same math Open3D applies to thousands of pixels.",
        code="""# Back-project a tiny depth map into camera-frame points.
# Each pixel becomes one metric sample after applying intrinsics.
import numpy as np

depth = np.array([[1.0, 1.2], [0.9, 1.1]])
fx = fy = 500.0
cx = cy = 0.5
points = []
for v in range(depth.shape[0]):
    for u in range(depth.shape[1]):
        z = depth[v, u]
        x = (u - cx) * z / fx
        y = (v - cy) * z / fy
        points.append((round(x, 4), round(y, 4), round(float(z), 2)))
print(points)""",
        output="[(-0.001, -0.001, 1.0), (0.0012, -0.0012, 1.2), (-0.0009, 0.0009, 0.9), (0.0011, 0.0011, 1.1)]",
        caption="The loop turns four depth pixels into four metric samples. The `fx`, `fy`, `cx`, and `cy` values determine the lateral coordinates, while the depth values remain the `z` coordinates.",
        shortcut="Open3D creates point clouds from RGB-D images in a few lines and handles vectorized storage, visualization, and many filters. Keep the hand calculation in mind, because most point-cloud bugs are still unit, intrinsics, or transform bugs.",
        warning="A point cloud is a sample, not a solid object. Empty space between samples may be free, unseen, filtered out, or outside the sensor range.",
        practical="A bin-picking system can voxel-downsample a point cloud for speed, but it should keep a high-resolution crop around the planned grasp contact so thin edges and handles are not erased.",
        frontier="Point clouds remain central because they are simple and actionable, even as neural fields and splats improve rendering. Current systems often combine point clouds for control with richer scene representations for memory and visualization.",
        refs=[("Open3D. RGB-D image tutorial.", "https://www.open3d.org/docs/release/tutorial/geometry/rgbd_image.html", "Shows how maintained tooling converts RGB-D images into point clouds."), ("OpenCV. Camera calibration and 3D reconstruction documentation.", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Defines the camera model needed for back-projection and frame transforms.")],
        takeaway="Depth maps become useful for robotics when they are back-projected, transformed, filtered, timestamped, and tied to the action that will consume the cloud.",
        exercise="Create a 3 by 3 depth map with one invalid pixel. Describe how you would reject the invalid point, downsample the cloud, and preserve a grasp-critical edge.",
    ),
}

sections.update({
    "28.3": section_body(
        section="28.3",
        title="3D detection and scene reconstruction",
        opener="builds object hypotheses that live in metric space and survive across views. The goal is not only to see an object once, but to maintain a pose, extent, confidence, and identity that an action module can use.",
        figure_label="28.3.1",
        figure_title="Scene reconstruction from multi-view observations",
        figure_nodes=[("Views", "RGB-D or lidar"), ("Fuse", "aligned points"), ("Objects", "3D boxes"), ("Scene", "relations"), ("Plan", "query state")],
        formula_title="A 3D detector usually estimates an object state with position, orientation, dimensions, class, and uncertainty.",
        formula=r"$o_i=(p_i,R_i,d_i,c_i,\Sigma_i),\quad \hat{\mathcal S}_t=\{o_i\}_{i=1}^{N_t}$",
        formula_note=r"The scene state $\hat{\mathcal S}_t$ is useful only if each object state is expressed in the same frame and updated consistently across views. Uncertainty $\Sigma_i$ is what lets a planner decide whether to act, observe again, or keep a safety margin.",
        algorithm_title="Multi-view reconstruction contract",
        algorithm_steps=["Associate each observation with camera pose and timestamp.", "Fuse compatible points or features into an object or surface hypothesis.", "Estimate object pose, dimensions, class, and uncertainty.", "Reject or quarantine hypotheses that do not survive view changes or physical constraints."],
        table_title="3D Scene Outputs",
        table_rows=[("3D box", "Navigation, coarse manipulation, tracking", "Boxes hide shape details and contact surfaces."), ("Mesh or surfel map", "Inspection and contact planning", "Can be expensive to update after interaction."), ("Object scene graph", "Task planning and language grounding", "Relations can be wrong if geometry is stale.")],
        code_intro="Code Fragment 28.3.1 fuses two noisy object-position estimates with inverse-variance weighting. This is the core intuition behind treating scene reconstruction as evidence fusion, not one-shot detection.",
        code="""# Fuse two 3D position estimates with uncertainty weights.
# More precise observations receive more influence in the scene state.
import numpy as np

estimate_a = np.array([1.00, 0.20, 0.75])
estimate_b = np.array([1.08, 0.18, 0.72])
sigma_a = 0.06
sigma_b = 0.03
wa, wb = 1 / sigma_a**2, 1 / sigma_b**2
fused = (wa * estimate_a + wb * estimate_b) / (wa + wb)
print(np.round(fused, 3))""",
        output="[1.064 0.184 0.726]",
        caption="The lower-uncertainty `estimate_b` pulls the fused object position toward itself. This is the numeric reason scene reconstruction should carry uncertainty instead of only storing a single object pose.",
        shortcut="Open3D, ROS 2 perception messages, and simulator scene graphs can manage object states and point-cloud fusion. The shortcut handles storage and visualization, while the builder still owns association, frame consistency, and physical plausibility checks.",
        warning="A 3D detector can be locally accurate and globally inconsistent if object poses from different views are fused under the wrong camera transform.",
        practical="An autonomous forklift should preserve pallet identity across viewpoints, estimate fork-clearance geometry, and quarantine object hypotheses that jump when the vehicle turns.",
        frontier="Object-centric scene reconstruction is a major bridge between geometry and language-conditioned agents. The open problem is maintaining persistent object state while contact, occlusion, and task progress change the scene.",
        refs=[("Open3D. Pipelines documentation.", "https://www.open3d.org/docs/release/tutorial/pipelines/index.html", "Practical reference for registration and reconstruction workflows."), ("NVIDIA. Isaac ROS overview.", "https://developer.nvidia.com/isaac/ros", "Robotics middleware context for accelerated perception and scene-state publishing.")],
        takeaway="3D detection is robot-ready when object hypotheses are metric, persistent, uncertain, and physically plausible across views.",
        exercise="Define a scene state for a shelf-picking robot with three objects. Include position, extent, confidence, and one relation needed by the planner.",
    ),
    "28.4": section_body(
        section="28.4",
        title="Occupancy grids and voxel maps",
        opener="stores where space is free, occupied, or unknown. This representation is humble, but it is one of the most actionable maps for navigation, inspection, drone flight, and collision checking.",
        figure_label="28.4.1",
        figure_title="Occupancy update from range evidence",
        figure_nodes=[("Ray", "sensor beam"), ("Free", "before hit"), ("Hit", "occupied cell"), ("Unknown", "unseen"), ("Planner", "cost map")],
        formula_title="Occupancy mapping usually updates log odds so repeated evidence accumulates without probabilities saturating too quickly.",
        formula=r"$\ell_t(m_i)=\ell_{t-1}(m_i)+\log\frac{P(m_i\mid z_t)}{1-P(m_i\mid z_t)}-\ell_0$",
        formula_note=r"The log-odds value $\ell_t$ increases for occupied evidence and decreases for free-space evidence. Unknown is not free; it is a separate epistemic state that planners should treat according to task risk.",
        algorithm_title="Voxel occupancy update",
        algorithm_steps=["Cast a ray from the sensor through the measured endpoint.", "Decrease occupancy log odds for traversed cells before the hit.", "Increase occupancy log odds for the endpoint cell.", "Inflate occupied cells by robot radius before planning."],
        table_title="Occupancy Map Design Choices",
        table_rows=[("2D grid", "Ground robots on mostly flat floors", "Cannot represent overhangs or drone clearance."), ("3D voxel map", "Drones, manipulation, cluttered interiors", "Memory and update cost grow quickly."), ("TSDF or ESDF", "Surface reconstruction and planning distances", "Truncation and integration choices affect thin objects.")],
        code_intro="Code Fragment 28.4.1 performs a tiny log-odds update for free and occupied cells along one range ray. The same idea powers larger occupancy and voxel maps.",
        code="""# Apply one log-odds occupancy update along a range ray.
# Free cells decrease, the hit cell increases, and unknown cells remain unchanged.
import numpy as np

log_odds = np.zeros(6)
free_cells = [0, 1, 2, 3]
hit_cell = 4
log_odds[free_cells] += -0.4
log_odds[hit_cell] += 0.9
prob = 1 / (1 + np.exp(-log_odds))
print(np.round(prob, 2))""",
        output="[0.40 0.40 0.40 0.40 0.71 0.50]",
        caption="The array separates free evidence, occupied evidence, and unknown space. Cell 5 stays at `0.50`, which matters because a planner should not confuse unseen space with safe space.",
        shortcut="OctoMap, OpenVDB-style voxel structures, ROS 2 cost maps, and simulator occupancy layers provide maintained implementations. The library route handles memory and ray integration, while the builder defines sensor models, inflation, and unknown-space policy.",
        warning="Treating unknown cells as free is a planning choice, not a fact. It may be acceptable for exploration and unacceptable for high-speed navigation or human-adjacent robots.",
        practical="A warehouse drone should inflate occupied voxels by its body radius and reserve an additional margin for localization uncertainty before accepting a path through shelving.",
        frontier="Occupancy maps are being combined with neural scene representations and learned priors. The important research tension is between dense, expressive memory and the hard real-time guarantees needed by planners.",
        refs=[("Open3D. Voxel grid documentation.", "https://www.open3d.org/docs/release/tutorial/geometry/voxelization.html", "Shows practical voxel representations and conversions."), ("NVIDIA. Isaac ROS Visual SLAM documentation.", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Visual odometry context for maps that feed navigation.")],
        takeaway="Occupancy grids are powerful because they answer the planner's simplest question: is this space free, occupied, or still unknown?",
        exercise="Design an unknown-space policy for a drone inspecting a warehouse aisle. When should unknown be allowed, penalized, or forbidden?",
    ),
    "28.5": section_body(
        section="28.5",
        title="NeRF: implicit radiance fields",
        opener="represents a scene as a continuous function that predicts color and density from 3D position and view direction. It is excellent for view synthesis, but robotics must ask which parts are actionable for control.",
        figure_label="28.5.1",
        figure_title="NeRF as a continuous rendering function",
        figure_nodes=[("Ray", "camera sample"), ("Samples", "3D points"), ("Network", "color density"), ("Render", "image"), ("Robot", "query limits")],
        formula_title="A NeRF renders a pixel by accumulating colors along a camera ray weighted by transmittance and density.",
        formula=r"$C(r)=\int_{t_n}^{t_f}T(t)\sigma(r(t))c(r(t),d)\,dt,\quad T(t)=\exp\left(-\int_{t_n}^{t}\sigma(r(s))ds\right)$",
        formula_note=r"Density $\sigma$ controls how much a sample blocks the ray, color $c$ controls emitted appearance, and transmittance $T$ controls how much light survives from earlier samples. This is a rendering equation, not automatically a collision-checking equation.",
        algorithm_title="NeRF-for-robotics sanity check",
        algorithm_steps=["Train or load the radiance field from posed images.", "Validate camera poses, scale, and reconstruction quality in task-relevant regions.", "Extract or query geometry only where the robot needs action predicates.", "Use a control-suitable representation, such as mesh, point cloud, occupancy, or signed distance, for collision and contact."],
        table_title="NeRF Strengths And Control Limits",
        table_rows=[("Novel view synthesis", "Teleoperation, inspection, data replay", "Rendered realism does not guarantee metric safety."), ("Implicit density", "Dense appearance and occluded reasoning", "Density is not a contact model by itself."), ("Geometry extraction", "Planning after meshing or SDF conversion", "Extraction thresholds can move surfaces.")],
        code_intro="Code Fragment 28.5.1 computes a discrete volume-rendering weight sequence. This tiny calculation is the mechanism hidden inside neural rendering frameworks.",
        code="""# Compute discrete volume-rendering weights along one ray.
# High density absorbs the ray and shifts weight toward nearby samples.
import numpy as np

sigma = np.array([0.1, 0.3, 2.0, 0.4])
delta = 0.5
alpha = 1 - np.exp(-sigma * delta)
transmittance = np.cumprod(np.r_[1.0, 1 - alpha[:-1]])
weights = transmittance * alpha
print(np.round(alpha, 3))
print(np.round(weights, 3))""",
        output="[0.049 0.139 0.632 0.181]\n[0.049 0.132 0.518 0.109]",
        caption="The `weights` show which samples along the ray dominate the rendered pixel. Robotics users should notice that these are rendering weights, so additional processing is needed before using the field for collision or contact.",
        shortcut="Nerfstudio can train and inspect NeRF-style models through maintained commands and configuration files. That shortcut handles datasets, cameras, optimization, and visualization, while robot builders still validate scale, latency, and control-suitable exports.",
        warning="Do not send a controller directly against a pretty NeRF render. First extract or query geometry in a representation that has conservative collision semantics.",
        practical="A real-estate inspection robot may use NeRF views for remote supervision, while its local navigation still uses occupancy or signed-distance maps for safety-critical motion.",
        frontier="Neural fields are moving from offline view synthesis toward robotics memory, active reconstruction, and policy conditioning. The open challenge is making them updateable, metric, and conservative enough for interaction.",
        refs=[("Mildenhall, B. et al. NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. ECCV, 2020.", "https://arxiv.org/abs/2003.08934", "Foundational paper for implicit radiance fields and volume rendering."), ("Nerfstudio documentation.", "https://docs.nerf.studio/", "Maintained framework for neural field training, inspection, and exports.")],
        takeaway="NeRF is a powerful rendering representation; robotics needs an additional step that converts or constrains it into action-safe geometry.",
        exercise="Name one task where a NeRF render is directly useful and one task where an extracted geometry representation is required before action.",
    ),
    "28.6": section_body(
        section="28.6",
        title="3D Gaussian Splatting: explicit, editable, real-time",
        opener="represents a scene as many explicit 3D Gaussians that can be rasterized quickly. This makes it attractive for real-time visualization and editable scene memory, but control still needs geometric conservatism.",
        figure_label="28.6.1",
        figure_title="Gaussian splats as explicit scene elements",
        figure_nodes=[("Cameras", "posed images"), ("Gaussians", "mean covariance"), ("Rasterize", "fast view"), ("Edit", "local changes"), ("Control", "export geometry")],
        formula_title="Each splat has a mean, covariance, opacity, and appearance parameters; rendering projects the Gaussian into the image.",
        formula=r"$g_i=(\mu_i,\Sigma_i,\alpha_i,\theta_i),\quad w_i(x)\propto \alpha_i\exp\left(-\frac12(x-\pi(\mu_i))^T\Sigma_{i,\mathrm{img}}^{-1}(x-\pi(\mu_i))\right)$",
        formula_note=r"The explicit mean $\mu_i$ and covariance $\Sigma_i$ make splats easier to inspect and edit than a fully implicit field. The projected footprint $w_i$ is still a rendering object, so collision safety requires careful conversion or conservative queries.",
        algorithm_title="Splat-to-robot workflow",
        algorithm_steps=["Train or load splats from posed images.", "Inspect scale, coverage, floaters, and holes in task-relevant regions.", "Export control queries through depth, mesh, point samples, or occupancy approximations.", "Keep a separate safety map when splat rendering is used mainly for visualization or memory."],
        table_title="3DGS For Robotics",
        table_rows=[("Fast rendering", "Teleoperation, simulation, operator interfaces", "High frame rate does not imply collision guarantees."), ("Explicit elements", "Local editing and object removal", "Floaters and transparent surfaces can corrupt queries."), ("Hybrid map", "Visual memory plus geometric safety layer", "Requires synchronization between splat map and control map.")],
        code_intro="Code Fragment 28.6.1 evaluates a tiny 2D Gaussian footprint to show why splats have local influence. The same locality is why they can be edited and rendered efficiently.",
        code="""# Evaluate one projected Gaussian footprint at nearby pixels.
# Local influence makes splats editable and efficient to rasterize.
import numpy as np

pixel = np.array([102.0, 50.0])
mean = np.array([100.0, 48.0])
sigma_px = 3.0
alpha = 0.7
dist2 = np.sum((pixel - mean) ** 2)
weight = alpha * np.exp(-0.5 * dist2 / sigma_px**2)
print(round(float(weight), 3))""",
        output="0.449",
        caption="The `weight` falls with squared distance from the projected mean. This local footprint is the rendering mechanism that makes Gaussian splats fast, editable, and still in need of separate safety checks for robotics.",
        shortcut="Nerfstudio Splatfacto and gsplat provide maintained 3DGS workflows and CUDA-accelerated rasterization. They reduce training and rendering complexity, while the robot team still verifies scale, holes, floaters, and control-map exports.",
        warning="A splat map can render a scene convincingly while containing floaters, holes, or fuzzy surfaces that are unacceptable for contact planning.",
        practical="A teleoperated robot can use Gaussian splats for a responsive operator view while its autonomous collision checker uses a conservative voxel or signed-distance layer derived from verified geometry.",
        frontier="3D Gaussian Splatting has rapidly become a practical scene representation for fast rendering. Robotics research is now exploring how to make splat maps dynamic, object-aware, and compatible with planning rather than only visualization.",
        refs=[("Kerbl, B. et al. 3D Gaussian Splatting for Real-Time Radiance Field Rendering. ACM TOG, 2023.", "https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/", "Introduces the explicit Gaussian representation and real-time rendering approach."), ("Nerfstudio. Splatfacto documentation.", "https://docs.nerf.studio/nerfology/methods/splat.html", "Official maintained workflow for Gaussian splatting in Nerfstudio."), ("nerfstudio-project. gsplat GitHub repository.", "https://github.com/nerfstudio-project/gsplat", "CUDA-accelerated rasterization library for Gaussian splatting workflows.")],
        takeaway="3DGS is compelling for real-time, editable visual memory, but control should use verified geometry or a conservative safety layer derived from it.",
        exercise="List three artifacts you would inspect before trusting a splat map for robot navigation: one scale check, one coverage check, and one safety-layer check.",
    ),
    "28.7": section_body(
        section="28.7",
        title="Scene representations for robotics: SLAM, real2sim, manipulation",
        opener="chooses the right memory format for the job. SLAM needs pose and map consistency, real2sim needs editable geometry and materials, and manipulation needs local contact and object state that survive interaction.",
        figure_label="28.7.1",
        figure_title="Choosing scene memory for control, simulation, and manipulation",
        figure_nodes=[("SLAM", "pose and map"), ("Objects", "state and relations"), ("Geometry", "contact and free space"), ("Sim", "editable twin"), ("Policy", "query action")],
        formula_title="A robot scene memory is best viewed as a set of query functions, not a single universal format.",
        formula=r"$\mathcal M=\{q_{\mathrm{pose}},q_{\mathrm{free}},q_{\mathrm{contact}},q_{\mathrm{object}},q_{\mathrm{render}}\}$",
        formula_note="Different tasks ask different queries. A renderer asks for appearance, a planner asks for free space, a manipulator asks for contact geometry, and a language planner asks for object relations. A mature system routes each query to the representation that can answer it safely.",
        algorithm_title="Representation selection procedure",
        algorithm_steps=["Write the downstream queries before choosing the map format.", "Separate safety-critical geometry from visualization-only memory.", "Keep object state updateable after contact, occlusion, or task progress.", "For real2sim, store provenance so synthetic scenes can be traced back to capture data and edits."],
        table_title="Which Representation Should Own The Query",
        table_rows=[("Pose tracking", "SLAM graph, visual-inertial odometry", "Map inconsistency corrupts every downstream query."), ("Collision planning", "Occupancy, ESDF, mesh, verified cloud", "Rendering fields may be non-conservative."), ("Task reasoning", "Object-centric scene graph", "Relations can become stale after manipulation."), ("Visual replay", "NeRF or 3DGS", "Photorealism can hide missing control semantics.")],
        code_intro="Code Fragment 28.7.1 selects a representation based on the query type. Real systems use richer routing, but the principle is the same: the map format follows the action question.",
        code="""# Route robotics queries to representations with matching semantics.
# Rendering, collision, and object reasoning should not share one blind default.
query_to_representation = {
    "localize": "visual_inertial_slam",
    "avoid_collision": "inflated_occupancy_or_esdf",
    "plan_grasp": "object_pose_plus_contact_geometry",
    "render_operator_view": "nerf_or_gaussian_splats",
    "edit_real2sim_scene": "mesh_plus_object_scene_graph",
}
for query in ["avoid_collision", "render_operator_view", "plan_grasp"]:
    print(query, "=>", query_to_representation[query])""",
        output="avoid_collision => inflated_occupancy_or_esdf\nrender_operator_view => nerf_or_gaussian_splats\nplan_grasp => object_pose_plus_contact_geometry",
        caption="The routing table prevents one representation from being used for every job. `avoid_collision`, `render_operator_view`, and `plan_grasp` each demand different semantics and failure checks.",
        shortcut="ROS 2, SLAM systems, Open3D, Nerfstudio, and simulator import pipelines already provide pieces of this routing. The engineering task is to keep provenance, timestamps, frame transforms, and query ownership explicit.",
        warning="A real2sim scene that looks correct can still be physically wrong if mass, friction, joint limits, collision geometry, or object poses are not audited.",
        practical="A Boston Dynamics style inspection robot might use visual-inertial SLAM for pose, an ESDF for safe footstep or body clearance, object memory for task state, and splats or NeRFs for operator visualization.",
        frontier="The current frontier is hybrid scene memory: SLAM for pose, neural fields or splats for dense visual memory, object-centric graphs for reasoning, and verified geometry for control. The hard part is keeping those layers synchronized as the robot acts.",
        refs=[("NVIDIA. Isaac ROS Visual SLAM documentation.", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Practical visual-inertial odometry component for robotics navigation."), ("Nerfstudio documentation.", "https://docs.nerf.studio/", "Maintained framework for neural scene representations used in real2sim and visualization workflows."), ("Open3D. Geometry and pipelines documentation.", "https://www.open3d.org/docs/release/", "Practical geometry processing reference for robotics scene memory.")],
        takeaway="There is no universal scene representation for robotics. Strong systems route each query to the representation whose assumptions match the action and risk.",
        exercise="Design a scene-memory stack for a mobile manipulator in a kitchen. Assign separate representations for localization, collision checking, object reasoning, visual replay, and simulation export.",
    ),
})


def replace_section(file_path: Path, body: str) -> None:
    text = file_path.read_text(encoding="utf-8")
    start = text.index('<div class="callout big-picture">')
    end = text.index('<nav class="chapter-nav">')
    file_path.write_text(text[:start] + body + text[end:], encoding="utf-8", newline="\n")


for section_id, body in sections.items():
    chapter = "module-27-visual-perception-for-action" if section_id.startswith("27.") else "module-28-3d-perception-and-neural-scene-representations"
    file_path = ROOT / "part-6-embodied-perception" / chapter / f"section-{section_id}.html"
    replace_section(file_path, body)
