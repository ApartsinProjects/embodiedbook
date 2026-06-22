# Part 11 Content Audit: Evaluation, Safety, Robustness, and Deployment

## Part Overview

Part 11 covers exactly the right material for a Boston Dynamics / embodied-AI-research audience (closed-loop evaluation, calibration and OOD, CBF/HJ reachability, shields, assurance cases, real-time deployment), and the safety chapter (54) is genuinely strong: real CMDP, CBF, and GSN content with current standards (UL 4600, ISO 21448 SOTIF, UNECE R157). The fatal weakness is template saturation: across all four chapters the sections are built from a shared boilerplate, and one block in particular, the four-row "Implementation Checklist" table (Scenario panel / Runtime interface / Metric script / Review layer), is byte-for-byte identical in 19 of 23 sections. Chapters 52 and 55 suffer most: their "Why This Matters" paragraphs, "Reader Pathway" callouts, epigraphs, "Same-Artifact Rule", "Practical Recipe", and "fun-note" are copy-pasted with only the section title swapped in, which is the exact non-substitutability failure the contract forbids. The result is a part with solid bones and real equations but a body that reads as 23 instances of one shell rather than 23 distinct lessons. There is also a real HTML bug: in sections 55.1-55.5 a `<figure>` is nested inside the `<blockquote class="epigraph">`, breaking the epigraph.

## Fun Elements to Preserve

The part is fun-poor. Catalog of what exists:

- **Ch 52 epigraph** (index): "A robot benchmark is only serious when it can disappoint your favorite model in a way you can replay." (Strong, witty, keep.)
- **Section 52.1 epigraph**: "A robot can classify the scene perfectly and still drive into the wrong next action." (Good, topic-specific, keep.)
- **Ch 53 epigraph** (53.1-53.4, reused): "A robust robot is not the one that never sees surprise, it is the one that notices surprise early enough to act differently." (Good aphorism; keep, but it is reused verbatim across all 4 sections, so vary the per-section epigraphs.)
- **Section 54.1 epigraph**: "Safety begins by naming the physical harm path, not by lowering a benchmark score." (Sharp, keep.)
- **Section 54.4 epigraph**: "A shield earns trust when every blocked action leaves an auditable trace." (Keep.)
- **Section 54.5 epigraph**: "An override is complete only when the robot reaches a verified safe state." (Keep.)
- **Section 54.6 epigraph**: "Approval is evidence traceability, not confidence performed in prose." (Keep.)
- **Section 54.7 epigraph**: "An assurance case is strong when its leaves are logs, tests, and replayable artifacts." (Keep.)
- **Section 55.x "fun-note" callouts** titled "A Useful Annoyance" (55.1-55.5): "schema strictness is cheaper than discovering a missing field during a moving-robot trial." This is the SAME text in all five sections; it is a fun-note in name only. Keep the device, rewrite four of the five to be section-specific or it is boilerplate.
- **Section 55.6 fun-note "Memory Hook"**: "makes [topic] visible twice: once in the design sketch and once in the replay artifact. The second view keeps the first one honest." (The one genuinely fresh fun-note in Ch 55; keep.)

No surprising facts, counterintuitive results, analogies to real systems by name, or "aha" moments are present. This is the single biggest engagement gap in the part.

## Chapter-by-Chapter Analysis

### Chapter 52: Evaluating Embodied Systems
**Quality**: NEEDS WORK

The conceptual spine (closed-loop utility, vector metrics, constraint satisfaction, CVaR tails, sim-as-proxy, benchmark hygiene) is correct and well-sequenced. But 52.2-52.6 are near-clones: identical "Reader Pathway" ("name the aggregation unit, the rollout panel that produced it, and the failure modes..."), identical epigraph ("a benchmark conclusion survives reruns only when the panel, seed policy, exclusion rules..."), identical "Why This Matters" first sentence ("matters because evaluation choices rewrite the scientific claim. If the metric drops time, energy, or safety terms..."), and the identical four-row checklist table in every section. Code examples are toy dict/list snippets, not runnable against any named simulator.

#### Section 52.1: Why accuracy is not enough - GOOD
**Lens 1 (Deep Explanation)**: Strong. The utility model $J = \mathbb{E}[\mathbb{1}\{\text{success}\} - \lambda_v V - \lambda_t T - \lambda_e E - \lambda_r R]$ is motivated, and the two-figure setup (loop diagram + dashboard) builds intuition. Four-question test passes. Minor: $\lambda$ weights are asserted (4.0, 0.02, ...) with no guidance on how to set them; add one sentence on normalizing weights to a common utility scale.
- Fix: After the code, add "These weights are not free parameters to tune for a flattering number: fix them once from the deployment cost model (dollars per second, joules per task, cost of one human rescue) before any policy is compared."

