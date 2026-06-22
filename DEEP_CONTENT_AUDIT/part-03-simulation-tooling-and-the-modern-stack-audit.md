# Part 3 Content Audit: Simulation, Tooling, and the Modern Stack

## Part Overview

Part 3 is the most uneven part of the book in terms of quality variance, and also one of the most technically valuable. Chapters 11 (physics simulators) and 12 (benchmarks) are genuinely strong: current to 2025/2026 (Gazebo Classic EOL January 2025, the Isaac Gym to Isaac Lab migration, Newton under Linux Foundation governance, ManiSkill3 GPU-parallel, Habitat 3.0 social tasks), with runnable topic-specific code, accurate tradeoff tables, and correct constructs. Chapter 10 (Gymnasium/PettingZoo) is also strong on the code front (real `gymnasium`/`pettingzoo` API that actually runs). The two weaknesses that recur are: (1) Chapter 9 carries heavy template boilerplate (the "Builder's Deep Dive", "Practical Tool Choices For This Section" table with five generic Gymnasium/PettingZoo/ROS 2/MuJoCo/LeRobot rows, the `EvidenceRecord` dataclass, and "Failure Analysis Pattern" are near-identical across 9.1/9.2/9.3 with only the section name swapped, a direct non-substitutability violation); and (2) a formulaic epigraph and intro scaffold ("X matters when the next action changes the evidence you thought you had", "What This Section Builds", "The Interface Is The Test" / "Evidence Is The Test" / "Transfer Is The Test") repeats verbatim across nearly every section of Chapters 10, 12, and 13.

The single dominant theme across the whole part, the "evidence rule" (co-compute compared numbers in one pass on one config), is correct and valuable, but it is restated in nearly every section to the point of redundancy, and in Chapter 9 it crowds out actual mechanism.

Section counts differ from the part index: the index lists 5 sections per chapter, but Chapters 10, 11, 12, 13 each have 6-8 section files (10.6 Evaluation protocol, 10.7 PettingZoo, 11.6 Genesis, 11.7 Drake/SAPIEN/ROS2/Gazebo, 11.8 decision lab, 12.6 leaderboard reading, 13.6 randomization vs realism). The part index `index.html` should be updated to list all sections.

## Fun Elements to Preserve

These are genuine, topic-specific, and must survive any edit:

- **9.1 Memory Hook**: "If a simulated policy knocks over a virtual lamp, the lab learns something. If the real robot does it, the lab also learns who ordered the replacement lamp." (excellent, memorable, topic-true)
- **9.2 Memory Hook**: "A simulator wearing four hats is fine. A results table that forgets which hat it wore is not."
- **9.2 epigraph**: "A simulator can be a camera, a wind tunnel, and a patient examiner, provided you label which job it is doing."
- **9.3 epigraph**: "Realism is not a volume knob. It is a mixing board with labels you should read before touching anything." (strong)
- **9.3 Memory Hook**: "A beautiful simulation with the wrong friction is a glossy brochure for a skill the robot does not have."
- **9.4 Memory Hook**: "The reality gap is the simulator's receipt. If the receipt does not list the same items as the hardware run, do not use it for accounting."
- **9.5 Memory Hook**: "A benchmark is a gym membership for one skill. Winning the treadmill does not prove you can assemble furniture." (excellent)
- **9.1 epigraph**: "The fastest robot lesson is the one learned before the robot hits the table."
- **11.1 Memory Hook**: "A simulator is a promise about the next state. The debugging trick is to ask which promise failed: the body model, the contact model, the sensor model, or the solver that glued them together."
- **11.2 Memory Hook**: "A robot model is ready for learning only when it is readable twice: once as source XML and once as compiled physics. If those two stories disagree, trust the compiled audit."
- **11.3 Memory Hook**: "MJX and MuJoCo Warp are not automatic speed labels. They are promises about where the arrays live, how many worlds move together, and which backend owns the contact calculation."
- **11.5 Memory Hook**: "Newton is a frontier engine, so the adoption rule is simple: enthusiasm can start the prototype, but the baseline comparison decides whether it becomes infrastructure."
- **11.6 Memory Hook**: "Generated worlds are useful only when they are diverse in the dimensions the robot feels. A thousand new mugs with the same friction are one physics example wearing many costumes." (excellent; reused as a near-twin in 11.6 body too)
- **11.7 Memory Hook**: "The trap is asking one tool to be a proof assistant, benchmark suite, RL factory, and robot middleware rehearsal."
- **12.1 Memory Hook**: "A benchmark row without its split, seed policy, and wrapper stack is like a robot demo without the camera angle."
- **12.2 Memory Hook**: "If the object split is leaky, the robot may look like it learned manipulation while really recognizing an old prop in a new pose."
- **12.1 / 12.2 / 12.4 / 12.5 figure captions**: these are genuinely custom, illustrative cartoon captions (benchmark auditor with magnifying glass; held-out vs familiar objects; household predicate checklist; short unsafe route vs longer safe route). Preserve.
- **13.1 Memory Hook**: "A random seed is not a receipt unless the manifest tells you what the seed was allowed to change."
- **13.6 framing**: "Randomization and realism are not rivals; they are budget choices for reducing transfer risk." (clean, accurate)

