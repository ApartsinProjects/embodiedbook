# Part 1 Content Audit: Foundations of Embodied AI

## Part Overview

Part 1 is two books wedged into one. Chapter 1 (8 sections) is publication-grade: every section frames a problem before its solution, derives real results (the O(eps*T^2) compounding penalty, the 1/(loop gain) disturbance-rejection law, the CMDP-vs-penalty distinction, the reality-gap functional Delta), ships correct topic-specific runnable code, names current systems (OpenVLA, pi-0, MuJoCo Warp 2025, Isaac Lab, LeRobot), and states open problems precisely. Chapters 2 and 3 (16 sections) are built on the OLD generated-template scaffold the lean section contract explicitly forbids: "Reader Pathway", "What This Section Develops", "Mechanism", "Worked Example", "Builder's Deep Dive", "Practical Tool Choices For Section X", "Implementation Recipe", "Teaching Move", "Failure Analysis Pattern", and an "evidence artifact" lab in every chapter index. In chapter 3 the boilerplate is so mechanical that whole paragraphs read "Formally, [TOPIC NAME] should be placed inside the closed-loop transition o_t -> s_hat_t -> a_t -> o_{t+1}", failing the non-substitutability rule on sight.

The core problem is unevenness, not a lack of good material. Chapters 2 and 3 each contain a genuinely strong, topic-specific core (one "Theory" paragraph + one comparison table + one "Failure Analysis" tail + a witty Fun Note) buried under ~70 percent reusable filler. The fix is not a rewrite from zero: it is to keep the topic-specific cores, promote chapter 1 to the structural template for the whole part, and delete the scaffold.

## Fun Elements to Preserve

These witty lines and epigraphs are genuine assets and must survive any edit:

Chapter 1 epigraphs (all strong, all topic-specific):
- Ch1: "The robot does not get to choose its next input. Its last action already did."
- 1.1: "A classifier answers a question once. An embodied agent answers, then inherits the consequences."
- 1.2: "I sensed, therefore I acted. Then I had to sense what acting had done."
- 1.3: "Interfaces matter because the agent can only act on what the experiment lets it see and do."
- 1.4: "Simulation gives you replay. Hardware tells you which assumptions survived contact."
- 1.5: "Physical AI is a transfer claim. The body decides how much of the claim survives."
- 1.6: "The loop is shared. The body sets the clock and the price of being wrong."
- 1.7: "The agent cannot see the whole state, cannot wait out the horizon, cannot explore into failure, and cannot collect mistakes for free."
- 1.8: "A good map does not tell you everything. It tells you where the next failure belongs."

Chapter 1 callouts to keep:
- 1.1 "Warehouse picking: accuracy went up, throughput went down" (the transparent-packaging recovery story; the single best worked anecdote in the part).
- 1.4 "Sim success is not capability" warning (the gripper interpenetration / soft-contact artifact list).

Chapter 2 fun:
- 2.1 epigraph: "The environment is the part of the experiment that gets a vote after every action." (excellent)
- 2.1 Memorable Shortcut: "If the environment wrapper cannot explain why an episode ended, it is not a benchmark yet. It is a suspense story with a CSV file."
- 2.2 epigraph: "My camera saw the block. My gripper discovered the friction. My log finally admitted both were incomplete."
- 2.2 Memorable Shortcut: "ask it where the object mass is hiding. The answer is usually 'in the failure case.'"
- 2.3 epigraph: "Choosing an action space is how you tell a robot what kinds of mistakes it is allowed to make." (excellent)
- 2.3 Memorable Shortcut: action space "is like a steering wheel: too small and you cannot maneuver, too large and the learner spends half the drive discovering the curb."
- 2.4 epigraph: "The robot maximized the reward exactly as written. That was the first problem." + author card "A Reward Designer With New Gray Hair."
- 2.4 Memorable Shortcut: "Reward is a suggestion written in math. Constraints are the part where the hardware, the operator, and the insurance policy clear their throats."
- 2.5 epigraph: "The robot did the right thing eventually. The evaluator had already gone home." + "An episode without a horizon is like a meeting without an end time."
- 2.6 epigraph: "The Bellman equation is what happens when a robot asks, 'and then what?' with mathematical persistence." + "The Markov property is a strict roommate: it does not want the full past on the couch, but it does expect the current state to bring all relevant luggage."
- 2.7 Fun Note: "A belief state is not what happened. It is the agent's best spreadsheet about what might have happened."
- 2.8 Fun Note: "The world does not provide a debug console. It provides shadows, delays, and one suspicious noise behind the robot."

Chapter 3 fun (the Fun Notes are the best-written lines in the chapter and must be preserved through any de-boilerplating):
- 3.1: "The canonical stack is a relay race where every runner blames the previous handoff until the robot misses the grasp."
- 3.2: "A modular pipeline is wonderfully debuggable right up to the moment every module insists the bug belongs next door."
- 3.3: "End-to-end learning removes the hand-coded middle. It also removes several convenient places to point when the robot gets creative."
- 3.4: "Hierarchy is how a robot says 'make coffee' without sending 40,000 individual motor commands to the meeting invite."
- 3.5: "Reactive agents have excellent reflexes. Deliberative agents have excellent reasons for being late."
- 3.6: "System 1 grabs the cup. System 2 asks whether it was supposed to be the blue cup after all."
- 3.7: "An LLM can explain the plan, a VLM can point at the object, and a VLA is where the explanation has to survive contact with the gripper."
- 3.8: "Architecture diagrams look tidy because they do not include the arrow labeled 'everyone assumed someone else checked that'."