**Lens 2 (Research Frontier)**: PASS but thin. The "Research Frontier" callout is generic ("benchmarks increasingly log videos..."). 
- Fix: Name a current artifact: "RoboArena (2025) and the Open X-Embodiment evaluation suite push toward logged-rollout comparison; the open problem is aggregating video + monitor traces across labs without a shared schema."

**Lens 3 (Fun/Engagement)**: Has the best epigraph in the chapter and a real worked contrast (88%->93% grasp accuracy that LOSES on utility). That 0.49 vs -0.34 sign flip is the chapter's one genuine "aha". Preserve it.

**Lens 4 (Examples/Analogies)**: Good warehouse mobile-manipulator example. No named real system though; could cite RT-1/RT-2 real-robot eval numbers.

**Lens 5 (Teaching Flow)**: Strong; this is the one section in Ch 52 that does NOT use the cloned template. Keep it as the model the others should be rewritten toward.

#### Section 52.2: Success rate, path efficiency, time and energy cost - NEEDS WORK
**Lens 1**: The score vector $m_i = [s_i, \rho_i, t_i, e_i]$ with $\rho_i = d^*_i/d_i$ (this is exactly SPL, Success weighted by Path Length, from Anderson et al. 2018) is correct but the section never names SPL. That is a missing connection a navigation researcher will immediately notice.
- Fix: "Path efficiency $\rho_i = d^*_i/d_i$ weighted by success is the SPL metric (Anderson et al., 2018, 'On Evaluation of Embodied Navigation Agents'), the de facto standard for PointNav and ObjectNav. SPL hides exactly the time and energy terms this section adds back."

**Lens 2**: "Pareto-front reporting and scenario-conditioned scorecards" is a reasonable frontier note but uncited. Add Habitat/iGibson leaderboard practice.

**Lens 3**: Quadruped oscillation-in-narrow-passages example is concrete and good. No humor; the "30% more turning, 18% more battery" detail is the memorable hook, keep it.

**Lens 4**: PASS. Driving (jerk/delay) and drone (trajectory deviation) transfers are appropriate.

**Lens 5**: Template "Reader Pathway" and "Why This Matters" are clones of 52.3-52.6. Cut the cloned framing; the section's own content is fine.

#### Section 52.3: Safety violations and constraint satisfaction - GOOD
**Lens 1**: Strong. $C = 1 - \frac{1}{N}\sum \mathbb{1}\{\exists t: g(x,u)<0\}$ is correct and the hard/soft distinction (log magnitude + duration) is the right depth. Passes four-question test.

**Lens 2**: "combining learned uncertainty with formal constraints, calibrating near-boundary warnings" is a real frontier; good.

**Lens 3**: The 95%-success-but-8%-torque-violation manipulator and the "minor workspace excursion vs force spike on a human-contact surface" distinction are the memorable content. Keep.

**Lens 4**: PASS. Delivery-robot constraints (pedestrian clearance, cornering speed, stop-distance) are concrete.

**Lens 5**: Good forward link to 54.2/54.3 (measurement -> enforcement). Cloned epigraph and checklist table remain the only flaw.

#### Section 52.4: Robustness and generalization metrics - GOOD
**Lens 1**: Strong. CVaR$_\alpha(L) = \mathbb{E}[L | L \ge q_\alpha]$ is correct, and the three-faces decomposition (interpolation / nuisance robustness / OOD) is graduate-depth. The code computes CVaR correctly (threshold_index, tail mean).
- Minor: the code uses `int(alpha*len(losses))` indexing which is a crude quantile; note it is approximate.

**Lens 2**: "compositional shift panels, versioned perturbation generators" is current and good.

**Lens 3**: Drone gust example with "worst decile" is the hook. Humanoid friction-drop tail example is good.

**Lens 4**: PASS.

**Lens 5**: PASS. Good bridge to 53.1/53.3.

#### Section 52.5: Reproducible evaluation: SIMPLER and sim-as-proxy - GOOD
**Lens 1**: Strong and topic-specific. Fidelity gap $\Delta = |\mathbb{E}[S]-\mathbb{E}[R]|$ PLUS rank correlation is exactly the right framing, and the worked example shows rank inversion (sim says A>B, real says B>A) while mean gap looks fine. This is the chapter's second genuine "aha".

**Lens 2**: SIMPLER is named but the bibliography entry is a placeholder ("Official SIMPLER resources") not a real citation. SIMPLER is Li et al., 2024, "Evaluating Real-World Robot Manipulation Policies in Simulation" (arXiv:2405.05941). 
- Fix: Replace the placeholder bib entry with the actual SIMPLER paper and a one-line on its MMRV / variance metrics.

**Lens 3**: CARLA-for-regression-but-not-sensor-contamination and MuJoCo/Isaac screening examples are concrete and current.

