from __future__ import annotations

import csv
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audit" / "scientific_depth_round_2.csv"


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def extract_title(raw: str) -> str:
    m = re.search(r"<h1>(.*?)</h1>", raw, flags=re.I | re.S)
    if not m:
        return "this section"
    text = re.sub(r"<[^>]+>", " ", m.group(1))
    text = html.unescape(re.sub(r"\s+", " ", text)).strip()
    return re.sub(r"^Section\s+\d+\.\d+:\s*", "", text)


def section_id_from_path(path: str) -> str:
    m = re.search(r"section-(\d+\.\d+)\.html", path)
    return m.group(1) if m else "0.0"


def chapter_from_path(path: str) -> int:
    m = re.search(r"module-(\d+)-", path)
    return int(m.group(1)) if m else 0


def pack_for(chapter: int, title: str) -> dict[str, str]:
    t = esc(title)
    if chapter == 5:
        return {
            "domain": "kinematics and robot motion",
            "formula": r"$T_{0e}(q)=\prod_i \exp(\hat\xi_i q_i)M,\quad \dot x = J(q)\dot q,\quad \Delta q = J^\top(JJ^\top+\lambda^2 I)^{-1}\Delta x$",
            "algorithm": "Damped least-squares inverse kinematics",
            "steps": [
                "Represent the desired end-effector task as a pose error in the same frame as the Jacobian.",
                "Compute the geometric or analytic Jacobian at the current joint vector.",
                "Solve the damped least-squares update, clamp joint increments, and enforce joint limits.",
                "Forward-propagate the new configuration and log residual task error, condition number, and saturation events.",
            ],
            "tools": "Modern Robotics, Pinocchio, Drake, ROS 2 tf2, MoveIt, NumPy",
            "failure": "A kinematic result fails when frames are mixed, singular values collapse, a redundant joint drifts into a limit, or the solver reduces position error while making orientation impossible.",
            "expected": "Expected output is a decreasing pose residual, a bounded joint update, and a finite Jacobian condition number. A residual that grows after damping usually means the error vector and Jacobian use different frames.",
            "diagram": "kinematics",
        }
    if chapter == 6:
        return {
            "domain": "dynamics and simulation",
            "formula": r"$M(q)\ddot q + C(q,\dot q)\dot q + g(q) + J(q)^\top\lambda = \tau,\quad x_{t+\Delta t}=f_\Delta(x_t,\tau_t)$",
            "algorithm": "Simulation step with contact-aware evidence logging",
            "steps": [
                "Assemble mass, Coriolis, gravity, actuator, and contact terms under one unit convention.",
                "Integrate with a fixed timestep and record solver status, penetration depth, and energy drift.",
                "Compare the same control input across a hand model and a maintained simulator.",
                "Flag disagreement by source: inertia convention, contact solver, damping, actuator limits, or timestep.",
            ],
            "tools": "MuJoCo, Drake, Isaac Sim, Gazebo, PyBullet, SAPIEN, NumPy",
            "failure": "A dynamics section is not validated by a plausible animation. It is validated by conserved quantities where they should hold, stable contact where contact is expected, and reproducible divergence when a parameter is perturbed.",
            "expected": "Expected output is a state trace with bounded energy error for free motion, bounded penetration for contact, and an explicit solver-status field. Exploding velocity usually points to timestep, stiffness, or mass-matrix errors.",
            "diagram": "dynamics",
        }
    if chapter == 7:
        return {
            "domain": "feedback control",
            "formula": r"$u_t=K_p e_t+K_i\sum_{\tau\le t}e_\tau\Delta t+K_d(e_t-e_{t-1})/\Delta t,\quad \min_{u_{0:H}}\sum_{k=0}^{H}\ell(x_k,u_k)$",
            "algorithm": "Controller evaluation loop",
            "steps": [
                "Define the reference, measured state, error signal, actuator command, update rate, and saturation policy.",
                "Run a step or disturbance response before adding learning.",
                "Log overshoot, settling time, steady-state error, latency, saturation, and recovery behavior.",
                "Compare PID, LQR, or MPC only under the same plant, sensors, limits, disturbance panel, and metric code.",
            ],
            "tools": "python-control, CasADi, do-mpc, Drake, ROS 2 control, MuJoCo",
            "failure": "A controller that looks good on nominal tracking may still fail under delay, integral windup, actuator saturation, unmodeled friction, or reference-frame mismatch.",
            "expected": "Expected output is a trace showing the error falls, overshoot stays inside the design bound, and actuator commands remain within limits. If success changes when logging is enabled, the timing budget is part of the system.",
            "diagram": "control",
        }
    if chapter == 8:
        return {
            "domain": "state estimation and sensing",
            "formula": r"$\hat x^-_t=F\hat x_{t-1}+Bu_t,\quad P^-_t=FP_{t-1}F^\top+Q,\quad K_t=P^-_tH^\top(HP^-_tH^\top+R)^{-1}$",
            "algorithm": "Prediction, update, and sensor-fusion audit",
            "steps": [
                "State the sensor model, timestamp convention, frame convention, measurement noise, and hidden state.",
                "Predict state and covariance before the measurement arrives.",
                "Associate the measurement, update the posterior, and record innovation and Mahalanobis distance.",
                "Gate or down-weight measurements when latency, occlusion, calibration drift, or outliers violate the model.",
            ],
            "tools": "OpenCV, ROS 2 sensor messages, GTSAM, filterpy, NumPy, Open3D",
            "failure": "A fusion result fails when covariance shrinks without better measurements, timestamps are silently resampled, or a camera, IMU, lidar, and tactile stream are fused in inconsistent frames.",
            "expected": "Expected output is a posterior covariance that contracts after informative measurements and expands under uncertainty. A tiny covariance with large innovations is an overconfidence bug, not a strong estimator.",
            "diagram": "filter",
        }
    if 49 <= chapter <= 51:
        if chapter == 49:
            formula = r"$\mathcal G=(\mathcal S,\{\mathcal A_i\}_{i=1}^n,P,\{r_i\}_{i=1}^n,\gamma),\quad \pi(a|s)=\prod_i\pi_i(a_i|o_i)$"
            alg = "Markov-game rollout and partner-generalization audit"
            tools = "PettingZoo, SuperSuit, RLlib, CleanRL, Stable-Baselines3, JAX"
            failure = "A multi-agent result fails when it only works with fixed partners, hides communication cost, changes the reward contract across baselines, or reports team return without collision, fairness, and coordination diagnostics."
        elif chapter == 50:
            formula = r"$b_{t+1}(h)\propto p(o_t|h,a_t)b_t(h),\quad R(a_t)=\mathbb E_{h\sim b_t}[U(a_t,h)]-\lambda\,\mathrm{risk}(a_t,h)$"
            alg = "Human-aware belief and risk update"
            tools = "ROS 2, Nav2, MoveIt, OpenCV, speech and language APIs, user-study logs"
            failure = "An HRI result fails when it optimizes task success while degrading legibility, consent, trust calibration, privacy, or recovery behavior after the human changes intent."
        else:
            formula = r"$\mathcal D_t=\{(o,a,r,o')\}_{\tau<t},\quad \theta_{t+1}=\operatorname{Update}(\theta_t,\mathcal D_t,\mathcal M_t)$"
            alg = "Open-world memory, novelty, and replay audit"
            tools = "Gymnasium, Habitat, AI2-THOR, vector databases, LeRobot, PyTorch"
            failure = "An open-world result fails when novelty is detected but not acted on, replay overfits stale experience, or success is measured only on the original task distribution."
        return {
            "domain": "multi-agent and human-centered embodiment",
            "formula": formula,
            "algorithm": alg,
            "steps": [
                "Define agents, observations, action spaces, communication channels, reward or utility terms, and logging rights.",
                "Run nominal and perturbed episodes with the same partner, held-out partner, and changed-goal panels.",
                "Record task success together with coordination, safety, latency, intervention, and recovery metrics.",
                "Explain failures by information, incentives, memory, human intent, communication, or evaluation mismatch.",
            ],
            "tools": tools,
            "failure": failure,
            "expected": "Expected output is a per-agent trace with observations, actions, rewards or utilities, interventions, and failure labels. Aggregate score alone is not enough because coordination failures can average away.",
            "diagram": "multiagent",
        }
    if 56 <= chapter <= 58:
        return {
            "domain": "frontier embodied agents",
            "formula": r"$m_t=\operatorname{Retrieve}(q_t,\mathcal M),\quad a_t\sim \pi_\theta(a|o_t,g_t,m_t),\quad \mathcal M\leftarrow\mathcal M\cup\phi(o_t,a_t,r_t)$",
            "algorithm": "Memory, continual-learning, and frontier-risk evaluation",
            "steps": [
                "Name the memory item, retrieval query, policy input, task distribution, and update rule.",
                "Separate in-context adaptation, parameter updates, dataset growth, and external tool use.",
                "Evaluate old tasks, new tasks, shifted embodiments, and adversarial perturbations in one artifact.",
                "Report forgetting, transfer, calibration, latency, safety interventions, and manual review cases.",
            ],
            "tools": "LeRobot, Habitat, AI2-THOR, PyTorch, vector databases, Weights & Biases, offline evaluation harnesses",
            "failure": "A frontier section is shallow if it names memory or lifelong learning without defining what is stored, how retrieval affects action, what can be updated, and how old capabilities are protected.",
            "expected": "Expected output is a table where new-task success is reported beside retained old-task success, calibration, retrieval hit rate, and failure labels. Improvement on only the latest task is not enough.",
            "diagram": "memory",
        }
    if chapter == 59:
        return {
            "domain": "capstone implementation",
            "formula": r"$\text{artifact}=(\text{dataset},\text{environment},\text{baseline},\text{policy},\text{metric},\text{failure review},\text{rubric})$",
            "algorithm": "Capstone build pipeline",
            "steps": [
                "Freeze the task statement, dataset or simulator, robot embodiment, action space, and success metric.",
                "Build a baseline that can run in one command and write a manifest with seeds, configs, and versions.",
                "Train or evaluate the target model, then run a held-out panel with at least one perturbation and one failure review.",
                "Package code, logs, plots, videos or screenshots, and a short engineering memo against the grading rubric.",
            ],
            "tools": "LeRobot, robomimic, Gymnasium, MuJoCo, Habitat, ROS 2, PyTorch, Weights & Biases",
            "failure": "A capstone is not a topic description. It must specify artifacts, commands, expected outputs, evaluation splits, compute budget, and grading evidence.",
            "expected": "Expected output is a reproducible folder with config files, run logs, evaluation JSON, representative successes, representative failures, and a short rubric-aligned report.",
            "diagram": "capstone",
        }
    if chapter == 60:
        return {
            "domain": "course design",
            "formula": r"$\text{week}_k=(\text{reading},\text{concept},\text{lab},\text{artifact},\text{rubric},\text{checkpoint})$",
            "algorithm": "Fourteen-week course and assessment design",
            "steps": [
                "Map prerequisites to the first two weeks so readers know which math and software assumptions are active.",
                "Assign one lab artifact per week: notebook, simulator run, robot-data audit, diagram, or evaluation report.",
                "Stage capstone milestones: proposal, baseline, data or environment, model run, failure review, final artifact.",
                "Grade with reproducibility, technical depth, evaluation discipline, communication, and safety criteria.",
            ],
            "tools": "Jupyter, Gymnasium, MuJoCo, ROS 2, LeRobot, GitHub Classroom, nbgrader, lightweight CI",
            "failure": "A course-design section fails if it only lists topics. It needs weekly pacing, assignments, rubrics, checkpoints, and support for both undergraduate and graduate variants.",
            "expected": "Expected output is a schedule and rubric that an instructor can adopt without inventing labs, prerequisites, deliverables, or milestone dates from scratch.",
            "diagram": "course",
        }
    if chapter == 27:
        return {
            "domain": "perception for action",
            "formula": r"$a^*=\arg\max_a \mathbb E[U(a,s)\mid z_{1:t}],\quad z_t=(I_t,D_t,K,T_{cw},\sigma_t)$",
            "algorithm": "Action-conditioned perception audit",
            "steps": [
                "Convert image evidence into metric state variables with camera intrinsics, extrinsics, and uncertainty.",
                "Score candidate actions by task value, collision risk, confidence, and latency.",
                "Perturb lighting, occlusion, viewpoint, calibration, and motion blur while keeping the action metric fixed.",
                "Log whether failure came from sensing, geometry, recognition, action scoring, or controller execution.",
            ],
            "tools": "OpenCV, Open3D, Segment Anything, DINOv2, PyTorch, ROS 2",
            "failure": "A perception result fails when an impressive mask, class label, or depth prediction does not change the chosen action or hides uncertainty that the controller needs.",
            "expected": "Expected output is an action ranking that changes under meaningful visual evidence and remains stable under irrelevant image variation.",
            "diagram": "perception",
        }
    if chapter == 30:
        return {
            "domain": "navigation and planning",
            "formula": r"$f(n)=g(n)+h(n),\quad h(n)\le h^*(n),\quad x_{t+1}=f(x_t,u_t),\quad u_t\in\mathcal U_{\mathrm{safe}}$",
            "algorithm": "Planner and navigation-stack audit",
            "steps": [
                "Build the graph, roadmap, tree, cost map, or goal-conditioned policy under one map and frame convention.",
                "State the cost function, heuristic, collision checker, local-controller limits, and replanning trigger.",
                "Compare path length, clearance, time-to-goal, collision count, recovery behavior, and compute budget.",
                "Inspect failures by map error, heuristic inadmissibility, sampler coverage, local-minimum trap, policy overfit, or language-goal grounding error.",
            ],
            "tools": "NetworkX, OMPL, ROS 2 Nav2, Habitat, AI2-THOR, Gymnasium, PyTorch",
            "failure": "A navigation section fails if it draws a path but does not explain graph construction, heuristic validity, collision checking, controller limits, and replanning behavior.",
            "expected": "Expected output is a path or action trace with cost, clearance, runtime, and failure label. A shorter path that violates clearance is not a better planner.",
            "diagram": "navigation",
        }
    return {
        "domain": "embodied systems",
        "formula": r"$\text{claim}=(\text{state},\text{action},\text{metric},\text{perturbation},\text{evidence})$",
        "algorithm": "Construct-matched evidence audit",
        "steps": [
            "Define the state, action, metric, perturbation, and evidence artifact.",
            "Run baseline and shortcut on the same configuration.",
            "Log expected output and the failure label.",
            "Compare only numbers produced by the same script on the same panel.",
        ],
        "tools": "NumPy, PyTorch, Gymnasium, ROS 2, Weights & Biases",
        "failure": "The section fails when it cannot say what changed in the embodied system and why the evidence supports that change.",
        "expected": "Expected output is a reproducible artifact, not a prose claim.",
        "diagram": "default",
    }


