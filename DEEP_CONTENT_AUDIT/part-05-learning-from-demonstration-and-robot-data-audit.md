# Part 5 Content Audit: Learning from Demonstration and Robot Data

## Part Overview

Part 5 is the data-and-imitation spine of the book and contains some of the strongest material in the whole project (Chapters 23 and 24) sitting next to some of the most template-bound (Chapters 21, 25, 26). The substantive content is genuinely good throughout: every section carries at least one real equation (BC objective with O(T^2 epsilon) compounding, ACT cVAE loss, MaxEnt IRL, relative SE(3) actions, per-embodiment normalization, mixture temperature sampling, offline support penalty, options/skill discovery mutual-information objective) plus a small inspectable code fragment. The problem is not depth, it is three different page templates of very different quality wrapped around that depth. The biggest single defect is mechanical title-substitution boilerplate: in Chapter 21 every section repeats an identical "What This Section Develops / Theory / Worked Example / Builder's Deep Dive / Agent Checklist" shell where the only thing that changes is the section title spliced into otherwise-static sentences, and in Chapters 25 and 26 the "Big Picture" paragraph is byte-for-byte identical across all five sibling sections. Cutting that boilerplate (not the depth blocks) is the single highest-leverage fix for the part.

Three template families are in use:
- **Template A (heavy/boilerplate)**: Chapter 21. One good `course-depth-block` buried inside a large generic shell with title substitution. Worst non-substitutability score.
- **Template B (lean/strong)**: Chapters 23, 24. Frame, one or two real theory sub-headings, one real worked example, comparison tables, named open problems, real labs. This is the model the rest of the part should converge to.
- **Template C (mid, repetitive)**: Chapters 22, 25, 26. Real depth block plus repeated diagrams and identical sibling paragraphs. Chapter 22 leans toward B; 25 and 26 lean toward A.

## Fun Elements to Preserve

Strong, genuinely witty section epigraphs (mostly in Chapters 23 and 24; these are the best fun elements in the part and must survive any edit):

- **23.1**: "A robot dataset is not a pile of videos. It is a memory of what the body was allowed to try."
- **23.2**: "The best joystick for an arm is sometimes another arm that admits it is only pretending."
- **23.3**: "I collected the demonstration in a kitchen. The robot insists it has never been to one."
- **23.4**: "The operator wanted depth perception. The robot delivered a network delay with excellent lighting."
- **23.5**: "Every dataset has a junk drawer. The question is whether you labeled it."
- **23.6**: "The folder looked organized until the policy asked which camera was the wrist camera."
- **24.1**: "A million trajectories sound large until you ask how many robot bodies they remember."
- **24.2**: "The policy read the video. The researcher read the license. Only one of them was ready to ship."
- **24.3**: "The robot arms agreed to share data. Their grippers asked to see the contract."
- **Chapter 21 / 22 index epigraph**: "An agent becomes interesting at the exact moment the world refuses to be a dataset."

Memorable analogies and "aha" callouts to keep:
- 23.1 "Coverage, Not Count" and the product-space combinatorics ("a thousand beautiful clips from one kitchen may still fail in a second kitchen").
- 23.2 "Interface Quality Becomes Label Quality" (a bad teleop interface injects noise into imitation targets).
- 23.5 "Failures Are Typed Evidence" and "Pitfall: Clean Data Can Be Too Clean."
- 22.1 "Temporal Intent" (a chunk is a compact declaration of near-future intent).
- 24.1 "Dataset Size Is Multidimensional."
- 21.2 "Distribution Before Architecture."

Fun gaps: Chapters 25 and 26 have NO witty epigraph (they all reuse the generic "A Careful Control Loop" cite) and almost no humor. They are the dullest reading in the part and should borrow the 23/24 epigraph style.

## Chapter-by-Chapter Analysis

### Chapter 21: Imitation Learning
**Quality**: NEEDS WORK (strong depth blocks trapped in heavy boilerplate)

The five depth blocks are good graduate-level content. Everything around them is the heaviest boilerplate shell in the part: identical "What This Section Develops", "Theory" (same two sentences with title spliced in), "Worked Example" (the same `dataset_root.glob("episode_*")` filler code in all five sections), "Builder's Deep Dive", identical EvidenceRecord dataclass repeated five times, identical "Practical Tool Choices" table listing Gymnasium/PettingZoo/ROS 2/MuJoCo/LeRobot with the same cell text in every row, and identical "Agent Checklist Integration" tables. The chapter index also contains a stray typo: "For , the practical stack should be introduced..." (empty placeholder where the topic name should be).

#### Section 21.1: Why learning from demonstration matters for robots - NEEDS WORK
**Lens 1 (Deep Explanation)**: Depth block PASSES (trajectory definition tau=(o0,a0,...), expert visitation d_E(o) vs learner d_pi(o), the metadata-contract code). But the surrounding shell fails the four-question test: "Theory" says only "should be placed inside the closed-loop transition... The important question is which variable... changes" with no actual theory. Fix: delete the generic "Theory"/"Mechanism"/"Worked Example" trio and promote the `course-depth-block` to be the section body; the glob filler code (Code Fragment 21.1.1) adds nothing the metadata-check code (Code Fragment 3) does not do better.

