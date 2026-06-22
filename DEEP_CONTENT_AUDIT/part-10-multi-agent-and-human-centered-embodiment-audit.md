# Part 10 Content Audit: Multi-Agent and Human-Centered Embodiment

## Part Overview

Part 10 covers three high-value chapters (Multi-Agent Embodied AI, Human-Robot Interaction, Open-World and Lifelong Embodiment) across 16 sections. Every section follows a rigid two-layer template: a large boilerplate top half (a templated epigraph, "What This Section Develops", a generic "Theory" placeholder, a filler "Worked Example" with throwaway `EmbodiedStep` code, a per-section `EvidenceRecord` filler block, and an identical 5-row tool table) wrapped around a genuinely strong "Technical Core" block at the bottom that carries real topic-specific equations, a topic-native algorithm, a runnable interpretive code fragment, and a topic-matched comparison table. The Technical Core blocks and the witty "Memory Hook" fun-notes are the best content in the part and lift most sections to GOOD; the boilerplate top halves are pure non-substitutable filler and are the dominant defect. The single highest-leverage fix for the entire part is to delete or replace the templated front matter (the placeholder Theory paragraphs, the `EmbodiedStep` worked example, and the `EvidenceRecord` code) so the strong Technical Core moves up to where the reader hits it first.

## Fun Elements to Preserve

The "Memory Hook" fun-notes are the standout asset of this part. Every one is topic-specific, witty, and accurate. Preserve all of them verbatim:

- 49.1: "A second robot is not a free performance upgrade; it is also a second opinionated body in the hallway."
- 49.2: "A message that never changes an action is just a robot group chat with better timestamps."
- 49.3: "Shared perception is not a democracy; a bad timestamp should not get an equal vote."
- 49.4: "A team reward can be a beautiful hiding place for one very lazy policy."
- 49.5: "Emergence is impressive until the fire exit becomes a group project."
- 50.1: "A hallway robot that is technically correct can still be socially terrible."
- 50.2: "A robot that hears every word but ignores the hallway is just a chatbot on wheels."
- 50.3: "Overtrust is what happens when a progress bar wears a lab coat."
- 50.4: "An explanation that cannot change a decision is just a receipt for confusion."
- 50.5: "Shared autonomy is not backseat driving if the backseat has the better obstacle sensor."
- 50.6: "A robot cannot apologize its way out of a data-retention policy."
- 51.1: "A closed-world benchmark is a tidy kitchen; deployment is the drawer where somebody put batteries, tape, and one mysterious screw."
- 51.2: "A mug with no handle is still a cup until the grasp planner files a complaint."
- 51.3: "A long-horizon task is a short task that invited all its dependencies to dinner."
- 51.4: "Catastrophic forgetting is the robot equivalent of learning a new recipe and forgetting where the kitchen is."
- 51.5: "A robot memory system needs a junk drawer, but it also needs the courage not to train on everything in it."

These 16 hooks are the strongest engagement layer in the part. None should be removed.