## Chapter-by-Chapter Analysis

### Chapter 1: From Static AI to Embodied AI
**Quality**: EXCELLENT

The chapter index is a model: real "Confluence, Not a Branch" lineage (Wiener, Brooks, Moravec, Pfeifer/Bongard), a genuine embodiment spectrum, exit competencies that are testable, and an annotated bibliography. No template filler. All 8 sections clear the lean contract.

#### Section 1.1: Static prediction vs. embodied interaction - EXCELLENT
**Lens 1 (Deep Explanation)**: PASS. Defines the formal object change (function on fixed D vs. policy in a controlled Markov process), motivates via tau ~ pi, derives the horizon penalty (O(eps*T) static vs O(eps*T^2) closed-loop, attributed to Ross/Gordon/Bagnell), and states when point accuracy misleads (reversibility weighting). Assumptions and regime explicit.
**Lens 2 (Research Frontier)**: PASS. OpenVLA and pi-0 named as predictor-controller collapse; open question stated precisely (calibration under shift/latency/contact, cost of on-policy correction); action chunking and flow-matching heads named as current partial answers.
**Lens 3 (Fun/Engagement)**: Strong epigraph; "the action changes the dataset" insight box; warehouse-picking anecdote is the part's best aha moment. No gap.
**Lens 4 (Examples/Analogies)**: PASS. Runnable compounding simulation is correct and topic-specific (not filler). Library-shortcut to gymnasium episode semantics is the right "right-tool payoff."
**Lens 5 (Teaching Flow)**: PASS. Two real exercises, clean What's Next into 1.2.

#### Section 1.2: Why intelligence needs a world; the perception-action loop - EXCELLENT
**Lens 1**: PASS. Open-loop vs closed-loop stated as a_t = pi(y_{0:t}); recursive Bayes belief update derived; the scalar plant y_inf algebra carried all the way to the 1/(loop gain) disturbance-rejection result. Regime stated (stability bound |a - bK| < 1).
**Lens 2**: PASS. Frontier = learned world models (Dreamer line, V-JEPA), framed against Ashby's requisite-variety bound. Precise open question.
**Lens 3**: Strong cybernetic-lineage narrative (Wiener, Ashby, Powers, Brooks). Good epigraph.
**Lens 4**: PASS. The open-loop-fails/feedback-corrects demo prints concrete numbers (90.5 percent rejection) tied back to the derived offset. python-control library shortcut is correct.
**Lens 5**: PASS. Exercise 1.2.1 sweeps gain and induces divergence at the predicted K; exercise 1.2.2 is a transfer task.

#### Section 1.3: Agents, environments, observations, actions, rewards, constraints - EXCELLENT
**Lens 1**: PASS. MDP -> POMDP -> CMDP developed in order with the load-bearing assumption (Markov) flagged; the constraint-vs-penalty distinction (r - lambda*c buys back safety; CMDP keeps c on its own budget line) is exactly the graduate-level subtlety the audience needs.
**Lens 2**: PASS. Frontier = reward/constraint specification, inverse constrained RL, safe exploration during training. Open question stated.
**Lens 3**: Good epigraph; "Reward names preference; cost names a boundary" is memorable.
**Lens 4**: PASS. The Reach1D Gymnasium env is real, topic-specific code that instantiates POMDP (noisy obs != state) and CMDP (cost on info channel, not reward) simultaneously. Note: my text extraction garbled one line (the `crossed = ...` wall-collision test) but inspection of the raw HTML shows the entity-escaped source is intact; verify it renders/runs as part of any edit pass.
**Lens 5**: PASS. Two exercises both build directly on the env.

#### Section 1.4: Physical vs. simulated embodiment - GOOD (one real defect)
**Lens 1**: PASS. Reality gap Delta(pi) = J_sim - J_real defined as a measurable quantity; three fidelity dimensions (physical/visual/behavioral) separated, plus a fourth (temporal) in the table; identification-vs-randomization tradeoff developed.
**Lens 2**: PASS. Frontier = real2sim2real, 3D Gaussian Splatting, generative world models; current tooling (MuJoCo Warp 2025, Newton, Isaac Lab) is up to date.
**Lens 3**: Strong "Sim success is not capability" warning. Good epigraph.
**Lens 4**: PASS. The 1D braking-controller reality-gap demo prints J_sim=1.00, J_real=0.02, Delta=0.98, with the overshoot mechanism shown.
**Lens 5**: ISSUE. The section has a duplicated tail: two "Key Takeaway" blocks and three "Exercise 1.4.1" references. After the first (correct) Key Takeaway + Exercise 1.4.1 + Exercise 1.4.2, a SECOND Key Takeaway ("Simulation and hardware answer different evidence questions...") and a redundant, shorter "Exercise 1.4.1" (the slip/missed-contact perturbation task) appear. This is leftover generated content that escaped a merge.
- Fix: delete the second Key Takeaway and the duplicate "Exercise 1.4.1" (lines after the first Exercise 1.4.2). Keep the original Key Takeaway, Exercise 1.4.1 (domain-randomization sweep) and Exercise 1.4.2 (reality-gap budget). If the slip/missed-contact prompt is worth keeping, renumber it Exercise 1.4.3 and reword so it is not a near-duplicate of 1.4.2.