Total distinct fun elements catalogued: 19 (plus 4 custom Chapter 12 figure captions).

## Chapter-by-Chapter Analysis

### Chapter 9: Why Simulation Is Central
**Quality**: NEEDS WORK (sections 9.1-9.3 carry the heaviest boilerplate in the part; 9.4-9.5 are GOOD)

#### Section 9.1: Why real-world learning is slow, costly, and risky - NEEDS WORK
**Lens 1 (Deep Explanation)**: The trial-budget ledger (Code Fragment 9.1.1) is a real, topic-specific worked example and passes. But the "Builder's Deep Dive" and "Implementation Recipe" sections are generic. The `EvidenceRecord` dataclass (9.1.2) has placeholder field values ("record after the perturbation run: sensor or state input") that print literally; this is exactly the `plan = [skill for skill in skills]` filler the contract forbids.
- Fix: Delete the `EvidenceRecord` dataclass and its output. Replace with a one-line extension of the actual trial-budget ledger, e.g. add a `sim_speedup` factor that shows how many simulated hours map to one hardware hour, tying directly to the section's economics argument.

**Lens 2 (Research Frontier)**: PASS in spirit, the Research Frontier callout (allocating trials across sim and hardware) is a real open problem. But it is generic.
- Fix: Name a concrete 2024-2026 reference. e.g. cite the RL-from-real-data-plus-sim work (e.g. SERL / HIL-SERL for real-world sample efficiency, or the "DayDreamer" world-model-on-hardware result) so the frontier feels alive rather than abstract.

**Lens 3 (Fun/Engagement)**: Strong. The "virtual lamp / replacement lamp" Memory Hook is one of the best in the part. Preserve.

**Lens 4 (Examples/Analogies)**: The cost ledger is concrete and grounded. The "Practical Tool Choices For This Section" table (Gymnasium/PettingZoo/ROS 2/MuJoCo/LeRobot all with identical advice "Use it when the experiment needs a maintained implementation rather than custom glue") is pure boilerplate.
- Fix: Cut that table entirely from 9.1, 9.2, 9.3. It adds no information.

**Lens 5 (Teaching Flow)**: The duplicated "Builder's Deep Dive" opening paragraph ("becomes useful when it is tied to a closed-loop contract... a sensor drops a frame or a controller saturates") appears verbatim in 9.1, 9.2, 9.3. Cut to one occurrence or rewrite per-section.

#### Section 9.2: Simulation as data generator, testbed, and curriculum - NEEDS WORK
**Lens 1**: The four-roles framing (data generator / testbed / curriculum / counterfactual probe) is genuinely good and topic-specific, and the curriculum-schedule code (9.2.1) is a real example. But the second half repeats the 9.1 boilerplate (same `EvidenceRecord`, same tool table, same failure-analysis paragraph).
- Fix: Keep the front half (through the curriculum schedule and "How To Keep Roles Separate"). Delete the entire `production-depth-expansion` boilerplate block and replace with a short, role-specific failure example (a curriculum whose final stage was easier than the benchmark, with the measured inflation it caused).

**Lens 2**: Research Frontier (ProcTHOR/Isaac Lab moving curricula from hand-authored to generated distributions) is current and good. PASS.

**Lens 3**: "Four hats" Memory Hook is strong. Preserve.

**Lens 4**: The warehouse-picking Practical Example is concrete. PASS on the front half.

**Lens 5**: Transition into the boilerplate block is abrupt. The first half flows well.

#### Section 9.3: Fidelity: physical, visual, behavioral - GOOD (front half EXCELLENT, back half boilerplate)
**Lens 1**: The fidelity-axis decomposition (physical/visual/sensor/behavioral) is excellent and the fidelity-match code (9.3.1, set difference of task needs vs simulator capabilities) is a genuinely good, topic-specific worked example. PASS for the body.
- Fix: same as above, delete the boilerplate `production-depth-expansion` tail.

**Lens 2**: OpenUSD-synchronization frontier callout is current. PASS.

**Lens 3**: Two strong analogies ("mixing board" epigraph, "glossy brochure" Memory Hook). Preserve both.

**Lens 4**: PASS, the MuJoCo-vs-ProcTHOR-vs-Isaac-Lab split is realistic.

**Lens 5**: PASS for body.

#### Section 9.4: The reality gap as a measurable quantity - GOOD
**Lens 1**: Strong. Real equation ($\Delta(c) = M_{real}(c) - M_{sim}(c)$ with sign interpretation), the paired-gap table (9.4.1) is the best worked example in the chapter (concrete numbers, low-friction row exposes the transfer failure), and the `GapRecord` here is topic-specific (case_id, sim/real metric, failure label, replay_uri) rather than the generic `EvidenceRecord`. PASS.
- Note: This is the model the rest of Chapter 9 should follow. The `production-depth-expansion` here is genuinely tailored (simulator-validity / policy / transfer claim separation), not boilerplate.

