from __future__ import annotations

from pathlib import Path


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


def replace_between(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    return text[:start] + "\n" + replacement.strip() + "\n" + text[end:]


def section_block(
    *,
    number: str,
    title: str,
    chapter_title: str,
    epigraph: str,
    cite: str,
    figure_html: str,
    big_picture: str,
    pathway: str,
    sections: list[str],
    code: str,
    code_output: str,
    code_caption: str,
    expected_output: str,
    shortcut: str,
    warning: str,
    example: str,
    frontier: str,
    self_check: str,
    takeaway: str,
    exercise: str,
    next_text: str,
    refs: list[tuple[str, str]],
) -> str:
    if chapter_title == "Evaluating Embodied Systems":
        tool_anchor = "Concrete stack anchors for this chapter include Pandas for paired episode tables, SciPy for bootstrap or paired significance tests, DVC for panel and artifact versioning, MLflow or Weights and Biases Artifacts for run lineage, and ROS 2 bags for synchronized physical replay."
    elif chapter_title == "Robustness and Uncertainty":
        tool_anchor = "Concrete stack anchors for this chapter include Albumentations or custom disturbance wrappers for controlled perturbations, Torchmetrics and scikit-learn for calibration analysis, MAPIE or related conformal wrappers for thresholding, PyOD-style OOD baselines for score comparison, and Prometheus or OpenTelemetry for deployment-time health traces."
    else:
        tool_anchor = "Concrete stack anchors for this chapter include hazard logs and FMEA tables for structured review, cvxpy and OSQP for small QP-based safety filters, reachability toolchains such as hj_reachability-style workflows for safe-set analysis, ROS 2 lifecycle nodes for intervention authority, and GSN-style assurance templates for release evidence."
    theory, formula, diagram_ref, algorithm, practice, deep_dive, failure, cross_refs, lab = sections
    bib_cards = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref}</p><p class="bib-annotation">{ann}</p></div>'
        for ref, ann in refs
    )
    return f"""
<blockquote class="epigraph">
<p>{epigraph}</p>
<cite>{cite}</cite>
</blockquote>
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>{big_picture}</p>
</div>
<div class="callout pathway">
<div class="callout-title">Reader Pathway</div>
<p>{pathway}</p>
</div>
{figure_html}
<h2>Why This Matters</h2>
<p>{theory}</p>
<p>{formula}</p>
<div class="callout key-insight">
<div class="callout-title">Key Insight</div>
<p>{diagram_ref}</p>
</div>
<div class="callout algorithm">
<div class="callout-title">Algorithmic View</div>
<ol>{algorithm}</ol>
</div>
<h2>Worked Example</h2>
<p>{practice}</p>
<pre><code class="language-python">{code}</code></pre>
<div class="code-output"><pre>{code_output}</pre></div>
<div class="code-caption">{code_caption}</div>
<p><strong>Expected output:</strong> {expected_output}</p>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>{shortcut}</p>
<p>{tool_anchor}</p>
</div>
<section class="production-depth-expansion">
<h2>Builder's Deep Dive</h2>
<p>{deep_dive}</p>
<p>{tool_anchor}</p>
<p>{failure}</p>
<div class="comparison-table">
<div class="comparison-table-title">Implementation Checklist For Section {number}</div>
<table>
<thead><tr><th>Layer</th><th>What To Freeze</th><th>What To Save</th></tr></thead>
<tbody>
<tr><td>Scenario panel</td><td>Task distribution, seeds, perturbation schedule, and reset rules.</td><td>Manifest, config, and task identifiers.</td></tr>
<tr><td>Runtime interface</td><td>Observation timestamps, state schema, action bounds, and monitor thresholds.</td><td>Synchronized logs, alerts, and controller states.</td></tr>
<tr><td>Metric script</td><td>Exact aggregation code, confidence interval rule, and filtering policy.</td><td>One result table plus replay links.</td></tr>
<tr><td>Review layer</td><td>Failure taxonomy, residual risk, and escalation owner.</td><td>Postmortem note and remediation ticket.</td></tr>
</tbody>
</table>
</div>
<h2>Cross-References</h2>
<p>{cross_refs}</p>
<div class="callout lab">
<div class="callout-title">Lab Recipe</div>
<p>{lab}</p>
</div>
</section>
<div class="callout warning">
<div class="callout-title">Failure Mode</div>
<p>{warning}</p>
</div>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>{example}</p>
</div>
<div class="callout research-frontier">
<div class="callout-title">Research Frontier</div>
<p>{frontier}</p>
</div>
<div class="callout self-check">
<div class="callout-title">Self Check</div>
<p>{self_check}</p>
</div>
<div class="callout key-takeaway">
<div class="callout-title">Key Takeaway</div>
<p>{takeaway}</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise {number}.1</div>
<p>{exercise}</p>
</div>
<section class="bibliography">
<h2>Section References</h2>
{bib_cards}
</section>
<div class="callout whats-next">
<div class="callout-title">What's Next</div>
<p>{next_text}</p>
</div>
"""


def index_block(
    *,
    chapter_number: str,
    chapter_title: str,
    epigraph: str,
    cite: str,
    big_picture: str,
    insight: str,
    overview: list[str],
    roadmap_items: list[tuple[str, str, str]],
    tooling_note: str,
    lab_objective: str,
    lab_steps: list[str],
    next_text: str,
    production_notes: list[str],
    tool_rows: list[tuple[str, str]],
    instructor_notes: list[str],
    readiness: str,
    takeaway: str,
    refs: list[tuple[str, str]],
) -> str:
    roadmap = "".join(
        f'<li><span class="section-num">{sec}</span> <a href="section-{sec}.html"><span class="section-title">{title}</span></a><span class="section-desc">{desc}</span></li>'
        for sec, title, desc in roadmap_items
    )
    tool_map = "".join(f"<tr><td>{tool}</td><td>{role}</td></tr>" for tool, role in tool_rows)
    bib_cards = "\n".join(
        f'<div class="bib-entry-card"><p class="bib-ref">{ref}</p><p class="bib-annotation">{ann}</p></div>'
        for ref, ann in refs
    )
    steps = "".join(f"<li>{step}</li>" for step in lab_steps)
    return f"""
<blockquote class="epigraph">
<p>{epigraph}</p>
<cite>{cite}</cite>
</blockquote>
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>{big_picture}</p>
</div>
<div class="callout key-insight">
<div class="callout-title">Remember This Chapter</div>
<p>{insight}</p>
</div>
<div class="overview">
<h2>Chapter Overview</h2>
<p>{overview[0]}</p>
<p>{overview[1]}</p>
<p>This chapter keeps a research-grade standard throughout: every promoted claim should be tied to one matched panel, one artifact bundle, and one replay path that lets another team inspect what changed in the closed loop.</p>
</div>
<div class="prereqs"><h3>Prerequisites</h3><p>{overview[2]}</p></div>
<h2>Chapter Roadmap</h2>
<ul class="sections-list">{roadmap}</ul>
<div class="callout library-shortcut">
<div class="callout-title">Tooling Note</div>
<p>{tooling_note}</p>
<p>The chapter's practical standard is simple: use tools that preserve provenance, timestamps, intervention traces, and replay links. A shorter script is only an advantage when the evidence chain stays intact.</p>
</div>
<section class="lab" id="lab-{chapter_number}">
<h2>Hands-On Lab: Build the Evaluation Stack</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 90 to 150 minutes</span><span class="lab-difficulty">Difficulty: Advanced</span></div>
<div class="lab-objective"><h3>Objective</h3><p>{lab_objective}</p></div>
<div class="lab-steps"><h3>Steps</h3><ol>{steps}</ol></div>
</section>
<div class="whats-next"><h3>What's Next?</h3><p>{next_text}</p></div>
<section class="production-depth-expansion">
<h2>Production Notes For Readers</h2>
<p>{production_notes[0]}</p>
<p>{production_notes[1]}</p>
<p>When reading or teaching the chapter, insist on one more question after every result: which files would another researcher need in order to reproduce, challenge, or extend this exact conclusion without guessing hidden protocol details?</p>
<div class="comparison-table">
<div class="comparison-table-title">Chapter Tool Map</div>
<table>
<thead><tr><th>Tool or Library</th><th>Where It Pays Off</th></tr></thead>
<tbody>{tool_map}</tbody>
</table>
</div>
<div class="callout lab"><div class="callout-title">Chapter Lab Extension</div><p>{production_notes[2]}</p></div>
</section>
<section class="production-index-depth-topup">
<h2>Instructor And Builder Notes</h2>
<p>{instructor_notes[0]}</p>
<p>{instructor_notes[1]}</p>
<div class="callout note"><div class="callout-title">Evaluation Standard</div><p>Each chapter in this part should end with a dossier, not only a plot: configuration, panel definition, metric script, synchronized logs, replay artifact, failure taxonomy, and a short statement of residual uncertainty or residual risk.</p></div>
<div class="callout practical-example"><div class="callout-title">Review Board Questions</div><p>A strong seminar or design review should ask four questions at the chapter boundary: what exactly was frozen, what evidence would falsify the claim, which tool preserves the audit trail, and which residual risk or uncertainty still remains after the best current mitigation is applied.</p></div>
<div class="callout self-check"><div class="callout-title">Readiness Check</div><p>{readiness}</p></div>
<div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>{takeaway}</p></div>
</section>
<section class="bibliography">
<h2>Bibliography &amp; Further Reading</h2>
<h3>Foundational Papers, Tools, and References</h3>
{bib_cards}
</section>
    """


def eval_section(
    *,
    number: str,
    title: str,
    image: str,
    figure_caption: str,
    big_picture: str,
    formula: str,
    key_insight: str,
    algorithm_items: list[str],
    worked_example: str,
    code: str,
    code_output: str,
    code_caption: str,
    expected_output: str,
    shortcut: str,
    deep_dive: str,
    failure: str,
    cross_refs: str,
    lab: str,
    warning: str,
    example: str,
    frontier: str,
    self_check: str,
    takeaway: str,
    exercise: str,
    next_text: str,
    refs: list[tuple[str, str]],
) -> str:
    algorithm = "".join(f"<li>{item}</li>" for item in algorithm_items)
    return section_block(
        number=number,
        title=title,
        chapter_title="Evaluating Embodied Systems",
        epigraph="A benchmark becomes scientific when it can tell you not just who won, but why the conclusion should survive reruns.",
        cite="An Evaluation Methodologist",
        figure_html=f"""
<figure class="illustration">
<img alt="{title} illustration for Chapter 52." loading="lazy" src="images/{image}"/>
<figcaption><strong>Figure {number}.1</strong>: {figure_caption}</figcaption>
</figure>
""",
        big_picture=big_picture,
        pathway="Read this section by asking which quantity is being aggregated, which rollout panel produced it, and which failure modes become visible or hidden under that choice.",
        sections=[
            f"{title} matters because evaluation choices rewrite the scientific claim. If the metric drops time, energy, or safety terms that the deployment team cares about, the benchmark no longer matches the real decision.",
            formula,
            key_insight,
            algorithm,
            worked_example,
            deep_dive,
            failure,
            cross_refs,
            lab,
        ],
        code=code,
        code_output=code_output,
        code_caption=code_caption,
        expected_output=expected_output,
        shortcut=shortcut,
        warning=warning,
        example=example,
        frontier=frontier,
        self_check=self_check,
        takeaway=takeaway,
        exercise=exercise,
        next_text=next_text,
        refs=refs,
    )


def robustness_section(
    *,
    number: str,
    title: str,
    image: str,
    figure_caption: str,
    big_picture: str,
    formula: str,
    key_insight: str,
    algorithm_items: list[str],
    worked_example: str,
    code: str,
    code_output: str,
    code_caption: str,
    expected_output: str,
    shortcut: str,
    deep_dive: str,
    failure: str,
    cross_refs: str,
    lab: str,
    warning: str,
    example: str,
    frontier: str,
    self_check: str,
    takeaway: str,
    exercise: str,
    next_text: str,
    refs: list[tuple[str, str]],
) -> str:
    algorithm = "".join(f"<li>{item}</li>" for item in algorithm_items)
    return section_block(
        number=number,
        title=title,
        chapter_title="Robustness and Uncertainty",
        epigraph="A robust robot is not the one that never sees surprise, it is the one that notices surprise early enough to act differently.",
        cite="A Runtime Monitoring Engineer",
        figure_html=f"""
<figure class="illustration">
<img alt="{title} illustration for Chapter 53." loading="lazy" src="images/{image}"/>
<figcaption><strong>Figure {number}.1</strong>: {figure_caption}</figcaption>
</figure>
""",
        big_picture=big_picture,
        pathway="Read this section by tracing the failure from disturbance to confidence signal to changed action. If the section never changes the action, the robustness mechanism is incomplete.",
        sections=[
            f"{title} is useful only when it distinguishes disturbance sources and ties them to specific corrective actions. Robustness is not one scalar, it is a map from perturbation class to degraded behavior, detection delay, and residual risk.",
            formula,
            key_insight,
            algorithm,
            worked_example,
            deep_dive,
            failure,
            cross_refs,
            lab,
        ],
        code=code,
        code_output=code_output,
        code_caption=code_caption,
        expected_output=expected_output,
        shortcut=shortcut,
        warning=warning,
        example=example,
        frontier=frontier,
        self_check=self_check,
        takeaway=takeaway,
        exercise=exercise,
        next_text=next_text,
        refs=refs,
    )


def safety_section(
    *,
    number: str,
    title: str,
    image: str,
    figure_caption: str,
    big_picture: str,
    formula: str,
    key_insight: str,
    algorithm_items: list[str],
    worked_example: str,
    code: str,
    code_output: str,
    code_caption: str,
    expected_output: str,
    shortcut: str,
    deep_dive: str,
    failure: str,
    cross_refs: str,
    lab: str,
    warning: str,
    example: str,
    frontier: str,
    self_check: str,
    takeaway: str,
    exercise: str,
    next_text: str,
    refs: list[tuple[str, str]],
) -> str:
    algorithm = "".join(f"<li>{item}</li>" for item in algorithm_items)
    return section_block(
        number=number,
        title=title,
        chapter_title="Safety in Embodied AI",
        epigraph="Safety is the art of specifying what the robot must refuse, even when the nominal policy is confident.",
        cite="A Safety-Critical Controls Researcher",
        figure_html=f"""
<figure class="illustration">
<img alt="{title} illustration for Chapter 54." loading="lazy" src="images/{image}"/>
<figcaption><strong>Figure {number}.1</strong>: {figure_caption}</figcaption>
</figure>
""",
        big_picture=big_picture,
        pathway="Read this section from hazard to intervention. First identify the unsafe state or action, then ask which mechanism blocks it, then ask which artifact proves the block worked under stress.",
        sections=[
            f"{title} sits at the boundary between learning and safety engineering. The question is not whether the policy usually behaves well, but whether dangerous states are detected, blocked, or exited fast enough to protect people, equipment, and mission goals.",
            formula,
            key_insight,
            algorithm,
            worked_example,
            deep_dive,
            failure,
            cross_refs,
            lab,
        ],
        code=code,
        code_output=code_output,
        code_caption=code_caption,
        expected_output=expected_output,
        shortcut=shortcut,
        warning=warning,
        example=example,
        frontier=frontier,
        self_check=self_check,
        takeaway=takeaway,
        exercise=exercise,
        next_text=next_text,
        refs=refs,
    )