**Lens 2 (Research Frontier)**: The generic "Research Frontier" callout is content-free ("treat frontier claims as hypotheses until they expose enough detail"). Fix: replace with a concrete 2024-2026 thread, e.g. "Open question: given a fixed teleop budget, can a learned data-value model predict which next demonstration most reduces closed-loop failure? Active demonstration selection (DROID, RoboMIND curation) is unsolved at scale."

**Lens 3 (Fun/Engagement)**: Present: "fun-note" Memory Hook, "Distribution Before Architecture" key-insight. Missing: a real hook; the epigraph is the auto-generated "Why X matters when the next action changes the evidence" pattern, weaker than the 23/24 epigraphs. Opportunity: open with the ALVINN-to-Mobile-ALOHA arc as a one-line surprise.

**Lens 4 (Examples/Analogies)**: Metadata-contract example is good and topic-specific. The "Practical Tool Choices" table (Gymnasium/PettingZoo for an imitation-learning section) is wrong-topic filler: PettingZoo is multi-agent RL, irrelevant here. Fix: replace with LeRobot/robomimic/imitation library rows.

**Lens 5 (Teaching Flow)**: Self-check cross-links (Ch 14, 23, 34) are good. But the section is roughly 60% boilerplate by length, which buries the one good idea and inflates cognitive load.

#### Section 21.2: Behavior cloning; the distribution-shift problem - GOOD
**Lens 1**: PASS. Best section in the chapter. Real BC objective, MSE/NLL/cross-entropy by action type, the O(T^2 epsilon) compounding-error result with intuition, and a numeric BC-loss-to-5cm-offset demonstration. The hands-on lab (EpisodeCard schema, CSV audit, library shortcut) is real and runnable.

**Lens 2**: The generic Research Frontier callout is still filler. Fix: name the current thread, e.g. "implicit BC / energy-based policies and action-chunking as partial covariate-shift mitigations; the open question is whether chunking trades covariate shift for staleness."

**Lens 3**: Present: "Compounding Error" warning (great), "Held-Out Task Evaluation" practical-example, fun-note. These are strong; keep.

**Lens 4**: PASS. Numeric example is topic-specific and well chosen.

**Lens 5**: PASS, though the lab plus the generic Builder's Deep Dive plus Agent Checklist is redundant; the lab alone is enough.

#### Section 21.3: DAgger and dataset aggregation - GOOD
**Lens 1**: PASS. D_{k+1} aggregation equation, the no-regret/online-learning reduction stated correctly, clear pseudocode, the cost framing (cheap in sim, expensive with humans, safety-critical on hardware). The provenance-tracking code (policy version per queried state) is a genuinely good engineering point.

**Lens 2**: The depth block names the right library (`imitation` on Stable-Baselines3). Generic Research Frontier callout still filler. Fix: add "SafeDAgger / EnsembleDAgger and human-gated intervention learning (HG-DAgger, Sirius) are the active threads; open question is minimizing expert queries under a hard safety budget."

**Lens 3**: fun-note present but weak ("makes X visible twice"). Opportunity: a witty line about the expert getting tired of being asked.

**Lens 4**: PASS. Provenance code is topic-specific.

**Lens 5**: PASS.

#### Section 21.4: Inverse reinforcement learning - GOOD
**Lens 1**: PASS. MaxEnt IRL trajectory distribution P_phi(tau) proportional to exp(sum r_phi), the reward-ambiguity point made concrete (cup-carrying could optimize path length, stability, comfort, or habit), and a two-reward-weight code example showing the expert vs shortcut ranking flip under counterfactuals. The "Reward Learning Frontier" callout here is actually specific (identifiability) - keep it.

**Lens 2**: This section has the best frontier callout in the chapter (the identifiability open problem). Still has the redundant generic one lower down; delete the generic duplicate.

**Lens 3**: fun-note present. The counterfactual-ranking-flip is a genuine aha moment; preserve and maybe foreground it.

**Lens 4**: PASS. The shortcut-vs-expert feature example is topic-specific and clever.

**Lens 5**: PASS. Good bridge to reward learning and preferences.

#### Section 21.5: Sources of demonstrations: humans, planners, foundation models - GOOD
**Lens 1**: PASS. The three-source audit table (human teleop / motion planner / foundation model with strength, risk, best-use) is genuinely useful, and the provenance-scorecard code (hardware/coverage/audit scores) makes the "different sources answer different needs" point concretely.

**Lens 2**: Generic frontier callout. Fix: name 2024-2026 reality - VLA-generated and simulation-distilled demonstrations (RT-2, Open X, AgiBot World), the open problem of grounding/filtering foundation-model action proposals before they enter robot datasets.

**Lens 3**: Source-audit table is the engagement payload. fun-note weak. The "human_teleop and planner_sim tie at 7 but mean different things" is a nice aha; keep.

**Lens 4**: PASS. Topic-specific.

**Lens 5**: PASS. Good transition to Chapter 22.