Also worth preserving: the "aha" interpretive sentences that follow each Technical Core code fragment (for example 49.2's "the extra 128 broadcasts buy only three additional reward points", 49.4's held-out-partner brittleness reading, 50.1's "extra 1.2 seconds nearly doubles clearance"). These turn raw numbers into a teaching moment and are the closest thing the part has to genuine worked examples.

## Chapter-by-Chapter Analysis

### Chapter 49: Multi-Agent Embodied AI
**Quality**: GOOD

The Technical Core blocks here are strong: 49.1 has a clean centralized-vs-decentralized factorization with a partner-dropout coordination-gap audit, 49.2 ties communication to an information-economics utility and a gain-per-message audit, 49.3 uses a real assignment LP, 49.4 covers CTDE plus partner-holdout evaluation, 49.5 uses a boids update rule with order parameters. The chapter is dragged down by the universal boilerplate front matter.

#### Section 49.1: One agent vs. many - GOOD
**Lens 1 (Deep Explanation)**:
- The "Theory" section is a placeholder: "One agent vs. many should be placed inside the closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$. The important question is which variable... changes." This is non-substitutable boilerplate (swap the topic name and nothing changes). The actual theory (the $J(\Pi)$ objective, the centralized-vs-decentralized factorization) is buried in the Technical Core 130 lines later.
- Fix: Delete the placeholder "Theory" and "Mechanism" callout. Promote the Technical Core "Formal Object" to be the section's Theory, and lead with: "A multi-agent task factorizes the joint policy. A centralized controller $\pi(a^{\mathrm{joint}}\mid o)$ coordinates globally but its action space grows as $\prod_i |A_i|$; a decentralized family $\{\pi_i(a_i\mid o_i,m_i)\}$ scales linearly and matches physical deployment but only preserves performance when local observations plus messages retain action-critical information. The factorization decision is therefore an information-sufficiency test, not a style choice."

**Lens 2 (Research Frontier)**:
- The "Research Frontier" callout is generic ("decentralized execution, emergent communication, language-mediated coordination"). No dated 2024-2026 work, no named open problem.
- Fix: Add a precise open problem: "Open question (2024-2026): ad-hoc teamwork with foundation-model agents. Can a policy trained with self-play coordinate zero-shot with a never-seen human or LLM-driven partner? See the Melting Pot 2.0 (2023) and ad-hoc teamwork literature; current methods still show large held-out-partner regret."

**Lens 3 (Fun/Engagement)**:
- Present and excellent: Memory Hook "A second robot is not a free performance upgrade..."; Misconception Check (single-point-dependence diagnostic). Both preserve.
- Opportunity: the warehouse two-manipulator example could earn a Boston Dynamics Stretch / Kiva-style anchor.

**Lens 4 (Examples/Analogies)**:
- The top "Worked Example" code (`EmbodiedStep("one_agent_vs_many", "act", "observe consequence")`) is pure filler and violates the no-`plan = [skill for skill in skills]` rule. The real worked example is the Technical Core dropout-audit fragment. Cut the filler.
- The Technical Core fragment (coordination_gap 0.02 vs 0.31) is a genuine, correct, topic-specific worked example. Strong.

**Lens 5 (Teaching Flow)**:
- Reader hits two placeholder "Theory"/"Mechanism" callouts and a filler code block before any real content. Cognitive load is wasted on boilerplate. Reorder so Technical Core leads.

#### Section 49.2: Cooperation, competition, communication - GOOD
**Lens 1**:
- Same placeholder "Theory" defect. The real content (utility with message cost $u_i = r_i - \lambda c(m_i)$) is excellent and belongs up front.
- Fix: Lead with the message-cost utility and the value-of-message principle: a message is worth sending only when its marginal effect on the joint action exceeds $\lambda c(m_i)$.

**Lens 2**:
- Frontier callout names "learned communication, language as a coordination medium, opponent modeling" but no dated landmark. 
- Fix: Add "Open question: emergent-communication protocols rarely transfer to new partners (the 'language drift' problem). Whether discrete autoencoder-style messages or natural-language channels generalize better across partner populations is unresolved."

**Lens 3**:
- Memory Hook "A message that never changes an action is just a robot group chat with better timestamps" is one of the best in the part. Preserve. Misconception Check (fewer-bits diagnostic) preserve.

**Lens 4**:
- Filler `EmbodiedStep` example. The Technical Core gain-per-message audit (intent_bit 1.5 vs full_broadcast 0.15) is a correct, memorable worked example. Cut the filler, keep the audit.

**Lens 5**: Same reorder need. Otherwise builds logically from 49.1.

#### Section 49.3: Shared perception and task allocation - GOOD
**Lens 1**:
- Placeholder Theory. Real content (the assignment ILP $\min \sum c_{ij}x_{ij}$ with constraints, map-fusion-then-assign pipeline) is solid graduate depth.
- Minor: the ILP formulation as written has an asymmetry ($\sum_j x_{ij}\le 1$ vs $\sum_i x_{ij}=1$) that is correct for "every task assigned, agents may idle" but is not explained. Add one sentence: "the inequality lets agents stay idle while the equality forces every task to be claimed exactly once."

**Lens 2**:
- Frontier (multi-robot scene graphs, decentralized mapping) is reasonable but undated. Add: "Open question: maintaining a consistent shared scene graph under communication dropout and clock skew, for example Hydra-style 3D scene graphs across multiple robots, remains open for dynamic scenes."

**Lens 3**: Memory Hook "Shared perception is not a democracy; a bad timestamp should not get an equal vote" is excellent. Preserve.

**Lens 4**: Filler `EmbodiedStep`. Technical Core cost-matrix assignment fragment is correct and topic-native. The follow-up failure attribution (wrong pose vs stale travel-time vs false skill claim) is good teaching.

**Lens 5**: Good once reordered.

#### Section 49.4: Multi-agent RL (with PettingZoo) - GOOD
**Lens 1**:
- Placeholder Theory. Real content names the three coupled MARL difficulties (non-stationarity, credit assignment, partner generalization) and CTDE; this is correct and well chosen.
- The "Formal Object" pairs a per-agent Q-function with a policy-gradient expression but does not connect them; a one-line bridge ("centralized critic estimates $\hat A$ from joint information while each $\pi_i$ stays decentralized") would tighten it.

**Lens 2**:
- Frontier (self-play, centralized critics, population training, foundation-model priors) is current-ish. Add a named open problem: "Open question: zero-shot human-AI coordination (Overcooked-AI, Hanabi). Population-based training improves held-out-partner play but no method reliably matches human-human teamwork."

**Lens 3**: Memory Hook "A team reward can be a beautiful hiding place for one very lazy policy" is excellent and reinforces the lazy-agent / credit-assignment point. Preserve. Misconception Check (one agent coasting) preserve.

**Lens 4**: Filler `EmbodiedStep`. Technical Core same_partner vs held_out_partner panel (entropy 0.42 -> 0.11, collisions 1 -> 6) is a genuinely instructive worked example of partner overfitting. Strong.

**Lens 5**: This is the most "alive" section in the chapter once the boilerplate is stripped.

#### Section 49.5: Swarms and emergent behavior; evaluating teams - GOOD
**Lens 1**:
- Placeholder Theory. Real content (boids-style velocity update plus an alignment order parameter $\Phi$, and a density/dropout robustness sweep) is correct and topic-native.

**Lens 2**:
- Frontier (scalable coordination, embodied collectives, differentiable simulators, sim-to-real for many bodies) is good. Add: "Open question: sim-to-real for large physical swarms is still gated by communication and localization, not by the local rule; resilience to Byzantine or silently-failing agents is largely untested on hardware."

**Lens 3**: Memory Hook "Emergence is impressive until the fire exit becomes a group project" is excellent. Preserve.

**Lens 4**: Filler `EmbodiedStep`. Technical Core density-sweep audit (low/medium/high coverage and collisions) with the "medium density is best" interpretation is a correct, memorable worked example.

**Lens 5**: Good. Closes the chapter on evaluation, which is the right capstone.

### Chapter 50: Human-Robot Interaction
**Quality**: GOOD

The strongest chapter for topic-native Technical Cores: 50.1 uses a legibility-plus-proximity multi-objective cost, 50.2 a Bayesian instruction-grounding model with a clarify-vs-execute margin rule, 50.3 a belief update plus trust-error metric, 50.4 a counterfactual value-drop explanation selector, 50.5 a dynamic authority-blending law $u_t=\alpha_t u^{human}+(1-\alpha_t)u^{robot}$, 50.6 an operational ethics review loop. These are real HRI mechanisms, not name-drops. Same boilerplate-front-matter problem throughout.

#### Section 50.1: Robots among humans - GOOD
**Lens 1**:
- Placeholder Theory. Real content (the multi-objective cost $J(\tau)=\ell_{task}+\lambda_1\ell_{prox}+\lambda_2\ell_{legibility}$ and the human-aware-vs-shortest-path trade) is good.
- Fix: Lead with the multi-objective cost and the human-factors framing (legibility, protected interpersonal zones, recoverability).

**Lens 2**:
- Frontier (embodied language, social navigation, user trust, long-term adaptation) is generic. Add a named open problem: "Open question: social navigation lacks a standardized benchmark; SocialNav / SEAN-style simulators disagree on metrics, so 'comfort' is rarely comparable across papers."

**Lens 3**: Memory Hook "A hallway robot that is technically correct can still be socially terrible" is excellent. The Dragan legibility reference is well chosen.

**Lens 4**: Filler `EmbodiedStep`. Technical Core shortest_path vs human_aware fragment (clearance 0.34 -> 0.79, comfort 2.1 -> 4.5) is a correct, motivating worked example. Could anchor to a real hospital-delivery robot (Diligent Moxi, Aethon TUG).

**Lens 5**: Good once reordered. Strong chapter opener.

#### Section 50.2: Natural-language interaction and social navigation - GOOD
**Lens 1**:
- Placeholder Theory. Real content (the grounding factorization $p(g,z\mid w,o)\propto p(w\mid g)p(g\mid z,o)p(z\mid o)$ and the clarify-vs-execute margin) is genuinely good and is the right way to teach grounding-vs-language-modeling.

**Lens 2**:
- Frontier mentions VLMs, navigation policies, dialogue managers but no dated landmark. Add: "Open question: VLM-grounded navigation (for example NaVILA, 2024-era VLN-CE follow-ups) still fails on referential ambiguity and negation ('do not block the nurse'); robust constraint grounding is unsolved."

**Lens 3**: Memory Hook "A robot that hears every word but ignores the hallway is just a chatbot on wheels" is excellent. Misconception Check (which physical constraint each phrase changed) is sharp.

**Lens 4**: Filler `EmbodiedStep`. Technical Core clarify-vs-execute margin fragment (margin 0.08 -> clarify) is a correct, useful worked example. The grounding-error table is topic-native.

**Lens 5**: Good. Builds correctly on 50.1.

#### Section 50.3: Intent recognition and trust calibration - GOOD
**Lens 1**:
- Placeholder Theory. Real content (Bayesian belief update $b_{t+1}(i)\propto p(o_t\mid i)b_t(i)$ plus trust error $|\hat p_{success}-p_{success}|$) correctly separates the two estimation problems (robot estimating human vs human estimating robot). This is the cleanest framing in the chapter.

**Lens 2**:
- Frontier is thin. Add: "Open question: trust calibration over long deployments. Trust both decays after errors and inflates after streaks of success; no deployed controller reliably keeps a user's reliance matched to the robot's true conditional success rate."

**Lens 3**: Memory Hook "Overtrust is what happens when a progress bar wears a lab coat" is one of the best in the part. Misconception Check (higher trust is not always better) is correct and important.

**Lens 4**: Filler `EmbodiedStep`. The belief-update / trust-error pairing is the worked content; confirm the Technical Core code fragment instantiates both (it does, per the algorithm loop).

**Lens 5**: Good. Strong link from 50.2 (clarification) into trust.

#### Section 50.4: Explainable robot behavior - GOOD
**Lens 1**:
- Placeholder Theory. Real content (top-k value-drop explanation selector $e_t=\arg\,\mathrm{topk}_k \Delta V_k$, where $\Delta V_k = V(s_t)-V(s_t\setminus\text{factor}_k)$) is a genuine, well-chosen counterfactual-explanation mechanism. This is graduate depth done right.

**Lens 2**:
- Add open problem: "Open question: faithfulness of robot explanations. Value-drop and saliency explanations can be plausible yet not causal; verifying that an explanation reflects the policy's true decision factors is unsolved for learned visuomotor policies."

**Lens 3**: Memory Hook "An explanation that cannot change a decision is just a receipt for confusion" is excellent and reinforces the actionability test. Misconception Check (longer is not better) is correct.

**Lens 4**: Filler `EmbodiedStep`. Technical Core counterfactual event-trace is topic-native. The three-message refusal Mini Lab (vague/technical/action-ready) is a strong concrete exercise.

**Lens 5**: Good. Connects naturally to trust (50.3) and feedback (50.5).

#### Section 50.5: Human feedback and shared autonomy - GOOD
**Lens 1**:
- Placeholder Theory. Real content (the authority-blending law $u_t=\alpha_t u^{human}+(1-\alpha_t)u^{robot}$ with $\alpha_t=f(\sigma_t,\rho_t,\kappa_t)$) is the correct shared-autonomy formulation (Dragan-Srinivasa policy-blending lineage). Strong.
- Fix: Add one sentence connecting $\alpha_t$ to the classic result that blending should track the robot's confidence in its prediction of the human goal, not a fixed slider.

**Lens 2**:
- Add: "Open question: shared autonomy under learned goal predictors. When the robot's goal estimate is a neural net with miscalibrated uncertainty, naive confidence-based blending can amplify errors; calibrated authority arbitration is open."

**Lens 3**: Memory Hook "Shared autonomy is not backseat driving if the backseat has the better obstacle sensor" is excellent. Misconception Check (autonomy is not a fixed slider) is the core insight.

**Lens 4**: Filler `EmbodiedStep`. The five-state authority machine Mini Lab is concrete and topic-native. Anchor opportunity: assistive teleoperation (wheelchair-mounted arms, NASA/space teleop) is a real-system example.

**Lens 5**: Good. Strong link from explanation (50.4) into authority allocation.

#### Section 50.6: Ethical concerns - GOOD
**Lens 1**:
- Placeholder Theory. Real content (operational ethics review loop: stakeholders, data types, harm channels, mitigation, logging, escalation owner) correctly treats ethics as engineering constraints rather than a postscript. This is the right framing for a practitioner audience.

**Lens 2**:
- Frontier should reference current regulation context (EU AI Act risk tiers, evolving robot-safety standards) as a dated anchor. Add open problem: "Open question: auditable accountability for learned policies. When a deployed robot harms or excludes a user, attributing the cause to data, objective, or update remains technically hard; reproducible incident forensics for continually-updated policies is unsolved."

**Lens 3**: Memory Hook "A robot cannot apologize its way out of a data-retention policy" is excellent. Misconception Check (ethics is not a final review) is the load-bearing point.

**Lens 4**: Filler `EmbodiedStep`. The HRI risk-register Mini Lab is concrete and reusable.

**Lens 5**: Good chapter capstone. Connects the chapter's accountability theme.

### Chapter 51: Open-World and Lifelong Embodiment
**Quality**: GOOD

The most technically substantive chapter once you reach the Technical Cores: 51.1 frames open-world as the right-to-abstain (open-set gate $\max_k \hat p_k \ge \tau$), 51.2 uses affordance embeddings for novelty, 51.3 a receding-horizon subgoal value function, 51.4 an explicit EWC-style retention regularizer $\ell_{retention}=\|\theta-\theta^\star\|_\Omega^2$, 51.5 a selective-retrieval memory model. These are correct, current, and topic-native. Same boilerplate-front-matter defect.

#### Section 51.1: Closed- vs. open-world tasks - GOOD
**Lens 1**:
- Placeholder Theory. Real content is excellent: "The defining difference between closed-world and open-world tasks is not model size, it is the right to abstain." The open-set gate ($\max_k \hat p_k \ge \tau$, otherwise abstain and query) is the correct formalization. This sentence should be the section opener.

**Lens 2**:
- Frontier (OOD detection, embodied foundation models, adaptive policies) is reasonable. Add: "Open question: calibrated abstention for embodied policies. OOD detectors tuned on vision benchmarks degrade under embodiment-specific shift (lighting, viewpoint, novel dynamics); when to abstain vs explore is unresolved."

**Lens 3**: Memory Hook "A closed-world benchmark is a tidy kitchen; deployment is the drawer where somebody put batteries, tape, and one mysterious screw" is the best in the part. Preserve.

**Lens 4**: Filler `EmbodiedStep`. Technical Core open-set gate is topic-native worked content. The two-panel familiar/shifted-object Mini Lab is concrete.

**Lens 5**: Strong chapter opener once reordered. The "right to abstain" framing carries the whole chapter.

#### Section 51.2: Novel objects and instructions; changing environments - GOOD
**Lens 1**:
- Placeholder Theory. Real content (affordance-first action $a_t=\pi(o_t,\phi(x_t),g_t)$ with $\phi$ an affordance embedding) correctly argues that reasoning over affordances beats reasoning over object names. Good graduate depth.

**Lens 2**:
- Frontier names VLM priors, open-vocabulary perception, object-centric memory. Add: "Open question: affordance transfer to truly novel objects. Open-vocabulary detectors name new objects well but predict graspable affordances poorly; closing the recognize-vs-manipulate gap is open."

**Lens 3**: Memory Hook "A mug with no handle is still a cup until the grasp planner files a complaint" is excellent and precisely illustrates the recognize-vs-afford gap. Preserve.

**Lens 4**: Filler `EmbodiedStep`. The novelty table (new object / new wording / changed layout, each with detection/question/action/fallback) is a strong topic-native artifact.

**Lens 5**: Good. Builds on 51.1's abstention into active novelty handling.

#### Section 51.3: Long-horizon tasks - GOOD
**Lens 1**:
- Placeholder Theory. Real content (subgoal-conditioned value $V^\pi(s_t,g_{1:H})$ plus receding-horizon replanning with verification and repair) correctly identifies error compounding and the need for subgoals plus monitoring, not just longer context.

**Lens 2**:
- Add: "Open question: verifier reliability for long-horizon robot plans. LLM/VLM progress-verifiers hallucinate success; grounding subgoal-completion checks in perception rather than language is unresolved."

**Lens 3**: Memory Hook "A long-horizon task is a short task that invited all its dependencies to dinner" is excellent. Misconception Check (longer context does not solve long-horizon control) is the key correction.

**Lens 4**: Filler `EmbodiedStep`. The six-step household plan with one missing precondition plus per-step verifier/recovery is a genuinely good exercise.

**Lens 5**: Good. The verification-and-repair theme links forward to continual learning.

#### Section 51.4: Continual learning and catastrophic forgetting - GOOD
**Lens 1**:
- Placeholder Theory. Real content is the strongest in the chapter: the explicit retention-regularized update $\theta_{t+1}=\theta_t-\eta\nabla_\theta(\ell_{new}+\beta\ell_{retention})$ with $\ell_{retention}=\|\theta-\theta^\star\|_\Omega^2$. This is the EWC / Fisher-weighted formulation done correctly, and the framing "in robotics, forgetting can become a safety problem" is exactly the right practitioner motivation.
- Minor: name the regularizer family ("this is the elastic-weight-consolidation form; $\Omega$ is a Fisher-information importance matrix") so readers can connect it to the literature.

**Lens 2**:
- Frontier (replay, regularization, modular policies, parameter-efficient updates) is current. Add: "Open question: plasticity-stability under foundation-model finetuning. Parameter-efficient adapters reduce forgetting but cap plasticity; the right trade for continually-deployed robot policies is unsolved."

**Lens 3**: Memory Hook "Catastrophic forgetting is the robot equivalent of learning a new recipe and forgetting where the kitchen is" is excellent. Misconception Check ("which old skill paid the price?") is the load-bearing insight.

**Lens 4**: Filler `EmbodiedStep`. The three-task retention panel with a rollback rule is a strong, concrete artifact.

**Lens 5**: Good. The natural payoff of the chapter's safety-under-change theme.

#### Section 51.5: Memory and experience replay; open-world evaluation - GOOD
**Lens 1**:
- Placeholder Theory. Real content (memory $\mathcal M_t=\{e_k\}$ with selective retrieval $q_t=\mathrm{Retrieve}(\mathcal M_t,o_t,g_t)$) correctly argues that retrieval selectivity, not capacity, is what makes memory useful, plus the open-world-evaluation hygiene point.

**Lens 2**:
- Frontier (episodic memory, retrieval-augmented policies, continual RL, lifelong benchmarks) is current. Add: "Open question: stale-memory detection. Retrieval-augmented policies have no reliable way to know a stored episode is no longer valid after the environment changed; safe memory invalidation is open."

**Lens 3**: Memory Hook "A robot memory system needs a junk drawer, but it also needs the courage not to train on everything in it" is excellent and reinforces the selective-retrieval point. Preserve.

**Lens 4**: Filler `EmbodiedStep`. The memory audit card (stored episode, retrieval reason, action effect, stale-memory test, replay sample, retention metric) is a strong topic-native artifact.

**Lens 5**: Good part capstone. Ties memory, replay, and evaluation hygiene together, which is the right close for the part's "log every adaptation" contract.

## Cross-Chapter Issues in This Part

1. **Identical templated front matter in all 16 sections.** Every section has a placeholder "What This Section Develops" sentence, a placeholder "Theory" paragraph ("should be placed inside the closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$"), a placeholder "Mechanism" callout, and a filler "Worked Example" with `EmbodiedStep(...)` code. All are fully non-substitutable boilerplate. This is the dominant defect of the part.

2. **The `EvidenceRecord` filler code block appears in all 16 sections**, identical except for the section number and tool name, with placeholder string values ("record after the perturbation run: sensor or state input"). This violates the lean-section "no filler code" rule. It adds ~25 lines of zero-information code per section.

3. **The 5-row "Practical Tool Choices For This Section" table is identical within each chapter** and lists the same tool in the "Role in the Topic" column for every row (literally repeating the section title five times). The "Role" column carries no information.

4. **Duplicated chapter epigraph.** All three chapter index pages use the identical epigraph "An agent becomes interesting at the exact moment the world refuses to be a dataset." and the identical "Big Picture matters because embodied intelligence is no longer a solo loop here" sentence. Differentiate per chapter.

5. **Duplicated section epigraph pattern.** All 16 section epigraphs are "[Section title] matters when the next action changes the evidence you thought you had." attributed to "A Careful Control Loop." This is a missed opportunity: each section has a great Memory Hook that would make a far better epigraph.

6. **Generic illustration captions.** Every Figure NN.NA caption is the same template ("is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation").

7. **Identical Technical Core SVG diagram in all 16 sections** (Assumptions -> Model -> Algorithm -> Evidence -> Failure, with "multi-agent and human-centered embodiment" hardcoded in the Model box for every section, including all of chapter 50 and 51). The diagram is decorative, not topic-specific.

8. **Frontier callouts lack dated (2024-2026) landmarks and precise open problems.** The real research papers (MADDPG/Lowe 2017, PettingZoo 2021, Goodrich survey 2007, Dragan legibility 2013) are pre-2022. No current frontier work is cited with narrative context.

9. **No "What's Next" transition at section level.** Sections end on a bibliography + nav bar; the motivated handoff to the next section is missing (chapter indexes have it, sections do not).

## Top 10 Highest-Priority Fixes for This Part

1. **Strip the placeholder "Theory" + "Mechanism" callouts in all 16 sections and promote each section's Technical Core "Formal Object" to be the real Theory.** This single change converts the part from "boilerplate wrapping real content" to "real content first." Files: all `section-*.html` in modules 49, 50, 51. Replace lines ~54-60 with the Formal Object equation and its surrounding 2-3 sentences (already written in each Technical Core).

2. **Delete the filler "Worked Example" `EmbodiedStep` code block in all 16 sections** (e.g. 49.1 lines 61-78) and re-label the Technical Core code fragment as the section's worked example. The Technical Core fragments are already correct, runnable, and topic-specific.

3. **Delete the `EvidenceRecord` filler code block in all 16 sections** (e.g. 49.1 lines 129-155). It is identical placeholder code with no per-topic value and violates the lean-section contract.

4. **Replace each section epigraph with that section's Memory Hook.** Example for 49.4: change "Multi-agent RL (with PettingZoo) matters when the next action changes the evidence you thought you had." to "A team reward can be a beautiful hiding place for one very lazy policy." This instantly makes 16 generic epigraphs into 16 memorable ones using content that already exists.

5. **Add a dated open problem to every Research Frontier callout.** Concrete drafts supplied per section above (e.g. 49.4 zero-shot human-AI coordination on Overcooked-AI/Hanabi; 51.4 plasticity-stability under foundation-model finetuning; 50.2 VLM-grounded navigation failing on negation). Files: all 16 sections.

6. **Make the "Practical Tool Choices" table's middle column informative.** Replace the repeated section-title text with the actual role each tool plays for that specific topic. For 49.4 the PettingZoo row should say "AEC/Parallel APIs that expose turn order and per-agent observations" not "Multi-agent RL (with PettingZoo)." Files: all 16 sections.

7. **Differentiate the three chapter epigraphs and Big Picture sentences.** modules 49/50/51 `index.html` lines 38, 43. Give chapter 50 an HRI-specific epigraph, chapter 51 a lifelong-learning-specific one, instead of the shared "world refuses to be a dataset" line.

8. **Name the literature behind the strong equations.** 51.4: identify $\ell_{retention}=\|\theta-\theta^\star\|_\Omega^2$ as elastic weight consolidation with $\Omega$ a Fisher-information matrix. 50.5: identify the blending law as policy-blending shared autonomy (Dragan-Srinivasa lineage). Files: section-51.4.html, section-50.5.html Technical Core.

9. **Anchor 2-3 worked examples to real systems.** 50.1 hospital-delivery robot -> name Diligent Moxi / Aethon TUG. 49.1 warehouse manipulators -> Kiva/Amazon Robotics. 50.5 shared autonomy -> assistive teleoperation. Adds the practitioner credibility the Boston Dynamics / Waymo audience expects. Files: section-50.1.html, section-49.1.html, section-50.5.html.

10. **Replace the identical Technical Core SVG** (which hardcodes "multi-agent and human-centered embodiment" in the Model box for every section) with either a per-section topic label in the Model box or removal in favor of the topic-specific comparison table that already follows it. Files: all 16 sections.

## Structure Suggestions for This Part

- **No chapters or sections should be dropped, merged, or moved.** The three-chapter split (multi-agent coordination / human-in-the-loop / open-world lifelong) is coherent, the section ordering within each chapter builds logically, and every section maps to a distinct, well-chosen topic. The part's scope is correct for the stated audience.

- **The defect is depth-of-execution, not structure.** Each section already contains a strong, correct, topic-native Technical Core; the fix is to remove the templated scaffolding that buries it, not to reorganize the part.

- **Consider one part-level addition:** a short "Coordination, Humans, and Change" synthesis at the end of 51.5 or in the part index that explicitly threads the three chapters through the part's stated "log every handoff or adaptation event" contract, since that contract is asserted in the part index but never revisited at the end.

- **Section-level "What's Next" links** should be added (one sentence each) to match the chapter-index pattern, improving the teaching flow called out in Lens 5.