#### Section 1.5: The "Physical AI" framing and why 2023-2026 changed the field - EXCELLENT
**Lens 1**: PASS. "Physical AI" reduced to a falsifiable transfer hypothesis with the abstraction a_t = g_theta(phi_theta(o_t, l_t), e); the five enablers each given a concrete mechanical cause and a compounding argument.
**Lens 2**: PASS. The strongest currency in the part: Isaac Gym/Lab, MJX, RT-2, Open X-Embodiment/RT-X, ALOHA/Mobile ALOHA, GELLO, UMI, LeRobot, OpenVLA, Octo, pi-0, all dated and tied to the enabler they evidence. Demonstrated-vs-vendor-demo distinction is exactly right for this audience.
**Lens 3**: "demos are existence proofs, not reliability claims" is a memorable, true line.
**Lens 4**: PASS. The transfer-audit snippet (representation_only vs representation_and_control) deliberately carries no performance numbers to force the reader to name the transferred layer; the end-effector swap example (gripper -> suction) is concrete and from real practice.
**Lens 5**: PASS. One substantial exercise (classify a recent system by enabler, separate replicated from demo).

#### Section 1.6: Examples (vacuum, drone, AV, manipulator, humanoid, game agent) - EXCELLENT
**Lens 1**: PASS. Each body read off the tuple E = (O, A, dt, k, H, kappa) with concrete rates (Franka 1 kHz, PX4 250-1000 Hz, Lee et al. 50 Hz policy over ~1 kHz PD). Cross-rate-transfer warning is the key insight.
**Lens 2**: PASS. Frontier = generalist policies across the whole spectrum; honest about what transfers (intent) vs what does not (dt and kappa).
**Lens 3**: Good. Game-agent kappa ~ 0 contrast is a clean aha.
**Lens 4**: PASS. Table 1.6.1 is real and comparative; the code tabulates the six tuples and computes the rate span.
**Lens 5**: PASS. Minor: this section has no hero illustration (only sections 1.1-1.5 carry chapter-01-illustration images; 1.6-1.8 rely on inline SVG concept diagrams). Not a defect, just an asymmetry worth noting if illustrations are being standardized.

#### Section 1.7: Why embodied AI is hard - EXCELLENT
**Lens 1**: PASS. Seven obstacles each with a formal cause (POMDP value-function piece growth, return variance ~ T, O(eps*T^2), constrained exploration, phase lag omega*tau_d, ||P - P_hat||, reward hacking) and a forward pointer to the chapter that addresses it. "Obstacles multiply, they do not add" is the load-bearing synthesis.
**Lens 2**: PASS. Frontier = long-horizon sparse-reward credit assignment and safe real-world exploration named as least-solved; honest that progress "routes around" via simulation and reopens sim-to-real.
**Lens 3**: Strong epigraph; the difficulty-profile framing is itself engaging.
**Lens 4**: PASS. The obstacle-scoring diagnostic snippet routes effort to the dominant term and points at chapters.
**Lens 5**: PASS. Two exercises, both build the diagnostic habit.

#### Section 1.8: Map of the book - EXCELLENT (for a map section)
**Lens 1**: PASS. Organizes 12 parts as the closed loop expanded and laid flat; each part's dependency stated.
**Lens 2**: N/A (navigation section); still names frontier chapters (34-35, 36-41, 56-58).
**Lens 3**: Good epigraph; "Read the loop, not the index" is a clean device.
**Lens 4**: PASS. Two concrete reading paths (practitioner / researcher) and an appendix-consultation guide.
**Lens 5**: PASS.

### Chapter 2: The Agent-Environment Interface
**Quality**: NEEDS WORK (strong cores, heavy template scaffold)

The chapter INDEX is pure boilerplate: epigraph "An agent becomes interesting at the exact moment the world refuses to be a dataset" and author card "A Patient Embodied AI Agent" are reused verbatim as the Chapter 3 index. "Chapter 2 develops The Agent-Environment Interface as a working piece of the embodied AI stack" is the swap-the-name template. The index also carries a full generic "Hands-On Lab: Build the Chapter Evidence Artifact", "Production Notes For Readers", "Instructor And Builder Notes", "Readiness Check", "Teaching Takeaway" - none topic-specific. Cross-chapter bibliography problem (see below): every section repeats the same 3 references (Bellman 1957, Kaelbling 1998, Gymnasium docs) regardless of topic.

The sections themselves split into two tiers. Tier A (real theory + correct topic-specific code): 2.2, 2.4, 2.6, 2.7 have genuine derivations (belief update, metric factorization, Bellman backup, discrete POMDP posterior with printed numbers). Tier B (thinner): 2.1, 2.3, 2.5, 2.8. All eight carry the forbidden scaffold sections.