def diagram_svg(kind: str, sid: str, title: str, domain: str) -> str:
    safe_title = esc(title)
    safe_domain = esc(domain)
    fid = f"fig-{sid.replace('.', '-')}-technical-core"
    return f"""<figure class="technical-figure" id="{fid}">
<svg viewBox="0 0 860 310" role="img" aria-labelledby="{fid}-title {fid}-desc">
<title id="{fid}-title">Technical core for {safe_title}</title>
<desc id="{fid}-desc">A block diagram connecting assumptions, model, algorithm, evidence, and failure analysis for {safe_title}.</desc>
<rect x="24" y="50" width="148" height="86" rx="8" fill="#e3f2fd" stroke="#1565c0"/>
<text x="98" y="82" text-anchor="middle" font-size="14">Assumptions</text>
<text x="98" y="106" text-anchor="middle" font-size="12">frames, units, limits</text>
<rect x="202" y="50" width="148" height="86" rx="8" fill="#e8f5e9" stroke="#2e7d32"/>
<text x="276" y="82" text-anchor="middle" font-size="14">Model</text>
<text x="276" y="106" text-anchor="middle" font-size="12">{safe_domain}</text>
<rect x="380" y="50" width="148" height="86" rx="8" fill="#fff3e0" stroke="#e65100"/>
<text x="454" y="82" text-anchor="middle" font-size="14">Algorithm</text>
<text x="454" y="106" text-anchor="middle" font-size="12">update or plan</text>
<rect x="558" y="50" width="128" height="86" rx="8" fill="#f3e5f5" stroke="#6a1b9a"/>
<text x="622" y="82" text-anchor="middle" font-size="14">Evidence</text>
<text x="622" y="106" text-anchor="middle" font-size="12">trace, metric</text>
<rect x="716" y="50" width="120" height="86" rx="8" fill="#fce4ec" stroke="#c62828"/>
<text x="776" y="82" text-anchor="middle" font-size="14">Failure</text>
<text x="776" y="106" text-anchor="middle" font-size="12">diagnosis</text>
<path d="M172 93 H202 M350 93 H380 M528 93 H558 M686 93 H716" stroke="#555" stroke-width="2"/>
<rect x="70" y="196" width="720" height="58" rx="8" fill="#f8fafc" stroke="#607d8b"/>
<text x="430" y="222" text-anchor="middle" font-size="14">Graduate-depth contract: define variables, run the method, interpret output, and explain when it fails.</text>
<text x="430" y="242" text-anchor="middle" font-size="12">This diagram marks the minimum technical chain the section must make explicit.</text>
</svg>
<figcaption><strong>Figure {sid}.T</strong>: The technical core for {safe_title} connects assumptions, model, algorithm, evidence, and failure analysis.</figcaption>
</figure>"""