**Lens 2**: Frontier (paired datasets, residual modeling, automatic system identification, trial allocation to reduce uncertainty) is precise. PASS.

**Lens 3**: "Simulator's receipt" Memory Hook. Preserve.

**Lens 4**: PASS. Grasping team 91% sim / 68% real example is concrete and realistic.

**Lens 5**: PASS.

#### Section 9.5: The landscape of benchmark environments (titled "Benchmark environment map") - GOOD
**Lens 1**: Strong. Construct-not-leaderboard framing, the `BenchmarkCard` is topic-specific, the construct-matching code (9.5.1) is real. PASS.
- Minor: title in the file ("Benchmark environment map") differs from the part-index title ("The landscape of benchmark environments"). Reconcile.

**Lens 2**: PASS. The "breadth diluting construct validity" frontier point is precise.

**Lens 3**: "Gym membership for one skill" Memory Hook is excellent. Preserve.

**Lens 4**: PASS. ManiSkill-only-candidate example is well chosen.

**Lens 5**: PASS. Overlaps in scope with Chapter 12 (it previews the whole benchmark chapter); consider trimming so it does not duplicate 12.1.

### Chapter 10: Environments with Gymnasium (and PettingZoo)
**Quality**: GOOD (strong runnable code throughout; formulaic epigraph + intro scaffold the main drag)

#### Section 10.1: Gym is dead; Gymnasium is the standard - GOOD
**Lens 1**: PASS. The terminated-vs-truncated distinction is explained with correct motivation (bootstrapping, incident analysis) and the code (10.1.1, real `gymnasium.make("CartPole-v1")` five-field unpack) runs. The migration mechanism is precise.

**Lens 2**: PASS. Farama-ecosystem-as-infrastructure framing is current.

**Lens 3**: The Memory Hook here ("could a teammate point to the log line... that proves the idea changed the agent's next action?") is generic and reused across multiple sections.
- Fix: Replace with a Gym-specific joke, e.g. on the `done` bit losing the cause of death: "The old `done` flag was a tombstone with no epitaph: you knew the episode died, never why."

**Lens 4**: PASS, real API.

**Lens 5**: The epigraph "Gym is dead; Gymnasium is the standard matters when the next action changes the evidence you thought you had" is awkward (title-as-subject grammar) and repeats across the chapter.
- Fix: Replace each section's epigraph with a distinct line. For 10.1: "A `done` flag tells you the episode ended. It never tells you whether the robot won, lost, or just ran out the clock."

#### Section 10.2: Observation and action spaces - GOOD
**Lens 1**: PASS. `Box`/`Discrete`/`MultiDiscrete`/`Dict` explained with the right design question ("what should the policy be allowed to observe?"), `space.contains` mechanism is correct, code (10.2.1 Dict space + contains check) runs.

**Lens 2**: PASS. Frontier (language goals, variable object counts, graph observations) is current.

**Lens 3**: "Control-room label" Memory Hook is decent but reused in 10.6 verbatim.

**Lens 4**: PASS. The privileged-pose-leak warning is a real, topic-specific failure mode.

**Lens 5**: PASS. Good forward reference to vectorization needing space design.

#### Section 10.3: Reward design and termination - GOOD
**Lens 1**: PASS. The reward-as-measurement-model framing and the terminated/truncated split with reward-term decomposition in `info` is solid. Code (10.3.1 forcing truncation via `max_episode_steps=3`) is a clean, illustrative real example.

**Lens 2**: PASS. Reward-design-as-active-problem (sparse + dense + safety + preference) is current.

**Lens 3**: Reward-hacking warning is good. Memory Hook is generic-ish.

**Lens 4**: PASS. Drawer-opening terminated-vs-truncated example is concrete.

**Lens 5**: PASS.

#### Section 10.4: Vectorized environments; wrappers - GOOD
**Lens 1**: PASS. Wrapper-as-transformation + vector-env-as-batch-dimension. Code (10.4.1 `TimeAwareObservation` changing 4->5 obs) is real and makes the wrapper-changes-the-contract point vividly.

**Lens 2**: PASS.

**Lens 3**: Memory Hook is the generic "ask what would be different in the next frame" reuse.
- Fix: a wrapper-specific line, e.g. "A wrapper stack is a stack of glasses. Forget which ones the policy wore, and you cannot say what it actually saw."

**Lens 4**: PASS. 32-arm vectorization + normalization example is realistic.

**Lens 5**: PASS.

#### Section 10.5: Rendering, logging, and debugging - GOOD
**Lens 1**: PASS. Render-vs-log distinction (what the env shows vs what the policy consumed) is a genuinely useful mental model. Code (10.5.1 `FrozenLake-v1` ansi render + structured trace) runs and pairs the two views.

**Lens 2**: PASS.

**Lens 3**: Generic Memory Hook reuse again.

