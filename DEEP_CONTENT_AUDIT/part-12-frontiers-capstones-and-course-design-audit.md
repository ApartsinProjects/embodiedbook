# Part 12 Content Audit: Frontiers, Capstones, and Course Design

## Part Overview
Part XII contains two qualitatively different bodies of writing under one cover. Chapters 56 and 57 (memory, continual learning) are genuinely well written: real equations with intuition, topic-specific worked examples, clear failure taxonomies, and named tooling (Avalanche, EWC, replay services). Chapters 58, 59, and 60 (frontiers, capstones, teaching) are built on a rigid two-tier template: each section opens with roughly 90 lines of topic-agnostic boilerplate (the "SectionContract" dataclass, "What This Section Develops", the identical "closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t$" paragraph, identical Practical Recipe, identical Research Frontier text) and only becomes substantive in the trailing `Topic-Native Deepening` block. The deepening blocks are good and topic-specific; the boilerplate halves fail the non-substitutability rule almost line for line. The single highest-value action for this part is to delete or radically compress the boilerplate top half of every section in chapters 58-60 and promote the deepening block to be the section body.

A second cross-cutting defect: the auto-generated `SectionContract` worked examples in 58-60 print **truncated, broken strings** (e.g. `'track data diversity, embodiment coverage, task coverage, and interv'`, `'object_search_in_a_simulated_hom'`). These are not runnable-result code; they are evidence-artifact filler the contract explicitly forbids, and the truncation makes them look like bugs to the Boston Dynamics / research-scientist audience.

## Fun Elements to Preserve
Strong, genuinely witty epigraphs (these are the best engagement asset in the part and must survive any rewrite):
- 56.1: "I remembered the last ten seconds perfectly, then promoted the wrong ten seconds forever." (cite: A Short-Term Buffer Seeking Tenure)
- 56.2: "The map knows where, the episode knows when, and the semantic store keeps insisting it knows why." (cite: A Three-Drawer Memory Cabinet)
- 56.3: "I found the relevant memory only after the planner stopped asking for nostalgia and started asking for actions."
- 56.4: "I was useful yesterday, stale today, and somehow still very persuasive." (cite: An Aging Memory Trace)
- 57.1: "Deployment is where training becomes a subscription service with consequences."
- 57.2: "I mastered the new drawer and now salute every chair like a handle." (cite: A Forgetful Adaptation Run)
- 57.3: "The human said no, which was the cleanest label I received all week."
- 57.4: "I can update myself safely, provided someone remembers the word rollback."
- 58.1: "I do scale with data, but only the data that contains the mess I will meet later."
- 58.2: "I am a generalist until the gripper asks for millimeters." (excellent, captures the precision/coverage tradeoff)
- 58.3: "My imagined rollout was cheaper than physics, which is not the same as being true." (excellent)
- 58.4: "My weights are open, my data is vague, and my license has entered the group chat." (very funny, current)
- 58.5: "I can solve the task once. Reliability is the part where the task notices."
- 58.99: "Every frontier claim becomes calmer after you ask for the artifact."
- 59.1: "I found the mug, the chair, and a very convincing false positive under the sofa."
- 59.4: "Fine-tuning made me confident. The baseline made me explain myself."
- 60.1: "Fourteen weeks is plenty of time, provided every theorem eventually touches a log file."
- 60.5: "My lab budget has three settings: local, cloud, and please use the small model today."
- 60.6: "I grade the artifact, the evidence, and the explanation, because copied code rarely survives questions."
- Chapter 59 index: "I am not a final project until my failure cases have filenames." (cite: A Capstone Artifact With Receipts)

`fun-note` / Memory Hook callouts exist in every 58-60 section, but most are templated and interchangeable (three rotating variants: "control-room label", "next frame of video", "could a teammate point to the log line"). These are NOT worth preserving as-is; they are boilerplate wearing a fun-note costume. The 58.2 and 58.3 variants are slightly better tuned. Total genuinely-distinct fun elements worth protecting: the ~19 epigraphs above.

## Chapter-by-Chapter Analysis

### Chapter 56: Embodied Agents with Memory
**Quality**: GOOD