### Chapter 22: Action Chunking and Diffusion Policies
**Quality**: GOOD (strong depth blocks, Template-A boilerplate shell still present but content is the richest in the part)

Seven sections, each with a real depth block. The boilerplate shell (same as Chapter 21) is still wrapped around them and should be trimmed, but the depth blocks here are the most technically current material in Part 5.

#### Section 22.1: Why single-step prediction fails on real manipulation - GOOD
**Lens 1**: PASS. Single-step a_t vs chunk A_t=(a_t,...,a_{t+H-1}), receding-horizon execution, mode-averaging and jitter motivation. The "execute only first part of chunk, then replan" code is the right intuition. Could add the actual variance/multimodality argument (why MSE regression collapses bimodal action distributions to their mean).

**Lens 2**: Missing a frontier callout entirely in the depth block. Fix: add "open question: optimal chunk horizon is task- and latency-dependent; learned adaptive horizons are an active thread."

**Lens 3**: "Temporal Intent" callout is a good aha. Keep.

**Lens 4**: The string-list chunk example ("reach","align","close","lift","retreat") is illustrative but toy; consider a numeric end-effector trajectory to match the rest of the chapter's rigor.

**Lens 5**: PASS. Strong motivating opener for the chapter.

#### Section 22.2: ACT and the cVAE formulation - GOOD
**Lens 1**: PASS. Full ACT loss with L1 reconstruction + beta-weighted KL, correct cVAE framing (encoder maps chunk to z, decoder predicts chunk from obs+z), temporal-ensembling recipe and weighted-average code. This is accurate and well explained.

**Lens 2**: Names LeRobot's ACT policy. No explicit open problem. Fix: "open question: how much of ACT's success is the cVAE vs simply the chunking + ensembling? Ablations disagree."

**Lens 3**: "Temporal Ensembling Recipe" is concrete and memorable.

**Lens 4**: PASS. The three-overlapping-chunks weighted-ensemble numeric example is exactly right.

**Lens 5**: PASS, bridges to ALOHA in 22.3.

#### Section 22.3: ALOHA, ALOHA 2, and Mobile ALOHA - GOOD
**Lens 1**: PASS. Frames ALOHA as a coupled data-system (hardware + teleop + synchronized cameras + ACT policy), and makes the key point that model quality and collection interface are inseparable. Real systems content (Boston Dynamics / DeepMind audience will value the data-system framing).

**Lens 2**: Could cite ALOHA Unleashed / ALOHA 2 hardware specifics and the cost-democratization angle. Mostly current.

**Lens 3**: Bimanual task audit (zipper, drawer, cable routing) is concrete and engaging.

**Lens 4**: PASS. Real-system grounding.

**Lens 5**: PASS. Explicitly tells the reader to read with Chapter 23, which is correct.

#### Section 22.4: Diffusion Policy: action generation by denoising - GOOD
**Lens 1**: PASS (depth block present). The noising/denoising objective and receding-horizon connection are the right content. Verify the DDPM loss is written with the standard epsilon-prediction form and that the sampler latency tradeoff (DDIM steps) is mentioned.

**Lens 2**: Diffusion Policy is current; should mention consistency-model / one-step distillation as the latency frontier.

**Lens 3**: Denoising-as-action-generation is inherently a nice aha; ensure it is foregrounded.

**Lens 4**: PASS.

**Lens 5**: PASS, bridges naturally to flow matching in 22.5.

#### Section 22.5: Flow matching for actions - GOOD
**Lens 1**: PASS. Flow matching as fast continuous-path generation under latency budgets is the right 2024-2026 framing (pi0 / flow-matching VLAs). Confirm the vector-field / ODE-integration explanation is present, not just named.

**Lens 2**: This is genuinely frontier (pi0, 2024). Strong currency. Name pi0 explicitly as the landmark.

**Lens 3**: Integrator-error/extrapolation watch-for is a good practitioner note.

**Lens 4**: PASS.

**Lens 5**: PASS.

#### Section 22.6: VQ-BeT and discretized behavior modeling - GOOD
**Lens 1**: PASS. Action tokenization, codebook coverage, precision-loss audit. The "tokens must still correspond to meaningful robot motions" caution is the right depth.

**Lens 2**: Could connect to action-tokenization in VLAs (RT-2, OpenVLA, FAST tokenizer 2024). Add that link.

**Lens 3**: Codebook-collapse failure mode is a good concrete pitfall.

**Lens 4**: PASS.

**Lens 5**: PASS, leads into the decision guide.

#### Section 22.7: Choosing an action representation: a decision guide - GOOD
**Lens 1**: PASS. The Action Representation Decision Matrix (one-step / ACT / diffusion / flow / discrete with use-when and watch-for) is exactly the synthesis a practitioner needs. The horizon-scoring code makes the latency tradeoff explicit.

**Lens 2**: PASS as a synthesis section.

**Lens 3**: "the best representation is the one that fits those constraints, not the one with the most fashionable name" is a good memorable line.

**Lens 4**: PASS. Decision matrix is the highlight.

**Lens 5**: Excellent capstone for the chapter.

### Chapter 23: Teleoperation and Data Collection
**Quality**: EXCELLENT (the strongest chapter in the part; lean Template B throughout)

