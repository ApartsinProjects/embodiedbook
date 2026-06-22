# Part 4 Content Audit: Reinforcement Learning for Embodied Agents

## Part Overview

Part 4 is the strongest-engineered part of the book on a per-section basis: nearly every one of its 37 sections carries real, topic-specific mathematics (return recursion, Bellman backups, discounted occupancy, the policy-gradient baseline identity, GAE, the PPO clip ratio, TD3 double-critic targets, the SAC soft value, importance ratios, potential-based shaping, HER relabeling, the Bradley-Terry preference model, constrained-MDP objectives, distillation loss, transfer ratios) and a short runnable Python fragment that actually computes the quantity under discussion. The content authors clearly knew RL. The dominant problem is therefore not thin content; it is heavy, mechanical templating laid over good content. A fixed scaffold repeats in all 37 sections: an identical templated epigraph ("X matters when the next action changes the evidence you thought you had"), an identical chapter-index opening paragraph in all 7 modules, an identical 5-step "Practical Recipe" list, an identical "Common Failure Mode" warning, a 5-card bibliography whose annotations are find-and-replaced per section, and (in modules 16-20) a degraded class of fun-notes and exercises that collapse into "fill the evidence record / design a schema" boilerplate. The fix work is mostly de-templating and topic-specializing the connective tissue, not rewriting the science.

The second structural issue: the part is RL-broad but light on the embodied frontier specifics the stated audience (Boston Dynamics engineers, embodied-AI research scientists) would expect. Landmark papers are almost entirely absent from the body. Module 17 (GPU RL) names the real tools (Isaac Lab, RSL-RL, rl_games, SKRL, Brax, MJX) but does not cite the papers that made the field (Rudin et al. "walk in minutes", Margolis/Agarwal RMA, Lee et al. legged-robot-in-the-wild, Hwangbo ANYmal). Frontier callouts exist in every section but are written generically; only one section (17.1) carries an explicit "As of 2026" currency anchor.

## Fun Elements to Preserve

These are genuine, topic-specific witty/analogy callouts that must survive any de-templating edit. Listed by section:

- **14.1 (Memory Hook):** "Discounting is the robot's memory budget written as arithmetic."
- **14.2 (Fun Note):** "A policy is a steering wheel. A value function is the road sign that says what the next few turns are likely to cost." (clean, accurate analogy)
- **14.3 (Memory Hook):** "Exploration is the agent asking, 'What if I am wrong?' Exploitation is the agent acting as if its current answer is good enough."
- **14.4 (Memory Hook):** "The replay buffer has a point of view. Off-policy learning starts by asking whose point of view it is." (strong)
- **14.5 (Fun Note):** "The hardware asks for two receipts: what reward did you earn, and what did it cost to earn it?"
- **15.1 (Memory Hook):** "A stochastic policy is not indecisive. It is keeping receipts for the choices it made..." (strong)
- **15.2 (Memory Hook):** "REINFORCE is the policy's accountability system..."
- **15.3 (Fun Note):** "The critic is the agent's skeptical lab partner. It does not celebrate reward by itself; it asks whether the reward was better than the state already predicted." (excellent)
- **15.4 (Memory Hook):** "A trust region is the optimizer's reminder that one lucky rollout is not permission to reinvent the robot's gait in a single update." (excellent, topic-specific)
- **15.5 (Fun Note):** "PPO's paperwork is the method." (memorable and true)
- **15.6 (Memory Hook):** "A shaped reward is a note to the optimizer. Write it assuming the optimizer will read it literally and ignore every unstated intention." (excellent)
- **15.6 (Teaching Move):** "Ask readers to propose an exploit for every reward component they add." (great teaching device, keep)
- **17.1 (Memory Hook):** "Thousands of environments are a choir, not a crowd, if every reset sings the same note. The conductor is the seed schedule." (excellent, the best in the part)
- **17.2 (Fun Note):** "The simulator can teach walking in minutes, but it can also teach falling with excellent confidence intervals. Always read the reset reasons." (excellent)
- **17.3 (Memory Hook):** "The wrapper is the adapter plug on the robot-learning workbench. Label it, or the next debugger will spend an afternoon asking why the critic knew the terrain and the actor did not." (excellent)
- **17.4 (Fun Note):** "JAX is happiest when the experiment arrives wearing the same tensor shape every day. Surprise it with a new shape mid-run, and the compiler gets a vote." (excellent)
- **17.5 (Memory Hook):** "Privileged distillation is a tutoring session where the teacher can read the answer key, but the final exam confiscates it." (excellent)
- **17.6 (Memory Hook):** "The cheapest successful run is the one that reaches the target before curiosity turns into a hyperparameter sweep."
- **18.1 (Fun Note):** "The simulator may applaud every rollout, but the hardware still asks for the receipt..." (this is the SEED of the later overused line; here it is in-context)
- **18.2 (Memory Hook):** "Dense reward is the coach shouting from the sideline. Sparse reward is the scoreboard. Do not let the coach secretly move the goalposts." (excellent)
- **18.3 (Memory Hook):** "HER is the robot saying, 'I missed your target, but I did hit this other one. Please file that under useful experience, not victory.'" (excellent)
- **18.4 (Fun Note):** "A reward hacker does not break the rules. It reads the rules with the enthusiasm of a very literal lawyer and the patience of a machine." (excellent, the best one-liner on reward hacking in the part)
- **18.5 (Memory Hook):** "A reward model is a judge with a very large clipboard. The policy will eventually learn which boxes on the clipboard matter..." (excellent)
- **18.6 (Memory Hook):** "Reward says, 'get there.' Constraint cost says, 'and do not knock over the furniture on the way.'" (excellent)
- **19.2 (Memory Hook):** "Curiosity is a good intern and a poor manager. It should bring the agent to promising evidence, not set the entire company strategy." (excellent)
- **19.3 (Memory Hook):** "Safe exploration is the only place where 'nothing happened' can be a result, as long as the log proves that the right risky thing did not happen." (excellent)
- **19.4 (Fun Note):** "Partial observability is where 'I have seen this before' and 'this looks like something I have seen before' become dangerously different sentences." (excellent, captures perceptual aliasing)
- **20.3 (Memory Hook):** "Treat domain randomization... like a control-room label. If the label does not tell a future debugger what was sampled, what was measured, and what was adapted, it is decoration." (good)
- **Chapter epigraph (all 7 indexes):** "An agent becomes interesting at the exact moment the world refuses to be a dataset." (excellent thesis line for the whole part; keep at the part level, but it is repeated 7 times, which dilutes it - see Cross-Chapter Issues)