#### Section 56.1: Why memory matters; short- vs. long-term - GOOD
**Lens 1 (Deep Explanation)**: PASS. Clean memory-augmented control model ($h_t=f_\theta(h_{t-1},o_t)$, retrieve, policy). Working vs long-term distinction is motivated before mechanism. The "Action Benefit Is The Admission Test" key-insight is a real design rule, not a name-drop.
**Lens 2 (Research Frontier)**: Adequate but thin. Frontier callout lists three open problems (learning what to remember, uncertainty over items, cross-embodiment sharing) but none is stated precisely enough to be falsifiable. Fix: name a concrete open question, e.g. "No published method jointly learns a promotion policy and a forgetting policy from downstream task reward on a real robot; current systems hand-tune TTLs."
**Lens 3 (Fun/Engagement)**: Strong epigraph (listed above). The dataclass MemoryItem example with working vs episodic TTL (2s vs 86400s) is a small "aha". No missed opportunity of note.
**Lens 4 (Examples/Analogies)**: PASS. Kitchen-robot mug occlusion and warehouse aisle-B-after-4pm are concrete and topic-specific. Code runs and prints meaningful output.
**Lens 5 (Teaching Flow)**: PASS. Has the "Reader Pathway" template callout which is mild boilerplate but harmless here. Good What's Next into 56.2.

#### Section 56.2: Spatial, episodic, and semantic memory - GOOD
**Lens 1**: PASS. Three-family formalization ($\mathcal M_{spatial}=(V,E,\psi)$ etc.), update-cadence distinction, and the comparison table (representation / query / failure mode) give real depth.
**Lens 2**: Adequate. Frontier on cross-memory-type translation is well posed.
**Lens 3**: Excellent epigraph. The "semantic prior silently overrides spatial evidence" warning ("the corridor is usually open") is a memorable counterintuitive point.
**Lens 4**: PASS. Scissors-search worked example is concrete.
**Lens 5 (Teaching Flow)**: ISSUE - duplicate callouts. The section contains the `research-frontier` callout twice (near-identical text at lines 78 and 81) and the `self-check` callout three times (lines 79, 80, 82), two of which are paraphrases of each other. Fix: delete the duplicates, keep one research-frontier and at most two distinct self-checks. Also two consecutive `library-shortcut` callouts ("Library Shortcut" then "Implementation Stack") is redundant; merge.

#### Section 56.3: Memory retrieval for planning - GOOD
**Lens 1**: PASS, strong. The scoring function $s(m;q,g)=\alpha\,\mathrm{sim}+\beta\,\mathrm{utility}-\gamma\,\mathrm{staleness}-\delta\,\mathrm{risk}$ with the two-stage retrieve-then-rerank mechanism is exactly the right depth. "Decision Value Beats Similarity" is a real insight.
**Lens 2**: PASS. The frontier (training retrieval from downstream control improvement, credit assignment across time) is precisely stated.
**Lens 3**: Good epigraph (nostalgia vs actions).
**Lens 4**: PASS. Tray-carrying mobile manipulator example; runnable scoring code with a defensible result (m2 wins despite lower similarity).
**Lens 5 (Teaching Flow)**: ISSUE - duplicate callouts again. Two `library-shortcut` (lines 67, 68), two `research-frontier` (73, 76), three `self-check` (74, 75, 77) with overlapping text. Same fix as 56.2: dedupe.

#### Section 56.4: Memory errors - GOOD
**Lens 1**: PASS, strong. Trust score $\rho(m)=\lambda_1\mathrm{src}+\lambda_2\mathrm{ctx}-\lambda_3\mathrm{age}-\lambda_4\mathrm{conflict}$, the "memory safety is a data-model problem" framing, and the four-row error taxonomy (staleness / aliasing / overconfidence / poisoning) with distinct remedies is genuinely graduate-level.
**Lens 2**: PASS. Frontier on fixed-vs-learned-vs-context-conditioned trust thresholds is concrete.
**Lens 3**: Excellent epigraph. The "stale plausible memory is more dangerous than no memory" point is the memorable through-line.
**Lens 4**: PASS. Hospital isolation-barrier and drone street-canyon-wind examples are vivid and correct.
**Lens 5 (Teaching Flow)**: ISSUE - duplicate callouts (two library-shortcut, two research-frontier, two self-check). Dedupe.