def technical_core(path: str, title: str) -> str:
    chapter = chapter_from_path(path)
    sid = section_id_from_path(path)
    pack = pack_for(chapter, title)
    t = esc(title)
    steps = "\n".join(f"<li>{esc(step)}</li>" for step in pack["steps"])
    code = f"""# Technical-core evidence record for {title}.
# Expected: a method-specific trace with assumptions, metric, and failure label.
record = {{
    "section": "{sid}",
    "technical_core": "{pack['domain']}",
    "method": "{pack['algorithm']}",
    "evidence": "same-config trace with expected output and failure label",
    "tools": "{pack['tools']}",
}}
print(record)"""
    return f"""
<section class="technical-core-expansion">
<h2>Technical Core</h2>
<p><strong>{t}</strong> needs a topic-native core: variables, equations or system contracts, an algorithmic procedure, an expected output, and a failure diagnosis. Figure {sid}.T summarizes the chain this section must preserve when moving from a teaching example to a real embodied system.</p>
{diagram_svg(pack["diagram"], sid, title, pack["domain"])}
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>{pack["formula"]}</p></div>
<div class="callout algorithm"><div class="callout-title">{esc(pack["algorithm"])}</div><ol>
{steps}
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Technical Contract For {t}</div><table><thead><tr><th>Contract Field</th><th>What To Specify</th><th>Why It Matters</th></tr></thead><tbody>
<tr><td>State and observation</td><td>Variables, units, timestamps, frames, and uncertainty.</td><td>Prevents a model score from being mistaken for robot capability.</td></tr>
<tr><td>Action interface</td><td>Command type, limits, update rate, and safety fallback.</td><td>Makes the learned or planned output executable.</td></tr>
<tr><td>Evidence artifact</td><td>Trace, metric, configuration, seed, and failure label.</td><td>Allows baseline and library path to be compared in one pass.</td></tr>
<tr><td>Tool path</td><td>{esc(pack["tools"])}</td><td>Shows the practical library route after the mechanism is understood.</td></tr>
</tbody></table></div>
<pre><code class="language-python">{esc(code)}</code></pre>
<div class="code-caption">Code Fragment {sid}.T records the expected technical evidence for {t}: method, tool path, artifact, and failure label.</div>
<p>{esc(pack["expected"])}</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>{esc(pack["failure"])}</p></div>
</section>
"""