Six sections, all with witty epigraphs, real equations, topic-specific runnable code, named open problems, and two genuine hands-on labs (23.3, and the format work in 23.6). This chapter should be the template the rest of Part 5 converges to.

#### Section 23.1: Why data is the bottleneck - EXCELLENT
**Lens 1**: PASS. Product-space coverage argument (|O||P||B||S||H| not the sum), the engineering-object-vs-supervised-object distinction, real coverage-counting code. Graduate depth with stated assumptions.
**Lens 2**: PASS. Names Open X, DROID, BridgeData V2, UMI, Mobile ALOHA and states the open problem precisely ("predict which additional episode is worth collecting next").
**Lens 3**: Best epigraph in the part; "Coverage, Not Count" aha. PASS.
**Lens 4**: PASS. Dishwasher-loading and second-kitchen examples are concrete.
**Lens 5**: PASS. Functions as the motivation for all of Part 5; the "Robot Data Bottlenecks" table is excellent.

#### Section 23.2: Leader-follower teleoperation (ALOHA, GELLO) - EXCELLENT
**Lens 1**: PASS. Affine joint-space calibration q_F=S(q_L-q_L^0)+q_F^0, latency math at 50 Hz vs 5 Hz, the latency-budget audit code that labels episodes clean vs latency-risk.
**Lens 2**: PASS. Open problem stated (standardize interface-quality metadata so cross-device demonstrations can be pooled).
**Lens 3**: PASS. Great epigraph; "Interface Quality Becomes Label Quality" and "Ergonomics Hides In The Dataset" are memorable.
**Lens 4**: PASS. Real systems (ALOHA, GELLO, Mobile ALOHA).
**Lens 5**: PASS. Daily-calibration-gate protocol is a real artifact.

#### Section 23.3: Handheld and in-the-wild collection (UMI) - EXCELLENT
**Lens 1**: PASS. Relative SE(3) trajectory representation Delta x = (T_t^-1 T_{t+1}, ...), why relative actions reduce frame dependence, 1-D inspectable code that scales to SE(3).
**Lens 2**: PASS. Open problem: how far portability extends as tasks become deformable/force-sensitive (missing tactile/compliance).
**Lens 3**: PASS. Excellent epigraph; "Portable Does Not Mean Uncalibrated."
**Lens 4**: PASS. Towel-folding-in-many-kitchens example.
**Lens 5**: PASS. Real hands-on lab (manifest audit, readiness rule).

#### Section 23.4: Immersive/VR teleoperation (Open-TeleVision) - EXCELLENT
**Lens 1**: PASS. Human-in-the-loop control framing, latency decomposition Delta t = camera+encode+network+render+control, episode-labeling code by delay/frames/tracking.
**Lens 2**: PASS. Open problem: does active visual feedback yield more policy data per minute once cost/training/latency are included?
**Lens 3**: PASS. Strong epigraph; "Presence Is Not Ground Truth" pitfall.
**Lens 4**: PASS. Cupboard-opening active-gaze example; names Open-TeleVision, ROS 2, Kalibr/OpenCV.
**Lens 5**: PASS. Note: the depth-block code variable `stable_video` combines dropped_frames<=3 and tracking>=0.95 (source is correct; an earlier extraction artifact made it look like an assignment bug). No fix needed, but worth a quick render check.

#### Section 23.5: Data quality, diversity, and labeling - EXCELLENT
**Lens 1**: PASS. Weighted quality score Q(e)=w_s S+w_c C+w_t T+w_l L-w_i I, the three-truth-layers framing (intended/executed/environment), routing code (train/stress/repair).
**Lens 2**: PASS. Open problem: active data selection without overfitting a benchmark.
**Lens 3**: PASS. Best junk-drawer epigraph; "Failures Are Typed Evidence", "Label Leakage" pitfall.
**Lens 4**: PASS. Bin-picking validation-split example.
**Lens 5**: PASS. Annotation schema and quality-gate protocol are real artifacts.

#### Section 23.6: (Dataset format / LeRobotDataset) - EXCELLENT
**Lens 1**: PASS. Four-question format contract, feature schema validation code, raw/normalized/training three-layer pipeline, random-access replay as the key verification.
**Lens 2**: PASS. Open problem: queryable robot experience (find episodes by language/failure/embodiment without custom parsers).
**Lens 3**: PASS. "A Loader Is A Scientific Instrument", "Unit Drift" pitfall.
**Lens 4**: PASS. GELLO raw-leader-vs-follower-target example.
**Lens 5**: PASS. Clean bridge into Chapter 24.

### Chapter 24: Robot Datasets and Data Scaling Laws
**Quality**: EXCELLENT (lean Template B; current dataset coverage)