### Chapter 57: Continual and Lifelong Learning
**Quality**: GOOD (the strongest chapter in the part)

#### Section 57.1: Learning after deployment - GOOD
**Lens 1**: PASS. Governed-pipeline model $D_t\rightarrow U_t\rightarrow\theta_{t+1}\rightarrow V_t\rightarrow R_t$ plus the five-stage table (monitoring/candidate/validation/rollout/rollback with failure-if-missing). The extra prose paragraphs (release-object bundle, perception-vs-control adaptation, organizational interfaces) add real depth without boilerplate.
**Lens 2**: PASS. Frontier (merging self-supervised field data with strict safety gates) is well posed.
**Lens 3**: Good epigraph ("subscription service with consequences"). No fun-note callout, but the prose carries it.
**Lens 4**: PASS. Shelf-picker reflective-packaging and hospital-waxed-floor examples are concrete.
**Lens 5**: PASS. No duplicate-callout problem (this chapter avoids the 56 defect). Clean.

#### Section 57.2: Catastrophic forgetting and mitigation - GOOD
**Lens 1**: PASS, strong. EWC penalty $L(\theta)=L_{new}+\lambda\sum_i F_i(\theta_i-\theta_i^\star)^2$ with Fisher-importance explanation; mitigation-family table (replay/regularization/parameter-isolation with strength+weakness); the diagnosis-before-mitigation stance is exactly right.
**Lens 2**: PASS. Selective replay and parameter routing at scale, well stated.
**Lens 3**: Best epigraph in the chapter ("salute every chair like a handle"). The interface-degradation insight (timing/contact degrade before headline success) is an "aha".
**Lens 4**: PASS. Glossy-cereal-box vs transparent-bottle forgetting example; forgetting statistic computed from one co-evaluated panel (matches the house "one-pass construct-matched" rule).
**Lens 5**: PASS. Avalanche named. Clean.

#### Section 57.3: Online adaptation; human correction as data - GOOD
**Lens 1**: PASS. Typed-correction record $c_t=(o_t,a_t,\tilde a_t,\kappa_t,\nu_t)$; correction-type table (demonstration/preference/relabel/safety-stop with downstream use). The local-repair-vs-generalization distinction is a strong addition.
**Lens 2**: PASS. Frontier (pricing operator attention, which failures deserve correction first) is concrete.
**Lens 3**: Excellent epigraph ("cleanest label I received all week").
**Lens 4**: PASS. Teleop-correction vs verbal-preference vs safety-stop routing example is concrete and correct.
**Lens 5**: PASS. Clean.

#### Section 57.4: Safe continual learning; evaluation over time - GOOD
**Lens 1**: PASS, strong. Release gate $G_t=[\Delta_{new}\ge\tau][F_t\le\tau][S_t\le\tau][\text{rollback\_ready}]$ with prequential evaluation; rare-event-slice and coupled-hardware-drift caveats are exactly the things a deployment engineer needs.
**Lens 2**: PASS. Long-horizon co-evolution (data, hardware wear, human workflows) frontier is precise.
**Lens 3**: Good epigraph ("remembers the word rollback").
**Lens 4**: PASS. Fleet-AMR canary example; runnable gate code returning accept/reject.
**Lens 5**: PASS. Prometheus/Grafana/registry tooling named. Clean.

### Chapter 58: Frontier and Open Problems
**Quality**: NEEDS WORK (good content trapped under heavy boilerplate)

Cross-section pattern (applies to ALL of 58.1-58.99): the section body before `Topic-Native Deepening` is template-generated and topic-agnostic. Specifically these blocks are byte-for-byte identical (modulo the topic-name substitution) across every section: the "What This Section Develops" heading and its two paragraphs; the "Theory" paragraph about "$o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$"; the "Mechanism" under-the-hood callout; the "Worked Example" sensor-reading-becomes-an-estimate paragraph; the entire `SectionContract` dataclass code; the five-step "Practical Recipe"; the "Common Failure Mode"; the "Practical Example" ("starts by writing the task panel"); the "Research Frontier" ("not whether a larger policy can produce a better demo"); the "Self Check". Swapping the topic name leaves every one of these unchanged: by the non-substitutability rule they are boilerplate and should be cut. The figure captions are also templated ("Section 58.X: ... is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation"). Fix for the whole chapter: delete the boilerplate top half, keep the epigraph + one framing paragraph, then promote `Topic-Native Deepening` to be the section body.

