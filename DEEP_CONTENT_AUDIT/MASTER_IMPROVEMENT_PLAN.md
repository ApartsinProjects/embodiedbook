# Master Improvement Plan - Building Embodied AI Deep Content Audit
## Date: 2026-06-22
## Scope: 60 chapters, 12 parts, ~379 sections

## Executive Summary

The book has a correct, current spine (it tracks the 2023-2026 shift to VLAs, GPU-parallel sim, diffusion/flow policies, generative world models, humanoids, and the LeRobot toolchain) and, where it is well authored, the per-section content is genuinely graduate-level: real equations with stated regimes of validity, runnable topic-specific code, named current systems, and precise open problems. The dominant book-wide defect is template residue: roughly 40 percent of sections are good content buried under (or, worse, replaced by) a generated scaffold that fails the BOOK_CONFIG non-substitutability rule (identical epigraphs, "What This Section Develops" / "Reader Pathway" headers, byte-identical tool tables, the `EvidenceRecord`/`SkillEvidence`/`SectionContract` toy-lab, and worked examples that slot the section title into a fixed sentence). The single most valuable action is a mechanical, scriptable de-scaffolding sweep that deletes the boilerplate and promotes the real "depth block" each section already contains. Beyond de-scaffolding, three clusters need substantive content (Part 2 is missing the field's core equations: the manipulator equation, the Kalman filter, twists, Jacobian/manipulability; Chapter 41 and several "syllabus" sections in Parts 9/12 are empty shells; landmark-paper citations are absent from section bodies across Parts 4, 10, and others). The structural skeleton needs only light surgery (about four merges, one rename, and a book-wide stale-index fix), not a redesign.

## Quality Distribution

| Part | Title | Excellent | Good | Needs Work | Poor | Overall |
|---|---|---|---|---|---|---|
| 1 | Foundations of Embodied AI | 7 | 9 | 8 | 0 | Mixed (Ch1 excellent, Ch2-3 scaffold) |
| 2 | Mathematical, Robotics, and Control Foundations | 0 | 4 | 12 | 20 | POOR (missing core equations) |
| 3 | Simulation, Tooling, and the Modern Stack | 7 | 22 | 3 | 0 | GOOD (Ch11-12 exemplary) |
| 4 | Reinforcement Learning for Embodied Agents | 2 | 35 | 0 | 0 | GOOD (strong content, heavy template) |
| 5 | Learning from Demonstration and Robot Data | 9 | 9 | 15 | 0 | Mixed (Ch23-24 exemplary) |
| 6 | Embodied Perception | 0 | 21 | 8 | 0 | GOOD (Ch29-30 strong) |
| 7 | Language, Vision, and Action | 7 | 29 | 0 | 1 | GOOD (Ch34-35 exemplary) |
| 8 | World Models and Model-Based Embodied AI | 8 | 18 | 4 | 2 | GOOD (Ch38 exemplary, Ch41 poor) |
| 9 | Manipulation, Locomotion, and Embodied Skills | 0 | 37 | 0 | 11 | Mixed (Ch42-46 good, Ch47-48 shells) |
| 10 | Multi-Agent and Human-Centered Embodiment | 0 | 16 | 0 | 0 | GOOD (real cores under boilerplate) |
| 11 | Evaluation, Safety, Robustness, and Deployment | 0 | 16 | 7 | 0 | GOOD (Ch54 exemplary) |
| 12 | Frontiers, Capstones, and Course Design | 0 | 8 | 24 | 0 | Mixed (Ch56-57 good, Ch58-60 shells) |
| **Total** | | **40** | **224** | **81** | **34** | |

Totals: 379 sections audited. Excellent 40 (11%), Good 224 (59%), Needs Work 81 (21%), Poor 34 (9%).

## TIER 1: CRITICAL FIXES (must fix before any other work)

### T1-1: Add the manipulator equation to Section 6.2
- **File**: `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.2.html`
- **Issue**: The section "Rigid-body dynamics; the manipulator equation" never states the equation. This is the single most important missing equation in the book.
- **Fix**: Add to the Theory block: the manipulator equation `M(q) q-ddot + C(q,q-dot) q-dot + g(q) = tau`, naming each term (mass matrix M, Coriolis/centrifugal C, gravity g), the structural properties (M symmetric positive-definite; `M-dot - 2C` skew-symmetric), and the regime of validity (rigid links, ideal actuators, no contact). Replace the `EmbodiedStep(...)` worked example with code that builds `M(q)` for a 2-link arm and verifies positive-definiteness via Cholesky. Frontier note: Featherstone articulated-body algorithm (O(n) forward dynamics, Pinocchio); open question on autodiff through ABA for trajectory optimization.
- **Impact**: A dynamics chapter for this audience that omits its title equation fails its core promise.

### T1-2: Add the Kalman filter to Section 8.6
- **File**: `part-2-.../module-08-sensors-perception-hardware-and-state-estimation/section-8.6.html`
- **Issue**: The flagship state-estimation section "Bayesian filtering: Kalman, EKF, particle filters" contains zero filter math, and its worked example is the irrelevant `points_camera = points_world - camera_offset` snippet (the clearest single non-substitutability failure in the book).
- **Fix**: Write the linear KF predict (`x-hat^- = A x-hat`, `P^- = A P A^T + Q`) and update (`K = P^- H^T (H P^- H^T + R)^-1`, state and covariance corrections), the EKF Jacobian linearization, and a particle-filter contrast for non-Gaussian/multimodal beliefs. Replace the snippet with a runnable 1D constant-velocity tracker that prints the shrinking covariance over steps.
- **Impact**: Second-most-serious omission in Part 2; everything downstream that assumes state estimation is unsupported.

### T1-3: Replace all banned filler worked examples in Part 2 (32 of 36 sections)
- **Files**: all of `module-05-*/section-5.*.html`, `module-06-*/section-6.*.html`, `module-07-*/section-7.*.html`, `module-08-*/section-8.*.html`
- **Issue**: Three banned patterns recur: `plan = [skill for skill in skills]` (Ch 5, 7), `EmbodiedStep("topic","act","observe consequence")` (Ch 6), and the identical `points_camera = points_world - camera_offset` (all of Ch 8) pasted regardless of topic.
- **Fix**: One runnable topic-specific example per section: 5.1 differentiate a frame to recover a twist; 5.3 integrate the differential-drive/bicycle model; 5.5 compute the 2-link FK already derived; 5.6 a damped-least-squares IK loop; 5.7 J + Yoshikawa manipulability; 6.4 explicit vs semi-implicit Euler on a spring (show divergence); 7.3 PID with anti-windup step response; 7.4 LQR via discrete Riccati; 8.2 disparity-to-depth; 8.5 noise sampling + covariance fit; 8.7 inverse-variance fusion.
- **Impact**: Restores the from-scratch-then-library payoff the lean contract demands across the most foundational part.

### T1-4: De-scaffold Chapter 3 (all 8 sections)
- **Files**: `part-1-foundations-of-embodied-ai/module-03-embodied-system-architectures/section-3.1.html` through `3.8.html`
- **Issue**: ~70% boilerplate per section, with literal title-substitution: "Formally, [TOPIC] should be placed inside the closed-loop transition o_t -> s_hat_t -> a_t -> o_{t+1}" and placeholder/elided "Worked Example" code.
- **Fix**: Keep only the epigraph, one real frame paragraph, the topic-specific Theory paragraph + equation/table, a real runnable worked example (drafts in the Part 1 report fix #3), the Fun Note, 2-4 topic-specific failure modes (mine the existing Failure Analysis tail), a cited Research Frontier, and one real exercise. Delete Reader Pathway, What This Section Develops, Action Is The Test, Mechanism, Self Check, Builder's Deep Dive, Practical Tool Choices For Section 3.X, Implementation Recipe, Teaching Move, and the evidence-schema code dicts. Promote the 3.7 model-interface table and the 3.8 failure-signature table to anchor their sections.
- **Impact**: Removes the sharpest quality cliff in the book (the Ch1->Ch2/3 boundary).

### T1-5: Rewrite Chapter 41 (all 5 sections) - Diffusion and Generative Planning
- **Files**: `part-8-.../module-41-diffusion-and-generative-planning/section-41.1.html` through `41.5.html`
- **Issue**: All five are template shells: generic epigraph naming the title, banned identical-cell tool table, `EvidenceRecord` toy-lab, duplicate Implementation Recipe / Failure Analysis Pattern, and (41.1) no diffusion math at all.
- **Fix**: Add real diffusion-planning math to 41.1: `tau_t = sqrt(alpha-bar_t) tau_0 + sqrt(1-alpha-bar_t) eps`, the learned reverse step, classifier-free guidance for return/goal conditioning, and why iterative denoising represents multiple viable trajectories where a unimodal regressor cannot. For 41.2-41.5, delete the scaffold and promote the existing topic-specific probes/equations/Memory Hooks (41.2 Diffuser loss + goal-vs-return scoring; 41.3 `S = lambda_r R - lambda_c C - lambda_d D - lambda_l L`; 41.4 mixture `L = E_real + alpha E_gen`; 41.5 support-mismatch audit).
- **Impact**: Converts the weakest chapter in a strong part to match the 40.1-40.3 standard.

### T1-6: Rewrite the 11 template-shell "syllabus" sections in Part 9 (Chapters 47, 48)
- **Files**: `module-47-drones-and-aerial-embodied-ai/section-47.1.html`-`47.5.html`; `module-48-autonomous-driving-as-embodied-ai/section-48.1.html`-`48.6.html`
- **Issue**: Section title mechanically slotted into fixed sentences; worked example is the banned `SkillEvidence` dataclass. The real content already exists in the appended deep sections (47.6-47.8, 48.7-48.9).
- **Fix**: Merge 47.2 (empty "Flight dynamics intuition") into 47.6 (real quadrotor model). Give 47.3/47.4/47.5 real VIO/coverage/failsafe content. For 48.1-48.6 add per-section equations (perception->prediction->planning chain; fusion covariance; minADE/minFDE; frenet/hybrid-A*; world-model loop; SOTIF safety case) and one runnable snippet each, cross-linking 48.4 to the real bicycle model in 48.7.
- **Impact**: Lifts Chapters 47-48 from NEEDS WORK to GOOD and removes 11 of the book's 34 POOR sections.

### T1-7: Rewrite Section 32.6 (the one POOR section in an otherwise excellent part)
- **File**: `part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.6.html`
- **Issue**: Fully generic template body with `points_world - camera_offset` code unrelated to "Limits of static VLMs in dynamic worlds".
- **Fix**: Formalize why an i.i.d.-trained VLM degrades under temporal correlation: static estimator `y-hat = f(I_t)` error decomposition when scene state is Markov but f ignores history, contrasted with a recurrent/memory-augmented estimator. Worked example: a moving object across 3 frames where per-frame CLIP top-1 flips while a memory-augmented score (reuse 32.5 freshness machinery) stays stable. Cite a current video-VLM / test-time-temporal-adaptation result. Alternatively fold into 32.5 and delete the shell.
- **Impact**: Removes the single POOR section dragging an EXCELLENT chapter.

### T1-8: Strip the boilerplate top half from all 29 sections of Chapters 58-60 (Part 12)
- **Files**: `part-12-frontiers-capstones-and-course-design/module-58-*/section-*.html`, `module-59-*/section-*.html`, `module-60-*/section-*.html`
- **Issue**: ~50% of each section is topic-agnostic boilerplate (SectionContract dataclass with truncated-string output, "What This Section Develops", closed-loop Theory paragraph, Practical Recipe, templated Research Frontier) followed by a good `Topic-Native Deepening` block.
- **Fix**: Keep epigraph + figure + one framing paragraph, delete the SectionContract print blocks (their output is truncated garbage like `'object_search_in_a_simulated_hom'`), and promote `Topic-Native Deepening` to the section body. In Chapter 60 also remove the topic-inappropriate closed-loop Theory paragraph and the "method-matched experiment / perturbation" Exercise (wrong for teaching topics).
- **Impact**: Moves 24 NEEDS WORK sections toward GOOD in one mechanical pass.

### T1-9: Delete the placeholder front matter in all 16 sections of Part 10 and promote the Technical Core
- **Files**: all `section-*.html` in `module-49-*`, `module-50-*`, `module-51-*`
- **Issue**: Every section wraps a genuinely strong "Technical Core" in placeholder "Theory"/"Mechanism" callouts, a filler `EmbodiedStep` worked example, an identical `EvidenceRecord` block, and an identical Technical-Core SVG that hardcodes "multi-agent and human-centered embodiment" for every section.
- **Fix**: Delete the placeholder Theory/Mechanism, the `EmbodiedStep` block, and the `EvidenceRecord` block; relabel the Technical Core "Formal Object" as the section Theory and the Technical-Core code fragment as the worked example (both already correct and topic-specific). Replace each section epigraph with that section's Memory Hook (all 16 are witty and already written).
- **Impact**: Converts "boilerplate wrapping real content" to "real content first" with near-zero new writing.

### T1-10: Fix the epigraph HTML bug in Sections 55.1-55.5
- **Files**: `part-11-.../module-55-deployment-architecture/section-55.1.html` through `section-55.5.html`
- **Issue**: A `<figure class="illustration">` is opened inside `<blockquote class="epigraph">`, so the illustration renders inside the epigraph and the `<cite>` is orphaned.
- **Fix**: Move the `<figure>` out of the `<blockquote>` (close the blockquote first). Mechanical, five files.
- **Impact**: Real rendering bug visible to every reader of the deployment chapter.

### T1-11: Replace the 37 identical section epigraphs in Part 4
- **Files**: every `section-*.html` in modules 14-20
- **Issue**: Every section opens with "[Section title] matters when the next action changes the evidence you thought you had." Swapping the title changes nothing.
- **Fix**: Per-topic epigraph each (drafts in the Part 4 report, e.g. 15.4 "A trust region is humility, formalized: change the policy, but not so fast you forget what worked."; 16.3 "Two critics, one pessimist: TD3 is the art of not believing your own best guess."). Keep the part-level line "An agent becomes interesting at the exact moment the world refuses to be a dataset." once, at the Part IV index only.
- **Impact**: Highest non-substitutability win by volume in the strongest-content part.

### T1-12: Fix the duplicated paragraphs and copy-paste defects across the book
- **Files**: `section-1.4.html` (duplicate Key Takeaway + Exercise 1.4.1); `module-28-*/section-28.1.html` and `section-28.5.html` (lines 49-50 each repeat a paragraph); `28.6`/`28.7` (verbatim shared Problem First/Key Insight); `section-53.1.html` and `section-53.4.html` ("Concrete stack anchors" paragraph twice); `section-59.12.html` (double body); Chapters 36-37 `code-output` mismatch bug in 8 sections.
- **Issue**: Literal copy-paste defects that read as bugs.
- **Fix**: Delete each duplicate; in Ch 36-37 rewrite the post-`code-output` paragraph to describe the actual probe shown (drafts per-section in the Part 8 report).
- **Impact**: Cheap, high-credibility fixes; these are the defects that most undermine reader trust.

### T1-13: Fix all stale part indexes (book-wide navigation correctness)
- **Files**: `part-3-*/index.html` (omits 10.6-10.7, 11.6-11.8, 12.6, 13.6); `part-6-*/index.html` (omits 29.8, 30.7); `part-7-*/index.html` + all module-3X indexes (advertise 5, ship 6-9: 31.6, 33.6-33.8, 34.6-34.9, 35.6-35.8); `part-8-*/index.html` (lists 32, 34 exist: add 38.6, 39.6, 39.7); `part-9-*/index.html` (omits Ch 42, 43 entirely and all deep sections 46.8-46.9, 47.6-47.8, 48.7-48.9); `part-12-*/index.html` (omits 58.99/58.6 and 60.6).
- **Issue**: Readers navigating from the part index miss up to a third of the content, including some of the best sections (33.8, 34.8, 35.7, 46.9).
- **Fix**: Regenerate each part-index chapter card and roadmap to match the files on disk. Renumber 58.99 to 58.6.
- **Impact**: Orphaned material is currently unreachable from navigation.

### T1-14: Inject missing landmark citations into section bodies (Parts 4, 10, and selectively elsewhere)
- **Files**: priority sections where the founding paper IS the section: 15.5 (Engstrom 2020 + CleanRL "37 details"), 17.1/17.2 (Rudin et al. 2021 "walk in minutes"; Makoviychuk Isaac Gym 2021), 17.5/20.3 (Lee 2020; Kumar RMA 2021; Miki 2022), 18.2 (Ng/Harada/Russell 1999), 18.3 (Andrychowicz HER 2017), 18.5 (Christiano 2017), 19.2 (Pathak ICM 2017; Burda RND 2018); plus de-template the recycled 5-card bibliographies in Parts 2, 4, 10.
- **Issue**: Every Part 4 section carries the same 5 recycled references with find-and-replaced annotations; the actual landmark papers appear in NO section body. Part 10 cites only pre-2022 work.
- **Fix**: Add a one-line "Paper Spotlight" callout per priority section with narrative context, and diversify the per-section bibliographies to the real source literature.
- **Impact**: For a research-scientist audience this is the single biggest content-credibility gap after the missing equations.

### T1-15: Replace placeholder/non-citations (SIMPLER and the "Official ... documentation" stubs)
- **Files**: `section-52.5.html` and `module-52-*/index.html` ("Official SIMPLER resources"); plus "Official ROS 2 documentation", "Official MLflow/DVC/ROS 2 logging documentation", etc. across Part 11.
- **Issue**: Bibliography stubs that are not real citations; SIMPLER is named in the chapter title yet not cited.
- **Fix**: Replace with Li, X. et al. "Evaluating Real-World Robot Manipulation Policies in Simulation" (SIMPLER), 2024, arXiv:2405.05941, with a one-line on its MMRV/variance metrics; resolve the other stubs to real sources. Name SPL (Anderson et al. 2018) in 52.2.
- **Impact**: Closes obvious credibility holes in the evaluation/deployment part.

## TIER 2: HIGH-VALUE IMPROVEMENTS

1. **De-scaffold Chapter 2 (all 8 sections)** - `part-1/module-02-*/section-2.*.html`. Same scaffold-deletion as T1-4, preserving Tier-A theory/code in 2.2/2.4/2.6/2.7 and all epigraphs/memorable shortcuts; delete the per-section Hands-On Labs in 2.3 and 2.7.
2. **Cut the boilerplate `production-depth-expansion` block from Chapter 9 sections 9.1-9.3** - `part-3/module-09-*/`. Delete the Builder's Deep Dive pair, the 5-row generic tool table, the placeholder `EvidenceRecord`, and the Failure Analysis Pattern; replace each with one topic-specific failure example (9.4/9.5 show the model).
3. **Add the missing options formalism to 26.2 and the CQL/IQL equations to 25.3** - `part-5/module-26-*/section-26.2.html`, `module-25-*/section-25.3.html`. 26.2 is titled "The options framework" but never states the (I, pi, beta) tuple or the SMDP backup; 25.3 has the intuition but not the CQL value-gap or IQL expectile loss.
4. **De-duplicate the byte-identical Big Picture paragraphs in Chapters 25 and 26** - all 5 sections each. Rewrite each opener section-specific; remove the identical SVG diagram from 4 of 5 sections per chapter.
5. **Strip Chapter 21 boilerplate shell; promote depth blocks** - `part-5/module-21-*/section-21.1.html`-`21.5.html`. Delete the glob-filler worked example, the repeated `EvidenceRecord`, Agent Checklist Integration, and the wrong-topic Gymnasium/PettingZoo tool table; keep the `course-depth-block`.
6. **Replace the identical Memory Hook in all 14 Chapter 27-28 sections** - `part-6/module-27-*`, `module-28-*`. Each currently repeats "For [topic], the perception result must answer what action changed...". Replace with section-specific hooks in the Ch 29-30 style.
7. **Unify Part 6 on the Chapter 29-30 template** - diversify the "Patient Embodied AI Agent" persona used for all 14 Ch 27-28 epigraphs; make the reused 5-box SVG contract figure topic-specific or demote it.
8. **Rewrite Section 40.4 (POOR) to GOOD** - `part-8/module-40-*/section-40.4.html`. Keep the `J(theta;phi)` theory, the frozen/adapter/fine-tune discussion, the sample-efficiency probe, and the Memory Hook (promote to epigraph); delete the identical-cell tool table, EvidenceRecord lab, and duplicate recipes.
9. **De-duplicate the repeated epigraph across Chapters 38 and 39 (13 sections)** - all use "The useful future is the one the controller can still steer." Give each a distinct topic-specific line.
10. **Replace the identical four-row checklist table in 19 of 23 Part 11 sections** - 52.1-52.6, 53.1-53.4, 54.1-54.7. Delete the Scenario panel/Runtime interface/Metric script/Review layer table; replace with section-specific content where it adds value.
11. **De-template Chapter 55 sections 55.2-55.5** - strip the shared Same-Artifact Rule, Mechanism, Practical Recipe, Builder's Deep Dive, Library Shortcut, fun-note, Self Check, What's Next; keep multirate-tails, placement-score, shadow/canary, recovery state-machine content. Replace the cloned evidence-contract SVG with topic-specific diagrams.
12. **Restore computational exercises in Part 4 Chapters 16-20** - replace the "design a schema/manifest/table" pattern with one "compute X with these numbers" exercise per section (e.g. the 4x4-grid Q-learning update for 16.1).
13. **Rewrite the 6 recycled "optimism is not an evaluation metric" fun-notes in Part 4** - 16.1, 16.4, 19.1, 20.2, 20.5 (keep the in-context original in 18.1). Topic-specific drafts in the Part 4 report.
14. **Replace the banned evidence-artifact toy labs (Chapters 27, 29, 30)** - `[{"section": s, ...} for s in sections]` filler. Model on Chapter 28's query-router lab: Ch 27 run a detector/SAM mask + back-project + clearance decision; Ch 29 a runnable MCL episode on a synthetic aliased map; Ch 30 A*-on-grid + DWA tracking with real path-cost/clearance/recovery numbers.
15. **Add real LeRobot/OpenVLA fine-tune code to 59.4** - `part-12/module-59-*/section-59.4.html`. The marquee hands-on capstone currently has only a manifest dict; add a compact runnable example (dataset load, LoRA config, train loop, eval call) and the missing hero figure.
16. **Replace the 6 duplicated epigraphs in Part 9** - 46.8, 46.9, 47.6, 47.7, 48.7, 48.8 all share "A robot earns trust one recovered disturbance at a time." Drafts in the Part 9 report (e.g. 47.6 "A quadrotor is four numbers arguing about six degrees of freedom.").
17. **Add the capture-point/ZMP equation to 45.2 and verify the OSC null-space hierarchy in 46.3** - `part-9/module-45-*/section-45.2.html`, `module-46-*/section-46.3.html`. Add `x_cap = x_com + x-dot_com sqrt(z/g)` with the LIP assumption; ensure 46.3 shows the prioritized null-space projection (or stacked QP), not a single task.
18. **Fix the asdict import bug in 11.4 and degenerate code in Part 11** - `section-11.4.html` (`asdict` used, not imported); 55.4 (coverage trivially 1.0), 55.3 (unexplained threshold 12), 53.2 (single-mean ECE not binned).
19. **Cut or shrink the identical ~120-line production-depth-expansion block in all 36 Part 2 sections** - move to one Part II appendix ("The Robotics Evidence Contract") referenced once instead of duplicated.
20. **Add the deadly-triad paragraph to 16.1 and the TRPO-to-PPO derivation sketch to 15.4** - close the only real depth gaps in Part 4's strongest chapters.

## TIER 3: POLISH AND ENRICHMENT

- **Preserve and redeploy existing fun elements** (full inventory below). Where a section's epigraph is a template clone but its Memory Hook is witty, swap the Memory Hook into the epigraph slot (Part 10 strategy: instant 16-for-16 upgrade).
- **Research frontier currency pass**: add dated 2024-2026 named results and one precise open problem to every generic "Research Frontier" callout. Highest need in Parts 2, 10 (cites only pre-2022), 27-28, and the thin frontier notes in 31.2/31.6.
- **Paper Spotlights**: add to 13.3 (OpenAI ADR "Solving Rubik's Cube with a Robot Hand"), 13.5 (Gaussian-splatting real2sim), 43.4 (dexterous in-hand RL sim-to-real with numbers), 46.4 (HumanPlus/HOVER).
- **Real-system anchors** for the Boston Dynamics / Waymo / frontier-lab audience: Spot fault modes, Waymo ODD, RT-2 eval numbers in Part 11 worked examples; Kiva/Amazon Robotics in 49.1; Diligent Moxi / Aethon TUG in 50.1; assistive teleoperation in 50.5.
- **Custom figure captions**: replace the generic "is easier to reason about when the figure shows the concept, evidence path, and action consequence" caption across Parts 3 (Ch 9,10,13), 6, 8 (40.4, all 41.x), 9 (47.1-47.5, 48.1-48.5), 12. Chapter 12's cartoon captions and 58.99/60.6 custom alt-text are the model.
- **Distinct illustrations**: generate unique figures for 38.6, 39.5, 39.6, 39.7 (currently all reuse illustration-05).
- **Add section-level "What's Next" bridges** where missing: all Ch 27-28 sections, Ch 31 (31.1-31.5 end on bibliography), Part 10 sections, the end of 24.5/25.4/25.5/26.5.
- **Analogy improvements**: add a coupling-sampling hook to 13.2; a digital-twin joke to 13.5; surface the 58.5 "90% short-episode success can be near-zero 20-minute reliability" as a fun-fact.

## Structural Recommendations (from Structural Architect)

Priority order:
1. **[HIGH] Deduplicate the lifelong/memory triple-overlap (Ch 51, 56, 57).** Catastrophic forgetting is a named section in both 51.4 and 57.2; memory/replay in both 51.5 and 56. Designate owners: Ch 56 owns memory, Ch 57 owns continual learning, Ch 51 becomes purely open-world.
2. **[HIGH] Rename Chapter 51** "Open-World and Lifelong Embodiment" -> "Open-World and Novelty-Robust Embodiment" (drop "Lifelong" so it no longer collides with Ch 57); fix its templated big-picture text to be about distribution shift, not teammates.
3. **[HIGH] Fix all stale part indexes** (see T1-13) - this is a navigation-correctness issue, not cosmetic.
4. **[MEDIUM] Merge Chapter 36 into Chapter 37** ("Learning Dynamics Models and Model-Based Control"); 36.4/36.5 duplicate 37.2/37.3. Part VIII is the most over-split part (6 chapters -> 4-5).
5. **[MEDIUM] Fold Chapter 40 (V-JEPA/JEPA) into Chapter 38** as a latent-world-model section pair; 40.1's "predict in latent space" thesis is 38.1's thesis.
6. **[MEDIUM] Confirm VQ-BeT and the action-representation decision guide are full sections in Chapter 22**; cross-ref the FAST tokenizer (Ch 34.5).
7. **[MEDIUM] Sharpen the Ch 53 / 54 / 55 boundary** so runtime monitoring is not re-derived three times (53 owns OOD/calibration as eval-time, 54 owns safety response, 55 owns deployment plumbing). Merge candidate: 54.6 + 54.7 (heavy overlap; 54.7 reads as a later add-on).
8. **[LOW] Tie the Part III/IV seam**: domain randomization (Ch 13) and sim-to-real RL (Ch 20) are one story split by a part boundary; make Ch 13 forward-reference Ch 20.
9. **[LOW] Reconcile 15.6 with Chapter 18** (reward shaping appears in both); retitle 15.6 "Reward shaping inside the PPO loop" with a forward-ref. Tighten SAC placement (16.3 title says SAC but 16.4 owns it).
10. **[LOW] Optionally split Chapter 33** into "LLM-Based Task Planning" and "LLM Agentic Control: Tools, Verification, Safety"; only if Part VII has room. Consider retitling Part IX to include "Application Domains" (47/48 are domains, not skills).

No wholesale re-architecture is warranted. The work is ~4 merges, 1 rename, 1 dedup cluster, and a book-wide index fix.

## Fun Elements Inventory (preserve through all edits)

- **Part 1**: 27 elements. Ch1 epigraphs all topic-specific (1.1 "A classifier answers a question once. An embodied agent answers, then inherits the consequences."); the warehouse-picking anecdote (1.1); all Ch2 epigraphs/memorable shortcuts (2.3 "Choosing an action space is how you tell a robot what kinds of mistakes it is allowed to make."); all 8 Ch3 Fun Notes (3.7 "An LLM can explain the plan, a VLM can point at the object, and a VLA is where the explanation has to survive contact with the gripper.").
- **Part 2**: 6 elements, concentrated in 4.1-4.3 (the lab-notebook, spreadsheet-headers, and Euler-angles fun-notes) + the Part II Memory Anchor. The Ch 5-8 templated fun-notes are NOT to be preserved.
- **Part 3**: 19 elements + 4 custom Ch12 figure captions (9.1 "If a simulated policy knocks over a virtual lamp... the lab also learns who ordered the replacement lamp."; 9.5 "A benchmark is a gym membership for one skill."; 11.6 "A thousand new mugs with the same friction are one physics example wearing many costumes.").
- **Part 4**: 29 elements (17.1 "Thousands of environments are a choir, not a crowd, if every reset sings the same note."; 18.4 "A reward hacker... reads the rules with the enthusiasm of a very literal lawyer."; 15.3 critic as "skeptical lab partner"). Keep the part epigraph once at part level.
- **Part 5**: 16 elements, mostly Ch 23-24 epigraphs (23.1 "A robot dataset is not a pile of videos. It is a memory of what the body was allowed to try."; 24.2 "The policy read the video. The researcher read the license.").
- **Part 6**: 13 elements, almost all in Ch 29-30 (persona "A Loop Closure That Came Back With Receipts"; 30.7 "A planner that ignores dynamics is a cartographer with excellent handwriting and no driver license."; 28.5 caption "A beautiful render is not a collision certificate.").
- **Part 7**: 21 elements (31.5 "Humans call it a clarifying question. Robots call it avoiding a future apology tour."; 34.3 gripper-convention-inverted aha; 35.4 "A giant average score is a trench coat.").
- **Part 8**: 28 elements (36.4 "A forecast without uncertainty is just a confident guess with better typography."; 40.1 "Do not ask me to repaint every pixel; ask me whether the mug will still be there when the gripper closes."; 41.5 "very confident intern").
- **Part 9**: 38 elements (46.3 "Operational space is the wish. Whole-body control is the bill."; 45.3 "Parallel RL is a microscope and a funhouse mirror at the same time."; plus the witty self-checks).
- **Part 10**: 16 Memory Hooks, all topic-specific and witty - the standout engagement asset (49.4 "A team reward can be a beautiful hiding place for one very lazy policy."; 51.1 "A closed-world benchmark is a tidy kitchen; deployment is the drawer where somebody put batteries, tape, and one mysterious screw."). Promote each into its section's epigraph slot.
- **Part 11**: 11 elements (52.1 "A robot can classify the scene perfectly and still drive into the wrong next action."; 54.4 "A shield earns trust when every blocked action leaves an auditable trace."). The part is fun-poor; flag for enrichment.
- **Part 12**: 19 epigraphs (58.4 "My weights are open, my data is vague, and my license has entered the group chat."; 57.2 "I mastered the new drawer and now salute every chair like a handle."). The 58-60 fun-notes are templated and NOT to be preserved.

Total genuine fun elements to preserve: approximately 243 (sum of per-part counts, excluding the templated ones explicitly flagged).

## Cross-Cutting Patterns (scriptable systemic fixes)

These appear across many sections and could be addressed with find/replace or generated-template removal scripts:

1. **The slotted-title epigraph** "[Title] matters when the next action changes the evidence you thought you had" (attributed "A Careful Control Loop") - Parts 3, 4, 5, 7, 8, 10, 12. Scriptable: detect and replace with per-section line or the section's existing Memory Hook.
2. **The closed-loop Theory boilerplate** "Formally, [TOPIC] should be placed inside the closed-loop transition o_t -> s_hat_t -> a_t -> o_{t+1}" - Parts 1 (Ch3), 2 (Ch5/6/8), 7 (32.6), 8 (40.4, 41.x), 10, 12 (58-60). Scriptable detection.
3. **The "What This Section Develops" / "Reader Pathway" / "Action Is The Test" headers** - Parts 1, 4, 8, 9, 12. Banned by the lean contract; delete on sight.
4. **The identical-cell tool table** (Gymnasium/PettingZoo/ROS 2/MuJoCo/LeRobot, or `SkillEvidence`/`EvidenceRecord`/`SectionContract` rows with repeated text) - Parts 2, 3 (Ch9), 5 (Ch21), 8 (40.4, 41), 9 (47-48), 10, 11, 12. Delete; replace with at most one sentence naming the one relevant tool.
5. **The evidence-artifact toy lab** (`[skill for skill in skills]`, `EmbodiedStep(...)`, `[{...} for s in sections]`) - Parts 2, 6 (Ch27/29/30 labs), 8, 9, 10, 12. Banned worked-example pattern; replace with one runnable topic-specific example.
6. **The four-row "Implementation Checklist" table** - 19 of 23 Part 11 sections. Delete.
7. **Recycled illustration/SVG assets** - the 5-box contract figure (Part 6 Ch27-28), the four-box closed-loop SVG (all 37 Part 7 sections), illustration-05 (Part 8), the hardcoded Technical-Core SVG (Part 10). Make topic-specific or demote to chapter-index level.
8. **Generic figure captions** - the "is easier to reason about when the figure shows the concept, evidence path, and action consequence" caption book-wide.

## Missing 2024-2026 Content (verify present or add)

- **Core robotics equations entirely missing** (not a currency issue, a correctness gap): manipulator equation (6.2), Kalman/EKF/particle filter (8.6), twists + adjoint (5.1), Jacobian/singularity/manipulability (5.7), friction cone/complementarity (6.3), integrators + stability bound (6.4), differentiable-sim gradient (6.5), GPU-parallel architecture (6.6), DH/PoE chain (5.4), non-holonomic constraint (5.2), inverse-variance fusion (8.7).
- **Landmark RL/robotics papers absent from bodies**: DQN, TD3, SAC, PPO/CleanRL details, GAE, Rudin parallel-RL, RMA, HER, Christiano preferences, Ng potential shaping, ICM/RND, CPO/Safety Gym (Part 4); options framework Sutton-Precup-Singh (26.2); CQL/IQL (25.3).
- **FAST action tokenizer**: present in 34.5; confirm cross-ref in the Ch 22 action-representation decision guide.
- **Newton physics engine, Genesis**: present in Ch 11 (verify Genesis renderer name "Nyx" vs historical "LuisaRender").
- **SmolVLA, RDT-1B, pi-0.5, GR00T N1.5, Gemini Robotics 1.5, Helix**: present and current in Ch 34/35 with Frontier-Watch caveats (the house model for vendor-system handling).
- **Genie 3, Cosmos 2026/Cosmos 3, V-JEPA 2, Dreamer 4, TD-MPC2**: present and current in Part 8.
- **Neural/Gaussian-splat SLAM** (SplaTAM, MonoGS, GS-SLAM): under-cited in 28.5/29.6; add.
- **Metric monocular depth** (Depth Anything v2, UniDepth, Metric3D): under-cited in 27.3 and 8.2.
- **VLN / image-goal navigation** current work: thin in 30.6.
- **System-1/System-2 fast-local/slow-cloud serving** (Helix, pi-0): name explicitly in 55.3.
- **Genuinely under-covered**: sim-to-real for manipulation specifically; latency/async inference for VLA serving (1-10 Hz constraints); data filtering/quality at scale for cross-embodiment pools (24.5 should be rigorous).

## Recommended Execution Order

**Phase A - Mechanical de-scaffolding sweep (scriptable, highest ROI, do first).** Run the cross-cutting pattern removals (T1-8, T1-9, T1-11, and cross-cutting items 1-8) across Parts 4, 7, 10, 12 and Chapters 2, 3, 9, 21, 25, 26, 27-28, 40.4, 41. Promote each section's existing depth block / Technical Core to the body and swap Memory Hooks into epigraph slots. This converts the largest count of NEEDS WORK sections to GOOD with near-zero new writing.

**Phase B - Copy-paste and HTML bug cleanup (cheap, high-credibility).** T1-10 (55.x epigraph), T1-12 (all duplicated paragraphs + Ch36-37 code-output mismatch), T1-13 (stale indexes), the asdict bug, the degenerate code (55.3/55.4/53.2). These are bugs that read as unprofessional and are fast to fix.

**Phase C - Substantive content for the empty/shell sections.** T1-1, T1-2, T1-3 (Part 2 core equations and runnable code - the biggest correctness gap), T1-5 (Ch 41 diffusion math), T1-6 (Part 9 Ch 47-48 rewrites), T1-7 (32.6). This is the real writing work.

**Phase D - Citations and currency.** T1-14 (landmark Paper Spotlights, de-template bibliographies), T1-15 (placeholder-citation fixes), and the Tier 3 research-frontier currency pass.

**Phase E - Structural surgery.** The lifelong/memory dedup + Ch 51 rename, the Part VIII merges (36+37, 40 into 38), and the 54.6+54.7 merge. Do this last so it operates on already-cleaned sections.

**Phase F - Enrichment and polish.** Custom figure captions, distinct illustrations, real-system anchors, What's Next bridges, analogy additions.

## Section Quality Heatmap (by chapter)

| Chapter | Quality | Note |
|---|---|---|
| 1 Static->Embodied | EXCELLENT | House-style model for the book |
| 2 Agent-Environment Interface | NEEDS WORK | Strong cores under scaffold |
| 3 System Architectures | POOR | ~70% boilerplate, title-substitution |
| 4 Spatial Frames | GOOD (4.4-4.7) / NEEDS WORK (4.1-4.3) | Promote 4.4-4.7 as Part 2 template |
| 5 Kinematics | POOR | Missing twists, FK code, Jacobian |
| 6 Dynamics | POOR | Missing manipulator equation, contact, integrators |
| 7 Control | NEEDS WORK | Good theory/callouts, filler code |
| 8 Sensors/Estimation | POOR | Missing Kalman filter, all code irrelevant |
| 9 Why Simulation | NEEDS WORK (9.1-9.3) / GOOD (9.4-9.5) | Cut production-block |
| 10 Gymnasium/PettingZoo | GOOD | Strong runnable code |
| 11 Physics Simulators | EXCELLENT | Book-wide template model |
| 12 Benchmarks | GOOD | Current facts, custom captions |
| 13 Domain Randomization | GOOD | Add ADR/real2sim spotlights |
| 14 RL Refresher | GOOD | Cleanest Part 4 chapter |
| 15 Policy Gradients/PPO | EXCELLENT (content) | Add TRPO->PPO sketch |
| 16 Value-Based/Off-Policy | GOOD / NEEDS WORK (engagement) | Recycled fun-notes |
| 17 GPU RL | GOOD | Best fun-notes; missing founding cites |
| 18 Reward Design | GOOD | Richest Part 4 chapter |
| 19 Exploration | GOOD / NEEDS WORK (template drift) | Thin chapter |
| 20 Sim-to-Real (RL) | GOOD | Add DR/RMA cites |
| 21 Imitation Learning | NEEDS WORK | Heaviest Part 5 boilerplate |
| 22 Action Chunking/Diffusion | GOOD | Richest Part 5 content |
| 23 Teleoperation/Data | EXCELLENT | Part 5 template model |
| 24 Datasets/Scaling | EXCELLENT | Current dataset coverage |
| 25 Offline RL | NEEDS WORK | Identical Big Picture x5 |
| 26 Skills/Hierarchy | NEEDS WORK | Identical Big Picture x5; missing options formalism |
| 27 Visual Perception | NEEDS WORK | Identical Memory Hook x7 |
| 28 3D/Neural Scenes | NEEDS WORK | Duplicated paragraphs; best lab |
| 29 SLAM | GOOD | Strongest Part 6 chapter |
| 30 Navigation/Planning | GOOD | Misapplied Big Picture in 30.5 |
| 31 Language-Guided | GOOD | Add 31.6 to index |
| 32 VLMs | GOOD / POOR (32.6) | 32.6 is the part's one POOR section |
| 33 LLMs as Planners | GOOD | 33.6-33.8 strong but orphaned |
| 34 VLA Models | EXCELLENT | Best chapter in Part 7 |
| 35 Robot Foundation Models | EXCELLENT | Frontier-Watch is the house model |
| 36 Predicting the Future | GOOD | code-output bug; merge candidate |
| 37 Model-Based RL/MPC | GOOD | code-output bug; merge target |
| 38 Latent World Models | EXCELLENT | Part 8 template model |
| 39 Generative/Video Worlds | GOOD | Repeated epigraph; asset reuse |
| 40 Predictive Representations | EXCELLENT (40.1-40.3) / POOR (40.4) | |
| 41 Diffusion Planning | POOR | Template shells; needs diffusion math |
| 42 Manipulation | GOOD | |
| 43 Grasping/Dexterity | GOOD | |
| 44 Tactile Learning | GOOD | |
| 45 Locomotion | GOOD | Strongest frontier writing in Part 9 |
| 46 Humanoids/WBC | GOOD | 46.8-46.9 orphaned |
| 47 Drones | POOR (47.1-47.5) / GOOD (47.6-47.8) | Template syllabus sections |
| 48 Autonomous Driving | POOR (48.1-48.6) / GOOD (48.7-48.9) | Template syllabus sections |
| 49 Multi-Agent | GOOD | Real cores under boilerplate |
| 50 HRI | GOOD | Strongest Part 10 cores |
| 51 Open-World/Lifelong | GOOD | Rename + dedup with 56/57 |
| 52 Evaluating Systems | NEEDS WORK | Cloned framing, name SPL |
| 53 Robustness/Uncertainty | GOOD | Duplicate paragraphs |
| 54 Safety | GOOD | Best chapter in Part 11 |
| 55 Deployment | NEEDS WORK | Epigraph HTML bug; cloned 55.2-55.5 |
| 56 Memory | GOOD | Duplicate callouts |
| 57 Continual Learning | GOOD | Strongest chapter in Part 12 |
| 58 Frontier/Open Problems | NEEDS WORK | Two-tier template |
| 59 Capstones | NEEDS WORK | Briefs buried; 59.4 needs real code |
| 60 Teaching | NEEDS WORK | Boilerplate most incongruous here |