**Count of genuinely good fun elements worth preserving: 29.**

## Chapter-by-Chapter Analysis

### Chapter 14: Reinforcement Learning Refresher
**Quality**: GOOD

The cleanest chapter in the part. Five sections, each with correct math and a hand-verifiable code fragment. The progression (return -> policies/values -> exploration -> taxonomy -> embodied difficulty) is logical and the "What's Next" links chain correctly. Main drag: shared template boilerplate.

#### Section 14.1: Learning from interaction; return and discounting - GOOD
**Lens 1 (Deep Explanation)**: PASS on what/why/how. MDP and POMDP defined, return derived, backward accumulation shown and hand-checkable. Regime-of-validity (Markov assumption) is stated. Minor: the four-step return output is presented but the reader is told to "read from bottom to top" without the equation $G_2 = 2.0 + 0.9(-1.0) = 1.1$ spelled out for at least one step.
- Fix: add one inline line: "For example $G_2 = r_3 + \gamma r_4 = 2.0 + 0.9\times(-1.0) = 1.10$, matching the printed value."

**Lens 2 (Research Frontier)**: Frontier callout is generic ("combine long-horizon return objectives with foundation-model priors"). No paper named.
- Fix: anchor to a concrete artifact: "See the discount-horizon analysis in Amit et al. (2020) on $\gamma$ as a bias-variance control, and the long-horizon credit problem highlighted by RL foundation-model surveys (2024-2025)."

**Lens 3 (Fun/Engagement)**: Good Memory Hook (discounting as memory budget). The templated epigraph is weak. Opening "Big Picture" is solid.

**Lens 4 (Examples/Analogies)**: PASS. Mobile-manipulator grasp episode is topic-specific.

**Lens 5 (Teaching Flow)**: PASS. "Reader Pathway" + "What This Section Develops" are template boilerplate that violate the lean contract criterion 1 and should be merged into a single one-paragraph frame.

#### Section 14.2: Policies and value functions - GOOD
**Lens 1**: PASS. Bellman expectation equation given with the "recursive not circular" clarification, which is exactly the intuition graduate readers need. Charging-robot policy evaluation runs to a fixed point.
**Lens 2**: Frontier (value calibration under distribution shift for VLA policies) is genuinely current but uncited.
- Fix: name the offline-RL value-overestimation line (Kumar et al. CQL 2020) and a VLA example (RT-2, 2023; OpenVLA, 2024) to ground "operate far outside their demonstrations."
**Lens 3**: "policy is a steering wheel / value function is the road sign" is an accurate, keepable analogy.
**Lens 4**: PASS.
**Lens 5**: PASS, but same template-frame issue as 14.1.

#### Section 14.3: Exploration vs. exploitation - GOOD
**Lens 1**: PASS. Epsilon-greedy distribution written correctly with the $1-\epsilon+\epsilon/|\mathcal A|$ form (a detail many texts get wrong). The "budget for controlled ignorance" framing is strong.
**Lens 2**: Safe-exploration frontier is appropriate but generic.
- Fix: cite control-barrier-function safe RL (Cheng et al. 2019) and the constrained-policy-optimization line (Achiam et al. CPO 2017) since they are named obliquely later in 18.6/19.3.
**Lens 3**: Good Memory Hook. Missing an "aha": no mention that pure greedy can be provably trapped while UCB/Thompson achieve sublinear regret - a surprising-result hook is available here.
- Fix: add an Open Question / surprising-fact callout: "Epsilon-greedy has linear regret in the worst case; UCB and Thompson sampling achieve logarithmic regret. On hardware, neither bound prices in a broken gripper - the regret that matters is physical."
**Lens 4**: PASS (three grasp choices).
**Lens 5**: PASS.

#### Section 14.4: Model-free vs. model-based; on- vs. off-policy - GOOD
**Lens 1**: PASS, and notably good: the discounted occupancy measure $d_\gamma^\pi$ is introduced and computed, which is more rigorous than most refreshers. The "two independent axes" framing prevents the common model-free=off-policy confusion.
**Lens 2**: Offline-RL frontier present but uncited.
- Fix: name MOPO/MOReL (model-based offline, 2020), COMBO, and the D4RL benchmark so "exploit large prior datasets" has anchors.
**Lens 3**: "The replay buffer has a point of view" is one of the best hooks in the chapter.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 14.5: Why RL is hard in embodied systems - GOOD
**Lens 1**: PASS. Constrained-MDP objective stated. The three-policy reward-vs-safety audit is the most decision-relevant code in the chapter (rejects the highest-return policy on cost budget).
**Lens 2**: Frontier generic.
- Fix: cite the sample-cost reality directly (Haarnoja et al. real-world SAC on Minitaur 2018/2019; Smith et al. "walk in the park" 2022 - 20 minutes real-world).
**Lens 3**: "two receipts" Fun Note is good. The "wins-only lesson for deployment" paragraph is a nice nod to honest reporting.
**Lens 4**: PASS.
**Lens 5**: PASS. Good chapter-closing What's Next into Ch 15.

### Chapter 15: Policy Gradient Methods and PPO
**Quality**: EXCELLENT (content) / GOOD (after template tax)

The technical high point of the part. Six sections that build REINFORCE -> baseline -> actor-critic/GAE -> trust region/PPO -> implementation details -> shaping hazards. The math is correct and the code fragments compute the real quantities (GAE backward recursion, PPO clip min, baseline identity). The exercises in this chapter are the best in the part (algebraic baseline proof; compute ratios + clip fraction + approx KL).