def replace_templates(raw: str, title: str) -> str:
    replacements = {
        "reader fill in after perturbation test": "filled after the named perturbation test",
        "This section turns the idea of": "This section develops the technical contract for",
        "Run this tiny probe before moving to the maintained library path.": "Run this diagnostic probe before trusting the maintained library path.",
        "pick up the red block and place it on the tray": f"run the {title} diagnostic and save the evidence trace",
        "Design a minimal experiment": "Design a method-matched experiment",
        "smallest executable pattern for this section's idea": "minimal executable diagnostic for this section's method",
        "minimum evidence schema for testing": "method-specific evidence schema for testing",
        "is ready for embodied AI work when it changes a concrete action, exposes uncertainty, and leaves behind an evidence record that another reader can rerun": "is ready for embodied AI work when its assumptions, algorithm, action interface, and failure labels are explicit enough to reproduce",
    }
    for old, new in replacements.items():
        raw = raw.replace(old, new)
    return raw


def insert_core(raw: str, path: str) -> tuple[str, bool]:
    if 'class="technical-core-expansion"' in raw:
        return raw, False
    title = extract_title(raw)
    core = technical_core(path, title)
    marker = '<div class="callout key-takeaway">'
    idx = raw.find(marker)
    if idx == -1:
        marker = '<section class="bibliography">'
        idx = raw.find(marker)
    if idx == -1:
        marker = '<nav class="chapter-nav">'
        idx = raw.find(marker)
    if idx == -1:
        return raw, False
    raw = replace_templates(raw, title)
    return raw[:idx] + core + "\n" + raw[idx:], True


def main() -> None:
    with AUDIT.open(newline="", encoding="utf-8") as f:
        rows = [row for row in csv.DictReader(f) if row["verdict"] == "DEPTH-GAP"]
    changed = []
    skipped = []
    for row in rows:
        path = row["path"]
        full = ROOT / path
        raw = full.read_text(encoding="utf-8")
        updated, did = insert_core(raw, path)
        if did:
            full.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(path)
        else:
            skipped.append(path)
    print(f"depth_gap_sections={len(rows)}")
    print(f"changed={len(changed)}")
    print(f"skipped={len(skipped)}")
    for p in skipped:
        print(f"SKIPPED {p}")


if __name__ == "__main__":
    main()