**Lens 4**: PASS. Save-one-video-plus-log-per-failed-seed is concrete advice.

**Lens 5**: PASS.

#### Section 10.6: Evaluation protocol and seeding - GOOD
**Lens 1**: PASS. Protocol-as-unit-of-comparison is correct; the seed smoke test (10.6.1) is real and the determinism-within-seed / variation-across-seed interpretation is right.
- Note: This section lacks the illustration figure (epigraph has no `<figure>`), unlike 10.1-10.5. Add a figure or note the inconsistency.

**Lens 2**: PASS. "Protocols that reveal robust vs lucky" is a precise frontier statement.

**Lens 3**: "Control-room label" Memory Hook is a verbatim copy of 10.2's.
- Fix: Replace with a seeding-specific line.

**Lens 4**: PASS.

**Lens 5**: PASS.

#### Section 10.7: PettingZoo for multi-agent - GOOD
**Lens 1**: PASS, and the strongest code in the chapter: a real, minimal `ParallelEnv` subclass (`TwoRobotLine`) with per-agent dict returns. AEC-vs-Parallel distinction is correct (`agent_iter()`/`last()` vs action-dict). This is exactly the "from-scratch then library" payoff.

**Lens 2**: PASS.

**Lens 3**: Reward-averaging-hides-freeloading warning is a good topic-specific insight.

**Lens 4**: PASS. Picker/carrier warehouse example maps cleanly to AEC vs Parallel.

**Lens 5**: PASS. Also missing the figure like 10.6.

### Chapter 11: Physics Simulators: MuJoCo, MJX, Isaac Lab, Genesis
**Quality**: EXCELLENT (the strongest chapter in the part; no template boilerplate, current facts, real code)

#### Section 11.1: What physics simulators model - EXCELLENT
**Lens 1**: PASS. Real state-transition equation $s_{t+1} = \text{step}(s_t, a_t, \Delta t, \theta)$ with $\theta$ enumerated (masses, inertias, friction, solver tolerances), solver-settings-are-not-cosmetic point, and a genuinely runnable from-scratch contact stepper (Code Fragment 1) with correct restitution physics and real numeric output. The "contacts are the hard part" mechanism section (friction cones, interpenetration, constraint forces) is graduate-depth.

**Lens 2**: PASS. "Contact-aware validation" as a 2026 frontier (policy sensitivity to friction/compliance/restitution before hardware) is precise.

**Lens 3**: "A simulator is a promise about the next state" Memory Hook. Preserve.

**Lens 4**: PASS. The from-scratch stepper followed by the MuJoCo `mj_step` shortcut (in 11.2) is the exact right-tool-payoff pattern.

**Lens 5**: PASS. Clean bridge from Chapter 9 to Chapter 13.

#### Section 11.2: MuJoCo and the MJCF/URDF model formats - EXCELLENT
**Lens 1**: PASS. Real MJCF model string, real `mujoco.MjModel.from_xml_string` + `mj_step` (Code Fragments 1 and 2), MJCF-vs-URDF tradeoff with the correct caveat (URDF underspecifies friction/contact, needs an import audit). Graduate depth on what to re-check after URDF import (inertias, mesh scale, collision simplification, transmission-to-actuator mapping).

**Lens 2**: PASS. USD-as-scene-interchange-while-keeping-compact-control-models is a current, precise frontier.

**Lens 3**: "Readable twice" Memory Hook. Preserve.

**Lens 4**: PASS. MuJoCo Menagerie cited in bibliography; gripper MJCF-in-a-day example is realistic.

**Lens 5**: PASS.

#### Section 11.3: MuJoCo MJX and MuJoCo Warp - EXCELLENT
**Lens 1**: PASS. MJX (JAX, `jit`/`vmap`, batched arrays) vs MuJoCo Warp (NVIDIA Warp kernels) distinction is accurate and current. Differentiability-is-not-magic section (contact discontinuities, validate gradients with finite differences) is graduate-depth and correct. Vectorized-NumPy fragment teaches the batching idea honestly (stated as a stand-in for JAX).

**Lens 2**: PASS. The convergence-on-accelerator-native-simulators frontier is precise.

**Lens 3**: "Promises about where the arrays live" Memory Hook. Preserve.

**Lens 4**: PASS. MJX-vs-Warp comparison table is genuinely differentiated (not boilerplate).

**Lens 5**: PASS.

#### Section 11.4: NVIDIA Isaac Sim + Isaac Lab; the migration - EXCELLENT
**Lens 1**: PASS. The Isaac Gym Preview / IsaacGymEnvs / OmniIsaacGymEnvs / Orbit -> Isaac Lab migration is stated correctly and the "start with Isaac Lab unless reproducing an older result" rule is the right practical guidance. TaskContract dataclass is topic-specific (robot/observations/actions/randomizations/success_metric).
- Minor bug: `TaskContract.as_row` calls `asdict(self)` but the snippet does not `from dataclasses import asdict` (only imports `dataclass`). The printed output uses `print(reach_task)` so it runs, but the method would `NameError`. Either import `asdict` or drop the unused method.