#### Section 15.1: Direct policy optimization; stochastic policies - GOOD
**Lens 1**: PASS. "credit assignment through sampling... cannot differentiate through drawer physics... can differentiate through the policy's own probability" is exactly the right intuition, stated before the formalism.
**Lens 2**: Frontier names diffusion action generators (current) but no citation.
- Fix: cite Diffusion Policy (Chi et al. 2023) and the score-based action line; this is the live 2024-2025 frontier the audience cares about.
**Lens 3**: Strong "keeping receipts" hook.
**Lens 4**: PASS (softmax over move_left/right/stop; Gaussian over joint velocity).
**Lens 5**: PASS.

#### Section 15.2: The policy gradient theorem; REINFORCE - GOOD
**Lens 1**: PASS, strong. The baseline zero-bias identity is proven, not asserted ("it can be shown" is correctly avoided). This meets the graduate-depth bar.
**Lens 2**: Frontier OK; could name the variance-reduction lineage explicitly.
**Lens 3**: "accountability system" hook is good.
**Lens 4**: PASS.
**Lens 5**: PASS. The Teaching Move (prove baseline identity for 2 then K actions) is excellent.

#### Section 15.3: Actor-critic and advantage estimation (GAE) - EXCELLENT
**Lens 1**: PASS, best-in-part. $\lambda$ bias-variance tradeoff explained with the embodied time interpretation ("a foot placement caused a stumble three frames later"). GAE backward recursion is correct and runnable.
**Lens 2**: Frontier (asymmetric actor-critic, privileged critic) is genuinely current and the deployment question it poses is sharp.
- Fix: cite Pinto et al. asymmetric AC (2017) and Lee et al. (legged locomotion, Science Robotics 2020) for privileged-critic-into-deployable-actor.
**Lens 3**: "skeptical lab partner" critic analogy is excellent.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 15.4: Trust regions; TRPO to PPO - GOOD
**Lens 1**: PASS. Ratio definition and clipped surrogate are correct. The min-operation intuition ("removes incentive for updates beyond the trust band") is right.
- Gap: TRPO's actual constraint (the KL trust region and the natural-gradient motivation) is named but the derivation sketch from the surrogate-objective lower bound to the clip heuristic is thin. Graduate readers will want one sentence on why clipping approximates the KL constraint.
- Fix: add: "PPO's clip is a first-order surrogate for TRPO's hard KL constraint: bounding the ratio to $[1-\epsilon, 1+\epsilon]$ caps the per-sample policy change that drives KL, trading TRPO's exact constraint for a cheap elementwise one."
**Lens 2**: Frontier OK.
**Lens 3**: "one lucky rollout is not permission to reinvent the robot's gait" hook is excellent.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 15.5: PPO in practice: the implementation details that matter - EXCELLENT
**Lens 1**: PASS. This is the section embodied practitioners will actually use: rollout-buffer field alignment, frozen-vs-recomputed quantities, the three classic PPO bugs (mismatched log-prob transforms, wrong termination convention, mismatched reward normalization). This is exactly the "37 implementation details" knowledge.
**Lens 2**: Frontier (PPO as part of a data engine) is current and correct.
- Fix: cite Engstrom et al. "Implementation Matters in Deep RL" (2020) and the CleanRL "37 details" blog (Huang et al.) by name - they are the canonical sources for this exact section and their absence is conspicuous.
**Lens 3**: "PPO's paperwork is the method" is memorable.
**Lens 4**: PASS (dataclass PPORow with the real fields).
**Lens 5**: PASS, excellent Teaching Move (mark frozen vs recomputed).

#### Section 15.6: Reward shaping and its hazards - GOOD
**Lens 1**: PASS. Potential-based shaping vs naive proximity bonus computed side by side; "sensor humility" point is good.
- Note: this section overlaps heavily with 18.2 (Sparse vs dense; shaping done right) and 18.1/18.4 (reward danger / hacking). See Structure Suggestions.
**Lens 2**: Frontier OK.
**Lens 3**: "Write it assuming the optimizer will read it literally" hook is excellent; Teaching Move (propose an exploit for every component) is excellent.
**Lens 4**: PASS.
**Lens 5**: PASS, but the chapter now has two reward sections (15.6 and all of Ch 18); the transition does not acknowledge the upcoming dedicated chapter.
- Fix: add to What's Next: "Chapter 18 treats reward design as a first-class subject; this section is the PPO-local view of why shaping can mislead the advantage estimate."

### Chapter 16: Value-Based and Off-Policy Methods
**Quality**: GOOD (content) / NEEDS WORK (engagement layer)

Content is solid: Q-learning TD target, replay + target-network rationale, TD3 double-critic + delayed-policy + target smoothing, SAC soft value with temperature, importance ratios with the variance warning. But this is where the engagement layer visibly degrades: 4 of 5 sections share the recycled "optimism is not an evaluation metric / the simulator may applaud" fun-note, and all 5 use the templated "fill the evidence record before you touch model code" Teaching Move. The exercises shift from "compute X" to "design a table/schema," drifting toward the evidence-artifact toy lab the lean contract warns against.

#### Section 16.1: Q-learning; deep Q-networks - GOOD
**Lens 1**: PASS. TD target and update shown, one update traced with numbers. DQN extension implied but the section is mostly tabular; the "deep" in the title (function approximation, the deadly triad) is underdeveloped relative to the title.
- Fix: add a paragraph on the deadly triad (function approximation + bootstrapping + off-policy = potential divergence), which is the core reason DQN needed replay + target nets, and forward-reference 16.2.
**Lens 2**: Frontier (conservative value estimation, offline-to-online) is current but uncited.
- Fix: cite Mnih et al. DQN (2015), Hessel et al. Rainbow (2018), Kumar et al. CQL (2020).
**Lens 3**: Fun Note is the recycled "optimism is not an evaluation metric" boilerplate - WEAK and non-substitutable-failing.
- Fix: write a Q-learning-specific hook, e.g. "Q-learning is an optimist with a bootstrap: it trusts its own best guess about the next state to teach itself about this one. Target networks are what stop the optimism from feeding on itself."
**Lens 4**: PASS (contact-cost grasp values).
**Lens 5**: Templated "evidence record" exercise weakens an otherwise computational section.
- Fix: replace with: "Run tabular Q-learning on a 4x4 grid with one pit; show the Q-values for the state next to the pit before and after the target update, with $\alpha=0.25, \gamma=0.9$."

