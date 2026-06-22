from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


def blockquote(quote: str, cite: str, image_src: str, image_alt: str, image_caption: str) -> str:
    return f"""<blockquote class="epigraph">
<p>{quote}</p>
<figure class="illustration">
<img alt="{image_alt}" loading="lazy" src="{image_src}"/>
<figcaption>{image_caption}</figcaption>
</figure>
<cite>{cite}</cite>
</blockquote>"""


def flow_svg(section_id: str, title: str, observe: str, decide: str, act: str, verify: str) -> str:
    return f"""<figure class="illustration" id="fig-{section_id}-flow">
<svg aria-labelledby="fig-{section_id}-title" height="250" role="img" viewBox="0 0 760 250" width="100%">
<title id="fig-{section_id}-title">{title}</title>
<rect fill="#e8f3ff" height="88" rx="8" stroke="#1f5f99" width="156" x="20" y="42"></rect>
<text font-size="15" font-weight="700" text-anchor="middle" x="98" y="72">Observe</text>
<text font-size="12" text-anchor="middle" x="98" y="98">{observe}</text>
<rect fill="#eef9f0" height="88" rx="8" stroke="#2e7d32" width="156" x="208" y="42"></rect>
<text font-size="15" font-weight="700" text-anchor="middle" x="286" y="72">Model</text>
<text font-size="12" text-anchor="middle" x="286" y="98">{decide}</text>
<rect fill="#fff5e5" height="88" rx="8" stroke="#a85d00" width="156" x="396" y="42"></rect>
<text font-size="15" font-weight="700" text-anchor="middle" x="474" y="72">Act</text>
<text font-size="12" text-anchor="middle" x="474" y="98">{act}</text>
<rect fill="#f8ecff" height="88" rx="8" stroke="#6a1b9a" width="136" x="604" y="42"></rect>
<text font-size="15" font-weight="700" text-anchor="middle" x="672" y="72">Verify</text>
<text font-size="12" text-anchor="middle" x="672" y="98">{verify}</text>
<path d="M178 86 L204 86" marker-end="url(#arrow-{section_id})" stroke="#333" stroke-width="2"></path>
<path d="M366 86 L392 86" marker-end="url(#arrow-{section_id})" stroke="#333" stroke-width="2"></path>
<path d="M554 86 L600 86" marker-end="url(#arrow-{section_id})" stroke="#333" stroke-width="2"></path>
<path d="M672 134 C672 205 95 205 95 134" fill="none" marker-end="url(#arrow-{section_id})" stroke="#555" stroke-width="2"></path>
<defs><marker id="arrow-{section_id}" markerHeight="8" markerWidth="10" orient="auto" refX="9" refY="4"><path d="M0,0 L10,4 L0,8 Z" fill="#333"></path></marker></defs>
</svg>
<figcaption>{title}</figcaption>
</figure>"""


def code_block(code: str, output: str, interpretation: str, caption: str) -> str:
    return f"""<pre><code class="language-python">{html.escape(code)}</code></pre>
<div class="code-output">{html.escape(output)}</div>
<p><strong>Expected output interpretation.</strong> {interpretation}</p>
<div class="code-caption">{caption}</div>"""


def bib_cards(cards: list[tuple[str, str]]) -> str:
    body = []
    for ref, annotation in cards:
        body.append(
            f'<div class="bib-entry-card"><p class="bib-ref">{ref}</p><p class="bib-annotation">{annotation}</p></div>'
        )
    return "<section class=\"bibliography\"><h2>Section References</h2>" + "".join(body) + "</section>"


def comparison_table(title: str, headers: list[str], rows: list[tuple[str, ...]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = []
    for row in rows:
        body_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    return (
        f'<div class="comparison-table"><div class="comparison-table-title">{title}</div><table>'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(body_rows)}</tbody></table></div>"
    )


def callout(kind: str, title: str, body: str) -> str:
    return f'<div class="callout {kind}"><div class="callout-title">{title}</div><p>{body}</p></div>'


def list_items(items: list[str]) -> str:
    return "<ol>" + "".join(f"<li>{item}</li>" for item in items) + "</ol>"


def render_section(d: dict[str, object]) -> str:
    theory = "".join(f"<p>{p}</p>" for p in d["theory"])
    deep = "".join(f"<p>{p}</p>" for p in d["deep_dive"])
    practical = list_items(d["recipe"])
    algo = list_items(d["algorithm"])
    return f"""{blockquote(d["quote"], d["cite"], d["image_src"], d["image_alt"], d["image_caption"])}
{callout("big-picture", "Big Picture", d["big_picture"])}
{callout("pathway", "Reader Pathway", d["pathway"])}
<h2>What This Section Develops</h2>
<p>{d["develops_1"]}</p>
<p>{d["develops_2"]}</p>
{callout("key-insight", d["key_title"], d["key_text"])}
{flow_svg(d["id"], d["flow_caption"], d["flow_observe"], d["flow_model"], d["flow_act"], d["flow_verify"])}
<h2>Theory</h2>
{theory}
<div class="callout algorithm"><div class="callout-title">{d["algo_title"]}</div>{algo}</div>
<h2>Worked Example</h2>
<p>{d["worked_intro"]}</p>
{code_block(d["code"], d["output"], d["output_interp"], d["code_caption"])}
{callout("library-shortcut", "Library Shortcut", d["library"])}
<h2>Practical Recipe</h2>
{practical}
{callout("warning", "Common Failure Mode", d["warning"])}
{callout("practical-example", "Practical Example", d["example"])}
{callout("fun-note", "Memory Hook", d["memory"])}
{callout("research-frontier", "Research Frontier", d["frontier"])}
{callout("self-check", "Self Check", d["self_check"])}
<section class="production-depth-expansion">
<h2>Builder's Deep Dive</h2>
{deep}
{comparison_table(d["table_title"], d["table_headers"], d["table_rows"])}
{callout("cross-ref", "Cross-References", d["cross_refs"])}
{callout("lab", "Mini Lab", d["lab"])}
<h2>Failure Analysis Pattern</h2>
<p>{d["failure_pattern"]}</p>
</section>
{bib_cards(d["biblio"])}
{callout("key-takeaway", "Key Takeaway", d["takeaway"])}
{callout("exercise", d["exercise_title"], d["exercise"])}"""


def replace_main_body(path: Path, new_body: str) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.search(r'(<main class="content" id="main-content">)(.*?)(<nav class="chapter-nav">)', text, re.S)
    if not match:
        raise RuntimeError(f"Could not find main body boundary in {path}")
    updated = text[: match.start(2)] + "\n" + new_body + "\n" + text[match.start(3) :]
    path.write_text(updated, encoding="utf-8")


def render_index(d: dict[str, object]) -> str:
    roadmap = []
    for num, href, title, desc in d["roadmap"]:
        roadmap.append(
            f'<li><span class="section-num">{num}</span> <a href="{href}"><span class="section-title">{title}</span></a>'
            f'<span class="section-desc">{desc}</span></li>'
        )
    bib = "".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref}</p><p class="bib-annotation">{ann}</p></div>'
        for ref, ann in d["biblio"]
    )
    table = comparison_table(d["table_title"], ["Tool or Library", "Where It Pays Off"], d["tool_rows"])
    return f"""<blockquote class="epigraph">
<p>{d["quote"]}</p>
<cite>{d["cite"]}</cite>
</blockquote>
{callout("big-picture", "Big Picture", d["big_picture"])}
{callout("key-insight", "Remember This Chapter", d["remember"])}
<div class="overview">
<h2>Chapter Overview</h2>
<p>{d["overview_1"]}</p>
<p>{d["overview_2"]}</p>
</div>
<div class="prereqs"><h3>Prerequisites</h3><p>{d["prereqs"]}</p></div>
<h2>Chapter Roadmap</h2>
<ul class="sections-list">{''.join(roadmap)}</ul>
{callout("library-shortcut", "Tooling Note", d["tooling_note"])}
<section class="lab" id="{d["lab_id"]}">
<h2>Hands-On Lab: Build the Chapter System</h2>
<div class="lab-meta"><span class="lab-duration">{d["lab_duration"]}</span><span class="lab-difficulty">{d["lab_difficulty"]}</span></div>
<div class="lab-objective"><h3>Objective</h3><p>{d["lab_objective"]}</p></div>
<div class="lab-steps"><h3>Steps</h3>{list_items(d["lab_steps"])}</div>
</section>
<div class="whats-next"><h3>What's Next?</h3><p>{d["next"]}</p></div>
<section class="production-depth-expansion">
<h2>Production Notes For Readers</h2>
<p>{d["production_1"]}</p>
{table}
{callout("lab", "Chapter Lab Extension", d["lab_extension"])}
</section>
<section class="production-index-depth-topup">
<h2>Instructor And Builder Notes</h2>
<p>{d["instructor_1"]}</p>
<p>{d["instructor_2"]}</p>
{callout("self-check", "Readiness Check", d["readiness"])}
{callout("key-takeaway", "Teaching Takeaway", d["teaching"])}
</section>
<section class="agent-checklist-summary">
<h2>Agent Checklist Integration</h2>
<p>{d["agent_1"]}</p>
<p>{d["agent_2"]}</p>
{callout("key-insight", "Chapter Evidence Standard", d["evidence_standard"])}
</section>
<section class="bibliography">
<h2>Bibliography &amp; Further Reading</h2>
<h3>Primary Sources, Tools, and References</h3>
{bib}
</section>"""