**Lens 2**: PASS. Isaac stack vocabulary table (Isaac Sim / Isaac Lab / OpenUSD / legacy Isaac Gym) is accurate.

**Lens 3**: Isaac Lab Memory Hook is decent.

**Lens 4**: PASS. Franka Panda reach task, legged-locomotion GPU-terrain-randomization example.

**Lens 5**: PASS. Good forward links to Ch 12, 13, 17.

#### Section 11.5: The Newton physics engine and OpenUSD - EXCELLENT
**Lens 1**: PASS. Newton positioned correctly (Warp + OpenUSD + multiple solvers + open governance via Linux Foundation), and the OpenUSD-is-more-than-a-file-format section with the scene-interchange-vs-physical-validity caveat is precise. The recency-aware adoption scorecard (Code Fragment 1) is a real, topic-appropriate worked example.

**Lens 2**: PASS. "Frontier Watch" callout dated "As of 2026" with the three-threads framing is exactly the live-frontier feel the rubric wants.

**Lens 3**: "Enthusiasm starts the prototype, baseline comparison decides infrastructure" Memory Hook. Preserve.

**Lens 4**: PASS. Humanoid-locomotion-benchmark prototype example with required mature baseline.

**Lens 5**: PASS.

#### Section 11.6: Genesis - EXCELLENT
**Lens 1**: PASS. Genesis (Pythonic, multi-physics, rendering, generative scene workflows) with the stricter-adoption-checklist and the generated-scene-trap (visual variety without physics variety). Scene-audit code is topic-specific.

**Lens 2**: PASS. "Reject generated worlds that are visually plausible but physically misleading" is a sharp open question.

**Lens 3**: "A thousand new mugs with the same friction" Memory Hook is one of the best in the part. Preserve.

**Lens 4**: PASS. Cloth-covered-objects example justifies multi-physics concretely.

**Lens 5**: PASS.
- Minor: the section mentions "Nyx rendering" for Genesis in the fit table; verify this is the current renderer name (Genesis has used "LuisaRender"-based pipelines historically). Flag for fact-check.

#### Section 11.7: Drake, SAPIEN, ROS 2, Gazebo - EXCELLENT
**Lens 1**: PASS. Each tool placed by job (Drake = optimization/control/verification, SAPIEN/ManiSkill = manipulation, ROS 2 + modern Gazebo = systems integration). Gazebo Classic EOL January 2025 stated correctly. The recommend-by-primary-risk classifier is a real worked example.

**Lens 2**: PASS. Multi-tool-pipeline reproducibility frontier is precise.

**Lens 3**: "Proof assistant, benchmark suite, RL factory, and robot middleware rehearsal" Memory Hook. Preserve.

**Lens 4**: PASS. Warehouse-mobile-robot multi-tool example is realistic.

**Lens 5**: PASS.

#### Section 11.8: Simulator selection decision guide and lab - GOOD
**Lens 1**: PASS. Selection guide table and the deprecation table (Gym->Gymnasium, Isaac Gym->Isaac Lab, Gazebo Classic->modern Gazebo) are accurate and useful. The co-computed scoring rubric is the right antidote to invalid cross-config comparison.

**Lens 2**: PASS.

**Lens 3**: Adequate.

**Lens 4**: PASS. The rubric scores tools on one config, reinforcing the part's evidence rule with a concrete artifact.

**Lens 5**: PASS. Good chapter-closing decision lab.

### Chapter 12: Benchmarks and Task Suites
**Quality**: GOOD (accurate benchmark facts and runnable audits; repeated intro scaffold the main weakness)

#### Section 12.1: Why standardized benchmarks matter - GOOD
**Lens 1**: PASS. Benchmark-as-sampled-closed-loop-episodes with the $\frac{1}{N}\sum_i m_i$ aggregate and the leakage-pipeline mechanism (sampler/sim/wrapper/policy/metric/aggregation). EvaluationRun audit (Code Fragment 1) is topic-specific and the `paper_table_ready` flag is a clean teaching device.

**Lens 2**: PASS. "Benchmark claims resistant to leakage and selective reporting" frontier is precise.

**Lens 3**: "Robot demo without the camera angle" Memory Hook. Preserve.

**Lens 4**: PASS. The cartoon figure caption (auditor with magnifying glass) is genuinely custom. Preserve.

**Lens 5**: The epigraph and "What This Section Builds" / "Evidence Is The Test" scaffold repeats across all of Chapter 12.
- Fix: Per-section distinct epigraphs and trim the repeated "treat the leaderboard as an instrument" key-insight to one canonical statement in 12.1, referenced thereafter.

#### Section 12.2: Manipulation suites - GOOD
**Lens 1**: PASS. ManiSkill3 (GPU-parallel) / robosuite (MuJoCo, controller choices) / RoboCasa (household variation) / robomimic (demonstration datasets, offline eval) / RLBench (vision-guided task variation) are each characterized correctly. The object-leakage audit (Code Fragment 1) is a real, topic-specific example.