#### Section 58.1: Scaling laws and data engines for robots - NEEDS WORK
**Lens 1**: Mixed. Top half boilerplate. Deepening half is good: real scaling object $\mathcal E(N,H,B)$, the "panel distribution $p_{eval}$ must not move while you grow N" point, and the data-engine algorithm (mine failures into a priority queue) are substantive.
**Lens 2**: PASS in deepening. Conditional-scaling-law frontier (how much data for a new embodiment/horizon/sensor) is precisely stated. References (Open X-Embodiment 2023, V-JEPA/Bardes 2024) are current and connected.
**Lens 3**: Good epigraph. Templated fun-note (cut it).
**Lens 4 (Examples/Analogies)**: ISSUE - the primary `SectionContract` code prints truncated garbage (`'track data diversity, embodiment coverage, task coverage, and interv'`, topic `'scaling_laws_and_data_engines_fo'`). The deepening `validate_artifact` example (widowx/aloha/mobile-manipulator, kitchen-v2 panel) is good and real. Fix: delete the broken SectionContract block.
**Lens 5**: Boilerplate breaks flow; once cut, deepening flows well. Good cross-links (Ch 24, Ch 52).

#### Section 58.2: Generalist vs. specialist policies - NEEDS WORK
**Lens 1**: Deepening is strong: router objective $\min_{\rho,\Pi}\mathbb E[\ell]+\lambda\,\text{latency}+\mu\,\text{ops\_cost}$, the "slightly stronger specialist that doubles maintenance can lose" point. Top half boilerplate.
**Lens 2**: PASS in deepening. Conditional-specialization frontier (MoE for embodied control, retrieval-augmented policy memory) is current.
**Lens 3**: Best epigraph in the chapter ("generalist until the gripper asks for millimeters").
**Lens 4**: Deepening example (generalist 0.79 vs specialist-mean 0.84 with 0.11 router error and latency table) is excellent and forces a real decision. SectionContract code truncated/broken (cut).
**Lens 5**: Same boilerplate issue.

#### Section 58.3: World models in the robot loop - NEEDS WORK
**Lens 1**: Deepening strong: latent model $z_{t+1}\sim p_\theta(z_{t+1}\mid z_t,a_t)$, MPC-in-latent-space planning, execute-first-action-then-replan. Top half boilerplate.
**Lens 2**: PASS. Action-relevant prediction frontier ("knows when uncertain, degrades gracefully under contact changes"). DreamerV3/TD-MPC2/mbrl-lib named.
**Lens 3**: Excellent epigraph ("cheaper than physics is not the same as being true").
**Lens 4**: Failure-test table (dynamics mismatch / observation aliasing / long-horizon drift) is topic-specific and good. SectionContract code broken (cut).
**Lens 5**: Same boilerplate issue.

#### Section 58.4: The open-vs-closed model divide - NEEDS WORK
**Lens 1**: Deepening good: utility $U=\alpha\,\text{cap}-\beta\,\text{lat}-\chi\,\text{cost}+\delta\,\text{inspect}+\eta\,\text{repro}$, governance framing. Top half boilerplate.
**Lens 2**: PASS. Frontier (can open robot foundation models close the capability gap while preserving inspectability) is current and well posed for the 2024-2026 window.
**Lens 3**: Funniest epigraph in the part ("my license has entered the group chat").
**Lens 4**: Decision matrix and the privacy-driven governance card (camera frames cannot leave site) are concrete. SectionContract code broken (cut).
**Lens 5**: Same boilerplate issue.

#### Section 58.5: What is still unsolved (long-horizon reasoning, reliability, real-world RL) - NEEDS WORK
**Lens 1**: Deepening strong: reliability $R(H)=\Pr(\text{success and no safety violation for all }t\le H)$, the success-rate-vs-reliability temporal-composition distinction is a genuine insight. Top half boilerplate.
**Lens 2**: PASS. Compositional-reliability frontier is precise.
**Lens 3**: Good epigraph ("Reliability is the part where the task notices").
**Lens 4**: The reliability ledger (episode_minutes [5,10,20] -> reliability [0.84,0.61,0.33]) showing degradation with horizon is the best single example in the chapter. SectionContract code broken (cut).
**Lens 5**: Same boilerplate issue.

