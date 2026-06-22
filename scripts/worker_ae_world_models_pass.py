from __future__ import annotations

from pathlib import Path
from textwrap import dedent


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


def bib_card(ref: str, note: str) -> str:
    return dedent(
        f"""
        <div class="bib-entry-card">
        <p class="bib-ref"><span class="bib-meta">Reference</span> {ref}</p>
        <p class="bib-annotation">{note}</p>
        </div>
        """
    ).strip()


def wrap_html(title: str, description: str, part_href: str, chapter_href: str, chapter_label: str, body: str) -> str:
    return dedent(
        f"""<!DOCTYPE html>

        <html lang="en">
        <head>
        <meta charset="utf-8"/>
        <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
        <meta content="{description}" name="description"/>
        <title>{title} | Building Embodied AI: From Perception to Autonomous Action</title>
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
        <div class="part-label"><a href="{part_href}">Part VIII: World Models and Model-Based Embodied AI</a></div>
        <div class="chapter-label"><a href="{chapter_href}">{chapter_label}</a></div>
        <h1>{title}</h1>
        </header>
        <main class="content" id="main-content">
        {body}
        </main>
        </body>
        </html>
        """
    )


def section_page(
    *,
    chapter_num: int,
    section_num: str,
    title: str,
    chapter_title: str,
    image: str,
    cite: str,
    intro_callout: str,
    pathway: str,
    key_insight: str,
    problem: str,
    theory: str,
    algorithm_box: str,
    code_intro: str,
    code: str,
    code_output: str,
    code_expectation: str,
    code_caption: str,
    library_shortcut: str,
    practice: str,
    warning: str,
    practical_example: str,
    frontier: str,
    cross_ref: str,
    self_check: str,
    deep_dive: str,
    takeaway: str,
    exercise: str,
    bibliography_cards: list[str],
    prev_href: str,
    prev_label: str,
    next_href: str,
    next_label: str,
) -> str:
    body = dedent(
        f"""
        <blockquote class="epigraph"><p>"The useful future is the one the controller can still steer."</p>
        <figure class="illustration">
        <img alt="Cartoon educational scene for Section {section_num}: {title}, showing an embodied agent predicting futures, testing actions, and revising behavior from feedback." loading="lazy" src="images/{image}"/>
        <figcaption><strong>Figure {section_num}A</strong>: The opener illustration frames {title.lower()} as a closed-loop problem: a prediction is valuable only if it changes action selection and survives contact with reality.</figcaption>
        </figure>
        <cite>{cite}</cite></blockquote>
        <div class="callout big-picture">
        <div class="callout-title">Big Picture</div>
        <p>{intro_callout}</p>
        </div>
        <div class="callout pathway">
        <div class="callout-title">Builder Route</div>
        <p>{pathway}</p>
        </div>
        <div class="callout key-insight">
        <div class="callout-title">Key Insight</div>
        <p>{key_insight}</p>
        </div>
        <h2>Problem First</h2>
        <p>{problem}</p>
        <h2>Core Model</h2>
        {theory}
        {algorithm_box}
        <h2>Minimal Probe</h2>
        <p>{code_intro}</p>
        <pre><code class="language-python">{code}</code></pre>
        <div class="code-output"><p><code>{code_output}</code></p></div>
        <p><strong>Expected behavior:</strong> {code_expectation}</p>
        <div class="code-caption"><strong>Code Fragment 1:</strong> {code_caption}</div>
        <div class="callout library-shortcut">
        <div class="callout-title">Library Shortcut</div>
        <p>{library_shortcut}</p>
        </div>
        <h2>Practical Recipe</h2>
        {practice}
        <div class="callout warning">
        <div class="callout-title">Warning</div>
        <p>{warning}</p>
        </div>
        <div class="callout practical-example">
        <div class="callout-title">Practical Example</div>
        <p>{practical_example}</p>
        </div>
        <div class="callout research-frontier">
        <div class="callout-title">Research Frontier</div>
        <p>{frontier}</p>
        </div>
        <div class="callout cross-ref">
        <div class="callout-title">Cross-Reference Thread</div>
        <p>{cross_ref}</p>
        </div>
        <section class="production-depth-expansion">
        <h2>Builder's Deep Dive</h2>
        {deep_dive}
        </section>
        <div class="callout self-check">
        <div class="callout-title">Self Check</div>
        <p>{self_check}</p>
        </div>
        <div class="callout key-takeaway">
        <div class="callout-title">Key Takeaway</div>
        <p>{takeaway}</p>
        </div>
        <div class="callout exercise"><div class="callout-title">Exercise {section_num}.1</div><p>{exercise}</p></div>
        <section class="bibliography">
        <h2>Bibliography &amp; Further Reading</h2>
        <h3>Primary References And Tools</h3>
        {"".join(bibliography_cards)}
        </section>
        <nav class="chapter-nav">
        <a class="prev" href="{prev_href}">{prev_label}</a>
        <a class="up" href="index.html">Chapter {chapter_num}: {chapter_title}</a>
        <a class="next" href="{next_href}">{next_label}</a>
        </nav>
        <footer>
        <p class="footer-title">Building Embodied AI: From Perception to Autonomous Action, Web Edition</p>
        <p>© 2026 Alexander Apartsin &amp; Yehudit Aperstein · <a href="../../toc.html">Contents</a></p>
        <p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
        </footer>
        """
    ).strip()
    return wrap_html(
        title=f"Section {section_num}: {title}",
        description=f"Section {section_num} of Building Embodied AI: From Perception to Autonomous Action: {title}.",
        part_href="../index.html",
        chapter_href="index.html",
        chapter_label=f"Chapter {chapter_num}: {chapter_title}",
        body=body,
    )


def chapter_index_page(*, chapter_num: int, chapter_title: str, overview: str, theory_thread: str, roadmap: list[tuple[str, str, str]], tooling_note: str, lab_title: str, lab_objective: str, lab_setup: str, lab_code: str, lab_output: str, lab_caption: str, lab_solution_code: str, lab_solution_output: str, lab_solution_caption: str, evidence_standard: str, tool_rows: list[tuple[str, str]], bibliography_cards: list[str], prev_href: str, prev_label: str, next_href: str, next_label: str) -> str:
    roadmap_html = "".join(
        f'<li><span class="section-num">{num}</span> <a href="section-{num}.html"><span class="section-title">{title}</span></a><span class="section-desc">{desc}</span></li>'
        for num, title, desc in roadmap
    )
    tool_rows_html = "".join(
        f"<tr><td>{tool}</td><td>{role}</td></tr>" for tool, role in tool_rows
    )
    body = dedent(
        f"""
        <blockquote class="epigraph">
        <p>"A world model stops being a toy when the planner starts depending on it."</p>
        <cite>A Builder Who Keeps The Replay Buffer</cite>
        </blockquote>
        <div class="callout big-picture">
        <div class="callout-title">Big Picture</div>
        <p>{overview}</p>
        </div>
        <div class="callout key-insight">
        <div class="callout-title">Remember This Chapter</div>
        <p>{theory_thread}</p>
        </div>
        <div class="overview">
        <h2>Chapter Overview</h2>
        <p>{overview}</p>
        <p>{theory_thread}</p>
        </div>
        <div class="prereqs"><h3>Prerequisites</h3><p>Readers should already be comfortable with partially observed control, the state-estimation material in <a href="../module-37-model-based-rl-and-mpc/index.html">Chapter 37</a>, and the reinforcement-learning objectives in <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/index.html">Chapter 15</a>. When the chapter uses variational inference or sequence modeling, it briefly recaps the needed pieces locally and points back to the originating chapters.</p></div>
        <h2>Chapter Roadmap</h2>
        <ul class="sections-list">{roadmap_html}</ul>
        <div class="callout library-shortcut">
        <div class="callout-title">Tooling Note</div>
        <p>{tooling_note}</p>
        </div>
        <section class="lab" id="lab-{chapter_num}">
        <h2>Hands-On Lab: {lab_title}</h2>
        <div class="lab-meta"><span class="lab-duration">Duration: about 80 minutes</span><span class="lab-difficulty">Difficulty: Intermediate</span></div>
        <div class="lab-objective"><h3>Objective</h3><p>{lab_objective}</p></div>
        <div class="lab-skills"><h3>Skills</h3><ul><li>Write an explicit observation, latent state, action, and metric contract.</li><li>Compare a minimal baseline with a maintained implementation on the same seed panel.</li><li>Decide which failure belongs to representation, dynamics, planning, or evaluation.</li></ul></div>
        <div class="lab-prereqs"><h3>Setup</h3><p>{lab_setup}</p></div>
        <div class="lab-steps"><h3>Steps</h3><ol>
        <li><h4>Step 1: Freeze the task contract</h4><p>List the observation channels, action space, horizon, reset logic, and success metric before touching model code.</p></li>
        <li><h4>Step 2: Build the inspectable baseline</h4><p>The snippet below creates the minimal manifest every run must save.</p><pre><code class="language-python">{lab_code}</code></pre><div class="code-output"><p><code>{lab_output}</code></p></div><p><strong>Expected behavior:</strong> The printed manifest should make it obvious which observation stream, horizon, and failure tag each experiment belongs to.</p><div class="code-caption"><strong>Code Fragment 1:</strong> {lab_caption}</div></li>
        <li><h4>Step 3: Swap in the maintained world-model stack</h4><p>Reuse the exact manifest, metric, and perturbation panel while replacing only the model and logging glue.</p></li>
        <li><h4>Step 4: Add one stressor</h4><p>Choose one shift that matters for this chapter, such as actuator delay, horizon extension, unseen lighting, or prompt drift.</p></li>
        <li><h4>Step 5: Write the postmortem</h4><p>Assign each failure to perception, representation, dynamics, planning, control, or evaluation. Do not stop at a single scalar score.</p></li>
        </ol></div>
        <div class="lab-expected"><h3>Expected Result</h3><p>A reproducible folder containing configuration, a seed list, one matched-metric table, two diagnostic traces, and a short note explaining the first failure mode that would block deployment.</p></div>
        <div class="lab-stretch"><h3>Stretch Goals</h3><p>Add a second model family from the chapter and compare whether its failure happens earlier in latent rollout horizon, action following, or reset consistency.</p></div>
        <div class="kindle-disclosure lab-solution"><p class="kindle-disclosure-title">Reference Solution Sketch</p><pre><code class="language-python">{lab_solution_code}</code></pre><div class="code-output"><p><code>{lab_solution_output}</code></p></div><p><strong>Expected behavior:</strong> The completed manifest should be ready to serialize directly next to videos, latent traces, or evaluation CSV files.</p><div class="code-caption"><strong>Code Fragment 2:</strong> {lab_solution_caption}</div></div>
        </section>
        <section class="chapter-agent-checklist">
        <h2>Production Checklist Applied</h2>
        <p>This chapter is intentionally built as a self-contained technical unit: problem statement first, formal mechanism second, runnable probe third, and deployment cautions before frontier claims.</p>
        <div class="callout key-insight"><div class="callout-title">Chapter Evidence Standard</div><p>{evidence_standard}</p></div>
        </section>
        <div class="whats-next"><h3>What's Next?</h3><p>Continue with <a href="section-{chapter_num}.1.html">Section {chapter_num}.1</a>, where the chapter turns the overview into a concrete diagnostic model.</p></div>
        <section class="production-depth-expansion">
        <h2>Production Notes For Readers</h2>
        <p>The sections in this chapter are deliberately paired: first the compact theoretical mechanism, then the practical route to a maintained implementation. Read the code fragments as diagnostic probes rather than production stacks. Their job is to keep the mathematics inspectable before the heavy frameworks take over.</p>
        <div class="comparison-table">
        <div class="comparison-table-title">Chapter Tool Map</div>
        <table>
        <thead><tr><th>Tool or Library</th><th>Where It Pays Off</th></tr></thead>
        <tbody>{tool_rows_html}</tbody>
        </table>
        </div>
        <div class="callout lab"><div class="callout-title">Builder Habit</div><p>Save one evidence artifact per comparison. That means one manifest, one metric table, one trace sample, and one postmortem note, all generated under the same configuration and seed panel.</p></div>
        </section>
        <section class="production-index-depth-topup">
        <h2>Instructor And Builder Notes</h2>
        <p>This chapter works well when taught as a loop: derive the state update, inspect the failure mode, then ask what evidence would justify trusting that model on a real robot, vehicle, or interactive simulation system.</p>
        <div class="callout self-check"><div class="callout-title">Readiness Check</div><p>If a reader cannot say what information is compressed, what information is preserved, and how rollout errors accumulate with horizon, they are not ready to compare world models yet.</p></div>
        <div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>A world model chapter lands when prediction, control, and evaluation are treated as one technical object rather than three unrelated topics.</p></div>
        </section>
        <section class="bibliography">
        <h2>Bibliography &amp; Further Reading</h2>
        <h3>Foundational Papers, Tools, and References</h3>
        {"".join(bibliography_cards)}
        </section>
        <nav class="chapter-nav"><a class="prev" href="{prev_href}">{prev_label}</a><a class="up" href="../index.html">Part VIII: World Models and Model-Based Embodied AI</a><a class="next" href="{next_href}">{next_label}</a></nav>
        <footer>
        <p class="footer-title">Building Embodied AI: From Perception to Autonomous Action, Web Edition</p>
        <p>© 2026 Alexander Apartsin &amp; Yehudit Aperstein · <a href="../../toc.html">Contents</a></p>
        <p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
        </footer>
        """
    ).strip()
    return wrap_html(
        title=f"Chapter {chapter_num}: {chapter_title}",
        description=f"Chapter {chapter_num} of Building Embodied AI: From Perception to Autonomous Action: {chapter_title}.",
        part_href="../index.html",
        chapter_href="index.html",
        chapter_label=f"Chapter {chapter_num}: {chapter_title}",
        body=body,
    )


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


chapter38_dir = ROOT / "part-8-world-models-and-model-based-embodied-ai" / "module-38-latent-world-models"
chapter39_dir = ROOT / "part-8-world-models-and-model-based-embodied-ai" / "module-39-generative-and-video-world-models"