**Lens 2**: PASS. Split-discipline-as-task-generators-grow frontier is precise.

**Lens 3**: "Recognizing an old prop in a new pose" Memory Hook. Preserve. Custom figure caption. Preserve.

**Lens 4**: PASS. The warning about importing a number from one suite/controller mode is exactly the right real-systems caution.

**Lens 5**: Same scaffold-repeat issue.

#### Section 12.3: Lifelong and language-conditioned (LIBERO, CALVIN, Meta-World) - GOOD
**Lens 1**: PASS. The $S_{k,t}$ task-by-stage matrix with the catastrophic-forgetting argument is graduate-depth, and the forgetting diagnostic (Code Fragment 1) is a real, well-chosen example. LIBERO (knowledge-shift kinds) / CALVIN (language-conditioned sequences) / Meta-World (multi-task vs meta-learning) constructs are correct.

**Lens 2**: PASS.

**Lens 3**: Custom figure caption ("the whole learning diary"). Preserve.

**Lens 4**: PASS. Different-task-order / different-adaptation-budget warning is the right caution.

**Lens 5**: Scaffold-repeat.

#### Section 12.4: Household and long-horizon (BEHAVIOR-1K / OmniGibson) - GOOD
**Lens 1**: PASS. Predicate-sequence framing, the partial-progress-vs-final-success distinction, and the predicate-accounting code (Code Fragment 1) are all topic-specific and correct. OmniGibson (interactive household sim) + BEHAVIOR-1K (human-need-inspired task suites) characterization is accurate.

**Lens 2**: PASS.

**Lens 3**: Custom figure caption (predicate checklist). Preserve.

**Lens 4**: PASS.

**Lens 5**: Scaffold-repeat.

#### Section 12.5: Navigation and social (Habitat 3.0, AI2-THOR / ProcTHOR) - GOOD
**Lens 1**: PASS. The SPL formula $S \cdot L / \max(P, L)$ is stated correctly with motivation, social navigation constraints (no crowding/blocking/colliding with humanoid) are accurate to Habitat 3.0's collaborative tasks, and the SPL-plus-collisions code (Code Fragment 1) co-computes efficiency and safety in one pass.

**Lens 2**: PASS.

**Lens 3**: Custom figure caption (short unsafe route vs longer safe route). Preserve.

**Lens 4**: PASS. ProcTHOR procedurally-generated-house framing is correct.

**Lens 5**: Scaffold-repeat.

#### Section 12.6: Reading a leaderboard without fooling yourself - GOOD
**Lens 1**: PASS. Leaderboard-row-as-summary-of-design-choices, the hidden-denominator argument, and the provenance-grouping code (Code Fragment 1, grouping rows by panel/split/seeds/metric) is a clean, real example that operationalizes the chapter's thesis.

**Lens 2**: PASS.

**Lens 3**: No figure (epigraph only), consistent with chapter-closer sections elsewhere.

**Lens 4**: PASS. The MT50 official-vs-tuned_validation grouping example is concrete.

**Lens 5**: Good chapter-closer. Scaffold-repeat in the intro.

### Chapter 13: Domain Randomization and Synthetic Data
**Quality**: GOOD (accurate DR/ADR/real2sim2real content; intro scaffold + reused generic figure captions the main weakness)

#### Section 13.1: Why synthetic variation matters - GOOD
**Lens 1**: PASS. Real DR formalism ($\theta \sim p_{train}(\theta)$ vs $p_{real}(\theta)$, support-overlap as the mechanism, coverage-not-chaos). The RandomizedFactor manifest (Code Fragment 1) ties each distribution to a named real failure mode, which is topic-specific and useful.

**Lens 2**: PASS. "Smallest randomized family that covers real variation without teaching the policy to ignore task-critical cues" is a precise open problem.

**Lens 3**: "A random seed is not a receipt" Memory Hook. Preserve.

**Lens 4**: PASS. Bin-picking detector example is realistic.

**Lens 5**: The figure caption here is the generic reused one ("is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation"), unlike Chapter 12's custom captions.
- Fix: Commission a custom caption like Chapter 12's (e.g. "Synthetic variety only helps along the axes the robot actually feels: matched friction across a thousand textures is still one physics example").

#### Section 13.2: Visual, physics, sensor, and task randomization - GOOD
**Lens 1**: PASS. The four-lever taxonomy with the coupling insight (shiny object affects both appearance and grasp friction; heavier object affects acceleration, slip, controller effort) is graduate-depth and exactly the right subtlety. FactorSample-with-class-label code supports later failure triage.

**Lens 2**: PASS (frontier implicit).

**Lens 3**: No standout Memory Hook here.
- Opportunity: add one on coupling, e.g. "Independent sampling is cheap; coherent sampling is what keeps the physics from lying."

**Lens 4**: PASS. The randomize-visual-when-the-real-problem-is-contact error is a sharp, real failure mode.