#### Section 58.99: Frontier Watch - NEEDS WORK
**Lens 1**: Deepening good: watch score $W=s_{artifact}+s_{indep}+s_{deploy}-s_{ambiguity}$, the "watchlist turns marketing velocity into judgment" framing. Top half boilerplate.
**Lens 2**: PASS. Meta-frontier (evaluation literacy) is the right closing note for the chapter.
**Lens 3**: Good epigraph. The custom hero illustration (figure 58.99A, real alt-text, not the templated caption) is a positive exception.
**Lens 4**: The watch-item manifest ("watch, do not rewrite syllabus yet") and the weekly-ritual teaching use are concrete. SectionContract code broken (cut).
**Lens 5**: ISSUE - section number 58.99 is an awkward placeholder ID; it should be renumbered 58.6. Same boilerplate issue otherwise.

### Chapter 59: Capstone Projects
**Quality**: NEEDS WORK (excellent capstone briefs buried under the same boilerplate as Ch 58)

The chapter index is strong (clear roadmap, tool map, evidence-card lab, real bibliography with RT-1/RT-2/Diffusion Policy/DreamerV3/LeRobot links). Every section 59.1-59.12 uses the same two-tier template as Ch 58 (boilerplate top half + good `Topic-Native Deepening`). The deepening halves are the most valuable in the chapter: each gives a real scoring/loss function, a fixed evaluation panel, and a project deliverable table. Same chapter-wide fixes apply: cut the boilerplate top half and the broken SectionContract code from every section.

#### Section 59.1: Object search in a simulated home - NEEDS WORK
**Lens 1/4**: Deepening strong: capstone score $J=\mathbb 1[\text{found}]-\lambda_T T_{find}-\lambda_C C-\lambda_L L-\lambda_F F$ with the "publish fixed weights across all teams" instruction; Habitat/AI2-THOR named; stop-rule ("3 consistent views") is the right pedagogical hook. SectionContract code prints truncated strings (cut).
**Lens 2**: Language-conditioned search under uncertainty frontier is concrete.
**Lens 3**: Good epigraph ("a very convincing false positive under the sofa").
**Lens 5**: Boilerplate top half; once cut this is a strong capstone brief.

#### Section 59.2: Language-guided navigation with replanning - NEEDS WORK
Same pattern. Deepening (grounded replanning, constraint-aware evaluation) is good. Cut boilerplate + broken code.

#### Section 59.3: Vision-based robotic pick-and-place (IL + RL) - NEEDS WORK
**Lens 1/4**: Deepening strong and the best-justified two-stage story in the chapter: $\mathcal L_{BC}=\sum_t\lVert a_t-\pi_\theta(o_t)\rVert^2$ then RL fine-tune; the "IL gives competence, RL spends budget on recovery/edge cases" framing; before/after on the SAME perturbation panel (bc 0.71 -> bc+rl 0.83) directly enforces the house construct-matched rule. ManiSkill/robomimic/Diffusion Policy named.
**Lens 2**: Cross-embodiment transfer extension is current.
**Lens 5**: Cut boilerplate top half.

#### Section 59.4: Fine-tune an open VLA on a custom task (LeRobot) - NEEDS WORK
**Lens 1**: Deepening good: $\mathcal L(\theta)=\mathbb E_{D_{custom}}[-\log\pi_\theta(a\mid o,g)]$, the "tokenization / action discretization / embodiment mismatch dominate the outcome" point.
**Lens 2**: PASS. Adaptation-efficiency frontier (how little data to retarget a foundation policy) is current.
**Lens 4 (Examples/Analogies)**: ISSUE - this is the single most important hands-on section in the whole part (it is the named LeRobot capstone), yet the only code is a manifest `dict` (`base_model: 'open-vla-small'`, episodes 180, frozen_backbone True) plus the broken SectionContract. There is no actual fine-tuning code. For a Boston-Dynamics / research-scientist audience this is the place the book most needs a real `lerobot`/`OpenVLA` training snippet (dataset load, LoRA config, train loop, eval call). Fix: add a compact but real runnable LeRobot fine-tune example (even ~20 lines invoking the actual API) in place of the broken SectionContract.
**Lens 3**: Good epigraph. NOTE: 59.4 is missing the hero illustration `<figure>` that every other section has - either add the image or this is a rendering inconsistency.
**Lens 5**: Cut boilerplate top half.