#### Section 2.1: Agents and environments formally - GOOD
**Lens 1**: PASS on substance. The reset/step contract, terminated-vs-truncated distinction, and "the interface is the experiment" point are correct and important. But wrapped in "Reader Pathway", "What This Section Develops", "Mechanism", "Builder's Deep Dive" template headers.
**Lens 2**: WEAK. "Research Frontier" paragraph is generic ("interfaces rich enough for robot data, multi-camera observations, action chunks"); no paper named, no precise open question.
- Fix: replace with a concrete frontier note: "Open robot-data formats are converging (LeRobotDataset, RLDS used by Open X-Embodiment); the unresolved problem is a shared episode contract that carries multi-rate sensor streams, action chunks, and safety-monitor state without forcing every body onto one observation schema. Cite Open X-Embodiment (2023) and the Gymnasium termination/truncation API change as the live design tension."
**Lens 3**: "suspense story with a CSV file" line is a keeper. Good epigraph.
**Lens 4**: PASS but thin. Code 2.1.1 is a real 1D right/left stepper with a Transition dataclass; correct but toy. Acceptable as a contract demo.
**Lens 5**: ISSUE. Too many pacing devices doing the same job: Reader Pathway + What This Section Develops + Self Check + Builder's Deep Dive + Teaching Move + Failure Analysis Pattern + Implementation Recipe + Mini Lab all restate "log the full transition tuple." Collapse to one frame paragraph + theory + code + 2-4 failure modes + one exercise.
- Fix: delete Reader Pathway, What This Section Develops, Action Is The Test, Self Check, Teaching Move, Implementation Recipe, Practical Tool Choices table; merge the surviving content into the lean shape used in chapter 1.

#### Section 2.2: State, observation, hidden variables, partial observability - GOOD
**Lens 1**: PASS. State-as-sufficient-statistic vs observation-as-evidence is defined cleanly; the variable ledger (observed/estimated/delayed/hidden/evaluator-only) is genuinely useful and topic-specific; the leak-test idea (evaluator-only variable in policy input) is a real practice.
**Lens 2**: WEAK. Frontier paragraph generic; name the concrete tension: learned latent state in robot foundation models vs. legibility for safety monitors. Cite a world-model paper (DreamerV3) and a recurrent-policy result.
**Lens 3**: "where the object mass is hiding... in the failure case" is excellent. Keep.
**Lens 4**: PASS. The occlusion-during-grasp anecdote (last-seen pose + elapsed time + confidence) is concrete and from practice.
**Lens 5**: Same scaffold-overload issue as 2.1.

#### Section 2.3: Action types: discrete, continuous, symbolic, motor-level, chunked - GOOD
**Lens 1**: PASS on substance. "Action space is architecture" (which layer owns intelligence) is the right framing; chunking-delays-correction is the key tradeoff. But "Theory" is a list of A examples, not a derivation; could state the exploration/sample-complexity consequence formally.
- Fix: add one quantitative sentence: discrete A of size n has tabular exploration cost ~ n per state; a d-dim continuous box needs function approximation and gradient signal; a chunk of length k commits k steps and so trades inference rate 1/k against correction latency k*dt. This makes "not the same learning problem" concrete.
**Lens 2**: WEAK. Frontier names VLA/diffusion/flow "fashions" without a precise open question. State one: what is the optimal chunk length as a function of contact bandwidth and latency budget, and why current VLAs pick it empirically.
**Lens 3**: steering-wheel analogy is accurate and memorable. Good epigraph.
**Lens 4**: ISSUE. The section's bibliography is Bellman/Kaelbling/Gymnasium, which is wrong for an action-representation section. It should cite ALOHA/ACT (action chunking), Diffusion Policy (Chi 2023), and pi-0 (flow-matching action head). Code 2.3.1 (four action representations) is topic-relevant.
**Lens 5**: This section ALSO carries a full "Hands-On Lab: Audit An Action Interface" with 4 numbered code-fragment steps on top of all the other scaffold. Heaviest boilerplate load in chapter 2.

#### Section 2.4: Rewards, goals, costs, constraints - GOOD
**Lens 1**: PASS. The four-field separation (goal / reward / cost vector / hard constraint) and the tradeability distinction are correct and match the CMDP treatment in 1.3 (good intra-part consistency). "Do not hide safety in a scalar" is the right warning.
**Lens 2**: PASS-ish. Frontier names safe RL, preference learning, control barrier functions, runtime assurance - real, but no paper cited and no single sharp open question.
**Lens 3**: "the insurance policy clear their throats" is a keeper. Strong epigraph + author card.
**Lens 4**: PASS. Code 2.4.1 scores two episodes where the higher-reward one violates a constraint - exactly the right demonstration.
**Lens 5**: Scaffold overload; same fix.

#### Section 2.5: Episodes, horizons, trajectories, discounting - GOOD
**Lens 1**: PASS. Discounted return formula with worked numbers (gamma=0.95 -> 0.708 vs gamma=0.5 -> 0.100) showing how discount changes the learned behavior (patient recovery vs risky shortcut). Truncation-vs-termination accounting is correct.
**Lens 2**: WEAK. Generic frontier ("action chunking, memory, subgoals, world models").
**Lens 3**: "meeting without an end time" analogy works. Good epigraph.
**Lens 4**: PASS. Code 2.5.1 computes return while preserving ending flags.
**Lens 5**: ISSUE. The "Reader Pathway" here is the literal fill-in-the-blank template: "identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign." This exact sentence appears in 2.5, 2.6, 3.1-3.8. It is the clearest non-substitutability failure in the part. Delete on sight everywhere it appears.