#### Section 24.1: The major datasets - EXCELLENT
**Lens 1**: PASS. Five-axis dataset-reading framework (embodiments/scenes/tasks/annotations/splits), coverage-proxy code, source-aware failure analysis.
**Lens 2**: PASS. Names Open X-Embodiment, DROID, BridgeData V2, RoboNet, RH20T, RoboMIND, AgiBot; RT-X open problem (pooling requires more than tokenizing observations because embodiments change the action space). Very current. Note: RH20T and AgiBot World appear in the chapter index but are lightly covered in 24.1 body; worth a sentence each.
**Lens 3**: PASS. Great epigraph; "Dataset Size Is Multidimensional."
**Lens 4**: PASS. Kitchen-generalization vs body-transfer vs language-tabletop examples.
**Lens 5**: PASS. "Choosing A Dataset" algorithm is actionable.

#### Section 24.2: Dataset structure, embodiment metadata, licensing - EXCELLENT
**Lens 1**: PASS. Minimum schema (i, t, o_{i,t}, a_{i,t}, m_i), dataset-card-fields table with "failure if missing" column, validation code, real Pydantic lab.
**Lens 2**: PASS. Governance/licensing as first-class is a current and under-taught point.
**Lens 3**: PASS. Best license epigraph; "Metadata Is Part Of The Data."
**Lens 4**: PASS. Franka card example, separate licenses for video/state/language stretch goal.
**Lens 5**: PASS. Real hands-on lab.

#### Section 24.3: Cross-embodiment pooling - EXCELLENT
**Lens 1**: PASS. Per-embodiment normalization tilde_a=(a-mu_e)/sigma_e with the crucial subscript-e point, three transfer mechanisms (shared task semantics / shared observation structure / conditioned action decoding) each with its assumption.
**Lens 2**: PASS. Four pooling failure causes (representation mismatch / source imbalance / action infeasibility / evaluation leakage); the source-classifier leakage test is a sharp diagnostic.
**Lens 3**: PASS. "Diplomat For Robot Bodies", "Normalize With The Body Still Visible."
**Lens 4**: PASS. Two-robot normalization example showing identical normalized values mean different hardware motion.
**Lens 5**: PASS. "Pooling Readiness Test" algorithm.

#### Section 24.4: Empirical data scaling laws - GOOD
**Lens 1**: Mostly PASS but the power-law form is referenced ("A common empirical form is:") with the equation apparently not rendering in the extracted text - verify the actual formula (e.g. failure ~ A N^{-alpha} + epsilon_inf) is present and not an empty line. The log-log slope-fitting code and the alpha=0.32 reading are good and honest about confounds.
**Lens 2**: PASS. Open problem: jointly varying demonstrations/tasks/embodiments/language/capacity under matched panels. Honest about robot scaling being younger than LM scaling.
**Lens 3**: "The Curve Is A Measurement Device" and "Scaling By Convenience" pitfall are strong.
**Lens 4**: PASS. BridgeData V2 scaling-experiment example.
**Lens 5**: Minor: no witty epigraph (24.4 and 24.5 drop the epigraph that 24.1-24.3 have). Add one to match the chapter.
**Fix**: confirm the power-law equation renders; if missing, insert $\mathrm{fail}(N) \approx \beta N^{-\alpha} + \mathrm{fail}_\infty$ with a one-line intuition.

#### Section 24.5: Curating and mixing data - GOOD
**Lens 1**: PASS. Mixture weights p_1..p_K, temperature sampling interpolating uniform-over-episodes vs uniform-over-sources, gradient-pressure mechanism, mixture-debugging source-classifier signal. (Confirm the temperature-sampling equation p_k ~ n_k^tau / sum renders; extracted text shows the code output but the inline equation may be missing.)
**Lens 2**: PASS. Open problems: automatic mixture optimization, cross-release dedup, source-aware evaluation, learned source downweighting.
**Lens 3**: "The Mixture Is A Claim" is a good framing; no epigraph though.
**Lens 4**: PASS. OpenX/DROID/BridgeData V2 temperature example with realistic weights.
**Lens 5**: PASS, but the chapter ends here with no "What's Next" bridge to Chapter 25 (the bridge is absent in 24.5). Add one.

### Chapter 25: Offline RL and Dataset-Based Robot Learning
**Quality**: NEEDS WORK (real worked traces, but Template C with identical sibling paragraphs and a repeated diagram)

The depth content is real (support penalties, CQL/IQL comparison, gated offline-to-online, importance-sampling instability), but this chapter has a severe repetition problem: **all five sections open with the byte-for-byte identical "Big Picture" paragraph** ("asks a hard robot-learning question: how can a policy improve from a fixed dataset... The answer is not 'train harder'..."), **all five reuse the same "A Careful Control Loop" cite**, **all five embed the same offline-RL pipeline diagram** (Robot dataset -> Behavior support -> Pessimistic critic -> Policy -> Same-panel eval), and **all five repeat the identical "Algorithm: Offline Policy Update With Support Guard" and "Practical Recipe" lists**. The section-specific content is only the "Why Offline RL Is Different" paragraph and the worked numeric trace. This is the second-worst non-substitutability problem in the part after Chapter 21.

