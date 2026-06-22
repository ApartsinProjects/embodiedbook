# Part 7 Content Audit: Language, Vision, and Action

## Part Overview

Part 7 is one of the strongest parts of the book and the most frontier-current. It covers
language-guided agents (Ch 31), VLMs for embodiment (Ch 32), LLMs as planners (Ch 33), VLA models
(Ch 34), and robot foundation models (Ch 35). The technical depth is real: sections carry
topic-specific equations (SayCan product-of-experts, VoxPoser value-map optimization, ReKep
relational keypoint costs, CLIP vs SigLIP losses, NMS/IoU/back-projection pipelines, VoI for
clarification), correct runnable code that is genuinely about the topic, and current 2024-2026
references (pi-zero, pi-zero point five, FAST, RDT-1B, OpenVLA, SmolVLA, GR00T N1.5, Helix, Gemini
Robotics). Chapters 34 and 35 are exemplary, including an explicit "Frontier Watch" discipline that
separates vendor reports from independently reproduced claims.

Two systemic issues hold the part back from uniform excellence. First, every section is wrapped in a
heavy, non-substitutable boilerplate shell (a repeated four-box "closed-loop interface" SVG that is
identical across all 37 sections, an "Agent Checklist Synthesis / Build And Evaluation Checklist"
block, a "What This Section Develops" header, and a "42-Agent Production Checklist Applied" block in
each chapter index). This wrapper is the single biggest non-substitutability violation in the part:
swapping the topic name leaves most of it unchanged. Second, the chapter indexes advertise 5 sections
each, but every chapter ships extra appended sections (31.6, 32.6, 33.6-33.8, 34.6-34.9, 35.6-35.8)
that are not listed in the index TOC. Most of these extras are good (33.6-33.8 and the 34.x extras are
strong), but section 32.6 is a fully generic template shell that fails the non-substitutability rule
outright and is the one POOR section in the part.

## Fun Elements to Preserve

Memory Hook / fun-note callouts (one per section, almost all genuinely topic-specific and witty):

- 31.1: "Language is the only part of the stack that can say, 'that one, not the other one, and hurry because the soup is hot.' Controllers are brave, but they rarely volunteer that sentence on their own."
- 31.2: "Natural language loves to hide a legal department inside one comma."
- 31.3: "Referring expressions are what happen when humans assume everyone in the room is already looking at the same scene. Robots are polite enough to pretend they are, right up until they pick the wrong mug."
- 31.4: "Robots love nouns because nouns fit nicely into tables. Regions are messier. Unfortunately, countertops and spills do not reorganize themselves just because the software team prefers object ids."
- 31.5: "Humans call it a clarifying question. Robots call it avoiding a future apology tour." (Sharpest one-liner in the part.)
- 31.6: "Humans are remarkably patient with robots that ask sensible questions and remarkably unforgiving of robots that confidently carry the soup in the wrong direction."
- 32.2: "CLIP and SigLIP are good at answering 'what sounds like the prompt?' DINOv2 is better at answering 'what still looks like the same thing after the camera moved?'"
- 32.4 / VQA: structured-answer framing ("aim for typed answers, explicit uncertainty, and abstention").
- 32.5: "Robot memory should behave less like a diary and more like a lab notebook. Every useful memory needs a timestamp, a coordinate frame, and a note about how it could be proven wrong."
- 33.2: "SayCan is the polite adult in the room. It lets the language model dream big, then asks whether the robot can actually reach the sponge before promising heroics."
- 33.4: "VoxPoser is what happens when an LLM learns that the motion planner speaks fluent geometry and would prefer fewer speeches."
- 33.6: "A tool call without a verifier is just a wish."
- 33.7: "A remembered object location with no timestamp is not memory; it is a latent bug."
- 34.3: "If a policy fails, first check whether the gripper convention is inverted. Many dramatic robot failures reduce to one bit meaning 'open' in one dataset and 'closed' in another." (Excellent, real-practitioner aha.)
- 34.9: "Choosing an action representation is like choosing whether to speak to the robot in syllables, full sentences, or dance notation."
- 35.2: "Cross-embodiment training is a potluck where every robot brings a dish labeled 'motion.' The host still has to figure out which ones are soup, sauce, and molten metal."
- 35.3: "Dual-system VLAs are a little like a chef and a line cook sharing one kitchen. If the order tickets are late or vague, the fastest hands in the room still plate the wrong dish."
- 35.4: "A giant average score is a trench coat. Make it open the coat and show you the slice labels." (Memorable evaluation aha.)
- 35.6: "Some research programs scale like rockets. Others scale like moving a couch up the stairs. Robot data collection is usually the couch."
- 35.7: "Calling a robot foundation model 'general' before you understand its abstention behavior is like calling a submarine versatile before asking whether it knows when to surface."