#### Section 2.6: Markov decision processes; Bellman equations - GOOD
**Lens 1**: PASS, strongest in chapter 2. (S,A,P,R,gamma) tuple, the fixed-policy Bellman backup written out, and the load-bearing-assumption discussion (if actuator wear / contact / past collisions change the next transition, the state is not Markov and the Bellman target mixes incompatible situations). The "add gripper contact + last velocity to the state" anecdote grounds it.
**Lens 2**: WEAK. Frontier generic (model-based RL / world models relax hand-specified transition models). Add a precise open question: when a learned latent state is used as the Bellman state, what guarantees the Bellman operator remains a contraction? This is a real, citable open issue.
**Lens 3**: "strict roommate" analogy is accurate and memorable. Strong epigraph.
**Lens 4**: PASS. Code 2.6.1 does tabular backups on a 3-state reach MDP with correct printed values (far=0.8, near=1.0, done=0.0) and the arithmetic explained.
**Lens 5**: ISSUE. The "Implementation Recipe", "Practical Tool Choices For Section 2.6" (Gymnasium/PettingZoo/ROS 2 with the SAME advice string three times), and "construct-matched evidence schema" code (Code 2.6.2, a dict literal) are pure filler. The Code 2.6.2 evidence-schema dict adds nothing a reader can run or learn from.

#### Section 2.7: Partially observable MDPs; belief states - GOOD
**Lens 1**: PASS. (S,A,P,R,Omega,O,gamma) tuple, the one-step belief update with normalizer eta written out, predict-observe-correct mechanism. The dry/slippery contact example with a force-spike likelihood is genuinely topic-specific.
**Lens 2**: WEAK-to-OK. Frontier (legible latent beliefs for safety monitors) is a real direction; sharpen with a citation.
**Lens 3**: "best spreadsheet about what might have happened" is a keeper.
**Lens 4**: PASS. Code 2.7.1 prints a real posterior (dry 0.263, slippery 0.737) and walks prior -> predicted -> corrected.
**Lens 5**: ISSUE. Carries BOTH the standard scaffold AND a full "Hands-On Lab: Build a Section Evidence Trace" with 4 numbered steps whose code fragments are described as "records Step 1... and reports that the evidence fields are concrete" - placeholder labs, not runnable teaching code. Delete the lab; keep the belief-update worked example and one real exercise.

#### Section 2.8: Why embodiment is usually partially observable - GOOD
**Lens 1**: PASS. The occlusion/contact/latency/other-agent taxonomy of hidden-state sources is correct and the "active perception" mechanism (act to change what can be known) is the right concept.
**Lens 2**: OK. Frontier (passive -> active perception, deciding when to change viewpoint / touch / wait / ask) is concrete.
**Lens 3**: "shadows, delays, and one suspicious noise behind the robot" is a keeper.
**Lens 4**: PASS. Code 2.8.1 maps four hidden-state sources to evidence fields and action modes (probe_first vs act_with_monitor); a useful checklist artifact.
**Lens 5**: Same scaffold overload + the generic evidence-schema code (2.8.2).

### Chapter 3: Embodied System Architectures
**Quality**: POOR (genuine cores exist but the boilerplate ratio is ~70 percent)

This chapter is the most template-driven in the part and fails the non-substitutability rule paragraph after paragraph. Every section uses the identical skeleton: epigraph "[TOPIC] matters when the next action changes the evidence you thought you had" + author card "A Careful Control Loop" + Big Picture ("[TOPIC] is one lens on embodied system architectures. We study it because an embodied agent needs decisions that survive contact with noisy sensors...") + Reader Pathway (the fill-in-the-blank sentence) + What This Section Develops + Action Is The Test + Theory (first two paragraphs are templated: "Formally, [TOPIC] should be placed inside the closed-loop transition o_t -> s_hat_t -> a_t -> o_{t+1}") + Mechanism ("The mechanism in [TOPIC] is the contract between representation and action") + Worked Example (templated, the code fragment captioned "turns [TOPIC] into an executable trace") + Library Shortcut + Practical Recipe (identical 5 bullets) + Common Failure Mode (identical) + Self Check + Builder's Deep Dive (identical) + Practical Tool Choices For Section 3.X (ROS 2 / MuJoCo / LeRobot with the SAME advice string thrice) + Implementation Recipe (identical) + Teaching Move + Failure Analysis Pattern + Key Takeaway ("[TOPIC] is useful when it makes the perception-action loop more reliable, not when it merely adds a more impressive model name") + Exercise ("Design a method-matched experiment for [TOPIC]"). Every section shares the same 3-reference bibliography (ROS / MuJoCo / RT-2).

What is real and worth keeping in each section: (1) ONE topic-specific Theory paragraph (the second one), (2) the Fun Note, (3) the topic-specific Failure Analysis tail paragraph, and (4) in 3.7 and 3.8 a genuinely good comparison table.