#### Section 16.2: Replay buffers and target networks - GOOD
**Lens 1**: PASS, strong. Correlation problem, uniform vs prioritized replay (with the importance-correction caveat), and the moving-target problem solved by Polyak averaging are all correct and well-motivated.
**Lens 2**: Frontier (coverage-aware sampling, offline-to-online replay) current, uncited.
- Fix: cite Schaul et al. Prioritized Experience Replay (2016) and Polyak/soft-update origin.
**Lens 3**: Memory Hook is the generic "ask what would be different in the next frame" template - WEAK.
- Fix: "A target network is a deliberately out-of-date copy of yourself. You learn faster by chasing last week's opinion than by chasing your own opinion as it moves."
**Lens 4**: PASS.
**Lens 5**: Templated exercise.

#### Section 16.3: Continuous control: DDPG, TD3, SAC - GOOD
**Lens 1**: PASS. DDPG brittleness -> TD3's three fixes (clipped double-Q, delayed actor, target smoothing) with the correct target formula. This is accurate and the right level.
- Gap: SAC is in the title but the soft actor mechanism (reparameterized Gaussian, automatic temperature tuning) is deferred to 16.4; 16.3 is really DDPG/TD3.
- Fix: either retitle 16.3 "Deterministic continuous control: DDPG and TD3" and let 16.4 own SAC, or add a SAC sketch here.
**Lens 2**: Frontier (critic uncertainty before high-torque commands) is a genuinely good embodied open question.
- Fix: cite Lillicrap et al. DDPG (2016), Fujimoto et al. TD3 (2018), Haarnoja et al. SAC (2018).
**Lens 3**: Recycled "could a teammate point to the log line" fun-note - WEAK, non-substitutable.
- Fix: "DDPG is an actor who believes every word its critic says. TD3 is the same actor after learning to ask a second critic and trust the more pessimistic one."
**Lens 4**: PASS (numeric TD3 target with clipped double critics).
**Lens 5**: Templated exercise (design a metric panel) - acceptable but generic.

#### Section 16.4: Maximum-entropy RL - GOOD
**Lens 1**: PASS. Max-ent objective with entropy term and temperature $\alpha$ exchange-rate interpretation; soft-value (log-sum-exp) backup computed. This is correct and well-explained.
**Lens 2**: Frontier (reset-free robotics, heterogeneous demos) current, uncited.
- Fix: cite Ziebart (max-ent IRL 2008) and Haarnoja et al. (soft Q-learning 2017, SAC 2018) and the automatic-temperature paper (2018).
**Lens 3**: Recycled "optimism is not an evaluation metric" fun-note (3rd occurrence) - WEAK.
- Fix: "Maximum-entropy RL pays the policy to stay curious. The temperature $\alpha$ is the exchange rate between 'do the best thing' and 'keep your options open' - and on hardware, options that include a collision are not free."
**Lens 4**: PASS.
**Lens 5**: Templated exercise.

#### Section 16.5: Sample efficiency and off-policy failure modes - GOOD
**Lens 1**: PASS. Importance ratio, variance blowup from multiplying ratios over horizon, and the practical clip/truncate/value-bootstrap response are correct and decision-relevant.
**Lens 2**: Frontier (turn coverage diagnostics into deployment decisions) is sharp and current.
- Fix: cite the off-policy-evaluation line (Precup et al.; Jiang & Li doubly robust) and offline-RL coverage (Levine et al. survey 2020).
**Lens 3**: Generic "make X visible twice" hook - WEAK.
**Lens 4**: PASS (logged action ratios flagging weak behavior-policy support).
**Lens 5**: Templated exercise.

### Chapter 17: Massively Parallel and GPU RL
**Quality**: GOOD

The most distinctive and audience-relevant chapter (this is what Boston Dynamics / NVIDIA-stack practitioners actually do). Six sections covering rollout shapes, the "walk in minutes" recipe, Isaac Lab runner contracts, MJX/Brax/JAX, teacher-student distillation, and throughput/cost engineering. The tool coverage (Isaac Lab, RSL-RL, rl_games, SKRL, Brax, MJX) is current and correct. The fun-notes here are the best in the part. Two weaknesses: (1) the foundational papers of GPU-scale legged RL are never cited, which is a glaring omission for this exact chapter; (2) the code fragments are mostly back-of-envelope sizing arithmetic rather than a real training-loop skeleton, so the "right tool payoff" (from-scratch then library) is asserted more than shown.

#### Section 17.1: Why thousands of parallel envs changed the field - GOOD
**Lens 1**: PASS. $T \times N \times d$ rollout block, the sample-count-vs-correlation distinction (seed families), and the coupled-design point are exactly right.
**Lens 2**: Best frontier callout in the part - has the only explicit "As of 2026" currency anchor and a real research risk (accelerator-scale training making success look mature before hardware confirms).
- Fix: still needs the founding citation: Rudin et al. "Learning to Walk in Minutes Using Massively Parallel Deep RL" (CoRL 2021) and Makoviychuk et al. Isaac Gym (2021).
**Lens 3**: "choir, not a crowd... the conductor is the seed schedule" is the best hook in the part. Preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 17.2: Learning to walk in minutes: the parallel-RL recipe - GOOD
**Lens 1**: PASS. Concrete numbers (4096 envs, T=24, 50 Hz, 98,304 transitions, 0.48 s/env) make the batch-size-vs-policy-lag tradeoff tangible. This is excellent embodied intuition.
**Lens 2**: Frontier good (morphology variation, transfer-predictive panels).
- Fix: cite Rudin et al. (2021) by name here - the section title is literally their paper's phrase, so not citing it is a citation-integrity gap.
**Lens 3**: "teach falling with excellent confidence intervals" is excellent.
**Lens 4**: PASS, but the code is sizing arithmetic; a real PPO-on-vectorized-env skeleton (even 15 lines with a fake VecEnv) would deliver the from-scratch payoff the contract asks for.
**Lens 5**: PASS.

