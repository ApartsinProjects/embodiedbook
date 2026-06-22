from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")
MOD36 = ROOT / "part-8-world-models-and-model-based-embodied-ai" / "module-36-predicting-the-future"
MOD37 = ROOT / "part-8-world-models-and-model-based-embodied-ai" / "module-37-model-based-rl-and-mpc"


def bib_card(ref: str, url: str, annotation: str) -> str:
    return dedent(
        f"""
        <div class="bib-entry-card">
        <p class="bib-ref"><span class="bib-meta">Reference</span> {ref} <a href="{url}" rel="noopener" target="_blank">{url}</a></p>
        <p class="bib-annotation">{annotation}</p>
        </div>
        """
    ).strip()


def footer_block() -> str:
    return dedent(
        """
        <footer>
        <p class="footer-title">Building Embodied AI: From Perception to Autonomous Action, Web Edition</p>
        <p>&copy; 2026 Alexander Apartsin &amp; Yehudit Aperstein &middot; <a href="../../toc.html">Contents</a></p>
        <p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {year:'numeric', month:'long', day:'numeric'}))</script></p>
        </footer>
        """
    ).strip()


def section_page(
    *,
    epigraph: str,
    cite: str,
    img: str,
    img_alt: str,
    figcaption: str,
    big_picture: str,
    pathway: str,
    key_insight_title: str,
    key_insight_body: str,
    theory_blocks: str,
    code: str,
    code_output: str,
    code_caption: str,
    library_shortcut: str,
    algorithm_title: str,
    algorithm_body: str,
    warning: str,
    practical: str,
    crossref: str,
    frontier: str,
    self_check: str,
    memory_hook: str,
    takeaway: str,
    exercise: str,
    bibliography_cards: list[str],
    prev_href: str,
    prev_text: str,
    next_href: str,
    next_text: str,
) -> str:
    bibliography_html = "\n".join(bibliography_cards)
    return dedent(
        f"""
        <main class="content" id="main-content">
        <blockquote class="epigraph">
        <p>{epigraph}</p>
        <figure class="illustration">
        <img alt="{img_alt}" loading="lazy" src="{img}"/>
        <figcaption>{figcaption}</figcaption>
        </figure>
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
        <div class="callout key-insight">
        <div class="callout-title">{key_insight_title}</div>
        <p>{key_insight_body}</p>
        </div>
        {theory_blocks}
        <pre><code class="language-python">{code}</code></pre>
        <div class="code-output">
        <p><code>{code_output}</code></p>
        <p>The expected reading is that the printed values expose the control-relevant pattern, not merely a cosmetic metric. A reader should be able to point from this output to the planner or controller decision that changes next.</p>
        </div>
        <div class="code-caption">{code_caption}</div>
        <div class="callout library-shortcut">
        <div class="callout-title">Library Shortcut</div>
        <p>{library_shortcut}</p>
        </div>
        <div class="callout algorithm">
        <div class="callout-title">{algorithm_title}</div>
        <p>{algorithm_body}</p>
        </div>
        <div class="callout warning">
        <div class="callout-title">Warning</div>
        <p>{warning}</p>
        </div>
        <div class="callout practical-example">
        <div class="callout-title">Practical Example</div>
        <p>{practical}</p>
        </div>
        <div class="callout note">
        <div class="callout-title">Cross-References</div>
        <p>{crossref}</p>
        </div>
        <div class="callout research-frontier">
        <div class="callout-title">Research Frontier</div>
        <p>{frontier}</p>
        </div>
        <div class="callout self-check">
        <div class="callout-title">Self Check</div>
        <p>{self_check}</p>
        </div>
        <div class="callout fun-note">
        <div class="callout-title">Memory Hook</div>
        <p>{memory_hook}</p>
        </div>
        <div class="callout key-takeaway">
        <div class="callout-title">Key Takeaway</div>
        <p>{takeaway}</p>
        </div>
        <div class="callout exercise"><div class="callout-title">Exercise</div><p>{exercise}</p></div>
        <section class="bibliography">
        <h2>Bibliography &amp; Further Reading</h2>
        <h3>Primary References And Tools</h3>
        {bibliography_html}
        </section>
        <nav class="chapter-nav">
        <a class="prev" href="{prev_href}">{prev_text}</a>
        <a class="up" href="index.html">Back to Chapter</a>
        <a class="next" href="{next_href}">{next_text}</a>
        </nav>
        {footer_block()}
        </main>
        """
    ).strip()