#### Section 59.5: Learned locomotion with sim-to-real analysis - NEEDS WORK
Deepening (transfer-gap centering, matched sim-to-hardware evidence) is good and topic-appropriate. Cut boilerplate + broken code. This section should name a concrete sim-to-real tool path (Isaac Lab domain randomization, MuJoCo/MJX) in a runnable form.

#### Section 59.6: World-model-based planning agent - NEEDS WORK
Deepening (latent prediction -> short-horizon planning, drift diagnostics) is good and complements 58.3. Cut boilerplate + broken code.

#### Section 59.7: Safety-shielded embodied agent - NEEDS WORK
Deepening (grade safety by intervention quality, false-alarm rate, task completion, not slogans) is good. Cut boilerplate + broken code.

#### Section 59.8: LLM-based household task planner - NEEDS WORK
Deepening (separate language planning from grounding/affordances/execution traces) is good and current. Cut boilerplate + broken code.

#### Section 59.9: Drone inspection planner - NEEDS WORK
Deepening (route planning + safety reserve + coverage as one mission-level evidence problem) is good; PX4 SITL named. Cut boilerplate + broken code.

#### Section 59.10: Multi-agent search and rescue - NEEDS WORK
Deepening (communication, role allocation, stale-information failure) is good and a distinctive topic. Cut boilerplate + broken code.

#### Section 59.11: Open-ended research project - NEEDS WORK
**Lens 1/4**: Deepening strong: the $(Q,B,P,A)$ tuple (question/baseline/perturbation panel/artifact set) and the falsifiable charter example (retrieval-augmented policy memory vs no-retrieval baseline) are exactly right for a research-scientist reader. "Choose the simplest baseline that could disprove the fancy method" is a genuine research-hygiene insight.
**Lens 2**: Meta-research-on-embodied-evaluation frontier is a strong, current extension.
**Lens 5**: Cut boilerplate top half.

#### Section 59.12: Application Track Capstone Templates - NEEDS WORK
**Lens 1/4**: Deepening good: template tuple $T=(\text{ODD},\text{state},\text{actions},\text{safety},\text{metrics},\text{artifacts})$ with the household/drone/driving/humanoid track table (CARLA, CommonRoad, PX4 SITL, Isaac Lab named).
**Lens 5 (Teaching Flow)**: ISSUE - structural inconsistency. Unlike its siblings, 59.12 has TWO complete bodies: a first body (its own `ApplicationEvidence` card with `Recipe For Builders`, a fun-note, a self-check, a research-frontier, a key-takeaway, AND an exercise) followed by a SECOND `Topic-Native Deepening` body with its own duplicate fun-note/self-check/research-frontier/key-takeaway/exercise. This looks like two generated sections concatenated. Fix: merge into one body; remove the duplicated callouts and the duplicated exercise.

### Chapter 60: Teaching with This Book
**Quality**: NEEDS WORK (good course-design content; boilerplate is most incongruous here)

Same two-tier template. The boilerplate is worse-fitting in this chapter than anywhere else: forcing a 14-week syllabus or an academic-integrity rubric into "should be placed inside the closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$" and into a "Worked Example" about "a sensor reading becomes an estimate" is simply wrong for the topic. The closing Exercise on every section ("Design a method-matched experiment ... observation schema, action interface, ... perturbation") is also nonsensical for a teaching topic. The `Topic-Native Deepening` halves, by contrast, are good and use appropriate teaching-specific formal objects (load models, budget models, rubric weightings).