**Lens 4**: PASS. Tabletop-grasp-transfers-but-insertion-does-not is a precise, true example.

**Lens 5**: PASS.

#### Section 52.6: Real-world evaluation hygiene; benchmark design - GOOD
**Lens 1**: Paired-difference estimator $\bar d = \frac1N\sum(y_i^A - y_i^B)$ with bootstrap CI is correct; the "lab schedule confound" framing (camera calibrated early vs lens smudge + battery sag) is excellent and concrete.

**Lens 2**: "audit logs for physical tests, standardized rerun policies" is reasonable but uncited. Could cite the rliable framework (Agarwal 2021, already in refs) for the stats half.

**Lens 3**: The "measuring the lab schedule as much as the policy" line is the memorable hook. Keep.

**Lens 4**: PASS. Drone-block-by-battery/wind and humanoid-block-by-floor/reset-crew are good.

**Lens 5**: Good chapter-closing forward link to Ch 53. Only the cloned blocks weaken it.

### Chapter 53: Robustness and Uncertainty
**Quality**: GOOD

The strongest-balanced chapter conceptually: disturbance taxonomy -> calibration (ECE) -> OOD -> runtime monitor state machine is a clean, correct arc, and 53.2/53.3 actually break the boilerplate with section-specific tool tables (Torchmetrics/scikit-learn/MAPIE; distance/energy/conformal). The reused epigraph across all four sections and the shared "Reader Pathway" and checklist table are the drag.

#### Section 53.1: What goes wrong: sensor noise, distribution shift - GOOD
**Lens 1**: Strong. Decomposition $y_t = h(x_t) + \epsilon_t$ with $x_t \sim p_{train}$ or $p_{deploy}$ cleanly separates observation corruption from distribution shift, and the key insight ("you do not fix missing depth frames with more policy regularization") is exactly the right intuition.

**Lens 2**: "richer perturbation ontologies and automatically generated stress suites" is reasonable; could name RoboDepth / common-corruptions benchmarks.

**Lens 3**: The depth-dropout (13.9 cm state error) vs motion-blur (4.2 cm) contrast showing "same task failure, different internal signature" is a real teaching hook. Rain-vs-route-closure and wind-vs-glare distinctions are good.

**Lens 4**: PASS.