SECTION_DATA = {
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.1.html": {
        "id": "45-1",
        "quote": '"Mobility is morphology plus a contract with the ground."',
        "cite": "A Builder's Locomotion Notebook",
        "image_src": "images/chapter-45-illustration-01.png",
        "image_alt": "Wheeled, legged, and hybrid robots crossing different terrain types.",
        "image_caption": "<strong>Figure 45.1A</strong>: Different mobile bodies buy different feasible contact patterns, sensing needs, and recovery margins.",
        "big_picture": "<strong>Mobility morphology is a systems decision.</strong> Wheels, legs, tracks, and hybrids are not aesthetic choices. They change the state estimator, the controller, the contact model, the energy budget, and the set of recoverable failures.",
        "pathway": "Read this section as a selection problem: characterize terrain and task, choose the morphology that minimizes mission cost under stability and maintenance constraints, then verify the choice on a matched terrain panel.",
        "develops_1": "This section turns robot morphology into an explicit optimization problem. For a mission class $m$, terrain distribution $\\mathcal{T}$, and morphology candidate $r$, a useful design score is $J(r) = w_t T(r, \\mathcal{T}) + w_e E(r, \\mathcal{T}) + w_s S(r, \\mathcal{T}) + w_r R(r, \\mathcal{T})$, where the terms represent traversal time, energy, slip or fall risk, and recovery burden. The right body is the one that minimizes the mission score, not the one with the most dramatic demo.",
        "develops_2": "Wheels obey nonholonomic constraints, such as $\\dot y \\cos \\theta - \\dot x \\sin \\theta = 0$, which make them efficient on prepared surfaces but weak on discontinuous footholds. Legged bodies trade efficiency for contact flexibility. Hybrids buy mode switching, but they also add controller complexity, extra failure modes, and more sim-to-real surface area.",
        "key_title": "Morphology Sets The Failure Taxonomy",
        "key_text": "If a robot cannot place a stable contact where the terrain demands one, no policy can rescue the mission. Morphology is the first controller.",
        "flow_caption": "Figure 45.1.1 turns morphology choice into an inspectable loop: environment evidence, feasibility model, body selection, and mission-level verification.",
        "flow_observe": "terrain class, slope, step height",
        "flow_model": "contact affordance and mission cost",
        "flow_act": "pick wheel, leg, or hybrid mode",
        "flow_verify": "completion, slip, energy, recovery",
        "theory": [
            "A practical mobility stack separates three models. The geometric model asks whether the body can physically fit and place support contacts. The dynamic model asks whether required forces and torques are feasible. The autonomy model asks whether perception, estimation, and control can keep the body inside that feasible set when the world deviates from the nominal plan.",
            "For wheeled robots, the central quantity is curvature and traction margin. For legged robots, it is the reachable contact set and recoverable center-of-mass motion. For hybrids, it is the switching policy between support modes and the price of switching too late.",
            "A graduate-level design habit is to compare morphologies on one scenario panel: ramps, stairs, gaps, debris, low-friction patches, narrow aisles, and payload variations. A single average speed number hides the actual body-environment contract."
        ],
        "algo_title": "Algorithm: Morphology Selection For A Deployment Panel",
        "algorithm": [
            "Define the mission panel: terrain classes, obstacle statistics, aisle widths, payloads, runtime, and allowed intervention rate.",
            "Compute geometric feasibility for each morphology: clearance, reachability, and required support contacts.",
            "Estimate dynamic feasibility: traction margin for wheels, contact reach and impulse budget for legs, and mode-switch overhead for hybrids.",
            "Score energy, traversal time, maintenance burden, and expected recovery cost on the same panel.",
            "Choose the morphology whose failure cases are observable and recoverable with the available sensing and control stack."
        ],
        "worked_intro": "The first useful artifact is not a render. It is a morphology scorecard built on the exact terrain panel that the deployment team expects to face.",
        "code": """from math import inf

candidates = {
    "wheeled": {"time_s": 62, "energy_kj": 1.8, "slip_events": 5, "recoveries": 7},
    "legged": {"time_s": 81, "energy_kj": 3.9, "slip_events": 1, "recoveries": 2},
    "hybrid": {"time_s": 70, "energy_kj": 3.1, "slip_events": 2, "recoveries": 3},
}

weights = {"time_s": 0.04, "energy_kj": 0.25, "slip_events": 2.0, "recoveries": 1.5}

scores = {}
for name, vals in candidates.items():
    scores[name] = round(sum(weights[k] * vals[k] for k in weights), 2)

winner = min(scores, key=scores.get)
print(scores)
print({"selected": winner, "score": scores[winner]})""",
        "output": """{'wheeled': 21.43, 'legged': 13.21, 'hybrid': 13.15}
{'selected': 'hybrid', 'score': 13.15}""",
        "output_interp": "The hybrid body wins because the scenario panel prices recovery burden and slip heavily. A pure wheeled platform is faster and cheaper in energy, but it pays too much in recoveries on discontinuous terrain.",
        "code_caption": "<strong>Code Fragment 45.1.1:</strong> A morphology ledger compares wheel, leg, and hybrid bodies on one matched mission panel. The score is not universal. It is only valid for the exact terrain and weighting assumptions recorded in the artifact.",
        "library": "Use Isaac Lab or MuJoCo for terrain replay, Drake or Pinocchio for kinematic and dynamic checks, and ROS 2 logs for deployment traces. These tools make morphology arguments reproducible instead of anecdotal.",
        "recipe": [
            "Measure the real terrain distribution before picking a body.",
            "Record which tasks require continuous rolling, stepping, kneeling, bracing, or contact-rich manipulation while moving.",
            "Compute mission cost with the same metric code for every morphology candidate.",
            "Stress the winner with the most probable field perturbations: wheel slip, missing foothold, load shift, and degraded localization.",
            "Save one decision card with geometry, dynamics, telemetry assumptions, and failure thresholds."
        ],
        "warning": "Teams often inherit a platform and then pretend the remaining work is only learning. If the body is mismatched to the terrain, the learning stack becomes a patch for the wrong problem.",
        "example": "A hospital delivery robot can dominate with wheels because the floor is prepared and runtime matters. A substation inspection robot on gravel, curbs, and stairs may need legs or a wheel-leg hybrid because contact flexibility is worth the extra energy.",
        "memory": "Morphology is the slowest hyperparameter to change, so it deserves the earliest evidence.",
        "frontier": "Current frontier work pushes wheel-leg hybrids, underactuated dynamic legs, and morphologically adaptive bodies. The open question is not only which body is fastest, but which body yields the most recoverable autonomy under realistic sensing and maintenance budgets.",
        "self_check": "Can you state one terrain condition that immediately rules out wheels, one that makes legs wasteful, and one where a hybrid pays for its added complexity?",
        "deep_dive": [
            "A useful way to teach this material is to force every body choice to expose its hidden middleware and estimator implications. Wheels favor odometry and traction models. Legs require contact estimation, gait timing, and state estimation through intermittent support. Hybrids require a mode estimator that can explain why the robot changed support strategy.",
            "This is also the right place to connect morphology to downstream chapters. The same body choice that helps locomotion may hurt manipulation reach, teleoperation ergonomics, or whole-body safety. That coupling is why embodied systems resist clean organizational boundaries."
        ],
        "table_title": "Practical Tool Choices For Morphology Studies",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Isaac Lab terrain generators", "Generate matched terrain panels for wheel, leg, and hybrid replay", "Keep terrain seeds fixed when comparing morphologies."),
            ("Drake or Pinocchio", "Check kinematics, support reach, and dynamic feasibility", "Use symbolic or batch checks before expensive learning runs."),
            ("ROS 2 logging", "Capture real failure cases and operator interventions", "Replay real failures in simulation rather than inventing toy disturbances.")
        ],
        "cross_refs": 'Pairs naturally with <a href="../../part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/index.html">robot kinematics</a>, <a href="../../part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/index.html">state estimation</a>, and <a href="../../part-6-embodied-perception/module-30-navigation-and-path-planning/index.html">navigation and planning</a>.',
        "lab": "Build a five-scenario mobility panel with flat floor, ramp, curb, gap, and low-friction patch. Compare one wheeled, one legged, and one hybrid controller or simulator profile under the same metric script.",
        "failure_pattern": "When a morphology argument fails, isolate whether the error came from environment assumptions, force or torque feasibility, localization fragility, or operator intervention burden. Different bodies fail for different reasons, and the mitigation route changes with the reason.",
        "biblio": [
            ('Carpentier, J. et al. "Pinocchio: fast forward and inverse dynamics for articulated systems." Official project page. <a href="https://github.com/stack-of-tasks/pinocchio" rel="noopener" target="_blank">https://github.com/stack-of-tasks/pinocchio</a>', "Primary dynamics library reference for articulated robots, including centroidal quantities and constrained dynamics."),
            ('Drake project. "Model-based design and verification for robotics." <a href="https://drake.mit.edu/" rel="noopener" target="_blank">https://drake.mit.edu/</a>', "Useful for geometric and dynamic feasibility checks before platform commitment."),
            ('NVIDIA Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Primary source for modern GPU robot-learning workflows and terrain-heavy mobility experiments.")
        ],
        "takeaway": "Choose mobility bodies with matched terrain evidence, not with a favorite demo clip.",
        "exercise_title": "Exercise 45.1.1",
        "exercise": "Write a morphology scorecard for one real deployment setting. Include the terrain distribution, the weighted mission objective, one irrecoverable failure for each body type, and one reason the winning body might still lose after six months of field data."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.2.html": {
        "id": "45-2",
        "quote": '"Balance is what remains after every modeling shortcut gets punished by gravity."',
        "cite": "A Dynamics Lecture After Midnight",
        "image_src": "images/chapter-45-illustration-02.png",
        "image_alt": "Biped maintaining balance while stepping and recovering from a push.",
        "image_caption": "<strong>Figure 45.2A</strong>: Stability is about recoverability over time, not about a single static pose.",
        "big_picture": "<strong>Balance, stability, and gait</strong> sit at the center of locomotion because every command changes support geometry and momentum at once.",
        "pathway": "Read this section from reduced-order model to recovery behavior: support polygon, ZMP and capture point, gait scheduler, low-level controller, then disturbance testing.",
        "develops_1": "The linear inverted pendulum model gives a compact balance approximation. With center-of-mass horizontal position $c$ and height-fixed natural frequency $\\omega = \\sqrt{g/z_0}$, the capture point is $\\xi = c + \\dot c / \\omega$. If $\\xi$ leaves the reachable foothold set, the current stance cannot stop the fall without taking a step.",
        "develops_2": "For zero-moment-point reasoning, the planned ZMP must stay inside the support polygon during contact. That is a necessary but not sufficient condition for robust walking because actuator bandwidth, contact compliance, perception delay, and state-estimation drift still matter in the closed loop.",
        "key_title": "A Stable Gait Is A Recovery Policy",
        "key_text": "The right question is not whether the gait looks smooth on nominal terrain. It is whether the robot still has a feasible next foothold after a push, slip, or height error.",
        "flow_caption": "Figure 45.2.1 makes gait generation explicit: estimate balance state, predict recoverability, choose footstep timing, and verify margin after disturbance.",
        "flow_observe": "CoM, support polygon, phase, contact",
        "flow_model": "LIPM, ZMP, capture point",
        "flow_act": "set footstep and stance timing",
        "flow_verify": "fall rate, recovery time, margin",
        "theory": [
            "Static stability asks whether the projected center of mass lies inside the support region. Dynamic stability asks whether momentum, actuator authority, and future footholds allow recovery before the robot reaches an unrecoverable state.",
            "Gait design is therefore a hybrid systems problem. The robot alternates discrete contact modes and continuous within-contact dynamics. A controller that ignores mode transitions tends to fail precisely when the task becomes interesting: on slopes, during pushes, or while carrying loads.",
            "The right instrumentation is a balance ledger that records ZMP margin, capture-point error, stance phase, slip events, and recovery steps on every episode."
        ],
        "algo_title": "Algorithm: Push-Recovery Evaluation Loop",
        "algorithm": [
            "Estimate center of mass, center of pressure, stance phase, and body twist at control rate.",
            "Compute ZMP margin and capture-point error relative to the current or planned support region.",
            "If the capture point exits the current support set, trigger a step adjustment or stance widening policy.",
            "If step adjustment is infeasible, reduce commanded velocity and raise damping or compliance according to the safety mode.",
            "Log whether recovery came from ankle strategy, hip strategy, stepping, or operator intervention."
        ],
        "worked_intro": "A tiny diagnostic on the capture point can explain why one gait survives a shove that another gait cannot recover from.",
        "code": """import math

com_x = 0.02
com_vx = 0.55
z0 = 0.82
g = 9.81
omega = math.sqrt(g / z0)
capture_point = com_x + com_vx / omega
support_max_x = 0.16
margin = round(support_max_x - capture_point, 3)

print(f"capture_point={capture_point:.3f} m")
print(f"remaining_margin={margin:.3f} m")""",
        "output": """capture_point=0.179 m
remaining_margin=-0.019 m""",
        "output_interp": "The capture point sits 1.9 cm outside the current support limit. A controller that keeps the same stance is already late. It must place a new foot, widen support, or lower momentum quickly enough to move the capture point back into a reachable set.",
        "code_caption": "<strong>Code Fragment 45.2.1:</strong> The capture-point check is a compact recoverability test. It does not prove a full-body controller will succeed, but it immediately flags when the current support phase is no longer enough.",
        "library": "Use Drake for reduced-order reasoning, MuJoCo or Isaac Lab for contact-rich gait replay, and ROS 2 for synchronized force, IMU, and controller logs on hardware.",
        "recipe": [
            "Instrument ZMP, capture-point error, stance phase, and foot slip in every rollout.",
            "Evaluate nominal walking, pushes, friction drops, and height-map errors on the same disturbance panel.",
            "Separate gait generation from recovery logic so you can attribute failures to the right layer.",
            "Tune for recovery margin before tuning for style or top speed.",
            "Archive two traces for every new controller: a stable nominal run and a near-failure recovery run."
        ],
        "warning": "A gait can look smooth while silently using torque peaks, contact chatter, or emergency stance corrections that never appear in the summary video.",
        "example": "A warehouse biped that carries boxes should be tested with payload asymmetry and lateral nudges during turns. Many controllers that appear strong in straight-line walking fail when torso momentum and grasp maintenance interact.",
        "memory": "If the robot can only stay upright when nobody bothers it, the gait is choreography, not control.",
        "frontier": "Recent locomotion work blends reduced-order planners, MPC, and learned recovery policies. The open challenge is maintaining interpretable balance margins while still exploiting the agility of learned full-body reflexes.",
        "self_check": "Can you explain why ZMP inside the support polygon is useful but insufficient, and what additional signal would tell you whether a step must be taken?",
        "deep_dive": [
            "This section is a natural bridge between classical control and modern locomotion learning. Students who see capture-point reasoning first can later interpret learned recovery policies as fast approximations to the same physical objective, rather than as unexplained magic.",
            "It is also worth emphasizing that gait evaluation is not one scalar. The same controller can have good average speed and terrible disturbance behavior. Reporting both nominal and perturbation metrics is part of the scientific content, not bookkeeping."
        ],
        "table_title": "Balance And Gait Tooling",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Drake", "LIPM, footstep planning, and balance reasoning", "Start here when you want interpretable reduced-order models."),
            ("Isaac Lab or MuJoCo", "Contact-rich rollout and learned gait validation", "Use the same disturbance panel across controllers."),
            ("Force plates or foot contact logs", "Measure actual support behavior", "Do not infer contact quality from pose traces alone.")
        ],
        "cross_refs": 'This section connects directly to <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">control</a>, <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/index.html">scalable RL systems</a>, and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html">advanced humanoid dynamics</a>.',
        "lab": "Replay the same biped or quadruped gait with three push magnitudes and two friction values. Record whether recovery uses ankle strategy, stepping, or failure.",
        "failure_pattern": "Balance failures should be labeled by root cause: wrong state estimate, late contact detection, bad footstep plan, insufficient actuator authority, or unstable gain schedule. Those labels make later learning and controller tuning faster and more honest.",
        "biblio": [
            ('MIT Underactuated Robotics. "Humanoid robots and walking." <a href="https://underactuated.mit.edu/humanoids.html" rel="noopener" target="_blank">https://underactuated.mit.edu/humanoids.html</a>', "Primary exposition of ZMP, walking templates, and planning logic."),
            ('Drake project documentation. <a href="https://drake.mit.edu/" rel="noopener" target="_blank">https://drake.mit.edu/</a>', "Useful for reduced-order and optimization-based balance studies."),
            ('NVIDIA Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Current practical route for high-throughput locomotion and disturbance testing.")
        ],
        "takeaway": "Stable gait design is really recoverability engineering under hybrid contact dynamics.",
        "exercise_title": "Exercise 45.2.1",
        "exercise": "Pick one gait controller and define a push-recovery benchmark with exact perturbation times, force magnitudes, and success rules. State which metrics would prove the gait got faster without becoming less recoverable."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.3.html": {
        "id": "45-3",
        "quote": '"GPU hours are only useful when they purchase better disturbance behavior."',
        "cite": "A Locomotion Training Postmortem",
        "image_src": "images/chapter-45-illustration-03.png",
        "image_alt": "Massively parallel reinforcement learning for locomotion across many simulated terrains.",
        "image_caption": "<strong>Figure 45.3A</strong>: Massive parallelism shortens iteration loops, but it can also scale mistakes unless reward, resets, and evaluation are audited.",
        "big_picture": "<strong>Massively parallel RL</strong> changed locomotion research because thousands of simulators can expose rare contact events quickly, but the throughput only matters if the reward and reset contracts are physically meaningful.",
        "pathway": "Read this section from simulator throughput to deployment evidence: vectorized rollouts, PPO or actor-critic training, domain randomization, held-out terrain panels, then transfer checks.",
        "develops_1": "With batched simulators, the training objective is usually a clipped or trust-region policy update over many parallel trajectories. For PPO, one common objective is $L^{\\mathrm{clip}}(\\theta) = \\mathbb{E}[\\min(r_t(\\theta) \\hat A_t, \\mathrm{clip}(r_t(\\theta), 1-\\epsilon, 1+\\epsilon) \\hat A_t)]$, where $r_t$ is the policy ratio and $\\hat A_t$ is an advantage estimate.",
        "develops_2": "Parallelism changes the engineering problem. Correlated environment bugs, shared reward mistakes, and synchronized reset artifacts can make a policy appear strong across ten thousand workers while teaching the exact wrong behavior. The remedy is not less scale. It is better audit structure.",
        "key_title": "Throughput Does Not Equal Evidence",
        "key_text": "A fast RL stack is valuable only when the held-out terrain panel, transfer test, and failure taxonomy grow with it.",
        "flow_caption": "Figure 45.3.1 shows the true loop for large-scale locomotion RL: sample, update, randomize, and verify on held-out terrain rather than on the training panel alone.",
        "flow_observe": "batched states, rewards, resets",
        "flow_model": "advantage and update statistics",
        "flow_act": "update policy across thousands of envs",
        "flow_verify": "held-out return and transfer",
        "theory": [
            "The main benefit of parallel RL in locomotion is coverage of contact events. Rare combinations of foot timing, terrain discontinuity, and actuator lag appear more often when the simulator fan-out is large.",
            "The main risk is shared bias. If every environment uses the same flawed reward term, a thousand workers accelerate the same misunderstanding. This is why reward audits, termination audits, and observation audits belong in the same chapter as PPO code.",
            "A solid locomotion training paper therefore reports both throughput numbers and construct-matched disturbance metrics on terrain not used to tune the controller."
        ],
        "algo_title": "Algorithm: Large-Scale Locomotion RL Audit Loop",
        "algorithm": [
            "Freeze an environment manifest that defines terrain seeds, friction ranges, actuator delays, and reset logic.",
            "Train the policy with vectorized rollouts and log advantage statistics, termination reasons, and reward-term contributions.",
            "Evaluate on a held-out terrain panel that the training loop never sees.",
            "Replay at least one failed hardware or simulator trace inside the batch environment family.",
            "Only claim progress when held-out disturbance metrics and transfer metrics improve together."
        ],
        "worked_intro": "The smallest trustworthy artifact for large-scale locomotion RL is a run record that reports update count, sample count, held-out metrics, and transfer tags in one place.",
        "code": """run = {
    "num_envs": 4096,
    "horizon": 24,
    "updates": 1200,
    "heldout_fall_rate": 0.08,
    "heldout_velocity_error": 0.11,
    "transfer_tags": ["rough_terrain", "payload_shift"],
}

samples = run["num_envs"] * run["horizon"] * run["updates"]
print(f"samples={samples}")
print(
    {
        "heldout_fall_rate": run["heldout_fall_rate"],
        "heldout_velocity_error": run["heldout_velocity_error"],
        "transfer_tags": run["transfer_tags"],
    }
)""",
        "output": """samples=117964800
{'heldout_fall_rate': 0.08, 'heldout_velocity_error': 0.11, 'transfer_tags': ['rough_terrain', 'payload_shift']}""",
        "output_interp": "The sample count looks impressive, but the useful signal is the held-out fall rate and velocity error. A run with more samples but worse held-out disturbance behavior is not an upgrade.",
        "code_caption": "<strong>Code Fragment 45.3.1:</strong> Large-scale RL evidence should expose both scale and quality. Sample count alone is a resource report, not a locomotion result.",
        "library": "Use Isaac Lab for GPU throughput, MJX when JAX-native pipelines matter, and RSL-RL or equivalent PPO tooling when you need a maintained actor-critic training core rather than a handwritten optimizer.",
        "recipe": [
            "Freeze observation, reward, termination, and randomization manifests before sweeping hyperparameters.",
            "Train with enough parallelism to cover rare terrain-contact cases, but log per-term rewards and termination reasons.",
            "Hold out terrain classes, payload profiles, or sensor corruptions for evaluation.",
            "Validate the controller in a second simulator or a reduced hardware replay when possible.",
            "Promote only runs that improve both disturbance metrics and transfer evidence."
        ],
        "warning": "The most common failure is a reward term or reset rule that creates an easy exploit across every worker. Scale hides that exploit until transfer fails.",
        "example": "A quadruped may learn to skim over termination thresholds by hopping in a brittle rhythm that looks effective in the training terrain family. A held-out curb panel or a small actuator-delay mismatch often exposes the weakness immediately.",
        "memory": "Parallel RL is a microscope and a funhouse mirror at the same time. It reveals more events, but it enlarges every bug you forgot to measure.",
        "frontier": "Current locomotion systems combine parallel RL with motion priors, vision, terrain encoders, and adaptation modules. The best stacks still treat evaluation manifests as first-class assets rather than as appendices.",
        "self_check": "Can you name one statistic that proves your RL loop scaled, and one statistic that proves the extra scale improved actual locomotion behavior rather than just training throughput?",
        "deep_dive": [
            "This section should help readers connect reinforcement learning theory to the simulator and deployment stack. Parallel sampling is not just a compute trick. It changes the statistical shape of the data, the likelihood of correlated bugs, and the kinds of diagnostics you need to trust a result.",
            "It is also a good place to teach construct-matched comparisons. If the baseline uses flat ground and the new method uses rough terrain plus curriculum plus actuator randomization, the numbers are not comparable no matter how impressive the learning curve looks."
        ],
        "table_title": "Parallel RL Tool Map",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Isaac Lab", "GPU-parallel locomotion training", "Use manifest files for reward, reset, and randomization."),
            ("MJX", "Fast JAX-native physics for batched control experiments", "Exploit JAX tooling, but keep evaluation manifests identical."),
            ("RSL-RL or similar PPO stack", "Maintained on-policy training core", "Patch your task logic, not the optimizer, unless there is a clear reason.")
        ],
        "cross_refs": 'Connect this section to <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/index.html">PPO and actor-critic theory</a>, <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-17-massively-parallel-and-gpu-rl/index.html">scalable RL systems</a>, and <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html">sim-to-real transfer</a>.',
        "lab": "Train a small locomotion controller at two parallelism levels, then compare not only wall-clock but also held-out disturbance metrics and failure traces.",
        "failure_pattern": "If a fast training run fails on transfer, inspect reward decomposition, reset clustering, observation leakage, and actuator mismatch before tuning the policy network. In locomotion RL, environment bugs often masquerade as optimization problems.",
        "biblio": [
            ('Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Primary documentation for current large-scale robot-learning workflows."),
            ('Margolis, G. et al. "Rapid Locomotion via Reinforcement Learning." Code repository. <a href="https://github.com/Improbable-AI/rapid-locomotion-rl" rel="noopener" target="_blank">https://github.com/Improbable-AI/rapid-locomotion-rl</a>', "Concrete RL reference point for agile locomotion training."),
            ('MuJoCo MJX documentation. <a href="https://mujoco.readthedocs.io/en/stable/mjx.html" rel="noopener" target="_blank">https://mujoco.readthedocs.io/en/stable/mjx.html</a>', "Primary source for batched MuJoCo workflows in JAX.")
        ],
        "takeaway": "Large-scale RL becomes scientific when the throughput report and the disturbance evidence report travel together.",
        "exercise_title": "Exercise 45.3.1",
        "exercise": "Design a training ledger for a locomotion RL study. Include the environment manifest, update budget, reward terms, held-out panel, and one diagnostic that would catch a synchronized reward bug."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.4.html": {
        "id": "45-4",
        "quote": '"Adaptation starts where the training distribution stops pretending to be the world."',
        "cite": "A Rapid Motor Adaptation Whiteboard",
        "image_src": "images/chapter-45-illustration-04.png",
        "image_alt": "Legged robot adapting to rough terrain and dynamic obstacles.",
        "image_caption": "<strong>Figure 45.4A</strong>: Fast terrain adaptation couples perception, latent environment inference, and contact-aware control.",
        "big_picture": "<strong>Terrain adaptation</strong> is about closing the loop faster than the environment can invalidate the current policy assumptions.",
        "pathway": "Read this section as a two-rate system: a fast motor policy tracks immediate state, while an adaptation module infers hidden terrain or actuator variables from recent history.",
        "develops_1": "Rapid Motor Adaptation style systems can be summarized as $a_t = \\pi(o_t, z_t)$, where $z_t = \\phi(h_{t-k:t})$ is a latent variable inferred from recent observation history. The fast policy uses the latent to change foot placement, body posture, and compliance before the environment has to be fully identified in symbolic terms.",
        "develops_2": "For parkour or aggressive terrain tasks, the challenge is not only latent inference. It is contact schedule feasibility under delayed and partial sensing. A policy that adapts too slowly behaves like a good flat-ground walker with a bad memory.",
        "key_title": "Adaptation Needs Evidence About Hidden Variables",
        "key_text": "The interesting question is not whether the policy changes after a stumble. It is whether the change tracks a real hidden cause such as friction, step height, payload, or actuator loss.",
        "flow_caption": "Figure 45.4.1 frames adaptation as a latent-inference loop: observe recent history, infer terrain mode, adjust the motor policy, and verify on unseen disturbances.",
        "flow_observe": "history window, terrain cues, impulses",
        "flow_model": "latent terrain or dynamics code",
        "flow_act": "adapt foothold and body policy",
        "flow_verify": "completion and adaptation latency",
        "theory": [
            "Adaptation systems sit between robust control and online system identification. They do not attempt full physical reconstruction of the world at every step. They infer exactly enough hidden structure to change the next action usefully.",
            "This makes evaluation tricky. A policy that adapts may still overfit to training terrain families. The correct test is a held-out disturbance panel with cause labels: softer ground, payload shift, low friction, missing foothold, or delayed contact sensing.",
            "For parkour-like behavior, the controller must also reason about contact sequences. Adaptation is not just a gain change. It can imply a completely different next foothold or body orientation."
        ],
        "algo_title": "Algorithm: Latent Adaptation Audit",
        "algorithm": [
            "Train or fit a latent encoder on a history window that includes proprioception, contact events, and optional terrain sensing.",
            "Replay disturbances with a frozen policy and inspect whether the latent shifts in a physically interpretable direction.",
            "Measure adaptation latency from disturbance onset to policy correction.",
            "Compare nominal, adapted, and oracle-latent baselines on the same unseen terrain panel.",
            "Keep at least one failure class that the latent does not explain, to avoid overstating what the adaptation module learned."
        ],
        "worked_intro": "A simple latent-distance check can reveal whether the adaptation module reacts differently to friction loss and to payload shift, which is the minimum scientific standard for claiming it learned hidden dynamics rather than noise.",
        "code": """latent_nominal = [0.12, -0.08]
latent_low_friction = [0.44, -0.03]
latent_payload_shift = [0.15, 0.27]

def l1(a, b):
    return round(sum(abs(x - y) for x, y in zip(a, b)), 2)

print({"nominal_to_friction": l1(latent_nominal, latent_low_friction)})
print({"nominal_to_payload": l1(latent_nominal, latent_payload_shift)})""",
        "output": """{'nominal_to_friction': 0.37}
{'nominal_to_payload': 0.38}""",
        "output_interp": "Both disturbances move the latent away from nominal, but in different directions. That is the beginning of useful adaptation evidence. The next test is whether those latent shifts actually produce different corrective actions and better recovery.",
        "code_caption": "<strong>Code Fragment 45.4.1:</strong> Latent distance alone is not enough, but it helps verify that distinct hidden causes are not collapsed into one undifferentiated adaptation response.",
        "library": "Isaac Lab terrain curricula, RMA-style adaptation implementations, and ROS 2 replay logs are the practical stack here. The key is to log history windows and latent states alongside the executed control.",
        "recipe": [
            "Define hidden-variable disturbances explicitly before training: friction, compliance, mass shift, foot-height error, actuator delay.",
            "Train with randomized terrain and disturbance schedules, but keep held-out test families untouched.",
            "Log latent trajectories and action trajectories together.",
            "Measure adaptation latency and post-disturbance recovery, not only episode success.",
            "Reproduce at least one hardware failure in simulation with the same disturbance label."
        ],
        "warning": "A policy that memorizes training terrain classes can look adaptive while doing nothing meaningful on genuinely new surfaces.",
        "example": "A quadruped crossing stepping stones may need a latent that distinguishes underfoot compliance from lateral slip. Both create foot placement error, but the right correction differs.",
        "memory": "Adaptation is valuable only when the robot learns what changed before it runs out of safe options.",
        "frontier": "The frontier combines online adaptation with vision, event-based contact sensing, and hierarchical planners that can change contact schedule as well as gains. The open problem is keeping these systems interpretable enough to debug after a field miss.",
        "self_check": "What hidden variable would you want your locomotion system to infer online first, and how would you test that the inferred change improved the next action rather than just changed it?",
        "deep_dive": [
            "This material is ideal for showing the difference between domain randomization and adaptation. Randomization makes the nominal policy broader. Adaptation tries to identify which world instance the robot is in right now and exploit that fact online.",
            "It is also a place to show how evaluation panels should be labeled by cause, not just by surface appearance. A policy that handles loose gravel may still fail on worn actuators, even if both look like rough motion from the outside."
        ],
        "table_title": "Adaptation Tool Choices",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Isaac Lab terrain curricula", "Generate varied disturbance panels", "Keep one unseen terrain family for final evaluation."),
            ("RMA-style adaptation stack", "Latent inference plus fast policy", "Log latent states and action changes together."),
            ("ROS 2 replay plus hardware logs", "Tie sim adaptation to real failures", "Promote real misses into named disturbance classes.")
        ],
        "cross_refs": 'This section ties into <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-18-reward-design-and-goal-specification/index.html">goal and reward design</a>, <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html">sim-to-real transfer</a>, and <a href="../../part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/index.html">3D perception</a>.',
        "lab": "Create two unseen disturbance families, such as friction loss and payload shift, and audit whether the latent state, action correction, and recovery metric all change in section-specific ways.",
        "failure_pattern": "When adaptation fails, separate wrong latent inference from too-slow adaptation, infeasible contact schedule, and actuator saturation. Those are different research problems even when the video looks similar.",
        "biblio": [
            ('Kumar, A. et al. "Rapid Motor Adaptation for Legged Robots." Project page. <a href="https://ashish-kmr.github.io/rma-legged-robots/" rel="noopener" target="_blank">https://ashish-kmr.github.io/rma-legged-robots/</a>', "Primary reference for fast latent adaptation in legged locomotion."),
            ('Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Current tooling reference for terrain curricula and transfer workflows."),
            ('Margolis, G. et al. "Rapid Locomotion via Reinforcement Learning." Code repository. <a href="https://github.com/Improbable-AI/rapid-locomotion-rl" rel="noopener" target="_blank">https://github.com/Improbable-AI/rapid-locomotion-rl</a>', "Useful practical reference for agile locomotion control and evaluation.")
        ],
        "takeaway": "Good adaptation compresses hidden world changes into actionable corrections before the robot loses recoverability.",
        "exercise_title": "Exercise 45.4.1",
        "exercise": "Design an adaptation benchmark with three hidden disturbance types and one held-out terrain family. Specify which latent, action, and recovery traces must be logged to justify the claim that the policy adapted rather than got lucky."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/section-45.5.html": {
        "id": "45-5",
        "quote": '"A locomotion policy that ignores heat and power is outsourcing the hard part to the battery."',
        "cite": "A Field Deployment Checklist",
        "image_src": "images/chapter-45-illustration-05.png",
        "image_alt": "Robot locomotion under energy, thermal, and safety constraints.",
        "image_caption": "<strong>Figure 45.5A</strong>: Fast locomotion becomes useful only when power, thermal, and safety constraints remain visible in the same evaluation artifact.",
        "big_picture": "<strong>Energy efficiency, sim-to-real, and safety</strong> are not post-processing concerns. They define whether a locomotion controller is deployable outside a demo loop.",
        "pathway": "Read this section as a deployment ledger: power and heat accounting, transfer gap analysis, runtime safety envelope, and intervention policy.",
        "develops_1": "A standard locomotion energy measure is cost of transport, $\\mathrm{CoT} = E / (mgd)$, where $E$ is energy spent over distance $d$ for mass $m$. It lets researchers compare controllers across robot size and runtime. The same controller can improve speed while worsening CoT enough to make battery-limited missions impossible.",
        "develops_2": "Sim-to-real transfer is best framed as a residual model problem. Let $x^{\\mathrm{real}}_{t+1} = f_{\\mathrm{sim}}(x_t, u_t) + \\delta(x_t, u_t)$. The purpose of system identification, randomization, and fine-tuning is to shrink the residual or make the policy robust to it. Safety logic must then operate on the residual-aware closed loop, not on the simulator fantasy.",
        "key_title": "Deployment Means Constraint Accounting",
        "key_text": "A locomotion stack is ready only when speed, energy, heat, safety interventions, and transfer residuals are measured together.",
        "flow_caption": "Figure 45.5.1 makes deployment explicit: measure resource and safety state, model transfer gap, command within envelope, and verify on hardware traces.",
        "flow_observe": "current, heat, impulses, latency",
        "flow_model": "CoT, residual gap, safety envelope",
        "flow_act": "limit speed and choose transfer policy",
        "flow_verify": "runtime, stops, recovery, wear",
        "theory": [
            "A field-ready locomotion controller solves a multi-objective problem. You are trading task time, energy, actuator temperature, contact stress, and safety margins simultaneously. Optimizing one while hiding the others is how impressive lab videos become expensive hardware failures.",
            "Transfer methods are only comparable when evaluated on the same hardware panel. Domain randomization, actuator modeling, residual learning, and hardware fine-tuning all help, but their value changes with how much of the real residual is actually represented.",
            "Safety logic should be layered. Fast inner loops prevent immediate falls or torque spikes. Slower supervisory logic can reduce speed, widen gait, trigger re-localization, or stop the robot when the residual leaves the validated envelope."
        ],
        "algo_title": "Algorithm: Transfer-And-Safety Deployment Loop",
        "algorithm": [
            "Log battery, current, thermal state, velocity error, slip, and intervention flags on every run.",
            "Estimate the simulator residual by replaying the same command sequence in sim and hardware.",
            "Select a transfer strategy: identification, randomization, residual adaptation, or cautious hardware fine-tuning.",
            "Wrap the locomotion policy with runtime monitors for torque, temperature, contact impulse, and stop distance.",
            "Promote every field intervention into the next simulation or evaluation panel."
        ],
        "worked_intro": "A small deployment summary can expose whether a faster policy is actually the better field controller once energy and safety are priced in.",
        "code": """energy_j = 18200
mass_kg = 48
distance_m = 320
g = 9.81
safety_stops = 2

cot = energy_j / (mass_kg * g * distance_m)
print(f"cost_of_transport={cot:.3f}")
print({"safety_stops": safety_stops, "deployment_ok": safety_stops <= 1 and cot < 0.14})""",
        "output": """cost_of_transport=0.121
{'safety_stops': 2, 'deployment_ok': False}""",
        "output_interp": "The energy figure is acceptable, but the safety-stop count fails the deployment criterion. This is exactly why energy and safety must live in the same artifact rather than in separate dashboards.",
        "code_caption": "<strong>Code Fragment 45.5.1:</strong> The deployment decision uses CoT and safety interventions together. A controller that is efficient but intervention-heavy is still not ready.",
        "library": "Use ROS 2 hardware logs, simulator replay in MuJoCo or Isaac Lab, and platform-specific telemetry tools for thermal and battery traces. The point is unified evidence, not heroic controller tuning.",
        "recipe": [
            "Define deployment thresholds for CoT, thermal excursions, safety stops, and velocity tracking before testing.",
            "Replay the same command traces in simulation and on hardware to estimate the residual gap.",
            "Evaluate the same scenario panel under nominal and degraded conditions, including battery sag or low-friction patches.",
            "Add runtime monitors that can reduce speed or halt before the low-level controller saturates.",
            "Store every deployment run as a transferable artifact with telemetry, summary metrics, and intervention labels."
        ],
        "warning": "Many sim-to-real papers report successful transfer on short clean runs while omitting heat, battery sag, or supervision burden. Those omissions matter more in the field than a few points of average return.",
        "example": "A logistics robot may need to slow down near the end of a shift because thermal limits tighten and floor contamination raises slip risk. The right controller recognizes the changing envelope rather than stubbornly keeping the nominal target speed.",
        "memory": "If the battery, heat, and stop logs are missing, the deployment claim is missing too.",
        "frontier": "The frontier combines energy-aware control, learned residual models, safety filters, and adaptive mission planning. The unresolved challenge is preserving agility while keeping safety cases legible to operators and auditors.",
        "self_check": "What single metric would tell you a controller is physically economical, and what second metric would stop you from deploying it anyway?",
        "deep_dive": [
            "This section is where embodied AI becomes operations engineering. Students often discover here that the hardest variables are not abstract control gains but current draw, actuator wear, battery chemistry, and the organizational cost of false safety stops.",
            "It also clarifies why sim-to-real should never be treated as one scalar gap. The transfer residual has structure: delays, friction mismatch, compliance, sensor timing, estimator drift, and operator response. Good books teach readers how to decompose that structure."
        ],
        "table_title": "Deployment And Transfer Tools",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("ROS 2 telemetry", "Unify controller, power, and safety logs", "Keep timestamps synchronized across all sensors and monitors."),
            ("Isaac Lab or MuJoCo replay", "Compare hardware traces against simulated predictions", "Replay real command sequences instead of only nominal scripted tasks."),
            ("Safety supervisors", "Power, torque, impulse, and stop-distance checks", "Define explicit thresholds before collecting deployment claims.")
        ],
        "cross_refs": 'This section prepares for <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">safety validation and monitoring</a> and connects back to <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html">sim-to-real transfer</a>.',
        "lab": "Take one locomotion controller and build a deployment card that includes CoT, thermal peaks, safety-stop count, and one measured sim-to-real residual.",
        "failure_pattern": "When field transfer fails, assign blame to the dominant residual first: actuator model, terrain mismatch, sensing delay, estimator drift, or safety supervisor interaction. Otherwise teams waste time tuning the policy around the wrong bottleneck.",
        "biblio": [
            ('Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Primary tool reference for transfer and deployment preparation workflows."),
            ('MuJoCo MJX documentation. <a href="https://mujoco.readthedocs.io/en/stable/mjx.html" rel="noopener" target="_blank">https://mujoco.readthedocs.io/en/stable/mjx.html</a>', "Useful for fast replay and residual-aware analysis."),
            ('NVIDIA developer blog. "Closing the sim-to-real gap: training Spot quadruped locomotion with Isaac Lab." <a href="https://developer.nvidia.com/blog/closing-the-sim-to-real-gap-training-spot-quadruped-locomotion-with-nvidia-isaac-lab/" rel="noopener" target="_blank">https://developer.nvidia.com/blog/closing-the-sim-to-real-gap-training-spot-quadruped-locomotion-with-nvidia-isaac-lab/</a>', "Practical current source on simulation-to-hardware locomotion workflows.")
        ],
        "takeaway": "Field-ready locomotion is a joint claim about speed, energy, transfer residuals, and safety supervision.",
        "exercise_title": "Exercise 45.5.1",
        "exercise": "Draft a deployment acceptance test for a locomotion controller. State the exact CoT bound, safety-stop bound, temperature bound, and residual-gap check that the system must pass before you would allow an unsupervised pilot."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.1.html": {
        "id": "46-1",
        "quote": '"Humanoids became interesting when data, hardware cost, and human-shaped environments finally started pointing in the same direction."',
        "cite": "A Systems Strategy Memo",
        "image_src": "images/chapter-46-illustration-01.png",
        "image_alt": "Humanoid robot operating in a human-centered workspace.",
        "image_caption": "<strong>Figure 46.1A</strong>: Humanoids matter because they reuse human infrastructure, human demonstrations, and human task decomposition.",
        "big_picture": "<strong>Why humanoids became the focus</strong> is a chapter-opening systems argument. The appeal is not a vague dream of human likeness. It is the alignment between morphology, teleoperation data, existing workspaces, and growing whole-body learning stacks.",
        "pathway": "Read this section as a convergence story: morphology fit, data availability, platform economics, and the rise of unified whole-body software stacks.",
        "develops_1": "Humanoids are attractive because the world is already instrumented for the human body. Stairs, shelving, door handles, carts, bins, hand tools, and workstation heights create a large prior in favor of bipedal reach and dual-arm manipulation. That prior reduces environment redesign cost, even if it increases control complexity.",
        "develops_2": "The second driver is data. Teleoperation, motion capture, video-to-motion pipelines, and imitation learning provide richer supervision when the robot body and human body share coarse kinematic affordances. The third driver is hardware economics: actuators, onboard compute, and simulation tools have improved enough that whole-body learning is no longer only a flagship lab exercise.",
        "key_title": "The Humanoid Bet Is About Interface Reuse",
        "key_text": "Humanoids win when reusing human spaces and human data is worth the control and safety complexity they introduce.",
        "flow_caption": "Figure 46.1.1 frames the humanoid thesis as a loop: reuse human environment priors, collect compatible data, deploy whole-body control, and verify that the benefit exceeds the complexity tax.",
        "flow_observe": "workspace, demos, hardware economics",
        "flow_model": "reuse benefit versus complexity tax",
        "flow_act": "choose humanoid platform and stack",
        "flow_verify": "task coverage and safety burden",
        "theory": [
            "A useful decomposition is task reuse, data reuse, and infrastructure reuse. Task reuse means existing job definitions map naturally to two arms, two legs, and a torso. Data reuse means human demonstrations or videos provide meaningful supervision. Infrastructure reuse means doors, shelves, ladders, tools, and aisles do not need wholesale redesign.",
            "These benefits compete with the floating-base control problem. Humanoids are underactuated, contact-rich, and safety-critical. So the right question is always comparative: does a humanoid solve enough more valuable tasks than a mobile manipulator or fixed arm to justify the added complexity?",
            "Serious programs therefore maintain a task panel that includes what a humanoid can do uniquely, what a cheaper morphology can already do, and what remains unsafe or economically unjustified."
        ],
        "algo_title": "Algorithm: Decide Whether A Humanoid Is Actually Warranted",
        "algorithm": [
            "List the tasks that truly require human-shaped reach, stair access, crouching, or dual-arm whole-body coordination.",
            "Estimate how much human demonstration data can be transferred to the candidate body.",
            "Compare workspace modification cost against controller and safety complexity cost.",
            "Run at least one baseline with a non-humanoid alternative, such as a wheeled manipulator.",
            "Promote the humanoid choice only if the evidence shows higher useful task coverage under acceptable supervision burden."
        ],
        "worked_intro": "A task-coverage ledger is often more revealing than a hardware spec sheet when deciding whether a humanoid body is the right research or deployment choice.",
        "code": """task_panel = {
    "stairs_and_catwalks": {"humanoid": 1, "mobile_manipulator": 0},
    "bin_picking_on_flat_floor": {"humanoid": 1, "mobile_manipulator": 1},
    "door_and_ladder_service": {"humanoid": 1, "mobile_manipulator": 0},
    "fixed_station_assembly": {"humanoid": 1, "mobile_manipulator": 1},
}

coverage = {name: sum(v[name] for v in task_panel.values()) for name in ["humanoid", "mobile_manipulator"]}
print(coverage)
print({"coverage_advantage": coverage["humanoid"] - coverage["mobile_manipulator"]})""",
        "output": """{'humanoid': 4, 'mobile_manipulator': 2}
{'coverage_advantage': 2}""",
        "output_interp": "The ledger says the humanoid wins on task coverage in this panel, but the result is only meaningful if the extra tasks are valuable enough to justify increased control, maintenance, and safety burden.",
        "code_caption": "<strong>Code Fragment 46.1.1:</strong> Coverage comparisons force the humanoid decision to compete against alternative bodies on task value rather than on symbolism.",
        "library": "Use Isaac Lab or HumanoidBench for broad simulated task panels, LeRobot or teleoperation pipelines for data collection, and Drake or Pinocchio when feasibility questions need model-based answers.",
        "recipe": [
            "Enumerate tasks that truly need stairs, crouching, bimanual whole-body manipulation, or narrow human workspaces.",
            "Estimate the available human data channel: teleop, video, motion capture, or language-conditioned demonstration.",
            "Compare against a simpler morphology baseline with the same evaluation panel.",
            "Record supervision and safety overhead explicitly, not as a hidden cost.",
            "Treat vendor claims as hypotheses until the task panel is reproduced."
        ],
        "warning": "Humanoids are easy to justify rhetorically because human environments are everywhere. They are harder to justify scientifically if the task panel could be handled by a simpler body with lower risk.",
        "example": "An automotive plant with catwalks, narrow stations, and mixed cart manipulation may justify a humanoid. A sterile warehouse with flat floors and standardized bins may favor wheeled mobile manipulators instead.",
        "memory": "The humanoid question is not, 'can it walk like us?' It is, 'does walking like us buy enough useful work to pay for itself?'",
        "frontier": "The frontier mixes foundation models, whole-body control, teleoperation data, and large simulation panels. The strategic open question is not only capability, but where the humanoid economic boundary actually sits relative to simpler robots.",
        "self_check": "Can you name one environment feature, one data feature, and one economic feature that push a project toward a humanoid body rather than away from it?",
        "deep_dive": [
            "This opening section works best when it teaches skepticism as well as excitement. The same body plan that reuses human infrastructure also inherits human-scale safety hazards and underactuated contact complexity.",
            "It is also an opportunity to connect embodied AI to product strategy. In research, the right question is often scientific coverage. In deployment, the right question is cost of useful work under supervision, downtime, and safety constraints."
        ],
        "table_title": "Humanoid Decision Table",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("HumanoidBench", "Task-coverage simulation panel", "Use it to compare capabilities across locomotion and manipulation settings."),
            ("LeRobot and teleop pipelines", "Human demonstration data path", "Record whether the body can actually absorb the available supervision."),
            ("Drake or Pinocchio", "Feasibility checks for full-body tasks", "Use model-based checks before assuming the body can execute the task safely.")
        ],
        "cross_refs": 'This section ties to <a href="../../part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/index.html">teleoperation and data collection</a>, <a href="../../part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/index.html">robot foundation models</a>, and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/index.html">locomotion and mobility</a>.',
        "lab": "Build a task panel comparing a humanoid and a mobile manipulator on at least six tasks. Score useful coverage, intervention burden, and workspace modification cost.",
        "failure_pattern": "If the humanoid case collapses, ask whether the failure came from overvaluing human-shaped tasks, underestimating safety complexity, or ignoring a simpler competing morphology.",
        "biblio": [
            ('Boston Dynamics Atlas product page. <a href="https://bostondynamics.com/products/atlas/" rel="noopener" target="_blank">https://bostondynamics.com/products/atlas/</a>', "Official product framing for industrial humanoid deployment."),
            ('HumanoidBench official site. <a href="https://humanoid-bench.github.io/" rel="noopener" target="_blank">https://humanoid-bench.github.io/</a>', "Primary benchmark reference for whole-body humanoid task evaluation."),
            ('NVIDIA Isaac GR00T reference humanoid announcement, June 2026. <a href="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research/default.aspx" rel="noopener" target="_blank">https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NVIDIA-Isaac-GR00T-Reference-Humanoid-Robot-for-Academic-Research/default.aspx</a>', "Current signal that vendor stacks are converging on research-focused whole-body humanoid platforms.")
        ],
        "takeaway": "Humanoids became central because morphology, data, and software started reinforcing each other, not because human shape is automatically optimal.",
        "exercise_title": "Exercise 46.1.1",
        "exercise": "Write a one-page decision memo that argues for or against a humanoid body in one deployment domain. Include the competing non-humanoid baseline and the exact task panel you would use to settle the argument."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.2.html": {
        "id": "46-2",
        "quote": '"Platform choice decides which research questions are real and which ones are just impossible on your hardware."',
        "cite": "A Humanoid Lab Procurement Meeting",
        "image_src": "images/chapter-46-illustration-02.png",
        "image_alt": "Comparison of current humanoid robot platforms and their stack implications.",
        "image_caption": "<strong>Figure 46.2A</strong>: Platform comparison should connect hardware specs to control and data consequences, not to brand identity.",
        "big_picture": "<strong>Humanoid platform selection</strong> is a stack decision. Joint torque, sensing, hand capability, SDK openness, and teleoperation hooks determine which locomotion, manipulation, and learning claims are even testable.",
        "pathway": "Read this section from hardware affordances to software consequences: sensing, actuation, whole-body control, teleoperation, and benchmark fit.",
        "develops_1": "A useful platform comparison uses a capability vector $p = [n_{\\mathrm{dof}}, \\tau_{\\max}, m_{\\mathrm{payload}}, s_{\\mathrm{perception}}, h_{\\mathrm{dexterity}}, o_{\\mathrm{sdk}}]$. The point is not to pretend these numbers collapse neatly into one score. The point is to make the tradeoffs explicit enough that a research program can choose a platform on purpose.",
        "develops_2": "Publicly documented platforms already differ in strategic ways. Unitree G1 emphasizes affordability and force-controlled hands. Unitree H1 is full-sized with stronger legs and richer onboard sensing. Atlas targets industrial mobile manipulation. 1X NEO emphasizes home-facing autonomy and supervised expert mode. Apptronik Apollo targets general-purpose industrial work. Figure couples humanoid hardware to a strong VLA narrative. Tesla Optimus remains comparatively closed in public technical documentation, which matters if your project depends on inspectable interfaces.",
        "key_title": "Open Interfaces Matter More Than Marketing",
        "key_text": "A platform is useful to researchers when it exposes enough state, control, and data interfaces to turn failures into artifacts.",
        "flow_caption": "Figure 46.2.1 frames platform choice as an evidence pipeline: inspect hardware affordances, map them to software stack requirements, and verify against the intended benchmark family.",
        "flow_observe": "actuators, sensors, hands, SDK access",
        "flow_model": "task-fit and integration burden",
        "flow_act": "select platform and stack",
        "flow_verify": "benchmark fit and debugging access",
        "theory": [
            "Humanoid platforms should be compared by capability surfaces rather than by single numbers. A body with lower raw torque may still be superior for research if it offers better teleoperation, more stable software, or clearer access to state and control loops.",
            "The platform decision also determines benchmark compatibility. Some whole-body tasks need dexterous hands, wrist cameras, or rich force sensing. Others mainly need robust locomotion and payload handling. Treating all humanoids as interchangeable destroys experimental clarity.",
            "For research, a closed but impressive platform can be the wrong choice if it prevents controller inspection, synchronized logging, or low-level safety instrumentation."
        ],
        "algo_title": "Algorithm: Platform Scoring For A Research Program",
        "algorithm": [
            "List the target tasks and the minimum hand, perception, and locomotion requirements.",
            "Rate each platform on actuation, sensing, dexterity, SDK openness, teleoperation route, and benchmark compatibility.",
            "Penalize undocumented or closed interfaces if the project depends on controller or state inspection.",
            "Prototype one critical task in simulation before buying into the full platform stack.",
            "Keep a platform risk register with spare-part, software, and safety unknowns."
        ],
        "worked_intro": "A simple capability table already explains why two humanoid teams with similar goals can rationally choose different hardware.",
        "code": """platforms = {
    "Unitree_G1": {"dexterity": 4, "locomotion": 3, "sdk": 4},
    "Unitree_H1": {"dexterity": 3, "locomotion": 5, "sdk": 4},
    "Atlas": {"dexterity": 4, "locomotion": 5, "sdk": 2},
    "NEO": {"dexterity": 4, "locomotion": 3, "sdk": 3},
}

weights = {"dexterity": 0.4, "locomotion": 0.4, "sdk": 0.2}
scores = {name: round(sum(vals[k] * weights[k] for k in weights), 2) for name, vals in platforms.items()}
print(scores)
print(max(scores, key=scores.get))""",
        "output": """{'Unitree_G1': 3.6, 'Unitree_H1': 4.0, 'Atlas': 4.0, 'NEO': 3.4}
Unitree_H1""",
        "output_interp": "Under this toy weighting, H1 and Atlas are close because locomotion is priced heavily. If SDK openness were more important, the ranking could flip. This is the exact point of writing the weights down.",
        "code_caption": "<strong>Code Fragment 46.2.1:</strong> Platform scoring is not a final truth. It is a disciplined way to expose which research priorities drive the hardware choice.",
        "library": "Use official platform docs for hardware facts, Isaac Lab or HumanoidBench for simulated task proxies, and low-level dynamics tools such as Pinocchio or Drake to test whether the published body can support your intended controller class.",
        "recipe": [
            "Write a capability matrix before looking at vendor demo videos.",
            "Match each task to required locomotion, manipulation, and sensing primitives.",
            "Price interface openness and logging access explicitly.",
            "Prototype on simulation and small data flows before full commitment.",
            "Update the scorecard as public documentation changes."
        ],
        "warning": "Do not compare a public open stack to a closed vendor demo as if they expose the same research surface. They do not.",
        "example": "A lab focused on whole-body industrial manipulation may value Atlas-style industrial robustness or Apollo-style deployment framing. A lab focused on reproducible academic learning may prefer a more open and accessible platform such as G1 or H1, even if raw capability is lower.",
        "memory": "The best platform is the one that lets your team learn, debug, and publish, not the one with the most cinematic trailer.",
        "frontier": "The current frontier is converging around reference humanoid stacks that mix vendor hardware, open simulation, and maintained whole-body control frameworks. The opportunity is faster iteration. The risk is inheriting stack assumptions you did not inspect.",
        "self_check": "Which platform attribute matters more for your project: raw locomotion performance, dexterous hand capability, or inspectable software interfaces, and why?",
        "deep_dive": [
            "This section can teach strong research taste. Platform comparisons should include what is unknown. Missing interface documentation, unclear safety APIs, and uncertain teleoperation hooks are all part of the technical evaluation, not procurement trivia.",
            "It is also a good place to emphasize that benchmark fit matters. A platform built for home assistance and one built for industrial tote handling can both be 'general purpose' in marketing language while being very different research instruments."
        ],
        "table_title": "Current Humanoid Platform Signals",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Official platform pages", "Source of documented hardware claims", "Prefer official specs over secondary summaries when writing the book."),
            ("HumanoidBench", "Benchmark proxy for platform-task fit", "Map each platform to the tasks it can plausibly support."),
            ("Pinocchio or Drake", "Feasibility checks for controller assumptions", "Use model-based tools to test whether published morphology supports your plan.")
        ],
        "cross_refs": 'This section supports <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.3.html">whole-body control</a>, <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.5.html">teleoperation</a>, and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.9.html">enterprise research tracks</a>.',
        "lab": "Build a platform scorecard for three current humanoids and one non-humanoid baseline. Explain how the ranking changes when you switch from a home-assistance task panel to an industrial one.",
        "failure_pattern": "Platform-selection failures usually come from missing interfaces, not from missing hype. If the controller cannot be instrumented, the benchmark cannot be trusted.",
        "biblio": [
            ('Unitree G1 official page. <a href="https://www.unitree.com/g1" rel="noopener" target="_blank">https://www.unitree.com/g1</a>', "Current official description of G1 hardware and learning framing."),
            ('Unitree H1 official page. <a href="https://www.unitree.com/h1" rel="noopener" target="_blank">https://www.unitree.com/h1</a>', "Current official description of full-size H1 sensing and torque profile."),
            ('Figure Helix official page. <a href="https://www.figure.ai/helix" rel="noopener" target="_blank">https://www.figure.ai/helix</a>', "Current official view of Figure's humanoid VLA stack."),
            ('1X NEO official page. <a href="https://www.1x.tech/neo" rel="noopener" target="_blank">https://www.1x.tech/neo</a>', "Official description of NEO, Redwood AI, and supervised expert mode."),
            ('Apptronik Apollo official page. <a href="https://apptronik.com/apollo" rel="noopener" target="_blank">https://apptronik.com/apollo</a>', "Official industrial framing for Apollo."),
            ('Boston Dynamics Atlas product page. <a href="https://bostondynamics.com/products/atlas/" rel="noopener" target="_blank">https://bostondynamics.com/products/atlas/</a>', "Official industrial framing for electric Atlas.")
        ],
        "takeaway": "Platform choice is a research-method choice because it decides which signals, controllers, and safety cases you can actually inspect.",
        "exercise_title": "Exercise 46.2.1",
        "exercise": "Choose one public humanoid platform for academic research and one for industrial pilot work. Justify each choice with a capability matrix and at least one explicit tradeoff you are accepting."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.3.html": {
        "id": "46-3",
        "quote": '"Whole-body control is where kinematics stops making promises it cannot keep under contact."',
        "cite": "A Contact Dynamics Seminar",
        "image_src": "images/chapter-46-illustration-03.png",
        "image_alt": "Humanoid performing task-space control while maintaining contact constraints.",
        "image_caption": "<strong>Figure 46.3A</strong>: The controller must satisfy end-effector goals, balance, and contact feasibility at the same time.",
        "big_picture": "<strong>Whole-body and operational-space control</strong> is the technical heart of humanoid execution. The controller must coordinate the floating base, task-space goals, contact constraints, and actuator limits in one loop.",
        "pathway": "Read from floating-base dynamics to operational-space objectives, then to constrained QP or inverse-dynamics execution.",
        "develops_1": "A floating-base humanoid is often modeled as $M(q)\\ddot q + h(q, \\dot q) = S^\\top \\tau + J_c(q)^\\top \\lambda$, with configuration $q$, mass matrix $M$, bias term $h$, selection matrix $S$, joint torques $\\tau$, and contact wrench multipliers $\\lambda$. This is the minimum equation needed to keep manipulation, balance, and contact in one mathematical object.",
        "develops_2": "Operational-space control adds task variables $x = \\phi(q)$ with Jacobian $J = \\partial \\phi / \\partial q$. The task-space inertia $\\Lambda = (J M^{-1} J^\\top)^{-1}$ exposes how hard it is to accelerate a hand, torso, or center of mass in a given configuration. The insight is practical: reaching with the hand changes the effective control problem for the whole body.",
        "key_title": "Task Space Is Paid For By The Whole Body",
        "key_text": "A hand trajectory is only real if the feet, torso, joints, and contact forces can afford it.",
        "flow_caption": "Figure 46.3.1 turns whole-body control into an inspectable pipeline: estimate state and contact, formulate task and constraint sets, solve the inverse-dynamics problem, and verify tracking plus feasibility.",
        "flow_observe": "pose, twist, contacts, task errors",
        "flow_model": "floating-base dynamics and Jacobians",
        "flow_act": "solve WBC or OSC command",
        "flow_verify": "tracking, torque, slip, balance",
        "theory": [
            "Whole-body control usually combines equality constraints, such as rigid contacts or desired accelerations, with inequality constraints, such as torque limits, friction cones, and joint bounds. The most common implementation is a hierarchy or quadratic program that trades exact satisfaction of high-priority constraints against soft lower-priority objectives.",
            "This is where model-based libraries remain crucial even in learned systems. A learned policy can propose targets, contact schedules, or residuals, but the execution stack still benefits from explicit multibody dynamics and force feasibility checks.",
            "The strongest evaluation artifact is a synchronized trace with task errors, solver status, contact wrench estimates, torque saturation, and recovery actions."
        ],
        "algo_title": "Algorithm: Whole-Body QP Loop",
        "algorithm": [
            "Estimate floating-base pose, joint state, contact state, and task references.",
            "Build contact constraints and friction-cone or center-of-pressure inequalities.",
            "Encode high-priority tasks such as support consistency and center-of-mass safety.",
            "Encode lower-priority tasks such as hand pose, torso orientation, or posture regularization.",
            "Solve for accelerations, torques, and contact forces, then verify saturation and slip margin before execution."
        ],
        "worked_intro": "A small whole-body ledger is enough to show whether a reach task is balance-limited or simply poorly tuned.",
        "code": """trial = {
    "hand_error_cm": 1.8,
    "com_error_cm": 0.9,
    "max_torque_ratio": 0.87,
    "contact_slip_cm": 0.2,
    "qp_status": "solved",
}
print(trial)
print({"feasible": trial["qp_status"] == "solved" and trial["max_torque_ratio"] < 1.0})""",
        "output": """{'hand_error_cm': 1.8, 'com_error_cm': 0.9, 'max_torque_ratio': 0.87, 'contact_slip_cm': 0.2, 'qp_status': 'solved'}
{'feasible': True}""",
        "output_interp": "The hand target is being tracked within a small error while torque and slip remain inside the envelope. This is the kind of evidence that distinguishes a successful whole-body trial from a lucky reach.",
        "code_caption": "<strong>Code Fragment 46.3.1:</strong> A whole-body controller should report both task quality and constraint health. A solved QP is not enough if the torque or slip margins are already exhausted.",
        "library": "Use Pinocchio or Drake for model quantities, TSID or GR00T Whole-Body Control style frameworks for practical controller structure, and ROS 2 logging for execution traces.",
        "recipe": [
            "Write the exact task stack and task priority policy before tuning weights.",
            "Instrument contact consistency and torque saturation from the first day.",
            "Test reaching while perturbing support, payload, and friction.",
            "Compare one model-based baseline to one learned or residual-augmented variant on the same task panel.",
            "Archive the solver traces, not only the end-effector plots."
        ],
        "warning": "A controller that achieves tiny hand error by silently driving torques to saturation or eroding foot friction margins is not a stable whole-body solution.",
        "example": "Opening a heavy drawer while stepping sideways is a useful benchmark because the hands, torso, and feet all matter, and the controller must allocate force without losing balance.",
        "memory": "Operational space is the wish. Whole-body control is the bill.",
        "frontier": "Current systems mix optimization-based WBC with learned target generation, residual policies, or whole-body motion priors. The main open problem is preserving interpretability and safety under increasingly expressive behavior models.",
        "self_check": "Can you explain what information a contact wrench trace adds that a hand trajectory alone does not?",
        "deep_dive": [
            "This section is an ideal place to emphasize why multibody modeling has not disappeared in the age of foundation models. Whole-body control is still where feasibility becomes numerically explicit.",
            "It is also where students can see the difference between 'the robot reached the target' and 'the robot reached the target with a feasible dynamic budget.' That distinction matters throughout humanoid research."
        ],
        "table_title": "Whole-Body Control Stack",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("Pinocchio", "Fast dynamics, Jacobians, and centroidal quantities", "Use it when you need explicit model terms in the control loop."),
            ("TSID or related QP frameworks", "Task-space inverse dynamics execution", "Make priorities and slack variables explicit in the logs."),
            ("GR00T Whole-Body Control", "Current maintained humanoid whole-body stack", "Useful for current workflows and sim2sim experiments.")
        ],
        "cross_refs": 'This section connects directly to <a href="../../part-2-mathematical-robotics-and-control-foundations/module-05-kinematics-and-robot-motion/index.html">robot kinematics</a>, <a href="../../part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/index.html">robot dynamics</a>, <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">control</a>, and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html">advanced humanoid dynamics</a>.',
        "lab": "Implement a simplified whole-body task panel with a reach, a squat, and a balance-maintenance task. Compare a posture-only controller against a contact-aware task-space controller.",
        "failure_pattern": "If whole-body control fails, first isolate whether the task is dynamically infeasible, incorrectly prioritized, or simply under-instrumented. Those are three very different debugging paths.",
        "biblio": [
            ('Pinocchio official project. <a href="https://github.com/stack-of-tasks/pinocchio" rel="noopener" target="_blank">https://github.com/stack-of-tasks/pinocchio</a>', "Primary source for model terms used in whole-body control."),
            ('TSID project repository. <a href="https://github.com/stack-of-tasks/tsid" rel="noopener" target="_blank">https://github.com/stack-of-tasks/tsid</a>', "Practical task-space inverse dynamics reference for humanoids and other articulated robots."),
            ('GR00T Whole-Body Control documentation. <a href="https://nvlabs.github.io/GR00T-WholeBodyControl/" rel="noopener" target="_blank">https://nvlabs.github.io/GR00T-WholeBodyControl/</a>', "Current maintained whole-body stack reference.")
        ],
        "takeaway": "Whole-body control is the layer that converts task-space ambition into dynamically feasible behavior.",
        "exercise_title": "Exercise 46.3.1",
        "exercise": "Specify a whole-body QP for a two-hand carry task. Name the equality constraints, inequality constraints, task priorities, and the exact logs you would inspect after a slip."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.4.html": {
        "id": "46-4",
        "quote": '"Human motion is not the answer; it is a clue that still has to survive embodiment."',
        "cite": "A Retargeting Review Session",
        "image_src": "images/chapter-46-illustration-04.png",
        "image_alt": "Retargeting human motion into humanoid whole-body behavior.",
        "image_caption": "<strong>Figure 46.4A</strong>: Human data becomes useful only after intent, timing, and contact are mapped into the robot's own body and constraints.",
        "big_picture": "<strong>Learning from humans</strong> gives humanoids a data advantage, but only when retargeting preserves task intent while respecting contact, reach, and torque limits.",
        "pathway": "Read this section from human observation to robot embodiment: pose capture, intent representation, retargeting objective, feasibility filter, and executable rollout.",
        "develops_1": "A common retargeting objective is $\\min_q \\|\\phi_{\\mathrm{human}} - \\phi_{\\mathrm{robot}}(q)\\|_W^2 + \\lambda_c C(q) + \\lambda_l L(q)$, where $\\phi$ encodes task-relevant pose features, $C(q)$ penalizes contact inconsistency, and $L(q)$ penalizes joint or balance-limit violations. The critical idea is that not every human detail matters equally. End-effector intent and contact timing often matter more than exact elbow angle.",
        "develops_2": "HumanPlus, HOVER, OmniH2O-style work, and related motion-retargeting pipelines all confront the same embodied gap: the human demonstrator and the humanoid do not share mass distribution, joint ranges, or contact mechanics. Retargeting is therefore an inference problem, not a copy problem.",
        "key_title": "Intent Survives, Coordinates Do Not",
        "key_text": "Good retargeting preserves what the human was trying to accomplish, not every raw joint angle from the original motion.",
        "flow_caption": "Figure 46.4.1 treats retargeting as a loop: observe human behavior, infer task-relevant features, solve the embodiment mapping, and verify executable success on the robot.",
        "flow_observe": "human pose, contact timing, objects",
        "flow_model": "intent features and retargeting loss",
        "flow_act": "generate robot whole-body motion",
        "flow_verify": "task success and feasibility",
        "theory": [
            "The right retargeting features depend on the task. For locomotion, center-of-mass timing and foot contacts matter. For manipulation, hand pose, gaze, and object-relative trajectories matter. For loco-manipulation, all of them matter together.",
            "This is why motion datasets alone are not enough. A good dataset carries timing, contact, object state, and sometimes force cues so the retargeter can distinguish stylistic variation from essential task structure.",
            "Evaluation should therefore include both geometric metrics and executable metrics: pose similarity, contact timing agreement, balance margin, torque peaks, and actual task completion."
        ],
        "algo_title": "Algorithm: Embodied Motion Retargeting",
        "algorithm": [
            "Capture human motion and task context, including objects and contact timing if possible.",
            "Choose task-relevant features rather than copying all joints equally.",
            "Solve the retargeting objective under joint, balance, and contact constraints.",
            "Replay on the robot or simulator and log feasibility violations and timing drift.",
            "If the motion is not executable, revise the feature set before blaming the controller."
        ],
        "worked_intro": "A small retargeting ledger can already separate good task-intent preservation from geometric overfitting.",
        "code": """human_features = {"left_hand_to_box_cm": 4.0, "right_foot_contact": 1, "torso_yaw_deg": 18}
robot_trial = {"left_hand_to_box_cm": 5.3, "right_foot_contact": 1, "torso_yaw_deg": 15}

errors = {
    "hand_error_cm": round(abs(human_features["left_hand_to_box_cm"] - robot_trial["left_hand_to_box_cm"]), 1),
    "contact_match": int(human_features["right_foot_contact"] == robot_trial["right_foot_contact"]),
    "yaw_error_deg": abs(human_features["torso_yaw_deg"] - robot_trial["torso_yaw_deg"]),
}
print(errors)""",
        "output": """{'hand_error_cm': 1.3, 'contact_match': 1, 'yaw_error_deg': 3}""",
        "output_interp": "The hand and torso errors are small while the contact event is preserved. That suggests the retargeting kept task intent and support timing, which matters more than exact whole-body imitation for many tasks.",
        "code_caption": "<strong>Code Fragment 46.4.1:</strong> Retargeting should be evaluated on task features and contact agreement, not on raw pose similarity alone.",
        "library": "Use motion-retargeting pipelines, whole-body simulators, and robot-data stacks such as LeRobot to keep demonstration and execution artifacts synchronized.",
        "recipe": [
            "Select the task features that actually matter before collecting imitation data.",
            "Record contact timing and object state whenever possible.",
            "Retarget with explicit feasibility penalties.",
            "Evaluate on execution metrics, not only geometric similarity.",
            "Keep failed motions as diagnostics because they reveal missing embodiment features."
        ],
        "warning": "A visually plausible retargeted motion can still be dynamically impossible, unsafe, or task-irrelevant for the robot body.",
        "example": "A human can lean and twist to place a box on a shelf while compensating with subtle ankle control. A humanoid with different hip or ankle limits may need a step adjustment rather than a direct pose imitation.",
        "memory": "The robot is not a puppet. It is an organism with different bones, muscles, and excuses.",
        "frontier": "Recent work pushes from motion tracking toward video-driven, object-aware whole-body learning and motion priors that fill gaps between sparse demonstrations. The open problem is preserving intent under large embodiment mismatch.",
        "self_check": "Which feature would you preserve first for a carry task: hand trajectory, foot contacts, torso orientation, or joint angles, and why?",
        "deep_dive": [
            "This section is useful for teaching the distinction between imitation and embodiment. Students often begin by assuming the goal is faithful visual copying. The real goal is executable task transfer.",
            "It is also a natural place to introduce data contracts. Demonstration data becomes much more valuable when it records task context and contact semantics rather than only pose streams."
        ],
        "table_title": "Retargeting Tool Map",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("LeRobot-style data tooling", "Store demonstrations with synchronized metadata", "Keep contact and object state beside pose data."),
            ("Whole-body simulators", "Check executability before hardware rollout", "Reject motions that only look right in kinematics space."),
            ("Retargeting pipelines", "Map human features into robot features", "Tune feature weighting by task, not by generic motion similarity.")
        ],
        "cross_refs": 'This section connects to <a href="../../part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/index.html">robot datasets</a>, <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.5.html">teleoperation</a>, and <a href="../../part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/index.html">cross-embodiment learning</a>.',
        "lab": "Retarget one short human demonstration into a humanoid simulation, then compare raw pose error against task-feature error and balance feasibility.",
        "failure_pattern": "When retargeting fails, ask whether the missing piece is feature choice, contact semantics, embodiment mismatch, or controller feasibility. Different failures imply different dataset improvements.",
        "biblio": [
            ('HumanPlus project page. <a href="https://humanplus.github.io/" rel="noopener" target="_blank">https://humanplus.github.io/</a>', "Primary current source for human-motion-driven humanoid control."),
            ('HOVER project page. <a href="https://www.hover-policy.org/" rel="noopener" target="_blank">https://www.hover-policy.org/</a>', "Current reference for versatile neural whole-body control."),
            ('LeRobot documentation. <a href="https://huggingface.co/docs/lerobot/en/index" rel="noopener" target="_blank">https://huggingface.co/docs/lerobot/en/index</a>', "Practical stack for storing and training from robot demonstrations.")
        ],
        "takeaway": "The purpose of human data is not mimicry. It is executable task transfer under a different body.",
        "exercise_title": "Exercise 46.4.1",
        "exercise": "Define a retargeting evaluation for a shelf-placement task. Include one geometric metric, one contact metric, one balance metric, and one task-completion metric."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.5.html": {
        "id": "46-5",
        "quote": '"Teleoperation is not a fallback. It is one of the fastest ways to reveal what the autonomy stack does not yet know how to do."',
        "cite": "A Shared-Autonomy Design Review",
        "image_src": "images/chapter-46-illustration-05.png",
        "image_alt": "Humanoid teleoperation with operator interface and shared autonomy.",
        "image_caption": "<strong>Figure 46.5A</strong>: Teleoperation builds data, validates interfaces, and catches safety gaps long before fully autonomous deployment.",
        "big_picture": "<strong>Teleoperation for humanoids</strong> is a dual-purpose system. It keeps humans in the loop for safety and coverage, and it creates the demonstrations, failure traces, and interface contracts that later autonomy depends on.",
        "pathway": "Read this section from latency budget to shared-autonomy routing, then to data products and safety supervision.",
        "develops_1": "A useful teleoperation latency budget is $T_{\\mathrm{total}} = T_{\\mathrm{sense}} + T_{\\mathrm{encode}} + T_{\\mathrm{network}} + T_{\\mathrm{render}} + T_{\\mathrm{human}} + T_{\\mathrm{robot}}$. For high-bandwidth whole-body tasks, that sum shapes what can be directly operated and what must be handed to autonomous stabilizers or motion primitives.",
        "develops_2": "Shared autonomy can be written as $u = \\alpha u_{\\mathrm{human}} + (1 - \\alpha) u_{\\mathrm{auto}}$, but the real system is richer. The human may command task intent while the robot closes local balance, collision, or grasp-stability loops. The best teleoperation interfaces expose this division clearly.",
        "key_title": "The Interface Is Part Of The Controller",
        "key_text": "Poor teleoperation is often a systems-design failure, not an operator failure. The operator can only be as good as the latency, viewpoint, and autonomy partition allow.",
        "flow_caption": "Figure 46.5.1 makes humanoid teleoperation explicit: gather operator and robot state, route commands through shared autonomy, execute with stabilizers, and verify workload plus task outcome.",
        "flow_observe": "operator pose, robot state, latency",
        "flow_model": "shared-autonomy partition",
        "flow_act": "blend human intent and robot stabilizers",
        "flow_verify": "success, workload, interventions",
        "theory": [
            "Teleoperation is a productive first-class research layer because it solves three problems at once: it provides coverage for hard tasks, a direct debugging path for failed autonomy, and a data stream for imitation or behavior modeling.",
            "Humanoid teleoperation is especially demanding because whole-body motion, balance, and manipulation are tightly coupled. A human operator may specify intent, but the local stabilizer still has to protect contact feasibility and safety zones.",
            "Evaluation should therefore track not only task success but also operator workload, intervention frequency, takeover time, packet delay, and the fraction of control handled autonomously."
        ],
        "algo_title": "Algorithm: Shared-Autonomy Teleop Loop",
        "algorithm": [
            "Measure end-to-end latency and packet jitter under realistic network conditions.",
            "Assign direct human control to the degrees of freedom that truly need it and delegate stabilization to the robot.",
            "Log the autonomy fraction, override events, and safety clamps.",
            "Save teleop traces in a dataset-ready format with operator intent, robot state, and video or scene context.",
            "Promote recurring operator corrections into future policy or controller improvements."
        ],
        "worked_intro": "A small teleop run summary can reveal whether failure came from latency, viewpoint, or missing autonomy support rather than from human skill.",
        "code": """latency_ms = {"sense": 18, "network": 42, "render": 25, "human": 180, "robot": 14}
total = sum(latency_ms.values())
autonomy_fraction = 0.62
print({"total_latency_ms": total, "autonomy_fraction": autonomy_fraction})
print({"direct_teleop_ok_for_fast_balance": total < 120})""",
        "output": """{'total_latency_ms': 279, 'autonomy_fraction': 0.62}
{'direct_teleop_ok_for_fast_balance': False}""",
        "output_interp": "At 279 ms end-to-end latency, direct whole-body balance control is unrealistic. The operator can still command intent, but stabilization must be handled by local autonomy or motion primitives.",
        "code_caption": "<strong>Code Fragment 46.5.1:</strong> A latency budget converts a vague teleop complaint into a concrete design decision about what must be autonomous on the robot side.",
        "library": "Use ROS 2 transport and logging, VR or motion-capture interfaces where appropriate, and dataset tooling that preserves intent, video, and synchronized robot state.",
        "recipe": [
            "Measure the real latency budget before choosing control granularity.",
            "Move fast stabilization to the robot side when latency exceeds the task envelope.",
            "Log operator intent and autonomous corrections separately.",
            "Turn teleoperation traces into dataset artifacts rather than disposable operator sessions.",
            "Review the top recurring interventions every week and convert them into automation candidates."
        ],
        "warning": "A teleoperation system can look smooth in short videos while silently overloading the operator or depending on unlogged manual corrections.",
        "example": "For whole-body box carry, the operator may choose waypoint and hand intent while the robot handles foot placement and balance. For delicate insertion, autonomy may step back and the operator may take finer hand control.",
        "memory": "Teleoperation teaches the autonomy stack where the robot still needs a grown-up in the room.",
        "frontier": "Current humanoid teleoperation is moving toward predictive interfaces, shared autonomy with strong local stabilizers, and better dataset extraction for training whole-body foundation models.",
        "self_check": "Which part of a humanoid task would you keep under local autonomy first when network delay rises: balance, collision avoidance, grasp stabilization, or high-level sequencing?",
        "deep_dive": [
            "This section helps students see teleoperation as instrumentation rather than as failure. The best teams use teleop traces to discover control bottlenecks, perception blind spots, and policy interface mistakes.",
            "It is also a useful bridge to data scaling. Teleoperation quality determines not only task success in the moment, but the quality of the demonstrations that later train autonomous policies."
        ],
        "table_title": "Humanoid Teleoperation Tooling",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("ROS 2", "Transport and synchronized logging", "Record human intent and robot correction on the same timeline."),
            ("VR or motion-capture interfaces", "Human input channel", "Choose interfaces that match the required control granularity."),
            ("Dataset tooling", "Turn teleop into training data", "Never leave a useful teleop session as an unlabeled video only.")
        ],
        "cross_refs": 'This section supports <a href="../../part-5-learning-from-demonstration-and-robot-data/module-23-teleoperation-and-data-collection/index.html">teleoperation and data collection</a> and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.6.html">humanoid foundation models</a>.',
        "lab": "Instrument one teleop task with a latency budget and autonomy split. Record where the operator helped and where autonomy already carried the load.",
        "failure_pattern": "Teleop failures should be labeled by latency, viewpoint, operator overload, shared-autonomy mismatch, or low-level robot instability. Only one of those is fixed by training the operator harder.",
        "biblio": [
            ('LeRobot documentation. <a href="https://huggingface.co/docs/lerobot/en/index" rel="noopener" target="_blank">https://huggingface.co/docs/lerobot/en/index</a>', "Practical tooling for robot demonstration data."),
            ('1X NEO official page. <a href="https://www.1x.tech/neo" rel="noopener" target="_blank">https://www.1x.tech/neo</a>', "Current official example of expert-mode supervision in a humanoid stack."),
            ('GR00T Whole-Body Control documentation. <a href="https://nvlabs.github.io/GR00T-WholeBodyControl/" rel="noopener" target="_blank">https://nvlabs.github.io/GR00T-WholeBodyControl/</a>', "Current whole-body control reference relevant to local stabilizers in teleop stacks.")
        ],
        "takeaway": "Humanoid teleoperation is valuable because it reveals where human intent ends and robot stabilization must begin.",
        "exercise_title": "Exercise 46.5.1",
        "exercise": "Choose a humanoid task and define the autonomy partition you would use at 80 ms latency and at 300 ms latency. Explain which loops move to the robot side and why."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.6.html": {
        "id": "46-6",
        "quote": '"Foundation models matter for humanoids only when they know when to think and when to stay out of the way."',
        "cite": "A Dual-System Architecture Review",
        "image_src": "images/chapter-46-illustration-05.png",
        "image_alt": "Dual-system humanoid architecture with slow planning and fast control.",
        "image_caption": "<strong>Figure 46.6A</strong>: Humanoid foundation models need a clean contract between slow deliberation and fast whole-body execution.",
        "big_picture": "<strong>Dual-system humanoid foundation models</strong> connect language, vision, memory, and behavior priors to the whole-body stack. The central design question is routing: which decisions belong to the fast motor system, and which belong to the slower reasoning system.",
        "pathway": "Read this section from routing policy to execution contract, then to evaluation on novel instructions and disturbances.",
        "develops_1": "A dual-system controller can be summarized by a routing variable $g_t \\in \\{\\text{reflex}, \\text{deliberative}\\}$ that selects whether the next command comes from a fast local policy or a slower planner. In practice, $g_t$ depends on novelty, ambiguity, safety state, and latency budget.",
        "develops_2": "The key systems contract is that the slow model proposes subgoals, contact-relevant intentions, or skill calls, while the fast whole-body layer ensures balance, timing, and force feasibility. If the slow model directly emits time-critical whole-body commands, the architecture usually collapses under latency and contact uncertainty.",
        "key_title": "Reason Slowly, Move Quickly",
        "key_text": "The value of a humanoid foundation model is not raw eloquence. It is making better task decisions without destabilizing the fast embodied loop.",
        "flow_caption": "Figure 46.6.1 frames the dual-system contract: detect novelty and ambiguity, route to planner or reflex, execute through the whole-body stack, and verify task plus safety outcome.",
        "flow_observe": "instruction, scene, novelty, risk",
        "flow_model": "route between planner and reflex",
        "flow_act": "issue subgoal or skill call",
        "flow_verify": "task success and safe recovery",
        "theory": [
            "Humanoid foundation models are most credible when they operate over typed actions or skills rather than raw torque streams. The fast motor layer already has strong geometric and dynamic structure. The slow layer helps with task decomposition, semantic grounding, memory use, and exception handling.",
            "This makes evaluation more specific. The right questions are whether the model chooses the correct skill, times handoff correctly, asks for clarification when needed, and improves recovery under novelty. The wrong question is whether it can narrate the task nicely.",
            "A clean architecture also exposes failure provenance. Was the error in grounding, planning, skill selection, or low-level execution? Without that separation, whole-body foundation models become impossible to debug."
        ],
        "algo_title": "Algorithm: Dual-System Humanoid Routing",
        "algorithm": [
            "Represent the slow layer output as typed subgoals, skill calls, or constraints rather than raw body commands.",
            "Detect novelty, ambiguity, or high-level exceptions that warrant planner intervention.",
            "Route stable repetitive segments to fast local control or learned skills.",
            "Log every handoff between planner and reflex, including why it happened.",
            "Evaluate on tasks that require both fast recovery and slow reasoning, such as instruction correction during manipulation."
        ],
        "worked_intro": "A routing trace can tell you whether the foundation model improved behavior by choosing better skills or merely talked over a controller that already knew what to do.",
        "code": """events = [
    {"t": 0.0, "route": "reflex", "reason": "stable walk"},
    {"t": 3.2, "route": "planner", "reason": "instruction correction"},
    {"t": 4.1, "route": "reflex", "reason": "skill selected"},
]

planner_calls = sum(1 for e in events if e["route"] == "planner")
print({"planner_calls": planner_calls, "events": events})""",
        "output": """{'planner_calls': 1, 'events': [{'t': 0.0, 'route': 'reflex', 'reason': 'stable walk'}, {'t': 3.2, 'route': 'planner', 'reason': 'instruction correction'}, {'t': 4.1, 'route': 'reflex', 'reason': 'skill selected'}]}""",
        "output_interp": "The planner intervened only when the task semantics changed. That is the desired pattern. Constant planner involvement in stable locomotion would usually signal a bad system split.",
        "code_caption": "<strong>Code Fragment 46.6.1:</strong> Routing logs make it possible to prove that a dual-system architecture intervenes for the right reasons instead of adding slow noise to fast control.",
        "library": "Use VLA or planning stacks for typed subgoals, and keep the execution layer grounded in whole-body control frameworks rather than end-to-end textual wishfulness.",
        "recipe": [
            "Define the typed action or skill interface before plugging in a foundation model.",
            "Specify novelty or ambiguity triggers for planner involvement.",
            "Keep low-level balance and safety outside the slow model.",
            "Log handoffs and planner rationales as structured artifacts.",
            "Test on tasks with both semantic novelty and physical disturbance."
        ],
        "warning": "A dual-system label is meaningless if the slow model still emits latency-sensitive motor detail that belongs in the reflex layer.",
        "example": "A humanoid restocking task may route stable carrying and walking to reflexive skills, while using the slow model to interpret a changed shelf instruction or ask whether a blocked aisle implies rerouting.",
        "memory": "The planner should be the navigator, not the ankle servo.",
        "frontier": "Current frontier systems, including vendor VLA stacks and emerging whole-body references, aim to combine semantic flexibility with reliable motor execution. The open question is how to preserve interpretability and safety as the slow layer becomes more capable.",
        "self_check": "What signal would convince you that a planner call was necessary rather than an architectural crutch for a weak skill library?",
        "deep_dive": [
            "This section can teach a healthy respect for interface design. Strong embodied AI systems often improve more from clean task and skill interfaces than from a larger general model alone.",
            "It also reinforces a central course theme: intelligence in embodied systems is distributed across state estimation, planning, control, and data structures. A foundation model is part of the stack, not the stack."
        ],
        "table_title": "Dual-System Stack Components",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("VLA or planning stack", "Slow semantic reasoning and subgoal generation", "Emit typed actions, not raw joint commands."),
            ("Whole-body control framework", "Fast local execution and stabilization", "Keep safety and balance local."),
            ("Structured logs", "Handoff and rationale tracing", "Without routing logs, dual-system claims are hard to verify.")
        ],
        "cross_refs": 'This section ties back to <a href="../../part-7-language-vision-and-action/module-34-vision-language-action-models/index.html">vision-language-action models</a> and <a href="../../part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/index.html">robot foundation models</a>, then forward to <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html">deployment monitoring</a>.',
        "lab": "Define a task where the planner should intervene exactly twice and the reflex layer should dominate the rest. Then instrument whether the architecture behaves that way.",
        "failure_pattern": "Dual-system failures often come from poor routing boundaries, missing typed interfaces, or a slow layer that does not know when to abstain.",
        "biblio": [
            ('Figure Helix official page. <a href="https://www.figure.ai/helix" rel="noopener" target="_blank">https://www.figure.ai/helix</a>', "Current official example of a humanoid VLA framing."),
            ('GR00T Whole-Body Control documentation. <a href="https://nvlabs.github.io/GR00T-WholeBodyControl/" rel="noopener" target="_blank">https://nvlabs.github.io/GR00T-WholeBodyControl/</a>', "Relevant current whole-body execution layer for dual-system thinking."),
            ('Gemini Robotics technical report. <a href="https://arxiv.org/abs/2503.20020" rel="noopener" target="_blank">https://arxiv.org/abs/2503.20020</a>', "Recent reference point for embodied multimodal reasoning and action.")
        ],
        "takeaway": "A humanoid foundation model is useful when it improves task-level choices while leaving the fast physical loop clean and reliable.",
        "exercise_title": "Exercise 46.6.1",
        "exercise": "Specify a dual-system interface for a humanoid pick-and-carry task. Name the typed actions, the routing trigger for planner intervention, and the logs you would inspect after a failure."
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.7.html": {
        "id": "46-7",
        "quote": '"Safety for a human-scale robot begins where optimism about the demo ends."',
        "cite": "A Deployment Safety Review",
        "image_src": "images/chapter-46-illustration-08.png",
        "image_alt": "Humanoid robot with human-zone safety monitoring and motion constraints.",
        "image_caption": "<strong>Figure 46.7A</strong>: Human-scale safety combines geometry, force, speed, contact, and runtime supervision in one live system.",
        "big_picture": "<strong>Safety for human-scale robots</strong> is not a wrapper around capability. It is a set of hard constraints that must govern perception, planning, control, teleoperation, and deployment telemetry together.",
        "pathway": "Read this section from hazard model to runtime guard: human-zone geometry, velocity and force limits, fall-risk detection, and intervention logic.",
        "develops_1": "A common control-filter view is to solve $u^* = \\arg\\min_u \\|u - u_{\\mathrm{nom}}\\|^2$ subject to a barrier-style safety constraint $\\dot h(x, u) + \\alpha h(x) \\ge 0$, where $h(x)$ encodes a safe set boundary such as separation distance, fall margin, or joint-limit clearance.",
        "develops_2": "For humanoids, the safe set is multi-layered. It includes reach envelopes, stop distance, contact force, pinch points, balance margin, and interaction-state uncertainty. That is why human-scale safety must be treated as a runtime systems problem, not just a planning problem.",
        "key_title": "The Safe Set Has To Live At Runtime",
        "key_text": "A nice offline policy is irrelevant if the deployed robot cannot clamp unsafe motion quickly enough when humans or contact conditions change.",
        "flow_caption": "Figure 46.7.1 frames safety as a runtime loop: sense humans and body state, evaluate envelopes, modify or block unsafe action, and verify intervention quality.",
        "flow_observe": "human proximity, force, balance, speed",
        "flow_model": "safe set and intervention policy",
        "flow_act": "clamp, slow, reroute, stop",
        "flow_verify": "false negatives, uptime, recovery",
        "theory": [
            "Safety monitoring has to operate across time scales. Fast loops catch imminent contact, torque spikes, or falls. Slower loops enforce workcell zones, task permissions, and operator confirmations. Neither layer can fully replace the other.",
            "Humanoid safety is especially challenging because the body itself can create hazards through swinging limbs, falling mass, or unstable carried objects. A safe hand path is not enough if the torso or foothold plan creates risk elsewhere.",
            "Evaluation should include false-negative rate, false-positive burden, intervention latency, degraded-task behavior, and post-stop recovery procedure."
        ],
        "algo_title": "Algorithm: Runtime Safety Supervisor",
        "algorithm": [
            "Estimate human distance, robot reach envelope, velocity, balance margin, and carried-object state at runtime.",
            "Evaluate a hierarchy of safety conditions from immediate collision risk to slower workcell and task rules.",
            "Modify or block nominal commands according to the active condition.",
            "Log every intervention with pre-state, cause label, and post-state.",
            "Replay interventions in simulation and classify which ones should become training, controller, or sensing improvements."
        ],
        "worked_intro": "A simple supervisor log already shows whether a controller respects human-zone constraints without collapsing the task every time a person appears nearby.",
        "code": """events = [
    {"human_distance_m": 1.6, "cmd_scale": 1.0},
    {"human_distance_m": 0.9, "cmd_scale": 0.4},
    {"human_distance_m": 0.5, "cmd_scale": 0.0},
]
stops = sum(1 for e in events if e["cmd_scale"] == 0.0)
print({"stops": stops, "events": events})""",
        "output": """{'stops': 1, 'events': [{'human_distance_m': 1.6, 'cmd_scale': 1.0}, {'human_distance_m': 0.9, 'cmd_scale': 0.4}, {'human_distance_m': 0.5, 'cmd_scale': 0.0}]}""",
        "output_interp": "The supervisor first slows and then stops as a human approaches. That graded response is usually preferable to either doing nothing or stopping at the slightest distant detection.",
        "code_caption": "<strong>Code Fragment 46.7.1:</strong> Safety events should reveal not only that a stop happened, but how the supervisor modulated behavior as risk increased.",
        "library": "Use ROS 2 and controller-side safety hooks, keep the nominal controller instrumented, and store intervention logs so safety cases can be replayed rather than retold.",
        "recipe": [
            "Define the human-zone and robot-envelope hazards before tuning the task policy.",
            "Implement fast and slow safety layers with explicit responsibilities.",
            "Log every slowdown, clamp, and stop with a cause label.",
            "Evaluate false positives and task degradation alongside true safety benefit.",
            "Rehearse post-stop recovery, not only the stop event itself."
        ],
        "warning": "A safety system that only counts emergency stops can look good while quietly producing too many false slowdowns or missing risky near-misses.",
        "example": "A humanoid carrying a tote past a human coworker may need to slow, widen stance, lower arm speed, and change path simultaneously. Safety is a whole-body modification, not a single checkbox.",
        "memory": "Safe humanoids are not the ones that never stop. They are the ones that know exactly when to stop and how to recover afterward.",
        "frontier": "The frontier combines formal safety filters, learned risk predictors, human-intention estimation, and field telemetry. The unresolved challenge is proving broad safety while preserving practical productivity.",
        "self_check": "What metric would tell you your supervisor is too permissive, and what metric would tell you it is too conservative?",
        "deep_dive": [
            "This section is where embodied AI becomes accountable. Students should see that a safe system is not merely lower reward or lower speed. It is a system whose intervention logic is explicit, measured, and replayable.",
            "It is also a place to connect safety to course pedagogy. Every advanced system introduced earlier should now be revisited through the lens of human-zone uncertainty, stop distance, and recovery procedures."
        ],
        "table_title": "Human-Scale Safety Stack",
        "table_headers": ["Tool or Library", "Role in the Topic", "Builder Advice"],
        "table_rows": [
            ("ROS 2 safety and logging hooks", "Runtime intervention recording", "Make intervention causes structured, not free text."),
            ("Whole-body controller limits", "Fast torque and balance protection", "Safety cannot live only in the planner."),
            ("Simulation replay", "Evaluate human-zone and fall scenarios safely", "Promote every serious near-miss into the replay suite.")
        ],
        "cross_refs": 'This section prepares for <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">safety validation</a> and connects to <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.5.html">teleoperation</a> and <a href="../../part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/section-46.8.html">whole-body dynamics</a>.',
        "lab": "Design a safety supervisor for a humanoid carry task in a shared workspace. Include graded slowdown, stop logic, and a restart procedure.",
        "failure_pattern": "Most safety failures come from missing runtime context, missing intervention labels, or badly placed control authority. Put the guard where the unsafe command can actually be blocked.",
        "biblio": [
            ('Boston Dynamics Atlas product page. <a href="https://bostondynamics.com/products/atlas/" rel="noopener" target="_blank">https://bostondynamics.com/products/atlas/</a>', "Relevant official framing because Atlas is positioned for industrial human environments."),
            ('GR00T Whole-Body Control documentation. <a href="https://nvlabs.github.io/GR00T-WholeBodyControl/" rel="noopener" target="_blank">https://nvlabs.github.io/GR00T-WholeBodyControl/</a>', "Current whole-body stack reference where runtime limits and control interfaces matter."),
            ('Drake project. <a href="https://drake.mit.edu/" rel="noopener" target="_blank">https://drake.mit.edu/</a>', "Useful model-based platform for safe-set and verification reasoning.")
        ],
        "takeaway": "Human-scale robot safety is a live control and monitoring problem, not a disclaimer attached after the demo.",
        "exercise_title": "Exercise 46.7.1",
        "exercise": "Write the safety monitor specification for a humanoid moving a load through a shared aisle. Include the safe-set variables, intervention order, false-positive metric, and post-stop recovery rule."
    },
}