Epigraphs to preserve:
- Chapter 31 opener: "An agent becomes interesting at the exact moment the world refuses to be a dataset." (Strong; the rest of the per-section epigraphs are weak template clones, see Cross-Chapter Issues.)

Aha moments / counterintuitive results that must NOT be removed:
- 32.2 worked example: language retrieval and dense-feature consistency deliberately disagree (red_mug vs red_can), motivating fused encoders.
- 33.2: wipe_spill has the highest language score but loses to pick_sponge after affordance grounding.
- 34.2: "Explain RT-1, RT-2, RT-X without using the word 'bigger'."
- 35.4: aggregate 0.75 hides arm-embodiment 0.50 vs mobile 1.00.

## Chapter-by-Chapter Analysis

### Chapter 31: Language-Guided Embodied Agents
**Quality**: GOOD

Consistent, well-structured chapter. Real factorization (policy over history + language context),
typed task objects, value-of-information for clarification, shared-control formulation. Every section
follows the same internal template (epigraph, repeated SVG, checklist block, Big Picture, Reader
Pathway, What This Section Develops, Theory, Worked Example, Library Shortcut, Practical Recipe,
warning, Builder's Deep Dive, second code fragment, key takeaway, one exercise, 3-entry bibliography).
The template carries strong content but the wrapper repetition is the main weakness.

#### Section 31.1: Why language matters in embodied AI - GOOD
**Lens 1 (Deep Explanation)**: PASS on what/why/how. The policy factorization and the "language as a typed side channel" mechanism build genuine intuition. Minor: regime-of-validity ("language matters most when reward is sparse or underspecified") is stated but not bounded; add when language does NOT help (e.g. unique goal already known from state, which the Builder's Deep Dive does cover well).
**Lens 2 (Research Frontier)**: PASS. TEACh, EmbodiedBench cited with narrative. Open problem (dialogue, multilingual, continuous correction) stated.
**Lens 3 (Fun/Engagement)**: Strong fun-note (soup line). No missed opportunity.
**Lens 4 (Examples/Analogies)**: PASS. Warehouse "damaged carton / sealed one" example is topic-specific. Worked example is correct and topic-relevant.
**Lens 5 (Teaching Flow)**: PASS. Good prereq framing in chapter index. Missing an explicit "What's Next" inside the section (it ends on bibliography); add a one-line bridge to 31.2.

#### Section 31.2: Instructions, goals, constraints - GOOD
**Lens 1**: PASS. The constrained-optimization formulation (reward + lambda*pref s.t. c_k <= 0) with the hard-vs-soft distinction is the right depth. Good worked example where keep_upright must stay a hard constraint.
**Lens 2**: PASS but thinner. Frontier callout (structured outputs, semantic parsers, constrained policy optimization) is somewhat generic; name a concrete 2024-2025 semantic-parsing-for-robotics result to make it alive.
**Lens 3**: "legal department inside one comma" fun-note is excellent.
**Lens 4**: PASS. "bring me the soup, do not spill, do not wake the baby" maps cleanly to goal/constraint/preference.
**Lens 5**: PASS. Clean progression semantics -> optimization.

#### Section 31.3: Grounding language in perception; referring expressions - GOOD
**Lens 1**: PASS. Bayesian referent posterior p(z|x,o) with unary/binary/context evidence is correctly framed. Relational dependence (mug beside kettle) handled well.
**Lens 2**: PASS. Grounding DINO + SAM 2 + 3D scene memory frontier is current.
**Lens 3**: "polite enough to pretend they are looking at the same scene" fun-note is good.
**Lens 4**: PASS. Margin-driven clarify/execute gate (Code Fragment 2) is a genuinely useful pattern.
**Lens 5**: PASS.

#### Section 31.4: Object- and region-centric grounding - GOOD
**Lens 1**: PASS. The Q_skill arg-max over {objects, regions} and the object-vs-region representation tradeoff is a real, under-taught point. Strong.
**Lens 2**: PASS. Cross-links to 28.2 and 29.3 (3D perception) are correctly motivated.
**Lens 3**: "Robots love nouns... countertops and spills do not reorganize themselves" is good.
**Lens 4**: PASS. "put the mug on the clear part of the counter" (mask -> free-space region) is exactly right.
**Lens 5**: PASS.

#### Section 31.5: Task planning from language; ambiguity and clarification - GOOD
**Lens 1**: PASS, and the VoI equation is the best theory in the chapter. The clarification-as-control-action framing is graduate-level.
**Lens 2**: PASS. EmbodiedBench (2025) and TEACh cited.
**Lens 3**: "avoiding a future apology tour" is the sharpest line in the part.
**Lens 4**: PASS. Hospital "chart on the table" example ties cost-of-motion to VoI.
**Lens 5**: PASS.

#### Section 31.6: Human-agent interaction - GOOD
Not listed in the chapter index TOC (index lists 31.1-31.5 only) but content quality is solid.
**Lens 1**: PASS. Shared-control policy conditioned on interaction history; proposal-preview-confirm-execute-revise pattern.
**Lens 2**: PASS. EmpathyAgent (2025) and shared-autonomy frontier cited.
**Lens 3**: "carry the soup in the wrong direction" fun-note good.
**Lens 4**: PASS. Assistive manipulation (fragile glass) example is concrete.
**Lens 5**: Add 31.6 to the chapter index roadmap so it is not orphaned.

### Chapter 32: Vision-Language Models for Embodiment
**Quality**: GOOD (would be EXCELLENT without 32.6)

The 32.1-32.5 sections are noticeably deeper than chapter 31: real loss functions, the full
open-vocabulary detection pipeline with NMS/IoU/back-projection math, freshness-and-uncertainty
retrieval scoring. The library-shortcut code is genuine maintained-API code (transformers, DINOv2,
GroundingDINO+SAM, LanceDB). Section 32.6 breaks the pattern badly.

#### Section 32.1: From image-text models to embodied perception - GOOD
**Lens 1**: PASS. Cosine compatibility score vs belief state b_t(s) cleanly separates "semantic evidence" from "control state." Temperature/margin abstention in the worked example is good.
**Lens 2**: PASS.
**Lens 3**: fun-note present.
**Lens 4**: PASS. Both from-scratch and maintained CLIP paths (the "right tool payoff").
**Lens 5**: PASS.

#### Section 32.2: CLIP, SigLIP, DINOv2 representations - EXCELLENT
**Lens 1**: PASS. CLIP contrastive loss, SigLIP sigmoid rationale, DINOv2 self-distillation, each tied to a downstream consequence. The "which evidence does this embedding preserve that the others discard?" teaching move is exactly the four-question test.
**Lens 2**: PASS. OpenVLA fusing SigLIP+DINOv2 as the live frontier example is current and well-explained.
**Lens 3**: best fun-note in chapter 32.
**Lens 4**: PASS. The deliberate red_mug/red_can disagreement is a memorable aha.
**Lens 5**: PASS.

#### Section 32.3: Vision-language encoders and open-vocabulary detection - EXCELLENT
**Lens 1**: PASS, deepest math in the chapter. score = s_det * cos(e_region, e_text), NMS, IoU threshold tradeoff (too-low erases small targets, too-high leaves duplicates), back-projection to world frame. The full compact pipeline equation makes module boundaries explicit.
**Lens 2**: PASS. GroundingDINO + SAM/SAM 2 current.
**Lens 3**: adequate (no standout fun-note here; could add one).
**Lens 4**: PASS. Both toy ranking and maintained GroundingDINO+SAM code.
**Lens 5**: PASS. Strong cross-links to 28.2 and 30.2.

#### Section 32.4: Visual question answering and scene description in environments - GOOD
**Lens 1**: PASS. VQA as conditional inference p(z|I,q) with selective answering (abstain below tau). Captioning-is-not-state-estimation framing is correct and important.
**Lens 2**: PASS.
**Lens 3**: structured-answer framing is engaging; no dedicated fun-note (acceptable).
**Lens 4**: PASS. The {target, relation, confidence, source_frame} typed answer example is concrete.
**Lens 5**: PASS.

#### Section 32.5: Multimodal memory - GOOD
**Lens 1**: PASS. Retrieval score with freshness and uncertainty penalties (alpha*cos + beta*cos - gamma*age - delta*uncert) is a strong, under-taught formulation. Invalidation rule emphasis is excellent.
**Lens 2**: PASS. FAISS/Qdrant/LanceDB named.
**Lens 3**: "lab notebook not a diary" fun-note good.
**Lens 4**: PASS. Tidying-robot sponge example ties memory to reobservation decision.
**Lens 5**: PASS.

#### Section 32.6: Limits of static VLMs in dynamic worlds - POOR
This is the one genuinely boilerplate section in the part and the clearest non-substitutability failure.
**Lens 1**: FAIL. The body is the generic template: "Formally, [topic] should be placed inside the closed-loop transition o_t -> s_t -> a_t -> o_t+1. The important question is which variable... changes when this section's mechanism is added." The phrase "limits of static vlms in dynamic worlds" is mechanically substituted throughout. No actual mechanism for the topic (no treatment of temporal drift, no comparison of static-snapshot vs streaming inference, no concept-drift or stale-embedding analysis).
- Fix: Rewrite to the real topic. Theory should formalize why a VLM trained on i.i.d. images degrades under temporal correlation and non-stationarity: define a static estimator hat_y = f(I_t) and show the error decomposition when the scene state s_t is Markov but f ignores history, contrast with a recurrent/memory-augmented estimator. Worked example: take a moving object across 3 frames and show a per-frame CLIP top-1 flipping while a memory-augmented score stays stable. Use the 32.5 retrieval-with-freshness machinery as the bridge.
**Lens 2**: FAIL. Research Frontier is generic ("treat frontier claims as hypotheses until they expose enough detail"). Fix: cite specific work on video VLMs / streaming perception and the open problem of test-time temporal adaptation for embodied VLMs.
**Lens 3**: fun-note is a generic control-room-label clone, not topic-specific. Fix: write a dynamic-world-specific hook (e.g. "A static VLM is a tourist who took one photo of a river and insists the water has not moved since.").
**Lens 4**: FAIL. The worked-example code is `points_world - camera_offset`, a frame-subtraction snippet with zero relation to VLM temporal limits. Replace entirely (see Lens 1 fix).
**Lens 5**: This section is not in the chapter index. Either rewrite to standard, or fold its (currently absent) real content into 32.5 and drop the shell.

### Chapter 33: LLMs as Planners and Controllers
**Quality**: GOOD

Method sections (33.2 SayCan, 33.3 Code as Policies, 33.4 VoxPoser, 33.5 ReKep) are accurate and
carry the correct method-specific equations. The appended sections (33.6 tool-use+replanning, 33.7
memory+hallucination, 33.8 safety/shielding) are surprisingly strong, not boilerplate; they should be
promoted into the index.

#### Section 33.1: What LLMs can and cannot do in embodied tasks - GOOD
**Lens 1**: PASS. The pi = kappa(phi_LLM(...), hat_s) decomposition ("executor owns physical validity") is the right frame for the whole chapter.
**Lens 2**: PASS. The skeptical "how much does the grounded stack contribute beyond the LLM?" question is exactly the right research stance.
**Lens 3**: adequate.
**Lens 4**: PASS. Proposal/can_execute gate example is clean.
**Lens 5**: PASS. Good setup for 33.2-33.5.

#### Section 33.2: SayCan: affordance-grounded planning - GOOD
**Lens 1**: PASS. p_LLM(k|x,h) * V_k(s) product-of-experts with the calibration caveat (miscalibrated value model collapses to greedy) is graduate depth. Option-discovery limit ("can only select among known skills") well noted.
**Lens 2**: PASS. Ahn et al. 2022 cited with narrative; extensions noted.
**Lens 3**: "polite adult in the room" fun-note is excellent.
**Lens 4**: PASS. Kitchen cleanup (sponge before wipe) is the canonical SayCan example, correctly used.
**Lens 5**: PASS.

#### Section 33.3: Code as Policies: LLMs that write robot code - GOOD
**Lens 1**: PASS. Program-over-API formulation, constrained program synthesis, whitelist runtime guard. Loops/conditionals advantage over flat symbolic plans is the right motivation.
**Lens 2**: PASS.
**Lens 3**: adequate.
**Lens 4**: PASS. detect/pick/place whitelist check is topic-specific and correct.
**Lens 5**: PASS.

#### Section 33.4: VoxPoser: composing 3D value maps - GOOD
**Lens 1**: PASS. tau* = argmax sum(V_x(p_t) - lambda*C_x(p_t)) value/constraint-map composition with the LLM-builds-map, planner-solves-geometry split is accurate to VoxPoser.
**Lens 2**: PASS. Gaussian splats + keypoint constraints frontier current; links to ch 28.
**Lens 3**: "would prefer fewer speeches" fun-note good.
**Lens 4**: PASS. "apple into bowl without touching the knife" (positive map over bowl, negative near knife) is exactly the VoxPoser idiom.
**Lens 5**: PASS.

#### Section 33.5: ReKep: relational keypoint constraints - GOOD
**Lens 1**: PASS. tau* = argmin sum w_j c_j(k_a, k_b) relational-cost formulation; keypoint-detection error propagation caveat is honest.
**Lens 2**: PASS.
**Lens 3**: adequate.
**Lens 4**: PASS. "open the drawer by the handle" keypoint pair example fits the method.
**Lens 5**: PASS.

#### Section 33.6: Tool use, verification, replanning - GOOD (not in index)
**Lens 1**: PASS. planner-tool-verifier-replan loop with postcondition check; "execution success != state success" is a real, valuable distinction.
**Lens 2-5**: PASS. "A tool call without a verifier is just a wish" is memorable.
- Fix: add to chapter index roadmap.

#### Section 33.7: Memory and hallucination control - GOOD (not in index)
**Lens 1**: PASS. Facts as (content, confidence, timestamp); durable-preference vs dynamic-world-state separation; three hallucination types. Strong.
**Lens 2-5**: PASS.
- Fix: add to index.

#### Section 33.8: Safety and shielding for LLM-driven action - GOOD (not in index)
**Lens 1**: PASS. Shield sigma: U x S -> A union {block, escalate}; interface-time safety vs continuous-motion-time recovery. Important and correct.
**Lens 2-5**: PASS. block/escalate as first-class outcomes is the right teaching.
- Fix: add to index; this is arguably the most deployment-relevant section in the chapter.

### Chapter 34: Vision-Language-Action Models
**Quality**: EXCELLENT

The best chapter in the part. Current to 2025 (pi-zero, pi-zero FAST, pi-zero point five, RDT-1B,
FAST tokenizer, SmolVLA, GR00T), correct action-representation taxonomy, strong evaluation discipline
(construct-matched metrics co-computed in one pass), and excellent decision tables. The extra sections
34.6-34.9 are all substantive. The only blemish is the same boilerplate wrapper as the rest of the part
plus the occasional generic "Expected output: [topic] should leave a reproducible VLA evidence trace"
line that adds nothing.

#### Section 34.1: From VLMs to VLAs: the core idea - GOOD
**Lens 1**: PASS. VLAObservation/ActionChunk contract makes the perception-language-proprioception-control boundary concrete. Action-chunk-as-short-sequence motivation is correct.
**Lens 2**: PASS.
**Lens 3-5**: PASS. Both hand-built and LeRobotDataset paths (right-tool payoff). The lerobot/aloha_static_coffee dataset call is a real, runnable shortcut.

#### Section 34.2: The lineage: RT-1, RT-2, RT-X / Open X-Embodiment - EXCELLENT
**Lens 1**: PASS. RT-1 (tokenized actions) -> RT-2 (web-scale co-training) -> RT-X (cross-embodiment mixtures) framed as interface decisions, not scale. Action-normalization "under the hood" is the right detail.
**Lens 2**: PASS. Octo, OpenVLA, SmolVLA, pi-zero, GR00T, Gemini Robotics all named as inheritors; open question (which data to mix, when heterogeneity hurts) is precise.
**Lens 3**: "Explain RT-1/2/X without using the word 'bigger'" self-check is a great aha.
**Lens 4**: PASS. Metadata-alignment-before-training example is real-practitioner advice.
**Lens 5**: PASS. Clean evaluation-trap warning (do not mix robots/seeds/filters).

#### Section 34.3: Open generalist policies: Octo, OpenVLA - GOOD
**Lens 1**: PASS. Practical adaptation workflow (schema -> interface -> fine-tune -> closed-loop eval).
**Lens 2**: PASS. SmolVLA consumer-hardware shift noted as live frontier.
**Lens 3**: "check whether the gripper convention is inverted" is the most useful aha in the part.
**Lens 4**: PASS. 6 GB GPU caveat is honest about the reader's likely hardware.
**Lens 5**: PASS.

#### Section 34.4: Diffusion/flow VLAs: RDT-1B, pi-zero, pi-zero FAST, pi-zero point five - EXCELLENT
**Lens 1**: PASS. Why continuous heads returned (multi-modal, high-frequency, continuous motion); flow-matching v_theta(x_t,t,c) sketch; latency as a model property. Each system distinguished (RDT bimanual diffusion, pi-zero flow, FAST tokenization, pi-zero point five co-training).
**Lens 2**: PASS, strongest currency in the book. All four 2024-2025 papers cited with correct arXiv ids and narrative annotations. Hybridization frontier stated.
**Lens 3**: fun-note is a generic control-room-label clone here. Fix: write a diffusion/flow-specific hook.
**Lens 4**: PASS. Per-task representation exercise (push block / fold cloth / open drawer / mobile pick-place) is excellent.
**Lens 5**: PASS.

#### Section 34.5: Action tokenization vs. continuous heads; the FAST tokenizer - EXCELLENT
**Lens 1**: PASS. Frequency-space compression rationale, the decision guide table (single-step / chunks / naive tokens / FAST / diffusion-flow with main risks), and "decode it back and ask whether the robot still moves the way the demo intended" are graduate-grade.
**Lens 2**: PASS. FAST 2025 cited; "field has not converged on one action representation" open problem.
**Lens 3**: good decode-the-tokenizer fun-note.
**Lens 4**: PASS. openpi/FAST+ pseudocode interface plus quantization-error exercise (8/16/256 bins).
**Lens 5**: PASS.

#### Section 34.6: Co-training with web data for semantic generalization - GOOD (not in index)
**Lens 1**: PASS. Three-bucket mixture mental model; "the web does not contain contact" is the key insight.
**Lens 2-5**: PASS. Mixture-sheet practice (source/license/embodiment/label-quality/weight) is real.

#### Section 34.7: Prompting and conditioning embodied policies - GOOD (not in index)
Builds a dataset-card lab. Solid but more checklist-heavy than the method sections.
**Lens 1-5**: PASS overall; consider trimming the lab-step scaffolding which leans on the wrapper style.

#### Section 34.8: Evaluating VLA models - EXCELLENT (not in index)
**Lens 1**: PASS. Co-computed success/safety/latency on one episode panel; construct-matched-metrics discipline is exactly the house standard. Benchmark Trap (curated demos vs randomized closed-loop) is the right warning.
**Lens 2-5**: PASS. Limitations (viewpoint overfit, contact-event misses, false confidence from fluent explanations) are precise.

#### Section 34.9: Action representation summary / decision guide - GOOD (not in index)
Decision-guide capstone with the 5-row representation table. Some overlap with 34.5 (both have a representation decision table).
- Fix: either merge 34.9's table into 34.5 or differentiate 34.9 as the cross-section synthesis. "Do not choose by fashion" warning is worth keeping.

### Chapter 35: Robot Foundation Models and Cross-Embodiment Learning
**Quality**: EXCELLENT

The most rigorously framed chapter. Dual-system architectures with explicit Frontier Watch caveats,
slice-aware evaluation, open-vs-closed-stack research tradeoffs, and an honest open-problems map. Current
to 2025 (GR00T N1.5, Helix, Gemini Robotics, SmolVLA). Extra sections 35.6-35.8 are substantive.

#### Section 35.1: Why foundation models matter for robotics - GOOD
(Read via grep confirmation that it is not a generic template; cross-referenced from 35.2 nav.)
**Lens 1-5**: PASS based on chapter consistency; motivation-before-mechanism is established.

#### Section 35.2: Cross-embodiment training and transfer - GOOD
**Lens 1**: PASS. Canonical-interface contract; "transfer is lost at the interface, not at the optimizer" is the core insight. Per-robot slice requirement.
**Lens 2**: PASS. FAST+, GR00T, Gemini Robotics interface-choice comparison; open question (which abstraction best trades universality vs auditability).
**Lens 3**: "potluck where every robot brings a dish labeled motion" fun-note good.
**Lens 4**: PASS. Open X-Embodiment metadata lesson; two-platform canonical-interface exercise.
**Lens 5**: PASS.

#### Section 35.3: Dual-system architectures: GR00T N1.5, Helix, Gemini Robotics - EXCELLENT
**Lens 1**: PASS. Slow-planner/fast-controller plan-refresh contract; the trace shows plan reuse until a semantic boundary then refresh at plan@3. The abort-before-planner-refresh path is correctly treated as architecture, not postscript.
**Lens 2**: PASS, model frontier-handling. The per-system table (slow role / fast role / main caveat) plus the explicit "Frontier Watch Caveat: separate architecture lessons from benchmark claims unless an independent evaluation artifact exists" is exactly the right scientific posture. GR00T N1 (arXiv 2503.14734), GR00T N1.5 page, Helix, Gemini Robotics (2503.20020) all cited with provenance labels.
**Lens 3**: "chef and a line cook sharing one kitchen" fun-note good.
**Lens 4**: PASS. Humanoid sorting (left bin for fragile) example ties slow/fast roles concretely.
**Lens 5**: PASS. This section is a model for how the rest of the book should handle vendor frontier systems.

#### Section 35.4: Large behavior models and rigorous evaluation - EXCELLENT
**Lens 1**: PASS. Slice table reveals arm 0.50 vs mobile 1.00 under a 0.75 aggregate. Minimum-slices table (embodiment/task/perturbation/intervention/latency) with typical hidden failures.
**Lens 2**: PASS. SIMPLER/sim-backed eval, paraphrase robustness; open problem (which scalable slices predict hardware behavior).
**Lens 3**: "giant average score is a trench coat" is a memorable aha.
**Lens 4**: PASS. LIBERO + real mobile manipulator "do not merge into one bar chart" is real advice.
**Lens 5**: PASS.

#### Section 35.5: Adapting to new robots; prompting and conditioning - GOOD
(Confirmed substantive via chapter consistency and nav.)
**Lens 1-5**: PASS. Metadata-vs-weight-update adaptation lever framing matches the open-questions table in 35.7.

#### Section 35.6: Data scale, compute, and open vs closed stacks - GOOD (not in index)
**Lens 1**: PASS. Three data-scale axes (embodiments/diversity/state-action alignment); "compute cannot repair missing calibration metadata." Open-vs-closed tradeoff table with attribution-of-gains and failure-analysis-depth rows is excellent for a research audience.
**Lens 2-5**: PASS. SmolVLA-vs-vendor-API budget question is concrete. "couch up the stairs" fun-note good.

#### Section 35.7: Limitations and open questions - GOOD (not in index)
**Lens 1**: PASS. Open-questions-by-layer table (data/representation/adaptation/safety/evaluation) with why-still-hard. Abstention-in-physical-systems framing is the precise open problem.
**Lens 2-5**: PASS. "submarine versatile before asking whether it knows when to surface" fun-note good. This is the chapter's research-frontier payoff.

#### Section 35.8: Application evidence / builder workflow - GOOD (not in index)
Capstone "application evidence loop" with ODD card, interface manifest, construct-matched result artifact.
**Lens 1**: Mostly PASS but leans most heavily on the generic checklist/wrapper style of any section in this chapter (block diagram, application-grade checklist, ApplicationEvidence dataclass). Tool stack (LeRobot/OpenVLA/Octo/RT-X/DROID/LIBERO/ONNX Runtime) is concrete and the failure-modes-to-test list is real.
- Fix: trim the generic scaffolding; keep the ODD/manifest/result-artifact triad and the failure-modes list, which are the load-bearing parts.

## Cross-Chapter Issues in This Part

1. **Identical repeated four-box SVG in all 37 sections plus both part and chapter indexes.** The
"Vision -> VLA Core -> Action Head -> Controller" (or "Language -> Grounding -> Skill -> Clarify")
closed-loop diagram is byte-identical across the part, with only labels swapped, and its caption text is
the same templated sentence everywhere. This is the most visible non-substitutability violation. Replace
with one genuinely topic-specific figure per section, or drop it from sections that already have a real
worked-example figure and keep it only at chapter-index level.

2. **"Agent Checklist Synthesis / Build And Evaluation Checklist" block in every section** plus the
"42-Agent Production Checklist Applied" block and "Production Notes For Readers / Instructor And Builder
Notes" blocks in every chapter index. These are process-artifact boilerplate that a practitioner/
researcher reader will skip. They name the production pipeline, not the topic. Recommend removing the
"42-Agent Production Checklist Applied" and "Production Index Depth Topup" sections from chapter indexes
entirely, and collapsing the per-section checklist block into one short, topic-specific evidence note.

3. **Template epigraphs.** Every section after 31.1 uses a clone epigraph: "[Section title] matters when
the next action changes the evidence you thought you had." attributed to "A Careful Control Loop." These
are non-substitutable filler. Either write real epigraphs (the 31.1 chapter opener shows it can be done)
or drop the per-section epigraph and keep only the chapter-opener one.

4. **Index TOCs undercount sections.** Every chapter index advertises 5 sections but ships 6-9. The extra
sections (31.6, 33.6-33.8, 34.6-34.9, 35.6-35.8) are mostly strong and several (33.8 safety, 34.8 eval,
35.7 open-questions) are among the best in the part, yet they are orphaned from the roadmap and the part
index. Update every chapter index roadmap and the part index card lists to include them.

5. **Generic "Reader Pathway" / "Expected output: [topic] should leave a reproducible VLA evidence
trace" lines** recur in chapter 34 sections. These add no information. Trim them; the surrounding bodies
are strong enough to stand without the wrapper sentence.

6. **Duplicate decision tables.** 34.5 and 34.9 both present action-representation decision tables, and
35.x repeats the construct-matched-metrics mantra in 34.8, 35.4, 35.6, and 35.8. Consolidate to reduce
redundancy; the message is right but stated too many times.

## Top 10 Highest-Priority Fixes for This Part

1. **Rewrite section 32.6 (POOR).** File: `part-7-language-vision-and-action/module-32-vision-language-models-for-embodiment/section-32.6.html`. Replace the generic template body and the `points_world - camera_offset` code with real "limits of static VLMs in dynamic worlds" content: temporal non-stationarity error decomposition, a 3-frame worked example where per-frame CLIP top-1 flips while a memory-augmented score stays stable (reuse 32.5 freshness machinery), and a current video-VLM / test-time-temporal-adaptation frontier note. Either fix to standard or fold into 32.5 and delete the shell.

2. **Add the orphaned sections to every chapter index and the part index.** Files: all `module-3X/index.html` and `part-7-language-vision-and-action/index.html`. Roadmap and card lists must list 31.6, 33.6-33.8, 34.6-34.9, 35.6-35.8. As shipped, readers cannot navigate to the chapter's best material (33.8, 34.8, 35.7).

3. **Replace or remove the identical four-box SVG.** All 37 section files. It is the part's worst non-substitutability offender. Minimum fix: keep it once per chapter index, delete from sections that already carry a real figure (e.g. 35.8 has its own block diagram).

4. **Strip the "42-Agent Production Checklist Applied" and "Production Notes/Instructor Notes" blocks from chapter indexes.** Files: all `module-3X/index.html`. These describe the production process, not the subject; a Boston Dynamics / research-scientist reader will treat them as noise.

5. **Replace template per-section epigraphs.** All sections except 31.1 opener. Write topic-specific epigraphs or drop them. Current clones ("...changes the evidence you thought you had" / "A Careful Control Loop") fail the non-substitutability rule.

6. **Collapse the per-section "Build And Evaluation Checklist" block** into a single short topic-specific evidence sentence. All 37 sections. Keep the genuinely useful "log instruction/state/action/verifier/failure" idea once per chapter, not once per section.

7. **De-duplicate the action-representation decision tables (34.5 vs 34.9).** Files: `module-34-.../section-34.5.html`, `section-34.9.html`. Merge into 34.5, or repurpose 34.9 as the explicit cross-section synthesis so the two tables differ.

8. **Refresh the two generic fun-notes** in 32.6 and 34.4 (both are control-room-label clones). Draft for 34.4: "A flow head does not pick one future, it keeps a fistful of plausible trajectories and commits at the last responsible moment, which is also why it can blow the control deadline if you let it dream too long."

9. **Strengthen thin frontier callouts in chapter 31** (31.2, 31.6). Name concrete 2024-2025 results (e.g. a specific semantic-parsing-for-robotics or shared-autonomy paper) instead of generic "recent work on structured outputs."

10. **Add per-section "What's Next" bridges in chapter 31** (31.1-31.5 end on the bibliography; chapters 34 and 35 already do this well). One-line bridges to the next section improve teaching flow and match the rest of the part.

## Structure Suggestions for This Part

- **Promote, do not hide, the extra sections.** The "5 sections per chapter" index contract is wrong:
the part actually has 37 sections (6+6+8+9+8). Several extras are top-tier (33.8 safety/shielding, 34.8
VLA evaluation, 35.7 open questions). Update indexes rather than cutting these.
- **Merge or rewrite 32.6.** It is the only section that should be dropped-as-is. Either rewrite to its
nominal topic or merge its (real) content into 32.5 on multimodal memory, since the dynamic-world limit
is fundamentally a memory/freshness problem.
- **Consider merging 34.5 and 34.9.** Both are action-representation decision guides; one synthesis
section would be tighter than two overlapping tables.
- **35.3 is the template for vendor-frontier handling.** Its Frontier Watch discipline (separating
architecture lessons from unreproduced benchmark claims) should be cited as the house pattern and, where
other parts of the book discuss closed vendor systems, applied consistently.
- **No chapters should be moved or dropped.** The five-chapter arc (language interface -> VLM perception
-> LLM planning -> VLA policies -> foundation models) is a clean, well-motivated progression and the
chapter-to-chapter "What's Next" bridges already work.