#### Section 25.1: Learning without online interaction - NEEDS WORK
**Lens 1**: Depth PASS. Extrapolation framing, the constrained objective max_pi E[Q(s,a)] - lambda E[d(a, supp(D_s))], support-distance numeric trace, "When Behavior Cloning Wins" (start with BC and make offline RL justify its complexity). Good. But the identical Big Picture paragraph is the section opener, which is generic.
**Lens 2**: Generic. Fix: name the current offline-RL-for-robots threads (IQL/CQL on real manipulation, Cal-QL for offline-to-online, the "BC is a strong baseline" result from D4RL/robomimic).
**Lens 3**: No epigraph (generic cite). Fix: add a witty offline-RL epigraph, e.g. on extrapolating confidently into actions never tried.
**Lens 4**: PASS. Support-distance example is topic-specific.
**Lens 5**: PASS as the chapter opener; the pipeline diagram is genuinely useful here (but should not be repeated identically in 25.2-25.5).

#### Section 25.2: Distribution shift and extrapolation error - NEEDS WORK
**Lens 1**: Depth PASS (state shift vs action shift vs extrapolation error, nearest-logged-action distance diagnostic). But Big Picture paragraph is identical to 25.1, 25.3, 25.4, 25.5.
**Lens 2**: Generic frontier. Fix: name the specific threads (uncertainty-penalized critics, support-constrained policies).
**Lens 3**: No unique epigraph. The diagram is repeated.
**Lens 4**: PASS. The 0.90-action-is-risky-not-bad example is good.
**Lens 5**: Weak: opens identically to siblings, so a reader moving 25.1 -> 25.2 sees the same three paragraphs twice. **Fix: rewrite each Big Picture to be section-specific; remove the duplicated diagram from 4 of 5 sections.**