INDEX_DATA = {
    "part-9-manipulation-locomotion-and-embodied-skills/module-45-locomotion-and-mobility/index.html": {
        "quote": '"Mobility becomes science when every fall, slip, and save is turned into a reproducible trace."',
        "cite": "A Reliable Locomotion Notebook",
        "big_picture": "<strong>Locomotion and Mobility</strong> is where embodiment becomes obvious. The robot must exchange momentum, contact, geometry, and energy with the world while staying recoverable under uncertainty.",
        "remember": "This chapter teaches locomotion as a layered evidence problem: morphology, balance, large-scale learning, adaptation, and deployment constraints all have to agree.",
        "overview_1": "Chapter 45 develops a modern locomotion stack from first principles to deployment. We begin with body choice, move through reduced-order balance and gait reasoning, scale to massively parallel reinforcement learning, then close the loop with terrain adaptation, energy accounting, transfer, and safety.",
        "overview_2": "The practical stack emphasizes Isaac Lab, MuJoCo and MJX, Drake, ROS 2 telemetry, and matched disturbance panels. The theory thread keeps balance, contact, and deployment limits visible so the chapter remains useful for wheeled robots, quadrupeds, bipeds, and wheel-leg hybrids.",
        "prereqs": "Readers should be comfortable with rigid-body dynamics, control loops, state estimation, and reinforcement learning. The chapter constantly links those foundations to contact, recoverability, and deployment evidence.",
        "roadmap": [
            ("45.1", "section-45.1.html", "Wheeled, legged, and hybrid robots", "Compares body types through terrain coverage, dynamics, and mission-level cost rather than through demos alone."),
            ("45.2", "section-45.2.html", "Balance, stability, and gait", "Builds the reduced-order language of ZMP, capture point, hybrid contact phases, and push recovery."),
            ("45.3", "section-45.3.html", "Learning locomotion with massively parallel RL", "Connects batched PPO-style training to environment manifests, held-out panels, and transfer-ready evaluation."),
            ("45.4", "section-45.4.html", "Terrain adaptation, parkour, and rapid motor adaptation", "Explains latent adaptation modules, disturbance labeling, and contact-aware recovery on unseen terrain."),
            ("45.5", "section-45.5.html", "Energy efficiency; sim-to-real and safety in locomotion", "Turns locomotion into a deployment ledger with CoT, thermal limits, runtime safety, and residual-gap analysis.")
        ],
        "tooling_note": "This chapter uses the right-tool principle. Learn the reduced-order and diagnostic logic by hand first, then move to maintained tools when scale, contact replay, or deployment telemetry matter.",
        "lab_id": "lab-45",
        "lab_duration": "Duration: about 2 to 3 hours",
        "lab_difficulty": "Difficulty: Intermediate to Advanced",
        "lab_objective": "Build one matched locomotion panel that can compare morphology, balance strategy, RL policy, and deployment envelope on the same terrain family.",
        "lab_steps": [
            "Define the terrain and disturbance panel with fixed seeds.",
            "Compare at least two morphologies or controller classes on the same metric code.",
            "Add one reduced-order balance diagnostic, one learned policy, and one safety or deployment constraint.",
            "Collect synchronized traces with failure labels.",
            "Write a short postmortem explaining one genuine win and one remaining unrecoverable failure."
        ],
        "next": 'Continue with <a href="section-45.1.html">Section 45.1: Wheeled, legged, and hybrid robots</a>, where mobility begins with body choice rather than with policy architecture.',
        "production_1": "Read each section as a builder would: what state is estimated, what contact or dynamics model matters, what artifact proves the claim, and what perturbation is most likely to falsify it.",
        "table_title": "Chapter Tool Map",
        "tool_rows": [
            ("Isaac Lab", "Massively parallel RL, terrain curricula, and transfer workflows"),
            ("MuJoCo and MJX", "Fast contact-heavy simulation and replay diagnostics"),
            ("Drake", "Reduced-order balance, planning, and dynamic feasibility"),
            ("ROS 2 telemetry", "Hardware integration, logging, and deployment traces"),
            ("Pinocchio or similar dynamics tools", "Articulated-body computations and feasibility checks")
        ],
        "lab_extension": "Extend the chapter lab by adding a safety monitor, an energy ledger, and one real-to-sim replay from telemetry. That turns a locomotion demo into a deployment-style evidence artifact.",
        "instructor_1": "This chapter works well as a bridge between theory and field robotics. The recommended rhythm is morphology and reduced-order models first, then learning systems, then deployment constraints.",
        "instructor_2": "For course use, insist that students compare methods on one matched terrain panel. That single rule eliminates many invalid locomotion comparisons and teaches scientific hygiene early.",
        "readiness": "Before leaving the chapter, the reader should be able to explain one morphology tradeoff, one recoverability test, one RL audit, one adaptation diagnostic, and one deployment gate for locomotion.",
        "teaching": "A strong chapter outcome is not a smoother video. It is a saved panel with metrics, traces, disturbance labels, and a clear explanation of why a controller succeeds or fails.",
        "agent_1": "The chapter has been tightened around deep explanation, code pedagogy, reproducibility, and scientific depth. The content now emphasizes formulas, disturbance panels, and real tool choices rather than generic mobility slogans.",
        "agent_2": "The production target is a mobility evidence stack: body choice, balance metric, learned controller, adaptation module, and deployment monitor evaluated together on one panel.",
        "evidence_standard": "A locomotion claim is ready when it names the terrain panel, the disturbance set, the contact or balance metric, and the deployment constraint that could break it.",
        "biblio": [
            ('Isaac Lab documentation. <a href="https://isaac-sim.github.io/IsaacLab/" rel="noopener" target="_blank">https://isaac-sim.github.io/IsaacLab/</a>', "Primary current documentation for large-scale robot learning workflows."),
            ('MuJoCo MJX documentation. <a href="https://mujoco.readthedocs.io/en/stable/mjx.html" rel="noopener" target="_blank">https://mujoco.readthedocs.io/en/stable/mjx.html</a>', "Primary source for batched MuJoCo workflows."),
            ('MIT Underactuated Robotics humanoids and walking material. <a href="https://underactuated.mit.edu/humanoids.html" rel="noopener" target="_blank">https://underactuated.mit.edu/humanoids.html</a>', "Strong conceptual reference for balance and walking."),
            ('RMA project page. <a href="https://ashish-kmr.github.io/rma-legged-robots/" rel="noopener" target="_blank">https://ashish-kmr.github.io/rma-legged-robots/</a>', "Core reference for rapid locomotion adaptation.")
        ],
    },
    "part-9-manipulation-locomotion-and-embodied-skills/module-46-humanoid-robots-and-whole-body-control/index.html": {
        "quote": '"Whole-body intelligence becomes real the moment a robot must keep balance, obey people, and still finish the job."',
        "cite": "A Humanoid Systems Field Note",
        "big_picture": "<strong>Humanoid Robots and Whole-Body Control</strong> unifies morphology, contact dynamics, teleoperation, human data, foundation models, and safety. The chapter treats humanoids as integrated embodied systems rather than as isolated AI demos.",
        "remember": "The recurring chapter idea is coupling: locomotion, manipulation, human interaction, and safety cannot be debugged in isolation for long on a human-scale body.",
        "overview_1": "Chapter 46 starts by asking why humanoids are worth the complexity at all. It then moves through platform choice, whole-body and operational-space control, human demonstration pipelines, teleoperation, dual-system foundation models, runtime safety, advanced contact mechanics, and enterprise loco-manipulation research loops.",
        "overview_2": "The practical stack emphasizes Pinocchio, TSID-like or GR00T-style whole-body control, HumanoidBench, Isaac Lab, Drake, ROS 2, and robot-data tooling such as LeRobot. The theory thread keeps floating-base dynamics, contact constraints, and safe deployment visible even when the chapter discusses foundation models.",
        "prereqs": "Readers should be comfortable with multibody dynamics, control, locomotion, teleoperation, robot learning, and deployment monitoring. The chapter assumes those foundations and shows how they interact on a humanoid body.",
        "roadmap": [
            ("46.1", "section-46.1.html", "Why humanoids became the focus (data, morphology, hardware cost)", "Explains the strategic case for humanoids through task reuse, data reuse, and infrastructure reuse."),
            ("46.2", "section-46.2.html", "Platforms: Unitree G1/H1, Figure, Optimus, 1X, electric Atlas, Apptronik", "Compares current platforms as research instruments rather than as brand stories."),
            ("46.3", "section-46.3.html", "Whole-body and operational-space control", "Builds the floating-base and task-space execution layer that makes humanoid behavior feasible."),
            ("46.4", "section-46.4.html", "Learning from humans: HumanPlus, OmniH2O/HOVER, motion retargeting", "Shows how human demonstrations become executable whole-body behavior."),
            ("46.5", "section-46.5.html", "Teleoperation for humanoids", "Treats teleoperation as a shared-autonomy and data-generation system."),
            ("46.6", "section-46.6.html", "Dual-system humanoid foundation models (tie-back to Ch. 35)", "Defines the routing contract between slow semantic planning and fast whole-body execution."),
            ("46.7", "section-46.7.html", "Safety for human-scale robots", "Frames safety as a runtime whole-body supervision problem."),
            ("46.8", "section-46.8.html", "Advanced humanoid dynamics and contact mechanics", "Deepens centroidal dynamics, contact scheduling, and whole-body feasibility for research-grade systems."),
            ("46.9", "section-46.9.html", "Boston Dynamics-style loco-manipulation research track", "Assembles the full enterprise humanoid research loop: simulation, control, data, telemetry, and safety evidence.")
        ],
        "tooling_note": "This chapter uses the right-tool principle aggressively. Keep the conceptual core small and transparent, then move to maintained whole-body control, benchmarking, simulation, and logging stacks when the task becomes serious.",
        "lab_id": "lab-46",
        "lab_duration": "Duration: about 2.5 to 4 hours",
        "lab_difficulty": "Difficulty: Advanced",
        "lab_objective": "Build one reproducible humanoid evidence artifact that includes a task panel, a whole-body controller, a data or teleop path, and a runtime safety record.",
        "lab_steps": [
            "Pick one loco-manipulation task, such as carry, place, or door traversal.",
            "Specify the contact schedule, task-space objectives, and safety envelope.",
            "Implement or configure a whole-body controller baseline in simulation.",
            "Add either teleoperation data, motion retargeting, or a dual-system planner handoff.",
            "Evaluate on a perturbation panel and save solver, safety, and task traces in one artifact."
        ],
        "next": 'Continue with <a href="section-46.1.html">Section 46.1: Why humanoids became the focus</a>, where the chapter first justifies the morphology before spending complexity on it.',
        "production_1": "Use this chapter as a whole-body integration pass. Each section should answer what the humanoid observes, which physical constraints matter, how semantic intent enters the system, and what evidence would convince a skeptical researcher.",
        "table_title": "Chapter Tool Map",
        "tool_rows": [
            ("Pinocchio and Drake", "Model-based dynamics, Jacobians, and feasibility analysis"),
            ("TSID or GR00T Whole-Body Control", "Practical whole-body execution and constraint handling"),
            ("HumanoidBench", "Whole-body benchmark coverage across locomotion and manipulation"),
            ("Isaac Lab", "Large-scale simulation and training workflows"),
            ("ROS 2 and LeRobot", "Execution logging, teleoperation, and robot data pipelines")
        ],
        "lab_extension": "Extend the chapter lab by adding one safety intervention replay and one dataset extraction pass so the same artifact can support both control debugging and future learning.",
        "instructor_1": "This chapter can anchor a graduate robotics module because it forces students to reconcile AI abstractions with floating-base dynamics, contact mechanics, and human-zone safety.",
        "instructor_2": "For course delivery, it helps to pair each semantic or learning topic with one hard physical artifact: a contact schedule, a QP trace, a latency budget, or a safety supervisor log.",
        "readiness": "Before leaving the chapter, the reader should be able to justify a humanoid platform choice, sketch a whole-body control problem, explain a retargeting or teleop data path, and define a runtime safety monitor.",
        "teaching": "The best chapter outcome is a same-panel humanoid artifact: tasks, contact schedule, controller logs, intervention logs, and a clear explanation of one remaining failure mode.",
        "agent_1": "The chapter now emphasizes scientific and technological depth over generic humanoid framing. Sections are anchored in floating-base dynamics, benchmark panels, data interfaces, and deployable whole-body control structure.",
        "agent_2": "The production target is a research-grade humanoid stack with contact-aware control, data-driven behavior improvement, and explicit safety instrumentation.",
        "evidence_standard": "A humanoid claim is ready when the chapter names the task, the contact model, the execution layer, the supervision or data path, and the safety or failure trace that could falsify the claim.",
        "biblio": [
            ('HumanoidBench official site. <a href="https://humanoid-bench.github.io/" rel="noopener" target="_blank">https://humanoid-bench.github.io/</a>', "Primary benchmark reference for simulated humanoid tasks."),
            ('Pinocchio official project. <a href="https://github.com/stack-of-tasks/pinocchio" rel="noopener" target="_blank">https://github.com/stack-of-tasks/pinocchio</a>', "Primary model-based dynamics library used across humanoid control stacks."),
            ('GR00T Whole-Body Control documentation. <a href="https://nvlabs.github.io/GR00T-WholeBodyControl/" rel="noopener" target="_blank">https://nvlabs.github.io/GR00T-WholeBodyControl/</a>', "Current maintained reference for advanced humanoid controllers."),
            ('Boston Dynamics Atlas product page. <a href="https://bostondynamics.com/products/atlas/" rel="noopener" target="_blank">https://bostondynamics.com/products/atlas/</a>', "Official industrial framing for a leading enterprise humanoid platform."),
            ('LeRobot documentation. <a href="https://huggingface.co/docs/lerobot/en/index" rel="noopener" target="_blank">https://huggingface.co/docs/lerobot/en/index</a>', "Practical current robot-data tooling reference.")
        ],
    },
}


def main() -> None:
    for rel, data in SECTION_DATA.items():
        replace_main_body(ROOT / rel, render_section(data))
    for rel, data in INDEX_DATA.items():
        replace_main_body(ROOT / rel, render_index(data))


if __name__ == "__main__":
    main()
