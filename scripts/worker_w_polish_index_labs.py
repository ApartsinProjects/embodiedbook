from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


LABS = {
    "part-6-embodied-perception/module-27-visual-perception-for-action/index.html": """<section class="lab" id="lab-27">
<h2>Hands-On Lab: Build A Closed-Loop Visual Evidence Panel</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 90 minutes</span><span class="lab-difficulty">Difficulty: Intermediate</span></div>
<div class="lab-objective"><h3>Objective</h3><p>Build a small visual-perception audit that turns masks, depth, motion, and affordance scores into an action decision with a replayable failure label.</p></div>
<div class="lab-skills"><h3>What You'll Practice</h3><ul><li>Designing a perception-to-action schema with frames, latency, and uncertainty.</li><li>Combining confidence, clearance, and affordance into an executable action score.</li><li>Testing perturbations such as occlusion, stale timestamps, and depth-scale error.</li><li>Writing a postmortem that separates visual failure from planning or control failure.</li></ul></div>
<div class="lab-prereqs"><h3>Setup</h3><p>Start with NumPy for the audit logic. Add OpenCV, PyTorch, SAM 2, or ROS 2 only after the schema is producing useful traces.</p><pre><code class="language-bash"># Install the lightweight baseline dependency.
python -m pip install numpy</code></pre><div class="code-caption"><strong>Code Fragment 27.L1:</strong> This setup installs only NumPy so the lab begins with an inspectable action audit. Heavier vision tools can be added after the evidence schema is correct.</div></div>
<div class="lab-steps"><h3>Steps</h3><div class="lab-step"><h4>Step 1: Define The Evidence Schema</h4><p>Create fields for image timestamp, camera frame, visual estimate, uncertainty, latency, candidate action, and failure label.</p></div><div class="lab-step"><h4>Step 2: Add Action Scores</h4><p>Combine visual confidence, metric clearance, task value, and latency penalty into one score per candidate command.</p><pre><code class="language-python"># Score three visual action candidates with safety and latency penalties.
# The panel explains why the selected robot command changes.
import numpy as np

actions = np.array(["grasp left", "grasp right", "wait"])
confidence = np.array([0.86, 0.72, 1.00])
clearance_m = np.array([0.025, 0.090, 0.500])
latency_ms = np.array([40, 42, 0])
score = confidence + 2.0 * clearance_m - 0.002 * latency_ms
print(actions[int(score.argmax())])
print(np.round(score, 3))</code></pre><div class="code-output">wait
[0.830 0.816 2.000]</div><div class="code-caption"><strong>Code Fragment 27.L2:</strong> The score includes `confidence`, `clearance_m`, and `latency_ms`, so the lab can explain why a high-confidence grasp may still be rejected. The `wait` action wins because the current clearance is not yet good enough for execution.</div></div><div class="lab-step"><h4>Step 3: Perturb One Factor</h4><p>Reduce clearance, increase latency, hide part of the mask, or add depth-scale error. Record whether the action changes for the expected reason.</p></div><div class="lab-step"><h4>Step 4: Add A Library Path</h4><p>Replace the toy confidence values with outputs from OpenCV, a detector, SAM 2, or a PyTorch affordance head while keeping the schema unchanged.</p></div><div class="lab-step"><h4>Step 5: Write The Replay Postmortem</h4><p>Save one success case and one failure case with enough metadata to reproduce the action decision.</p></div></div>
<div class="lab-expected"><h3>Expected Output</h3><p>A table with candidate actions, visual estimates, uncertainty fields, latency, action scores, chosen command, and a failure label for at least one perturbation.</p></div>
<div class="lab-stretch"><h3>Stretch Goals</h3><ul><li>Replay the same schema from a ROS 2 bag.</li><li>Add a mask-to-affordance score using a SAM 2 or detector-generated region.</li><li>Plot the action score as depth scale or latency changes.</li></ul></div>
<div class="kindle-disclosure lab-solution"><p class="kindle-disclosure-title">Complete Solution</p><pre><code class="language-python"># Complete baseline for the closed-loop visual evidence panel.
# It records the selected command and a failure label for replay.
import numpy as np

actions = np.array(["grasp left", "grasp right", "wait"])
confidence = np.array([0.86, 0.72, 1.00])
clearance_m = np.array([0.025, 0.090, 0.500])
latency_ms = np.array([40, 42, 0])
score = confidence + 2.0 * clearance_m - 0.002 * latency_ms
chosen = int(score.argmax())
failure_label = "insufficient_clearance" if actions[chosen] == "wait" else "none"
print({"chosen": actions[chosen], "failure_label": failure_label})</code></pre><div class="code-output">{'chosen': 'wait', 'failure_label': 'insufficient_clearance'}</div><div class="code-caption"><strong>Code Fragment 27.L3:</strong> The complete solution emits a replayable dictionary with `chosen` and `failure_label`. This is the minimum artifact needed before swapping the toy values for OpenCV, SAM 2, or PyTorch outputs.</div></div>
</section>""",
    "part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/index.html": """<section class="lab" id="lab-28">
<h2>Hands-On Lab: Build A Scene-Representation Query Router</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 90 minutes</span><span class="lab-difficulty">Difficulty: Intermediate</span></div>
<div class="lab-objective"><h3>Objective</h3><p>Build a small router that sends localization, collision, contact, rendering, and real2sim queries to representations with matching semantics.</p></div>
<div class="lab-skills"><h3>What You'll Practice</h3><ul><li>Separating visualization memory from safety-critical geometry.</li><li>Choosing between point clouds, occupancy, object graphs, NeRFs, and Gaussian splats.</li><li>Attaching provenance, frame, and update-rate requirements to each query.</li><li>Designing a failure label for stale or mismatched scene memory.</li></ul></div>
<div class="lab-prereqs"><h3>Setup</h3><p>Start with Python's standard data structures. Add Open3D, Nerfstudio, or ROS 2 only after the query ownership table is clear.</p><pre><code class="language-bash"># Optional tools for extending the lab after the baseline router works.
python -m pip install numpy open3d</code></pre><div class="code-caption"><strong>Code Fragment 28.L1:</strong> This command installs NumPy and Open3D for optional geometry experiments. The first router can run without them, which keeps the representation decision visible.</div></div>
<div class="lab-steps"><h3>Steps</h3><div class="lab-step"><h4>Step 1: List The Robot Queries</h4><p>Write queries for localize, avoid collision, plan grasp, render operator view, and export a real2sim scene.</p></div><div class="lab-step"><h4>Step 2: Route Each Query</h4><p>Assign each query to a representation that can answer it with the right semantics and risk level.</p><pre><code class="language-python"># Route scene queries to representations with matching safety semantics.
# Rendering and collision checking deliberately use different owners.
routes = {
    "localize": "visual_inertial_slam",
    "avoid_collision": "inflated_occupancy_or_esdf",
    "plan_grasp": "object_pose_plus_contact_geometry",
    "render_operator_view": "nerf_or_gaussian_splats",
    "export_real2sim": "mesh_plus_object_scene_graph",
}
for query, owner in routes.items():
    print(f"{query}: {owner}")</code></pre><div class="code-output">localize: visual_inertial_slam
avoid_collision: inflated_occupancy_or_esdf
plan_grasp: object_pose_plus_contact_geometry
render_operator_view: nerf_or_gaussian_splats
export_real2sim: mesh_plus_object_scene_graph</div><div class="code-caption"><strong>Code Fragment 28.L2:</strong> The router gives `avoid_collision` a conservative map while assigning `render_operator_view` to NeRF or Gaussian splats. That separation is the central safety lesson of the chapter.</div></div><div class="lab-step"><h4>Step 3: Add Freshness Requirements</h4><p>Attach maximum age, frame, and provenance fields to each route so stale scene memory can be rejected.</p></div><div class="lab-step"><h4>Step 4: Add A Failure Case</h4><p>Create one case where a rendered scene is visually plausible but too stale or too non-conservative for collision checking.</p></div><div class="lab-step"><h4>Step 5: Replace One Route With A Tool</h4><p>Use Open3D for a point-cloud or voxel route, or Nerfstudio for a visual replay route, while preserving the query contract.</p></div></div>
<div class="lab-expected"><h3>Expected Output</h3><p>A query table that maps each robot question to a representation, required metadata, freshness limit, and failure label.</p></div>
<div class="lab-stretch"><h3>Stretch Goals</h3><ul><li>Create a tiny Open3D point cloud and route collision queries to it.</li><li>Add a Gaussian-splat route for visualization with an explicit no-control warning.</li><li>Export the routing table as JSON for a simulator or ROS 2 node.</li></ul></div>
<div class="kindle-disclosure lab-solution"><p class="kindle-disclosure-title">Complete Solution</p><pre><code class="language-python"># Complete baseline for the scene-representation query router.
# It flags unsafe attempts to use rendering memory for collision checks.
routes = {
    "avoid_collision": {"owner": "inflated_occupancy_or_esdf", "max_age_ms": 100},
    "render_operator_view": {"owner": "nerf_or_gaussian_splats", "max_age_ms": 2000},
}
requested_owner = routes["render_operator_view"]["owner"]
failure_label = "wrong_representation_for_collision" if "splat" in requested_owner else "none"
print(failure_label)</code></pre><div class="code-output">wrong_representation_for_collision</div><div class="code-caption"><strong>Code Fragment 28.L3:</strong> The complete solution labels an unsafe routing attempt when visualization memory is reused for collision checking. The `failure_label` makes the representation mismatch replayable.</div></div>
</section>""",
}


for rel, lab in LABS.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(
        r'<section class="lab" id="lab-\d+">.*?</section>',
        lab,
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f"Could not replace lab in {path}")
    path.write_text(updated, encoding="utf-8", newline="\n")