#### Section 3.1: The canonical stack - NEEDS WORK
**Lens 1**: PARTIAL. The real content is the pipeline equation o_t -sense-> x_t -perceive-> y_t -estimate-> s_hat_t -predict-> s_hat_{t+1:t+H} -plan-> tau_t -control-> a_t -act-> o_{t+1} with each symbol defined, and the "breaks down when one stage silently changes units, frames, latency, uncertainty" point. That single paragraph is good. Everything around it is templated.
**Lens 2**: FAIL. "Research Frontier" is the generic "treat frontier claims as hypotheses" sentence. No paper, no open question.
**Lens 3**: relay-race Fun Note is a keeper.
**Lens 4**: FAIL. Code 3.1.1 is elided/placeholder ("turns the canonical stack into an executable trace"); 3.1.2 is the evidence-schema dict. Neither is a real worked example of a 7-stage pipeline.
- Fix: replace with a runnable mini-pipeline: noisy sensor -> simple perceive (threshold) -> 1D Kalman estimate -> 1-step predict -> greedy plan -> P controller -> act, printing the value carried at each arrow and a frame/units annotation, so the "silent handoff" failure can be demonstrated by corrupting one stage.
**Lens 5**: FAIL on pacing economy: ~15 scaffold headers for one real idea.

#### Section 3.2: Classical modular robotics pipeline - NEEDS WORK
**Lens 1**: PARTIAL. Real content: the module contract is more than a datatype - (pose, Sigma, frame, t, confidence) - and "interface optimism" (every module correct under its own assumptions, combined assumptions cannot all hold). That is a genuine, useful idea. The Failure Analysis tail ("Which interface accepted a value it should have rejected?", covariance/timestamp reveals stale evidence) is also real and good.
**Lens 2**: FAIL. Generic frontier sentence.
**Lens 3**: "the bug belongs next door" Fun Note is a keeper.
**Lens 4**: FAIL. Placeholder code; needs a real two-module handoff demo where a stale-timestamp pose passes a type check but fails the covariance/age gate.
**Lens 5**: Carries the standard scaffold PLUS a full placeholder Hands-On Lab.

#### Section 3.3: End-to-end learned policy pipeline - NEEDS WORK
**Lens 1**: PARTIAL. Real content: a_t = pi_theta(o_{<=t}, g) with the loss family (regression / cross-entropy on action tokens / diffusion denoising) and the representation-freedom-vs-diagnostic-opacity tradeoff. The Failure Analysis tail (nearest-neighbor audit of the training set: coverage vs representation-alignment vs temporal-window diagnosis) is genuinely good and topic-specific.
**Lens 2**: FAIL. Generic frontier; should cite RT-2/OpenVLA/Diffusion Policy and state an open question (e.g. how to attribute a closed-loop failure to coverage vs. architecture without on-robot ablation).
**Lens 3**: "convenient places to point when the robot gets creative" Fun Note is a keeper.
**Lens 4**: FAIL. Placeholder code.
**Lens 5**: scaffold overload.

#### Section 3.4: Hybrid and hierarchical architectures - NEEDS WORK
**Lens 1**: PARTIAL but the real content is strong: the options framework omega = (I_omega, pi_omega, beta_omega) with initiation set, intra-option policy, and termination, plus the conditions for it to work (meaningful skill boundaries, observable termination, no impossible preconditions). The Failure Analysis tail (high-level selects "open drawer" with gripper misaligned; low-level reports success after moving the handle without opening) is concrete.
**Lens 2**: FAIL. Generic frontier; should cite Sutton/Precup/Singh options (1999) and a modern HRL or skill-chaining result, and state an open question on learned termination conditions.
**Lens 3**: "without sending 40,000 individual motor commands" Fun Note is a keeper.
**Lens 4**: FAIL. Placeholder code; needs a real 2-level option demo.
**Lens 5**: scaffold overload.

#### Section 3.5: Reactive vs. deliberative agents - NEEDS WORK
**Lens 1**: PARTIAL. Real content: reactive a_t = pi(o_t) vs deliberative argmax over an H-step model rollout, with the timing-decision framing ("not a personality type") and the trap example (push object into a corner before grasping). The Failure Analysis tail (vary deadline and lookahead-need separately; if both tests show the same behavior the architecture lacks the separation it claims) is a real diagnostic.
**Lens 2**: FAIL. Generic frontier.
**Lens 3**: "excellent reasons for being late" Fun Note is a keeper.
**Lens 4**: FAIL. Placeholder code; needs a gridworld where a reflex collides and a 1-step lookahead avoids the trap.
**Lens 5**: scaffold overload.

#### Section 3.6: Dual-system (System 1 / System 2) designs - NEEDS WORK
**Lens 1**: PARTIAL. Real content: the routing rule route(o_t) = System 1 if u(o_t) < tau and r(o_t) < rho else System 2, with u as uncertainty, r as risk, the measurability assumption, and the false-confidence failure mode. The Failure Analysis tail (diagnose the router before either subsystem; log uncertainty/risk/path/deliberation-time; examine near-threshold cases) is good. Note: my text extraction truncated the routing cases block; verify the KaTeX cases environment renders correctly in the raw HTML.
**Lens 2**: FAIL. The section's intellectual root (Kahneman, Thinking Fast and Slow) is named in the title but NOT cited; the bibliography is ROS/MuJoCo/RT-2. Should cite Kahneman and a robotics dual-system paper (e.g. the System-1/System-2 framing in recent VLA-plus-planner work).
**Lens 3**: "asks whether it was supposed to be the blue cup" Fun Note is a keeper.
**Lens 4**: FAIL. Placeholder code; needs a real router demo sweeping the threshold.
**Lens 5**: scaffold overload.