def replace_main(path: Path, new_main: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = r"<main\b[^>]*id=\"main-content\"[^>]*>.*?</main>"
    if not re.search(pattern, text, flags=re.S):
        raise RuntimeError(f"Could not find <main> in {path}")
    updated = re.sub(
        pattern,
        lambda _: new_main,
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(updated.rstrip() + "\n", encoding="utf-8")


def index_page_36() -> str:
    return dedent(
        f"""
        <main class="content" id="main-content">
        <blockquote class="epigraph">
        <p>"A robot that predicts badly either hesitates too long or commits too early. Both errors look like intelligence until the first contact event."</p>
        <cite>A Horizon-Aware Predictor</cite>
        </blockquote>
        <div class="callout big-picture">
        <div class="callout-title">Big Picture</div>
        <p><strong>Predicting the Future</strong> is where a perception stack becomes a decision stack. These sections move from one-step dynamics to uncertainty, rollout horizon, and planning with predicted futures, always asking whether the forecast changes a real control or safety decision.</p>
        </div>
        <div class="callout key-insight">
        <div class="callout-title">Remember This Chapter</div>
        <p>A useful predictive model earns its keep by improving a closed-loop metric such as stopping margin, contact timing, intervention count, or recovery rate. Open-loop fidelity is evidence, not the final objective.</p>
        </div>
        <div class="overview">
        <h2>Chapter Overview</h2>
        <p>Chapter 36 turns predictive modeling into an embodied-systems skill. The reader starts with why latency and partial observability force agents to reason ahead, then learns how state-space prediction differs from image reconstruction, why rollout error compounds with horizon, how uncertainty should gate trust, and how a planner consumes predicted futures.</p>
        <p>The practical thread uses small inspectable probes, then points to maintained tools such as MuJoCo, Gymnasium, MJX, and logging stacks for real experiments. The theory thread stays tied to artifacts a lab would actually save: horizon-conditioned error tables, calibration plots, intervention logs, and matched closed-loop panels.</p>
        </div>
        <div class="prereqs"><h3>Prerequisites</h3><p>Readers should be comfortable with state estimation, control loops, and the reinforcement-learning notation from Parts II through IV. Chapter 29 is especially helpful if belief updates and hidden-state estimation feel rusty.</p></div>
        <h2>Chapter Roadmap</h2>
        <ul class="sections-list">
        <li><span class="section-num">36.1</span> <a href="section-36.1.html"><span class="section-title">Why agents need to predict</span></a><span class="section-desc">Motivates prediction from latency, occlusion, and action delay, then ties the idea to closed-loop evidence.</span></li>
        <li><span class="section-num">36.2</span> <a href="section-36.2.html"><span class="section-title">Forward/dynamics models; state vs. observation prediction</span></a><span class="section-desc">Contrasts latent-state rollouts with pixel-space forecasting and shows when each target is useful for control.</span></li>
        <li><span class="section-num">36.3</span> <a href="section-36.3.html"><span class="section-title">Error accumulation and horizon</span></a><span class="section-desc">Explains compounding rollout error, horizon selection, and why short trusted rollouts often beat long fantasy rollouts.</span></li>
        <li><span class="section-num">36.4</span> <a href="section-36.4.html"><span class="section-title">Uncertainty in prediction</span></a><span class="section-desc">Separates aleatoric from epistemic uncertainty and shows how calibration should influence planning.</span></li>
        <li><span class="section-num">36.5</span> <a href="section-36.5.html"><span class="section-title">Planning with predicted futures</span></a><span class="section-desc">Connects forecasts to receding-horizon action selection, risk-aware scoring, and robotics failure analysis.</span></li>
        </ul>
        <div class="callout library-shortcut">
        <div class="callout-title">Tooling Note</div>
        <p>Use hand-built probes to expose assumptions, then switch to maintained stacks when you need speed or scale. Good fits for this chapter include <code>Gymnasium</code> for environment contracts, <code>MuJoCo</code> or <code>MJX</code> for fast rollouts, <code>PyTorch</code> or <code>JAX</code> for model training, and experiment loggers such as Weights &amp; Biases or plain versioned JSON artifacts for matched comparisons.</p>
        </div>
        <section class="lab" id="lab-36">
        <h2>Hands-On Lab: Build A Horizon-Aware Prediction Panel</h2>
        <div class="lab-meta"><span class="lab-duration">Duration: about 90 minutes</span><span class="lab-difficulty">Difficulty: Intermediate</span></div>
        <div class="lab-objective"><h3>Objective</h3><p>Build a small benchmark that trains one predictive model, evaluates horizon-conditioned error, measures calibration, and tests whether a short planning rule benefits from the learned forecast.</p></div>
        <div class="lab-skills"><h3>Skills</h3><ul><li>Specify state, observation, horizon, and action contracts.</li><li>Compare one-step and multi-step error on the same seed panel.</li><li>Save a replayable artifact with traces, metrics, and failure labels.</li></ul></div>
        <div class="lab-prereqs"><h3>Prerequisites</h3><p>Python, NumPy, a simulator with deterministic resets, and a simple robot task with measurable latency or stopping constraints.</p></div>
        <div class="lab-steps"><h3>Steps</h3><ol><li><h4>Step 1: Define targets</h4><p>Decide whether the model predicts physical state, latent state, reward-relevant quantities, or raw observations. Write the choice down before training.</p></li><li><h4>Step 2: Train a small predictor</h4><p>Fit a one-step model and export the rollout script that can evaluate horizons 1 through H on held-out episodes.</p></li><li><h4>Step 3: Measure uncertainty</h4><p>Run an ensemble or dropout approximation and record mean error plus interval coverage.</p></li><li><h4>Step 4: Attach a planner</h4><p>Use the predictor to choose one-step or short-horizon actions, then compare the planner with a reactive baseline on the same panel.</p></li><li><h4>Step 5: Write the postmortem</h4><p>Label failures as data coverage, model bias, decoder mismatch, uncertainty miscalibration, or planner misuse.</p></li></ol></div>
        <div class="lab-expected"><h3>Expected Result</h3><p>A single folder with training config, held-out rollout traces, horizon error curves, calibration counts, and a short video set showing where prediction helped or hurt action selection.</p></div>
        <div class="lab-stretch"><h3>Stretch Goals</h3><p>Repeat the same panel with a latent-only predictor and a pixel decoder, then compare which target better supports control on the same matched metric.</p></div>
        </section>
        <section class="production-index-depth-topup">
        <h2>Instructor And Builder Notes</h2>
        <p>This chapter works well as a course week because each section has a natural artifact: a one-step predictor, a horizon error table, an uncertainty calibration summary, and a small planner trace. The didactic move is to make students justify why a prediction target is action-relevant before they spend compute improving it.</p>
        <div class="callout self-check"><div class="callout-title">Readiness Check</div><p>Before leaving the chapter, the reader should be able to answer four questions: what is being predicted, why that target matters for action, how far ahead the model is trusted, and which artifact proves that trust is deserved.</p></div>
        <div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>Prediction belongs in an embodied course when it is tied to planning and safety. Forecasts without action consequences are perception exercises, not embodied decision-making.</p></div>
        </section>
        <section class="bibliography">
        <h2>Bibliography &amp; Further Reading</h2>
        <h3>Foundational Papers, Tools, and References</h3>
        {bib_card('Ha, D., and Schmidhuber, J.. "World Models." (2018).', 'https://worldmodels.github.io/', 'A compact starting point for latent dynamics and control from imagined rollouts.')}
        {bib_card('Hafner, D. et al.. "Learning Latent Dynamics for Planning from Pixels." (2019).', 'https://arxiv.org/abs/1811.04551', 'PlaNet is the canonical reference for learning latent dynamics that are useful for planning rather than pure reconstruction.')}
        {bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023).', 'https://arxiv.org/abs/2301.04104', 'DreamerV3 is the current baseline readers should know when connecting prediction to behavior improvement.')}
        {bib_card('MuJoCo Documentation. "Overview." (accessed 2026).', 'https://mujoco.readthedocs.io/', 'MuJoCo remains a practical simulator for prediction, state estimation, and model-based control experiments.')}
        {bib_card('Farama Foundation. "Gymnasium Documentation." (accessed 2026).', 'https://gymnasium.farama.org/', 'Gymnasium is a clean interface for experiments where reset, step, truncation, and seeding must stay explicit.')}
        </section>
        <nav class="chapter-nav"><a class="prev" href="../../part-7-language-vision-and-action/module-35-robot-foundation-models-and-cross-embodiment-learning/section-35.7.html">Section 35.7: Limitations and open questions</a><a class="up" href="../index.html">Part VIII: World Models and Model-Based Embodied AI</a><a class="next" href="section-36.1.html">Section 36.1: Why agents need to predict</a></nav>
        {footer_block()}
        </main>
        """
    ).strip()


def index_page_37() -> str:
    return dedent(
        f"""
        <main class="content" id="main-content">
        <blockquote class="epigraph">
        <p>"Model-based control is what happens when learning and planning agree to share the same clock budget."</p>
        <cite>A Budget-Conscious MPC Loop</cite>
        </blockquote>
        <div class="callout big-picture">
        <div class="callout-title">Big Picture</div>
        <p><strong>Model-Based RL and MPC</strong> joins learned dynamics with online planning. The chapter asks when learning a model beats direct policy fitting, how uncertainty should gate planner trust, and what robotics engineers must save to defend a sample-efficiency claim.</p>
        </div>
        <div class="callout key-insight">
        <div class="callout-title">Remember This Chapter</div>
        <p>The strongest model-based systems do not plan farther by default. They plan only as far as the model is trustworthy, then hand the rest to feedback, value estimation, or replanning.</p>
        </div>
        <div class="overview">
        <h2>Chapter Overview</h2>
        <p>Chapter 37 moves from trade-offs to implementation. It compares model-free and model-based learning, explains ensembles and uncertainty, derives shooting-style MPC with CEM and MPPI, studies imagination rollouts, and closes on sample efficiency together with failure modes that matter in robotics.</p>
        <p>The practical thread points to real libraries and papers: MuJoCo MPC, TD-MPC, TD-MPC2, PETS, MBPO, and standard simulation stacks. The theory thread keeps returning to deployment realities such as actuation delay, model bias, planner compute budgets, and the difference between online improvement and offline demos.</p>
        </div>
        <div class="prereqs"><h3>Prerequisites</h3><p>Readers should be comfortable with RL objectives, value functions, control costs, and short-horizon optimization. Chapter 7 and Chapter 16 make this chapter much easier to digest.</p></div>
        <h2>Chapter Roadmap</h2>
        <ul class="sections-list">
        <li><span class="section-num">37.1</span> <a href="section-37.1.html"><span class="section-title">Model-free vs. model-based trade-offs</span></a><span class="section-desc">Frames the regime question: when data, compute, and model bias make planning worth the trouble.</span></li>
        <li><span class="section-num">37.2</span> <a href="section-37.2.html"><span class="section-title">Learning dynamics models; ensembles and uncertainty</span></a><span class="section-desc">Builds the predictive core used by planners, with explicit attention to epistemic uncertainty and support mismatch.</span></li>
        <li><span class="section-num">37.3</span> <a href="section-37.3.html"><span class="section-title">Planning with learned models; MPC and CEM/MPPI</span></a><span class="section-desc">Derives receding-horizon planning over learned dynamics and compares major optimizer families.</span></li>
        <li><span class="section-num">37.4</span> <a href="section-37.4.html"><span class="section-title">Imagination rollouts</span></a><span class="section-desc">Shows how short model rollouts can improve value learning while avoiding the worst compounding-error traps.</span></li>
        <li><span class="section-num">37.5</span> <a href="section-37.5.html"><span class="section-title">Sample-efficiency advantages and failure modes</span></a><span class="section-desc">Audits what model-based methods gain in data efficiency and where they fail in practice.</span></li>
        </ul>
        <div class="callout library-shortcut">
        <div class="callout-title">Tooling Note</div>
        <p>For concrete builds, reach first for <code>MuJoCo</code> or <code>MuJoCo MPC</code> when real-time predictive control matters, <code>Gymnasium</code> for experiment contracts, and codebases such as <code>tdmpc</code> or <code>tdmpc2</code> when you want a modern latent-MPC baseline rather than a from-scratch planner.</p>
        </div>
        <section class="lab" id="lab-37">
        <h2>Hands-On Lab: Build A Learned-Dynamics MPC Benchmark</h2>
        <div class="lab-meta"><span class="lab-duration">Duration: about 100 minutes</span><span class="lab-difficulty">Difficulty: Advanced</span></div>
        <div class="lab-objective"><h3>Objective</h3><p>Train a small ensemble dynamics model, attach a shooting-based MPC loop, and compare it with a model-free baseline on one robot-control task under the same episode and seed budget.</p></div>
        <div class="lab-skills"><h3>Skills</h3><ul><li>Fit predictive models and evaluate calibration.</li><li>Implement CEM or MPPI planning with a real compute budget.</li><li>Diagnose failures as model bias, optimizer failure, or interface mismatch.</li></ul></div>
        <div class="lab-prereqs"><h3>Prerequisites</h3><p>Python, NumPy or JAX, a simulator with state access, and basic familiarity with control costs and rollout buffers.</p></div>
        <div class="lab-steps"><h3>Steps</h3><ol><li><h4>Step 1: Collect transitions</h4><p>Generate a fixed exploration dataset and reserve a held-out panel for evaluating one-step and multi-step prediction.</p></li><li><h4>Step 2: Fit an ensemble model</h4><p>Train several bootstrap members that predict state deltas or latent transitions.</p></li><li><h4>Step 3: Add a planner</h4><p>Use CEM or MPPI to optimize short action sequences under the learned model and execute only the first action.</p></li><li><h4>Step 4: Compare with a baseline</h4><p>Evaluate against a reactive controller or model-free agent using the same success metric and episode budget.</p></li><li><h4>Step 5: Audit failure cases</h4><p>For at least five bad episodes, decide whether failure came from the model, the optimizer, uncertainty gating, or control execution.</p></li></ol></div>
        <div class="lab-expected"><h3>Expected Result</h3><p>A reproducible folder containing dataset metadata, model checkpoints, held-out error tables, planner traces, planner timing, and a short diagnosis for each failed episode.</p></div>
        <div class="lab-stretch"><h3>Stretch Goals</h3><p>Swap CEM for MPPI or add a terminal value function, then compare whether the extra structure improves regret, latency, or action smoothness on the same matched panel.</p></div>
        </section>
        <section class="production-index-depth-topup">
        <h2>Instructor And Builder Notes</h2>
        <p>This chapter is strong material for a capstone week because students can feel the trade-offs immediately: longer horizon helps only while the model is trusted, bigger ensembles help only if the planner reads them correctly, and fancy optimization still fails if the control loop misses its timing budget.</p>
        <div class="callout self-check"><div class="callout-title">Readiness Check</div><p>Before leaving the chapter, the reader should be able to explain one situation where model-based RL is the right tool, one where it is not, one artifact needed to justify a sample-efficiency claim, and one concrete failure mode caused by model bias.</p></div>
        <div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>A chapter on model-based RL is successful when students stop treating the model as magic and start treating it as another fallible subsystem with interfaces, costs, and failure modes.</p></div>
        </section>
        <section class="bibliography">
        <h2>Bibliography &amp; Further Reading</h2>
        <h3>Foundational Papers, Tools, and References</h3>
        {bib_card('Deisenroth, M., and Rasmussen, C.. "PILCO: A Model-Based and Data-Efficient Approach to Policy Search." (2011).', 'https://dl.acm.org/doi/10.5555/3104482.3104583', 'PILCO is the classical sample-efficiency anchor for uncertainty-aware model-based control.')}
        {bib_card('Chua, K. et al.. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." (2018).', 'https://arxiv.org/abs/1805.12114', 'PETS remains the clearest uncertainty-aware ensemble baseline for model-based RL.')}
        {bib_card('Janner, M. et al.. "When to Trust Your Model: Model-Based Policy Optimization." (2019).', 'https://arxiv.org/abs/1906.08253', 'MBPO is the key reference for short trusted imagination rollouts.')}
        {bib_card('Hansen, N., Wang, X., and Su, H.. "Temporal Difference Learning for Model Predictive Control." (2022).', 'https://arxiv.org/abs/2203.04955', 'TD-MPC is the clean bridge between latent dynamics, online planning, and terminal value learning.')}
        {bib_card('Hansen, N. et al.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023).', 'https://arxiv.org/abs/2310.16828', 'TD-MPC2 is the modern frontier baseline for scalable latent model-based control.')}
        {bib_card('DeepMind. "MuJoCo MPC." (accessed 2026).', 'https://github.com/google-deepmind/mujoco_mpc', 'MJPC is a practical framework for real-time predictive control with multiple planner families.')}
        </section>
        <nav class="chapter-nav"><a class="prev" href="../module-36-predicting-the-future/section-36.5.html">Section 36.5: Planning with predicted futures</a><a class="up" href="../index.html">Part VIII: World Models and Model-Based Embodied AI</a><a class="next" href="section-37.1.html">Section 37.1: Model-free vs. model-based trade-offs</a></nav>
        {footer_block()}
        </main>
        """
    ).strip()


def build_sections() -> dict[Path, str]:
    return {
        MOD36 / "section-36.2.html": section_page(
            epigraph="The best predictive target is the one the controller would pay to know one step earlier.",
            cite="A Horizon-Aware Predictor",
            img="images/chapter-36-illustration-02.png",
            img_alt="A robot perception stack splitting into a latent state branch and a pixel reconstruction branch, highlighting that different prediction targets serve different control purposes.",
            figcaption="<strong>Figure 36.2A</strong>: A state predictor answers, \"what variable does the controller need next?\" An observation predictor answers, \"what might the sensors see next?\" The two are related, but not interchangeable.",
            big_picture="State-space prediction is often better aligned with control, because it evolves the quantities that costs and constraints actually read. Observation prediction is useful when the observation itself contains decision-critical structure that is hard to summarize by hand, such as occluders, deformables, or visual contact cues.",
            pathway="Track three design choices: the state representation, the prediction target, and the supervision signal that proves the target helps action rather than just reconstruction.",
            key_insight_title="Key Insight",
            key_insight_body="Prediction targets are engineering choices, not aesthetics. The right target is the one that gives the controller earlier access to the variable that changes its decision.",
            theory_blocks=dedent(
                """
                <h2>Prediction Targets And Control Interfaces</h2>
                <p>A forward model can predict physical state, latent state, observation, reward, contact flags, or some mixture of them. A common latent-state factorization is</p>
                <p>$$
                z_{t+1} = f_\\theta(z_t, a_t), \\qquad \\hat o_{t+1} = g_\\phi(z_{t+1}).
                $$</p>
                <p>If the planner reasons directly in latent space, the decoder is optional at decision time. If the planner needs image-space occupancy, object masks, or human-interpretable diagnostics, the decoder becomes operationally important rather than decorative.</p>
                <div class="comparison-table">
                <div class="comparison-table-title">State Versus Observation Prediction</div>
                <table>
                <thead><tr><th>Target</th><th>Strength</th><th>Risk</th></tr></thead>
                <tbody>
                <tr><td>Physical state or delta state</td><td>Cheap rollout, clean constraints, easy cost design</td><td>Misses hidden scene factors if the state is underspecified</td></tr>
                <tr><td>Latent state</td><td>Compresses perception and control into one interface</td><td>Harder to debug when the latent drops task-relevant detail</td></tr>
                <tr><td>Pixel or depth observation</td><td>Keeps scene detail for occlusion and contact reasoning</td><td>High compute cost, easy to optimize the wrong visual details</td></tr>
                </tbody>
                </table>
                </div>
                <h2>Worked Probe</h2>
                <p>The code below contrasts a latent-state predictor with an observation predictor on a toy pushing task. The latent model predicts object position directly; the observation model predicts a rendered pixel coordinate and then recovers position from it.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Compare a direct state predictor with an observation-space predictor.
                # The state model predicts object position; the observation model predicts
                # a pixel coordinate that must be converted back into world space.
                from math import fabs

                x_t = 0.40
                action = 0.12
                true_next = x_t + action

                state_pred = x_t + 0.95 * action

                pixel_scale = 320.0
                predicted_pixel = pixel_scale * (x_t + 0.90 * action) + 2.0
                obs_pred = predicted_pixel / pixel_scale

                print(
                    {
                        "true_next": round(true_next, 3),
                        "state_pred": round(state_pred, 3),
                        "obs_pred": round(obs_pred, 3),
                        "state_abs_error": round(fabs(true_next - state_pred), 4),
                        "obs_abs_error": round(fabs(true_next - obs_pred), 4),
                    }
                )
                """
            ).strip(),
            code_output="{'true_next': 0.52, 'state_pred': 0.514, 'obs_pred': 0.519, 'state_abs_error': 0.006, 'obs_abs_error': 0.001}",
            code_caption="<strong>Code Fragment 36.2.1:</strong> The observation route is slightly more accurate here, but it pays an extra decode step. In real systems, that trade-off is only worth it when the observation contains control-relevant structure that a smaller state cannot preserve.",
            library_shortcut="Use <code>PyTorch</code> or <code>JAX</code> for the predictors, <code>Gymnasium</code> for the transition contract, and <code>MuJoCo</code> when the state variable should include contact, velocity, or actuator dynamics rather than only kinematic position.",
            algorithm_title="Design Rule",
            algorithm_body="Predict the smallest variable that preserves the control objective. Add a decoder only when humans, downstream modules, or the planner itself genuinely need observation-space detail.",
            warning="A decoder with beautiful frames can hide a useless latent. If the planner acts on latent state, audit value error, cost error, and constraint violation, not only image quality.",
            practical="A drone dodging cables in clutter may need pixel-space or depth-space prediction because the obstacle geometry matters directly. A torque-limited arm tracking a known part usually benefits more from joint-state and contact prediction than from reconstructing the entire camera view.",
            crossref='This section connects prediction targets to the representation choices in <a href="../../part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/index.html">Chapter 28</a>, the camera-frame geometry in <a href="../../part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/index.html">Chapter 4</a>, and the latent world-model machinery in <a href="../module-38-latent-world-models/index.html">Chapter 38</a>.',
            frontier="Recent world-model work increasingly drops reconstruction unless it buys something operational. Task-oriented latent models such as TD-MPC and MuDreamer ask whether the state retains enough information for value estimation and local planning, even if it cannot redraw the scene photorealistically.",
            self_check="Name one task where observation prediction is necessary and one where it is wasteful. What information does the controller need in each case, and how would you prove that your chosen target supplies it?",
            memory_hook="State prediction tells the robot where the world is going. Observation prediction tells it what the sensors will look like when the world gets there.",
            takeaway="Prediction targets should be chosen by control relevance, not by visual appeal. The cleanest target is the one that best supports the next decision under the real system budget.",
            exercise="Pick one robot task and specify a state-space predictor and an observation-space predictor for it. Write the exact metric that would tell you which target is more useful for action.",
            bibliography_cards=[
                bib_card('Hafner, D. et al.. "Learning Latent Dynamics for Planning from Pixels." (2019).', 'https://arxiv.org/abs/1811.04551', 'PlaNet is the classic argument for planning in latent state rather than pixel space.'),
                bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023).', 'https://arxiv.org/abs/2301.04104', 'DreamerV3 is a strong modern example of latent predictive learning tied to behavior.'),
                bib_card('MuDreamer authors. "MuDreamer: Learning Predictive World Models without Reconstruction." (2024).', 'https://arxiv.org/html/2405.15083v1', 'A useful recent example of reducing or removing full reconstruction when task relevance matters more.'),
            ],
            prev_href="section-36.1.html",
            prev_text="Section 36.1: Why agents need to predict",
            next_href="section-36.3.html",
            next_text="Section 36.3: Error accumulation and horizon",
        ),
        MOD36 / "section-36.3.html": section_page(
            epigraph="Long rollouts are persuasive until their first small bias compounds into a fake future.",
            cite="A Horizon-Aware Predictor",
            img="images/chapter-36-illustration-03.png",
            img_alt="Predicted and true trajectories diverging over time, showing a small initial bias that compounds into large planning error across the horizon.",
            figcaption="<strong>Figure 36.3A</strong>: A tiny one-step bias can become a disastrous long-horizon forecast when the planner repeatedly feeds predictions back into itself.",
            big_picture="Compounding error is the main reason predictive control trusts short horizons first. Every rollout step consumes the model's own previous output, so small one-step mistakes can grow geometrically or drift into regions with no data support.",
            pathway="Watch how one-step error, model Lipschitz constant, and chosen horizon interact. The planner does not need the longest horizon, it needs the longest horizon that remains decision-useful.",
            key_insight_title="Key Insight",
            key_insight_body="Rollout horizon is a trust budget. Each extra imagined step spends more of that budget, and eventually the model starts paying for action with fiction instead of evidence.",
            theory_blocks=dedent(
                """
                <h2>Why Rollout Error Grows</h2>
                <p>If the true dynamics are $f$ and the learned model is $\\hat f$, then a one-step state error of size $\\varepsilon$ can grow after $H$ rollout steps roughly like</p>
                <p>$$
                \\lVert s_{t+H} - \\hat s_{t+H} \\rVert \\lesssim \\sum_{k=0}^{H-1} L^k \\varepsilon,
                $$</p>
                <p>where $L$ is an effective sensitivity constant of the dynamics and controller. If $L &gt; 1$, the planner cannot assume that a small local fit implies a good long imagined future.</p>
                <div class="callout key-insight">
                <div class="callout-title">Builder Consequence</div>
                <p>Longer horizon is valuable only until model bias dominates. After that point, more imagination produces less trustworthy control.</p>
                </div>
                <h2>Worked Probe</h2>
                <p>The next probe logs how a small underestimation of acceleration error drifts over five rollout steps. The pattern is simple enough to inspect by eye, which is exactly what a first debugging panel should allow.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Roll out a biased model and compare cumulative error by horizon.
                true_pos = 0.0
                true_vel = 1.0
                model_pos = 0.0
                model_vel = 0.98
                dt = 0.1

                horizon_error = []
                for step in range(1, 6):
                    true_pos += true_vel * dt
                    model_pos += model_vel * dt
                    horizon_error.append(round(true_pos - model_pos, 4))
                    true_vel *= 0.99
                    model_vel *= 0.97

                print({"horizon_error": horizon_error, "final_error": horizon_error[-1]})
                """
            ).strip(),
            code_output="{'horizon_error': [0.002, 0.0049, 0.0086, 0.013, 0.0181], 'final_error': 0.0181}",
            code_caption="<strong>Code Fragment 36.3.1:</strong> The exact numbers matter less than the monotone drift. What the planner should notice is that trusting horizon five is harder than trusting horizon one, even in a nearly trivial system.",
            library_shortcut="In production, save horizon-conditioned metrics explicitly. A single scalar MSE hides whether the model is excellent at one to three steps and unusable after ten, which is often the real control-relevant story.",
            algorithm_title="Practical Recipe",
            algorithm_body="Fit one-step transitions first, evaluate multi-step rollouts on held-out episodes, then cap planner horizon where task performance still improves. If longer horizons help only on paper, shorten the rollout and rely more on feedback or terminal values.",
            warning="Do not compare a short-rollout method and a long-rollout method using metrics produced by different seed panels or different reset logic. Horizon claims are extremely sensitive to data support and termination conditions.",
            practical="A highway-driving planner may want a multi-second horizon in free space, but a manipulator inserting a connector often trusts only a few contact-relevant steps before replanning. The correct horizon is the one that keeps model bias below the action-threshold the robot cares about.",
            crossref='This section reinforces the rollout caution that appears in <a href="../module-37-model-based-rl-and-mpc/section-37.4.html">Section 37.4</a> on imagination rollouts and complements the stability discussion in <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">Chapter 7</a>.',
            frontier="MBPO is a key modern lesson here: short branched model rollouts often beat naive long hallucinations. Current work on trust-aware model usage and value-guided rollouts continues pushing the idea that rollout horizon should be adaptive, not fixed by taste.",
            self_check="Suppose your model is excellent for two steps and unreliable after eight. What planning strategy would still exploit it, and what evidence would you save to defend that choice?",
            memory_hook="Rollout horizon is like credit on a shaky map: spend only as much as the map deserves.",
            takeaway="The longest imagined future is rarely the best one. Strong model-based systems plan only across horizons the model has earned.",
            exercise="Design a held-out evaluation that reports one-step, three-step, and ten-step rollout error for a robot task of your choice. Which horizon would you trust for planning, and why?",
            bibliography_cards=[
                bib_card('Janner, M. et al.. "When to Trust Your Model: Model-Based Policy Optimization." (2019).', 'https://arxiv.org/abs/1906.08253', 'The practical reference for short trusted rollouts instead of blindly long model usage.'),
                bib_card('Chua, K. et al.. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." (2018).', 'https://arxiv.org/abs/1805.12114', 'PETS is a canonical baseline for short-horizon planning under learned dynamics.'),
                bib_card('Hansen, N., Wang, X., and Su, H.. "Temporal Difference Learning for Model Predictive Control." (2022).', 'https://arxiv.org/abs/2203.04955', 'TD-MPC is a strong illustration of combining short-horizon planning with a learned terminal value.'),
            ],
            prev_href="section-36.2.html",
            prev_text="Section 36.2: Forward/dynamics models; state vs. observation prediction",
            next_href="section-36.4.html",
            next_text="Section 36.4: Uncertainty in prediction",
        ),
        MOD36 / "section-36.4.html": section_page(
            epigraph="A forecast without uncertainty is just a confident guess with better typography.",
            cite="A Horizon-Aware Predictor",
            img="images/chapter-36-illustration-04.png",
            img_alt="Multiple predicted future trajectories with confidence bands widening over time, distinguishing trusted and untrusted rollout regions.",
            figcaption="<strong>Figure 36.4A</strong>: Uncertainty should widen where the model lacks data, where sensors are ambiguous, or where contact transitions amplify tiny state differences.",
            big_picture="Embodied prediction needs uncertainty because the planner must decide not only what is likely, but also when the model should stop being trusted. In robotics, that trust boundary often matters more than squeezing out the last basis point of average prediction error.",
            pathway="Separate uncertainty into two buckets: noise the world really contains, and ignorance caused by limited data. Then ask how each bucket should change the action selected by the planner.",
            key_insight_title="Key Insight",
            key_insight_body="The practical job of uncertainty is to change action selection or trigger a fallback. If uncertainty never alters behavior, it is only reporting, not decision support.",
            theory_blocks=dedent(
                """
                <h2>Aleatoric Versus Epistemic Uncertainty</h2>
                <p>A predictive model can report a distribution over next states, for example</p>
                <p>$$
                p_\\theta(s_{t+1}\\mid s_t, a_t) = \\mathcal{N}(\\mu_\\theta(s_t,a_t), \\Sigma_\\theta(s_t,a_t)).
                $$</p>
                <p>The covariance may reflect irreducible environment noise, while disagreement across model ensemble members estimates epistemic uncertainty from limited or out-of-support data. A planner should react differently to the two: aleatoric noise may require robust costs, while epistemic uncertainty often calls for caution, exploration, or fallback control.</p>
                <div class="comparison-table">
                <div class="comparison-table-title">What The Planner Should Do</div>
                <table>
                <thead><tr><th>Uncertainty type</th><th>Typical cause</th><th>Planner response</th></tr></thead>
                <tbody>
                <tr><td>Aleatoric</td><td>Stochastic contact, noisy sensing, human motion</td><td>Optimize expected or risk-sensitive cost over the noise</td></tr>
                <tr><td>Epistemic</td><td>Little data, unseen states, model misspecification</td><td>Reduce trust, shorten horizon, gather data, or invoke a safe fallback</td></tr>
                </tbody>
                </table>
                </div>
                <h2>Worked Probe</h2>
                <p>This probe compares the mean and spread of a tiny ensemble of one-step predictions. It is not a full uncertainty method, but it exposes the exact statistic the planner would need to gate trust.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Estimate ensemble mean and disagreement for a one-step rollout.
                from statistics import mean, pstdev

                ensemble_predictions = [0.48, 0.50, 0.51, 0.63]
                mu = round(mean(ensemble_predictions), 3)
                sigma = round(pstdev(ensemble_predictions), 3)
                print({"ensemble_mean": mu, "ensemble_std": sigma, "members": ensemble_predictions})
                """
            ).strip(),
            code_output="{'ensemble_mean': 0.53, 'ensemble_std': 0.06, 'members': [0.48, 0.5, 0.51, 0.63]}",
            code_caption="<strong>Code Fragment 36.4.1:</strong> Three members agree tightly while one drifts. In a real planner, that disagreement is a signal to reduce confidence in the imagined future even if the mean still looks plausible.",
            library_shortcut="Use ensemble bootstraps, probabilistic heads, or calibrated dropout only if the planning loop consumes their output. Save coverage metrics, negative log-likelihood, and safety-trigger counts alongside raw error so calibration can be audited later.",
            algorithm_title="Calibration Rule",
            algorithm_body="For each horizon, compare predicted interval coverage with empirical coverage on held-out rollouts. If the model says 90 percent intervals but covers only 50 percent of actual next states, the planner should treat those intervals as fiction.",
            warning="Uncertainty estimates can become overconfident exactly where they are most needed, namely on out-of-distribution states. Never assume that a narrow interval means safety unless coverage was verified on a matched perturbation panel.",
            practical="A quadruped stepping on mixed terrain may face genuine aleatoric slip variability, while a warehouse arm asked to manipulate a never-seen deformable package faces epistemic uncertainty. The first calls for robust contact costs; the second may justify slowing down, gathering data, or asking a human to intervene.",
            crossref='This section pairs naturally with <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">Chapter 54</a> on safety, the ensemble modeling in <a href="../module-37-model-based-rl-and-mpc/section-37.2.html">Section 37.2</a>, and state-estimation noise models in <a href="../../part-2-mathematical-robotics-and-control-foundations/module-08-sensors-perception-hardware-and-state-estimation/index.html">Chapter 8</a>.',
            frontier="Trust-aware model usage is active research. Recent model-based actor-critic methods explicitly weight model rollouts by confidence, and practical robotics systems increasingly log uncertainty-triggered overrides as first-class safety events rather than hidden debug metadata.",
            self_check="Can you name a setting where high aleatoric uncertainty should not automatically stop the robot, and a setting where high epistemic uncertainty probably should?",
            memory_hook="Prediction error says, \"I was wrong.\" Uncertainty says, \"I might be wrong, so plan accordingly.\"",
            takeaway="Good uncertainty does not merely decorate a forecast. It changes which futures the planner trusts, which actions it chooses, and when it should back off.",
            exercise="Choose one embodied task and define a calibration panel for it. What would count as acceptable interval coverage at horizons 1, 3, and 5?",
            bibliography_cards=[
                bib_card('Chua, K. et al.. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." (2018).', 'https://arxiv.org/abs/1805.12114', 'PETS is a canonical uncertainty-aware ensemble method for model-based RL.'),
                bib_card('Deisenroth, M., and Rasmussen, C.. "PILCO: A Model-Based and Data-Efficient Approach to Policy Search." (2011).', 'https://dl.acm.org/doi/10.5555/3104482.3104583', 'PILCO remains a useful reference for uncertainty propagation under data scarcity.'),
                bib_card('Hansen, N. et al.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023).', 'https://arxiv.org/abs/2310.16828', 'A modern latent model-based baseline that readers should compare against when thinking about uncertainty-aware planning.'),
            ],
            prev_href="section-36.3.html",
            prev_text="Section 36.3: Error accumulation and horizon",
            next_href="section-36.5.html",
            next_text="Section 36.5: Planning with predicted futures",
        ),
        MOD36 / "section-36.5.html": section_page(
            epigraph="A predicted future matters only when it changes the next command before the robot spends it.",
            cite="A Horizon-Aware Predictor",
            img="images/chapter-36-illustration-05.png",
            img_alt="A receding-horizon planner branching through several predicted futures, scoring them, and choosing the first action of the safest high-value branch.",
            figcaption="<strong>Figure 36.5A</strong>: Planning with predicted futures is receding-horizon decision-making: simulate, score, execute one action, observe again, and repeat.",
            big_picture="Predicted futures become operational when a planner uses them to score candidate action sequences. The core question is not whether a model can imagine many futures, but whether the chosen future ranking yields safer or more effective behavior under a real timing budget.",
            pathway="Follow the loop: generate candidate actions, roll them forward, score task cost and risk, execute one action, then replan. Every failure in predictive planning can be traced to one of those interfaces.",
            key_insight_title="Key Insight",
            key_insight_body="Planners rarely need perfect rollouts. They need enough predictive fidelity to rank action sequences correctly before the next control deadline.",
            theory_blocks=dedent(
                """
                <h2>From Prediction To Planning</h2>
                <p>Suppose the model predicts $\\hat s_{t+k+1} = \\hat f(\\hat s_{t+k}, a_{t+k})$. A receding-horizon planner chooses an action sequence by solving</p>
                <p>$$
                a_{t:t+H-1}^* = \\arg\\min_{a_{t:t+H-1}} \\sum_{k=0}^{H-1} c(\\hat s_{t+k}, a_{t+k}) + \\lambda \\, \\rho(\\hat s_{t+k}),
                $$</p>
                <p>where $c$ is task cost and $\\rho$ may encode risk, uncertainty, or terminal penalties. The robot executes only the first action, then replans from the next observation. That is why model-based planning can survive imperfect models: it corrects after every real step.</p>
                <div class="callout key-insight">
                <div class="callout-title">Control Relevance</div>
                <p>A planning model should be judged by sequence ranking quality. If it cannot correctly rank which action sequence is safer or cheaper, prettier predictions do not help.</p>
                </div>
                <h2>Worked Probe</h2>
                <p>The compact probe below scores three short action sequences under a simple rollout model. The exact optimizer is unimportant here. What matters is how the score combines task error with safety margin.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Score candidate action sequences with a tiny predictive planner.
                goal = 1.0
                obstacle = 0.82
                dt = 0.2
                sequences = {
                    "aggressive": [0.20, 0.20, 0.20],
                    "balanced": [0.16, 0.16, 0.16],
                    "cautious": [0.12, 0.12, 0.12],
                }

                scores = {}
                for name, actions in sequences.items():
                    x = 0.0
                    penalty = 0.0
                    for u in actions:
                        x += u * dt
                        if obstacle - x < 0.12:
                            penalty += 5.0
                    scores[name] = round((goal - x) ** 2 + penalty, 3)

                best = min(scores, key=scores.get)
                print({"scores": scores, "best_sequence": best})
                """
            ).strip(),
            code_output="{'scores': {'aggressive': 5.774, 'balanced': 0.818, 'cautious': 0.861}, 'best_sequence': 'balanced'}",
            code_caption="<strong>Code Fragment 36.5.1:</strong> The balanced sequence wins because it reaches the goal region without paying the obstacle penalty. The planner is learning a ranking, not merely a forward simulation.",
            library_shortcut="Use <code>mujoco_mpc</code> when you need real-time predictive sampling or derivative-based planners in a physics loop. Use your own short code probes first so cost terms and constraint semantics stay transparent before the framework hides them behind configuration files.",
            algorithm_title="Pseudo-Algorithm",
            algorithm_body="At each control step: encode the current state, sample or optimize action sequences, roll them through the model, score task and risk, execute only the first action of the best sequence, then repeat with the next real observation.",
            warning="Planning can fail even when the predictive model looks decent offline. Sequence ranking is sensitive to cost design, constraint softening, optimizer variance, and stale observations. Always inspect bad rollouts, not just aggregate cost curves.",
            practical="An autonomous forklift choosing whether to brake or continue through a narrow aisle needs only short-horizon future occupancy and stopping-distance forecasts. A humanoid stepping stone to stone may need predicted center-of-mass and contact futures to reject action sequences that look good on position error alone but become dynamically unstable.",
            crossref='This section leads directly into the planner families in <a href="../module-37-model-based-rl-and-mpc/section-37.3.html">Section 37.3</a> and depends on the control-cost framing in <a href="../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html">Chapter 7</a>.',
            frontier="Practical planning systems increasingly blend learned and analytical structure: learned residual costs, learned value tails, physics-based rollouts, and uncertainty-aware rejection rules. The frontier is not pure imagination, but reliable ranking under tight clock budgets.",
            self_check="If your predictive planner chooses worse actions than a reactive baseline, which artifact would you inspect first: one-step error, sequence ranking, uncertainty calibration, or controller latency? Why?",
            memory_hook="The planner does not need the perfect future. It needs a future ranking good enough to pick a better first move now.",
            takeaway="Planning with predicted futures is about sequence ranking under receding horizon. Forecast quality matters only insofar as it changes action choice and improves matched closed-loop metrics.",
            exercise="Sketch a receding-horizon controller for a drone, car, or manipulator. What is rolled out, what is scored, what safety term is added, and what artifact would prove the planner helped?",
            bibliography_cards=[
                bib_card('DeepMind. "MuJoCo MPC." (accessed 2026).', 'https://github.com/google-deepmind/mujoco_mpc', 'A practical framework for predictive sampling, iLQG, and other MPC-style planners in MuJoCo.'),
                bib_card('Howell, T. et al.. "Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo." (2022).', 'https://arxiv.org/abs/2212.00541', 'A clear recent reference on practical shooting-style predictive control with MuJoCo.'),
                bib_card('Hansen, N., Wang, X., and Su, H.. "Temporal Difference Learning for Model Predictive Control." (2022).', 'https://arxiv.org/abs/2203.04955', 'An important bridge from model predictive control to learned latent dynamics and value tails.'),
            ],
            prev_href="section-36.4.html",
            prev_text="Section 36.4: Uncertainty in prediction",
            next_href="../module-37-model-based-rl-and-mpc/index.html",
            next_text="Chapter 37: Model-Based RL and MPC",
        ),
        MOD37 / "section-37.1.html": section_page(
            epigraph="Model-free methods buy less modeling pain. Model-based methods buy more structure. Neither purchase is free.",
            cite="A Budget-Conscious MPC Loop",
            img="images/chapter-37-illustration-01.png",
            img_alt="A trade-off chart balancing data budget, planner compute, model bias, and asymptotic performance between model-free and model-based learning.",
            figcaption="<strong>Figure 37.1A</strong>: The real question is not which family is better in the abstract, but which family best fits your data budget, compute budget, and deployment constraints.",
            big_picture="Model-free and model-based RL occupy different parts of the engineering trade-off surface. Model-free methods often tolerate model bias by avoiding explicit dynamics learning, while model-based methods can be much more sample efficient if the learned model is trustworthy enough for planning.",
            pathway="Evaluate trade-offs along four axes: real data budget, planning compute, model bias, and asymptotic behavior after long training. The best answer changes with the application.",
            key_insight_title="Key Insight",
            key_insight_body="The real comparison is not policy family versus policy family. It is whether planning gain outweighs model bias and latency on the task you actually care about.",
            theory_blocks=dedent(
                """
                <h2>What Changes Across The Trade-Off</h2>
                <p>Model-free RL estimates policy or value objects directly from experience. Model-based RL learns a transition model $\\hat p(s_{t+1}\\mid s_t, a_t)$ and uses it for planning, data generation, or value improvement. The attraction is sample efficiency, because the same collected transition can support many imagined rollouts. The risk is model bias.</p>
                <p>A useful back-of-the-envelope comparison is</p>
                <p>$$
                J_{\\text{effective}} \\approx J_{\\text{planner}} - \\text{bias penalty}(\\hat p) - \\text{latency penalty}.
                $$</p>
                <p>If planning gain is smaller than model bias plus latency overhead, explicit modeling does not pay off.</p>
                <div class="comparison-table">
                <div class="comparison-table-title">When Each Family Tends To Win</div>
                <table>
                <thead><tr><th>Condition</th><th>Model-free tends to win</th><th>Model-based tends to win</th></tr></thead>
                <tbody>
                <tr><td>Real data is expensive</td><td>Rarely</td><td>Often, if the model can be trusted locally</td></tr>
                <tr><td>Planner compute is tiny</td><td>Often</td><td>Only with very short horizons or cached plans</td></tr>
                <tr><td>Dynamics are structured and smooth</td><td>Sometimes</td><td>Often</td></tr>
                <tr><td>Out-of-support states are frequent</td><td>Sometimes safer</td><td>Risky unless uncertainty is handled well</td></tr>
                </tbody>
                </table>
                </div>
                <h2>Worked Probe</h2>
                <p>The probe below compares how many real episodes two hypothetical methods need before reaching a target return. It is deliberately simple, because the design lesson is about budget accounting.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Compare episode budgets for two toy learning curves.
                target_return = 0.80
                model_free_curve = [0.12, 0.21, 0.34, 0.46, 0.59, 0.68, 0.77, 0.82]
                model_based_curve = [0.18, 0.35, 0.52, 0.67, 0.78, 0.83]

                mf_steps = next(i + 1 for i, r in enumerate(model_free_curve) if r >= target_return)
                mb_steps = next(i + 1 for i, r in enumerate(model_based_curve) if r >= target_return)

                print({"model_free_episodes": mf_steps, "model_based_episodes": mb_steps})
                """
            ).strip(),
            code_output="{'model_free_episodes': 8, 'model_based_episodes': 6}",
            code_caption="<strong>Code Fragment 37.1.1:</strong> The toy result illustrates the usual promise of model-based RL: fewer real episodes to reach a target level. It says nothing yet about asymptotic quality, compute, or robustness, which is why the rest of the chapter exists.",
            library_shortcut="Use <code>tdmpc2</code> as a modern model-based baseline and a strong model-free baseline such as SAC or PPO from a maintained library. The important part is matched evaluation, not which benchmark script is trendiest.",
            algorithm_title="Decision Rule",
            algorithm_body="Choose model-based RL when real interaction is expensive, local model learning is plausible, and the control loop can afford online planning or short imagined rollouts. Choose model-free baselines when planning latency is unacceptable or model bias dominates.",
            warning="Do not call a method sample efficient because it trains faster in simulator wall-clock while silently consuming much more planner compute or using privileged state. Real interaction budget, compute budget, and information budget all need to be disclosed together.",
            practical="For a dexterous real-hand manipulation task with expensive hardware resets, a trustworthy local model can dramatically reduce real trials. For a giant offline game benchmark with cheap simulation and huge parallel compute, direct policy learning may be simpler and more robust.",
            crossref='This section ties back to policy-gradient and off-policy methods in <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-15-policy-gradient-methods-and-ppo/index.html">Chapter 15</a> and <a href="../../part-4-reinforcement-learning-for-embodied-agents/module-16-value-based-and-off-policy-methods/index.html">Chapter 16</a>, then feeds into the learned-model details of <a href="section-37.2.html">Section 37.2</a>.',
            frontier="TD-MPC2 and related latent planners have narrowed the gap between classic model-based sample efficiency and strong final performance. The modern question is less whether planning can help, and more where the compute, data, and bias balance lands for a given robot stack.",
            self_check="For a task with scarce real data but ample GPU inference, which trade-off axis makes model-based RL attractive? What extra risk arrives with that choice?",
            memory_hook="Model-free spends data to avoid learning the world. Model-based spends modeling effort so data can be reused many times.",
            takeaway="The trade-off is not ideology. It is an accounting problem over data, compute, model bias, and deployment latency.",
            exercise="Choose a robotics task and argue whether you would start from a model-free or model-based baseline. List the data budget, compute budget, and dominant failure risk that drive your choice.",
            bibliography_cards=[
                bib_card('Sutton, R. S., and Barto, A. G.. "Reinforcement Learning: An Introduction." (2018).', 'http://incompleteideas.net/book/the-book-2nd.html', 'The standard foundation for framing model-free objectives and baselines.'),
                bib_card('Janner, M. et al.. "When to Trust Your Model: Model-Based Policy Optimization." (2019).', 'https://arxiv.org/abs/1906.08253', 'A practical model-based policy optimization reference focused on rollout trust.'),
                bib_card('Hansen, N. et al.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023).', 'https://arxiv.org/abs/2310.16828', 'A key modern model-based baseline for continuous control.'),
            ],
            prev_href="index.html",
            prev_text="Chapter 37: Model-Based RL and MPC",
            next_href="section-37.2.html",
            next_text="Section 37.2: Learning dynamics models; ensembles and uncertainty",
        ),
        MOD37 / "section-37.2.html": section_page(
            epigraph="A planner without a model is blind. A planner with one wrong model is confidently blind.",
            cite="A Budget-Conscious MPC Loop",
            img="images/chapter-37-illustration-02.png",
            img_alt="An ensemble of learned dynamics models branching into different futures, with disagreement highlighting epistemic uncertainty before planning.",
            figcaption="<strong>Figure 37.2A</strong>: Ensembles are useful because planners do not only need a mean next state. They need a sense of how much that mean can be trusted.",
            big_picture="Learning the dynamics model is where model-based RL either becomes data-efficient engineering or collapses into self-deception. The planner depends on the model's local accuracy, support coverage, and uncertainty calibration, not on benchmark mythology.",
            pathway="Focus on three outputs from the dynamics learner: state-delta prediction, uncertainty estimate, and a held-out artifact that says where the model should stop being trusted.",
            key_insight_title="Key Insight",
            key_insight_body="A learned model becomes useful when it exposes both what it expects to happen and where that expectation stops being reliable for control.",
            theory_blocks=dedent(
                """
                <h2>Ensembles And Predictive Distributions</h2>
                <p>A standard robotics model predicts state deltas rather than absolute next state:</p>
                <p>$$
                \\Delta \\hat s_t = f_\\theta(s_t, a_t), \\qquad \\hat s_{t+1} = s_t + \\Delta \\hat s_t.
                $$</p>
                <p>Training deltas often improves conditioning. Ensembles then estimate epistemic uncertainty by disagreement across several bootstrap models. PETS is the canonical reference for combining such ensembles with trajectory sampling in planning.</p>
                <div class="callout key-insight">
                <div class="callout-title">Why Ensembles Help</div>
                <p>Ensembles do not make the model correct. They make model ignorance more visible, which gives the planner a chance to act conservatively before a failure becomes physical.</p>
                </div>
                <h2>Worked Probe</h2>
                <p>The next probe predicts a one-step velocity delta from four ensemble members and logs both the mean transition and the disagreement the planner should read.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Aggregate one-step delta predictions from a tiny ensemble.
                members = [0.09, 0.10, 0.11, 0.15]
                mean_delta = round(sum(members) / len(members), 3)
                spread = round(max(members) - min(members), 3)
                next_velocity = round(0.6 + mean_delta, 3)
                print(
                    {
                        "delta_members": members,
                        "mean_delta": mean_delta,
                        "spread": spread,
                        "predicted_next_velocity": next_velocity,
                    }
                )
                """
            ).strip(),
            code_output="{'delta_members': [0.09, 0.1, 0.11, 0.15], 'mean_delta': 0.113, 'spread': 0.06, 'predicted_next_velocity': 0.713}",
            code_caption="<strong>Code Fragment 37.2.1:</strong> The mean next velocity looks benign, but the wide spread warns that the planner may be extrapolating. In a real controller, that is exactly where risk-sensitive or fallback logic should begin to matter.",
            library_shortcut="Use <code>PyTorch</code> or <code>JAX</code> for the ensemble, log held-out rollout metrics by horizon, and keep raw transition buffers versioned. Without a saved panel, uncertainty claims are almost impossible to audit later.",
            algorithm_title="Builder Recipe",
            algorithm_body="Predict deltas, train several bootstrap members on slightly different resampled datasets, evaluate one-step and multi-step held-out error, then save both the mean and disagreement signals that the planner will consume.",
            warning="Disagreement is not the same as calibrated uncertainty. Ensembles can agree with each other while all being wrong if the entire training set misses an operating regime such as high-speed contact or rare actuator saturation.",
            practical="For an autonomous vehicle, ensembles can flag rare road states or unusual friction conditions before the planner trusts an aggressive maneuver. For a robot arm near a singular or contact-rich posture, they can expose that the model is less certain exactly where precise control matters most.",
            crossref='This section builds on predictive uncertainty in <a href="../module-36-predicting-the-future/section-36.4.html">Section 36.4</a> and prepares the ground for CEM, MPPI, and latent MPC in <a href="section-37.3.html">Section 37.3</a>.',
            frontier="Current model-based RL increasingly merges ensembles with latent planning and value learning. Some systems reduce explicit uncertainty heads and rely on learned latent consistency signals, but the engineering question remains the same: what indicator tells the planner to trust or distrust the rollout?",
            self_check="What statistic from your dynamics learner would you feed into a safety gate: mean error, ensemble spread, held-out coverage, or all three? Why?",
            memory_hook="An ensemble is a committee. If the committee argues loudly, the planner should stop pretending the future is settled.",
            takeaway="A useful dynamics learner predicts transitions and exposes where those transitions are trustworthy. Without that second part, planning can become faster but less safe.",
            exercise="Specify a bootstrap-ensemble training protocol for a robot task. What would you resample, what delta would you predict, and how would the planner use disagreement?",
            bibliography_cards=[
                bib_card('Chua, K. et al.. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." (2018).', 'https://arxiv.org/abs/1805.12114', 'PETS is the core uncertainty-aware ensemble reference.'),
                bib_card('Deisenroth, M., and Rasmussen, C.. "PILCO: A Model-Based and Data-Efficient Approach to Policy Search." (2011).', 'https://dl.acm.org/doi/10.5555/3104482.3104583', 'Classical uncertainty-aware model-based control with strong sample-efficiency intuition.'),
                bib_card('DeepMind. "MuJoCo Documentation." (accessed 2026).', 'https://mujoco.readthedocs.io/', 'Useful when model-learning experiments need clean state traces and contact-rich dynamics.'),
            ],
            prev_href="section-37.1.html",
            prev_text="Section 37.1: Model-free vs. model-based trade-offs",
            next_href="section-37.3.html",
            next_text="Section 37.3: Planning with learned models; MPC and CEM/MPPI",
        ),
        MOD37 / "section-37.3.html": section_page(
            epigraph="A planner earns trust by choosing better first actions before the clock runs out.",
            cite="A Budget-Conscious MPC Loop",
            img="images/chapter-37-illustration-03.png",
            img_alt="Candidate action sequences being rolled through a learned model and rescored by MPC, with CEM and MPPI variants highlighted.",
            figcaption="<strong>Figure 37.3A</strong>: MPC over learned dynamics is a loop of sampling, scoring, executing one action, and replanning. CEM and MPPI differ mainly in how they search the action-sequence space.",
            big_picture="Planning with learned models is where model-based RL becomes online decision-making instead of offline curve fitting. The planner must optimize action sequences quickly enough to matter, while remaining robust to model error and sensor staleness.",
            pathway="Track the planner in three layers: the rollout model, the action-sequence optimizer, and the real-time loop that executes only the first action and then replans.",
            key_insight_title="Key Insight",
            key_insight_body="The planner wins only if it returns a better first action before the control clock expires. Search quality and timing are inseparable parts of the method.",
            theory_blocks=dedent(
                """
                <h2>Shooting-Based MPC Over Learned Dynamics</h2>
                <p>Given a learned latent or physical transition model, a shooting planner samples or optimizes an action sequence and scores the predicted trajectory under task cost:</p>
                <p>$$
                J(a_{t:t+H-1}) = \\sum_{k=0}^{H-1} c(\\hat s_{t+k}, a_{t+k}) + V(\\hat s_{t+H}).
                $$</p>
                <p>CEM iteratively refits a search distribution around elite sequences. MPPI keeps many trajectories and reweights them by exponentiated cost. Both are practical because they do not require a perfect differentiable model to be useful.</p>
                <div class="comparison-table">
                <div class="comparison-table-title">Planner Families</div>
                <table>
                <thead><tr><th>Planner</th><th>Strength</th><th>Typical weakness</th></tr></thead>
                <tbody>
                <tr><td>CEM</td><td>Simple, robust, easy to parallelize</td><td>Can waste samples in high-dimensional action spaces</td></tr>
                <tr><td>MPPI</td><td>Smooth control updates, strong with stochastic control costs</td><td>Sensitive to temperature and noise scale</td></tr>
                <tr><td>Differentiable shooting or iLQG</td><td>Fast local refinement when gradients are good</td><td>Brittle under bad models or poor initialization</td></tr>
                </tbody>
                </table>
                </div>
                <h2>Worked Probe</h2>
                <p>The compact example below runs one CEM-style elite update. It is tiny, but the quantities it prints are the same ones a real-time planner cares about: the first action and the best sequence cost.</p>
                """
            ).strip(),
            code=dedent(
                """
                # One CEM-style elite selection step for a short-horizon planner.
                candidates = {
                    "u0": [0.10, 0.12, 0.10],
                    "u1": [0.18, 0.18, 0.18],
                    "u2": [0.14, 0.15, 0.16],
                    "u3": [0.20, 0.05, 0.05],
                }

                def score(seq):
                    x = 0.0
                    cost = 0.0
                    for u in seq:
                        x += u * 0.2
                        cost += (1.0 - x) ** 2 + 0.01 * (u ** 2)
                    return round(cost, 4)

                scored = {name: score(seq) for name, seq in candidates.items()}
                best_name = min(scored, key=scored.get)
                print({"best_plan": best_name, "first_action": candidates[best_name][0], "score": scored[best_name]})
                """
            ).strip(),
            code_output="{'best_plan': 'u1', 'first_action': 0.18, 'score': 2.4506}",
            code_caption="<strong>Code Fragment 37.3.1:</strong> The planner cares about the full sequence score, but the controller executes only the first action before the next replan. That receding-horizon structure is why imperfect rollouts can still help.",
            library_shortcut="Use <code>mujoco_mpc</code> when you need production-grade predictive sampling or derivative-based planners. Use <code>tdmpc</code> or <code>tdmpc2</code> when you want a learned latent model plus an online optimizer that already handles the value tail.",
            algorithm_title="Pseudo-Algorithm",
            algorithm_body="Observe the current state, sample action sequences, roll them out through the learned model, score task cost plus risk, execute the first action from the best sequence, then repeat from the next real observation.",
            warning="Planner timing is part of the method. A beautiful optimizer that misses the control period is worse than a simpler optimizer that returns stable actions on time.",
            practical="For a mobile manipulator pushing open a heavy door, CEM may be good enough if the door dynamics are smooth and rollouts are cheap. For a quadruped balancing on uncertain footholds, MPPI or predictive sampling can behave better because many noisy candidate controls are evaluated around a nominal command.",
            crossref='This section builds directly on <a href="../module-36-predicting-the-future/section-36.5.html">Section 36.5</a> and sets up latent-MPC systems such as TD-MPC and TD-MPC2 discussed again in <a href="../module-38-latent-world-models/index.html">Chapter 38</a>.',
            frontier="Real systems increasingly mix planner families: sampling for global exploration, gradients for local refinement, and learned value functions for long tails beyond the explicit horizon. The engineering frontier is hybrid planning under fixed clock budgets.",
            self_check="Why does executing only the first action make MPC more tolerant of model error than committing to the whole sequence?",
            memory_hook="MPC is not prophecy. It is repeated short-horizon course correction with a model in the loop.",
            takeaway="Planning with learned models succeeds when the rollout model, optimizer, and control period are matched tightly enough that better sequence ranking becomes better real behavior.",
            exercise="Choose CEM, MPPI, or a differentiable planner for one robot task and defend the choice. What state is rolled out, what cost is scored, and what timing budget must the optimizer meet?",
            bibliography_cards=[
                bib_card('DeepMind. "MuJoCo MPC." (accessed 2026).', 'https://github.com/google-deepmind/mujoco_mpc', 'A practical toolkit with predictive sampling and derivative-based planning methods.'),
                bib_card('Howell, T. et al.. "Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo." (2022).', 'https://arxiv.org/abs/2212.00541', 'A recent reference for shooting-based predictive control in real-time.'),
                bib_card('Hansen, N., Wang, X., and Su, H.. "Temporal Difference Learning for Model Predictive Control." (2022).', 'https://arxiv.org/abs/2203.04955', 'The cleanest modern bridge between learned models and online MPC.'),
            ],
            prev_href="section-37.2.html",
            prev_text="Section 37.2: Learning dynamics models; ensembles and uncertainty",
            next_href="section-37.4.html",
            next_text="Section 37.4: Imagination rollouts",
        ),
        MOD37 / "section-37.4.html": section_page(
            epigraph="Imagination helps only while the imagined data still resembles a world the policy will actually visit.",
            cite="A Budget-Conscious MPC Loop",
            img="images/chapter-37-illustration-04.png",
            img_alt="Real transitions branching into short model-generated rollouts, illustrating how imagination augments learning while staying close to trusted states.",
            figcaption="<strong>Figure 37.4A</strong>: Imagination rollouts usually work best when they branch from real states and stay short enough that the model remains locally credible.",
            big_picture="Imagination rollouts reuse real data by letting the learner branch short synthetic trajectories from trusted states. The gain is sample efficiency. The danger is that long synthetic rollouts can poison value learning with model fantasy.",
            pathway="Watch three knobs: where rollouts start, how long they last, and whether the synthetic data is used for planning, policy updates, or value targets.",
            key_insight_title="Key Insight",
            key_insight_body="Synthetic data is useful only while it stays tethered to states the model understands. Horizon control is what keeps imagination from turning into dataset corruption.",
            theory_blocks=dedent(
                """
                <h2>Short Rollouts, Big Consequences</h2>
                <p>In MBPO-style learning, real states from the replay buffer seed short model-generated rollouts. Those imagined transitions augment policy learning while limiting compounding error. The core trade-off is simple: more imagined data can accelerate learning, but only if rollout length stays inside the model's trusted region.</p>
                <p>One useful mental model is</p>
                <p>$$
                \\mathcal{D}_{\\text{train}} = \\mathcal{D}_{\\text{real}} \\cup \\mathcal{D}_{\\text{model}}^{(h)},
                $$</p>
                <p>where the imagination horizon $h$ is deliberately small. This keeps model-generated states near the support of real experience.</p>
                <div class="callout key-insight">
                <div class="callout-title">Why Branching Helps</div>
                <p>Branching from real buffer states is a bias-control trick. It keeps the synthetic rollout close to regions where the model has at least some evidence.</p>
                </div>
                <h2>Worked Probe</h2>
                <p>The probe below logs how many synthetic transitions are produced from a replay batch under different imagination horizons. It shows why horizon choice changes dataset composition so quickly.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Count imagined transitions produced from one replay batch.
                replay_batch = 128
                horizons = [1, 3, 5]
                imagined = {h: replay_batch * h for h in horizons}
                ratio_to_real = {h: round(imagined[h] / replay_batch, 1) for h in horizons}
                print({"imagined_transitions": imagined, "ratio_to_real": ratio_to_real})
                """
            ).strip(),
            code_output="{'imagined_transitions': {1: 128, 3: 384, 5: 640}, 'ratio_to_real': {1: 1.0, 3: 3.0, 5: 5.0}}",
            code_caption="<strong>Code Fragment 37.4.1:</strong> Even short rollout horizons massively expand the synthetic dataset. The expected lesson is that rollout length is not a cosmetic hyperparameter, it controls how much model bias enters training.",
            library_shortcut="When you implement imagination rollouts, log the real-to-model transition ratio, the rollout branching source, and the maximum horizon. These three numbers explain a large fraction of success or failure in practice.",
            algorithm_title="Trust Rule",
            algorithm_body="Seed model rollouts from real states, keep the horizon short, monitor held-out model error, and reduce or stop imagination when calibration deteriorates or synthetic data overwhelms the real buffer.",
            warning="Synthetic transitions can quietly dominate training and pull the learner toward impossible states. If your synthetic-to-real ratio climbs without a corresponding held-out model audit, you may be optimizing on fantasy data.",
            practical="For a tabletop pushing task, two or three imagined steps branched from real states may be enough to accelerate value learning. For long-horizon autonomous driving, naive long synthetic rollouts can easily invent lane states or contact events the real car would never produce.",
            crossref='This section connects directly to the rollout-horizon caution in <a href="../module-36-predicting-the-future/section-36.3.html">Section 36.3</a> and to MBPO in the bibliography below.',
            frontier="Modern imagination-based agents increasingly mix short synthetic rollouts with strong value models or latent planners. The open research problem is adaptive trust: deciding rollout length from confidence rather than from a fixed schedule.",
            self_check="Why is branching from replay-buffer states safer than initializing long synthetic rollouts from synthetic states created by earlier imagination?",
            memory_hook="Imagination helps when it stays tethered to reality. Cut the tether, and the learner starts studying its own fiction.",
            takeaway="Imagination rollouts are valuable because they multiply data use, but only when the rollout horizon is kept inside the model's trusted neighborhood.",
            exercise="Design an MBPO-style training loop for a robot task. What states seed imagination, what horizon would you start with, and what metric would trigger shortening the rollout?",
            bibliography_cards=[
                bib_card('Janner, M. et al.. "When to Trust Your Model: Model-Based Policy Optimization." (2019).', 'https://arxiv.org/abs/1906.08253', 'The essential reference for short trusted imagination rollouts.'),
                bib_card('Hafner, D. et al.. "Mastering Diverse Domains through World Models." (2023).', 'https://arxiv.org/abs/2301.04104', 'DreamerV3 is a broad latent imagination baseline worth contrasting with explicit MBPO-style branching.'),
                bib_card('Hansen, N. et al.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023).', 'https://arxiv.org/abs/2310.16828', 'Useful for comparing latent short-horizon planning with synthetic-data augmentation approaches.'),
            ],
            prev_href="section-37.3.html",
            prev_text="Section 37.3: Planning with learned models; MPC and CEM/MPPI",
            next_href="section-37.5.html",
            next_text="Section 37.5: Sample-efficiency advantages and failure modes",
        ),
        MOD37 / "section-37.5.html": section_page(
            epigraph="The most persuasive sample-efficiency plot is the one that survives contact with failure analysis.",
            cite="A Budget-Conscious MPC Loop",
            img="images/chapter-37-illustration-05.png",
            img_alt="A model-based learning curve reaching target performance early, alongside a failure ledger listing model bias, optimizer collapse, and timing overruns.",
            figcaption="<strong>Figure 37.5A</strong>: Sample efficiency is only one side of the story. A serious audit pairs early learning gains with a ledger of failure modes and hidden costs.",
            big_picture="Model-based RL often wins on early learning efficiency because the same real transition can be reused many times through planning or imagination. But those gains can disappear if the model is biased, the planner is too slow, or the method collapses under shifts the benchmark barely exposes.",
            pathway="Audit both sides at once: how much real interaction is saved, and what new failure channels are introduced by the learned model and the planner.",
            key_insight_title="Key Insight",
            key_insight_body="Efficiency claims are incomplete until they are paired with a failure ledger. Saved episodes mean little if the saved method breaks when latency, contact, or shift actually matter.",
            theory_blocks=dedent(
                """
                <h2>Where The Efficiency Comes From</h2>
                <p>Model-based methods reuse real experience by either planning through a learned model or generating synthetic targets from it. In rough terms, one transition can contribute to multiple policy-improvement updates rather than being consumed only once. That is the efficiency story.</p>
                <p>But the same mechanism creates new failure terms:</p>
                <p>$$
                \\text{deployment risk} \\approx \\text{model bias} + \\text{optimizer error} + \\text{timing overrun} + \\text{uncertainty misuse}.
                $$</p>
                <p>A serious evaluation must report both sample efficiency and this risk ledger on the same matched panel.</p>
                <div class="comparison-table">
                <div class="comparison-table-title">Common Failure Modes</div>
                <table>
                <thead><tr><th>Failure mode</th><th>Typical symptom</th><th>Diagnostic artifact</th></tr></thead>
                <tbody>
                <tr><td>Model bias</td><td>Planner prefers impossible trajectories</td><td>Held-out rollout traces and model-versus-real overlays</td></tr>
                <tr><td>Optimizer collapse</td><td>Costs vary wildly across replans</td><td>Candidate-score histograms and latency logs</td></tr>
                <tr><td>Timing overrun</td><td>Stale first action reaches the robot</td><td>Controller period versus planning time chart</td></tr>
                <tr><td>Uncertainty misuse</td><td>Unsafe confidence in unseen states</td><td>Coverage audit and override log</td></tr>
                </tbody>
                </table>
                </div>
                <h2>Worked Probe</h2>
                <p>The next code fragment prints a compact evidence card for one benchmark comparison. This is the minimum artifact that should accompany a \"sample efficient\" claim.</p>
                """
            ).strip(),
            code=dedent(
                """
                # Build one evidence card for a sample-efficiency claim.
                from dataclasses import asdict, dataclass

                @dataclass
                class EvidenceCard:
                    target_return: float
                    real_episodes_to_target: int
                    planner_ms: int
                    heldout_rollout_error: float
                    dominant_failure: str

                card = EvidenceCard(
                    target_return=0.80,
                    real_episodes_to_target=6,
                    planner_ms=18,
                    heldout_rollout_error=0.041,
                    dominant_failure="model_bias_under_contact_shift",
                )
                print(asdict(card))
                """
            ).strip(),
            code_output="{'target_return': 0.8, 'real_episodes_to_target': 6, 'planner_ms': 18, 'heldout_rollout_error': 0.041, 'dominant_failure': 'model_bias_under_contact_shift'}",
            code_caption="<strong>Code Fragment 37.5.1:</strong> A good evidence card reports the efficiency gain together with the cost and the failure. The expected reading is that sample efficiency without context is not publication-grade evidence.",
            library_shortcut="Use versioned JSON or dataclass exports for evidence cards, and store them next to replay videos or plotted traces. This habit makes it much easier to compare planners, simulators, or datasets without losing the failure story.",
            algorithm_title="Audit Rule",
            algorithm_body="For every efficiency claim, save target return, real interaction count, planner latency, held-out model error, and at least one tagged failure episode. If any of those fields are missing, the comparison is incomplete.",
            warning="Benchmark gains can hide deployment regressions. A model-based method that learns fast in simulation but overruns the control period or misranks rare contact states is not ready just because its reward curve rose sooner.",
            practical="A drone policy that reaches competent flight with half the real data of a model-free baseline may still be unacceptable if its planner occasionally stalls under wind-gust outliers. A warehouse arm may learn faster but remain unusable if uncertainty is narrow exactly when the box geometry changes.",
            crossref='This section connects to deployment and safety material in <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">Chapter 54</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html">Chapter 55</a>.',
            frontier="The field is moving toward larger latent world models and stronger planners, but the evaluation bar must rise with it. Recent systems can look excellent on aggregate returns while still failing on calibration, latency, or real-robot shift. Those failure channels need first-class reporting.",
            self_check="If a model-based method reaches target return with fewer episodes but twice the planner latency and worse shift robustness, would you still call it better? What additional evidence would you need?",
            memory_hook="Sample efficiency is the opening argument. Failure analysis is the cross-examination.",
            takeaway="Model-based RL often earns its place through data efficiency, but only a joint audit of efficiency, bias, uncertainty, and timing tells you whether the method is truly better.",
            exercise="Design an evidence card for a model-based benchmark in your domain. Which fields are mandatory before you would believe the sample-efficiency claim?",
            bibliography_cards=[
                bib_card('Chua, K. et al.. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." (2018).', 'https://arxiv.org/abs/1805.12114', 'A standard reference for strong sample efficiency under uncertainty-aware planning.'),
                bib_card('Janner, M. et al.. "When to Trust Your Model: Model-Based Policy Optimization." (2019).', 'https://arxiv.org/abs/1906.08253', 'A practical efficiency reference that also foregrounds model-trust limits.'),
                bib_card('Hansen, N. et al.. "TD-MPC2: Scalable, Robust World Models for Continuous Control." (2023).', 'https://arxiv.org/abs/2310.16828', 'A modern frontier baseline worth studying for both gains and remaining risks.'),
            ],
            prev_href="section-37.4.html",
            prev_text="Section 37.4: Imagination rollouts",
            next_href="../module-38-latent-world-models/index.html",
            next_text="Chapter 38: Latent World Models",
        ),
    }


def main() -> None:
    replace_main(MOD36 / "index.html", index_page_36())
    replace_main(MOD37 / "index.html", index_page_37())
    for path, content in build_sections().items():
        replace_main(path, content)


if __name__ == "__main__":
    main()