#### Section 60.1: One-semester graduate course (14 weeks) - NEEDS WORK
**Lens 1**: Deepening good: weekly-load model $L_k=\alpha T_k+\beta C_k+\gamma P_k$ with the "bound $\max_k L_k$" design check; the 4-block weekly arc table is genuinely useful to an instructor.
**Lens 5 (Teaching Flow)**: ISSUE - the boilerplate "closed-loop transition" Theory paragraph and the "method-matched experiment / perturbation" Exercise are topic-inappropriate. Fix: replace the Exercise with a real teaching task, e.g. "Take the 14-week arc table and reassign two weeks to fit a department that already teaches a separate control course; show the new $L_k$ profile."
**Lens 3**: Good epigraph ("every theorem eventually touches a log file"). References (Biggs 1999; Anderson & Krathwohl 2001) are correct pedagogy sources.

#### Section 60.2: One-semester advanced undergraduate course - NEEDS WORK
Same pattern; deepening (lighter theory, more labs) is appropriate. Cut/replace boilerplate and the experiment-style exercise.

#### Section 60.3: Two-semester sequence - NEEDS WORK
Same pattern. Cut/replace boilerplate and exercise.

#### Section 60.4: Research-seminar track - NEEDS WORK
**Lens 1/4**: Deepening strong: weekly $(p,a,q)$ tuple (paper / artifact-audit / forward question), the "audit changes the energy of the room - students stop performing summary and start performing judgment" insight, and the seminar-ledger item linking to Ch 58 frontier-watch. This is the best deepening block in the chapter.
**Lens 5**: Same topic-inappropriate boilerplate + experiment-exercise. Cut/replace.

#### Section 60.5: Lab infrastructure and compute budgeting for instructors - NEEDS WORK
**Lens 1/4**: Deepening good: compute-demand model $C_i=n_s(t_{cpu}+g_i t_{gpu})+c_i t_{cloud}$, CPU-safe / local-GPU / cloud-first classification, fallback paths (smaller model, shorter horizon, prerecorded logs), the $48 cloud-budget card. Practical and instructor-facing. Colab/dev-containers/Docker named.
**Lens 5**: Same boilerplate + experiment-exercise. Cut/replace.

#### Section 60.6: Assessment, rubrics, and academic-integrity notes for code assignments - NEEDS WORK
**Lens 1/4**: Deepening strong: rubric $G=w_t T+w_i I+w_e E+w_f F+w_r R$ with weighted card (0.20/0.30/0.25/0.15/0.10); the "grade the evidence trail, allow disclosed AI assistants but require defending the system" stance is current and exactly right for 2026. Custom hero illustration (60.6A) with real alt-text.
**Lens 5 (Teaching Flow)**: ISSUE - this section exists but is NOT listed in the part index (index.html shows Chapter 60 ending at 60.5) and the chapter index card lists only 60.1-60.5. Fix: add 60.6 to both the part index and the chapter roadmap. Same boilerplate + experiment-exercise issue.

## Cross-Chapter Issues in This Part
1. **Two-tier template across all of Ch 58, 59, 60 (29 of 32 sections).** Each section is ~50% topic-agnostic boilerplate (SectionContract dataclass, "What This Section Develops", closed-loop Theory paragraph, Practical Recipe, Common Failure Mode, templated Research Frontier and Self Check) followed by a good `Topic-Native Deepening` block. The boilerplate fails non-substitutability outright. Single biggest fix in the part.
2. **Broken/truncated worked-example code.** Every `SectionContract` print in 58-60 outputs truncated strings (slices like `[:64]`). These are not runnable results and look like bugs. Delete them; rely on the deepening blocks' real evidence-card code (which prints correctly).
3. **Evidence-artifact filler instead of real code.** The lean-section contract requires "one real worked example with correct topic-specific runnable code (no `plan = [skill for skill in skills]` filler)". The 58-60 SectionContract and most deepening `dict` cards are exactly that filler. The deepening cards are at least topic-specific, but several sections (notably 59.4 LeRobot) need actual runnable library code, not a manifest dict.
4. **Templated figure captions.** Most 58-60 figures use the caption "Section X: ... is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation." Identical across sections = boilerplate. 58.99 and 60.6 (custom alt-text) show the right pattern.
5. **Duplicate callouts in Chapter 56** (56.2, 56.3, 56.4 each repeat research-frontier / self-check / library-shortcut). Different defect from 58-60 but same cleanup discipline.
6. **Topic-inappropriate framing in Chapter 60.** The closed-loop $o_t\rightarrow a_t$ Theory paragraph and the "method-matched experiment / perturbation" Exercise are wrong for teaching/course-design topics.
7. **Stale indexes.** Part index and Ch 59/60 chapter cards do not match actual files: Ch 58 has a 58.99 (Frontier Watch) not listed; Ch 60 has a 60.6 (Assessment) not listed; the part overview still says "Chapters: 5. Each chapter includes ... a library shortcut, and exercises" generic text.
8. **Templated fun-notes.** The Memory Hook callouts in 58-60 rotate among three fixed strings; they add no per-topic value and should be either cut or rewritten per topic.