#### Section 3.7: Where LLMs, VLMs, and VLAs sit in the stack - NEEDS WORK (best in chapter)
**Lens 1**: GOOD core. The interface table (model family / typical input / typical output / interface risk) is genuinely useful and topic-specific: LLM may produce ungrounded plans, VLM may miss geometry/contact/timing, VLA may hide action scaling and recovery logic. The reframe ("not which model is most capable, but which interface needs learned generalization vs an explicit contract") is exactly right for the audience.
**Lens 2**: FAIL on form. The CONTENT is current (LLM/VLM/VLA roles) but no papers cited beyond the shared RT-2; should cite SayCan/PaLM-E (LLM planner), an open VLM, OpenVLA/pi-0 (VLA), and state the open question (verification between stages).
**Lens 3**: "where the explanation has to survive contact with the gripper" is the best Fun Note in the part.
**Lens 4**: GOOD. The oracle-substitution Failure Analysis (replace one model output with a verified value to localize the fault) is a real, reusable technique. Worked-example code is still placeholder though.
**Lens 5**: scaffold overload around a strong table.

#### Section 3.8: Failure modes of each architecture - NEEDS WORK (strong content, heavy scaffold)
**Lens 1**: GOOD core. The "Failure Signatures By Architecture" table (architecture / likely first suspect / evidence to inspect / best perturbation) is the single most useful artifact in chapters 2-3 and ties the whole chapter together. The three-pass diagnostic (classify architecture -> one oracle substitution -> rerun across a panel; "a cause that flips one case is a clue, a cause that flips a panel is evidence") is excellent and matches the construct-matched-evidence discipline in the global style rules.
**Lens 2**: FAIL on form. No frontier note beyond generic; could point at automated failure attribution / root-cause tooling as an open area.
**Lens 3**: "the arrow labeled 'everyone assumed someone else checked that'" Fun Note is a keeper.
**Lens 4**: GOOD content, placeholder code.
**Lens 5**: Carries the full scaffold PLUS a placeholder Hands-On Lab on top of the two strong tables.

## Cross-Chapter Issues in This Part