**Lens 5**: PASS. Note: the "Concrete stack anchors for this chapter" paragraph appears TWICE in this section (in Library Shortcut AND verbatim in Builder's Deep Dive). Delete the duplicate.

#### Section 53.2: Model uncertainty and calibration - GOOD
**Lens 1**: Strong. ECE $= \sum_b \frac{|S_b|}{n}|\text{acc}(S_b)-\text{conf}(S_b)|$ is correct, and the "right ordering, wrong scale" insight plus the warning that the mean gap can hide local miscalibration via cancellation is graduate-depth and honest.
- Minor: the code computes a single mean-gap "ece_like_gap" not real binned ECE; the caption admits this, good. Could add a true 2-bin version.

**Lens 2**: "sequence-level calibration, calibration for action distributions" is a genuine current frontier. Good. Add temperature scaling vs conformal as the named methods (Guo 2017 is cited).

**Lens 3**: The 0.95-confidence-but-0.70-success grasp example is the hook. Self-driving occupancy-vs-semantic-class point is sharp.

**Lens 4**: PASS. Has a real section-specific tool table (Torchmetrics / scikit-learn / MAPIE) with audit questions: this is the model for what every section should have instead of the cloned checklist.

**Lens 5**: PASS.

#### Section 53.3: Out-of-distribution detection - GOOD
**Lens 1**: Correct. Threshold rule $s(x) > \tau$ tied to action-cost tradeoff, with the key reframe that OOD detection is only useful if it changes behavior (slow/replan/switch-sensor/handoff). Good depth.

**Lens 2**: Strong and current: "sequential OOD detection, active information gathering after novelty alerts, joint perception+dynamics+map novelty." Cites Hendrycks 2017 and Liu 2020 (energy) correctly.

**Lens 3**: Reflective-floor-patch -> lower-speed-mode is concrete. AUROC-without-operational-cost critique is the memorable point.

**Lens 4**: PASS. Section-specific OOD tool table (distance/energy/conformal) is good.

**Lens 5**: PASS.

#### Section 53.4: Runtime monitoring and fail-safe behavior - GOOD
**Lens 1**: Strong. Health state machine $z_{t+1} = M(z_t, h_t)$ over {normal, degraded, stopped, recovery} with the insight "logging an alarm after a bad action is observability, not fail-safe control." The code is a real, runnable threshold state machine (the most useful code in Ch 53).

**Lens 2**: "learned runtime assurance, fusion of heterogeneous health signals, monitors that actively seek information" is a real frontier. Cites Amodei 2016 (a bit dated as the only ML-safety ref).
- Fix: Add a 2023-2025 runtime-monitoring reference (e.g., runtime monitoring for learned perception, or the "RTA / Simplex architecture" lineage).

**Lens 3**: Drone-stale-localization -> hover/land is concrete. "degraded is just a label" critique is sharp.

**Lens 4**: PASS. Note the "Concrete stack anchors" paragraph is duplicated here too (Library Shortcut + Builder's Deep Dive). Delete duplicate.

**Lens 5**: Excellent hand-off to Ch 54.

### Chapter 54: Safety in Embodied AI
**Quality**: GOOD (best chapter in the part)

This chapter carries Part 11. It has real safety-engineering depth: hazard ranking ($r = S \times E \times C$), CMDP, CBF inequality, HJ reachability, projection safety filter, MTTI, GSN-style assurance template $\mathcal A = (G,C,E,D,R)$, and current standards (UL 4600, ISO 21448, UNECE R157, NHTSA, FAA). 54.3, 54.6, 54.7 have extra section-specific tables and procedures that break the template. Still carries the cloned "Why This Matters" sentence ("sits at the boundary between learning and safety engineering...") in all 7 sections and the cloned checklist table.

#### Section 54.1: Why embodied safety is different (physical harm) - GOOD
**Lens 1**: Strong. $r = S \times E \times C$ hazard surrogate, explicitly flagged as NOT a replacement for STPA/formal verification (good honesty about regime of validity). Four-question test passes.

**Lens 2**: PASS. UL 4600 (Koopman) cited well. Could add STPA (Leveson) as a named method since it is mentioned.

**Lens 3**: "hurry through a corridor" service robot becoming unsafe while staying task-optimal is the hook. blocked_exit (36) outranking pinch (20) is a small "aha".

**Lens 4**: PASS. Warehouse blind-corner-collision example concrete.

**Lens 5**: Strong opener for the chapter. Cloned "Why This Matters" sentence is the only flaw.

#### Section 54.2: Constraint violations and safe exploration - GOOD
**Lens 1**: Strong. CMDP $\max_\pi J_R$ s.t. $J_{C_k}(\pi) \le d_k$ is the correct formal object, and the "violations are evidence to analyze, not acceptable tuition fees" framing is excellent. Insistence on logging BLOCKED attempts (not just realized violations) is a real practitioner insight.

**Lens 2**: Strong and current. García & Fernández 2015 survey + Wabersich 2023 probabilistic shields. Frontier ("scalable constrained RL for contact-rich tasks, online safe-set expansion") is precise.

**Lens 3**: Mobile-manipulator "should not ram a shelf just because reward eventually penalizes contact" is memorable. Drone geofence / humanoid fall-risk transfers good.

**Lens 4**: PASS. Could name a constrained-RL library (e.g., omnisafe, safety-gymnasium) rather than generic "constrained RL libraries."

**Lens 5**: PASS.

#### Section 54.3: Control barrier functions and Hamilton-Jacobi reachability - GOOD (strongest single section)
**Lens 1**: Strongest math in the part. Control-affine $\dot x = f(x)+g(x)u$, CBF condition $\nabla h^\top(f+gu) + \alpha(h) \ge 0$, plus HJ value-function framing, all correct. The 1D worked example projects nominal speed onto the admissible value, which is a genuine (if simplified) barrier correction.
- Minor: the 1D code conflates a velocity command with $\dot h$; a one-line note that this is a scalar single-integrator illustration would prevent a controls reader from over-reading it.

**Lens 2**: Strong. Ames 2017 (CBF-QP) and Fisac 2019 (HJ) are the canonical refs and correctly used. Frontier ("uncertainty-aware, learned-dynamics, multi-agent barriers") is current.

**Lens 3**: "nominal intelligence must yield to explicit safety geometry" is the memorable line. The "Formal Safety Tool Anchors" table with a "Failure To Watch" column (deployed controller solves different optimization than notebook) is genuinely useful and breaks the template.

**Lens 4**: PASS. Real tools named (cvxpy, OSQP, CasADi, Drake, python-control, hj_reachability). Driving headway / drone altitude / manipulator force transfers good.

**Lens 5**: PASS. The reduced-model-assumption warning ("proof depends on the deployed interface, not the math on paper") is the right caution.

#### Section 54.4: Shielded policies and safety filters - GOOD
**Lens 1**: Strong. Minimal-intervention filter $u^{safe} = \arg\min_{u \in \mathcal U_{safe}} \|u - u^{nom}\|^2$ is the standard safety-filter QP, correct. The "veto distribution tells you where the policy is misaligned" insight (shield produces a dataset, not just a block) is a real second-order point.

**Lens 2**: Alshiekh 2018 (shielding) + Wabersich 2023 are the right refs. Frontier (probabilistic shields, learned safe sets, intent-uncertainty filters) current.

**Lens 3**: Language-conditioned mobile manipulator reaching through a crowd, and the unit-mismatch/stale-transform "filter appears active but lets unsafe commands through" failure mode are both memorable and true.

**Lens 4**: PASS. Code is a runnable clip-projection shield with intervention flag.

**Lens 5**: PASS.

#### Section 54.5: Human override and safety testing - GOOD
**Lens 1**: Strong and underrated topic. MTTI $= \frac1N\sum(t^{override}_i - t^{hazard}_i)$ plus success-after-override, and the crucial distinction between override-command-accepted vs achieved-safe-state (coasting/swinging/drifting). The code separates override_delay from safe_state_delay, which is the whole point.

**Lens 2**: NHTSA VSSA and FAA UAS are appropriate operational refs. Frontier ("shared autonomy under uncertainty, alert design under workload, operator cognition vs idealized lab reactions") is genuinely current human-factors research.

**Lens 3**: "emergency-stop button vs emergency-stop SYSTEM" is the memorable framing. Teleoperated-humanoid-unsure-which-mode-is-active is concrete.

**Lens 4**: PASS. AV takeover / warehouse stop-authority / drone RTH-under-poor-link transfers are good.

**Lens 5**: PASS.

#### Section 54.6: Deployment approval and safety cases - GOOD
**Lens 1**: Strong. Approval tuple $A = (\text{ODD}, \text{evidence}, \text{defeaters}, \text{residual risk}, \text{rollback})$, GSN goal-structuring framing, and the constrained-argmax formalization in the deep dive ("approved policy is the candidate whose evidence satisfies the safety case, not the argmax of performance") is a sophisticated point.

**Lens 2**: UL 4600 + ISO 21448 SOTIF are the right standards. Domain-creep failure mode is a real, current concern for fleet-updated systems.

**Lens 3**: Indoor-daytime-office-only delivery robot is concrete. The release-blocked-by-incomplete-evidence code (release_ready=False) makes the gate behavior visceral.

**Lens 4**: PASS. Has both a "Release Packet Tool Anchors" table (GSN / hazard log / experiment tracker, with review checks) AND a "Release Board Procedure" algorithm: this section has the most non-boilerplate scaffolding in the part.

**Lens 5**: PASS.

#### Section 54.7: Safety Cases And Assurance Arguments For Embodied AI - GOOD
**Lens 1**: Strong. $\mathcal A = (G, C, E, D, R)$ assurance template, "rhetorical assurance" anti-pattern (confident prose with no artifact traceability) is exactly the right warning. The AssuranceCard dataclass is a clean, runnable artifact.

**Lens 2**: UL 4600 + ISO 21448 + UNECE R157 (a concrete regulation with evidence obligations) is current and well chosen. Frontier ("machine-readable safety cases, telemetry-integrated assurance, updating cases for post-release learning systems") is precise.

**Lens 3**: Warehouse-strong-case-for-aisles-weak-for-public-spaces keeps domains distinct, memorable.

**Lens 4**: PASS.

**Lens 5**: PASS, good consolidation of 54.3-54.6 and hand-off to Ch 55. NOTE: this section appears to be a later-added "application reference" section (figure filename `chapter-54-application-reference-7.png`), and it overlaps heavily with 54.6. Consider merging 54.6 and 54.7 (see Structure Suggestions).

### Chapter 55: Deployment Architecture
**Quality**: NEEDS WORK

Conceptually the right deployment topics (notebook->robot contract, multirate freshness, edge/cloud placement, observability, recovery/security, fleet ops) and 55.1 is genuinely strong (timing inequality, two real SVG state machines, runnable DeploymentManifest dataclass). But 55.2-55.5 are the most aggressively templated sections in the entire part: identical "Same-Artifact Rule" callout, identical evidence-contract SVG (literally the same observation->state->action->monitor->artifact diagram in 55.1-55.5), identical "Mechanism" paragraph ("observe, estimate, choose, constrain..."), identical "Practical Recipe" (5 steps), identical "Builder's Deep Dive" three-claims paragraph, identical Library Shortcut ("about 24 lines"), identical "fun-note", identical Self Check, identical "What's Next", and identical references (ROS + OpenTelemetry in every section). Swapping the topic name leaves 60%+ of each section unchanged.

**HTML BUG (55.1-55.5)**: the epigraph is malformed: a `<figure class="illustration">` is opened inside `<blockquote class="epigraph">` before the `</blockquote>`, so the illustration renders inside the epigraph and the `<cite>` lands after the figure. This should be fixed in all five files: move the figure out of the blockquote.

#### Section 55.1: From notebook to robot - GOOD
**Lens 1**: Strong. Timing chain $\tau_{sense}+\tau_{queue}+\tau_{infer}+\tau_{publish} \le T_{policy} \le k T_{ctrl}$ and the staleness reframe ("once violated, it is no longer model quality but stale-command control") is exactly right. Evidence record $e_i$ tuple is concrete. Two real SVG diagrams (evidence contract + boot/ready/autonomous/degraded/rollback state machine) and a runnable DeploymentManifest. This is the best deployment section.

**Lens 2**: "robot-native release engineering, shadow deployment, formal runtime assurance; preserve real-time guarantees while deploying larger multimodal policies" is current and precise. Refs (ROS, OpenTelemetry) are thin for a frontier claim.
- Fix: add a 2024-2025 ref on real-time large-policy deployment (e.g., action chunking / async inference for VLA models).

**Lens 3**: The MuJoCo->hardware reality ("the grasp policy is NOT the first thing that fails; camera frames, stale extrinsics, actuator enable races, late control packets are") is the chapter's best "aha". Keep.

**Lens 4**: PASS. Real tool table (ROS 2 lifecycle / Docker or Nix / MLflow or DVC).

**Lens 5**: Strong. The "notebook mode intellectually even if physically on a robot" line is memorable.

#### Section 55.2: Real-time inference and control rates - NEEDS WORK
**Lens 1**: The actual content is good: multirate Hz bands (controller 200-1000, estimator 30-200, policy 5-30, planner 0.5-2), tail-latency contract $\Pr(\tau_{age} > \tau_{max}) \le \epsilon$, and "p95/p99 belong in the same artifact" is the correct, non-obvious point. The quantiles code is runnable.
- Problem: this real content is buried under the cloned Same-Artifact Rule, cloned evidence-contract SVG, cloned Mechanism, cloned Practical Recipe, cloned fun-note.

**Lens 2**: "asynchronous policies, action chunking, speculative planning to fit large models in real-time loops" is current and the most on-point frontier note in Ch 55. Should cite Diffusion Policy / action-chunking (ACT, Zhao 2023) and a VLA latency paper.

**Lens 3**: GPU-stall-pushes-command-age-past-horizon is a real, memorable failure. But the fun-note is the cloned one.

**Lens 4**: PASS on content (TensorRT, ROS 2 executors named). The evidence-contract SVG is identical to 55.1/55.3/55.4/55.5.
- Fix: replace the cloned SVG with a multirate timing diagram (overlaid loop rates + a latency-tail histogram).

**Lens 5**: The cloned "Reader Pathway / Same-Artifact Rule / Practical Recipe / Builder's Deep Dive" make this read as a fill-in-the-blank of 55.1. Strip the shared blocks and keep the multirate content.

#### Section 55.3: Edge vs. cloud-robot computation; asynchronous inference - NEEDS WORK
**Lens 1**: Good core idea: placement score $R = w_1\,\text{crit} + w_2\,\text{latency} + w_3\,\text{availability} + w_4\,\text{privacy}$, keep-local-if-action-critical-and-deadline-sensitive. Correct. The threshold-12 rule in code is arbitrary and unexplained.
- Fix: explain the threshold or replace with a normalized score in [0,1] and a stated cutoff rationale.

**Lens 2**: "asynchronous robot foundation models split fast local control from slower cloud reasoning, caches, confidence-gated requests" is current (this is the Helix / pi-zero / system-1-system-2 pattern). Should NAME that pattern and cite.
- Fix: "This fast-local / slow-cloud split is the System 1 / System 2 pattern in recent robot foundation models (e.g., Figure Helix 2025, Physical Intelligence pi-0 2024): a high-rate reactive policy on-robot, a slower VLM reasoning layer that may run on edge or cloud."

**Lens 3**: "Cloud can summarize a room inventory but must not decide whether to brake before contacting a person" is the memorable, correct architectural line. Keep. The hidden-cloud-dependency warning (remote tokenization, centralized map lookup, auth handshakes) is sharp.

**Lens 4**: PASS on content. Same cloned SVG problem.

**Lens 5**: Same template-saturation problem as 55.2.

#### Section 55.4: Logging, monitoring, model updates - NEEDS WORK
**Lens 1**: Good content: observability tuple $o_i$, and the shadow/canary/promote/rollback discipline with retained-skill + safety thresholds is exactly right for fleet ML ops. The "promotion unjustified unless measurable AND reversible; reject improved-score-but-incomplete-coverage candidate" point is strong.
- Problem: the code is weak: required_fields == logged_fields by construction so coverage is trivially 1.0. Make logged_fields deliberately miss a field to show a blocked promotion.

**Lens 2**: "continuous evaluation: every update carries shadow run, canary panel, rollback trigger, drift monitor" is current. No ML-ops or drift-detection citation.

**Lens 3**: Grasp-update-improves-cartons-but-fails-on-reflective-packaging is concrete and memorable.

**Lens 4**: NEEDS WORK on code (see above). Tool table (ROS 2 bags / Prometheus / artifact registry) is fine.

**Lens 5**: Template saturation; strip shared blocks.

#### Section 55.5: Failure recovery, security, maintenance - NEEDS WORK
**Lens 1**: Good content: guarded state machine {nominal, degraded, recovery, safe stop} + security trust predicates + maintenance slow-state (battery health, encoder drift, calibration age). The "compromised command channel and worn actuator both change the safe physical action" framing (security/maintenance ARE safety) is a strong, non-obvious point.
- The code is reasonable (splits recoverable vs secure-maintenance vs operator-repair).

**Lens 2**: "security-by-design, operational resilience, maintenance-aware learning" is reasonable but uncited; this section has the thinnest research grounding (only ROS + OpenTelemetry, neither about security). 
- Fix: add a robot/CPS security reference and an adversarial-physical-input reference (the section mentions "adversarial inputs can target physical behavior" with zero citation).

**Lens 3**: Blocked-wheel + expired-certificate needing two different recovery paths is concrete and memorable.

**Lens 4**: NEEDS WORK. Security is a major topic given one toy example and no named tools beyond "secure boot / watchdogs / maintenance logs." Add a real example (sensor spoofing, GPS spoofing for drones, command-injection).

**Lens 5**: Template saturation.

#### Section 55.6: Industrial Fleets, Open-RMF, AMR Interoperability, And Operations - GOOD
**Lens 1**: This is a later-added application section with a DIFFERENT template (Why This Section Was Added / Technical Core / Practical Stack). KPI tuple is a "system contract not a loss function" (honest framing). Real, named, current stack: Open-RMF, MassRobotics AMR Interoperability Standard, ROS-Industrial, ISO 3691-4, ANSI/RIA R15.08, NIST ARIAC. This is the most real-world-grounded section in Ch 55.

**Lens 2**: Strong, current, well-cited (6 real references including the AMR interoperability standard and the safety standards). Frontier note (open robot foundation models + fleet telemetry) is fine.

**Lens 3**: The "Memory Hook" fun-note ("visible twice: design sketch and replay artifact; the second keeps the first honest") is the one fresh fun-note in the chapter.

**Lens 4**: PASS. Warehouse-fleet-across-receiving/putaway/picking/dock example is concrete and named. ApplicationEvidence card is runnable.

**Lens 5**: PASS, though it reads as a bolt-on (different template, "Why This Section Was Added" heading). It is good content but stylistically inconsistent with 55.1-55.5.

## Cross-Chapter Issues in This Part

1. **The identical four-row checklist table** (Scenario panel / Runtime interface / Metric script / Review layer, with byte-identical cell text) appears in 19 of 23 sections: ALL of 52.1-52.6, 53.1-53.4, 54.1-54.7. It is the single most repeated block in the part and the clearest contract violation (swapping the topic leaves it 100% unchanged). Recommendation: delete it from every section and replace with a per-topic 2-3 row table where it adds nothing (most sections already have a topic-specific checklist elsewhere).

2. **Cloned framing sentences per chapter**: Ch 52 sections 2-6 share the same epigraph, "Reader Pathway", and "Why This Matters" opening sentence. Ch 53 shares one epigraph across all 4 sections and one "Reader Pathway". Ch 54 shares the "sits at the boundary between learning and safety engineering..." sentence across all 7. Ch 55 sections 2-5 share ~60% of their prose. Each needs section-specific framing.

3. **The evidence-contract SVG in Ch 55** (observation->state->action->monitor->artifact) is literally identical in 55.1-55.5. Four of the five should be replaced with topic-specific diagrams (multirate timing, edge/cloud split, shadow/canary pipeline, recovery state machine).

4. **Placeholder / non-citations**: "Official SIMPLER resources," "Official robot benchmarking and fleet telemetry documentation," "Official ROS 2 diagnostics documentation," "Official MLflow, DVC, and ROS 2 logging documentation" appear as bibliography entries. SIMPLER especially has a real paper (Li et al. 2024, arXiv:2405.05941) and must be cited properly given the chapter is named after it.

5. **Toy code throughout 52 and 55**: most code fragments operate on hardcoded dicts/lists, not against any named simulator or library. The contract asks for "correct topic-specific runnable code"; the code IS runnable and topic-shaped, but several pieces are degenerate (55.4 coverage==1.0 by construction; 55.3 threshold=12 unexplained; 53.2 ECE is a single mean not binned). These should be made non-degenerate.

6. **Duplicated paragraphs within sections**: 53.1 and 53.4 each repeat the "Concrete stack anchors for this chapter" paragraph verbatim in both Library Shortcut and Builder's Deep Dive. Delete the duplicates.

7. **Engagement deficit**: no named real-system anecdotes (Spot, Atlas, Waymo, RT-2, Helix) appear in worked examples even though the audience IS Boston Dynamics / frontier labs. Adding 1-2 real-system "war stories" per chapter would dramatically raise memorability without touching depth.

## Top 10 Highest-Priority Fixes for This Part

1. **Fix the epigraph HTML bug in 55.1-55.5** (`.../module-55-deployment-architecture/section-55.1.html` through `section-55.5.html`): move the `<figure class="illustration">` out of the `<blockquote class="epigraph">`. Currently the figure renders inside the epigraph and the `<cite>` is orphaned. Mechanical, high-value, affects 5 files.

2. **De-template Chapter 55 sections 55.2-55.5**: strip the shared "Same-Artifact Rule", "Mechanism", "Practical Recipe", "Builder's Deep Dive three-claims", Library Shortcut "about 24 lines", fun-note, Self Check, and "What's Next" that are identical across the four. Keep each section's genuine content (multirate tails, placement score, shadow/canary, recovery state machine). This is the largest quality win in the part.

3. **Delete the identical four-row checklist table** from all 19 sections that carry it (52.1-52.6, 53.1-53.4, 54.1-54.7). Replace with section-specific content where needed.

4. **Replace the cloned evidence-contract SVG in 55.2-55.5** with topic-specific diagrams: 55.2 multirate timing + latency-tail histogram; 55.3 edge/cloud split with action-criticality gate; 55.4 shadow->canary->promote/rollback pipeline; 55.5 recovery/security/maintenance guarded state machine.

5. **Fix placeholder citations**, priority on SIMPLER: in `section-52.5.html` and `module-52.../index.html`, replace "Official SIMPLER resources" with Li, X. et al., "Evaluating Real-World Robot Manipulation Policies in Simulation" (SIMPLER), 2024, arXiv:2405.05941, with a one-line on its MMRV metric. Same pass for the other "Official ... documentation" bib stubs.

6. **Name SPL in 52.2** (`section-52.2.html`): connect $\rho_i = d^*_i/d_i$ to SPL (Anderson et al. 2018). A navigation researcher will not trust a path-efficiency section that omits the field-standard metric name.

7. **Name the System-1/System-2 robot-foundation-model pattern in 55.3** (`section-55.3.html`): tie the fast-local/slow-cloud split to Helix (2025) and pi-0 (Physical Intelligence, 2024). This is the current frontier the section gestures at without naming.

8. **Vary the per-section epigraphs in Chapter 53** (`section-53.1.html`-`53.4.html`): all four currently use the same "A robust robot is not the one that never sees surprise..." Keep it on 53.1; write distinct epigraphs for calibration, OOD, and runtime monitoring.

9. **Fix degenerate code**: 55.4 (`section-55.4.html`) make `logged_fields` miss a field so coverage < 1.0 and the gate blocks; 55.3 explain or normalize the placement threshold; 53.2 add a real 2-bin ECE so the "cancellation hides local miscalibration" warning is demonstrated, not just stated.

10. **Delete intra-section duplicate paragraphs** in 53.1 and 53.4 (the repeated "Concrete stack anchors" paragraph), and add named real-system examples (Spot fault modes, Waymo ODD, RT-2 eval) to one worked example per chapter to close the engagement gap.

## Structure Suggestions for This Part

1. **Merge 54.6 and 54.7.** "Deployment approval and safety cases" (54.6) and "Safety Cases And Assurance Arguments For Embodied AI" (54.7) cover heavily overlapping material (approval tuple, GSN, ODD, defeaters, residual risk, rollback). 54.7 reads as a later application-reference add-on (figure `chapter-54-application-reference-7.png`). Either merge into one "Deployment Approval and Safety Cases" section, or sharpen the split: 54.6 = the release-gate decision process, 54.7 = the structured assurance-argument artifact only, with the redundant tuple math removed from one of them.

2. **Reconcile the Chapter 55 template inconsistency.** 55.1-55.5 use one shell (Problem First / Theory / Mechanism / Same-Artifact Rule) and 55.6 uses a different shell (Why This Section Was Added / Technical Core / Practical Stack). 55.6 is good content but stylistically alien. Either bring 55.6 into the chapter template or, better, use 55.6's more real-world-grounded, well-cited style as the target and lift the other deployment sections toward it.

3. **The part index "Part Overview" and chapter-card descriptions are boilerplate** ("This chapter develops X as part of the embodied AI stack" for all four). Rewrite each chapter card with a one-line specific hook (e.g., Ch 54: "From hazard ranking through CBF/HJ safe sets to GSN assurance cases and release gates").

4. **No structural deletions needed at chapter level.** All four chapters earn their place for this audience; the work is de-duplication and depth-evening, not removal. Section counts (6/4/7/6) are reasonable; the only merge candidate is 54.6+54.7.