**Lens 5**: Generic reused figure caption (same fix as 13.1).

#### Section 13.3: Curriculum and automatic randomization - GOOD
**Lens 1**: PASS. ADR-as-outer-loop-controller framing is accurate (this is the OpenAI Dactyl ADR idea, correctly described: expand above the success band, hold/narrow below, rebalance the dominant-failure factor). The `update_friction_range` code (Code Fragment 1) is a real, runnable example of the controller.

**Lens 2**: PASS.
- Opportunity: cite OpenAI's "Solving Rubik's Cube with a Robot Hand" (ADR) by name in a Paper Spotlight to make the lineage explicit.

**Lens 3**: No standout hook.

**Lens 4**: PASS.

**Lens 5**: Generic reused figure caption.

#### Section 13.4: Photoreal rendering and tiled cameras - GOOD
**Lens 1**: PASS. Visual-realism-vs-sensor-realism distinction (depth holes, exposure, rolling shutter, segmentation boundaries differing from the real sensor) is the right graduate-level subtlety. Tiled-camera budget code is topic-appropriate.

**Lens 2**: PASS.

**Lens 3**: No standout hook.

**Lens 4**: PASS. Start-from-the-real-camera recipe is concrete.
- Opportunity: name Isaac Lab tiled-camera APIs and Omniverse Replicator / BlenderProc explicitly in the worked example rather than only in the library shortcut.

**Lens 5**: Generic reused figure caption.

#### Section 13.5: real2sim2real and asset/scene reconstruction - GOOD
**Lens 1**: PASS. Four-step loop (measure / reconstruct / randomize residual / validate on held-out real) with the calibration-vs-evaluation split as the critical discipline. The measured-dimensions-to-residual-range code (Code Fragment 1) with an explicit holdout object is a clean, leakage-aware example.

**Lens 2**: PASS.
- Opportunity: connect to current real2sim work (Gaussian-splatting / NeRF-to-sim asset reconstruction, e.g. "Robot See Robot Do" or splatting-based digital twins) in a Paper Spotlight to make the frontier current.

**Lens 3**: No standout hook.
- Opportunity: a digital-twin-as-test-set-mirror joke.

**Lens 4**: PASS.

**Lens 5**: Generic reused figure caption.

#### Section 13.6: Randomization vs. realism; measuring transfer readiness - GOOD
**Lens 1**: PASS. The randomization-vs-realism-as-budget-choices framing is accurate, the when-to-prefer-each guidance (randomize when the real distribution is broad/uncertain/expensive to reconstruct; realism when measured details dominate failure; hybrid usually strongest) is correct, and the shared-panel comparison code (Code Fragment 1, baseline/randomized/realistic/hybrid all in one dict) is the right co-computed-comparison artifact.

**Lens 2**: PASS.

**Lens 3**: "Not rivals, budget choices" framing is clean.

**Lens 4**: PASS. The hybrid-wins example is realistic and the construct-matching caution (do not compare detector AP from one run to robot success from another) directly enforces the part's evidence rule.

**Lens 5**: Good chapter-closer.

## Cross-Chapter Issues in This Part

1. **Template boilerplate concentrated in Chapter 9 (9.1-9.3)**: the `production-depth-expansion` block ("Builder's Deep Dive" + "Practical Tool Choices For This Section" 5-row generic table + generic `EvidenceRecord` dataclass with literal-placeholder field strings + "Failure Analysis Pattern") is reused with only the section name swapped. This is the clearest non-substitutability violation in the part. Chapters 11, 12, 13 do NOT have this block, which proves it is removable. Cut it from 9.1, 9.2, 9.3.

2. **Formulaic epigraph across Chapters 10, 12, 13**: "<Title> matters when the next action changes the evidence you thought you had", attributed to "A Careful Control Loop", appears in roughly 15 sections. It reads as auto-generated. Each section needs a distinct, topic-true epigraph (Chapter 9 and 11 already have good distinct ones; use them as the model).

3. **Repeated intro scaffold**: "What This Section Builds" (two paragraphs) followed by a "The Interface Is The Test" / "Evidence Is The Test" / "Transfer Is The Test" key-insight callout appears verbatim-structured in nearly every section of 10, 12, 13. The per-chapter thesis is stated once per section when once per chapter would suffice. Trim to one canonical statement per chapter and let sections open with section-specific framing.

4. **Reused generic figure captions in Chapter 13** (and 9, 10): "<Section> is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation." Chapter 12 has genuinely custom cartoon captions; Chapters 9, 10, 13 mostly use the generic one. Commission custom captions matching Chapter 12's quality.

5. **Part index out of date**: `part-3.../index.html` lists 5 sections per chapter, but Chapters 10-13 each have 6-8 sections. The roadmap and chapter cards omit 10.6, 10.7, 11.6, 11.7, 11.8, 12.6, 13.6. Update the index.