INDEX_CONTENT = {
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html": index_block(
        chapter_number="52",
        chapter_title="Evaluating Embodied Systems",
        epigraph="A robot benchmark is only serious when it can disappoint your favorite model in a way you can replay.",
        cite="A Skeptical Evaluation Engineer",
        big_picture="Chapter 52 turns evaluation from a leaderboard ritual into a scientific instrument. The central object is a matched rollout panel that produces task success, efficiency, safety, robustness, and replay artifacts in one pass.",
        insight="Evaluation numbers are only comparable when they come from the same task panel, the same metric script, the same hardware or simulator contract, and the same perturbation schedule.",
        overview=[
            "This chapter defines the evaluation unit for embodied AI: the closed-loop episode with fixed task sampling, logged perturbations, synchronized monitors, and reproducible aggregation. We work from single-task rollouts to chapter-level benchmark design.",
            "The theory thread covers construct-matched metrics, confidence intervals, statistical validity, and sim-as-proxy arguments. The practical thread shows how to organize logs, replay artifacts, and benchmark manifests so other teams can reproduce claims instead of reinterpreting them.",
            "Readers should already know the perception-action loop, simulator workflow, and the role of runtime monitors from earlier parts. Chapter 12 on task suites, Chapter 20 on sim-to-real transfer, and Chapter 51 on lifelong adaptation are especially relevant.",
        ],
        roadmap_items=[
            ("52.1", "Why accuracy is not enough", "Replace static model scores with closed-loop utility and failure-aware evaluation."),
            ("52.2", "Success rate, path efficiency, time and energy cost", "Build multi-objective metrics that respect physical resources and timing budgets."),
            ("52.3", "Safety violations and constraint satisfaction", "Measure whether the robot stayed inside the operational envelope, not only whether it finished."),
            ("52.4", "Robustness and generalization metrics", "Separate nominal performance from perturbation response, OOD behavior, and worst-case tails."),
            ("52.5", "Reproducible evaluation: SIMPLER and sim-as-proxy", "Use simulator proxies without losing contact with real-world evidence."),
            ("52.6", "Real-world evaluation hygiene; benchmark design", "Pre-register protocols, control operator effects, and audit every comparison artifact."),
        ],
        tooling_note="Use lightweight data classes to make the metric contract explicit, then graduate to DVC, MLflow, Weights and Biases Artifacts, ROS 2 bags, and benchmark manifests. The right tool matters because evaluation work fails more often from missing provenance than from missing model capacity.",
        lab_objective="Build a matched evaluation panel for one embodied task, with one simulator run set and one small physical or replay-based validation set. Save all scalar metrics, rollout traces, perturbation labels, and postmortems in one manifest.",
        lab_steps=[
            "Define the task suite, perturbation schedule, and failure taxonomy before choosing a model variant.",
            "Implement one metric script that computes success, efficiency, safety, and robustness from the same episode table.",
            "Run a nominal panel, a perturbed panel, and one replay inspection pass.",
            "Compute confidence intervals or bootstrap bands for each metric.",
            "Write a one-page review note explaining whether the simulator panel is a usable proxy for the real task.",
        ],
        next_text='Continue with <a href="section-52.1.html">Section 52.1: Why accuracy is not enough</a>, where closed-loop utility replaces static accuracy as the central evaluation object.',
        production_notes=[
            "Read this chapter with the mindset of a reviewer who asks, for every claimed improvement, which panel produced the number, how the perturbations were sampled, and which replay artifact could reproduce the conclusion.",
            "A strong evaluation chapter leaves behind a complete chain: task distribution, environment version, reset policy, seed schedule, metric script, synchronized logs, failure taxonomy, and a result table whose rows can be traced back to episode artifacts.",
            "Extend the lab by adding a second policy family and reusing the exact same panel. If the comparison still needs hand explanations, the protocol is underspecified.",
        ],
        tool_rows=[
            ("DVC", "Version task manifests, panel definitions, and replay artifacts so benchmark changes are explicit."),
            ("MLflow or Weights and Biases Artifacts", "Store configuration, metric tables, videos, and model checkpoints under one run id."),
            ("ROS 2 bagging", "Capture synchronized sensor, action, and monitor traces for physical-system replay."),
            ("Pandas plus SciPy", "Compute confidence intervals, paired tests, and bootstrap summaries from one episode table."),
            ("Hydra or OmegaConf", "Freeze evaluation configuration so panel drift is visible."),
        ],
        instructor_notes=[
            "Teach these sections as a sequence from scalar metrics to benchmark governance. Students often understand success rate before they understand why evaluation panels must be matched by construction.",
            "For project-based teaching, insist that every team submit one result artifact with both wins and failure labels. That single discipline turns demonstrations into cumulative evidence.",
        ],
        readiness="Before leaving the chapter, the reader should be able to design a matched evaluation panel, compute at least one uncertainty interval, explain why a simulator proxy is or is not trustworthy, and audit an invalid comparison.",
        takeaway="The chapter succeeds when evaluation becomes an engineering object: matched panels, one metric script, explicit perturbations, and replayable evidence.",
        refs=[
            ('Henderson, P. et al. "Deep Reinforcement Learning that Matters." (2018). <a href="https://arxiv.org/abs/1709.06560" rel="noopener" target="_blank">https://arxiv.org/abs/1709.06560</a>', "A classic warning that reported RL gains often collapse under weak evaluation practice."),
            ('Agarwal, R. et al. "Deep Reinforcement Learning at the Edge of the Statistical Precipice." (2021). <a href="https://arxiv.org/abs/2108.13264" rel="noopener" target="_blank">https://arxiv.org/abs/2108.13264</a>', "Useful for confidence intervals, aggregate statistics, and matched comparisons."),
            ('Brohan, A. et al. "RT-1: Robotics Transformer for real-world control at scale." (2022). <a href="https://arxiv.org/abs/2212.06817" rel="noopener" target="_blank">https://arxiv.org/abs/2212.06817</a>', "A reference point for large-scale real-robot evaluation with task diversity."),
            ('Official SIMPLER resources and related sim-to-real benchmark artifacts.', "Use the project assets for proxy-evaluation design and traceability across simulation and real execution."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/index.html": index_block(
        chapter_number="53",
        chapter_title="Robustness and Uncertainty",
        epigraph="Uncertainty is only useful when it changes a control decision before the collision, the timeout, or the empty grasp.",
        cite="A Runtime Assurance Researcher",
        big_picture="Chapter 53 treats robustness as a property of the whole embodied loop, not just the perception model. Disturbance channels, calibration errors, OOD states, and monitor transitions all have to be measured together.",
        insight="A robot is robust only when it detects that its assumptions are breaking, updates confidence faithfully, and changes behavior before the failure compounds.",
        overview=[
            "This chapter organizes robustness by disturbance source: sensor corruption, domain shift, uncertainty miscalibration, OOD states, and runtime degradation. The goal is not to list threats but to tie each threat to detection, mitigation, and measurable residual risk.",
            "We move from shift taxonomies and uncertainty decomposition to practical OOD scores, calibration diagnostics, runtime monitor design, and fail-safe transitions. Every method is evaluated through the same artifact discipline introduced in Chapter 52.",
            "Readers should be comfortable with probability, rollout evaluation, and safety-aware deployment ideas. Chapter 27 on action-conditioned perception, Chapter 29 on SLAM, and Chapter 52 on evaluation methodology form the main prerequisites.",
        ],
        roadmap_items=[
            ("53.1", "What goes wrong: sensor noise, distribution shift", "Map failure classes to disturbance channels and repair paths."),
            ("53.2", "Model uncertainty and calibration", "Separate aleatoric and epistemic uncertainty, then measure calibration quality."),
            ("53.3", "Out-of-distribution detection", "Score novelty before it becomes silent policy extrapolation."),
            ("53.4", "Runtime monitoring and fail-safe behavior", "Convert uncertainty signals into state transitions, degraded modes, and recovery logic."),
        ],
        tooling_note="Start with direct NumPy and PyTorch estimators so the uncertainty equations are visible, then use torchmetrics, conformal wrappers, ROS diagnostics, Prometheus, and observability tooling when the signal needs to survive deployment.",
        lab_objective="Instrument one embodied policy with perturbation labels, uncertainty estimates, and a runtime monitor. The deliverable is a table that links each failure to the channel that announced it earliest.",
        lab_steps=[
            "Inject at least three perturbation types, such as motion blur, dropped depth frames, and actuation delay.",
            "Log ensemble or dropout variance, calibration metrics, and OOD scores alongside task outcomes.",
            "Define threshold-based monitor states and record state transitions.",
            "Replay failure cases and determine which signal gave the earliest actionable warning.",
            "Write one intervention policy that changes behavior when uncertainty crosses a threshold.",
        ],
        next_text='Continue with <a href="section-53.1.html">Section 53.1: What goes wrong: sensor noise, distribution shift</a>, where robustness starts by naming the disturbance channel precisely.',
        production_notes=[
            "The key reading habit is to ask which uncertainty is being discussed. Observation noise, model uncertainty, planner uncertainty, and map uncertainty have different mitigations and different deployment consequences.",
            "A high-quality robustness pipeline always saves the clean baseline, the perturbation family, the uncertainty signal, the chosen threshold, the monitor transition, and the final outcome in one artifact set.",
            "Extend the lab by fitting one threshold on a calibration panel and testing it on a shifted panel. This makes threshold drift visible.",
        ],
        tool_rows=[
            ("Albumentations or custom wrappers", "Generate controlled visual perturbations for disturbance panels."),
            ("Torch ensemble or MC dropout tooling", "Produce predictive variance estimates that can be logged per action or prediction."),
            ("Torchmetrics calibration utilities", "Compute ECE, reliability bins, and calibration curves."),
            ("Prometheus plus Grafana", "Expose uncertainty and health signals in deployment."),
            ("ROS 2 diagnostics", "Route monitor alarms and degraded-state transitions through the runtime stack."),
        ],
        instructor_notes=[
            "Students often treat robustness as a vague aspiration. Force specificity by requiring every reported failure to be labeled as noise, shift, calibration failure, OOD exposure, or monitor design failure.",
            "The most useful exercises ask learners to choose an intervention threshold and defend it with data. This converts uncertainty from theory into an operational decision rule.",
        ],
        readiness="A reader is ready to leave the chapter when they can distinguish disturbance classes, compute calibration diagnostics, choose an OOD score, and explain how a monitor uses these signals to alter behavior.",
        takeaway="Robustness is a runtime property. The right question is not whether uncertainty exists, but whether it is detected, calibrated, and turned into safer control decisions.",
        refs=[
            ('Kendall, A., and Gal, Y. "What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?" (2017). <a href="https://arxiv.org/abs/1703.04977" rel="noopener" target="_blank">https://arxiv.org/abs/1703.04977</a>', "A useful distinction between aleatoric and epistemic uncertainty that transfers well to embodied perception."),
            ('Ovadia, Y. et al. "Can You Trust Your Model’s Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift." (2019). <a href="https://arxiv.org/abs/1906.02530" rel="noopener" target="_blank">https://arxiv.org/abs/1906.02530</a>', "A strong reference for calibration collapse under shift."),
            ('Amodei, D. et al. "Concrete Problems in AI Safety." (2016). <a href="https://arxiv.org/abs/1606.06565" rel="noopener" target="_blank">https://arxiv.org/abs/1606.06565</a>', "Still useful for framing monitoring and intervention problems."),
            ('Official ROS 2 diagnostics and observability documentation.', "Use current runtime tooling docs for deployment interfaces and monitor-state implementation details."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html": index_block(
        chapter_number="54",
        chapter_title="Safety in Embodied AI",
        epigraph="Safety is the discipline of deciding which actions your system is never allowed to improvise.",
        cite="A Runtime Safety Architect",
        big_picture="Chapter 54 moves from generic caution to explicit safety engineering. Hazards, constraints, barrier functions, shields, overrides, and assurance arguments are treated as first-class parts of the embodied stack.",
        insight="Safety claims are credible only when they define the operating domain, the forbidden states and actions, the intervention authority, and the evidence that shows the system respected those limits.",
        overview=[
            "This chapter builds a layered view of safety: hazard analysis, constrained optimization, formal safety envelopes, runtime shields, human override, and deployment approval. The goal is to show how learned policies fit inside a larger assurance architecture.",
            "The theory thread spans constrained Markov decision processes, control barrier functions, Hamilton-Jacobi reachability, and assurance cases. The implementation thread focuses on monitors, intervention latency, override protocols, and release gates.",
            "Readers should know basic control, uncertainty-aware evaluation, and deployment logging. Chapter 37 on controllers, Chapter 52 on evaluation, and Chapter 53 on robustness are the main prerequisites.",
        ],
        roadmap_items=[
            ("54.1", "Why embodied safety is different (physical harm)", "Translate model errors into hazards, severity, exposure, and controllability."),
            ("54.2", "Constraint violations and safe exploration", "Learn under constraints without treating violations as ordinary exploration noise."),
            ("54.3", "Control barrier functions and Hamilton-Jacobi reachability", "Compute formal safe sets and action corrections around a learned policy."),
            ("54.4", "Shielded policies and safety filters", "Place runtime supervisors between policy output and actuator command."),
            ("54.5", "Human override and safety testing", "Design intervention interfaces and evidence-producing test campaigns."),
            ("54.6", "Deployment approval and safety cases", "Build release gates, residual-risk narratives, and operational restrictions."),
            ("54.7", "Safety Cases And Assurance Arguments For Embodied AI", "Turn the whole chapter into a structured assurance artifact."),
        ],
        tooling_note="Use small hand-built examples to make the constraints visible, then move to CBF solvers, reachability tools, hazard logs, runtime supervisors, and assurance templates. The shortcut matters because safety logic must be inspectable, testable, and maintainable under change.",
        lab_objective="Wrap one embodied policy with a simple safety monitor, a safety filter, and an operator override path. Produce one release dossier containing the task envelope, hazard log, test evidence, and residual risk summary.",
        lab_steps=[
            "Write an operational design domain or site card before policy tuning begins.",
            "Specify at least one hard state constraint, one action-rate constraint, and one emergency-stop path.",
            "Implement a simple safety filter or barrier-style correction around the nominal controller.",
            "Run nominal, degraded-sensing, near-boundary, and override tests on the same panel.",
            "Assemble a safety case summary that names evidence, defeaters, and residual risks.",
        ],
        next_text='Continue with <a href="section-54.1.html">Section 54.1: Why embodied safety is different (physical harm)</a>, where the chapter starts with hazards rather than metrics.',
        production_notes=[
            "Read this chapter from the outside in: start with the operating domain, then inspect the forbidden states and actions, then move inward to the learning or planning algorithm. That order reflects how real safety reviews are run.",
            "A credible safety artifact links hazard analysis, intervention authority, runtime monitoring, and replayable test evidence. Missing any one of these usually means the claimed safety property is only conceptual.",
            "Extend the lab by asking a second reader to challenge the safety case with a new defeater. If the evidence folder cannot answer the challenge, the assurance argument is still immature.",
        ],
        tool_rows=[
            ("Hazard logs and FMEA tables", "Track hazards, causes, mitigations, owners, and verification evidence."),
            ("CBF or QP-based safety filters", "Project unsafe actions back into an admissible control set."),
            ("Reachability tooling", "Approximate safe sets and worst-case envelopes for simplified dynamics."),
            ("ROS 2 lifecycle and safety nodes", "Route intervention logic outside ordinary policy code paths."),
            ("Assurance case templates", "Tie claims, evidence, and defeaters into a reviewable release dossier."),
        ],
        instructor_notes=[
            "Students often overfocus on the learning algorithm. Repeatedly bring them back to action authority: who can veto a command, how quickly, and based on which signals.",
            "The best projects in this chapter are small but rigorous. A simple robot with a real hazard log and a tested override path teaches more than a large policy with no safety evidence.",
        ],
        readiness="Before leaving the chapter, the reader should be able to define an operating domain, map hazards to mitigations, write a barrier-style safety condition, explain shield behavior, and assemble an assurance argument.",
        takeaway="Safety in embodied AI is not a final patch. It is the architecture that constrains action, routes intervention, and turns deployment into a reviewable evidence package.",
        refs=[
            ('Ames, A. D. et al. "Control Barrier Function Based Quadratic Programs for Safety Critical Systems." (2017). <a href="https://arxiv.org/abs/1609.06408" rel="noopener" target="_blank">https://arxiv.org/abs/1609.06408</a>', "A core reference for barrier-function-based safety filters."),
            ('Fisac, J. F. et al. "General Safety and Control of Autonomous Systems: A Hamilton-Jacobi Reachability-Based Approach." (2019). <a href="https://arxiv.org/abs/1810.07406" rel="noopener" target="_blank">https://arxiv.org/abs/1810.07406</a>', "Useful for safe set reasoning and worst-case analysis."),
            ('Wabersich, K. P. et al. "Safe Reinforcement Learning Using Probabilistic Shields." (2023). <a href="https://arxiv.org/abs/2210.00746" rel="noopener" target="_blank">https://arxiv.org/abs/2210.00746</a>', "A modern reference on shielding strategies around learned policies."),
            ('UL 4600 overview and related assurance guidance.', "A practical anchor for release gates and structured safety cases."),
        ],
    ),
}


SECTION_CONTENT = {
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.1.html": section_block(
        number="52.1",
        title="Why accuracy is not enough",
        chapter_title="Evaluating Embodied Systems",
        epigraph="A robot can classify the scene perfectly and still drive into the wrong next action.",
        cite="A Closed-Loop Experimentalist",
        figure_html="""
<figure class="illustration">
<img alt="Illustration of an evaluation dashboard where a high perception score coexists with timeout, collision, and energy penalties." loading="lazy" src="images/chapter-52-illustration-01.png"/>
<figcaption><strong>Figure 52.1.1</strong>: This section begins with the core mismatch: a system can look accurate at one stage while failing as a closed-loop embodied agent.</figcaption>
</figure>
<figure class="technical-figure">
<svg aria-labelledby="fig-52-1-title fig-52-1-desc" role="img" viewBox="0 0 840 280">
<title id="fig-52-1-title">Closed-loop utility versus stage accuracy</title>
<desc id="fig-52-1-desc">A diagram showing perception accuracy feeding into state estimation, policy action, monitor intervention, and final task utility.</desc>
<rect x="30" y="90" width="120" height="70" rx="8" fill="#e6f2ff" stroke="#2b6cb0"/>
<text x="90" y="118" text-anchor="middle" font-size="14">Perception</text>
<text x="90" y="138" text-anchor="middle" font-size="12">accuracy</text>
<rect x="200" y="90" width="120" height="70" rx="8" fill="#edfdf3" stroke="#2f855a"/>
<text x="260" y="118" text-anchor="middle" font-size="14">State</text>
<text x="260" y="138" text-anchor="middle" font-size="12">estimate</text>
<rect x="370" y="90" width="120" height="70" rx="8" fill="#fff6e8" stroke="#c05621"/>
<text x="430" y="118" text-anchor="middle" font-size="14">Policy</text>
<text x="430" y="138" text-anchor="middle" font-size="12">action</text>
<rect x="540" y="90" width="120" height="70" rx="8" fill="#fff1f1" stroke="#c53030"/>
<text x="600" y="118" text-anchor="middle" font-size="14">Monitor</text>
<text x="600" y="138" text-anchor="middle" font-size="12">intervention</text>
<rect x="700" y="70" width="110" height="110" rx="8" fill="#f7fafc" stroke="#4a5568"/>
<text x="755" y="110" text-anchor="middle" font-size="14">Utility</text>
<text x="755" y="132" text-anchor="middle" font-size="12">success, time,</text>
<text x="755" y="150" text-anchor="middle" font-size="12">energy, safety</text>
<path d="M150 125 H200 M320 125 H370 M490 125 H540 M660 125 H700" stroke="#2d3748" stroke-width="2"/>
</svg>
<figcaption><strong>Figure 52.1.2</strong>: Accuracy is only one upstream input. The deployment claim is made on utility after the whole loop, including monitor intervention, has run.</figcaption>
</figure>
""",
        big_picture="Embodied evaluation starts from the fact that task value is produced by a closed loop, not by a single predictor. Accuracy can improve while latency, safety violations, and failed recoveries make the overall robot worse.",
        pathway="Read this section in three passes: first identify the stage metric that looks attractive, then ask what downstream behavior it changes, then ask which same-panel artifact proves the claimed improvement survives contact with the world.",
        sections=[
            "In an embodied system, the useful question is not whether a perception or policy submodule has a high scalar score. The useful question is whether the full loop reaches goals faster, more safely, and more reproducibly under the same rollout panel.",
            "A compact utility model is $$J = \\mathbb{{E}}[\\mathbb{{1}}\\{{\\text{{success}}\\}} - \\lambda_v V - \\lambda_t T - \\lambda_e E - \\lambda_r R],$$ where $V$ counts violations, $T$ is completion time, $E$ is resource or energy cost, and $R$ counts recoveries or rescues. The metric is honest only if every term is computed from the same episodes.",
            "The diagram matters because it shows exactly where isolated accuracy can disappear: state estimation can be stale, action selection can be slow, and monitors can intervene often enough to erase any upstream gain.",
            "<li>Freeze a task panel with explicit initial states, perturbations, and reset rules.</li><li>Run the closed loop, not only the predictor, and log action timestamps, monitor states, and termination causes.</li><li>Aggregate success, violations, time, energy, and recovery into one utility table.</li><li>Compare methods only on paired episodes or a fixed seed schedule.</li><li>Inspect failure traces before celebrating any utility improvement.</li>",
            "A pick-and-place policy can improve grasp-point classification from 88 percent to 93 percent, yet lower the final task score because it now pauses longer before actuation and triggers more timeout recoveries.",
            "When teams say accuracy is not enough, the real scientific claim is that the stage metric is not construct-matched to the deployment objective. The cure is not to discard accuracy, but to embed it inside a utility table that also sees timing, control, and intervention.",
            "A common postmortem pattern is that the high-scoring method moved the error to a later stage: better detection, worse pose estimate; better pose estimate, slower planning; better planning, more aggressive actions. Closed-loop artifacts reveal where the gain leaked away.",
            'It connects backward to <a href="../../part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/index.html">Chapter 12 on task suites</a>, anticipates <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.2.html">Section 52.2 on multi-objective metrics</a>, and points forward to <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/index.html">Chapter 53 on uncertainty</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">Chapter 54 on safety</a>.',
            "Create an episode table for one embodied task with columns for `success`, `time_s`, `energy_j`, `violation_count`, and `recovery_count`. Add one model change that improves an upstream score, then verify whether the total utility also improves.",
        ],
        code="""from dataclasses import dataclass\n\n@dataclass\nclass Episode:\n    success: int\n    violations: int\n    time_s: float\n    energy_j: float\n    recoveries: int\n\n\ndef utility(ep: Episode,\n            lambda_v: float = 4.0,\n            lambda_t: float = 0.02,\n            lambda_e: float = 0.005,\n            lambda_r: float = 0.5) -> float:\n    return (\n        ep.success\n        - lambda_v * ep.violations\n        - lambda_t * ep.time_s\n        - lambda_e * ep.energy_j\n        - lambda_r * ep.recoveries\n    )\n\nbaseline = Episode(success=1, violations=0, time_s=16.0, energy_j=38.0, recoveries=0)\naccurate_but_slow = Episode(success=1, violations=0, time_s=29.0, energy_j=52.0, recoveries=1)\n\nprint({\n    \"baseline_utility\": round(utility(baseline), 3),\n    \"accurate_but_slow_utility\": round(utility(accurate_but_slow), 3),\n})""",
        code_output="""{'baseline_utility': 0.49, 'accurate_but_slow_utility': -0.34}""",
        code_caption="Code Fragment 52.1.1 compares two successful episodes under one utility contract, showing that a slower, recovery-heavy policy can lose despite identical task success.",
        expected_output="The two episodes both succeed, but the second receives a lower utility because extra delay, energy use, and one recovery consume the apparent gain. That is the signature of a stage metric that is not sufficient on its own.",
        shortcut="The hand-built utility is about 20 lines. In practice, a benchmark runner can stream episode traces into Pandas, MLflow, or Weights and Biases Artifacts so the same utility contract is computed automatically for every rollout while preserving the raw evidence.",
        warning="Do not compare a perception accuracy number from one task distribution with a utility score from another. Once the panels diverge, the comparison stops being an evaluation and becomes a story.",
        example="For a warehouse mobile manipulator, the deployment review should compare utility across matched pallets, aisle widths, battery states, and operator reset rules. A model that localizes objects better but demands more interventions does not earn promotion.",
        frontier="Recent embodied benchmarks increasingly log videos, monitor traces, and action latency beside scalar task scores. The open problem is to make these richer artifacts easy to aggregate without losing comparability.",
        self_check="Can you state one case where success rate stayed constant while the overall utility changed sign? If not, the difference between stage metrics and closed-loop value is not yet solid.",
        takeaway="Accuracy is a diagnostic input, not the deployment objective. The real claim lives in a same-panel utility table that includes success, violations, delay, energy, and recovery.",
        exercise="Take one embodied benchmark you know well and design a utility function that would demote a policy that succeeds often but needs frequent human rescue or burns excessive time.",
        next_text='Section 52.2 keeps the same matched-panel discipline and asks how to combine success, path quality, time, and energy into a more interpretable score.',
        refs=[
            ('Henderson, P. et al. "Deep Reinforcement Learning that Matters." (2018). <a href="https://arxiv.org/abs/1709.06560" rel="noopener" target="_blank">https://arxiv.org/abs/1709.06560</a>', "A reminder that seemingly better stage metrics often disappear under careful end-to-end evaluation."),
            ('Sutton, R. S., and Barto, A. G. "Reinforcement Learning: An Introduction." (2018). <a href="http://incompleteideas.net/book/the-book-2nd.html" rel="noopener" target="_blank">http://incompleteideas.net/book/the-book-2nd.html</a>', "Useful background for reward, utility, and rollout-based assessment."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.2.html": eval_section(
        number="52.2",
        title="Success rate, path efficiency, time and energy cost",
        image="chapter-52-illustration-02.png",
        figure_caption="A multi-objective scorecard for a mobile robot makes it obvious that two equally successful policies can have very different path quality and power cost.",
        big_picture="Embodied evaluation needs vector metrics because time, path length, smoothness, and energy all compete under fixed task success. This section shows how to keep those quantities interpretable without hiding tradeoffs.",
        formula="One useful representation is the episode score vector $$m_i = [s_i,\\; \\rho_i,\\; t_i,\\; e_i],$$ with $s_i$ for success, $\\rho_i = d^*_i / d_i$ for path efficiency, $t_i$ for completion time, and $e_i$ for energy. A scalar summary is acceptable only after the vector is logged and inspectable.",
        key_insight="Path efficiency and energy cost should remain visible as separate columns even if the benchmark publishes one scalar rank. Otherwise teams optimize the weighted sum while reviewers lose the tradeoff surface.",
        algorithm_items=[
            "Compute shortest-feasible reference distance or nominal task budget before running candidate methods.",
            "Record actual path length, action count, elapsed time, and energy or torque proxy for every episode.",
            "Normalize each quantity against a baseline or physical reference when cross-task aggregation is needed.",
            "Report both the raw vector and any scalarized utility.",
            "Audit whether the scalar ranking changes under small weight perturbations.",
        ],
        worked_example="A quadruped navigation policy may tie the baseline on success rate but use 30 percent more turning and 18 percent more battery because it oscillates in narrow passages. A scalar success metric would never show the regression.",
        code="""episodes = [\n    {\"success\": 1, \"optimal_path_m\": 8.0, \"actual_path_m\": 9.0, \"time_s\": 21.5, \"energy_j\": 440.0},\n    {\"success\": 1, \"optimal_path_m\": 8.0, \"actual_path_m\": 11.6, \"time_s\": 28.2, \"energy_j\": 590.0},\n]\n\nsummary = []\nfor ep in episodes:\n    path_eff = ep[\"optimal_path_m\"] / ep[\"actual_path_m\"]\n    summary.append({\n        \"success\": ep[\"success\"],\n        \"path_efficiency\": round(path_eff, 3),\n        \"time_s\": ep[\"time_s\"],\n        \"energy_j\": ep[\"energy_j\"],\n    })\n\nprint(summary)""",
        code_output="""[{'success': 1, 'path_efficiency': 0.889, 'time_s': 21.5, 'energy_j': 440.0}, {'success': 1, 'path_efficiency': 0.69, 'time_s': 28.2, 'energy_j': 590.0}]""",
        code_caption="Code Fragment 52.2.1 logs success with path efficiency, completion time, and energy so two successful runs remain distinguishable.",
        expected_output="Both episodes succeed, but the second is visibly less efficient, slower, and more expensive. That is the point: success rate should not erase operational cost.",
        shortcut="Once the vector definition is stable, use a benchmark dataframe plus MLflow or Weights and Biases tables to compute per-task and aggregate summaries automatically. The important part is that the raw vector remains accessible.",
        deep_dive="Scalarization is a policy decision, not a law of nature. Different applications weight speed, smoothness, and energy differently, so good benchmark design publishes the underlying vector and documents any chosen weights.",
        failure="When teams overcompress these metrics, they often rediscover hidden regressions late in deployment, especially thermal issues, battery drain, and route oscillations that were invisible in success-only dashboards.",
        cross_refs='This section links back to <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">Chapter 7 on control-oriented costs and tradeoffs</a> and forward to <a href="section-52.4.html">Section 52.4 on robustness metrics</a>, where the same vector idea is extended across perturbation families.',
        lab="Instrument one navigation or manipulation task with path efficiency and energy proxy. Then perturb controller gains and verify whether the tradeoff surface changes even when success stays flat.",
        warning="Do not compute path efficiency against a reference planner that quietly violates the robot's kinematic or dynamic limits. The denominator must be a feasible reference, not a fantasy route.",
        example="For autonomous driving, this metric vector can include route completion, jerk, delay, and energy. For drones, swap path efficiency for trajectory deviation and power draw. The structure stays the same while the physics changes.",
        frontier="Recent embodied benchmarks are moving toward Pareto-front reporting and scenario-conditioned scorecards, especially for fleets where battery, heat, and wear matter as much as mission completion.",
        self_check="Can you explain why a benchmark should publish both the metric vector and the scalar rank? If not, you are still trusting the aggregation more than the evidence.",
        takeaway="Success rate is the entry ticket, not the whole evaluation. Path efficiency, time, and energy reveal whether the robot succeeded in a deployable way.",
        exercise="Choose one embodied task and design a feasible reference path or action budget. Then define a vector metric and one scalar utility, and explain which tradeoffs the scalar hides.",
        next_text="Section 52.3 adds hard constraints to this vector view by asking not just how efficiently the robot moved, but whether it remained inside the allowed envelope.",
        refs=[
            ('Paden, B. et al. "A Survey of Motion Planning and Control Techniques for Self-Driving Urban Vehicles." (2016). <a href="https://arxiv.org/abs/1604.07446" rel="noopener" target="_blank">https://arxiv.org/abs/1604.07446</a>', "A useful reference for trajectory quality and control-oriented evaluation quantities."),
            ('Official robot benchmarking and fleet telemetry documentation for the platform under study.', "Use platform-native energy, thermal, or power interfaces rather than guessed proxies when possible."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.3.html": eval_section(
        number="52.3",
        title="Safety violations and constraint satisfaction",
        image="chapter-52-illustration-03.png",
        figure_caption="A constraint-aware evaluation view highlights forbidden states, action-rate limits, and intervention counts alongside ordinary task outcome.",
        big_picture="Embodied systems operate inside hard or soft constraints: collision margins, force limits, speed caps, no-go zones, thermal budgets, and human-separation rules. Evaluation is incomplete if these are not measured explicitly.",
        formula="A common constraint statistic is the satisfaction rate $$C = 1 - \\frac{1}{N}\\sum_{i=1}^{N}\\mathbb{1}\\{\\exists t: g(x_{i,t}, u_{i,t}) < 0\\},$$ where $g(x,u) \\ge 0$ defines the allowed set. For soft constraints, also log the violation magnitude and duration.",
        key_insight="Constraint satisfaction is not a detail added after task scoring. It changes which episodes count as acceptable and often changes which baseline should be considered competitive at all.",
        algorithm_items=[
            "State every hard and soft constraint in measurable units before running the benchmark.",
            "Log the first violation time, maximum violation magnitude, and total time outside the safe set.",
            "Distinguish near-boundary episodes from true violations so threshold tuning can be audited.",
            "Aggregate per-constraint statistics before merging them into a chapter-level summary.",
            "Pair every violation with a replay artifact and causal postmortem label.",
        ],
        worked_example="A manipulator that completes a cabinet-opening task in 95 percent of trials but exceeds wrist torque limits in 8 percent of them is not simply 'slightly worse'. It violates a deployment gate.",
        code="""samples = [\n    {\"clearance_cm\": 12.0, \"speed_mps\": 0.7},\n    {\"clearance_cm\": 4.0, \"speed_mps\": 0.8},\n    {\"clearance_cm\": 9.5, \"speed_mps\": 1.3},\n]\n\nviolations = []\nfor s in samples:\n    v = {\n        \"clearance_violation\": s[\"clearance_cm\"] < 8.0,\n        \"speed_violation\": s[\"speed_mps\"] > 1.0,\n    }\n    violations.append(v)\n\nprint(violations)""",
        code_output="""[{'clearance_violation': False, 'speed_violation': False}, {'clearance_violation': True, 'speed_violation': False}, {'clearance_violation': False, 'speed_violation': True}]""",
        code_caption="Code Fragment 52.3.1 evaluates two explicit constraints per sample, which is the minimum structure needed to discuss constraint satisfaction clearly.",
        expected_output="The output separates clearance and speed failures instead of collapsing them into one vague unsafe label. That separation is what supports diagnosis and mitigation.",
        shortcut="In production, constraint evaluation belongs in the controller or monitor stack, with alerts exported into the benchmark artifact. The maintained tools save you from hand-parsing timestamps and threshold crossings after the fact.",
        deep_dive="Constraint tables often reveal that two models with similar utility differ sharply in safety profile. One may violate rarely but severely, while another grazes boundaries often without crossing them. Both patterns matter.",
        failure="A common failure pattern is to count only whether a violation happened, not how long it lasted or how large it became. That throws away the information needed for risk ranking and controller redesign.",
        cross_refs='This section sets up <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.2.html">Section 54.2 on safe exploration</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.3.html">Section 54.3 on barrier functions</a>, where constraint satisfaction moves from measurement to enforcement.',
        lab="Define two hard constraints and one soft constraint for an existing embodied task. Run a panel, compute satisfaction rate, maximum violation, and time-outside-safe-set, then inspect the worst episode replay.",
        warning="Do not average all violations into one severity-free percentage when the underlying hazards have different consequences. A minor workspace excursion and a force spike on a human-contact surface should not carry the same semantic weight.",
        example="For a delivery robot, relevant constraints include pedestrian clearance, maximum cornering speed, and stop-distance budget. The benchmark should tell you which one failed first and how close nominal runs operate to the boundary.",
        frontier="Open problems include combining learned uncertainty with formal constraints, calibrating near-boundary warnings, and deciding which soft constraint violations are acceptable during adaptation or exploration.",
        self_check="Can you list one hard constraint, one soft constraint, and one severity field you would log for your platform? If not, the safety envelope is still underspecified.",
        takeaway="Constraint satisfaction turns evaluation into an operational review. The benchmark must say whether the robot stayed inside the allowed envelope, not just whether it reached the goal.",
        exercise="Take a benchmark you know and rewrite its success definition so any hard-constraint violation marks the episode unacceptable. Explain how that changes the leaderboard logic.",
        next_text="Section 52.4 extends this constraint-aware view into robustness by asking how performance degrades under shift, perturbation, and worst-case tails.",
        refs=[
            ('Ames, A. D. et al. "Control Barrier Function Based Quadratic Programs for Safety Critical Systems." (2017). <a href="https://arxiv.org/abs/1609.06408" rel="noopener" target="_blank">https://arxiv.org/abs/1609.06408</a>', "Useful background for thinking about measurable constraint sets."),
            ('Koopman, P., and Wagner, M. "Challenges in Autonomous Vehicle Safety." (2017). <a href="https://arxiv.org/abs/1705.01284" rel="noopener" target="_blank">https://arxiv.org/abs/1705.01284</a>', "A reminder that safety evaluation depends on explicit operational constraints."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.4.html": eval_section(
        number="52.4",
        title="Robustness and generalization metrics",
        image="chapter-52-illustration-04.png",
        figure_caption="A perturbation panel separates clean performance from shifted performance and worst-case tail behavior.",
        big_picture="Nominal average return is only one slice of evaluation. Embodied systems also need shift-sensitive, worst-case, and outlier-aware metrics because the world does not sample only clean conditions.",
        formula="A compact robustness report can include the clean score $J_{clean}$, the mean shifted score $J_{shift}$, and the tail-risk statistic $$\\text{CVaR}_{\\alpha}(L) = \\mathbb{E}[L \\mid L \\ge q_{\\alpha}],$$ where $L$ is loss and $q_{\\alpha}$ is the upper-tail quantile. This keeps average and worst-case behavior visible together.",
        key_insight="Generalization is not a single number. It has at least three faces: interpolation to new task instances, robustness to nuisance perturbations, and behavior under truly out-of-support states.",
        algorithm_items=[
            "Partition the rollout panel into clean, interpolated, shifted, and stress-test slices.",
            "Compute average performance on each slice and a tail-risk statistic on the hardest slice.",
            "Report confidence intervals per slice, not only globally.",
            "Store enough metadata to recreate which perturbation family produced each tail event.",
            "Rank models only after checking whether one model's gain is just a clean-slice artifact.",
        ],
        worked_example="Two drone policies can tie on average mission success while differing dramatically on gust-heavy scenes. The difference may only appear in the worst decile of episodes, which is why tail metrics matter.",
        code="""losses = [0.1, 0.2, 0.25, 0.3, 0.35, 0.9, 1.1, 1.4]\nalpha = 0.75\nthreshold_index = int(alpha * len(losses))\nq_alpha = sorted(losses)[threshold_index]\ntail = [x for x in losses if x >= q_alpha]\ncvar = sum(tail) / len(tail)\nprint({\"q_alpha\": q_alpha, \"cvar\": round(cvar, 3), \"tail_count\": len(tail)})""",
        code_output="""{'q_alpha': 0.9, 'cvar': 1.133, 'tail_count': 3}""",
        code_caption="Code Fragment 52.4.1 computes a simple tail-risk summary so the worst perturbation outcomes remain visible beside average scores.",
        expected_output="The output identifies the tail threshold and the mean of the worst episodes. A large gap between average loss and CVaR signals brittle behavior hidden by nominal aggregates.",
        shortcut="Use a dataframe pipeline plus SciPy or NumPy quantile utilities for production analysis. The important part is not the software, but that clean, shifted, and tail slices are all computed from the same stored episodes.",
        deep_dive="Embodied robustness work benefits from treating perturbation families as experimental factors. Lighting shift, texture shift, actuation delay, and friction change should each have their own slice before they are rolled into an aggregate robustness view.",
        failure="A common benchmark error is to mix interpolation and true OOD states into one bucket called generalization. That makes it impossible to tell whether the model fails because of modest novelty or because the state is physically outside the training support.",
        cross_refs='This section prepares the ground for <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.1.html">Section 53.1 on disturbance classes</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.3.html">Section 53.3 on OOD detection</a>.',
        lab="Take one existing evaluation table and split it into clean, shifted, and stress-test slices. Add a CVaR column and compare whether the method ranking changes.",
        warning="Do not declare a model robust because it survived one handpicked perturbation family. Robustness claims require coverage across perturbation classes and disclosure of where the model remains weak.",
        example="For a humanoid locomotion controller, clean floors, mild friction changes, and severe friction drops should appear as separate rows. The right policy may be worse on average but far safer in the tail.",
        frontier="Current research is moving toward richer perturbation taxonomies, compositional shift panels, and benchmark artifacts that keep the perturbation generator itself versioned and auditable.",
        self_check="Can you distinguish the average shifted score from a tail-risk statistic like CVaR? If not, your robustness vocabulary is still too coarse.",
        takeaway="Generalization metrics should preserve clean, shifted, and worst-case structure. One average score is rarely enough for embodied deployment decisions.",
        exercise="Define a robustness report for one robot task with at least three perturbation families and one tail metric. Explain which deployment question each slice answers.",
        next_text="Section 52.5 now asks when simulation can stand in for physical evaluation and what evidence is needed to justify that proxy.",
        refs=[
            ('Ovadia, Y. et al. "Can You Trust Your Model’s Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift." (2019). <a href="https://arxiv.org/abs/1906.02530" rel="noopener" target="_blank">https://arxiv.org/abs/1906.02530</a>', "A helpful bridge between shift evaluation and calibrated uncertainty."),
            ('Agarwal, R. et al. "Deep Reinforcement Learning at the Edge of the Statistical Precipice." (2021). <a href="https://arxiv.org/abs/2108.13264" rel="noopener" target="_blank">https://arxiv.org/abs/2108.13264</a>', "Useful for careful metric aggregation and confidence intervals."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.5.html": eval_section(
        number="52.5",
        title="Reproducible evaluation: SIMPLER and sim-as-proxy",
        image="chapter-52-illustration-05.png",
        figure_caption="A sim-to-real evaluation ladder shows how simulator panels can be useful proxies when their limits are named rather than ignored.",
        big_picture="Simulation is valuable because it is cheap, repeatable, and broad. It is dangerous when teams forget that proxy quality is itself a hypothesis that must be tested against physical evidence.",
        formula="Let $S$ be the simulator score and $R$ the real-world score over matched tasks. A practical proxy check is the fidelity gap $$\\Delta = \\left|\\mathbb{E}[S] - \\mathbb{E}[R]\\right|$$ plus a rank correlation between methods over the same task panel. A low average gap without rank preservation is still a weak proxy.",
        key_insight="A simulator is not validated by looking plausible. It is validated when the same ranking, failure modes, or sensitivity trends survive on the matched real panel often enough to support the intended decision.",
        algorithm_items=[
            "Define which decision the simulator proxy is supposed to support, such as model ranking, hyperparameter filtering, or failure-mode search.",
            "Construct a matched sim and real panel with aligned task definitions and artifact schema.",
            "Compute mean gaps, ranking stability, and overlap in failure taxonomy.",
            "Document where the simulator is trustworthy and where it is only exploratory.",
            "Re-check the proxy whenever the robot hardware, perception stack, or environment distribution changes materially.",
        ],
        worked_example="A simulator may preserve policy ranking on tabletop grasping but fail to preserve contact-rich insertion errors because friction and compliance are mis-modeled. That makes it a good filter for broad candidate screening but a weak final judge for insertion policies.",
        code="""sim_scores = {\"A\": 0.84, \"B\": 0.76, \"C\": 0.72}\nreal_scores = {\"A\": 0.68, \"B\": 0.70, \"C\": 0.61}\nranking_sim = sorted(sim_scores, key=sim_scores.get, reverse=True)\nranking_real = sorted(real_scores, key=real_scores.get, reverse=True)\nmean_gap = round(sum(abs(sim_scores[k] - real_scores[k]) for k in sim_scores) / len(sim_scores), 3)\nprint({\"ranking_sim\": ranking_sim, \"ranking_real\": ranking_real, \"mean_gap\": mean_gap})""",
        code_output="""{'ranking_sim': ['A', 'B', 'C'], 'ranking_real': ['B', 'A', 'C'], 'mean_gap': 0.11}""",
        code_caption="Code Fragment 52.5.1 compares simulator and real rankings directly, making proxy failure visible even when the mean gap looks moderate.",
        expected_output="The proxy loses trust here because the best simulator method is not the best real-world method. The mean gap alone would miss that decision-level failure.",
        shortcut="SIMPLER-style infrastructure, benchmark manifests, and replay artifacts help because they enforce matched schemas across simulation and real execution. The library advantage is standardization, not magic transfer.",
        deep_dive="The strongest simulator proxy claims are narrow and explicit. A simulator might be trusted for policy ranking within one morphology and camera setup, but not for fleet-wide energy forecasting or human-interaction safety.",
        failure="A common failure mode is to treat a proxy as universally valid after one early correlation result. Proxy validity is local to task family, hardware configuration, and decision type.",
        cross_refs='This section connects backward to <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html">Chapter 20 on sim-to-real transfer</a> and forward to <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.6.html">Section 52.6 on benchmark hygiene</a>.',
        lab="Take three candidate policies, evaluate them in simulation and on a small real panel, and compute both mean score gap and ranking agreement. Then write one paragraph naming which decision the simulator can support reliably.",
        warning="Do not use simulator-only confidence intervals to justify real-world deployment approval. Proxy evidence can prioritize tests, but it cannot replace the tests whose outcome it is only trying to predict.",
        example="For autonomous driving, CARLA may be strong for regression testing and scenario replay but incomplete for real sensor contamination or rare human behavior. For manipulation, MuJoCo or Isaac may screen policies well while missing subtle compliance errors.",
        frontier="The frontier is richer simulator realism plus better validity auditing: not just more realistic scenes, but better methods for measuring which conclusions transfer and which do not.",
        self_check="Can you state one decision for which your simulator is trustworthy and one for which it is not? If not, the proxy contract is still too vague.",
        takeaway="Sim-as-proxy is a scientific claim about decision support. It earns trust through matched panels, explicit fidelity gaps, and repeated checks against real evidence.",
        exercise="Choose one simulator you use. Define the decision it is meant to support, the matched real panel needed to test that claim, and the failure signal that would invalidate the proxy.",
        next_text="Section 52.6 closes the chapter by moving from metric design to benchmark governance, protocol control, and real-world evaluation hygiene.",
        refs=[
            ('Official SIMPLER and related benchmark resources.', "Use the project artifacts to see how matched simulator and real evaluation can share manifests and replay structure."),
            ('Todorov, E., Erez, T., and Tassa, Y. "MuJoCo: A physics engine for model-based control." (2012). <a href="https://mujoco.org/" rel="noopener" target="_blank">https://mujoco.org/</a>', "A central simulator lineage for embodied control research."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.6.html": eval_section(
        number="52.6",
        title="Real-world evaluation hygiene; benchmark design",
        image="chapter-52-illustration-01.png",
        figure_caption="A physical benchmark protocol includes reset rules, operator instructions, calibration checks, and audit trails, not only task labels.",
        big_picture="Real-world embodied evaluation is vulnerable to operator effects, wear, reset quality, battery drift, calibration drift, and post-hoc reruns. Good benchmark design makes these confounders explicit and controllable.",
        formula="For paired comparisons, one simple estimator is the mean episode difference $$\\bar{d} = \\frac{1}{N}\\sum_{i=1}^{N}(y_i^{A} - y_i^{B}),$$ with a bootstrap or paired confidence interval over matched episodes. Matching is the whole point: without it, even the statistics are answering the wrong question.",
        key_insight="Benchmark design is about experimental control. The best metric script cannot rescue a protocol that lets methods see different resets, different hardware health, or different operator discretion.",
        algorithm_items=[
            "Pre-register the task panel, hardware checklist, reset protocol, and abort criteria.",
            "Block or randomize operator, battery level, and environment ordering where feasible.",
            "Log every rerun and every exclusion with a reason code.",
            "Use paired or blocked analysis whenever two methods share the same task instances.",
            "Publish enough artifact detail that another lab could rerun the protocol without guessing.",
        ],
        worked_example="Suppose one manipulation policy is tested early in the day on a newly calibrated camera while another is tested after lens smudging and battery sag. Without protocol control, the benchmark is measuring the lab schedule as much as the policy.",
        code="""results = [\n    {\"task_id\": 1, \"A\": 1, \"B\": 0},\n    {\"task_id\": 2, \"A\": 1, \"B\": 1},\n    {\"task_id\": 3, \"A\": 0, \"B\": 0},\n    {\"task_id\": 4, \"A\": 1, \"B\": 0},\n]\npaired_diffs = [row[\"A\"] - row[\"B\"] for row in results]\nmean_diff = sum(paired_diffs) / len(paired_diffs)\nprint({\"paired_differences\": paired_diffs, \"mean_difference\": round(mean_diff, 3)})""",
        code_output="""{'paired_differences': [1, 0, 0, 1], 'mean_difference': 0.5}""",
        code_caption="Code Fragment 52.6.1 computes paired task differences, the basic object behind matched-panel significance analysis.",
        expected_output="The paired difference vector keeps task identity alive. That lets you ask whether method A won on the same tasks, not merely whether its separate average looked larger.",
        shortcut="Protocol automation matters here: DVC for manifest versioning, ROS 2 bags for raw trace capture, and experiment trackers for run metadata. The tooling keeps the hygiene burden from collapsing into unreviewed manual notes.",
        deep_dive="Strong embodied benchmarks behave more like experimental science than like casual demos. They specify inclusion criteria, rerun policy, calibration cadence, environment reset instructions, and how anomalous episodes are handled.",
        failure="The most damaging benchmark failure is silent protocol drift: lighting changes, operator habits, robot wear, or policy-specific reruns that are not recorded. Once drift is silent, the scoreboard cannot be trusted.",
        cross_refs='This closing section ties back to <a href="../../part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/index.html">Chapter 12 on task suite construction</a> and forward to <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html">Chapter 55 on deployment architecture</a>, where evaluation artifacts become part of release infrastructure.',
        lab="Write a one-page benchmark protocol for a small embodied task. Include operator instructions, rerun policy, hardware checklist, calibration cadence, and paired-analysis plan, then ask a second reader to identify loopholes.",
        warning="Do not discard difficult episodes after seeing the results unless the exclusion rule was written in advance and applies symmetrically to all methods.",
        example="A benchmark for drones might block by battery freshness and wind condition. A benchmark for humanoid locomotion might block by floor condition and operator reset crew. These are not administrative details; they are causal variables.",
        frontier="The field still needs better benchmark governance: audit logs for physical tests, standardized rerun policies, and richer public failure-case reporting that does not collapse into marketing.",
        self_check="Can another lab rerun your benchmark from the artifact package alone? If the answer is no, the evaluation is not yet reproducible enough.",
        takeaway="Real-world evaluation hygiene is the discipline that makes leaderboard claims scientifically interpretable instead of operationally mysterious.",
        exercise="Audit a public embodied benchmark or one from your lab. List three protocol variables that could drift silently and propose how to freeze or log them.",
        next_text="Chapter 53 picks up the story from the disturbance side, asking how to measure and use uncertainty before those benchmark failures become deployment incidents.",
        refs=[
            ('Agarwal, R. et al. "Deep Reinforcement Learning at the Edge of the Statistical Precipice." (2021). <a href="https://arxiv.org/abs/2108.13264" rel="noopener" target="_blank">https://arxiv.org/abs/2108.13264</a>', "A strong reminder to pair careful statistics with careful evaluation design."),
            ('Official MLflow, DVC, and ROS 2 logging documentation.', "Practical references for building auditable evaluation pipelines."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.1.html": robustness_section(
        number="53.1",
        title="What goes wrong: sensor noise, distribution shift",
        image="chapter-53-illustration-01.png",
        figure_caption="A disturbance map separates noise, occlusion, latency, and full distribution shift so the repair path becomes explicit.",
        big_picture="Robustness starts by refusing to call every failure 'brittleness'. Sensor noise, timestamp drift, actuation delay, novel objects, and environment shift have different signatures and different fixes.",
        formula="A simple disturbance decomposition is $$y_t = h(x_t) + \\epsilon_t, \\qquad x_t \\sim p_{train}(x) \\;\\text{or}\\; p_{deploy}(x),$$ where $\\epsilon_t$ captures observation corruption and the change from $p_{train}$ to $p_{deploy}$ captures distribution shift. Different corrective actions target these two terms.",
        key_insight="If the disturbance source is mislabeled, the mitigation often makes the system worse. You do not fix missing depth frames with more policy regularization, and you do not fix unseen object classes with a timestamp smoother.",
        algorithm_items=[
            "Label perturbations by channel: observation corruption, state-estimation drift, action delay, or environment shift.",
            "Measure outcome degradation under each channel separately before composing them.",
            "Record whether the first visible symptom appears in perception, state estimation, planning, or control.",
            "Attach each failure to a replay artifact with the disturbance label in metadata.",
            "Choose mitigations after the disturbance label is stable across multiple episodes.",
        ],
        worked_example="A mobile robot that misses docking targets under motion blur needs either sensor robustness or slower approach speeds. The same failure under dropped timestamps points toward synchronization, not representation learning.",
        code="""disturbances = [\n    {\"label\": \"motion_blur\", \"success\": 0, \"state_error_cm\": 4.2},\n    {\"label\": \"depth_dropout\", \"success\": 0, \"state_error_cm\": 13.9},\n    {\"label\": \"novel_texture\", \"success\": 1, \"state_error_cm\": 6.4},\n]\n\nsummary = {}\nfor row in disturbances:\n    summary[row[\"label\"]] = {\n        \"success\": row[\"success\"],\n        \"state_error_cm\": row[\"state_error_cm\"],\n    }\n\nprint(summary)""",
        code_output="""{'motion_blur': {'success': 0, 'state_error_cm': 4.2}, 'depth_dropout': {'success': 0, 'state_error_cm': 13.9}, 'novel_texture': {'success': 1, 'state_error_cm': 6.4}}""",
        code_caption="Code Fragment 53.1.1 records disturbance labels beside outcome and state error, making channel-specific diagnosis possible.",
        expected_output="The output shows that two failures share task failure but not the same internal signature. The depth-dropout episode has a far larger state error, which points toward a different repair path.",
        shortcut="Observation wrappers, ROS diagnostics, and sensor-injection utilities make it easy to build repeatable perturbation panels once the disturbance taxonomy is defined clearly.",
        deep_dive="Embodied robustness work improves when failure categories are causal rather than cosmetic. Label the disturbance by what physically changed, not only by how the image looked or whether the policy failed.",
        failure="The most common mistake is to aggregate all shifted scenes into one bucket. That hides whether the problem is sensor corruption, timing, morphology mismatch, or a new semantic object class.",
        cross_refs='This section ties back to <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/section-52.4.html">Section 52.4 on perturbation metrics</a> and leads to <a href="section-53.2.html">Section 53.2 on calibration</a> and <a href="section-53.3.html">Section 53.3 on OOD detection</a>.',
        lab="Create a disturbance panel with at least three channels, such as motion blur, missing depth frames, and unseen textures. For each failed rollout, record which channel was active and which internal variable drifted first.",
        warning="Do not call a disturbance distribution shift if it is really a logging or synchronization bug. Robustness experiments become misleading when infrastructure failures are mislabeled as model limitations.",
        example="For autonomous driving, rain may degrade perception while route closure introduces semantic shift. For drones, wind gusts act through dynamics while glare acts through sensing. The diagnostic matrix should reflect that distinction.",
        frontier="The field is starting to use richer perturbation ontologies and automatically generated stress suites, but good causal labeling still requires careful human judgment and replay review.",
        self_check="Can you name one perturbation that primarily affects sensing and one that primarily affects dynamics? If not, the disturbance taxonomy is still too flat.",
        takeaway="Robustness work begins with disturbance taxonomy. Different failure channels deserve different measurements and different fixes.",
        exercise="Take a recent embodied failure from your own work and relabel it by disturbance channel. Then propose one experiment that would falsify your diagnosis.",
        next_text="Section 53.2 asks how the robot should represent uncertainty once the disturbance source has been identified.",
        refs=[
            ('Kendall, A., and Gal, Y. "What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?" (2017). <a href="https://arxiv.org/abs/1703.04977" rel="noopener" target="_blank">https://arxiv.org/abs/1703.04977</a>', "Useful background for how disturbance channels interact with uncertainty types."),
            ('Official ROS 2 diagnostics documentation.', "Practical support for surfacing sensor-health and timing signals at runtime."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.2.html": robustness_section(
        number="53.2",
        title="Model uncertainty and calibration",
        image="chapter-53-illustration-02.png",
        figure_caption="A reliability diagram and confidence trace show that confidence must match empirical correctness, not just feel intuitive.",
        big_picture="Uncertainty estimates are useful only if they are calibrated enough to support action gating, planning fallbacks, or human alerts. This section separates uncertainty source from calibration quality.",
        formula="A standard calibration statistic is the expected calibration error $$\\mathrm{ECE} = \\sum_{b=1}^{B} \\frac{|S_b|}{n}\\, |\\mathrm{acc}(S_b) - \\mathrm{conf}(S_b)|,$$ where $S_b$ is the set of predictions whose confidence falls in bin $b$. In embodied systems, calibration should be evaluated on action-relevant predictions, not only class labels.",
        key_insight="An uncertainty signal can have the right ordering but the wrong scale. Calibration is what makes the scale actionable for a threshold, an intervention rule, or a planner cost.",
        algorithm_items=[
            "Choose the prediction interface that matters for action, such as grasp success probability or collision-free path confidence.",
            "Collect held-out or replayed episodes with prediction confidence and empirical outcome.",
            "Compute calibration summaries such as ECE, reliability bins, and threshold-conditioned precision.",
            "If needed, fit a calibration map on one panel and test it on a separate shifted panel.",
            "Use the calibrated confidence only if it remains stable under the deployment shifts you care about.",
        ],
        worked_example="A manipulation policy may be good at ranking candidate grasps yet still overclaim 0.95 confidence on cases that succeed only 0.70 of the time. A runtime gate built on that confidence will intervene too late.",
        code="""bins = [\n    {\"confidence\": 0.9, \"correct\": 1},\n    {\"confidence\": 0.8, \"correct\": 1},\n    {\"confidence\": 0.8, \"correct\": 0},\n    {\"confidence\": 0.6, \"correct\": 1},\n]\nacc = sum(x[\"correct\"] for x in bins) / len(bins)\nconf = sum(x[\"confidence\"] for x in bins) / len(bins)\nece = abs(acc - conf)\nprint({\"accuracy\": round(acc, 3), \"avg_confidence\": round(conf, 3), \"ece_like_gap\": round(ece, 3)})""",
        code_output="""{'accuracy': 0.75, 'avg_confidence': 0.775, 'ece_like_gap': 0.025}""",
        code_caption="Code Fragment 53.2.1 computes a simple calibration gap, the minimal signal needed before choosing a confidence threshold.",
        expected_output="The small gap here suggests the average scale is close, but a real evaluation would still inspect bins because cancellation can hide local miscalibration. Calibration is about the full reliability shape, not only the mean.",
        shortcut="Torchmetrics, scikit-learn calibration tools, MAPIE-style conformal wrappers, and reliability-diagram notebooks can automate reliability curves and threshold audits once the action-relevant prediction interface is defined.",
        deep_dive="In embodied systems, calibration must be tied to consequences. A poorly calibrated collision predictor and a poorly calibrated object classifier are not equally serious if only one gates a safety-critical maneuver. In practice, teams often compare temperature scaling, isotonic regression, and conformal intervals on the exact signal that drives a stop, reroute, or human-review threshold.",
        failure="A frequent failure is to calibrate on clean validation data and deploy on shifted scenes. The confidence scale then looks disciplined in the notebook and collapses in the field.",
        cross_refs='This section connects to <a href="section-53.3.html">Section 53.3 on OOD detection</a> and <a href="../module-54-safety-in-embodied-ai/section-54.4.html">Section 54.4 on shielded policies</a>, where calibrated thresholds become actual intervention logic.',
        lab="Log confidence and outcome for one embodied prediction task, compute a reliability diagram, then decide whether you trust a threshold to trigger degraded mode or human review.",
        warning="Do not calibrate confidence on a proxy metric that the action policy never uses. The only calibration that matters is the calibration of the signal tied to a real decision.",
        example="For a self-driving perception stack, calibration may matter most for occupancy or collision probability, not for semantic class labels that have no immediate control effect.",
        frontier="Open work includes sequence-level calibration, calibration for action distributions rather than labels, and joint calibration across planners, policies, and monitors in one control loop.",
        self_check="Can you explain why an accurate but miscalibrated confidence head can still be dangerous in deployment? If not, connect the threshold choice to a missed or false intervention.",
        takeaway="Calibration turns uncertainty from a descriptive score into a decision-support signal that can safely trigger thresholds and fallbacks.",
        exercise="Take one model output from your own stack and define how you would test whether its confidence is calibrated enough to drive a runtime threshold.",
        next_text="Section 53.3 continues by asking how to detect states that should not be trusted at all because they lie outside the supported distribution.",
        refs=[
            ('Guo, C. et al. "On Calibration of Modern Neural Networks." (2017). <a href="https://arxiv.org/abs/1706.04599" rel="noopener" target="_blank">https://arxiv.org/abs/1706.04599</a>', "A standard reference for calibration evaluation and post-hoc adjustment."),
            ('Ovadia, Y. et al. "Can You Trust Your Model’s Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift." (2019). <a href="https://arxiv.org/abs/1906.02530" rel="noopener" target="_blank">https://arxiv.org/abs/1906.02530</a>', "Calibration under shift is the real embodied challenge."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.3.html": robustness_section(
        number="53.3",
        title="Out-of-distribution detection",
        image="chapter-53-illustration-03.png",
        figure_caption="An OOD detector draws a boundary around known operating support and routes suspicious states toward caution or human review.",
        big_picture="OOD detection asks whether the current input or state belongs to the support on which the system was tuned and evaluated. In embodied settings, this matters because extrapolating silently can create physically irreversible mistakes.",
        formula="Given an OOD score $s(x)$, a detector triggers when $$s(x) > \\tau,$$ where $\\tau$ is chosen against a cost tradeoff between missed OOD events and unnecessary interventions. The right threshold depends on what action becomes available when the alert fires.",
        key_insight="OOD detection is not useful because it labels novelty abstractly. It is useful because it decides when to slow down, replan, switch sensors, or hand control to a safer subsystem.",
        algorithm_items=[
            "Choose an OOD score, such as energy, reconstruction error, distance in feature space, or conformal nonconformity.",
            "Build an in-support panel and at least one clearly out-of-support panel tied to deployment concerns.",
            "Measure false positive and false negative costs in action terms, not only in ROC space.",
            "Attach a behavior policy to the alert: degrade, stop, seek more information, or escalate to a human.",
            "Review false alarms to see whether the support definition is wrong or the score is too noisy.",
        ],
        worked_example="A warehouse robot that sees a reflective floor patch unlike anything in training should not continue as if the scene were ordinary. Even a blunt OOD alert can be valuable if it triggers a lower-speed navigation mode.",
        code="""scores = [0.12, 0.18, 0.22, 0.74, 0.81]\nthreshold = 0.5\nflags = [score > threshold for score in scores]\nprint({\"threshold\": threshold, \"flags\": flags, \"flag_rate\": sum(flags) / len(flags)})""",
        code_output="""{'threshold': 0.5, 'flags': [False, False, False, True, True], 'flag_rate': 0.4}""",
        code_caption="Code Fragment 53.3.1 applies a simple OOD threshold, illustrating the interface between score and intervention policy.",
        expected_output="Two states are flagged as OOD. The real question is what the robot does next, which is why the detector should always be evaluated together with its downstream intervention logic.",
        shortcut="Feature-space detectors, PyOD-style baseline suites, conformal wrappers, and replay dashboards reduce the friction of threshold sweeps and failure review. The detector still needs a task-specific cost model to be meaningful.",
        deep_dive="OOD signals are especially useful when paired with task context. A scene can be novel but harmless, or common-looking but dangerous because the action consequences are unusual. The detector should be interpreted through the active task and control state. In practice, teams often compare simple distance-based, energy-based, and reconstruction-based scores before promoting one score into the runtime monitor.",
        failure="The classic mistake is to report AUROC without defining the operational meaning of false alarms and misses. In deployment, the question is whether the alert changes behavior appropriately, not whether a curve looks elegant.",
        cross_refs='This section pairs naturally with <a href="section-53.4.html">Section 53.4 on runtime monitoring</a> and <a href="../module-54-safety-in-embodied-ai/section-54.1.html">Section 54.1 on embodied safety</a>, because OOD alerts often become one input to a broader safety supervisor.',
        lab="Choose one OOD score for a robot perception or planning state, define a threshold on a development panel, and inspect whether the resulting alerts would have prevented any previously observed failures.",
        warning="Do not evaluate OOD detectors on synthetic novelty only if your deployment failures come from timing, wear, or control mismatch. Novelty needs to be defined around the real support boundary that matters.",
        example="For drones, unfamiliar weather or lighting may be the relevant OOD family. For manipulation, unusual object compliance or unusual contact configuration may matter more than pixel novelty alone.",
        frontier="The frontier includes sequential OOD detection, active information gathering after novelty alerts, and joint novelty scores that combine perception, dynamics, and map uncertainty rather than treating each in isolation.",
        self_check="If your detector fires, what exact behavior changes? If the answer is vague, the detector is still an analytic curiosity rather than a deployment tool.",
        takeaway="OOD detection matters when it defines a boundary of trust and hands control to a safer behavior before silent extrapolation becomes damage.",
        exercise="Define an OOD notion for your platform and propose a threshold policy. Then describe one false alarm you would accept and one missed alarm you would consider unacceptable.",
        next_text="Section 53.4 closes the chapter by integrating uncertainty and OOD signals into runtime monitors and fail-safe state transitions.",
        refs=[
            ('Hendrycks, D., and Gimpel, K. "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks." (2017). <a href="https://arxiv.org/abs/1610.02136" rel="noopener" target="_blank">https://arxiv.org/abs/1610.02136</a>', "A foundational starting point for simple OOD scoring."),
            ('Liu, W. et al. "Energy-based Out-of-distribution Detection." (2020). <a href="https://arxiv.org/abs/2010.03759" rel="noopener" target="_blank">https://arxiv.org/abs/2010.03759</a>', "A widely used modern OOD score family."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/section-53.4.html": robustness_section(
        number="53.4",
        title="Runtime monitoring and fail-safe behavior",
        image="chapter-53-illustration-04.png",
        figure_caption="A runtime monitor moves the robot through normal, degraded, stop, and recovery modes based on health and uncertainty signals.",
        big_picture="Runtime monitoring turns robustness from an offline evaluation concept into an online control layer. A monitor observes health signals and decides when the nominal policy should lose authority.",
        formula="A simple health-state machine can be written as $$z_{t+1} = M(z_t, h_t),$$ where $z_t \\in \\{\\text{normal}, \\text{degraded}, \\text{stopped}, \\text{recovery}\\}$ and $h_t$ collects latency, uncertainty, sensor freshness, and constraint-margin signals. The deployment claim is about this state machine as much as about the policy itself.",
        key_insight="The monitor is useful only if it has authority to change behavior. Logging an alarm after a bad action is observability, not fail-safe control.",
        algorithm_items=[
            "Define the monitor inputs, such as confidence, sensor age, latency, and constraint margin.",
            "Set transitions between normal, degraded, stop, and recovery states.",
            "Specify what authority each state has over velocity, planning horizon, or human override.",
            "Test the transition latency on the same stress cases that motivated the monitor.",
            "Save every transition in the rollout artifact and review false triggers as carefully as missed triggers.",
        ],
        worked_example="A drone localization stream that goes stale should trigger hover or controlled landing within a bounded delay. The monitor has failed even if the postmortem log is perfect but the unsafe action already happened.",
        code="""state = \"normal\"\nhealth = [\n    {\"latency_ms\": 25, \"uncertainty\": 0.12},\n    {\"latency_ms\": 48, \"uncertainty\": 0.18},\n    {\"latency_ms\": 130, \"uncertainty\": 0.55},\n]\n\ntransitions = []\nfor h in health:\n    if h[\"latency_ms\"] > 100 or h[\"uncertainty\"] > 0.5:\n        state = \"stopped\"\n    elif h[\"latency_ms\"] > 40 or h[\"uncertainty\"] > 0.15:\n        state = \"degraded\"\n    transitions.append({\"health\": h, \"state\": state})\n\nprint(transitions)""",
        code_output="""[{'health': {'latency_ms': 25, 'uncertainty': 0.12}, 'state': 'normal'}, {'health': {'latency_ms': 48, 'uncertainty': 0.18}, 'state': 'degraded'}, {'health': {'latency_ms': 130, 'uncertainty': 0.55}, 'state': 'stopped'}]""",
        code_caption="Code Fragment 53.4.1 maps health signals to runtime states, illustrating the minimal interface behind a fail-safe monitor.",
        expected_output="The monitor first degrades behavior under moderate health drift and then stops under severe drift. That progression is the key design choice, not the exact threshold numbers.",
        shortcut="ROS 2 lifecycle nodes, Prometheus metrics, and OpenTelemetry traces help implement the monitor as a real system service rather than an afterthought buried in policy code.",
        deep_dive="Good monitors are designed as control authorities with explicit latency budgets. A monitor that decides correctly but too slowly still fails its deployment role.",
        failure="A recurrent mistake is to define degraded mode without specifying what actually degrades, such as speed cap, action horizon, sensing requirement, or human-supervision demand. Without that, degraded is just a label.",
        cross_refs='This section hands off naturally to <a href="../module-54-safety-in-embodied-ai/section-54.4.html">Section 54.4 on safety filters</a> and <a href="../module-54-safety-in-embodied-ai/section-54.5.html">Section 54.5 on human override</a>, where runtime authority becomes explicit.',
        lab="Implement a four-state monitor for one robot task, feed it uncertainty and latency signals, and replay at least one episode where the monitor should have intervened earlier than the nominal policy would have.",
        warning="Do not tune monitor thresholds only on clean logs. Stress cases and near-failures are the data that determine whether the monitor will matter in the field.",
        example="A delivery robot might enter degraded mode by lowering speed and requiring fresher localization, then stop entirely when map confidence collapses. A manipulator might shrink force limits and approach speed before requesting human review.",
        frontier="Research directions include learned runtime assurance, better fusion of heterogeneous health signals, and monitors that can actively seek information rather than only stopping or slowing.",
        self_check="Can you name the signals, thresholds, and authority change in each runtime state for your system? If not, your monitor is not specified tightly enough to test.",
        takeaway="Runtime monitoring is the bridge from uncertainty to safer behavior. Its quality is measured by the timeliness and correctness of its state transitions.",
        exercise="Design a runtime state machine for one embodied system and define the exact actions allowed in each state. Then identify one transition you would expect to be most fragile in deployment.",
        next_text="Chapter 54 now takes over by turning monitoring and intervention into a full safety architecture with hazards, formal envelopes, shields, and assurance cases.",
        refs=[
            ('Amodei, D. et al. "Concrete Problems in AI Safety." (2016). <a href="https://arxiv.org/abs/1606.06565" rel="noopener" target="_blank">https://arxiv.org/abs/1606.06565</a>', "Still helpful for the broader framing of interventions and monitoring."),
            ('Official ROS 2 lifecycle and diagnostics documentation.', "Useful implementation references for stateful runtime supervision."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.1.html": safety_section(
        number="54.1",
        title="Why embodied safety is different (physical harm)",
        image="chapter-54-illustration-01.png",
        figure_caption="A hazard map ties the same robot action to different consequences for people, equipment, and mission continuity.",
        big_picture="Embodied safety is different because mistakes become forces, impacts, blockages, spills, and near-misses in the physical world. The system must therefore reason about hazard severity and intervention authority, not only task reward.",
        formula="A common hazard-ranking surrogate is $$r = S \\times E \\times C,$$ where $S$ is severity, $E$ is exposure, and $C$ is uncontrollability or low controllability. This does not replace deeper methods like STPA or formal verification, but it disciplines the review.",
        key_insight="The same policy error can have trivial consequences in simulation and unacceptable consequences on hardware. Safety analysis therefore starts from harm pathways, not from model internals.",
        algorithm_items=[
            "List hazardous states and actions before choosing mitigation mechanisms.",
            "Rank each hazard by severity, exposure, and controllability.",
            "Attach each major hazard to a sensor, monitor, or override path that can detect or interrupt it.",
            "Define residual risk and restricted operating conditions explicitly.",
            "Save the hazard log together with rollout evidence and intervention traces.",
        ],
        worked_example="A service robot instructed to hurry through a corridor can remain task-optimal while becoming unsafe because it now violates human-clearance and stop-distance assumptions.",
        code="""hazards = [\n    {\"name\": \"pinch\", \"severity\": 5, \"exposure\": 2, \"controllability\": 2},\n    {\"name\": \"blocked_exit\", \"severity\": 4, \"exposure\": 3, \"controllability\": 3},\n]\nfor h in hazards:\n    h[\"risk_score\"] = h[\"severity\"] * h[\"exposure\"] * h[\"controllability\"]\nprint(hazards)""",
        code_output="""[{'name': 'pinch', 'severity': 5, 'exposure': 2, 'controllability': 2, 'risk_score': 20}, {'name': 'blocked_exit', 'severity': 4, 'exposure': 3, 'controllability': 3, 'risk_score': 36}]""",
        code_caption="Code Fragment 54.1.1 computes a simple hazard ranking so safety work begins with explicit harm pathways rather than vague concern.",
        expected_output="The blocked-exit hazard outranks the pinch hazard under this crude scheme because exposure and controllability are worse. The exact numbers are less important than making the ranking auditable and discussable.",
        shortcut="Hazard logs, FMEA tables, and structured ODD cards reduce the temptation to hold safety assumptions only in people’s heads. The maintained tools help because safety work is documentation and coordination as much as computation.",
        deep_dive="Safety reviews should ask what the robot can do physically, how quickly, around whom, and with which fallback. Those questions often reveal risks long before one reaches policy architecture details.",
        failure="A common failure is to treat safety as a final acceptance test. By then the interfaces, latency budgets, and intervention authority may already be too rigid to fix cheaply.",
        cross_refs='This section motivates <a href="section-54.2.html">Section 54.2 on constrained learning</a>, <a href="section-54.5.html">Section 54.5 on override testing</a>, and <a href="section-54.7.html">Section 54.7 on assurance arguments</a>.',
        lab="Write a small hazard log for one embodied task with five hazards, their rankings, detection paths, and residual-risk notes. Then identify which hazards the nominal policy cannot mitigate by itself.",
        warning="Do not confuse low probability with low consequence. Rare harms can still dominate the release decision when severity and uncontrollability are high.",
        example="For a warehouse robot, blocked aisles and blind-corner collisions may outrank many manipulation mistakes because they couple to human traffic and emergency movement.",
        frontier="Current work is trying to connect robot learning more tightly with classic safety engineering, so hazard analysis, runtime monitoring, and learned control share a common evidence language.",
        self_check="Can you name one hazard that comes from the environment and one that comes from the robot’s own action authority? If not, the safety analysis is still too generic.",
        takeaway="Embodied safety starts with harm pathways and intervention authority. Model quality matters, but hazards and mitigations define the release gate.",
        exercise="Take one embodied application and write three hazards that would remain even if the policy were more accurate. Then propose the mitigation layer for each.",
        next_text="Section 54.2 now asks how to learn or explore while respecting hard limits instead of treating violations as ordinary data collection.",
        refs=[
            ('Koopman, P., and Wagner, M. "Challenges in Autonomous Vehicle Safety." (2017). <a href="https://arxiv.org/abs/1705.01284" rel="noopener" target="_blank">https://arxiv.org/abs/1705.01284</a>', "A useful systems view of safety as more than model accuracy."),
            ('UL 4600 overview. <a href="https://users.ece.cmu.edu/~koopman/ul4600/index.html" rel="noopener" target="_blank">https://users.ece.cmu.edu/~koopman/ul4600/index.html</a>', "A practical assurance anchor for autonomous-system release arguments."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.2.html": safety_section(
        number="54.2",
        title="Constraint violations and safe exploration",
        image="chapter-54-illustration-02.png",
        figure_caption="Safe exploration surrounds the nominal learning loop with constraint counters, intervention rules, and budget accounting.",
        big_picture="Learning in the physical world cannot treat collisions, dangerous forces, or boundary crossings as just another negative reward sample. Safe exploration introduces hard or probabilistic limits that the learner must respect while still gathering information.",
        formula="A constrained Markov decision process writes the objective as $$\\max_\\pi J_R(\\pi) \\quad \\text{subject to} \\quad J_{C_k}(\\pi) \\le d_k, \\; k=1,\\dots,K,$$ where each $J_{C_k}$ is an expected safety cost and $d_k$ is the allowed budget.",
        key_insight="If violations are genuinely unacceptable, they cannot be left to the optimizer to trade away implicitly. They need explicit budgets, shields, or action filters.",
        algorithm_items=[
            "Define safety costs and hard constraints separately from task reward.",
            "Set allowable budgets or zero-tolerance rules before data collection.",
            "Choose the intervention layer: supervisor, safety filter, human operator, or reset routine.",
            "Log every exploratory violation attempt, even if the supervisor blocks it.",
            "Use postmortems to refine the safe set rather than only penalizing the agent numerically.",
        ],
        worked_example="A mobile manipulator learning to reach around clutter may need to try unfamiliar approaches, but it should not be allowed to ram a shelf just because the reward eventually penalizes contact.",
        code="""trajectory = [\n    {\"state\": \"nominal\", \"safety_cost\": 0.0},\n    {\"state\": \"near_boundary\", \"safety_cost\": 0.4},\n    {\"state\": \"blocked_by_filter\", \"safety_cost\": 1.0},\n]\nbudget = 1.0\nused = sum(step[\"safety_cost\"] for step in trajectory)\nprint({\"budget\": budget, \"used\": used, \"within_budget\": used <= budget})""",
        code_output="""{'budget': 1.0, 'used': 1.4, 'within_budget': False}""",
        code_caption="Code Fragment 54.2.1 treats safety cost as a constrained resource rather than an afterthought hidden inside reward shaping.",
        expected_output="The trajectory exceeds the exploration safety budget. In a real system that should trigger supervisor action, tighter reset policy, or the end of the current training run.",
        shortcut="Constrained RL libraries, safety wrappers, and supervisor nodes help enforce budgets and log blocked actions. The value is not only algorithmic, it is that every blocked action becomes inspectable evidence.",
        deep_dive="Safe exploration should be understood as allocation of risk during learning. Even when a violation is blocked, the attempted violation still teaches you where the current policy wants to go and where the safe set may be underspecified.",
        failure="The main failure is to turn a hard safety requirement into a soft reward penalty because that makes the optimizer appear simpler. In physical systems, the simplicity is fake and the risk is real.",
        cross_refs='This section leads naturally to <a href="section-54.3.html">Section 54.3 on barrier functions</a> and <a href="section-54.4.html">Section 54.4 on shielded policies</a>, where constraints gain direct action-level enforcement.',
        lab="Wrap one exploration policy with a safety budget and a blocking rule. Log every attempted unsafe action and compare the nominal learning curve to the blocked-action trace.",
        warning="Do not report safe exploration results without the blocked-attempt statistics. A method that looks safe only because a supervisor silently intercepted many dangerous actions is telling an incomplete story if the interceptions are hidden.",
        example="For drones, safe exploration may mean geofence and velocity envelopes during policy learning. For humanoids, it may mean fall-risk constraints and torque or joint-rate limits.",
        frontier="Open problems include scalable constrained RL for contact-rich tasks, better online safe-set expansion, and principled use of human teleoperators inside exploration loops.",
        self_check="Can you distinguish a safety budget, a hard constraint, and a blocked action event in your logs? If not, your exploration evidence is probably too coarse.",
        takeaway="Safe exploration means learning under explicit risk controls. Violations are evidence to analyze, not acceptable tuition fees.",
        exercise="Design a CMDP-style formulation for one embodied learning problem. Name the reward, at least two safety costs, one hard limit, and the supervisor that would enforce it.",
        next_text="Section 54.3 moves from constrained objectives to explicit safe-set enforcement with control barrier functions and reachability methods.",
        refs=[
            ('García, J., and Fernández, F. "A Comprehensive Survey on Safe Reinforcement Learning." (2015). <a href="https://jmlr.org/papers/v16/garcia15a.html" rel="noopener" target="_blank">https://jmlr.org/papers/v16/garcia15a.html</a>', "A broad survey framing constrained learning problems."),
            ('Wabersich, K. P. et al. "Safe Reinforcement Learning Using Probabilistic Shields." (2023). <a href="https://arxiv.org/abs/2210.00746" rel="noopener" target="_blank">https://arxiv.org/abs/2210.00746</a>', "A modern perspective on guarding exploration with explicit safety layers."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.3.html": safety_section(
        number="54.3",
        title="Control barrier functions and Hamilton-Jacobi reachability",
        image="chapter-54-illustration-03.png",
        figure_caption="A safe-set picture shows the nominal policy trying to exit the admissible region while the safety layer projects the command back inside.",
        big_picture="Control barrier functions and reachability methods give formal language for safe sets. They do not solve every robotics problem, but they provide a disciplined way to define when nominal actions must be corrected or rejected.",
        formula="For a control-affine system $\\dot{x}=f(x)+g(x)u$, a control barrier function $h(x)$ enforces the safe set $\\mathcal{S}=\\{x: h(x) \\ge 0\\}$ through the inequality $$\\nabla h(x)^{\\top}(f(x)+g(x)u) + \\alpha(h(x)) \\ge 0.$$ Hamilton-Jacobi reachability instead reasons about a value function whose superlevel set marks states from which safety can still be guaranteed.",
        key_insight="A barrier or reachability layer is valuable because it speaks directly in state and action geometry. It says which commands keep safety recoverable, regardless of whether the nominal controller came from optimization, imitation, or a foundation model.",
        algorithm_items=[
            "Choose a reduced dynamics model and define the safe state set in coordinates that matter physically.",
            "Construct a barrier condition or reachable safe set that can be evaluated online.",
            "Given a nominal action, solve a correction step that finds the nearest admissible command.",
            "Log both the nominal and corrected actions for later audit.",
            "Validate the approximation limits, because safe-set claims are only as good as the model used to derive them.",
        ],
        worked_example="A mobile robot commanded toward a human workspace can have its velocity projected onto a safe half-space that preserves clearance, even if the nominal planner wanted a more aggressive turn.",
        code="""x = {\"distance_m\": 0.55, \"velocity_mps\": 0.8}\nclearance = 0.5\nalpha = 1.0\nh = x[\"distance_m\"] - clearance\nlhs_nominal = -x[\"velocity_mps\"] + alpha * h\nu_corrected = min(x[\"velocity_mps\"], alpha * h)\nprint({\"h\": round(h, 3), \"lhs_nominal\": round(lhs_nominal, 3), \"u_corrected\": round(u_corrected, 3)})""",
        code_output="""{'h': 0.05, 'lhs_nominal': -0.75, 'u_corrected': 0.05}""",
        code_caption="Code Fragment 54.3.1 shows a one-dimensional barrier-style correction: the nominal speed violates the condition, so the filter projects it down to an admissible value.",
        expected_output="The negative nominal left-hand side indicates the command would leave the safe set too aggressively. The corrected control restores feasibility, which is the practical role of a barrier filter.",
        shortcut="CBF and QP solvers, plus reachability toolchains, save substantial derivation and numerical work. Small filters are often prototyped with cvxpy and OSQP, while reachability studies rely on dedicated level-set or hj_reachability-style workflows once the reduced model is fixed.",
        deep_dive="These methods work best when the safety set can be expressed in low-dimensional coordinates that are updated reliably at runtime. They become brittle when the state estimate is poor or the reduced model hides important contact or delay effects. A practical workflow is to prototype the barrier inequality in a notebook, validate it in replay, and only then move the filter into the runtime controller path.",
        failure="The dangerous mistake is to assume a formal safe-set proof transfers unchanged when the perception stack, latency profile, or actuation limits change. The proof depends on the deployed interface, not only on the math on paper.",
        cross_refs='This section connects back to <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">Chapter 7 on control design</a> and forward to <a href="section-54.4.html">Section 54.4 on shielded policies</a>, where these corrections become part of a larger runtime supervisor.',
        lab="Implement a tiny barrier filter for a 1D or 2D toy robot, then log nominal and corrected actions under near-boundary states. Inspect which states generate repeated corrections.",
        warning="Do not claim more safety than the reduced dynamics model can support. Barrier and reachability methods are powerful, but only inside the modeling assumptions they actually enforce.",
        example="For autonomous driving, a barrier can enforce headway or lane boundary margins. For drones, it may enforce altitude and obstacle separation. For manipulators, it may enforce joint, speed, or force limits.",
        frontier="Current research is expanding barrier methods to uncertainty-aware, learned-dynamics, and multi-agent settings, but the challenge remains to keep the guarantees meaningful under real sensing and delay.",
        self_check="Can you say what your safe set is, in state variables, without mentioning the controller implementation? If not, the barrier idea is still too abstract.",
        takeaway="Barrier and reachability methods matter because they define when nominal intelligence must yield to explicit safety geometry.",
        exercise="Define a safe set for one embodied platform, write the corresponding barrier condition or reachable-state description, and identify which state estimate errors would undermine the guarantee most.",
        next_text="Section 54.4 widens the lens from geometric corrections to general shielded policies and runtime safety filters around learned agents.",
        refs=[
            ('Ames, A. D. et al. "Control Barrier Function Based Quadratic Programs for Safety Critical Systems." (2017). <a href="https://arxiv.org/abs/1609.06408" rel="noopener" target="_blank">https://arxiv.org/abs/1609.06408</a>', "A core barrier-function reference."),
            ('Fisac, J. F. et al. "General Safety and Control of Autonomous Systems: A Hamilton-Jacobi Reachability-Based Approach." (2019). <a href="https://arxiv.org/abs/1810.07406" rel="noopener" target="_blank">https://arxiv.org/abs/1810.07406</a>', "A strong introduction to reachability-based safety reasoning."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.4.html": safety_section(
        number="54.4",
        title="Shielded policies and safety filters",
        image="chapter-54-illustration-04.png",
        figure_caption="A shield sits between policy output and actuator command, vetoing or modifying unsafe proposals before they reach hardware.",
        big_picture="A shielded policy architecture separates nominal competence from intervention authority. The policy proposes an action; the shield checks whether that action is admissible under current state, rules, and monitor status.",
        formula="A simple safety filter solves $$u_t^{safe} = \\arg\\min_{u \\in \\mathcal{U}_{safe}(x_t)} \\|u - u_t^{nom}\\|^2,$$ which keeps the deployed command close to the nominal proposal while forcing it to remain inside the safe action set.",
        key_insight="The shield is not a post-hoc penalty. It is a runtime contract that explicitly decides when the policy’s authority ends.",
        algorithm_items=[
            "Define the nominal action interface and the safe action set in the same coordinates and units.",
            "Evaluate the nominal command against geometric, probabilistic, or rule-based safety checks.",
            "Project, replace, or veto the command when it leaves the admissible set.",
            "Log nominal action, safe action, veto reason, and monitor state together.",
            "Audit the veto distribution to see whether the underlying policy is learning unsafe tendencies or whether the filter is too conservative.",
        ],
        worked_example="A language-conditioned mobile manipulator may suggest a long reach through a crowded area. The shield can cap speed, reroute motion primitives, or require confirmation instead of trusting the proposal directly.",
        code="""nominal = {\"vx\": 0.8, \"vy\": 0.0}\nlimits = {\"vx_max\": 0.4, \"vy_max\": 0.2}\nsafe = {\n    \"vx\": max(min(nominal[\"vx\"], limits[\"vx_max\"]), -limits[\"vx_max\"]),\n    \"vy\": max(min(nominal[\"vy\"], limits[\"vy_max\"]), -limits[\"vy_max\"]),\n}\nprint({\"nominal\": nominal, \"safe\": safe, \"intervened\": nominal != safe})""",
        code_output="""{'nominal': {'vx': 0.8, 'vy': 0.0}, 'safe': {'vx': 0.4, 'vy': 0.0}, 'intervened': True}""",
        code_caption="Code Fragment 54.4.1 applies a simple projection-style shield by clipping an unsafe velocity command into the admissible set.",
        expected_output="The shield preserves the command direction but reduces its magnitude to stay within the allowed envelope. The boolean intervention flag is crucial for later audit and policy improvement.",
        shortcut="Safety wrappers, controller-side filters, and runtime supervisors provide reusable infrastructure for shield logic. The point of the maintained stack is consistency and auditability, not just shorter code.",
        deep_dive="A good shield produces two kinds of value. First, it prevents immediate unsafe action. Second, it generates a dataset of vetoed proposals that tells you where the nominal policy is systematically misaligned with safe behavior.",
        failure="One major failure mode is to deploy a shield whose safe-action coordinates do not match the policy output coordinates. Unit mismatches and stale transforms can make the filter appear active while still letting unsafe commands through.",
        cross_refs='This section connects naturally to <a href="section-54.3.html">Section 54.3 on barrier-based corrections</a> and <a href="section-54.5.html">Section 54.5 on override testing</a>.',
        lab="Wrap a simple nominal controller with a projection filter, then log how often the filter intervenes under nominal and stress-test panels. Decide whether the underlying policy needs retraining or the filter needs redesign.",
        warning="Do not evaluate shielded systems using only final safe actions. Without the nominal command log, you cannot tell whether the policy itself is becoming safer or whether the shield is doing all the work.",
        example="For a drone, a shield may clip velocity near no-fly boundaries. For a manipulator, it may project a pose command into a joint-safe or force-safe subspace. For autonomous driving, it may veto accelerations that violate a rule set.",
        frontier="The frontier includes probabilistic shields, learned safe-set approximations, and filters that reason jointly about intent uncertainty, constraints, and human preferences.",
        self_check="Can you describe one situation where the shield should modify the action and one where it should fully veto it? If not, the intervention policy is still underspecified.",
        takeaway="Shielded policies work because they formalize the boundary between nominal intelligence and enforced safety authority.",
        exercise="Design a shield for one embodied action interface. Specify the nominal command, safe set, modification rule, veto rule, and the logs you would save after every intervention.",
        next_text="Section 54.5 shifts from automatic safety intervention to human override paths and the test campaigns that prove they work under pressure.",
        refs=[
            ('Alshiekh, M. et al. "Safe Reinforcement Learning via Shielding." (2018). <a href="https://ojs.aaai.org/index.php/AAAI/article/view/11741" rel="noopener" target="_blank">https://ojs.aaai.org/index.php/AAAI/article/view/11741</a>', "A classic shielded-RL reference."),
            ('Wabersich, K. P. et al. "Safe Reinforcement Learning Using Probabilistic Shields." (2023). <a href="https://arxiv.org/abs/2210.00746" rel="noopener" target="_blank">https://arxiv.org/abs/2210.00746</a>', "A modern update on shielding strategies under uncertainty."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.5.html": safety_section(
        number="54.5",
        title="Human override and safety testing",
        image="chapter-54-illustration-05.png",
        figure_caption="Override controls, alert paths, and test matrices matter because the final safety layer is often a human or operator team with finite reaction time.",
        big_picture="Human override is part of the safety architecture, not an embarrassing backup plan. If the system depends on people to recover from uncertain states, the interface and latency of that intervention must be designed and tested explicitly.",
        formula="One useful statistic is the mean time to intervention $$\\mathrm{MTTI} = \\frac{1}{N}\\sum_{i=1}^{N}(t_i^{override} - t_i^{hazard}),$$ paired with a success-after-override rate. Override quality is about both speed and whether the system enters a truly safe state afterward.",
        key_insight="A human override path that exists on paper but is hard to trigger under cognitive load is not a real mitigation. Safety testing has to include the operator as part of the system.",
        algorithm_items=[
            "Specify who can override, through which interface, and under what authority transitions.",
            "Measure the time from hazard onset to alert, to operator awareness, to override completion, and to safe-state confirmation.",
            "Test override during realistic workload, not only in calm scripted demos.",
            "Record false alarms, missed alerts, and confusing interface states.",
            "Update training, interface, and autonomy boundaries based on observed intervention failures.",
        ],
        worked_example="A teleoperated humanoid may have an emergency stop button, but if the operator cannot tell which control mode is active or whether the button was accepted, the mitigation is weaker than it appears in a requirements sheet.",
        code="""events = [\n    {\"hazard_s\": 10.2, \"override_s\": 11.1, \"safe_state_s\": 11.9},\n    {\"hazard_s\": 22.5, \"override_s\": 24.0, \"safe_state_s\": 25.8},\n]\nmetrics = []\nfor e in events:\n    metrics.append({\n        \"override_delay_s\": round(e[\"override_s\"] - e[\"hazard_s\"], 2),\n        \"safe_state_delay_s\": round(e[\"safe_state_s\"] - e[\"hazard_s\"], 2),\n    })\nprint(metrics)""",
        code_output="""[{'override_delay_s': 0.9, 'safe_state_delay_s': 1.7}, {'override_delay_s': 1.5, 'safe_state_delay_s': 3.3}]""",
        code_caption="Code Fragment 54.5.1 measures both operator reaction and safe-state confirmation delay, which are distinct quantities in override testing.",
        expected_output="The second event reaches safe state much later even though override still occurred. That distinction matters because override authority is only half the story; the platform must also settle safely.",
        shortcut="Structured test matrices, HIL setups, ROS 2 telemetry, and interface event logs make human override tests reproducible instead of anecdotal.",
        deep_dive="Safety testing should include degraded sensing, workload, ambiguous alerts, and repeated interventions. Otherwise the operator interface may look robust only because the test removed the stress that makes it fail.",
        failure="A common failure is to measure emergency-stop latency but not verify the achieved state. Some platforms accept the override command quickly yet continue coasting, swinging, or drifting long enough to remain unsafe.",
        cross_refs='This section supports <a href="section-54.6.html">Section 54.6 on deployment approval</a> and <a href="section-54.7.html">Section 54.7 on assurance cases</a>, because override evidence often becomes part of the release dossier.',
        lab="Run a tabletop or simulated override campaign with at least three hazard types. Measure alert timing, operator reaction, safe-state timing, and post-intervention confusion or recovery quality.",
        warning="Do not treat operator training as a substitute for interface design. If the interface hides mode, state, or acknowledgment, no amount of training fully repairs the architecture.",
        example="In autonomous vehicles, the challenge may be takeover requests and driver state. In warehouse robots, it may be which worker has authority to stop or restart. In drones, it may be RC fallback or return-to-home confirmation under poor connectivity.",
        frontier="Important open questions include shared autonomy under uncertainty, better alert design under workload, and safety testing that captures real operator cognition instead of idealized lab reactions.",
        self_check="Can you name the full chain from hazard onset to safe-state confirmation for your system? If not, the override path is not testable yet.",
        takeaway="Human override is part of embodied control. It deserves timing budgets, interface design, and evidence just as much as the policy itself.",
        exercise="Design an override test matrix for one embodied platform. Include at least three hazard types, one workload manipulation, and the metrics you would report to a release board.",
        next_text="Section 54.6 assembles these safety layers into deployment approval gates and structured safety cases.",
        refs=[
            ('NHTSA Voluntary Safety Self-Assessment. <a href="https://www.nhtsa.gov/automated-driving-systems/voluntary-safety-self-assessment" rel="noopener" target="_blank">https://www.nhtsa.gov/automated-driving-systems/voluntary-safety-self-assessment</a>', "A practical reference for operational safety evidence and human factors discussion."),
            ('FAA Remote ID and UAS safety guidance. <a href="https://www.faa.gov/uas" rel="noopener" target="_blank">https://www.faa.gov/uas</a>', "Useful deployment-facing references for intervention and operational control expectations."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.6.html": safety_section(
        number="54.6",
        title="Deployment approval and safety cases",
        image="chapter-54-illustration-01.png",
        figure_caption="Deployment approval requires more than a successful demo: it needs a bounded operating domain, evidence map, and named residual risks.",
        big_picture="Deployment approval is the point where all previous sections meet. The team must decide whether the operating domain is bounded, the mitigations are in place, the evidence is sufficient, and the residual risk is acceptable for the intended use.",
        formula="A simple approval tuple is $$A = (\\mathrm{ODD}, \\mathrm{evidence}, \\mathrm{defeaters}, \\mathrm{residual\\ risk}, \\mathrm{rollback}),$$ where every element must be explicit enough for an external reviewer or internal safety board to challenge. Many teams then arrange this tuple in a goal-structuring tree so each top-level release claim has child claims, evidence links, and explicit challenge conditions.",
        key_insight="Approval is not a scalar threshold. It is a structured argument that says which evidence supports which claim and what conditions would invalidate the release.",
        algorithm_items=[
            "Freeze the operating domain, excluded cases, and authority boundaries.",
            "Assemble evidence from evaluation panels, monitor tests, override tests, hazard analysis, and trace matrices.",
            "Map each release claim to one or more concrete artifacts in a goal-structuring or assurance template.",
            "List defeaters, missing evidence, and residual risks explicitly, with named owners.",
            "Define rollback, disablement, and post-deployment monitoring plans, then approve only for the claimed domain.",
        ],
        worked_example="A delivery robot may be approved for indoor daytime office routes with marked lanes and trained operators, but not for crowded public spaces or unstructured loading docks. Approval is domain-bounded by design.",
        code="""approval = {\n    \"odd_defined\": True,\n    \"evidence_complete\": False,\n    \"override_tested\": True,\n    \"residual_risk_named\": True,\n}\napproval[\"release_ready\"] = all(approval.values())\nprint(approval)""",
        code_output="""{'odd_defined': True, 'evidence_complete': False, 'override_tested': True, 'residual_risk_named': True, 'release_ready': False}""",
        code_caption="Code Fragment 54.6.1 encodes a minimal release gate, showing that one missing evidence block can and should block approval.",
        expected_output="The release is blocked because the evidence set is incomplete. That is exactly how a safety gate should behave: incomplete evidence is itself a meaningful decision signal.",
        shortcut="Assurance templates, hazard logs, experiment trackers, and Goal Structuring Notation style review packets help teams assemble release evidence consistently. The goal is not paperwork for its own sake, but traceable linkage between claims and evidence.",
        deep_dive="Good approval practice names the boundary conditions clearly. A system can be approved for one environment, one workload, or one operator model without implying readiness everywhere else. In mature programs, each approval claim is backed by a trace matrix that points to benchmark artifacts, monitor tests, override results, and the exact owner for unresolved residual risks.",
        failure="One of the most dangerous approval failures is domain creep, where a system slowly begins operating outside the bounded domain because no one wrote the exclusions sharply enough or monitored them after release.",
        cross_refs='This section sets up the capstone logic of <a href="section-54.7.html">Section 54.7 on assurance arguments</a> and prepares the transition to <a href="../module-55-deployment-architecture/index.html">Chapter 55 on deployment architecture</a>.',
        lab="Create a mock release packet for a small embodied system with an ODD card, hazard log, evaluation summary, override evidence, and one blocked release reason. Then ask whether the packet really supports the intended domain.",
        warning="Do not let a passing benchmark substitute for an approval argument. Benchmarks are inputs to approval, not approval itself.",
        example="For autonomous vehicles, the ODD may be limited by weather, road class, and speed range. For manipulation in labs, it may be limited by object set, human proximity rules, and supervision level.",
        frontier="The field is still building shared norms for approval arguments around learning-enabled robots, especially where models update frequently and fleet telemetry changes the available evidence base after release.",
        self_check="Can you list the intended operating domain and the excluded domain for your system in one sentence each? If not, the approval boundary is probably too fuzzy.",
        takeaway="Deployment approval is a structured argument over bounded use, evidence sufficiency, and residual risk, not a celebration of one good demo.",
        exercise="Write a one-page approval gate for a robot system you know. Include explicit no-release conditions and one rollback trigger for post-deployment operation.",
        next_text="Section 54.7 turns approval logic into a full assurance argument with claims, evidence, defeaters, and replay artifacts.",
        refs=[
            ('UL 4600 overview. <a href="https://users.ece.cmu.edu/~koopman/ul4600/index.html" rel="noopener" target="_blank">https://users.ece.cmu.edu/~koopman/ul4600/index.html</a>', "A practical reference for structured autonomous-system safety arguments."),
            ('ISO 21448 SOTIF overview. <a href="https://www.iso.org/standard/77490.html" rel="noopener" target="_blank">https://www.iso.org/standard/77490.html</a>', "Relevant for performance limitations and intended-functionality hazards."),
        ],
    ),
    "part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/section-54.7.html": safety_section(
        number="54.7",
        title="Safety Cases And Assurance Arguments For Embodied AI",
        image="chapter-54-application-reference-7.png",
        figure_caption="A complete assurance case ties operating domain, claims, evidence, defeaters, and replay artifacts into one reviewable structure.",
        big_picture="A safety case is the structured object that tells reviewers why the robot is acceptably safe for a bounded operating domain, what evidence supports that claim, and which defeaters would still break the argument.",
        formula="A concise assurance template is $$\\mathcal{A} = (G, C, E, D, R),$$ where $G$ are goals or claims, $C$ the context and assumptions, $E$ the evidence, $D$ the defeaters or challenge conditions, and $R$ the residual risks and release restrictions.",
        key_insight="The power of an assurance case is not that it looks formal. It is that every safety claim has to point to evidence, every evidence item has to fit a bounded context, and every open weakness has to be named.",
        algorithm_items=[
            "State the top-level claim about acceptable safety within a bounded operating domain.",
            "Decompose the claim into monitor, controller, human-override, and evidence subclaims.",
            "Attach concrete artifacts: logs, benchmark manifests, hazard analyses, and replay cases.",
            "List defeaters such as stale calibration, untested weather, or unsupported task variants.",
            "Publish residual risk and rollback rules together with the approval boundary.",
        ],
        worked_example="A warehouse robot may have a strong safety case for marked indoor aisles with trained operators and capped speed, yet a weak case for mixed public spaces. The assurance argument keeps those domains distinct instead of letting success in one imply readiness in the other.",
        code="""from dataclasses import dataclass, asdict\n\n@dataclass\nclass AssuranceCard:\n    claim: str\n    context: str\n    evidence: list[str]\n    defeaters: list[str]\n    residual_risk: str\n\ncard = AssuranceCard(\n    claim=\"Robot is acceptably safe for marked indoor aisles under supervised operation.\",\n    context=\"Indoor warehouse, capped speed, trained operators, no public interaction.\",\n    evidence=[\"hazard_log_v3\", \"override_campaign_v2\", \"matched_panel_eval_v5\"],\n    defeaters=[\"camera_calibration_stale\", \"unvalidated_public_spaces\"],\n    residual_risk=\"Minor contact remains possible during rare localization degradation.\"\n)\nprint(asdict(card))""",
        code_output="""{'claim': 'Robot is acceptably safe for marked indoor aisles under supervised operation.', 'context': 'Indoor warehouse, capped speed, trained operators, no public interaction.', 'evidence': ['hazard_log_v3', 'override_campaign_v2', 'matched_panel_eval_v5'], 'defeaters': ['camera_calibration_stale', 'unvalidated_public_spaces'], 'residual_risk': 'Minor contact remains possible during rare localization degradation.'}""",
        code_caption="Code Fragment 54.7.1 builds a minimal assurance card with explicit claim, context, evidence, defeaters, and residual risk.",
        expected_output="The output is useful because every field has a review function. If the card lacks context, the claim is overbroad; if it lacks defeaters, the argument is not honest enough to guide safe release.",
        shortcut="Structured safety-case templates, hazard logs, incident replay archives, and review dashboards reduce the odds that key assumptions remain trapped in meeting notes or memory.",
        deep_dive="Assurance arguments work best when they are maintained artifacts rather than one-time documents. Every new monitor, hardware change, or deployment context should update the case, not sit outside it.",
        failure="The biggest failure mode is rhetorical assurance: a document full of confident claims with no artifact-level traceability. In embodied AI, a safety case that cannot point to logs and replay files is mostly ceremonial.",
        cross_refs='This section consolidates <a href="section-54.3.html">formal safety envelopes</a>, <a href="section-54.4.html">runtime shields</a>, <a href="section-54.5.html">override evidence</a>, and <a href="section-54.6.html">approval gates</a> into one release artifact. It also prepares the operational focus of <a href="../module-55-deployment-architecture/index.html">Chapter 55</a>.',
        lab="Write an assurance card for one embodied system with a bounded domain, three evidence items, two defeaters, and one residual-risk statement. Then try to defeat your own argument by proposing a domain expansion.",
        warning="Do not let the assurance case quietly broaden when the product scope expands. A good safety case narrows claims precisely; a bad one grows vague as deployment pressure rises.",
        example="For drones, the assurance case may name altitude ceiling, geofence, link quality assumptions, and return-to-home behavior. For humanoids, it may focus on human proximity, fall risk, and whole-body intervention authority.",
        frontier="Open work includes machine-readable safety cases, tighter integration with fleet telemetry, and methods for updating assurance arguments when learning-enabled systems evolve after release.",
        self_check="Can you point from each major safety claim to one concrete artifact and one defeater? If not, the assurance case is not yet doing its job.",
        takeaway="Safety cases turn a collection of tests and mitigations into a reviewable deployment argument. They are where technical evidence becomes operational permission.",
        exercise="Draft one assurance argument for a learned robot policy, including claim decomposition, evidence links, defeaters, and a rule for when the argument must be rebuilt after system changes.",
        next_text="Chapter 55 continues from this assurance perspective and asks how deployment architecture should preserve logs, monitors, fallbacks, and update control over the full system lifecycle.",
        refs=[
            ('UL 4600 overview. <a href="https://users.ece.cmu.edu/~koopman/ul4600/index.html" rel="noopener" target="_blank">https://users.ece.cmu.edu/~koopman/ul4600/index.html</a>', "A useful anchor for autonomous-system assurance structure."),
            ('ISO 21448 SOTIF overview. <a href="https://www.iso.org/standard/77490.html" rel="noopener" target="_blank">https://www.iso.org/standard/77490.html</a>', "Useful for discussing performance limitations and intended-functionality hazards."),
            ('UNECE R157 automated lane keeping systems. <a href="https://unece.org/transport/documents/2021/03/standards/un-regulation-no-157-automated-lane-keeping-systems-alks" rel="noopener" target="_blank">https://unece.org/transport/documents/2021/03/standards/un-regulation-no-157-automated-lane-keeping-systems-alks</a>', "A concrete example of structured operational restrictions and evidence obligations."),
        ],
    ),
}


def write_file(rel_path: str, content: str) -> None:
    path = ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    updated = replace_between(text, '<main class="content" id="main-content">', '<nav class="chapter-nav">', content)
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    for rel_path, content in INDEX_CONTENT.items():
        write_file(rel_path, content)
    for rel_path, content in SECTION_CONTENT.items():
        write_file(rel_path, content)


if __name__ == "__main__":
    main()