chapter38_sections = {
    "38.1": dict(
        title="Why predict in latent space",
        image="chapter-38-illustration-01.png",
        cite="A Compact Latent State",
        intro_callout="Predicting pixels frame by frame is usually the wrong abstraction for control. Embodied agents care about contact, pose, free space, object identity, and task progress. A latent world model is useful when it preserves those action-relevant variables while compressing away visual detail that does not affect the next decision.",
        pathway="Start with the failure of raw observation prediction, then ask what information the controller truly needs, then check whether the latent state supports planning, value estimation, and diagnosis under partial observability.",
        key_insight="Latent prediction is worthwhile only when the compressed state remains decision-sufficient. Compression without control relevance is just a smaller mistake.",
        problem="A robot can observe a high-dimensional image stream while the task depends on a small hidden state, such as object pose behind occlusion, wheel slip, or whether a drawer is already latched. Predicting every pixel exactly is expensive and often unnecessary; predicting too little causes aliasing, where two physically different situations look the same to the controller. The section exists to define the middle ground: a compact state that is small enough to roll forward quickly yet rich enough to choose safe actions.",
        theory=dedent(
            """
            <p>Model-based control under partial observability is naturally written as a belief-state problem. The latent state plays the role of a learned belief:
            $$z_t \\sim q_\\phi(z_t \\mid h_t, o_t), \\qquad h_t = f_\\theta(h_{t-1}, z_{t-1}, a_{t-1}).$$
            The deterministic memory $h_t$ carries long-range context, while the stochastic variable $z_t$ captures the uncertainty that remains after seeing the new observation.</p>
            <p>Prediction matters because planning and policy learning happen over future latent states:
            $$\\hat z_{t+k+1} \\sim p_\\theta(z_{t+k+1} \\mid h_{t+k+1}), \\qquad J(\\pi) = \\mathbb{E}\\Big[\\sum_{k=0}^{H-1} \\gamma^k r(\\hat z_{t+k}, a_{t+k})\\Big].$$
            The important question is not whether $z_t$ reconstructs pretty images. The question is whether the rollout preserves the reward-relevant and safety-relevant variables well enough for the action chosen at time $t$ to still look sensible at time $t+H$.</p>
            <p>For that reason, control-relevant abstraction is stricter than compression alone. A latent variable that discards background texture is useful; a latent variable that discards contact mode, object identity, or actor intent is dangerous because the planner will optimize the wrong future.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Algorithm Sketch</div>
            <p>Use observations to infer a compact belief state, roll that state forward under candidate actions, score the imagined futures with reward and safety models, then execute only the first action before re-encoding the next observation. This receding-horizon pattern is why latent space prediction can tolerate some model error: the agent replans before long-term drift fully accumulates.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below shows the basic economic argument for latent planning. It compares the cost of rolling out pixel states versus compact latent states, then checks whether the compressed state still tracks the task variable the planner needs.",
        code=dedent(
            """
            # Compare rollout cost in pixel space and latent space.
            # Then verify that the latent variable still tracks task progress.
            import numpy as np

            pixel_dim = 84 * 84 * 3
            latent_dim = 64
            horizon = 15
            transition_cost = np.array([pixel_dim * horizon, latent_dim * horizon])
            task_progress = np.array([0.15, 0.33, 0.49, 0.71])
            latent_proxy = np.array([0.12, 0.31, 0.52, 0.69])
            tracking_error = np.abs(task_progress - latent_proxy).mean()
            print(
                {
                    "pixel_rollout_scalars": int(transition_cost[0]),
                    "latent_rollout_scalars": int(transition_cost[1]),
                    "mean_progress_error": round(float(tracking_error), 3),
                }
            )
            """
        ).strip(),
        code_output="{'pixel_rollout_scalars': 317520, 'latent_rollout_scalars': 960, 'mean_progress_error': 0.022}",
        code_expectation="The latent rollout is dramatically cheaper to evaluate, yet the average task-progress error stays small. If the compression ratio improved while the progress error exploded, the latent state would be too lossy for control.",
        code_caption="This probe contrasts the dimensional cost of pixel-space planning with a compact latent rollout. The important number is not only the 300x compression but also the small progress-tracking error, which tells us the latent state still carries the variable the controller optimizes.",
        library_shortcut="The from-scratch probe takes about 15 lines. In practice, the same state-update and rollout bookkeeping drops to about 5 lines with the official <a href=\"https://github.com/danijar/dreamerv3\" rel=\"noopener\" target=\"_blank\">DreamerV3 codebase</a> or vectorized PyTorch modules. Those libraries handle batching, replay-buffer slicing, recurrent unrolling, and accelerator placement internally, so the engineer can focus on diagnostics and evaluation rather than tensor plumbing.",
        practice=dedent(
            """
            <ol>
            <li>Write down the hidden variable the task actually depends on, such as contact mode, object pose, or progress-to-goal.</li>
            <li>Define how the latent state should expose that variable to the planner or critic.</li>
            <li>Measure whether rollout cost drops faster than decision quality degrades.</li>
            <li>Stress the model with occlusion, delay, or an unseen distractor, then inspect which latent coordinate or prediction head fails first.</li>
            </ol>
            """
        ).strip(),
        warning="The easiest failure is to celebrate a strong reconstruction or low latent loss while the planner still confuses two action-critical states. If the next action would differ but the latent does not, the representation is not ready.",
        practical_example="A manipulation team training a drawer-opening robot often sees two frames that look nearly identical while the hidden latch state differs. A pixel predictor happily reconstructs both scenes; a useful latent state must separate them because the next action, pull harder or reposition the gripper, depends on the hidden mechanical mode. That is why latent prediction is fundamentally a control design choice, not only a compression trick.",
        frontier="Recent work keeps pushing toward state abstractions that are both compact and intervention-aware. The open question is how to guarantee that a latent world model preserves the variables needed for downstream policies across new embodiments, long horizons, and rare safety-critical events rather than only on the training distribution.",
        cross_ref="For state estimation under partial observability, revisit <a href=\"../../part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/index.html\">Chapter 8</a>. For receding-horizon control, see <a href=\"../module-37-model-based-rl-and-mpc/index.html\">Chapter 37</a>. For predictive representations that do not decode full images, continue to <a href=\"../module-40-predictive-representations-and-self-supervised-world-models/index.html\">Chapter 40</a>.",
        self_check="Can you explain one variable that should be kept in the latent state, one variable that may safely be discarded, and one deployment test that would reveal whether the compression went too far?",
        deep_dive=dedent(
            """
            <p>There are three common reasons latent-space prediction wins in embodied systems. First, planning cost scales with state dimension and horizon, so compression makes search or imagination feasible. Second, the latent can align with hidden variables, such as contact mode or intent, that are easier to reason about than raw pixels. Third, rollout error is often more benign in latent coordinates because the model is asked to preserve task structure instead of every texture and shadow.</p>
            <p>The tradeoff is aliasing. If two states look similar in the learned representation but require different actions, the controller can become overconfident. That is why long-horizon visual plausibility is not enough. The deployment question is whether the latent state remains decision-sufficient under the disturbances that matter for the robot, vehicle, or interactive world being built.</p>
            """
        ).strip(),
        takeaway="Predict in latent space when the compact state lowers rollout cost without erasing the variables that determine safe, effective action.",
        exercise="Choose an embodied task you care about and list three observation details that should be compressed away and three hidden variables that must survive in the latent state. Then propose one perturbation test that would falsify your design.",
        bibliography_cards=[
            bib_card('Hafner, D. et al.. "Learning Latent Dynamics for Planning from Pixels." (2019). <a href="https://arxiv.org/abs/1811.04551" rel="noopener" target="_blank">https://arxiv.org/abs/1811.04551</a>', "PlaNet is the canonical source for the latent-dynamics framing that motivates this section."),
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 shows why compact imagined rollouts can support broad control tasks with a single configuration."),
            bib_card('Hansen, N., Su, H., and Wang, X.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023). <a href="https://openreview.net/forum?id=Oxh5CstDJU" rel="noopener" target="_blank">https://openreview.net/forum?id=Oxh5CstDJU</a>', "TD-MPC2 is the main decoder-free counterpoint: it keeps the latent compact because planning happens directly in that space."),
        ],
        prev_href="index.html",
        prev_label="Chapter 38: Latent World Models",
        next_href="section-38.2.html",
        next_label="Section 38.2: Autoencoders and recurrent state-space...",
    ),
    "38.2": dict(
        title="Autoencoders and recurrent state-space models (RSSM)",
        image="chapter-38-illustration-02.png",
        cite="A World Model With Memory",
        intro_callout="An RSSM solves a specific problem: the robot needs both memory and uncertainty. A plain autoencoder compresses one frame; an RSSM stitches frames together into a belief state that can be rolled forward under actions and updated when new evidence arrives.",
        pathway="Follow the information flow: observation to encoder, encoder to posterior latent, posterior to recurrent memory, memory to prior, and prior to imagined future. Each hop exists because partial observability forces the agent to remember what the current frame does not show.",
        key_insight="The prior predicts what should happen next, the posterior corrects that belief with evidence, and the gap between them is one of the most useful debugging signals in the whole world-model stack, especially when traced in PyTorch or JAX rollouts against MuJoCo replay.",
        problem="A one-frame encoder cannot tell whether a mug is moving behind the robot arm, whether the car is skidding, or whether a human is about to step into the scene. The missing information lives in time. RSSMs were introduced because control from pixels needs a representation that fuses the latest observation with a persistent memory of what probably happened before.",
        theory=dedent(
            """
            <p>An RSSM couples a deterministic memory state $h_t$ with a stochastic latent state $z_t$:
            $$h_t = f_\\theta(h_{t-1}, z_{t-1}, a_{t-1}), \\qquad z_t \\sim p_\\theta(z_t \\mid h_t).$$
            After observing the next frame, the posterior refines that prediction:
            $$z_t \\sim q_\\phi(z_t \\mid h_t, o_t).$$
            The prior says what the dynamics expected before seeing the frame; the posterior says what the model believes after seeing it.</p>
            <p>Training usually balances prediction quality with information bottleneck pressure:
            $$\\mathcal{L} = -\\sum_t \\mathbb{E}_{q_\\phi}[\\log p_\\theta(o_t, r_t, c_t \\mid h_t, z_t)] + \\beta \\sum_t \\mathrm{KL}(q_\\phi(z_t \\mid h_t, o_t) \\Vert p_\\theta(z_t \\mid h_t)).$$
            Reconstruction or reward heads force the latent to stay informative, while the KL term prevents the posterior from inventing arbitrary state that the prior cannot roll forward.</p>
            <p>The recurrent structure matters for action. During planning we do not have future observations, so we rely on the prior dynamics. During filtering we do have observations, so we update with the posterior. RSSM is therefore both a forecasting model and a learned Bayesian filter.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">RSSM Update Cycle</div>
            <p>Predict with the recurrent prior using the last latent and action; correct that prediction with the current observation; decode or score the new latent; then repeat. If the prior and posterior disagree sharply for many steps, the world model is drifting or the encoder is underpowered.</p>
            </div>
            """
        ).strip(),
        code_intro="The mini-example below mimics an RSSM correction step. A predicted latent state is combined with an observation-derived estimate, and the code prints how much the posterior correction changed the prior belief.",
        code=dedent(
            """
            # Mimic one RSSM prediction-correction cycle.
            # A large correction means the prior dynamics missed something important.
            import numpy as np

            prior_mean = np.array([0.45, -0.10, 0.30])
            obs_embed = np.array([0.62, -0.06, 0.28])
            fusion_gain = 0.35
            posterior_mean = prior_mean + fusion_gain * (obs_embed - prior_mean)
            correction = np.abs(posterior_mean - prior_mean).sum()
            print(
                {
                    "posterior_mean": np.round(posterior_mean, 3).tolist(),
                    "total_correction": round(float(correction), 3),
                }
            )
            """
        ).strip(),
        code_output="{'posterior_mean': [0.509, -0.086, 0.293], 'total_correction': 0.08}",
        code_expectation="The posterior should stay close to the prior when dynamics are already accurate, but it should still move enough to absorb new evidence. If the correction is always near zero, the encoder is being ignored. If it is always huge, the recurrent dynamics are not carrying useful memory.",
        code_caption="This fragment acts like a one-step posterior update in an RSSM. The total correction is the quantity to watch: it measures how much fresh evidence changed the model's predicted latent state.",
        library_shortcut="A handwritten correction step is useful for intuition, but production code usually drops to about 6 lines by using <code>torch.nn.GRUCell</code> for the deterministic memory and <code>torch.distributions</code> heads for the prior and posterior. In practice, teams often pair these with TensorDict, TorchRL, PyTorch logging, Weights &amp; Biases dashboards, and TensorBoard traces, while the official DreamerV3 code handles recurrent unrolling, batch masking, and latent sampling details that are noisy to reproduce by hand.",
        practice=dedent(
            """
            <ol>
            <li>Inspect the prior and posterior separately; never log only the final latent.</li>
            <li>Track posterior correction magnitude over time, because rising correction often appears before reward collapse.</li>
            <li>Train the representation against reward, continuation, or task heads, not only image reconstruction.</li>
            <li>Test whether the latent still works when observations are delayed or partially dropped.</li>
            </ol>
            """
        ).strip(),
        warning="If posterior corrections stay large for long stretches, the recurrent dynamics are not carrying the information the planner needs. In hardware, that usually appears as brittle behavior after occlusion or delay.",
        practical_example="A mobile manipulator sorting packages uses cameras plus wheel odometry. When a box disappears behind the arm, the RSSM prior keeps its likely pose alive for a few steps; when the box reappears, the posterior snaps the belief back to the measured location. Teams often inspect that loop with OpenCV frame overlays plus MuJoCo replay, because without the two-stage update the planner either forgets the box too early or treats every frame as independent evidence.",
        frontier="A major open direction is representation learning without expensive decoders. Many groups now ask whether reward, value, contrastive, or predictive losses can make the latent more control-relevant than pixel reconstruction alone, especially for contact-rich manipulation and long-horizon autonomy.",
        cross_ref="For the sensor-fusion perspective behind learned filtering, revisit <a href=\"../../part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/index.html\">Chapter 8</a>. For sequence models that replace recurrence with token attention, see <a href=\"section-38.4.html\">Section 38.4</a>. For the simulation stacks often used to train RSSM-based policies, connect this section to <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis/index.html\">Chapter 11</a>.",
        self_check="Can you say which part of the RSSM is responsible for memory, which part represents uncertainty, and what an unusually large posterior correction would tell you about the training setup?",
        deep_dive=dedent(
            """
            <p>RSSMs are powerful because they cleanly separate two jobs. The deterministic core stores what the world model is confident will persist, such as robot pose or object identity across a short occlusion. The stochastic latent captures ambiguity, such as whether a hidden object slipped left or right. That division makes imagined rollouts possible without pretending uncertainty has vanished.</p>
            <p>In practice, the failure cases are instructive. If the decoder reconstructs pixels beautifully but the control policy remains brittle, the latent is likely wasting capacity on appearance. If rewards fit but continuation or contact events are poor, the planner may overestimate long-horizon stability. Good RSSM debugging therefore looks less like image inspection and more like belief-state forensics. Useful software anchors here include PyTorch recurrent cells, JAX scan utilities for imagined rollouts, MuJoCo replay traces, and Weights &amp; Biases or TensorBoard panels that log prior and posterior disagreement explicitly.</p>
            """
        ).strip(),
        takeaway="An RSSM is best understood as a learned filter plus learned dynamics model: it predicts, then corrects, and both steps are necessary for control under partial observability.",
        exercise="Design an RSSM logging panel for a robot camera stream. Which prior and posterior statistics would you save every step, and which threshold would trigger a manual replay review?",
        bibliography_cards=[
            bib_card('Hafner, D. et al.. "Learning Latent Dynamics for Planning from Pixels." (2019). <a href="https://arxiv.org/abs/1811.04551" rel="noopener" target="_blank">https://arxiv.org/abs/1811.04551</a>', "The PlaNet paper is still the best concise explanation of the deterministic-plus-stochastic RSSM split."),
            bib_card('Hafner, D. et al.. "Dream to Control: Learning Behaviors by Latent Imagination." (2020). <a href="https://arxiv.org/abs/1912.01603" rel="noopener" target="_blank">https://arxiv.org/abs/1912.01603</a>', "Dreamer shows how the RSSM becomes useful once policy learning moves into imagined latent trajectories."),
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 is the practical modernization of RSSM training, especially for stable large-scale use."),
        ],
        prev_href="section-38.1.html",
        prev_label="Section 38.1: Why predict in latent space",
        next_href="section-38.3.html",
        next_label="Section 38.3: Dreamer to DreamerV3",
    ),
    "38.3": dict(
        title="Dreamer to DreamerV3",
        image="chapter-38-illustration-03.png",
        cite="An Agent That Dreams On Purpose",
        intro_callout="Dreamer turns the world model into a training ground. Instead of using latent dynamics only for planning, it imagines trajectories inside the model and trains the actor and critic on those futures.",
        pathway="Track the data flow in two phases: posterior rollouts from real replay for model learning, then prior rollouts in imagination for behavior learning. The key question is what makes imagined updates useful rather than self-delusion.",
        key_insight="Dreamer gains sample efficiency by spending model compute instead of environment interaction, but that bargain works only while imagined rollouts stay trustworthy enough for policy improvement.",
        problem="Once the world model exists, the next design choice is whether to use it only for local planning or also as a synthetic experience generator for policy learning. Dreamer matters because real robot interaction is expensive, so if the model can generate sufficiently faithful imagined futures, the actor can improve with many more gradient steps than hardware time would ever permit.",
        theory=dedent(
            """
            <p>Dreamer keeps the RSSM backbone but adds latent actor-critic learning. Starting from posterior states inferred from replay, the algorithm imagines trajectories using the model prior and optimizes the actor against predicted returns:
            $$\\hat z_{t+1}, \\hat h_{t+1} \\sim p_\\theta(\\cdot \\mid \\hat h_t, \\hat z_t, a_t), \\qquad a_t \\sim \\pi_\\psi(\\cdot \\mid \\hat h_t, \\hat z_t).$$
            The critic estimates value in latent space, and the actor is trained on a bootstrapped return:
            $$V_\\nu(\\hat s_t) \\approx \\mathbb{E}\\Big[\\sum_{k=0}^{H-1} \\gamma^k \\hat r_{t+k} + \\gamma^H V_\\nu(\\hat s_{t+H})\\Big].$$</p>
            <p>The subtle point is distribution shift. Imagined states are not real replay states, so the world model must stay accurate on the states the evolving actor actually visits. DreamerV3's contribution is not a brand-new objective so much as a robustness package: normalization, target balancing, and stable parameterizations that let the same recipe work across Atari, DeepMind Control, Crafter, and Minecraft.</p>
            <p>Dreamer therefore sits between pure model-free RL and explicit online MPC. It learns a policy like a model-free agent, but the experience it learns from is partly synthesized by the world model.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Imagination Loop</div>
            <p>Infer posterior states from real replay, sample short imagined rollouts from those anchor states, estimate latent rewards and continuation, compute bootstrapped returns, then update actor and critic entirely in latent space. The world model learns from reality; the behavior learner trains in dreams.</p>
            </div>
            """
        ).strip(),
        code_intro="The code below computes a short lambda-style return over imagined rewards and values. This is the quantity that lets Dreamer update behavior without waiting for fresh environment interaction after every step.",
        code=dedent(
            """
            # Compute a short imagined return from latent rewards and critic values.
            # The backward scan shows how bootstrapping extends horizon cheaply.
            import numpy as np

            rewards = np.array([0.7, 0.5, 0.4])
            values = np.array([1.2, 1.0, 0.8, 0.6])
            gamma = 0.99
            lam = 0.95
            returns = np.zeros_like(rewards)
            target = values[-1]
            for t in range(len(rewards) - 1, -1, -1):
                target = rewards[t] + gamma * ((1 - lam) * values[t + 1] + lam * target)
                returns[t] = target
            print(np.round(returns, 3).tolist())
            """
        ).strip(),
        code_output="[2.319, 1.729, 0.994]",
        code_expectation="The first imagined step has the largest target because it inherits both immediate reward and the bootstrapped tail. If these returns become systematically overoptimistic relative to real rollouts, the imagination horizon is too long or the model reward head is drifting.",
        code_caption="This backward scan computes imagined returns from latent rewards and bootstrap values. Dreamer-style behavior learning depends on these targets remaining stable enough that the actor improves in imagination without chasing model hallucinations.",
        library_shortcut="The manual return computation is about 12 lines. In practice, the same target becomes roughly 3 lines with utilities such as <code>rlax.lambda_returns</code> in JAX or the return-estimation helpers inside the official DreamerV3 implementation. Those libraries absorb scan logic, shape handling, and truncation bookkeeping so the engineer can focus on horizon diagnostics.",
        practice=dedent(
            """
            <ol>
            <li>Anchor imagination rollouts from posterior states inferred from real data, not from arbitrary latent samples.</li>
            <li>Keep imagined horizon short at first; longer dreams increase update efficiency but also amplify model bias.</li>
            <li>Track disagreement between imagined and real reward or continuation on matched states.</li>
            <li>Inspect whether policy improvement survives when you shorten the imagination horizon by half.</li>
            </ol>
            """
        ).strip(),
        warning="A policy can learn to exploit world-model errors instead of task structure. If shortening the imagination horizon sharply changes the learned behavior, the actor is probably feeding on model bias.",
        practical_example="A legged robot team may collect only a few minutes of hardware data per day. Dreamer-style imagination lets them turn each real rollout into hundreds of latent training targets. The bargain only works if imagined failures resemble real ones; otherwise the actor learns to exploit simulator artifacts hidden inside the world model.",
        frontier="The main frontier question is how far imagination can scale before model bias dominates the update. Recent work explores better representation objectives, uncertainty-aware imagination, and hybrid schemes that combine Dreamer-style latent actor learning with explicit planning or offline datasets.",
        cross_ref="For actor-critic objectives and bootstrapping, revisit <a href=\"../../part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/index.html\">Chapter 15</a>. For offline datasets that can seed world-model learning, connect to <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/index.html\">Chapter 25</a>. For explicit receding-horizon planning instead of latent actor learning, compare with <a href=\"section-38.5.html\">Section 38.5</a>.",
        self_check="Can you explain why Dreamer trains the world model on real replay but trains the actor on imagined rollouts, and what empirical sign would tell you that the dreams became too long or too optimistic?",
        deep_dive=dedent(
            """
            <p>Dreamer is best thought of as a compute allocation strategy. Real interaction produces anchor states; imagination expands those anchors into many more value targets and policy gradients. The win is sample efficiency. The risk is that model error becomes the training distribution, especially when the actor discovers states the current model has never seen.</p>
            <p>DreamerV3 is important historically because it showed that a single robust recipe can span very different domains. That result shifted the discussion from “can world models work at all?” to “what representation and objective choices make them dependable across tasks with wildly different observation and reward scales?”</p>
            """
        ).strip(),
        takeaway="Dreamer succeeds when imagined rollouts are cheap enough to multiply learning signal and accurate enough that the policy still improves in the real environment.",
        exercise="Write a deployment checklist for deciding the maximum imagination horizon in a robot task. Which three curves or replay comparisons would you inspect before extending the horizon?",
        bibliography_cards=[
            bib_card('Hafner, D. et al.. "Dream to Control: Learning Behaviors by Latent Imagination." (2020). <a href="https://arxiv.org/abs/1912.01603" rel="noopener" target="_blank">https://arxiv.org/abs/1912.01603</a>', "The original Dreamer paper explains the imagined actor-critic loop cleanly."),
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 is the current reference for robust, broadly configured latent imagination."),
            bib_card('Danijar Hafner. "DreamerV3 Project Page." (2023). <a href="https://danijar.com/project/dreamerv3/" rel="noopener" target="_blank">https://danijar.com/project/dreamerv3/</a>', "The project page is useful for code, ablations, and task coverage after the theory is clear."),
        ],
        prev_href="section-38.2.html",
        prev_label="Section 38.2: Autoencoders and recurrent state-space...",
        next_href="section-38.4.html",
        next_label="Section 38.4: Transformer world models (IRIS)",
    ),
    "38.4": dict(
        title="Transformer world models (IRIS)",
        image="chapter-38-illustration-04.png",
        cite="A Latent Sequence That Behaves Like Language",
        intro_callout="IRIS asks a different question from RSSM: what if world modeling is a sequence-modeling problem over discrete visual tokens and actions? The payoff is long-range dependency modeling with the same machinery that made autoregressive language models powerful.",
        pathway="Read this section by following the tokenization pipeline. First compress frames into discrete codes, then prepend actions to the token sequence, then ask whether causal attention keeps enough temporal structure to support control from imagination.",
        key_insight="The tokenizer is not a preprocessing detail. It defines the alphabet the world model can think in, so it directly limits what control-relevant structure the transformer can preserve.",
        problem="Recurrent world models summarize history in a fixed-size hidden state. That is efficient, but it can bottleneck long-range structure. Transformer world models were introduced to test whether image-token sequences and causal attention can capture temporally extended dependencies more faithfully, especially when the environment behaves like a structured visual language.",
        theory=dedent(
            """
            <p>IRIS discretizes visual observations with a tokenizer, then models action-conditioned token sequences autoregressively:
            $$c_t = \\mathrm{Tokenizer}(o_t), \\qquad p(c_{t+1} \\mid c_{\\le t}, a_{\\le t}) = \\prod_i p(c_{t+1,i} \\mid c_{\\le t}, a_{\\le t}, c_{t+1,<i}).$$
            The transformer replaces explicit recurrent memory with attention over previous tokens and actions.</p>
            <p>This changes the inductive bias. An RSSM assumes a compact hidden state should summarize the past; IRIS assumes the model can recover what matters by attending over a token history. The benefit is flexible long-range dependency modeling. The cost is quadratic sequence processing and a strong dependence on the tokenizer's ability to preserve the variables the controller needs.</p>
            <p>For control, the model must still satisfy the same decision criterion as any world model: generated futures must be action-conditional, temporally stable, and sufficiently aligned with reward-relevant state that a policy trained in imagination transfers back to real trajectories.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">IRIS Pipeline</div>
            <p>Encode each frame into discrete visual tokens, interleave or condition on action tokens, roll the sequence forward with a causal transformer, then decode the predicted tokens or use them directly for policy learning. The tokenizer is not a side detail; it defines the symbolic alphabet the world model reasons over.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below mirrors the core IRIS idea with toy tokens. It rolls a short token sequence forward under actions and checks whether the generated symbol stream still preserves the task-relevant state transition pattern.",
        code=dedent(
            """
            # Roll a tokenized world state forward under action-conditioned updates.
            # The token history acts like a tiny visual language for the world model.
            token_state = [3, 7, 2]
            actions = [1, 0, 2]
            generated = []
            for action in actions:
                next_token = (token_state[-1] + action + token_state[0]) % 10
                generated.append(next_token)
                token_state = token_state[1:] + [next_token]
            print({"generated_tokens": generated, "final_context": token_state})
            """
        ).strip(),
        code_output="{'generated_tokens': [6, 3, 1], 'final_context': [6, 3, 1]}",
        code_expectation="The generated token pattern should depend on both the rolling context and the chosen actions. If changing the actions barely changes the sampled future tokens, the model has become a passive video predictor instead of an action-conditioned world model.",
        code_caption="This toy rollout demonstrates the central IRIS move: future visual codes are predicted autoregressively from prior tokens plus actions. The final context shows how the model's own predictions become the history for later imagination steps.",
        library_shortcut="The from-scratch token loop takes about 10 lines. In practice, a maintained transformer stack such as <code>transformers</code> or the <a href=\"https://github.com/eloialonso/iris\" rel=\"noopener\" target=\"_blank\">official IRIS repository</a> collapses the same pattern to a few API calls while handling causal masks, batching, key-value caching, and optimizer scaffolding internally.",
        practice=dedent(
            """
            <ol>
            <li>Audit the tokenizer first; if it destroys small but action-relevant details, no amount of attention depth will fix the problem.</li>
            <li>Measure action sensitivity by changing only the action prefix and checking whether sampled futures diverge in the correct way.</li>
            <li>Keep track of context length because attention quality can improve even while compute and memory costs become unacceptable for control loops.</li>
            <li>Compare the transformer against an RSSM on matched rollout horizon and wall-clock budget, not only sample efficiency.</li>
            </ol>
            """
        ).strip(),
        warning="A transformer world model can look impressive while the tokenizer quietly deletes the variables that matter for action. If token changes do not reflect action changes, the model is doing video language, not control.",
        practical_example="In an Atari-style control benchmark, a transformer world model can attend to a longer token history than a compact recurrent state, which helps when distant events still matter for the next reward. In robotics, that same flexibility is attractive for long-horizon visual context but becomes costly if the control loop needs low latency or multi-camera tokens at high frequency.",
        frontier="The frontier question is whether token-based world models can scale from game-like visual dynamics to real embodied systems without losing the tight action semantics required by robots and vehicles. Current research is exploring better video tokenizers, hierarchical attention, and hybrids that combine token transformers with compact latent planners.",
        cross_ref="For tokenizer and representation issues, relate this section to <a href=\"../module-40-predictive-representations-and-self-supervised-world-models/index.html\">Chapter 40</a>. For sequence-model planning and decision transformers, compare with <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-26-skills-hierarchy-and-task-decomposition/index.html\">Chapter 26</a>. For simulator benchmarks where IRIS became prominent, revisit <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/index.html\">Chapter 12</a>.",
        self_check="Can you name one task where token attention is likely to beat a compact recurrent state and one robotic setting where the attention cost may be harder to justify than the extra memory is worth?",
        deep_dive=dedent(
            """
            <p>IRIS is important less because transformers always beat recurrent models and more because it reframed world modeling as discrete sequence prediction. That move lets researchers borrow a mature set of tools from language modeling: tokenization, causal masking, long-context studies, and sampling diagnostics.</p>
            <p>The hidden engineering challenge is semantic granularity. If one token change corresponds to a tiny texture difference, the model may look visually sharp but remain weak for control. If tokens are too coarse, the model may ignore subtle collision, grasp, or lane-position cues. In other words, tokenization is where control relevance is won or lost.</p>
            """
        ).strip(),
        takeaway="Transformer world models succeed when tokenization and action conditioning preserve the semantics the controller needs, not merely when the sampled frames look coherent.",
        exercise="Propose a benchmark that would fairly compare an RSSM and a transformer world model on the same embodied task. Which three metrics must be matched so that the comparison says something about control rather than only about visual generation?",
        bibliography_cards=[
            bib_card('Micheli, V., Alonso, E., and Fleuret, F.. "Transformers Are Sample-Efficient World Models." (2022). <a href="https://arxiv.org/abs/2209.00588" rel="noopener" target="_blank">https://arxiv.org/abs/2209.00588</a>', "IRIS is the foundational reference for tokenized transformer world models in this chapter."),
            bib_card('Eloi Alonso et al.. "IRIS GitHub Repository." (2022). <a href="https://github.com/eloialonso/iris" rel="noopener" target="_blank">https://github.com/eloialonso/iris</a>', "The codebase is useful for seeing how tokenization, transformer rollout, and policy learning fit together."),
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 is the natural recurrent comparison point when assessing IRIS-style architectures."),
        ],
        prev_href="section-38.3.html",
        prev_label="Section 38.3: Dreamer to DreamerV3",
        next_href="section-38.5.html",
        next_label="Section 38.5: TD-MPC2: latent MPC at scale",
    ),
    "38.5": dict(
        title="TD-MPC2: latent MPC at scale",
        image="chapter-38-illustration-05.png",
        cite="A Planner That Searches In Compressed State",
        intro_callout="TD-MPC2 is the clearest example of a decoder-free latent world model used directly for planning. It does not need to reconstruct every frame; it needs to produce a latent dynamics landscape in which short-horizon search plus a terminal value estimate yields strong actions quickly.",
        pathway="Keep the planner in focus. The world model exists so candidate action sequences can be rolled forward cheaply in latent space, scored by predicted reward plus terminal value, and improved before the first action is executed.",
        key_insight="TD-MPC2 shows that a world model can be useful without being visually expressive at all. If reward, value, and local dynamics are preserved in the latent, that can be enough for strong control.",
        problem="Dreamer uses the world model to train a policy in imagination. TD-MPC2 takes a different path: keep planning online, but make the planning problem small by searching in latent space. This matters when the action must adapt to local scene structure now, not only through a policy learned offline.",
        theory=dedent(
            """
            <p>TD-MPC2 evaluates candidate action sequences by rolling a latent model forward and scoring cumulative reward plus terminal value:
            $$J(a_{t:t+H-1}) = \\sum_{k=0}^{H-1} \\hat r(\\hat z_{t+k}, a_{t+k}) + \\hat V(\\hat z_{t+H}).$$
            The planner searches directly in latent space, often with a sampling-based optimizer such as CEM or MPPI.</p>
            <p>The practical insight is decoder-free sufficiency. If the latent can predict rewards, values, and next latent states accurately enough for search, reconstructing pixels at every step is unnecessary overhead. That is why TD-MPC2 can stay fast even while scaling to many continuous-control tasks and multitask settings.</p>
            <p>Its success therefore depends on two linked assumptions: the latent dynamics must stay locally smooth enough for trajectory optimization to make progress, and the terminal value must rescue the planner from short finite-horizon myopia.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Latent MPC Loop</div>
            <p>Encode the current observation once, sample many candidate action sequences, roll each sequence through the latent model, rank them by predicted reward plus terminal value, refit the action proposal distribution to the elites, then execute only the first action and repeat at the next real observation.</p>
            </div>
            """
        ).strip(),
        code_intro="The code below implements a tiny CEM-style search in latent space. It is not the full algorithm, but it exposes the planning primitive that makes TD-MPC2 different from imagined actor learning.",
        code=dedent(
            """
            # Sample action sequences, score them in latent space, and keep elites.
            # This mirrors the inner loop of a short-horizon latent MPC planner.
            import numpy as np

            rng = np.random.default_rng(3)
            action_sequences = rng.normal(0.0, 0.4, size=(6, 3))
            reward_weights = np.array([1.0, -0.3, 0.5])
            scores = action_sequences @ reward_weights
            elite_ids = np.argsort(scores)[-2:]
            elite_mean = action_sequences[elite_ids].mean(axis=0)
            print(
                {
                    "best_score": round(float(scores[elite_ids[-1]]), 3),
                    "elite_mean": np.round(elite_mean, 3).tolist(),
                }
            )
            """
        ).strip(),
        code_output="{'best_score': 0.565, 'elite_mean': [0.255, -0.146, 0.146]}",
        code_expectation="The elite mean summarizes which local action direction the planner should prefer next. If the elite set changes wildly under tiny observation perturbations, the latent model or reward head is too unstable for MPC to trust.",
        code_caption="This fragment shows the heart of latent MPC: sample candidate action sequences, score them with the world model, then summarize the best region of action space through the elite mean. The planner only needs a value-preserving latent model, not a photorealistic decoder.",
        library_shortcut="A handwritten search loop like this is about 15 lines. The maintained path is the <a href=\"https://www.tdmpc2.com/\" rel=\"noopener\" target=\"_blank\">official TD-MPC2 stack</a>, which handles batched candidate rollouts, target networks, multitask action heads, and planner-state warm starts internally. That reduces the engineering burden while preserving the decoder-free planning pattern.",
        practice=dedent(
            """
            <ol>
            <li>Keep planning horizon and wall-clock budget in the same table, because latent MPC wins only if it is fast enough to matter.</li>
            <li>Warm-start the action proposal distribution from the previous planning step; this often matters as much as model accuracy.</li>
            <li>Audit terminal value bias by truncating horizon and checking whether the chosen action changes drastically.</li>
            <li>When scaling across tasks, inspect whether one shared latent still preserves task-specific geometry and actuation constraints.</li>
            </ol>
            """
        ).strip(),
        warning="Online replanning can become a latency trap. A planner that scores better on paper but misses the control deadline is operationally worse than a slightly weaker method that acts in time.",
        practical_example="A manipulator reaching around clutter may need to replan every few tens of milliseconds as the target shifts or a human enters the workspace. A decoder-free latent planner is attractive here because the action search can stay cheap. The danger is local model bias: if the latent oversmooths collision or contact dynamics, the planner will confidently choose unsafe elites.",
        frontier="TD-MPC2 opened the door to multitask latent MPC, but the frontier remains hard: how should a shared world model preserve geometry, actuation, and cost structure across many embodiments without collapsing into an average latent that is too vague for precise planning?",
        cross_ref="For classical MPC intuition, revisit <a href=\"../module-37-model-based-rl-and-mpc/index.html\">Chapter 37</a>. For control constraints and safety filters that planners must eventually obey, connect to <a href=\"../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html\">Chapter 7</a>. For offline data regimes that can pretrain the latent, see <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-25-offline-rl-and-dataset-based-robot-learning/index.html\">Chapter 25</a>.",
        self_check="Can you explain why TD-MPC2 can skip image reconstruction, what role the terminal value plays, and what measurement would tell you the planner is too slow to justify its better sample efficiency?",
        deep_dive=dedent(
            """
            <p>TD-MPC2 is a reminder that world models are not one family. Some are useful because they let you train a policy cheaply in imagination; others are useful because they let you optimize the next action online. The architecture, loss, and evaluation protocol should therefore be chosen around the intended control interface, not around visual elegance.</p>
            <p>Its broader importance is scale. The paper argues that the same core design can cover many continuous-control tasks and multi-embodiment settings. For embodied AI builders, that matters because it suggests a practical path between narrow task-specific MPC and fully general policy models.</p>
            """
        ).strip(),
        takeaway="TD-MPC2 works when the latent space is accurate enough for short-horizon search and cheap enough that online replanning fits the task's timing budget.",
        exercise="Suppose your planner improved reward by 8 percent but doubled control latency. Write the experiment table you would need to decide whether the TD-MPC2-style planner is still the right choice.",
        bibliography_cards=[
            bib_card('Hansen, N., Su, H., and Wang, X.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023). <a href="https://openreview.net/forum?id=Oxh5CstDJU" rel="noopener" target="_blank">https://openreview.net/forum?id=Oxh5CstDJU</a>', "This is the primary source for the multitask decoder-free latent MPC story."),
            bib_card('TD-MPC2 Project Page. <a href="https://www.tdmpc2.com/" rel="noopener" target="_blank">https://www.tdmpc2.com/</a>', "The project page is useful for task coverage, videos, and implementation links."),
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 remains the most important comparison point for latent imagination rather than latent MPC."),
        ],
        prev_href="section-38.4.html",
        prev_label="Section 38.4: Transformer world models (IRIS)",
        next_href="section-38.6.html",
        next_label="Section 38.6: World models for visual control",
    ),
    "38.6": dict(
        title="World models for visual control",
        image="chapter-38-illustration-05.png",
        cite="A Latent State That Must Survive Contact",
        intro_callout="Visual control is where all latent-world-model abstractions are tested at once. The representation must fuse images with proprioception, survive occlusion and contact, and still be fast enough for the control loop that actually moves hardware.",
        pathway="Read this section as a deployment checklist: choose sensors, define which hidden variables matter for the task, decide whether the latent must reconstruct images or only preserve control variables, then instrument the closed-loop failures you expect in the real robot.",
        key_insight="In hardware, the rejection decision is often more important than the nominal prediction. A world model needs a fallback story, not only a best-case story.",
        problem="A world model that looks great on benchmark rollouts can still fail the moment vision becomes ambiguous, latency spikes, or the robot makes contact. Visual control is the acid test because the learned state must handle high-dimensional sensing while preserving the low-dimensional geometry and timing that control depends on.",
        theory=dedent(
            """
            <p>A deployed visual-control latent often combines multiple sensing streams:
            $$z_t = f_\\theta\\big(\\mathrm{enc}_{\\text{vision}}(o_t^{1:m}), \\mathrm{enc}_{\\text{prop}}(q_t, \\dot q_t), a_{t-1}, h_{t-1}\\big).$$
            This matters because vision alone rarely resolves hidden contact state, while proprioception alone rarely resolves scene structure.</p>
            <p>The control objective remains the same, but rollout error should now be read through a safety lens:
            $$a_t = \\pi(z_t), \\qquad \\text{reject if } \\Pr(\\text{collision or instability} \\mid z_t) > \\tau.$$
            In practice, the world model becomes one module in a larger stack that may include a low-level stabilizer, safety filter, or reflex policy.</p>
            <p>Visual control therefore favors representations that are task-sufficient, multimodal, and timing-aware. A perfect decoder is optional. Stable contact prediction, fast inference, and recoverable failure handling are not.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Deployment Rule</div>
            <p>Fuse vision and proprioception before planning, monitor rollout confidence during execution, and hand off to a safer controller or reflex when the latent state becomes unreliable. A world model in hardware is part of a fallback architecture, not the whole architecture.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below fuses a visual embedding with proprioception and then checks whether a simple confidence gate would reject an unsafe rollout. The logic is intentionally small, because this is the boundary every hardware stack eventually needs to expose.",
        code=dedent(
            """
            # Fuse vision and proprioception, then gate execution by confidence.
            # The rejection decision is often more important than the nominal action.
            import numpy as np

            vision_latent = np.array([0.62, 0.18, 0.51])
            proprio_latent = np.array([0.55, 0.24, 0.48])
            fused = 0.7 * vision_latent + 0.3 * proprio_latent
            uncertainty = np.abs(vision_latent - proprio_latent).mean()
            execute = uncertainty < 0.08
            print({"fused_state": np.round(fused, 3).tolist(), "uncertainty": round(float(uncertainty), 3), "execute": execute})
            """
        ).strip(),
        code_output="{'fused_state': [0.599, 0.198, 0.501], 'uncertainty': 0.053, 'execute': True}",
        code_expectation="Execution should proceed only when the sensing streams agree closely enough for the controller to trust the fused state. If uncertainty stays high during contact or occlusion, the stack needs a fallback mode rather than a stronger decoder.",
        code_caption="This fusion probe shows a minimal hardware-facing contract: combine visual and proprioceptive evidence, estimate disagreement, then decide whether the action should be executed at all. In visual control, rejection logic is part of the model design, not an afterthought.",
        library_shortcut="The from-scratch fusion check is about 10 lines. In practice, teams pair world-model code with maintained robotics stacks such as <a href=\"https://github.com/huggingface/lerobot\" rel=\"noopener\" target=\"_blank\">LeRobot</a>, <a href=\"https://github.com/isaac-sim/IsaacLab\" rel=\"noopener\" target=\"_blank\">Isaac Lab</a>, or MuJoCo-based controllers. Those stacks handle sensor synchronization, rollout logging, and hardware interfaces so the world-model engineer can concentrate on state quality and failure gating.",
        practice=dedent(
            """
            <ol>
            <li>Log vision-only, proprio-only, and fused-state diagnostics separately.</li>
            <li>Define a rejection policy for latent uncertainty before the first hardware test.</li>
            <li>Stress the model with lighting change, occlusion, calibration drift, and mild contact mismatch.</li>
            <li>Measure wall-clock latency alongside task success; a stronger latent that arrives too late is still a failure.</li>
            </ol>
            """
        ).strip(),
        warning="If visual and proprioceptive streams disagree, executing the nominal action can be less safe than doing nothing or handing off to a fallback controller. Hardware world models must be calibrated for abstention.",
        practical_example="A humanoid stepping over clutter needs foot-contact timing, scene geometry, and body-state estimates in one loop. If the camera overexposes or the proprioception drifts, the latent may still look numerically plausible while the next foot placement becomes unsafe. Good visual-control pipelines therefore log disagreement, trigger fallback controllers, and treat world-model confidence as an operational signal.",
        frontier="The frontier is moving toward multimodal world models that unify camera streams, proprioception, force, and language goals while still meeting deployment latency. The unresolved issue is how to calibrate rollout confidence well enough that a real robot knows when to trust its predicted future and when to back off.",
        cross_ref="For visual sensing failure modes, revisit <a href=\"../../part-6-embodied-perception/module-27-visual-perception-for-action/index.html\">Chapter 27</a>. For contact dynamics and friction that latent rollouts often struggle with, see <a href=\"../../part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/index.html\">Chapter 6</a>. For deployment audits and safety metrics, connect to <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/index.html\">Chapter 53</a>.",
        self_check="If a world model controls hardware from vision, can you name the fallback policy, the uncertainty signal that triggers it, and the first real-world perturbation you would run before trusting the rollout horizon?",
        deep_dive=dedent(
            """
            <p>Visual control is where world models stop being abstract. The useful representation must carry geometry, embodiment, and timing in one state. That often means a multimodal latent, a shorter imagination horizon than benchmark videos suggest, and an explicit contract for when to reject the model's advice.</p>
            <p>There is also a design decision about decoding. Some teams keep an image decoder because reconstructions expose what the latent forgot. Others remove it and devote capacity to reward, value, or contact heads. The better choice depends on what failures the builder needs to diagnose and how much inference budget the controller has.</p>
            """
        ).strip(),
        takeaway="For visual control, a world model is only as good as its multimodal state quality, latency budget, and fallback behavior under uncertainty.",
        exercise="Design a rejection policy for a camera plus proprioception world model on a mobile manipulator. Which signal would trigger the fallback controller, and how would you test that threshold before deployment?",
        bibliography_cards=[
            bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "DreamerV3 remains the main reference for vision-based latent control at scale."),
            bib_card('Hansen, N., Su, H., and Wang, X.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023). <a href="https://openreview.net/forum?id=Oxh5CstDJU" rel="noopener" target="_blank">https://openreview.net/forum?id=Oxh5CstDJU</a>', "TD-MPC2 highlights the latency-sensitive, decoder-free end of the design spectrum."),
            bib_card('Hugging Face. "LeRobot." (2024). <a href="https://github.com/huggingface/lerobot" rel="noopener" target="_blank">https://github.com/huggingface/lerobot</a>', "LeRobot is a practical reference for the logging, dataset, and policy infrastructure that visual-control teams actually use."),
        ],
        prev_href="section-38.5.html",
        prev_label="Section 38.5: TD-MPC2: latent MPC at scale",
        next_href="../module-39-generative-and-video-world-models/index.html",
        next_label="Chapter 39: Generative and Video World Models",
    ),
}


chapter39_sections = {
    "39.1": dict(
        title="Generative models as learned simulators",
        image="chapter-39-illustration-01.png",
        cite="A Playable Future Must Still Obey The Task",
        intro_callout="A generative model becomes a simulator only when actions can steer it, state can persist across time, and the generated future supports the same decisions the real environment would require.",
        pathway="Start by separating renderer from simulator. Then ask which control signals enter the generator, which state variables must remain consistent over long horizons, and how you would detect a beautiful but useless video model.",
        key_insight="Simulation quality is bottlenecked by the weakest control-relevant property, not by the prettiest frame in the rollout.",
        problem="Video models can now produce visually striking futures, but robotics and autonomous systems care about more than plausibility. A simulator must preserve action consequences, reset logic, persistent objects, and failure modes. This section defines the standard that keeps generative world models from being mistaken for cinematic renderers.",
        theory=dedent(
            """
            <p>A learned simulator models future observations conditioned on action and context:
            $$p(o_{t+1:t+H} \\mid o_{\\le t}, a_{t:t+H-1}, c).$$
            The context $c$ can include text, maps, embodiment state, or scene metadata. To be useful for control, the generated futures must satisfy more than image quality: they must preserve state continuity and causal response to action.</p>
            <p>That leads to a simulator-focused evaluation vector rather than a single fidelity score:
            $$s = (\\text{controllability}, \\text{temporal consistency}, \\text{object persistence}, \\text{reset reproducibility}, \\text{task validity}).$$
            A model that is strong on only the first component, visual plausibility, is still weak as a simulator.</p>
            <p>In embodied settings, the strongest claim a generative model can make is not “this looks real,” but “a planner or policy trained on these futures learns something that transfers back to the real task.” That is a much harder objective. Teams therefore track success rate, risk, monitor-trigger statistics, and out-of-distribution behavior, not just visual preference.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Simulator Gate</div>
            <p>Condition on the current world state and action stream, generate a future, then score whether actions changed the right parts of the future, whether state stayed coherent across frames, and whether a downstream task policy benefited from training or evaluation on that future.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below turns that idea into a simple scorecard. It does not ask whether the video looks impressive; it asks which simulator property is the weakest and therefore likely to fail first in a control pipeline.",
        code=dedent(
            """
            # Score a generative world model as a simulator, not as a renderer.
            # The weakest component usually reveals the deployment bottleneck.
            metrics = {
                "controllability": 0.71,
                "temporal_consistency": 0.83,
                "object_persistence": 0.64,
                "reset_reproducibility": 0.76,
            }
            weakest = min(metrics, key=metrics.get)
            simulator_ok = min(metrics.values()) > 0.65
            print({"weakest_axis": weakest, "simulator_ok": simulator_ok})
            """
        ).strip(),
        code_output="{'weakest_axis': 'object_persistence', 'simulator_ok': False}",
        code_expectation="The model fails the simulator gate because object persistence is too weak even though the other axes look decent. That is the right conclusion for control: a missing object or identity swap breaks planning long before a slightly blurry texture does.",
        code_caption="This scorecard treats a generative world model as a bundle of simulator properties rather than one visual-quality number. The weakest axis, here object persistence, is the first place a planner or evaluator would lose trust.",
        library_shortcut="The diagnostic above is about 10 lines. In practice, the same evaluation harness can be paired with maintained platforms such as <a href=\"https://www.nvidia.com/en-us/ai/cosmos/\" rel=\"noopener\" target=\"_blank\">NVIDIA Cosmos</a>, Project Genie interfaces, or open video-model tooling built on <code>diffusers</code>, then logged through PyTorch, TensorBoard, or Weights &amp; Biases dashboards. Those systems handle generation and batching; your job is still to keep the simulator gate explicit and comparable across runs.",
        practice=dedent(
            """
            <ol>
            <li>Score controllability and persistence separately from aesthetic quality.</li>
            <li>Test reset reproducibility because planners and evaluators rely on repeatable initial conditions.</li>
            <li>Run a downstream task or policy-transfer probe whenever possible; simulation value is ultimately instrumental.</li>
            <li>Keep the real-world baseline in the same report so the simulator is never judged only against itself.</li>
            </ol>
            """
        ).strip(),
        warning="A visually convincing model can still be a dangerous simulator if object identity, action semantics, or resets drift under rollout. Never let aesthetics stand in for causal validity.",
        practical_example="An autonomous-driving team may generate heavy-rain scenes that look convincing but silently drop a cyclist after two seconds of occlusion. A perception benchmark might still look fine frame by frame. A closed-loop planner, however, would learn the wrong threat model. That is exactly why simulator metrics must include persistence and action-conditioned consistency.",
        frontier="The research frontier is shifting from passive video generation toward interactive world models with explicit action channels, persistent agents, and embodied evaluation protocols. The hard unresolved question is how to prove that the generated futures preserve the decision boundaries that matter for the downstream robot or vehicle.",
        cross_ref="For synthetic-data pipelines and domain randomization, see <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/index.html\">Chapter 13</a>. For robot evaluation hygiene, connect to <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html\">Chapter 52</a>. For latent state models that do not decode photorealistic video, compare this section with <a href=\"../module-38-latent-world-models/index.html\">Chapter 38</a>.",
        self_check="Can you list two properties that make a video model look realistic and two stricter properties that make it usable as a simulator for policy learning or evaluation?",
        deep_dive=dedent(
            """
            <p>The central conceptual shift is from generative quality to decision quality. A renderer can hallucinate around the edges and still impress a viewer. A simulator cannot, because the missing or inconsistent detail often changes what the agent should do next. That is why embodied AI researchers increasingly treat world-model demos from systems such as Sora, Genie, or Cosmos as hypotheses that need task-grounded validation rather than as finished evidence.</p>
            <p>This also explains why the best generative simulators are often paired with old-fashioned bookkeeping: structured prompts, reset manifests, object-identity checks, and downstream transfer tests. The glamorous part is video generation; the reliable part is evaluation discipline, often implemented in custom replay harnesses plus maintained generation backends such as Diffusers or Cosmos.</p>
            """
        ).strip(),
        takeaway="A generative model is a simulator only when its futures are steerable, persistent, and useful for the same decisions the real environment demands.",
        exercise="Define a five-axis simulator scorecard for one embodied application you care about. Which axis would you expect to fail first, and how would you measure it with one reproducible artifact?",
        bibliography_cards=[
            bib_card('OpenAI. "Video Generation Models as World Simulators." (2024). <a href="https://openai.com/index/video-generation-models-as-world-simulators/" rel="noopener" target="_blank">https://openai.com/index/video-generation-models-as-world-simulators/</a>', "The Sora report is a key statement of the world-simulator framing from the video-generation side."),
            bib_card('NVIDIA. "Physical AI with World Foundation Models." (2026). <a href="https://www.nvidia.com/en-us/ai/cosmos/" rel="noopener" target="_blank">https://www.nvidia.com/en-us/ai/cosmos/</a>', "The Cosmos platform is a current primary source for physical-AI oriented simulator claims."),
            bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "Genie 3 represents the interactive-world-model line that explicitly pushes beyond passive videos."),
        ],
        prev_href="index.html",
        prev_label="Chapter 39: Generative and Video World Models",
        next_href="section-39.2.html",
        next_label="Section 39.2: Genie 1-3: interactive, playable...",
    ),
    "39.2": dict(
        title="Genie 1-3: interactive, playable world models",
        image="chapter-39-illustration-02.png",
        cite="A World That Responds To You",
        intro_callout="The Genie line is important because it makes interactivity explicit. Instead of merely predicting the next frame, it asks whether a generated world can be stepped through, controlled, and kept coherent as actions accumulate.",
        pathway="Read this section as a lineage. Genie begins with learned latent actions from video, expands into large-scale interactive world generation in Genie 2, and then moves toward photorealistic real-time exploration in Genie 3 and Project Genie.",
        key_insight="Interactivity is a stronger test than next-frame quality. Every extra action exposes whether the world model actually preserved causal state or only short-term visual momentum.",
        problem="Many video models can continue a clip, but a world model for embodied AI must do something stricter: respond to the user's or agent's actions while keeping the environment coherent. Genie matters because it frames interactivity, not only fidelity, as the main benchmark for progress.",
        theory=dedent(
            """
            <p>The early Genie formulation learns a latent action interface from unlabeled videos:
            $$p(o_{t+1} \\mid o_{\\le t}, u_t),$$
            where $u_t$ is a learned latent action that stands in for the unknown control responsible for the next frame. This is powerful because internet videos rarely come with button presses or motor torques attached.</p>
            <p>Later systems move toward explicit or user-facing interactivity. Genie 2 is presented by Google DeepMind as a large-scale foundation world model for diverse 3D environments, while Genie 3 is described as a general-purpose interactive world model capable of generating photorealistic environments that can be explored in real time. The conceptual progression is from inferred latent control to more explicit, controllable world simulation.</p>
            <p>The important scientific point is that interactivity is a much stronger demand than next-frame prediction. The model must preserve state variables over many steps, respond causally to actions, and avoid drifting into visually plausible but unplayable nonsense. In a practical benchmark, that means replaying the same action script through Genie-like systems, Project Genie interfaces, or other interactive generators and checking whether later states still encode the same intended control semantics, uncertainty, and controllability objective.</p>
            <p>Another way to say this formally is that the state-space dynamics induced by the generator should preserve the policy-relevant variables over horizon, not only the pixels. If the uncertainty over latent action consequences grows faster than the useful horizon, the interactive world stops being a trustworthy training environment.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Interactive World-Model Test</div>
            <p>Initialize the world from a prompt or context frame, apply an action sequence, render the resulting trajectory, then check whether the state transition pattern matches the intended action semantics over many steps rather than only the first step.</p>
            </div>
            """
        ).strip(),
        code_intro="The tiny evaluation loop below mirrors what makes the Genie family interesting: repeated action following. It accumulates a score across multiple steps, because single-step obedience is much easier than long-horizon interactive consistency.",
        code=dedent(
            """
            # Score whether an interactive world follows actions over time.
            # A few good first steps do not rescue long-horizon drift.
            intended = ["left", "left", "jump", "right"]
            observed = ["left", "left", "jump", "idle"]
            step_scores = [int(i == o) for i, o in zip(intended, observed)]
            action_follow_rate = sum(step_scores) / len(step_scores)
            print({"step_scores": step_scores, "action_follow_rate": round(action_follow_rate, 2)})
            """
        ).strip(),
        code_output="{'step_scores': [1, 1, 1, 0], 'action_follow_rate': 0.75}",
        code_expectation="The sequence shows why interactive evaluation is sequential. The world followed the first three actions correctly and then drifted on the last step. A polished screenshot from the first frame would miss the exact failure that matters for agent training.",
        code_caption="This sequential score highlights the central Genie requirement: actions must keep meaning the same thing over repeated interaction. The last-step failure is more informative than a frame-level visual score because it reveals horizon breakdown.",
        library_shortcut="There is no fully open one-line Genie SDK for all versions, so the practical shortcut is conceptual rather than purely programmatic: use the official <a href=\"https://labs.google/projectgenie\" rel=\"noopener\" target=\"_blank\">Project Genie</a> or Google DeepMind materials to define the interaction contract, then wrap that contract inside your own benchmark harness. The maintained tool handles generation; your code should handle action scripts, scoring, replay storage, and if needed token-level analysis with PyTorch, JAX, and standard transformer tooling.",
        practice=dedent(
            """
            <ol>
            <li>Evaluate with action scripts, not free-form visual inspection.</li>
            <li>Report how performance decays with horizon, because many interactive models fail gradually.</li>
            <li>Separate prompt diversity from control fidelity; a model can be creative and still be a weak simulator.</li>
            <li>Keep latent-action systems and explicit-action systems in distinct tables so readers do not confuse the control interfaces.</li>
            </ol>
            """
        ).strip(),
        warning="A generated world that follows the first few commands well can still become unusable when horizons extend. Early-step success should not be mistaken for a stable interactive simulator.",
        practical_example="A warehouse-navigation agent trained in an interactive generated world may learn useful avoidance behavior if doors, shelves, and people remain persistent under actions. If the world reinterprets the same joystick command differently from one step to the next, the resulting policy learns to exploit generative quirks rather than real navigation structure.",
        frontier="The immediate frontier is richer, longer, more controllable interactive worlds. The deeper frontier is interface design: how should language, joystick commands, robot actions, and latent actions be represented so that generated environments remain causally stable enough for serious agent research?",
        cross_ref="For action-conditioned video as a policy-learning substrate, connect this section to <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/index.html\">Chapter 22</a>. For simulation and benchmark concerns, revisit <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-12-benchmarks-and-task-suites/index.html\">Chapter 12</a>. For the broader world-model landscape, compare with <a href=\"section-39.4.html\">Section 39.4</a> on Cosmos.",
        self_check="Can you explain the difference between a latent-action world model trained from raw video and an interactive world model exposed directly to user or agent commands?",
        deep_dive=dedent(
            """
            <p>The Genie line matters because it makes a missing assumption visible. Much of classic video prediction quietly assumes the action stream is known. Internet video does not provide that. By learning or inferring a control interface, Genie opens a path from passive observation datasets toward interactive world models, while Project Genie and later Google DeepMind demos expose how that interface behaves under repeated user control, replay monitoring, and success-rate style evaluation.</p>
            <p>That does not mean the problem is solved. The more interactive a generated world becomes, the more it exposes its weaknesses: state drift, identity swaps, and ambiguous control semantics. In this sense, interactivity is not only a capability showcase. It is a stronger microscope for world-model failure.</p>
            """
        ).strip(),
        takeaway="The real advance in the Genie family is not prettier video but stronger interactivity, because a world model that cannot be steered cannot train or evaluate agents reliably.",
        exercise="Design a benchmark script for an interactive world model with four fixed action sequences. Which metrics would tell you whether the environment is merely reactive at one step or genuinely coherent over time?",
        bibliography_cards=[
            bib_card('Edwards, A. et al.. "Genie: Generative Interactive Environments." (2024). <a href="https://arxiv.org/abs/2402.15391" rel="noopener" target="_blank">https://arxiv.org/abs/2402.15391</a>', "The original Genie paper introduces latent actions learned from video and frames the interactive-environment problem clearly."),
            bib_card('Google DeepMind. "Genie 2: A Large-Scale Foundation World Model." (2024). <a href="https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/</a>', "Genie 2 is the official source for the large-scale 3D environment direction."),
            bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "Genie 3 is the current official reference for real-time, photorealistic interactive worlds in this family."),
        ],
        prev_href="section-39.1.html",
        prev_label="Section 39.1: Generative models as learned simulators",
        next_href="section-39.3.html",
        next_label="Section 39.3: Video generation as world simulation...",
    ),
    "39.3": dict(
        title="Video generation as world simulation: Sora and successors",
        image="chapter-39-illustration-03.png",
        cite="A Video Model That Starts To Behave Like Physics",
        intro_callout="Sora pushed the idea that large video models can acquire simulation-like structure. The key question for embodied AI is how much of that structure survives when the model is asked to support action and decision-making rather than passive viewing.",
        pathway="Follow the distinction between physical-looking coherence and control-relevant coherence. The section is not about whether the clips are visually striking, but whether the learned dynamics resemble a world you could actually plan in.",
        key_insight="Photorealism is evidence of structure, not proof of control reliability. For embodied work, intervention is the real exam.",
        problem="Scaled video generation can model cameras, objects, and motion with surprising realism, but agents do not need beautiful movies, they need futures that remain causally trustworthy when actions intervene. This section exists to sort out what is genuinely useful in the Sora-style framing and what still falls short for embodied control.",
        theory=dedent(
            """
            <p>The Sora report popularized the phrase “video generation models as world simulators.” The intuition is that predicting long coherent video forces the model to internalize structure about objects, geometry, and motion. At a high level, the generator learns a conditional distribution over future frames:
            $$p(o_{t+1:t+H} \\mid o_{\\le t}, c),$$
            where $c$ may include text or image context.</p>
            <p>For embodied AI, however, one more argument is required: the latent geometry learned for passive generation must remain useful under intervention. That missing action channel is why Sora-style models are best viewed as evidence that large video models can encode world regularities, not as immediate replacements for explicit action-conditioned simulators.</p>
            <p>The right scientific reading is therefore cautious. Photorealism can signal that the model has learned some structure of the world, but it can also mislead the reader into overestimating causal faithfulness. Real simulation requires identity persistence, controllability, and task validity under action.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Successor Test</div>
            <p>Take a visually compelling video world model, inject action or control signals if available, then measure whether the model preserves object identities and task outcomes over a long horizon. If not, treat it as a rich prior for synthetic scenes, not as a policy-training simulator.</p>
            </div>
            """
        ).strip(),
        code_intro="The following diagnostic checks whether one object keeps the same identity across a short generated clip. That sounds simple, but it is exactly where photorealistic video models can look plausible while silently losing the world state a planner needs.",
        code=dedent(
            """
            # Audit object identity persistence across generated frames.
            # A simulator fails if objects silently change identity mid-rollout.
            object_ids = ["forklift", "forklift", "forklift", "unknown", "forklift"]
            persistent = sum(obj == "forklift" for obj in object_ids) / len(object_ids)
            first_break = next(i for i, obj in enumerate(object_ids) if obj != "forklift")
            print({"persistence_rate": round(persistent, 2), "first_break_frame": first_break})
            """
        ).strip(),
        code_output="{'persistence_rate': 0.8, 'first_break_frame': 3}",
        code_expectation="The failure at frame 3 is the meaningful result. The clip can still look globally coherent, but if the object identity breaks that early, any planner using the clip as a simulated future would be reasoning over the wrong state.",
        code_caption="This identity audit illustrates why visual smoothness is not enough. A single mid-rollout identity failure can invalidate the entire future for planning, evaluation, or synthetic-data generation.",
        library_shortcut="The diagnostic itself is tiny, but the practical shortcut for experimenting with video-model backbones is the <code>diffusers</code> ecosystem, which can reduce a custom sampler to a few lines while handling schedulers, device placement, and checkpoint loading internally. That does not make the result a simulator by itself, but it does make controlled evaluation of successor models much easier.",
        practice=dedent(
            """
            <ol>
            <li>Use photorealistic video models first as synthetic-scene priors or evaluation stressors, not automatically as full control simulators.</li>
            <li>Measure object identity and event persistence over time, because those failures often appear before gross visual collapse.</li>
            <li>If an action channel exists, test counterfactual prompts or control signals that should produce sharply different futures.</li>
            <li>Keep a clear note in reports separating vendor-reported visual capability from independently measured simulator capability.</li>
            </ol>
            """
        ).strip(),
        warning="Do not promote a passive video model to a control simulator just because the clip looks physically plausible. Without action-grounded evidence, the safest claim is still limited.",
        practical_example="A humanoid policy team might use a Sora-like model to generate rare recovery scenes, such as slippery floors or falling objects, then evaluate whether perception modules remain robust. That is already useful. It is still different from claiming the model can replace contact-accurate control simulation for training the whole policy.",
        frontier="The frontier around Sora-style systems is hybridization: combine rich visual generation with stronger action conditioning, structured control interfaces, or external physics constraints. The open question is whether that route can preserve photorealism while gaining the causal reliability required by embodied policies.",
        cross_ref="For diffusion-based action generation, revisit <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-22-action-chunking-and-diffusion-policies/index.html\">Chapter 22</a>. For synthetic evaluation and domain randomization, connect to <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/index.html\">Chapter 13</a>. For the stricter evaluation checklist, continue to <a href=\"section-39.7.html\">Section 39.7</a>.",
        self_check="What is the strongest useful claim you would allow a Sora-style model to make in an embodied pipeline today, and what stronger claim would still require action-conditioned evidence?",
        deep_dive=dedent(
            """
            <p>The reason Sora matters in this book is not that every robotics team should use it directly. It matters because it changed the prior about what large video models can internalize: geometry, continuity, and multi-object interaction may emerge to a meaningful degree under pure generative training.</p>
            <p>The embodied systems lesson is more conservative. Emergent structure is promising, but agents need explicit contracts. Until action, persistence, and task validity are measured together, the right role for these models is often augmentation, analysis, or synthetic stress testing rather than closed-loop policy training.</p>
            """
        ).strip(),
        takeaway="Photorealistic video can be evidence of learned world structure, but it becomes a usable simulator only when that structure remains stable under intervention and task evaluation.",
        exercise="Write two different capability claims for a Sora-like model: one claim you would accept after visual inspection plus persistence tests, and one stronger claim you would refuse without action-conditioned transfer evidence.",
        bibliography_cards=[
            bib_card('OpenAI. "Video Generation Models as World Simulators." (2024). <a href="https://openai.com/index/video-generation-models-as-world-simulators/" rel="noopener" target="_blank">https://openai.com/index/video-generation-models-as-world-simulators/</a>', "This is the primary source for the Sora-style world-simulator framing."),
            bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "Genie provides a useful comparison because it makes interactivity more explicit."),
            bib_card('Hugging Face Diffusers Documentation. <a href="https://huggingface.co/docs/diffusers/index" rel="noopener" target="_blank">https://huggingface.co/docs/diffusers/index</a>', "Diffusers is the most practical maintained toolkit for experimenting with open diffusion-style video model components."),
        ],
        prev_href="section-39.2.html",
        prev_label="Section 39.2: Genie 1-3: interactive, playable...",
        next_href="section-39.4.html",
        next_label="Section 39.4: NVIDIA Cosmos: world foundation...",
    ),
    "39.4": dict(
        title="NVIDIA Cosmos: world foundation models for physical AI",
        image="chapter-39-illustration-04.png",
        cite="A Platform That Treats World Models As Infrastructure",
        intro_callout="Cosmos is notable because it turns world modeling into a developer platform for physical AI rather than a single research demo. The framing is practical: robots, autonomous vehicles, and smart environments need data pipelines, tokenizers, guardrails, and evaluation tooling around the model itself.",
        pathway="Read this section as a systems stack. The world model is only one layer. Around it sit tokenizers, synthetic-data generation paths, transfer tools, guardrails, and post-training workflows specialized for physical AI.",
        key_insight="The platform is the point. A large generator without tokenization, manifests, and evaluation loops is still not enough for physical-AI engineering, even if the underlying PyTorch checkpoints or Isaac assets look strong in isolation.",
        problem="Many world-model papers stop at one benchmark or one model family. Physical AI teams need something broader: a way to generate and transfer scenarios, train customized models, and evaluate policies at scale. Cosmos matters because it explicitly presents world models as platform infrastructure for those tasks.",
        theory=dedent(
            """
            <p>The Cosmos platform frames a world foundation model as a general-purpose model that can be specialized into downstream world models for robots, vehicles, or smart infrastructure. In that framing, the generator is part of a larger map:
            $$\\text{context} \\rightarrow \\text{world model} \\rightarrow \\text{synthetic data / simulation / action model} \\rightarrow \\text{policy evaluation}. $$</p>
            <p>The 2025 platform paper emphasizes digital-first physical AI: learn a policy model, a digital twin of the agent, and a digital twin of the world before expensive real-world iteration. More recent official NVIDIA materials position Cosmos 3 as an open omnimodal world model that connects understanding, generation, simulation, and action across text, image, video, audio, and actions.</p>
            <p>The scientific point for readers is that scale alone is not the story. Cosmos couples scale with tooling: tokenizers, transfer models, distributed pipelines, and benchmarks that try to make synthetic world generation operational for embodied development rather than merely impressive in a demo reel.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Physical-AI Platform Loop</div>
            <p>Curate multimodal world data, post-train a world model on embodiment-specific context, generate scenarios or synthetic trajectories, evaluate policies on matched panels, then feed the failures back into the data and post-training pipeline. The platform value lies in the loop, not only in the base model.</p>
            </div>
            """
        ).strip(),
        code_intro="The manifest below captures the kind of scenario specification a physical-AI world-model platform needs. It is less glamorous than the generator, but without this contract synthetic data cannot be audited or compared across robots and vehicles.",
        code=dedent(
            """
            # Describe one physical-AI scenario for a world-model pipeline.
            # Structured manifests make synthetic data auditable and reusable.
            scenario = {
                "camera_setup": "front-left, front-right, wrist",
                "embodiment": "warehouse manipulator",
                "task": "bin pick with occluded package",
                "stressors": ["dim light", "forklift crossing"],
                "evaluation_target": "pick success without emergency stop",
            }
            print({"fields": len(scenario), "task": scenario["task"]})
            """
        ).strip(),
        code_output="{'fields': 5, 'task': 'bin pick with occluded package'}",
        code_expectation="The output is simple by design. A usable platform starts from well-specified scenario manifests, because every synthetic video, rollout, or evaluation artifact must be traceable back to a concrete embodiment and task contract.",
        code_caption="This manifest demonstrates the infrastructure view of world models. The generator is only useful when scenario metadata, embodiment assumptions, and evaluation targets are explicit enough to reproduce downstream policy results.",
        library_shortcut="A handwritten manifest is trivial, but the real shortcut is the <a href=\"https://github.com/NVIDIA/cosmos\" rel=\"noopener\" target=\"_blank\">NVIDIA Cosmos</a> ecosystem and related repositories such as <a href=\"https://github.com/NVIDIA/Cosmos-Tokenizer\" rel=\"noopener\" target=\"_blank\">Cosmos-Tokenizer</a>, <a href=\"https://github.com/NVIDIA/cosmos-framework\" rel=\"noopener\" target=\"_blank\">Cosmos-Framework</a>, and the transfer-model repositories such as Cosmos-Transfer. In practice these are often paired with PyTorch serving, Isaac simulation assets, TensorBoard, and Weights &amp; Biases evaluation runs. They absorb model packaging, tokenization, serving, and distributed workflow glue that would otherwise take hundreds of lines to rebuild.",
        practice=dedent(
            """
            <ol>
            <li>Version every scenario manifest together with the generated assets.</li>
            <li>Keep transfer, generation, and evaluation outputs in separate folders so you can trace which stage introduced a failure.</li>
            <li>Do not compare robot and vehicle results unless the synthetic-world contract is matched on camera layout, horizon, and task definition.</li>
            <li>Evaluate whether the platform shortens the policy-improvement loop, not merely whether it produces realistic videos.</li>
            </ol>
            """
        ).strip(),
        warning="Platform scale can hide domain mismatch. If the scenario manifest and evaluation contract are vague, a large world-model stack can produce polished artifacts that are still useless for the actual robot or vehicle task.",
        practical_example="A warehouse robotics team may use Cosmos-style world models to synthesize rare crossing-traffic scenes, then evaluate a grasping or navigation policy on that edge-case panel before new hardware tests. The productivity gain comes from platform reuse: once the scenario and evaluation contract exist, new world-model variants can be compared quickly and systematically with PyTorch services, Isaac scenes, OpenCV inspection tools, and TensorBoard traces.",
        frontier="The frontier here is platform integration. Teams are moving toward world models that not only generate scenes but also support transfer from simulation to camera domains, generate action-conditioned futures, and plug directly into evaluation loops for robots and autonomous vehicles. The open question is how much of that stack can remain open, auditable, and reproducible as the models grow larger.",
        cross_ref="For synthetic data and randomization strategy, revisit <a href=\"../../part-3-simulation-tooling-and-the-modern-stack/module-13-domain-randomization-and-synthetic-data/index.html\">Chapter 13</a>. For robot datasets and scaling laws that feed world models, connect to <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/index.html\">Chapter 24</a>. For deployment concerns, compare with <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html\">Chapter 55</a>.",
        self_check="Can you explain why a world-model platform needs tokenizers, manifests, and evaluation pipelines in addition to a large generator, and which of those pieces you would audit first after a synthetic-data failure?",
        deep_dive=dedent(
            """
            <p>Cosmos is useful pedagogically because it widens the frame. It reminds the reader that embodied AI teams do not adopt world models in isolation. They adopt pipelines: tokenization, generation, transfer, safety checks, serving, and evaluation. A model can be scientifically interesting and still be operationally weak if those surrounding tools are missing. Cosmos-Tokenizer, Cosmos-Framework, PyTorch inference services, JAX post-training experiments, Isaac assets, OpenCV diagnostics, and the public platform repositories make that tooling layer unusually visible.</p>
            <p>The recent Cosmos 3 materials also point toward omnimodal integration, where action is no longer a side channel but part of the shared model vocabulary. That is a strong signal about where the field is heading, even if each application domain still needs careful benchmarking before the platform claims can be trusted locally.</p>
            """
        ).strip(),
        takeaway="Cosmos matters because it treats world models as physical-AI infrastructure: generation, transfer, tokenization, and evaluation all have to work together for the model to matter in practice.",
        exercise="Pick one physical-AI application, such as a warehouse arm or an autonomous vehicle, and write the scenario manifest fields you would require before accepting synthetic data from a Cosmos-style pipeline.",
        bibliography_cards=[
            bib_card('NVIDIA. "Physical AI with World Foundation Models." (2026). <a href="https://www.nvidia.com/en-us/ai/cosmos/" rel="noopener" target="_blank">https://www.nvidia.com/en-us/ai/cosmos/</a>', "The main product and ecosystem page is the current primary source for Cosmos capabilities and tooling."),
            bib_card('NVIDIA Research. "Cosmos World Foundation Model Platform for Physical AI." (2025). <a href="https://arxiv.org/abs/2501.03575" rel="noopener" target="_blank">https://arxiv.org/abs/2501.03575</a>', "The platform paper explains the digital-first physical-AI framing."),
            bib_card('NVIDIA. "NVIDIA/cosmos GitHub Repository." (2026). <a href="https://github.com/NVIDIA/cosmos" rel="noopener" target="_blank">https://github.com/NVIDIA/cosmos</a>', "The repository provides the most concrete public entry point into the platform stack."),
        ],
        prev_href="section-39.3.html",
        prev_label="Section 39.3: Video generation as world simulation...",
        next_href="section-39.5.html",
        next_label="Section 39.5: GameNGen and Oasis: neural game engines",
    ),
    "39.5": dict(
        title="GameNGen and Oasis: neural game engines",
        image="chapter-39-illustration-05.png",
        cite="A World Model That Tries To Replace The Engine",
        intro_callout="GameNGen and Oasis are useful because they make the claim maximally concrete: the model is not only predicting a future clip, it is trying to serve as the interactive engine itself.",
        pathway="Compare the two systems through the lens of controllability and substrate. GameNGen shows a diffusion-based neural engine for a classic game; Oasis shows an interactive generated world that exposed both the promise and instability of frame-by-frame generative environments.",
        key_insight="When the model becomes the engine, compounding error stops being abstract. It shows up immediately as broken affordances, drifting map logic, or controls that lose their meaning.",
        problem="A world model can assist simulation, or it can attempt to become the simulator. Neural game engines matter because they reveal what breaks when the model itself must sustain interactive dynamics in real time, not merely continue a clip or produce synthetic training data offline.",
        theory=dedent(
            """
            <p>GameNGen models an interactive environment by predicting the next frame conditioned on past frames and actions, then reusing its own output autoregressively. The challenge is compounding error:
            $$o_{t+1} \\sim p_\\theta(o_{t+1} \\mid o_{\\le t}, a_t), \\qquad o_{t+k} \\text{ depends on generated } o_{t+1:t+k-1}.$$
            Every small artifact can become part of the state the next step conditions on.</p>
            <p>The GameNGen paper is important because it reports real-time interactive simulation of DOOM with a diffusion model and foregrounds long-trajectory stability as a central technical hurdle. Oasis, first framed as an AI-generated game world and more recently extended toward physical-AI uses, exposed the same phenomenon publicly: interactivity is compelling, but state drift and inconsistency quickly become visible when the model is the engine.</p>
            <p>The lesson for embodied AI is that real-time generation pressure is informative. It reveals whether the model's internal state is robust enough to support long action loops rather than just short cinematic continuations.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Neural Engine Stress Test</div>
            <p>Run repeated user or agent actions through the model in real time, track whether identities, map structure, and action semantics remain stable, and count how long the world remains playable before semantic drift or catastrophic resets appear.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below measures playable horizon. It counts how many interactive steps remain semantically valid before the neural engine drifts out of the task manifold.",
        code=dedent(
            """
            # Count how long a neural game engine remains semantically valid.
            # Horizon matters more than one impressive generated screenshot.
            validity = [1, 1, 1, 1, 0, 0]
            playable_horizon = validity.index(0)
            survival_rate = sum(validity) / len(validity)
            print({"playable_horizon": playable_horizon, "survival_rate": round(survival_rate, 2)})
            """
        ).strip(),
        code_output="{'playable_horizon': 4, 'survival_rate': 0.67}",
        code_expectation="The model remains semantically valid for four steps before drift appears. That is the relevant operational metric for an interactive engine, because the first few frames may look convincing even when the loop is already unstable.",
        code_caption="This horizon counter captures the central challenge in neural engines: generated state becomes future input. Once semantic validity breaks, later frames are no longer merely low quality, they are the wrong world.",
        library_shortcut="There is not yet a single stable, open, plug-and-play neural-engine library that erases all of this complexity. The practical shortcut is to use the official <a href=\"https://gamengen.github.io/\" rel=\"noopener\" target=\"_blank\">GameNGen project materials</a> or the <a href=\"https://oasis-model.github.io/\" rel=\"noopener\" target=\"_blank\">Oasis project page</a> as reference implementations, then wrap them in your own horizon and controllability harness rather than treating the demo itself as the benchmark.",
        practice=dedent(
            """
            <ol>
            <li>Report playable horizon explicitly.</li>
            <li>Store action traces next to generated clips so replay can reveal whether drift was visual, semantic, or control-related.</li>
            <li>Measure control lag, because real-time feel is part of the engine claim.</li>
            <li>Use neural engines for stress testing and representation research before trusting them as full control simulators.</li>
            </ol>
            """
        ).strip(),
        warning="Real-time interactivity can make weak models look stronger than they are because the early frames are impressive. Always score playable horizon, not only first-frame fidelity or short clips.",
        practical_example="An embodied-navigation researcher can use a neural engine to explore how an agent reacts to unusual corridor layouts or moving distractors. That is valuable for stress testing. It is different from using the engine as the sole truth source for collision-rich control, because one semantic glitch in the generated world can invalidate the policy lesson.",
        frontier="The frontier is convergence between neural engines, interactive world models, and physical-AI platforms. GameNGen and Oasis showed that real-time interaction is possible. The open problem is how to keep that interaction semantically stable for long horizons and safety-critical tasks rather than only for demos or entertainment-oriented environments.",
        cross_ref="For interactive world models with stronger platform ambitions, continue to <a href=\"section-39.4.html\">Section 39.4</a>. For evaluation methodology, jump ahead to <a href=\"section-39.7.html\">Section 39.7</a>. For model-based control in compact latent spaces rather than fully generated frames, compare with <a href=\"../module-38-latent-world-models/section-38.5.html\">Section 38.5</a>.",
        self_check="What is the difference between a neural game engine that looks convincing for ten seconds and one that is reliable enough to support agent research or safety evaluation?",
        deep_dive=dedent(
            """
            <p>These systems are educational because they expose compounding error in the most intuitive possible way: the world stops making sense. In a benchmark table that may appear as a fidelity drop. In an interactive engine it appears as broken affordances, shifting geometry, or controls that stop meaning the same thing across time.</p>
            <p>The public fascination with Oasis was therefore scientifically useful. It showed many people, very quickly, what researchers already know: when a generative model becomes the environment, persistence and action semantics become the whole game.</p>
            """
        ).strip(),
        takeaway="Neural game engines are the sharpest stress test for generative world models because compounding error becomes immediately visible as broken interactivity.",
        exercise="Design a replay artifact for a neural engine benchmark. Which fields would you save so another researcher could diagnose whether failure came from control lag, semantic drift, or object-identity collapse?",
        bibliography_cards=[
            bib_card('Valevski, D. et al.. "Diffusion Models Are Real-Time Game Engines." (2024). <a href="https://arxiv.org/abs/2408.14837" rel="noopener" target="_blank">https://arxiv.org/abs/2408.14837</a>', "GameNGen is the primary academic reference for a real-time neural engine."),
            bib_card('GameNGen Project Page. <a href="https://gamengen.github.io/" rel="noopener" target="_blank">https://gamengen.github.io/</a>', "The project page is useful for demonstrations and reported metrics."),
            bib_card('Oasis Project Page. <a href="https://oasis-model.github.io/" rel="noopener" target="_blank">https://oasis-model.github.io/</a>', "Oasis is a concrete public reference for interactive generated worlds and their limitations."),
        ],
        prev_href="section-39.4.html",
        prev_label="Section 39.4: NVIDIA Cosmos: world foundation...",
        next_href="section-39.6.html",
        next_label="Section 39.6: Using generative world models for data...",
    ),
    "39.6": dict(
        title="Using generative world models for data and evaluation (e.g., humanoid pipelines)",
        image="chapter-39-illustration-05.png",
        cite="Synthetic Worlds Need Audit Trails",
        intro_callout="Generative world models become immediately useful when they generate edge cases, rare combinations, or evaluation panels that would be slow or dangerous to collect in the real world. The challenge is keeping those synthetic worlds matched to the task you actually care about.",
        pathway="Follow the pipeline from scenario specification to generation to task evaluation. Every gain in data volume or scenario diversity must be checked against one risk: the synthetic world may shift the policy toward solving artifacts rather than the intended task.",
        key_insight="Synthetic data is best treated as a targeted experiment, not as a wholesale substitute for real experience. Coverage helps only when causal structure stays aligned and the training monitor still agrees with real-world success rate.",
        problem="Humanoids, mobile manipulators, and autonomous vehicles all suffer from sparse exposure to rare but important events. Generative world models promise to fill that gap, but they can also inject unrealistic correlations or shortcut cues. This section is about using generated worlds as training or evaluation assets without fooling yourself about transfer.",
        theory=dedent(
            """
            <p>Let $\\mathcal{D}_{\\text{real}}$ be the observed dataset and $\\mathcal{D}_{\\text{gen}}$ the generated dataset. A simple mixture view is:
            $$\\mathcal{D}_{\\text{mix}} = \\alpha \\mathcal{D}_{\\text{real}} + (1-\\alpha) \\mathcal{D}_{\\text{gen}}.$$
            The benefit grows when $\\mathcal{D}_{\\text{gen}}$ covers rare but task-relevant states; the risk grows when generated states alter the causal structure of the task.</p>
            <p>For evaluation, the logic is similar but stricter. A generated panel is useful when it systematically probes failure modes that are hard to capture in the field, such as sudden lighting change, near-collision geometry, or unusual human motion. The panel is misleading when it adds unrealistic shortcuts that inflate performance.</p>
            <p>Humanoid pipelines sharpen this tradeoff because balance, contact timing, and recovery dynamics are fragile. A visually plausible synthetic clip may still miss the contact transitions that determine whether the policy falls.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Synthetic Data Gate</div>
            <p>Specify the rare event you want more of, generate the scenario family, run a matched policy evaluation on real and synthetic panels, and accept the synthetic data only if it improves the intended robustness metric without degrading transfer on the untouched real validation set.</p>
            </div>
            """
        ).strip(),
        code_intro="The probe below computes a simple mixture ledger. The goal is not to maximize synthetic share blindly, but to keep track of how much real supervision anchors the generated edge cases.",
        code=dedent(
            """
            # Track how much of a training mix comes from generated worlds.
            # The ledger matters because synthetic coverage and synthetic bias rise together.
            real_episodes = 320
            generated_episodes = 180
            synthetic_fraction = generated_episodes / (real_episodes + generated_episodes)
            print({"synthetic_fraction": round(synthetic_fraction, 2), "real_anchor_kept": synthetic_fraction < 0.5})
            """
        ).strip(),
        code_output="{'synthetic_fraction': 0.36, 'real_anchor_kept': True}",
        code_expectation="A moderate synthetic fraction can be healthy because real data still anchors the task. The number itself is not universal, but the ledger forces the team to state how much of the policy's experience came from generated worlds before they interpret transfer results.",
        code_caption="This mixture ledger turns a vague training recipe into an auditable data contract. Without it, teams often cannot explain whether a transfer failure came from insufficient synthetic coverage or too much synthetic bias.",
        library_shortcut="The bookkeeping is only a few lines, but the practical shortcut is to pair it with generated-scenario platforms such as Cosmos, Project Genie-style interfaces, or open data stacks such as LeRobot and Open X-Embodiment while keeping the ledger in your own training and evaluation code. Teams often log those runs through PyTorch-based trainers, Isaac or MuJoCo validation scenes, and TensorBoard or Weights &amp; Biases dashboards. The platform generates the worlds; your pipeline must preserve the provenance and the real-versus-generated split explicitly.",
        practice=dedent(
            """
            <ol>
            <li>Generate synthetic data for named failure modes, not for generic volume.</li>
            <li>Keep real-only, synthetic-only, and mixed evaluations side by side.</li>
            <li>Inspect whether the policy learned cues that exist only in the generated worlds.</li>
            <li>For humanoids and contact-rich robots, prioritize edge cases tied to balance recovery, occlusion, or human interaction over purely cosmetic variation.</li>
            </ol>
            """
        ).strip(),
        warning="Generated worlds can teach the wrong lesson faster than real data can. If a policy improves only on synthetic panels while slipping on untouched real validation, the synthetic coverage is probably injecting a shortcut.",
        practical_example="A humanoid locomotion team may synthesize slippery-floor or moving-obstacle scenes that are too risky to over-sample on hardware. The generated data is valuable when it teaches early recovery behavior and preserves contact timing. It is harmful if the synthetic world makes falls too predictable or textures correlate spuriously with safe footholds. In practice, teams often compare those runs in PyTorch trainers against Isaac or MuJoCo validation scenes while watching TensorBoard or Weights &amp; Biases dashboards for real-versus-synthetic drift.",
        frontier="The most promising direction is targeted synthetic coverage: use world models to generate the exact corner cases that real data lacks, then verify those cases with matched real-world probes. The hardest open problem is causal fidelity, especially for contact-rich humanoid and manipulation tasks where small errors can change the whole recovery strategy.",
        cross_ref="For robot datasets and scaling decisions, see <a href=\"../../part-5-learning-from-demonstration-and-robot-data/module-24-robot-datasets-and-data-scaling-laws/index.html\">Chapter 24</a>. For sim-to-real transfer protocols, revisit <a href=\"../../part-4-reinforcement-learning-for-embodied-agents/module-20-sim-to-real-transfer-rl-focus/index.html\">Chapter 20</a>. For deployment monitoring after synthetic pretraining, connect to <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html\">Chapter 55</a>.",
        self_check="Can you state one rare event that should be over-sampled with a world model, one artifact that would make that synthetic data dangerous, and one real-world probe that would verify transfer?",
        deep_dive=dedent(
            """
            <p>Generated worlds are most valuable when they sharpen coverage rather than replace reality wholesale. That is especially true in humanoid pipelines, where the policy's mistakes are shaped by contact and embodiment details that are easy to blur in a video-centric generator. Teams often pair generated scenarios with real-data anchors from LeRobot, Open X-Embodiment, or task-specific logs for exactly this reason.</p>
            <p>The right mental model is not “synthetic data is cheaper real data.” It is “synthetic data is a controllable experimenter.” Use it to target missing cases, but keep real data as the anchor that decides whether those generated cases taught the right lesson.</p>
            """
        ).strip(),
        takeaway="Use generative world models to target missing edge cases and structured evaluations, while keeping real data as the anchor that decides whether the synthetic lesson transfers.",
        exercise="Pick one humanoid or robot task and define a synthetic-data policy: what event will you generate, what real validation panel will you keep untouched, and what failure would make you discard the generated data?",
        bibliography_cards=[
            bib_card('NVIDIA. "Physical AI with World Foundation Models." (2026). <a href="https://www.nvidia.com/en-us/ai/cosmos/" rel="noopener" target="_blank">https://www.nvidia.com/en-us/ai/cosmos/</a>', "Cosmos is the clearest current source for synthetic-world pipelines aimed at physical AI."),
            bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "Genie 3 shows how interactive world generation may feed future data-generation and evaluation loops."),
            bib_card('Open X-Embodiment Collaboration. "Open X-Embodiment." (2023). <a href="https://arxiv.org/abs/2310.08864" rel="noopener" target="_blank">https://arxiv.org/abs/2310.08864</a>', "This is a useful contrast point because it emphasizes broad real-data aggregation rather than synthetic generation."),
        ],
        prev_href="section-39.5.html",
        prev_label="Section 39.5: GameNGen and Oasis: neural game engines",
        next_href="section-39.7.html",
        next_label="Section 39.7: Evaluating consistency, controllability...",
    ),
    "39.7": dict(
        title="Evaluating consistency, controllability, and horizon",
        image="chapter-39-illustration-05.png",
        cite="A World Model Needs More Than One Score",
        intro_callout="World-model evaluation fails when it collapses many failure modes into one aesthetic score. Consistency, controllability, and usable horizon are different properties, and embodied systems often break on the weakest one rather than on the average.",
        pathway="Treat this section as the chapter's audit sheet. Each metric exists because a different kind of simulator failure misleads a planner or evaluator in a different way.",
        key_insight="The minimum of the evaluation axes is usually the most operationally honest number. Agents fail at the bottleneck, not at the mean.",
        problem="Researchers and product teams love single numbers, but generative world models rarely fail in one dimension. A future can look consistent but ignore action, obey action for a few steps but drift later, or stay persistent while breaking task semantics. Evaluation must therefore expose the failure axis, not hide it.",
        theory=dedent(
            """
            <p>A useful evaluation panel separates at least three core properties:
            $$\\text{consistency}: o_t \\rightarrow o_{t+1} \\text{ stays semantically coherent},$$
            $$\\text{controllability}: a_t \\text{ changes the future in the intended direction},$$
            $$\\text{usable horizon}: H^* = \\max H \\text{ such that the generated future remains decision-valid.}$$</p>
            <p>For embodied use, the usable horizon is usually the most revealing number. It measures not how long the model can keep drawing plausible frames, but how long the generated future remains trustworthy enough for policy learning, evaluation, or planning.</p>
            <p>The evaluation artifact should always include trajectories, not just aggregates. Horizon failure is often visible in one trace long before it meaningfully shifts an average score.</p>
            """
        ).strip(),
        algorithm_box=dedent(
            """
            <div class="callout algorithm">
            <div class="callout-title">Three-Axis Audit</div>
            <p>Run the same initial state and action script through the generator, score semantic continuity, score whether actions had the intended effect, then determine the first time step at which the future stops being decision-valid. Save both the summary numbers and the trace that broke earliest.</p>
            </div>
            </div>
            """
        ).strip().replace("</div>\n            </div>", "</div>"),
        code_intro="The following snippet computes the minimum of the three axes directly. That minimum is a better deployment signal than the average because the planner will fail where the weakest property fails.",
        code=dedent(
            """
            # Combine consistency, controllability, and horizon into a conservative audit.
            # The minimum axis is the bottleneck the deployment team must fix first.
            metrics = {
                "consistency": 0.88,
                "controllability": 0.72,
                "usable_horizon": 0.54,
            }
            bottleneck = min(metrics, key=metrics.get)
            print({"bottleneck": bottleneck, "audit_pass": min(metrics.values()) >= 0.7})
            """
        ).strip(),
        code_output="{'bottleneck': 'usable_horizon', 'audit_pass': False}",
        code_expectation="The audit fails because the usable horizon is too short even though the short-term clip looks coherent and somewhat controllable. That is exactly the point of the panel: a planner or evaluator needs a long-enough trustworthy future, not merely an attractive first second.",
        code_caption="This conservative audit surfaces the weakest link in the generated world. Here the bottleneck is usable horizon, which means the team should spend effort on long-rollout stability before celebrating visual or short-step control quality.",
        library_shortcut="The audit logic is tiny, but it becomes powerful when paired with maintained generation backends and reproducible evaluation scripts. The right shortcut is not a magic simulator score library. It is a stable harness that replays the same seed states and action scripts against every new model version and stores the traces next to the summary table.",
        practice=dedent(
            """
            <ol>
            <li>Report each axis separately and report the bottleneck explicitly.</li>
            <li>Keep at least one broken trace in every evaluation packet.</li>
            <li>Test horizon under repeated actions and under branching counterfactual actions.</li>
            <li>Do not compare models unless they are scored on the same initial-state panel, action scripts, and acceptance thresholds.</li>
            </ol>
            """
        ).strip(),
        warning="Averaging over axes can hide the very failure that would sink deployment. If one property is below threshold, the world model should fail the gate even when the average looks healthy.",
        practical_example="An evaluation team for a warehouse robot may find that a generated world model preserves object identities and follows turns for three seconds, then silently shortens hallways and changes shelf geometry. A short clip looks fine. A usable-horizon audit reveals that the planner's future became untrustworthy exactly where navigation decisions become harder.",
        frontier="The frontier is automated world-model evals that stay task-grounded. Researchers are pushing toward metrics that capture causal consistency, not just perceptual quality, and toward evaluation loops that connect world-model scores directly to downstream policy improvement or failure.",
        cross_ref="For broader embodied-system evaluation design, revisit <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html\">Chapter 52</a>. For uncertainty and safety, connect to <a href=\"../../part-11-evaluation-safety-robustness-and-deployment/module-53-robustness-and-uncertainty/index.html\">Chapter 53</a>. For compact latent alternatives with different audit needs, compare against <a href=\"../module-38-latent-world-models/index.html\">Chapter 38</a>.",
        self_check="If you had to reject a generative world model version today, which axis would you inspect first for your application, and what single broken trace would convince a teammate that the rejection was justified?",
        deep_dive=dedent(
            """
            <p>Good evaluation is not an afterthought to world-model research. It shapes what progress means. If the field rewards only photorealism, models optimize photorealism. If the field rewards task-grounded controllability and usable horizon, model design and data curation follow those incentives.</p>
            <p>This is also why reproducibility matters so much here. A world model can fail on one initial state and look excellent on another. Without saved seed panels and trace artifacts, evaluation quickly collapses back into storytelling. The right artifact makes the failure replayable.</p>
            """
        ).strip(),
        takeaway="Evaluate generative world models by their weakest control-relevant property, because the agent will break at the bottleneck, not at the average.",
        exercise="Create a three-axis evaluation card for one world-model application. Define the acceptance threshold for each axis and describe the exact trace you would save when the model fails that threshold.",
        bibliography_cards=[
            bib_card('OpenAI. "Video Generation Models as World Simulators." (2024). <a href="https://openai.com/index/video-generation-models-as-world-simulators/" rel="noopener" target="_blank">https://openai.com/index/video-generation-models-as-world-simulators/</a>', "The report motivates the simulator framing that this audit section then tightens."),
            bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "A current interactive-world-model reference that makes controllability and horizon questions unavoidable."),
            bib_card('NVIDIA. "Physical AI with World Foundation Models." (2026). <a href="https://www.nvidia.com/en-us/ai/cosmos/" rel="noopener" target="_blank">https://www.nvidia.com/en-us/ai/cosmos/</a>', "A platform reference for why evaluation must connect generated worlds to downstream policy development."),
        ],
        prev_href="section-39.6.html",
        prev_label="Section 39.6: Using generative world models for data...",
        next_href="../../part-8-world-models-and-model-based-embodied-ai/module-40-predictive-representations-and-self-supervised-world-models/index.html",
        next_label="Chapter 40: Predictive representations and self...",
    ),
}


chapter38_index = chapter_index_page(
    chapter_num=38,
    chapter_title="Latent World Models",
    overview="Chapter 38 explains how embodied agents compress observations into action-relevant latent state, predict that state forward under candidate actions, and use the result for planning, value estimation, or imagined policy learning. The through-line is decision sufficiency: the latent must preserve what matters for control while discarding what only bloats computation.",
    theory_thread="The theory thread moves from state abstraction to RSSMs, Dreamer-style imagination, transformer token world models, and decoder-free latent MPC. The practical thread keeps asking the same operational question: what evidence shows that the latent state improved closed-loop behavior rather than only reconstruction quality or benchmark aesthetics?",
    roadmap=[
        ("38.1", "Why predict in latent space", "Defines the control argument for compression, belief state, and decision-sufficient latent dynamics."),
        ("38.2", "Autoencoders and recurrent state-space models (RSSM)", "Builds the prior-posterior memory model that underlies latent filtering and imagination."),
        ("38.3", "Dreamer to DreamerV3", "Explains how actor-critic learning happens inside imagined latent trajectories and why robust training matters."),
        ("38.4", "Transformer world models (IRIS)", "Casts world modeling as token sequence prediction and compares attention-based memory with recurrent state."),
        ("38.5", "TD-MPC2: latent MPC at scale", "Shows how decoder-free latent dynamics support online trajectory optimization across many continuous-control tasks."),
        ("38.6", "World models for visual control", "Turns latent theory into a deployment checklist for multimodal sensing, uncertainty, and fallback behavior."),
    ],
    tooling_note="This chapter follows the right-tool pattern carefully. Learn the mechanics with small probes, then reach for maintained stacks such as DreamerV3, the IRIS repository, TD-MPC2, PyTorch sequence modules, JAX utilities, MuJoCo, and Isaac Lab when the task becomes a real system rather than a didactic exercise.",
    lab_title="Build a Latent World-Model Audit Panel",
    lab_objective="Build a reproducible audit panel that compares one latent world-model baseline and one maintained implementation on the same observation, action, horizon, and failure-tag contract.",
    lab_setup="Use Python, NumPy, and one maintained stack of your choice, such as DreamerV3 or TD-MPC2. Keep the evaluation artifact format identical across both paths.",
    lab_code=dedent(
        """
        # Create the run manifest before touching the model code.
        # The same manifest must be reused by the baseline and the maintained stack.
        manifest = {
            "chapter": 38,
            "observation_stream": "rgb plus proprio",
            "action_space": "continuous gripper velocity",
            "horizon": 12,
            "failure_tag": "representation",
        }
        print(manifest)
        """
    ).strip(),
    lab_output="{'chapter': 38, 'observation_stream': 'rgb plus proprio', 'action_space': 'continuous gripper velocity', 'horizon': 12, 'failure_tag': 'representation'}",
    lab_caption="The manifest fixes the contract that both latent-world-model implementations must obey. If the contract changes between runs, any later comparison of reward, horizon, or safety becomes invalid.",
    lab_solution_code=dedent(
        """
        # Extend the manifest with the exact metric and perturbation used in the audit.
        manifest = {
            "chapter": 38,
            "observation_stream": "rgb plus proprio",
            "action_space": "continuous gripper velocity",
            "horizon": 12,
            "metric": "success without emergency stop",
            "perturbation": "camera occlusion for 0.5 seconds",
            "failure_tag": "representation",
        }
        print(manifest)
        """
    ).strip(),
    lab_solution_output="{'chapter': 38, 'observation_stream': 'rgb plus proprio', 'action_space': 'continuous gripper velocity', 'horizon': 12, 'metric': 'success without emergency stop', 'perturbation': 'camera occlusion for 0.5 seconds', 'failure_tag': 'representation'}",
    lab_solution_caption="The completed manifest is ready to save beside latent traces, videos, and metric tables. It also makes it obvious what perturbation the world model was expected to survive.",
    evidence_standard="Compare latent world models only when the observation interface, action space, horizon, seed panel, perturbation, and saved artifact are all matched. A prettier reconstruction or a lower latent loss is not enough.",
    tool_rows=[
        ("DreamerV3", "Robust latent imagination for actor-critic learning across diverse domains."),
        ("TD-MPC2", "Decoder-free latent planning for continuous-control tasks with tight replanning loops."),
        ("IRIS", "Tokenized transformer world modeling when long-range visual context matters."),
        ("PyTorch and JAX", "Sequence modules, distributions, scans, and return-estimation utilities for building small probes."),
        ("MuJoCo and Isaac Lab", "Simulation backends for visual-control experiments and matched rollout evaluation."),
    ],
    bibliography_cards=[
        bib_card('Hafner, D. et al.. "Learning Latent Dynamics for Planning from Pixels." (2019). <a href="https://arxiv.org/abs/1811.04551" rel="noopener" target="_blank">https://arxiv.org/abs/1811.04551</a>', "Foundational RSSM and latent-planning reference."),
        bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023). <a href="https://arxiv.org/abs/2301.04104" rel="noopener" target="_blank">https://arxiv.org/abs/2301.04104</a>', "Primary DreamerV3 reference."),
        bib_card('Micheli, V., Alonso, E., and Fleuret, F.. "Transformers Are Sample-Efficient World Models." (2022). <a href="https://arxiv.org/abs/2209.00588" rel="noopener" target="_blank">https://arxiv.org/abs/2209.00588</a>', "Primary IRIS reference."),
        bib_card('Hansen, N., Su, H., and Wang, X.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023). <a href="https://openreview.net/forum?id=Oxh5CstDJU" rel="noopener" target="_blank">https://openreview.net/forum?id=Oxh5CstDJU</a>', "Primary TD-MPC2 reference."),
    ],
    prev_href="../module-37-model-based-rl-and-mpc/section-37.5.html",
    prev_label="Section 37.5: Sample-efficiency advantages and failu...",
    next_href="section-38.1.html",
    next_label="Section 38.1: Why predict in latent space",
)


chapter39_index = chapter_index_page(
    chapter_num=39,
    chapter_title="Generative and Video World Models",
    overview="Chapter 39 studies the more visually expressive side of world modeling: generative simulators, interactive video worlds, and world-foundation-model platforms aimed at physical AI. The chapter is careful about the distinction between a compelling demo and a controllable simulator that can actually train or evaluate embodied agents.",
    theory_thread="The theory thread moves from simulator criteria to interactive world models, video-generation systems framed as simulators, platform approaches such as Cosmos, neural game engines, synthetic-data pipelines, and evaluation protocols that separate consistency, controllability, and usable horizon.",
    roadmap=[
        ("39.1", "Generative models as learned simulators", "Defines what a generative model must satisfy before it deserves to be called a simulator."),
        ("39.2", "Genie 1-3: interactive, playable world models", "Tracks the shift from latent-action video modeling to real-time explorable generated worlds."),
        ("39.3", "Video generation as world simulation: Sora and successors", "Interprets high-fidelity video generation through the stricter lens of embodied causality."),
        ("39.4", "NVIDIA Cosmos: world foundation models for physical AI", "Treats world models as a platform for synthetic data, transfer, and policy-development loops."),
        ("39.5", "GameNGen and Oasis: neural game engines", "Uses real-time interactive generation as the sharpest stress test for compounding world-model error."),
        ("39.6", "Using generative world models for data and evaluation (e.g., humanoid pipelines)", "Shows how generated worlds can target rare events without replacing real data as the anchor."),
        ("39.7", "Evaluating consistency, controllability, and horizon", "Builds the audit panel that decides whether a generative world is useful for agents."),
    ],
    tooling_note="This chapter uses practical tools without pretending the ecosystem is fully settled. Learn the scoring and audit logic with tiny probes, then use maintained systems such as Cosmos, Diffusers, Project Genie interfaces, or official research code when you need real generation backends.",
    lab_title="Build a Generative World-Model Evaluation Harness",
    lab_objective="Build a reproducible harness that scores one generative world model on controllability, persistence, and usable horizon while saving the traces that caused the first failure.",
    lab_setup="Use Python and your preferred generator backend or recorded clips. The important constraint is that every model version is replayed on the same initial states and action scripts.",
    lab_code=dedent(
        """
        # Store the scenario contract for a generated-world evaluation.
        # Every model version must replay the same initial state and action script.
        manifest = {
            "chapter": 39,
            "initial_state_id": "warehouse-turn-07",
            "action_script": ["left", "left", "stop", "back"],
            "max_horizon": 12,
            "evaluation_axis": "controllability",
        }
        print(manifest)
        """
    ).strip(),
    lab_output="{'chapter': 39, 'initial_state_id': 'warehouse-turn-07', 'action_script': ['left', 'left', 'stop', 'back'], 'max_horizon': 12, 'evaluation_axis': 'controllability'}",
    lab_caption="The manifest fixes the replay conditions for every generative-world evaluation. Without it, later claims about consistency or horizon can silently compare different prompts, seeds, or action scripts.",
    lab_solution_code=dedent(
        """
        # Extend the replay contract with the exact failure trace to save.
        manifest = {
            "chapter": 39,
            "initial_state_id": "warehouse-turn-07",
            "action_script": ["left", "left", "stop", "back"],
            "max_horizon": 12,
            "evaluation_axis": "controllability",
            "trace_to_save": "first_object_identity_break",
            "accept_threshold": 0.8,
        }
        print(manifest)
        """
    ).strip(),
    lab_solution_output="{'chapter': 39, 'initial_state_id': 'warehouse-turn-07', 'action_script': ['left', 'left', 'stop', 'back'], 'max_horizon': 12, 'evaluation_axis': 'controllability', 'trace_to_save': 'first_object_identity_break', 'accept_threshold': 0.8}",
    lab_solution_caption="The completed manifest makes the evaluation reproducible and tells the team which trace to archive when the generated world fails its threshold.",
    evidence_standard="Compare generative world models only on the same initial-state panel, action scripts, horizon budget, and acceptance thresholds. A compelling demo clip is not evidence of simulator quality.",
    tool_rows=[
        ("NVIDIA Cosmos", "World-foundation-model platform for physical-AI generation, transfer, and evaluation loops."),
        ("Project Genie and Genie materials", "Interactive world-model references for action-following and generated-environment research."),
        ("Diffusers", "Practical toolkit for open diffusion-style video model experiments and ablations."),
        ("GameNGen and Oasis demos", "Stress tests for real-time interactive generation and compounding error."),
        ("Custom replay harnesses", "The layer that actually makes world-model comparisons fair and reproducible."),
    ],
    bibliography_cards=[
        bib_card('OpenAI. "Video Generation Models as World Simulators." (2024). <a href="https://openai.com/index/video-generation-models-as-world-simulators/" rel="noopener" target="_blank">https://openai.com/index/video-generation-models-as-world-simulators/</a>', "Primary Sora reference for the simulator framing."),
        bib_card('Google DeepMind. "Genie 3: A New Frontier for World Models." (2025). <a href="https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/" rel="noopener" target="_blank">https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/</a>', "Current official Genie reference."),
        bib_card('NVIDIA. "Physical AI with World Foundation Models." (2026). <a href="https://www.nvidia.com/en-us/ai/cosmos/" rel="noopener" target="_blank">https://www.nvidia.com/en-us/ai/cosmos/</a>', "Current official Cosmos platform reference."),
        bib_card('Valevski, D. et al.. "Diffusion Models Are Real-Time Game Engines." (2024). <a href="https://arxiv.org/abs/2408.14837" rel="noopener" target="_blank">https://arxiv.org/abs/2408.14837</a>', "Primary GameNGen reference for neural-engine evaluation."),
    ],
    prev_href="../module-38-latent-world-models/section-38.6.html",
    prev_label="Section 38.6: World models for visual control",
    next_href="section-39.1.html",
    next_label="Section 39.1: Generative models as learned simulators",
)


write(chapter38_dir / "index.html", chapter38_index)
write(chapter39_dir / "index.html", chapter39_index)

chapter38_titles = [cfg["title"] for cfg in chapter38_sections.values()]
chapter39_titles = [cfg["title"] for cfg in chapter39_sections.values()]

for idx, (section_num, cfg) in enumerate(chapter38_sections.items()):
    prev_href = cfg["prev_href"]
    prev_label = cfg["prev_label"]
    next_href = cfg["next_href"]
    next_label = cfg["next_label"]
    html = section_page(
        chapter_num=38,
        section_num=section_num,
        title=cfg["title"],
        chapter_title="Latent World Models",
        image=cfg["image"],
        cite=cfg["cite"],
        intro_callout=cfg["intro_callout"],
        pathway=cfg["pathway"],
        key_insight=cfg["key_insight"],
        problem=cfg["problem"],
        theory=cfg["theory"],
        algorithm_box=cfg["algorithm_box"],
        code_intro=cfg["code_intro"],
        code=cfg["code"],
        code_output=cfg["code_output"],
        code_expectation=cfg["code_expectation"],
        code_caption=cfg["code_caption"],
        library_shortcut=cfg["library_shortcut"],
        practice=cfg["practice"],
        warning=cfg["warning"],
        practical_example=cfg["practical_example"],
        frontier=cfg["frontier"],
        cross_ref=cfg["cross_ref"],
        self_check=cfg["self_check"],
        deep_dive=cfg["deep_dive"],
        takeaway=cfg["takeaway"],
        exercise=cfg["exercise"],
        bibliography_cards=cfg["bibliography_cards"],
        prev_href=prev_href,
        prev_label=prev_label,
        next_href=next_href,
        next_label=next_label,
    )
    write(chapter38_dir / f"section-{section_num}.html", html)

for section_num, cfg in chapter39_sections.items():
    html = section_page(
        chapter_num=39,
        section_num=section_num,
        title=cfg["title"],
        chapter_title="Generative and Video World Models",
        image=cfg["image"],
        cite=cfg["cite"],
        intro_callout=cfg["intro_callout"],
        pathway=cfg["pathway"],
        key_insight=cfg["key_insight"],
        problem=cfg["problem"],
        theory=cfg["theory"],
        algorithm_box=cfg["algorithm_box"],
        code_intro=cfg["code_intro"],
        code=cfg["code"],
        code_output=cfg["code_output"],
        code_expectation=cfg["code_expectation"],
        code_caption=cfg["code_caption"],
        library_shortcut=cfg["library_shortcut"],
        practice=cfg["practice"],
        warning=cfg["warning"],
        practical_example=cfg["practical_example"],
        frontier=cfg["frontier"],
        cross_ref=cfg["cross_ref"],
        self_check=cfg["self_check"],
        deep_dive=cfg["deep_dive"],
        takeaway=cfg["takeaway"],
        exercise=cfg["exercise"],
        bibliography_cards=cfg["bibliography_cards"],
        prev_href=cfg["prev_href"],
        prev_label=cfg["prev_label"],
        next_href=cfg["next_href"],
        next_label=cfg["next_label"],
    )
    write(chapter39_dir / f"section-{section_num}.html", html)