#### Section 25.3: Conservative methods (CQL, IQL) and their intuition - NEEDS WORK
**Lens 1**: Depth PASS and this is the best trace in the chapter: side-by-side BC vs CQL-pessimism vs IQL-advantage-weighting with tiny visible arrays. Could add the CQL value-gap objective and IQL expectile-regression equation to reach full graduate depth (currently the intuition is present but the two defining equations are not).
**Lens 2**: Generic. Fix: state the open problem (hyperparameter sensitivity of CQL's alpha; when expectile tau in IQL matters).
**Lens 3**: Identical Big Picture, identical diagram, no epigraph.
**Lens 4**: PASS. The three-method array comparison is excellent and topic-specific.
**Lens 5**: Identical opener problem again.
**Fix**: add CQL objective $\min_Q \alpha(\mathbb{E}_{a\sim\mu}[Q] - \mathbb{E}_{a\sim D}[Q]) + \mathrm{TD\ error}$ and IQL expectile loss; rewrite Big Picture.

#### Section 25.4: Offline-to-online fine-tuning - NEEDS WORK
**Lens 1**: Depth PASS. Safety-gated online adaptation, the per-rollout success/interventions/support_drift trace is a good practitioner artifact. But Big Picture identical to siblings.
**Lens 2**: Generic. Fix: name Cal-QL, the distribution-shift-on-unfreeze problem, and warm-start collapse.
**Lens 3**: Identical opener, repeated diagram.
**Lens 4**: PASS. Gated-rollout trace is topic-specific.
**Lens 5**: Missing a "What's Next" and an epigraph.

#### Section 25.5: Evaluating offline policies rigorously - NEEDS WORK
**Lens 1**: Depth PASS. Off-policy evaluation difficulty, importance-sampling instability shown numerically (product of ratios makes one trajectory dominate), the multi-pronged evaluation plan. But Big Picture identical to siblings.
**Lens 2**: Generic. Fix: name OPE methods (FQE, weighted IS, doubly-robust) and the open problem that real-robot rollouts remain the only trustworthy evaluation.
**Lens 3**: Identical opener, repeated diagram.
**Lens 4**: PASS. The IS-variance numeric example is exactly right for the topic.
**Lens 5**: Good capstone content trapped in the repeated shell.

### Chapter 26: Skills, Hierarchy, and Task Decomposition
**Quality**: NEEDS WORK (real worked implementations, but Template C with identical sibling paragraphs and repeated diagram)

Same repetition disease as Chapter 25: **all five sections open with the identical "Big Picture" paragraph** ("treats action as a hierarchy rather than a flat stream of motor commands. A skill gives the planner a reusable temporal abstraction with an initiation condition, an internal policy, a termination rule, and a verification contract"), **all five reuse "A Careful Control Loop"**, **all five embed the identical hierarchical-policy diagram** (Mission goal -> Task graph -> Navigate/Manipulate/Recover -> Verifier), and **all five repeat the identical "Algorithm: Verified Skill Execution" and "Practical Recipe" lists**. Section-specific content is only the "Why Hierarchy Matters" paragraph and the worked implementation.

#### Section 26.1: What a skill is; low- vs. high-level actions - NEEDS WORK
**Lens 1**: Depth PASS. Skill-as-promise (initiation predicate, internal policy, termination, verification contract), the dataclass skill with start/stop/verify. Good. But add the formal options tuple here or defer cleanly to 26.2; currently "Formal Contract" appears as a heading with the content thin.
**Lens 2**: Generic. Fix: connect to current VLA-as-high-level-planner (SayCan, RT-H, Code-as-Policies) and the open problem of skill verification in sensor space.
**Lens 3**: No epigraph; identical Big Picture. "Skill Equals Promise" is a decent hook but it is repeated in all 5 sections so it loses force.
**Lens 4**: PASS. Verb-object skill naming (navigate_to_station, grasp_handle, dock_drone, change_lane) spans drone/AV/humanoid embodiments, good for the practitioner audience.
**Lens 5**: Good opener content, but the verifier/skill diagram should be unique to 26.1, not repeated 5x.

#### Section 26.2: The options framework - NEEDS WORK
**Lens 1**: Depth needs strengthening. The worked option-as-temporal-abstraction code (three primitive ticks compressed to one option outcome) is good, but the section is titled "The options framework" and **the defining options formalism (initiation set I, intra-option policy pi, termination condition beta) and the SMDP value equation are not stated**. This is the one section where the boilerplate "Formal Contract" heading most needs real content. Fix: add the Sutton-Precup-Singh option tuple (I, pi, beta) and the option-value / SMDP Bellman backup.
**Lens 2**: Generic. Fix: cite Sutton/Precup/Singh 1999 and modern option-discovery.
**Lens 3**: Identical Big Picture and diagram.
**Lens 4**: PASS. The option-compression numeric trace is topic-specific.
**Lens 5**: Identical opener.

#### Section 26.3: Skill discovery and hierarchical RL - NEEDS WORK
**Lens 1**: Depth PASS. The mutual-information skill-discovery objective max_{pi,z} I(z;s_T) + E[sum r_task] is the right DIAYN/variational-skill formalism, and the toy clustering-into-named-skills code makes the "discovered behavior is useful only when nameable/verifiable/selectable" point.
**Lens 2**: Generic. Fix: name DIAYN, DADS, and the open problem (mutual-information skills rarely align with task-useful abstractions).
**Lens 3**: Identical Big Picture and diagram.
**Lens 4**: PASS. Clustering example is topic-specific.
**Lens 5**: Identical opener; the worked block is good.

#### Section 26.4: Language as a high-level controller - NEEDS WORK
**Lens 1**: Depth PASS. Grounding language into a typed skill library with affordance checks, the inspect/navigate/grasp grounding example where grasp is blocked until reachable. This is the correct SayCan-style framing.
**Lens 2**: Generic. Fix: name SayCan, RT-2/RT-H, PaLM-E, Code-as-Policies (2022-2024) and the open problem of closed-loop replanning when a grounded skill fails mid-execution.
**Lens 3**: Identical Big Picture and diagram (though 26.4 does have a section-specific Figure 26.4.B caption noting language sits above the task graph - good, keep that).
**Lens 4**: PASS. The grounding/affordance example is topic-specific and current.
**Lens 5**: Identical opener.

#### Section 26.5: Skill libraries for embodied agents - NEEDS WORK
**Lens 1**: Depth PASS. Skill library as engineering asset (controllers + learned policies + task-graph nodes + verification tests + metadata), the cost/risk skill-selector code that rejects the cheap-but-risky lane change. Strong practitioner framing.
**Lens 2**: Generic. Fix: connect to growing/lifelong skill libraries (Voyager-style skill accumulation, code-skill libraries) and the open problem of skill-library maintenance and dedup.
**Lens 3**: No epigraph; missing "Big Picture" entirely in the extracted opener (26.5 may have a slightly different structure - verify it still has a frame). Identical diagram.
**Lens 4**: PASS. The AV lane-change/pull-over selector is topic-specific.
**Lens 5**: Good capstone for the chapter and the part; ensure it has a "What's Next" bridging to Part 6.

## Cross-Chapter Issues in This Part

1. **Three inconsistent templates within one part.** Chapters 23-24 are lean and excellent; 21 is heavy boilerplate; 22 is heavy-but-rich; 25-26 are repetitive. The reader experiences a quality whiplash. Converge everything to the Chapter 23/24 lean template.

2. **Title-substitution boilerplate (Chapter 21, partially 22).** Identical "Theory", "Worked Example" (same glob code), "Builder's Deep Dive" (same EvidenceRecord), "Agent Checklist Integration", and "Practical Tool Choices" tables appear in every section with only the title spliced in. By the non-substitutability rule these passages are boilerplate and should be cut, leaving the `course-depth-block` as the section body.

3. **Identical sibling paragraphs (Chapters 25, 26).** Every section in Chapter 25 opens with the same "Big Picture" paragraph; every section in Chapter 26 opens with the same one. This is verifiable byte-for-byte duplication (5x each). Each Big Picture must be rewritten to be section-specific.

4. **Repeated identical diagrams (Chapters 25, 26).** The offline-RL pipeline SVG and the hierarchical-skill SVG are embedded identically in all five sections of their chapters. Keep the diagram in the chapter opener (25.1, 26.1) and remove it from the other four, or make each instance section-specific.

5. **Wrong-topic tool tables (Chapters 21, 22).** The "Practical Tool Choices" tables list Gymnasium, PettingZoo, ROS 2, MuJoCo, LeRobot for imitation-learning and action-representation sections. PettingZoo (multi-agent RL) and bare Gymnasium are off-topic here. Replace with LeRobot, robomimic, the `imitation` library, ACT/Diffusion Policy repos.

6. **Generic "Research Frontier" callouts.** Most sections in Chapters 21, 22, 25, 26 carry a content-free frontier callout ("treat frontier claims as hypotheses until they expose enough detail to reproduce"). Chapters 23-24 show how to do it right (named systems + a precise open question). Replace every generic one with a 2024-2026 named thread.

7. **Index typo across chapters.** The chapter index "Instructor And Builder Notes" contains "For , the practical stack should be introduced..." with an empty placeholder where the chapter topic name belongs. This appears in multiple chapter indexes (21, 22 confirmed).

8. **Epigraph drought in 24.4-24.5, 25, 26.** Chapters 23-24.3 have excellent witty epigraphs; the later sections drop them for the generic "A Careful Control Loop" cite. Add section-specific epigraphs in the 23/24 voice.

## Top 10 Highest-Priority Fixes for This Part

1. **De-duplicate Chapter 25 Big Picture paragraphs.** Files: `module-25-offline-rl-and-dataset-based-robot-learning/section-25.1.html` through `25.5.html`. Replace the shared opener. Draft for 25.2: "Offline RL fails in a specific way: the critic is most confident exactly where the data is thinnest. This section separates the two shifts that cause it - state shift (deployment observations differ from logged ones) and action shift (the policy proposes actions the behavior policy never tried) - and shows why extrapolation error is the critic's confident wrong answer in the unsupported region."

2. **De-duplicate Chapter 26 Big Picture paragraphs.** Files: `module-26-.../section-26.1.html` through `26.5.html`. Draft for 26.2: "The options framework gives the repeated phrase 'a skill is a temporal abstraction' a precise mathematical form: an option is a triple of an initiation set, an intra-option policy, and a termination condition, and a planner that reasons over options is solving a semi-Markov decision process."

3. **Add the missing options formalism to 26.2.** File: `section-26.2.html`. Insert the (I, pi, beta) option tuple and the SMDP option-value backup; the section is named "The options framework" but never states it.

4. **Add CQL and IQL defining equations to 25.3.** File: `section-25.3.html`. Insert the CQL value-gap term and the IQL expectile-regression loss alongside the existing (good) intuition trace.

5. **Strip Chapter 21 boilerplate shell; promote the depth blocks.** Files: `module-21-.../section-21.1.html` through `21.5.html`. Delete the generic "Theory", "Worked Example" (glob filler), "Builder's Deep Dive", "Implementation Recipe", and "Agent Checklist Integration" blocks; keep the `course-depth-block`, the bibliography, and one self-check. This roughly halves each page and removes the worst non-substitutability content.

6. **Fix the index placeholder typo.** Files: all six `module-2X-.../index.html`. Replace "For , the practical stack..." with "For this chapter, the practical stack...".

7. **Replace wrong-topic tool tables in Chapters 21 and 22.** Swap Gymnasium/PettingZoo rows for LeRobot, robomimic, the `imitation` library, and the relevant policy repos (ACT, Diffusion Policy, pi0).

8. **Replace all generic Research Frontier callouts with named threads.** Priority files: every section in Chapters 21, 22, 25, 26. Use the precise open problems drafted per-section above (active demonstration selection; flow-matching/consistency distillation; Cal-QL offline-to-online; DIAYN/DADS skill-task misalignment).

9. **Remove the repeated SVG diagrams from 25.2-25.5 and 26.2-26.5.** Keep one in each chapter opener. The current identical-five-times embedding is visual boilerplate.

10. **Verify two equations render and add missing epigraphs.** Files: `section-24.4.html` (power-law form), `section-24.5.html` (temperature-sampling weight equation). Confirm they are present, not empty lines. Then add section-specific witty epigraphs to 24.4, 24.5, and all of Chapters 25-26 in the Chapter 23 voice.

## Structure Suggestions for This Part

- **No chapters should be dropped or merged.** The six-chapter arc (imitation -> action representation -> data collection -> datasets/scaling -> offline RL -> skills/hierarchy) is logically clean and each chapter earns its place.
- **Promote Chapters 23 and 24 as the house template.** They already meet the lean section contract; the editing effort should be making 21, 22, 25, 26 look like them, not the reverse.
- **Chapter 26 placement is slightly awkward inside "Learning from Demonstration and Robot Data."** Skills/hierarchy/options is more a control-and-planning topic than a data topic. It works as a capstone (composing learned policies into skills), but the chapter intro should explicitly justify why it lives in Part 5 (answer: skill libraries are how demonstration-trained policies become reusable assets). Add one framing sentence rather than moving it.
- **Consider splitting Chapter 22's 22.4 (diffusion) and 22.5 (flow matching) verification.** Both are the most frontier-sensitive sections; ensure their generative-model equations (DDPM epsilon-prediction loss; flow-matching vector field / ODE) actually render, since they are the sections most likely to have KaTeX gaps.
- **Add the missing "What's Next" bridges** at the end of 24.5 (into Chapter 25), 25.4, 25.5 (into 26 / Part 6), and 26.5 (into Part 6). Chapters 23-24 have these; the later chapters drop some.