1. Two incompatible production templates in one part. Chapter 1 = lean contract; chapters 2-3 = old generated scaffold (Reader Pathway / What This Section Develops / Mechanism / Worked Example / Builder's Deep Dive / Practical Tool Choices / Implementation Recipe / Teaching Move / Failure Analysis Pattern / evidence-artifact lab). This is the dominant issue and the reader will feel the quality cliff at the 1->2 boundary.

2. Non-substitutability failures are systemic in chapters 2-3. The sentences "Use this section to make [TOPIC] operational: identify the quantity or representation being carried, the interface that carries it through the embodied stack, and the failure evidence that would force a redesign" and "Formally, [TOPIC] should be placed inside the closed-loop transition o_t -> s_hat_t -> a_t -> o_{t+1}" appear verbatim across ~10 sections. By the contract's own rule, every such passage should be cut.

3. Boilerplate bibliographies. All of chapter 2 repeats Bellman 1957 / Kaelbling 1998 / Gymnasium; all of chapter 3 repeats ROS / MuJoCo / RT-2. Sections on action spaces (2.3), reactive/deliberative (3.5), dual-system (3.6), and VLA placement (3.7) cite none of their actual source literature. Chapter 1, by contrast, has correct per-section references.

4. Placeholder code in chapter 3. Where chapter 1 ships runnable, output-printing examples and chapter 2 ships small-but-real ones, chapter 3's "Worked Example" code fragments are described, not shown ("turns [TOPIC] into an executable trace"), and the second code fragment in each section is an evidence-schema dict literal that teaches nothing. This violates lean contract item 3.

5. Reused chapter-index identity. Chapter 2 and chapter 3 indexes share the same epigraph ("An agent becomes interesting at the exact moment the world refuses to be a dataset") and author card ("A Patient Embodied AI Agent"). Each needs its own.

6. Generic "Research Frontier" callouts. Chapters 2-3 mostly state "treat frontier claims as hypotheses" rather than naming a 2024-2026 result and a precise open problem. Chapter 1 does this well and is the model to copy.

7. Illustration asymmetry (minor). Chapter 1 sections 1.6-1.8 carry no hero illustration (only 1.1-1.5 use the 5 chapter-01 images); all of chapters 2-3 use inline SVG concept diagrams whose captions are themselves templated ("[TOPIC] is easiest to reason about as a closed-loop evidence, decision, consequence pattern").

## Top 10 Highest-Priority Fixes for This Part

1. De-scaffold chapter 3 (all 8 sections). For each of `module-03-embodied-system-architectures/section-3.1.html` through `3.8.html`, keep only: the epigraph, ONE frame paragraph (replace "X is one lens on embodied system architectures..." with a real opener), the topic-specific Theory paragraph + equation/table, a real worked example (see fix 3), the Fun Note, 2-4 topic-specific failure modes (mine the existing Failure Analysis tail), a precise Research Frontier with citations, one real exercise. Delete Reader Pathway, What This Section Develops, Action Is The Test, Mechanism, Self Check, Builder's Deep Dive, Practical Tool Choices For Section 3.X, Implementation Recipe, Teaching Move, and the evidence-schema code dicts.

2. Fix section 1.4 duplicate tail. In `module-01-from-static-ai-to-embodied-ai/section-1.4.html`, delete the SECOND "Key Takeaway" ("Simulation and hardware answer different evidence questions...") and the duplicate "Exercise 1.4.1" (slip/missed-contact) that follow the first Exercise 1.4.2. Keep the first Key Takeaway, Exercise 1.4.1 (DR sweep), Exercise 1.4.2 (reality-gap budget). This is a clean, high-value, low-risk fix.

3. Replace placeholder code in chapter 3 with one runnable example per section. 3.1: a 7-stage mini-pipeline that prints the value at each arrow and breaks when one stage corrupts a frame/unit. 3.2: a two-module handoff where a stale-timestamp pose passes a type check but a covariance/age gate rejects it. 3.3: a tiny BC policy vs an oracle, with a nearest-neighbor coverage audit on a held-out scene. 3.4: a 2-level option (high-level skill selector + low-level controller) with logged preconditions/termination. 3.5: a gridworld where a reflex hits a trap and 1-step lookahead avoids it. 3.6: a router sweeping the (tau, rho) thresholds and reporting safety/latency. 3.7: an oracle-substitution harness over LLM-plan / VLM-grounding / VLA-action stages. 3.8: code that computes the smallest single intervention that flips a failure across a panel.

4. De-scaffold chapter 2 (all 8 sections) to the lean shape, preserving the Tier-A theory and code in 2.2/2.4/2.6/2.7 and the epigraphs/memorable shortcuts everywhere. Delete the same scaffold list as fix 1, plus the per-section Hands-On Labs in 2.3 and 2.7.

5. Fix the bibliographies. Chapter 2: give each section its real sources (2.3 -> ALOHA/ACT, Diffusion Policy (Chi 2023), pi-0; 2.5 -> Sutton & Barto chapters on returns/discounting; 2.6 -> Puterman; 2.7 -> Kaelbling/Littman/Cassandra is correct, add a particle-filter ref). Chapter 3: 3.4 -> Sutton/Precup/Singh options (1999); 3.6 -> Kahneman (2011) + a robotics dual-system paper; 3.7 -> SayCan/PaLM-E, OpenVLA, pi-0; 3.2 -> a SLAM/Nav2 reference; 3.5 -> Brooks subsumption + an MPC reference.

6. Rewrite the chapter 2 and chapter 3 indexes. Give each a unique epigraph and author card (stop sharing "A Patient Embodied AI Agent"); replace "Chapter N develops X as a working piece of the embodied AI stack" with a real one-paragraph frame; delete the generic Hands-On Lab / Production Notes / Instructor And Builder Notes / Readiness Check blocks or replace them with chapter-specific content. Use the chapter 1 index as the template.

7. Upgrade every "Research Frontier" in chapters 2-3 to chapter-1 standard: one named 2024-2026 result + one precisely stated open problem. Highest value in 2.6 (Bellman contraction with learned latent state), 3.6 (dual-system routing calibration), 3.7 (inter-stage verification for LLM+VLM+VLA stacks).

8. Promote the two strong chapter-3 tables (3.7 model-interface table, 3.8 failure-signature table) to anchor their sections; build the surrounding prose around them rather than around the scaffold. The 3.8 three-pass diagnostic should become the chapter's closing synthesis.

9. Delete the repeated "Practical Tool Choices For Section X" tables across chapters 2-3 (Gymnasium/PettingZoo/ROS 2 or ROS 2/MuJoCo/LeRobot, each with the identical advice string three times). Replace with at most one sentence naming the one tool that matters for that topic, in the chapter-1 library-shortcut voice.

10. Add real worked examples / fix the templated SVG captions. The inline concept-diagram captions "[TOPIC] is easiest to reason about as a closed-loop evidence, decision, consequence pattern" are themselves boilerplate; rewrite each to describe what its specific diagram actually shows.

## Structure Suggestions for This Part

- Keep all three chapters and the 8+8+8 section split; the topic coverage and ordering are sound (static-vs-embodied -> interface formalism -> architectures is the right dependency chain, and 1.8's map confirms it).
- Chapter 2 section 2.6 (MDPs/Bellman) and 2.7 (POMDPs/belief) overlap heavily with chapter 1 section 1.3 (MDP/POMDP/CMDP). This is acceptable as deliberate reinforcement, but 2.6/2.7 should explicitly build on 1.3 rather than re-introducing the tuple from scratch; add a back-reference and push 2.6/2.7 deeper (value iteration convergence, belief-MDP piecewise-linear value function) so they are not a thinner repeat of 1.3.
- Consider merging chapter 3 sections 3.5 (reactive vs deliberative) and 3.6 (dual-system) if de-scaffolding leaves each too thin; the dual-system design IS the engineered resolution of the reactive/deliberative split, so they form one natural narrative. Only merge if, after fix 1, each cannot stand as a full lean section.
- No sections should be dropped. After de-scaffolding, every chapter-2 and chapter-3 section has enough topic-specific core (one theory result + one table or example + one real failure analysis + a Fun Note) to meet the lean contract; the work is subtraction of filler and addition of real code and citations, not removal of topics.