#### Section 17.3: Isaac Lab with SKRL / rl_games / RSL-RL - GOOD
**Lens 1**: PASS. Asymmetric actor-critic observation routing, and the runner-vs-task distinction ("the task is the scientific object; the runner is the optimizer and storage") is a genuinely useful mental model.
**Lens 2**: Frontier (kit-less workflows, multi-backend physics) current.
- Fix: pin versions ("Isaac Lab 1.x / Isaac Sim 4.x as of 2026") and cite Mittal et al. Orbit/Isaac Lab (2023).
**Lens 3**: "adapter plug... label it" hook excellent.
**Lens 4**: PASS (RunnerContract dataclass comparing wrappers) - this is the most tool-specific code in the chapter.
**Lens 5**: PASS.

#### Section 17.4: MJX/Brax-training and JAX RL - GOOD
**Lens 1**: PASS. Pure-function batched-state model, static shapes, donation, and rollout-buffer byte sizing are the right JAX-specific concerns.
**Lens 2**: Frontier (physics+inference+learning in one accelerator program) current.
- Fix: cite Freeman et al. Brax (2021) and the MJX/MuJoCo 3 release (DeepMind 2024).
**Lens 3**: "JAX is happiest when the experiment arrives wearing the same tensor shape every day" excellent.
**Lens 4**: PASS (memory estimate).
**Lens 5**: PASS.

#### Section 17.5: Teacher-student and privileged-information distillation - GOOD
**Lens 1**: PASS. Distillation loss written explicitly, with the crucial caveat that distribution coverage and closed-loop student performance (not standalone loss) are what matter. Masked-loss numpy fragment is correct.
**Lens 2**: Frontier (latent terrain encoders, history-based students, recovery states) is current and exactly the legged-locomotion frontier.
- Fix: cite the canonical pair: Lee et al. (Science Robotics 2020) and Kumar et al./Margolis RMA line (2021-2022); Miki et al. ANYmal-in-the-wild (Science Robotics 2022). This section is incomplete without them.
**Lens 3**: "tutoring session... final exam confiscates the answer key" excellent.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 17.6: Throughput, wall-clock, and cost engineering - GOOD
**Lens 1**: PASS, and unusually practical: cost-per-robust-behavior vs cost-per-step, the throughput-vs-sample-efficiency tension, dollars-to-target-checkpoint. This is real production engineering content.
**Lens 2**: Frontier (full-stack efficiency, cost per robust behavior) good.
**Lens 3**: "cheapest successful run" hook good.
**Lens 4**: PASS (throughput + dollar cost from a run).
**Lens 5**: PASS. This section is a strong, non-obvious addition; keep it.

### Chapter 18: Reward Design and Goal Specification
**Quality**: GOOD

Six sections: reward danger, sparse/dense shaping, goal-conditioned + HER, reward hacking case studies, RLHF-for-control, safety-constrained rewards. Conceptually the richest chapter, and the fun-notes recover here (mostly fresh and topic-specific). The math is lighter (one or two equations per section) but appropriate - reward design is more about taxonomy and failure modes than derivation. Main issues: overlap with 15.6 and with Chapter 19 on safe exploration; the "case studies" promised in 18.4's title are illustrative-but-generic rather than drawn from named real incidents.

#### Section 18.1: Why rewards are dangerous - GOOD
**Lens 1**: PASS. Utility-wider-than-reward framing, omission vs channel failures - a clean, useful taxonomy.
**Lens 2**: Frontier (subtle shortcuts in larger policies) current.
- Fix: cite Krakovna et al. specification-gaming list (DeepMind 2020) and Amodei et al. "Concrete Problems in AI Safety" (2016).
**Lens 3**: "the hardware still asks for the receipt" - here it is the original, in-context use; keep, but vary the wording so the later copies in 16/19/20 can be removed without losing this one.
**Lens 4**: PASS (proxy-return vs evidence-fields rollout comparison).
**Lens 5**: PASS.