6. **The evidence rule is over-restated**: the co-compute-in-one-pass principle is correct and central, but it appears as a named callout ("Simulation Hypothesis Ledger" / "Benchmark Evidence Rule" / "Randomization Evidence Rule" / "Simulator Choice Evidence Rule") in almost every section. State it richly once per chapter; elsewhere reference it.

7. **Minor inconsistencies**: 10.6 and 10.7 lack the per-section illustration figure that 10.1-10.5 have. 9.5's file title ("Benchmark environment map") differs from the part-index title ("The landscape of benchmark environments"). 11.4's `TaskContract.as_row` references `asdict` without importing it.

## Top 10 Highest-Priority Fixes for This Part

1. **Cut the boilerplate `production-depth-expansion` block from Chapter 9 sections 9.1, 9.2, 9.3.** Files: `module-09-why-simulation-is-central/section-9.1.html`, `section-9.2.html`, `section-9.3.html`. Delete the "Builder's Deep Dive" paragraph pair, the "Practical Tool Choices For This Section" 5-row table, the generic `EvidenceRecord` dataclass and its printed placeholder output, and the "Failure Analysis Pattern" paragraph. Replace each with one short topic-specific failure example (9.4 and 9.5 already show the model: a tailored claim-separation block instead of a generic one).

2. **Replace the generic `EvidenceRecord` placeholder code in 9.1 and 9.2** with a runnable extension of that section's actual worked example (extend the trial-budget ledger in 9.1; extend the curriculum schedule in 9.2). The current code prints literal strings like "record after the perturbation run: sensor or state input", which is filler.

3. **Replace the formulaic epigraph in all Chapter 10, 12, 13 sections** with distinct topic-true lines. File set: all `section-10.*`, `section-12.*`, `section-13.*`. Draft for 10.1: "A `done` flag is a tombstone with no epitaph. `terminated` and `truncated` finally tell you the cause of death." Draft for 12.1: "A leaderboard number is a denominator you cannot see. Two rows only subtract if they share one."

4. **Trim the repeated "What This Section Builds" + "X Is The Test" intro scaffold** in Chapters 10, 12, 13 to one canonical per-chapter statement; open each section with section-specific framing instead. Highest payoff in Chapter 12 (6 sections, identical "treat the leaderboard as an instrument" callout).

5. **Update the part index** `part-3-simulation-tooling-and-the-modern-stack/index.html` to list all sections (add 10.6, 10.7, 11.6, 11.7, 11.8, 12.6, 13.6 to the chapter cards and the Production Spine through-line).

6. **Commission custom figure captions for Chapters 9, 10, 13** matching Chapter 12's cartoon-caption quality. File set: `section-9.*`, `section-10.1-10.5`, `section-13.*`. Replace the generic "is easier to reason about when the figure shows the concept, evidence path, and action consequence" caption.

7. **Add a Paper Spotlight to 13.3** naming OpenAI's Automatic Domain Randomization ("Solving Rubik's Cube with a Robot Hand", 2019) since the `update_friction_range` example IS the ADR controller; and a Paper Spotlight to 13.5 naming a current real2sim asset-reconstruction method (Gaussian-splatting / NeRF-to-sim digital twins). File: `section-13.3.html`, `section-13.5.html`. This makes the frontier feel current.

8. **Fix the `asdict` import bug in 11.4** (`section-11.4.html`): `TaskContract.as_row` calls `asdict(self)` but only `dataclass` is imported. Add `from dataclasses import dataclass, asdict` or remove the unused `as_row` method.

9. **Reconcile 9.5's title** ("Benchmark environment map" in the file vs "The landscape of benchmark environments" in the part index) and **trim 9.5's overlap with 12.1** so the landscape-preview in Chapter 9 does not duplicate the full benchmark treatment in Chapter 12.

10. **Reduce the evidence-rule callout density**: keep one rich statement per chapter (e.g. the "Part III Evidence Rule" in the part index plus one per-chapter callout), and convert the per-section repeats into a one-line back-reference. Affects every chapter; biggest gain in Chapters 9, 12, 13.

## Structure Suggestions for This Part

- **Chapter 9 should be the shortest chapter and the least template-heavy, but currently it is the most boilerplate-laden.** After cutting the `production-depth-expansion` blocks, 9.1-9.3 will be lean and strong. Consider merging 9.5 ("landscape of benchmark environments") forward into Chapter 12 as a short opener, since Chapter 12 is the real benchmark chapter and 9.5 currently previews it in full. That would tighten Chapter 9 to four focused sections (cost, roles, fidelity, reality gap) that flow directly into Chapter 11's simulators.

- **Chapters 11 and 12 are excellent and should be the template for the rest of the book.** No structural change needed; they demonstrate that the no-boilerplate, current-facts, runnable-code standard is achievable in this codebase.

- **Verify the part-index section list against the actual files** (7 sections omitted). This is a correctness issue, not just polish: readers navigating from the part index will miss a third of the content.

- **No chapter should be dropped.** All five carry distinct, necessary material (economics, environment contracts, simulators, benchmarks, synthetic data). The work is trimming repetition, not removing topics.