## Top 10 Highest-Priority Fixes for This Part
1. **Strip the boilerplate top half from all 29 sections of Ch 58-60** (`E:/Projects/Books/EmbodiedAI/part-12-frontiers-capstones-and-course-design/module-58-*/section-*.html`, `module-59-*/section-*.html`, `module-60-*/section-*.html`). Keep epigraph + figure + one framing paragraph, then promote `Topic-Native Deepening` to the section body. This single change moves most of the part from NEEDS WORK toward GOOD.
2. **Delete every broken `SectionContract` print block** across Ch 58-60 (the truncated-string outputs). Replace with nothing where a real deepening card already exists.
3. **Add real runnable LeRobot/OpenVLA fine-tune code to 59.4** (`module-59-capstone-projects/section-59.4.html`): dataset load, LoRA/adapter config, short train loop, and an eval call against the nominal/camera_shift/unseen split. This is the marquee hands-on capstone and currently has only a manifest dict.
4. **Fix Chapter 60 topic-inappropriate boilerplate** (`module-60-*/section-*.html`): remove the closed-loop $o_t\rightarrow a_t$ Theory paragraph and replace each "method-matched experiment / perturbation" Exercise with a real course-design task (sample given in 60.1 above).
5. **Dedupe Chapter 56 callouts** in 56.2, 56.3, 56.4 (`module-56-embodied-agents-with-memory/section-56.{2,3,4}.html`): keep one research-frontier, two distinct self-checks, one merged library-shortcut per section.
6. **Repair 59.12 double-body structure** (`module-59-capstone-projects/section-59.12.html`): merge the pre-deepening body and the deepening body into one; remove duplicated fun-note, self-check, research-frontier, key-takeaway, and the duplicated Exercise 59.12.1.
7. **Update stale indexes**: add 58.99 (rename to 58.6) and 60.6 to the part index (`part-12.../index.html`) and to the Ch 59/60 chapter roadmaps; rewrite the generic "Chapters: 5 ..." overview line to describe the actual deliverables table already present.
8. **Add the missing hero figure to 59.4** (or confirm/remove if intentional) so it matches the rest of Chapter 59.
9. **Rewrite or remove the templated Memory Hook fun-notes** in Ch 58-60; the epigraphs already carry the humor, so per-topic surprising facts (e.g. in 58.5, "a policy that succeeds 90% of short episodes can still have near-zero 20-minute reliability") would be a better engagement payoff.
10. **Replace templated figure captions** in Ch 58-60 with topic-specific captions following the 58.99 / 60.6 model.

## Structure Suggestions for This Part
- **Renumber 58.99 to 58.6.** "58.99" is a placeholder ID that leaks into the nav ("Section 58.99: Frontier Watch"). It is a legitimate sixth section of the chapter; give it a real number.
- **Chapter 59 is large (12 sections) and repetitive in structure.** After the boilerplate is stripped, consider grouping into thematic clusters in the index (navigation/search: 59.1-59.2; manipulation/VLA: 59.3-59.4; control/world-model: 59.5-59.6; safety/planning: 59.7-59.8; multi-robot/aerial: 59.9-59.10; meta: 59.11-59.12) rather than presenting 12 flat siblings. No merges required; the briefs are distinct.
- **Consider merging 60.2 and 60.3** (advanced-undergrad course and two-semester sequence) only if, after de-boilerplating, their deepening blocks overlap heavily; keep separate if each retains a distinct load profile and weekly arc. (Recommend keep-separate pending the de-boilerplate pass.)
- **Promote the part-index "Reader Deliverables" table** (already strong) into the lead of the part overview; it is the most substantive thing on the landing page and currently sits below generic filler.