#### Section 18.2: Sparse vs. dense; shaping done right - GOOD
**Lens 1**: PASS, strong. Ng et al. potential-based shaping invariance ($F = \gamma\Phi(s') - \Phi(s)$) is the right theorem and it is stated with its policy-preservation property.
- Fix: state the assumption explicitly: "potential-based shaping preserves the optimal policy under the standard infinite-horizon discounted MDP; it does NOT guarantee the same learning dynamics, and with function approximation and finite horizons the guarantee weakens."
**Lens 2**: Frontier good.
- Fix: cite Ng, Harada & Russell (1999) by name - it is the source of the equation on the page.
**Lens 3**: "coach shouting / scoreboard / move the goalposts" excellent.
**Lens 4**: PASS.
**Lens 5**: PASS. Overlaps 15.6 - acknowledge.

#### Section 18.3: Goal-conditioned policies; hindsight experience replay - GOOD
**Lens 1**: PASS. HER relabeling mechanism and the critical evaluation caveat (evaluate on the original goal distribution) are both correct and the second is often omitted elsewhere.
**Lens 2**: Frontier (language-conditioned control, foundation-model goal proposals, grounding) is current and sharp.
- Fix: cite Andrychowicz et al. HER (2017) and Schaul et al. UVFA (2015); for the frontier, RT-2 / language-conditioned policies.
**Lens 3**: "I missed your target but I did hit this other one... file under useful experience, not victory" excellent.
**Lens 4**: PASS (relabeling fragment). Minor: CODE_LANGS detected stray `language-grounded`/`language-conditioned` tokens, likely a malformed `<code>` or class attribute in prose.
- Fix: audit 18.3 HTML for a broken inline code span (a `class="language-..."` leaked onto a non-code element).
**Lens 5**: PASS.

#### Section 18.4: Reward hacking, with case studies - GOOD
**Lens 1**: PASS. The causal distinction (action->task->reward vs action->measurement-artifact->reward) is the correct and rigorous way to define hacking, and the diagnostic (high reward persists when task metric fails) is operational.
**Lens 2**: Frontier (adversarial eval, automated red-team envs) current.
- Fix: the title promises "case studies" but the examples are generic (vibrating navigator, object pinned to wall). Add 1-2 NAMED cases: the CoastRunners boat-loop (OpenAI 2016) and a robotics specification-gaming entry from Krakovna's list.
**Lens 3**: "very literal lawyer and the patience of a machine" is the best reward-hacking line in the part.
**Lens 4**: PASS (metric-disagreement flagging).
**Lens 5**: PASS.

#### Section 18.5: Human preferences and learned reward models (RLHF for control) - GOOD
**Lens 1**: PASS. Bradley-Terry preference model stated and a preference loss computed. Correct and current for the RLHF-for-control framing.
**Lens 2**: Frontier (multimodal feedback, active queries, robustness under optimization pressure) current.
- Fix: cite Christiano et al. "Deep RL from Human Preferences" (2017) - it is the foundational paper for this exact section and is absent.
**Lens 3**: "judge with a very large clipboard" excellent.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 18.6: Safety-aware and constrained rewards - GOOD
**Lens 1**: PASS. Constrained-MDP objective with cost budget. Note: this is the third place the same $\max J_R$ s.t. $J_C \le d$ formulation appears (also 14.5, 19.3) - consolidate the derivation in one place and reference it.
**Lens 2**: Frontier (shielded policies, runtime monitors, sim-to-hardware constraint transfer) current.
- Fix: cite Achiam et al. CPO (2017), Ray et al. Safety Gym (2019), and the shielding line (Alshiekh et al. 2018).
**Lens 3**: "do not knock over the furniture on the way" excellent.
**Lens 4**: PASS.
**Lens 5**: PASS. Strong handoff into Ch 19 exploration.

### Chapter 19: Exploration in Embodied Worlds
**Quality**: GOOD (content) / NEEDS WORK (template drift)

Four sections: cost/risk of embodied exploration, intrinsic motivation/curiosity/count-based, safe exploration, exploration under partial observability. The content is good and embodied-specific (information-per-recoverable-cost objective; controllable curiosity; safety shield; belief-entropy active sensing). But this chapter shows the most template drift: three of four sections open the Theory with the identical "We can view the agent at time $t$ as receiving an observation $o_t$, maintaining an internal state estimate $\hat s_t$..." sentence, and the exercises all follow "Design a [topic] experiment in simulation. Specify..." The recycled "optimism is not an evaluation metric" fun-note appears in 19.1.

#### Section 19.1: Why embodied exploration is expensive and risky - GOOD
**Lens 1**: PASS. The four-stream accounting (information, motion/time, reset burden, hazard) and the "information per unit of recoverable cost, refuse irreversible probes" objective are genuinely good embodied framing.
**Lens 2**: Frontier (reset-aware exploration) current and well-targeted to home/field robotics.
- Fix: cite Eysenbach et al. Leave No Trace / reset-free RL (2018) and Sharma et al. autonomous RL.
**Lens 3**: Fun Note is the recycled "optimism is not an evaluation metric" - WEAK, 4th copy.
- Fix: "Exploration in the real world has a deposit, not just a price: some probes you can refund by resetting, and some you cannot. The agent should spend boldly on the refundable ones and treat the rest like glass."
**Lens 4**: PASS (probe pricing by info/reset/hazard).
**Lens 5**: PASS.

#### Section 19.2: Intrinsic motivation, curiosity, count-based and novelty methods - GOOD
**Lens 1**: PASS, strong. Count-based bonus $\beta/\sqrt{N}$, forward-model prediction-error curiosity, and the noisy-TV problem (unpredictable noise looks "interesting") are all correct and the noisy-TV caveat is the key insight.
**Lens 2**: Frontier (controllable curiosity, disagreement bonuses) current.
- Fix: cite Bellemare et al. count-based/pseudo-counts (2016), Pathak et al. ICM (2017), Burda et al. RND (2018), Pathak et al. disagreement (2019). This well-developed section is conspicuously uncited.
**Lens 3**: "Curiosity is a good intern and a poor manager" excellent.
**Lens 4**: PASS (count-based bonus over feature bins).
**Lens 5**: Templated "design an experiment" exercise.

#### Section 19.3: Safe exploration - GOOD
**Lens 1**: PASS. Constrained objective + safety shield filtering exploratory actions by clearance/recoverability. Note overlap with 14.3, 14.5, 18.6.
**Lens 2**: Frontier (safety envelopes under distribution shift) current.
- Fix: cite control-barrier-function RL (Cheng et al. 2019), Turchetta et al. safe exploration (2016/2019).
**Lens 3**: "nothing happened can be a result" excellent.
**Lens 4**: PASS (safety-shield filter).
**Lens 5**: Templated exercise.

#### Section 19.4: Exploration under partial observability - GOOD
**Lens 1**: PASS, strong. Belief update over hidden states, active sensing triggered by belief entropy, perceptual aliasing made explicit. The belief-entropy-triggers-active-sensing fragment is the best code in the chapter.
**Lens 2**: Frontier (learned memory: when to store history, query a map, act to gather info) current and sharp.
- Fix: cite the POMDP/belief-space planning line and recurrent-policy RL (Hausknecht & Stone DRQN 2015); for active sensing, the information-gathering-action literature.
**Lens 3**: "'I have seen this before' vs 'this looks like something I have seen before'" excellent - captures aliasing perfectly.
**Lens 4**: PASS.
**Lens 5**: Templated exercise.

### Chapter 20: Sim-to-Real Transfer (RL focus)
**Quality**: GOOD

Five sections: reality gap, what transfers, domain randomization/sysID/RMA, hardware fine-tuning, measuring transfer. This is core embodied-AI content and the treatment is practical and honest (transfer ledgers, gap diagnostics, safety gates, transfer ratio with matched-panel caveat). The RMA section is current and correct. Issues: the recycled fun-notes return (20.2 and 20.5 both use "optimism is not an evaluation metric"), and the founding domain-randomization / RMA papers are uncited.

#### Section 20.1: The reality gap revisited - GOOD
**Lens 1**: PASS. $P_{sim}$ vs $P_{real}$, and the "load-bearing when it changes the policy ranking" definition is the right operational notion of the gap.
**Lens 2**: Frontier (gap as measurement problem, not only robustness) is a sharp, current framing.
- Fix: cite the foundational sim-to-real surveys (Zhao et al. 2020) and the contact-gap literature.
**Lens 3**: Generic "ask what would be different in the next frame" hook - WEAK.
- Fix: "The reality gap is not a wall; it is a place where the simulator's confident prediction and the robot's actual next state quietly disagree. Your job is to find the exact interface where they part ways."
**Lens 4**: PASS (paired sim/real push trace).
**Lens 5**: PASS.

#### Section 20.2: What transfers and what does not - GOOD
**Lens 1**: PASS. Policy decomposition $\pi(a|z)$, $z=f(o_{0:t})$; representation may transfer, action distribution and reward model often do not. Clear and correct.
**Lens 2**: Frontier (modular transfer, calibrated adapters, residual controllers) current.
- Fix: cite residual policy learning (Johannink et al. 2019; Silver et al. 2018).
**Lens 3**: Recycled "optimism is not an evaluation metric" - WEAK, 5th copy.
- Fix: "What transfers is what the simulator could not fake: geometry, contact phase, goal relation. What breaks is what the simulator made too easy: clean force readings, instant vision, a robot with no backlash."
**Lens 4**: PASS (component reuse/recalibrate/constrain/discard ledger).
**Lens 5**: PASS.

#### Section 20.3: Domain randomization, system identification, adaptation (RMA) - GOOD
**Lens 1**: PASS, strong. DR over $\theta \sim p_{train}$, sysID estimating $\hat\theta$, residual randomization around the identified value, and RMA's online adaptation vector $z_t$ inferred from recent history. This is the correct and current account.
**Lens 2**: Frontier (which parameters matter, estimate from short traces, prevent adaptation masking unsafe behavior) is excellent and current.
- Fix: cite Tobin et al. domain randomization (2017), Peng et al. DR for manipulation (2018), Kumar et al. RMA (2021), OpenAI dexterous-hand (2019). RMA is in the title and uncited.
**Lens 3**: "control-room label" hook good.
**Lens 4**: PASS (randomization centered on identified params with residual width).
**Lens 5**: PASS.

#### Section 20.4: Fine-tuning on hardware; safe real-world RL - GOOD
**Lens 1**: PASS. Constrained update with safety gates, freeze-perception-and-stabilizer + adapt-residual to limit blast radius. Practical and correct.
**Lens 2**: Frontier (residual learning, shielding, offline-to-online, intervention learning) current.
- Fix: cite Smith et al. "Walk in the Park" (real-world fine-tuning, 2022) and HIL-SERL / intervention-learning line.
**Lens 3**: "visible twice... the second view keeps the first one honest" hook OK (reused phrasing with 16.5).
**Lens 4**: PASS (gate residual action before robot).
**Lens 5**: PASS.

#### Section 20.5: Measuring transfer performance - GOOD
**Lens 1**: PASS. Transfer ratio $\rho = S_{real}/S_{sim}$ with the matched-panel caveat, plus the gap-diagnostic suite (success gap, intervention rate, safety-violation rate, blocked-action rate, failure-category distribution). This is exactly the rigorous evaluation the audience needs.
**Lens 2**: Frontier (comparable evidence across robots/labs/simulators) is a real and current open problem.
- Fix: cite reproducibility-in-RL (Henderson et al. 2018) and robot-eval-standardization efforts.
**Lens 3**: Recycled "optimism is not an evaluation metric" - WEAK, 6th copy.
- Fix: "A transfer ratio of 0.7 is not a grade; it is a question. It asks which 30 percent failed, whether a human caught them, and whether a safety gate or the policy itself gave up."
**Lens 4**: PASS (transfer metrics from one matched artifact).
**Lens 5**: PASS. Strong part-closing section.

## Cross-Chapter Issues in This Part

1. **Identical templated epigraph in all 37 sections.** Every section opens with "[Section title] matters when the next action changes the evidence you thought you had." This fails the non-substitutability rule outright (swap the title, nothing else changes). Replace each with a section-specific epigraph or a real quotation. Highest-value single fix in the part by volume.

2. **Identical chapter-index opening paragraph in all 7 modules.** "[Chapter title] matters because embodied intelligence is a closed loop. The agent must turn partial observations into useful state, choose actions under uncertainty, and learn from the consequences..." Same epigraph too ("An agent becomes interesting at the exact moment the world refuses to be a dataset" - a great line, but repeating it 7 times destroys it; keep it once at the Part level).

3. **Identical "Practical Recipe" 5-step list in at least 5 sections** (14.1-14.5 verbatim: "Write the observation, action, and success metric... Build a baseline... Add the library implementation... Record failures as structured cases... Run at least one perturbation test"). Generic enough to be content-free per section.

4. **Identical "Common Failure Mode" warning** ("...celebrate the component score before checking the closed-loop handoff... stale state, wrong frame, delayed action, saturated actuator...") repeated across module-14 sections and beyond. The lean contract wants 2-4 failure modes specific to THIS topic; this is one generic paragraph reused.

5. **Recycled "optimism is not an evaluation metric / the simulator may applaud every rollout" fun-note in 6+ sections** (16.1, 16.4, 19.1, 20.2, 20.5, plus the in-context original 18.1). Keep one (18.1), rewrite the rest as topic-specific hooks (drafts provided per section above).

6. **Templated "fill the evidence record before you touch model code" Teaching Move across all of Chapter 16** and the "Design a [topic] experiment/schema/manifest. Specify..." exercise pattern across Chapters 16-20. Modules 14-15 have genuinely computational exercises ("compute every $G_t$", "prove the baseline identity", "compute ratios + clip fraction + approx KL"); the later modules drift into the "evidence-artifact toy lab" the lean contract explicitly warns against. At least restore one compute-something exercise per section in 16-20.

7. **Near-total absence of body citations.** Every section has a 5-card bibliography, but those 5 cards are the SAME five references (Sutton & Barto, Puterman, OpenAI Gym, Gymnasium, MuJoCo) in modules 14-15, with annotations find-and-replaced per section ("For this section, connect the source to [title]..."). The actual landmark papers for each topic (DQN, TD3, SAC, PPO/CleanRL details, GAE, Rudin parallel-RL, RMA, HER, Christiano preferences, Ng potential shaping, ICM/RND, CPO/Safety Gym) appear in NONE of the bodies. For a research-scientist audience this is the single biggest content gap. Per-section citation drafts are in the Lens 2 entries above.

8. **Topic overlap to reconcile:** reward shaping appears in 15.6 AND 18.2; reward danger/hacking spans 18.1 and 18.4; the constrained-MDP $\max J_R$ s.t. $J_C\le d$ objective is derived three times (14.5, 18.6, 19.3); safe exploration spans 14.3, 14.5, 18.6, 19.3, 20.4. None of these cross-reference each other. Add cross-refs and consolidate the constrained-MDP derivation in one canonical spot (18.6) referenced elsewhere.

9. **Repeated Theory-opening sentence in Chapter 19** ("We can view the agent at time $t$ as receiving an observation $o_t$, maintaining an internal state estimate...") in 19.1/19.3/19.4. De-duplicate.

10. **Frontier callouts are present everywhere (a strength) but only 17.1 carries a dated currency anchor.** Add "as of 2026" framing and 1-2 named recent works to each frontier callout so the chapters feel alive rather than generically forward-looking.

## Top 10 Highest-Priority Fixes for This Part

1. **Replace the 37 identical section epigraphs.** Files: every `section-*.html` in all 7 modules. Each `<blockquote class="epigraph">` currently reads "[title] matters when the next action changes the evidence you thought you had." Draft a per-topic line; e.g. 15.4: "A trust region is humility, formalized: change the policy, but not so fast you forget what worked." 16.3: "Two critics, one pessimist: TD3 is the art of not believing your own best guess." This is mechanical but the highest non-substitutability win.

2. **Inject the missing landmark citations into section bodies** (not just the recycled 5-card bibliography). Priority sections where the founding paper IS the section: 15.5 (Engstrom 2020 + CleanRL 37-details), 17.1/17.2 (Rudin et al. 2021; Makoviychuk Isaac Gym 2021), 17.5/20.3 (Lee 2020; Kumar RMA 2021; Miki 2022), 18.2 (Ng/Harada/Russell 1999), 18.3 (Andrychowicz HER 2017), 18.5 (Christiano 2017), 19.2 (Pathak ICM 2017; Burda RND 2018). Each as a one-line "Paper Spotlight" callout with narrative context.

3. **De-template the per-section bibliography annotations.** Files: all section-*.html. Replace "For this section, connect the source to [title] and check the original resource before copying settings" with a real one-sentence reason the cited work matters to this specific topic, and diversify the 5 cards per topic.

4. **Rewrite the 6 recycled "optimism is not an evaluation metric" fun-notes** (16.1, 16.4, 19.1, 20.2, 20.5; keep 18.1). Topic-specific drafts provided in the per-section Lens 3 entries above.

5. **Restore computational exercises in Chapters 16-20.** Files: section-16.1 through 20.5. Replace the "design a schema/manifest/table" pattern with at least one "compute X with these numbers" exercise per section (drafts in Lens 5 entries, e.g. the 4x4-grid Q-learning update for 16.1).

6. **Collapse the boilerplate frame** ("Reader Pathway" + "What This Section Develops") into a single one-paragraph section frame per the lean contract criterion 1. Files: all 37 sections. The current two-callout opener is template scaffolding.

7. **Add the deadly-triad paragraph and DQN function-approximation content to 16.1** so the "deep Q-networks" half of the title is delivered (currently mostly tabular). File: module-16.../section-16.1.html.

8. **Add the TRPO-to-PPO derivation sketch to 15.4** (one sentence on why clipping approximates the KL constraint). File: module-15.../section-15.4.html. Closes the only real depth gap in the strongest chapter.

9. **Add 1-2 NAMED reward-hacking case studies to 18.4** (CoastRunners boat-loop, OpenAI 2016; a Krakovna specification-gaming robotics entry) so the title's "case studies" promise is met. File: module-18.../section-18.4.html.

10. **Replace the back-of-envelope-only code in 17.2 (and optionally 17.1) with a minimal real vectorized-PPO rollout skeleton** so the GPU-RL chapter delivers the from-scratch-then-library payoff rather than only sizing arithmetic. File: module-17.../section-17.2.html. Also fix the leaked `class="language-grounded/conditioned"` token in 18.3.

## Structure Suggestions for This Part

- **Reconcile 15.6 with Chapter 18.** Section 15.6 (Reward shaping and its hazards) duplicates 18.2 (Sparse vs dense; shaping done right). Either retitle 15.6 to "Reward shaping inside the PPO loop" (scoped to how shaping distorts the advantage estimate, with a forward-ref to Ch 18 for reward design proper), or move it into Chapter 18 and let Chapter 15 stay purely policy-gradient mechanics. Recommend the retitle + forward-ref; it is cheaper and keeps the PPO-local angle.

- **Tighten the SAC placement in Chapter 16.** 16.3's title is "DDPG, TD3, SAC" but SAC's mechanism lives in 16.4 (Maximum-entropy RL). Retitle 16.3 "Deterministic continuous control: DDPG and TD3" and let 16.4 own SAC end-to-end, or fold the two into one stronger continuous-control section and reclaim a slot.

- **Consolidate the constrained-MDP derivation.** The same $\max J_R$ s.t. $J_C \le d$ objective is derived in 14.5, 18.6, and 19.3. Make 18.6 the canonical derivation and have 14.5 and 19.3 reference it. No section needs to be dropped, but the triple-derivation is redundant.

- **No section should be cut for thinness** - unlike some parts, every section here has real content. The work is de-templating, citing, and reconciling overlap, not removal.

- **Consider promoting the part-level epigraph** ("An agent becomes interesting at the exact moment the world refuses to be a dataset") to the Part IV index only, and giving each chapter its own distinct epigraph, so the line keeps its impact instead of being diluted across 7 reuses.
