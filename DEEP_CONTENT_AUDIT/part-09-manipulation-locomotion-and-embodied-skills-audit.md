# Part 9 Content Audit: Manipulation, Locomotion, and Embodied Skills

## Part Overview

Part 9 spans 7 chapters (modules 42-48) and 48 section files: manipulation (42), grasping and dexterity (43), tactile learning (44), locomotion (45), humanoids (46), drones (47), and autonomous driving (48). The first five chapters plus the "deep" appended sections of the last two are solid, GOOD-quality practitioner content: real equations with regime-of-validity notes, topic-specific runnable snippets, named/versioned tools, 2-4 topic failure modes, and live research-frontier callouts with stated open problems. The dominant problem is concentrated and severe: the eleven "syllabus" sections of chapters 47 and 48 (47.1-47.5, 48.1-48.6) are template-generated boilerplate where the section title is mechanically slotted into fixed sentences and the worked example is the exact `SkillEvidence` dataclass filler the lean contract forbids. A secondary issue spans the whole part: the part `index.html` is stale (it lists only chapters 44-48 and omits 42, 43, and every "deep" section), and a template "Reader Pathway" / "What This Section Develops" / "Action Is The Test" scaffold repeats in all 48 sections.

## Fun Elements to Preserve

These crafted epigraphs and Memory Hook fun-notes are genuine assets and must survive any edit. Chapters 42-46 are rich; chapters 47-48 main sections are not (see issues).

**Epigraphs (chapters 42-46, hand-crafted):**
- 42.1 "A robot first learns humility from friction."
- 42.2 "Pipelines look boring until one missing state estimate breaks the whole warehouse."
- 42.3 "The world stops being polite when insertion begins."
- 42.4 "A grasp starts as a perceptual claim."
- 42.5 "Policies are only interesting when the object disagrees."
- 42.6 "Robustness is a recovery policy with receipts."
- 42.7 "A mobile manipulator is a negotiation between reachability and route planning."
- 43.1 "A grasp is a hypothesis about future contact stability."
- 43.2 "More fingers buy options, not free competence."
- 43.3 "The hard part of dexterity is not holding on, it is changing contact without losing meaning."
- 43.4 "Demonstrations teach the hand where the search should begin."
- 43.5 "Dexterity in simulation becomes interesting only after hardware disagrees."
- 44.1 "Vision sees where contact might happen, touch says what contact actually became."
- 44.2 "A tactile camera turns deformation into geometry."
- 44.3 "Simulated touch is a promise about which contact features will survive reality."
- 44.4 "The point of multimodality is to make one channel useful when the other one lies."
- 44.5 "Fusion is only useful when it changes what the robot decides next."
- 45.1 "Mobility is morphology plus a contract with the ground."
- 45.2 "Balance is what remains after every modeling shortcut gets punished by gravity."
- 45.3 "GPU hours are only useful when they purchase better disturbance behavior."
- 45.4 "Adaptation starts where the training distribution stops pretending to be the world."
- 45.5 "A locomotion policy that ignores heat and power is outsourcing the hard part to the battery."
- 46.1 "Humanoids became interesting when data, hardware cost, and human-shaped environments finally started pointing in the same direction."

**Memory Hook fun-notes (high-value, witty, topic-locked):**
- 42.1 "If the table were covered with dry-erase marker, the real skill would show up as streaks on the object path, not on the robot arm path."
- 42.2 "Pick-and-place demos love the moment of lift. Production robots earn their salary during the far less cinematic moments of handoff, transport, and final pose verification."
- 42.3 "If your insertion plot looks like a mountain and your displacement plot looks like a sidewalk curb, the robot is arguing with the environment and losing."
- 42.5 "A policy with great losses and terrible object outcomes is just a very committed impersonator."
- 42.6 "Nothing reveals a missing recovery design faster than a robot attempting the exact same doomed grasp with heroic consistency."
- 42.7 "A mobile manipulator can absolutely reach the wrong place with stunning confidence."
- 43.1 "A perfectly centered grasp on a slippery shampoo bottle can still become an expensive lesson in rigid-body optimism."
- 43.2 "A five-finger hand can absolutely outperform a two-finger gripper, right after it finishes asking for better calibration, better tactile sensing, and several more weeks of control tuning."
- 45.3 "Parallel RL is a microscope and a funhouse mirror at the same time. It reveals more events, but it enlarges every bug you forgot to measure."
- 46.3 "Operational space is the wish. Whole-body control is the bill."
- 46.4 "The robot is not a puppet. It is an organism with different bones, muscles, and excuses."
- 46.5 "Teleoperation teaches the autonomy stack where the robot still needs a grown-up in the room."
- 46.6 "The planner should be the navigator, not the ankle servo."
- 46.7 "Safe humanoids are not the ones that never stop. They are the ones that know exactly when to stop and how to recover afterward."

**Self-check rhetorical jabs worth keeping (engagement):** 43.1 "or is the score just a number with good marketing?"; 43.2 "or are you using dexterity as a synonym for ambition?"; 42.6 "are you pretending diagnosis matters while routing everything to retry?".

Count of distinct, crafted fun elements found: **38** (24 crafted epigraphs + 14 standout Memory Hooks; the witty self-checks are bonus).

## Chapter-by-Chapter Analysis

### Chapter 42: Robotic Manipulation
**Quality**: GOOD

Seven sections (42.1-42.7), all the same lean template: crafted epigraph, Big Picture, Reader Pathway, Theory with one display equation, Mechanism, Algorithm, topic-specific worked example, Library Shortcut, Practical Recipe, Common Failure Mode, Practical Example, Memory Hook, Research Frontier, Self Check, Builder's Deep Dive with tool table, Failure Analysis Pattern, Section References, Key Takeaway, one Exercise. Tools are named and current (MoveIt 2, cuRobo/cuMotion, Drake, MuJoCo, ManiSkill, Dex-Net/GQ-CNN, BehaviorTree.CPP, Nav2, Habitat 3.0, Mobile ALOHA).

#### Section 42.1: What manipulation is; reaching and pushing - GOOD
**Lens 1 (Deep Explanation)**: Mostly PASS. Motion-cone framing for quasi-static pushing is correct and well-motivated; the equation block ties Jacobian, object-state transition, and success indicator. Weakness: the equation is asserted, the motion cone is named in prose but not derived; "regime of validity" (quasi-static, rigid object, point contact) is stated only loosely.
- Fix: add one sentence after the equation: "This holds under quasi-static contact (inertial terms negligible relative to friction), a single rigid object, and a point or small-patch pusher; once the object accelerates or rolls, the motion-cone prediction degrades and the verifier residual is the only trustworthy signal."

**Lens 2 (Research Frontier)**: PASS. Frontier callout names the durable contribution (better contact-state supervision over bigger nets). Could cite a concrete recent push/contact paper.

**Lens 3 (Fun/Engagement)**: Strong. Epigraph + dry-erase Memory Hook (preserve both).

**Lens 4 (Examples/Analogies)**: The worked example is a 7-line push-quality scorer: topic-specific but a toy heuristic, not a runnable push controller. Acceptable for a lean section but it is illustrative, not a real implementation. Right-tool payoff (MoveIt Task Constructor / cuRobo / Drake) is present in Library Shortcut.

**Lens 5 (Teaching Flow)**: PASS. Clear build, good prereqs in chapter index. The "Reader Pathway" + "What This Section Develops" headers are boilerplate scaffolding the lean contract flags for removal.

#### Section 42.2: Pick-and-place pipelines - GOOD
**Lens 1**: PASS. Stage-contract factorization (grasp quality x reachable x collision-free) is clear and well-motivated. Equation correctly separates grasp scoring from trajectory composition.
**Lens 2**: PASS. Frontier note on learned-proposal + optimization-placement is current.
**Lens 3**: Epigraph and the "earn their salary during handoff" Memory Hook are excellent; preserve.
**Lens 4**: Worked example (grasp filter by score x reachable x place_ok) is topic-specific and makes the right pedagogical point (feasibility gates raw score).
**Lens 5**: PASS. Strong stage-by-stage flow.

#### Section 42.3: Contact-rich interaction - GOOD
**Lens 1**: PASS, this is one of the strongest. Impedance law plus complementarity conditions (lambda_n >= 0, phi(q) >= 0, lambda_n phi(q) = 0) are correct and the prose explains contact modes (sliding/sticking/jamming/separation). Regime is implicit; state that admittance vs impedance choice depends on environment stiffness relative to robot stiffness.
- Fix: add "Use impedance control when the robot is stiffer than the environment and admittance control when the environment is stiffer; mixing them up is the most common cause of contact instability."
**Lens 2**: PASS. Differentiable contact sim and visuo-tactile policies named.
**Lens 3**: "mountain vs sidewalk curb" Memory Hook is memorable; preserve.
**Lens 4**: Jam-detector worked example (force slope vs travel gain) is genuinely good and topic-locked.
**Lens 5**: PASS.

#### Section 42.4: Perception for manipulation - GOOD
**Lens 1**: PASS. Action-conditioned perception framed as marginalization over pose with a mean-minus-variance grasp objective; this is the right Bayesian framing and is well-motivated.
**Lens 2**: PASS, current (3D foundation models, affordance fields, open-vocab). SAM 2 named.
**Lens 3**: "seeing slightly less of the object can still be fine" Memory Hook is a real aha; preserve.
**Lens 4**: Uncertainty-aware grasp ranking example (mean_q - beta*var_q) is topic-specific.
**Lens 5**: PASS.

#### Section 42.5: Learning manipulation policies (IL, RL, VLA) - GOOD
**Lens 1**: PASS. BC vs RL vs VLA contrasted by supervision consumed and action interface emitted; covariate-shift and sample-efficiency tradeoffs stated. The three-way equation (BC loss, RL return, policy map) is appropriate.
**Lens 2**: PASS, current (cross-embodiment VLAs, OpenVLA, policy distillation). 2024-2026 currency is fine.
**Lens 3**: "a very committed impersonator" is a great line; preserve.
**Lens 4**: The worked example (if-else policy-family selector) is the weakest in the chapter: it is a decision-tree heuristic, not manipulation code. Borderline filler.
- Fix: replace with a minimal robomimic or LeRobot config snippet that loads a dataset and prints the action-space spec, so the "action interface first" lesson is shown in real API terms.
**Lens 5**: PASS.

#### Section 42.6: Failure detection and recovery - GOOD
**Lens 1**: PASS. Failure-state-machine abstraction with residual feature vector and recovery transition is clear and correct.
**Lens 2**: PASS (learned failure predictors, language-annotated recovery).
**Lens 3**: "heroic consistency" Memory Hook; preserve.
**Lens 4**: Recovery-router worked example (slip/occlusion/progress -> branch) is topic-specific and didactic.
**Lens 5**: PASS. Good link to safety and evaluation.

#### Section 42.7: Mobile Manipulation - GOOD
**Lens 1**: PASS. Coupled cost over (base pose, arm config, visibility, risk) is the right formulation; multi-timescale reasoning explained.
**Lens 2**: PASS (foundation-model perception + whole-body planning + household sim). Mobile ALOHA, Habitat 3.0, BEHAVIOR-1K named.
**Lens 3**: "reach the wrong place with stunning confidence" Memory Hook; preserve.
**Lens 4**: Base-pose scorer (reach/view/risk weighted sum) is topic-specific.
**Lens 5**: PASS. Good synthesis section closing the chapter.

### Chapter 43: Grasping and Dexterous Manipulation
**Quality**: GOOD

Five sections (43.1-43.5), same template, consistently strong on contact mechanics.

#### Section 43.1: Grasp synthesis: analytic and learned (Dex-Net lineage) - GOOD
**Lens 1**: PASS. Epsilon-quality (largest ball inscribed in the convex hull of the grasp wrench set) is the correct force-closure metric and is paired with the learned GQ-CNN proxy. Good bridge.
**Lens 2**: PASS (synthetic supervision, point-cloud encoders, tactile, task-aware scoring).
**Lens 3**: shampoo-bottle Memory Hook; "good marketing" self-check; preserve.
**Lens 4**: Worked example (gqcnn x reachable ranking) makes the image-confidence vs robot-feasibility point well.
**Lens 5**: PASS.

#### Section 43.2: Parallel-jaw vs. multi-finger hands - GOOD
**Lens 1**: PASS. Grasp-matrix rank, action-dimension blowup, and system-cost proportionality are stated; task-match framing (not human-likeness) is the right lens.
**Lens 2**: PASS (tactile skins, learned controllers; deployment payback question).
**Lens 3**: the "several more weeks of control tuning" Memory Hook is one of the funniest in the part; preserve.
**Lens 4**: Decision-heuristic example is light (a weighted-score chooser) but topic-appropriate here since the section IS about a design decision.
**Lens 5**: PASS.

#### Section 43.3: In-hand manipulation and reorientation - GOOD
**Lens 1**: PASS. Contact-sequence formulation (orientation as a product of incremental rotations, reachable contact transitions, drop probability constraint) is correct and graduate-level.
**Lens 2**: PASS.
**Lens 3**: Epigraph is excellent ("changing contact without losing meaning"); preserve.
**Lens 4**: Topic-specific.
**Lens 5**: PASS.

#### Section 43.4: Dexterous RL with demonstrations - GOOD
**Lens 1**: PASS. BC-init + RL-finetune with combined loss is the standard recipe; covariate-shift and reward-hacking risks stated.
**Lens 2**: PASS. Could name a specific result (e.g., in-hand reorientation with RMA-style adaptation) for narrative grounding.
- Fix: add a Paper Spotlight on a concrete dexterous-RL-from-demos result with the sim-to-real transfer numbers, to make the frontier "alive".
**Lens 3**: Epigraph good; preserve.
**Lens 4**: Topic-specific.
**Lens 5**: PASS.

#### Section 43.5: Sim-to-real for dexterity - GOOD
**Lens 1**: PASS. Domain-randomization objective plus real-sim trajectory distance metric; the "contact realism over image realism" insight is the correct and non-obvious point.
**Lens 2**: PASS.
**Lens 3**: Epigraph good; preserve.
**Lens 4**: Topic-specific.
**Lens 5**: PASS. Good chapter close (transfer ledger).

### Chapter 44: Tactile and Visuo-Tactile Learning
**Quality**: GOOD

Five sections (44.1-44.5), each with 2 equations, 1 Python snippet, 1 fun-note, crafted epigraph. Sensors are current and correctly named (GelSight, DIGIT, AnySkin, TACTO, Tactile Gym, PyTouch).

#### Section 44.1: Why touch matters for contact-rich tasks - GOOD
**Lens 1**: PASS. Touch framed as the modality that resolves contact ambiguity vision cannot; motivation precedes mechanism.
**Lens 2**: PASS.
**Lens 3**: Epigraph "touch says what contact actually became" is excellent; preserve.
**Lens 4**: Topic-specific snippet.
**Lens 5**: PASS.

#### Section 44.2: Vision-based tactile sensors (GelSight, DIGIT) - GOOD
**Lens 1**: PASS. "tactile camera turns deformation into geometry" is the right mental model; photometric-stereo / membrane-deformation mechanism explained.
**Lens 2**: PASS.
**Lens 3**: Epigraph + Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 44.3: Simulating touch (tactile sim in Isaac) - GOOD
**Lens 1**: PASS. Sim-as-promise framing; which contact features survive transfer is the right question.
**Lens 2**: PASS (TACTO, Isaac tactile). Current.
**Lens 3**: Epigraph good; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 44.4: Visuo-tactile pretraining and policies - GOOD
**Lens 1**: PASS. Multimodal complementarity ("one channel useful when the other lies") is precise and well-motivated.
**Lens 2**: PASS.
**Lens 3**: Epigraph is a standout; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 44.5: Combining vision and touch - GOOD
**Lens 1**: PASS. Fusion-changes-the-decision framing avoids the common "fusion for its own sake" trap.
**Lens 2**: PASS.
**Lens 3**: Epigraph good; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS. The "What's Next" nav points back to the chapter index rather than the next chapter (minor; same in several chapter-final sections).

### Chapter 45: Locomotion and Mobility
**Quality**: GOOD (strongest frontier writing in the part)

Five sections (45.1-45.5). Research-frontier callouts here state genuine open problems precisely (recoverable autonomy under sensing/maintenance budgets; interpretable balance margins vs learned reflex agility; interpretability after field misses; legible safety cases). Tools current (Isaac Lab, MJX, ROS 2).

#### Section 45.1: Wheeled, legged, and hybrid robots - GOOD
**Lens 1**: PASS. Morphology-as-slowest-hyperparameter is a sharp, correct framing.
**Lens 2**: PASS. Open question stated well (which body yields most recoverable autonomy, not which is fastest).
**Lens 3**: "Morphology is the slowest hyperparameter to change" Memory Hook; preserve.
**Lens 4**: Hospital-delivery-vs-substation-inspection practical example is concrete and real.
**Lens 5**: PASS.

#### Section 45.2: Balance, stability, and gait - GOOD
**Lens 1**: PASS, but this section carries only 1 display equation; balance deserves the ZMP / capture-point / centroidal-momentum formalism explicitly.
- Fix: add the capture point equation $x_{cap} = x_{com} + \dot x_{com}\sqrt{z/g}$ with one sentence on the linear-inverted-pendulum assumption and where it breaks (significant angular momentum, compliant contact).
**Lens 2**: PASS (reduced-order + MPC + learned recovery).
**Lens 3**: "choreography, not control" Memory Hook is excellent; preserve.
**Lens 4**: Box-carrying biped with lateral nudges is a good real test.
**Lens 5**: PASS.

#### Section 45.3: Learning locomotion with massively parallel RL - GOOD
**Lens 1**: PASS. Reward-exploit-at-scale failure mode is exactly the right thing to teach here.
**Lens 2**: PASS (parallel RL + motion priors + terrain encoders + adaptation).
**Lens 3**: "microscope and funhouse mirror" Memory Hook is the best line in the chapter; preserve.
**Lens 4**: Quadruped hopping-exploit example is concrete.
**Lens 5**: PASS.

#### Section 45.4: Terrain adaptation, parkour, and rapid motor adaptation - GOOD
**Lens 1**: PASS. RMA / latent-adaptation framing; the underfoot-compliance vs lateral-slip distinction is a precise, non-obvious teaching point.
**Lens 2**: PASS (online adaptation + vision + event-based contact + hierarchical planners; interpretability open problem).
**Lens 3**: Memory Hook good; preserve.
**Lens 4**: Stepping-stones example is topic-locked.
**Lens 5**: PASS.

#### Section 45.5: Energy efficiency; sim-to-real and safety - GOOD
**Lens 1**: PASS. Cost-of-transport, thermal, and battery-sag framing is the correct field-readiness lens.
**Lens 2**: PASS (energy-aware control + safety filters + adaptive mission planning).
**Lens 3**: "outsourcing the hard part to the battery" epigraph + "logs are missing, the deployment claim is missing" Memory Hook; preserve both.
**Lens 4**: End-of-shift thermal-throttle example is realistic.
**Lens 5**: PASS. Strong chapter close.

### Chapter 46: Humanoid Robots and Whole-Body Control
**Quality**: GOOD

Nine sections (46.1-46.9). The index lists 46.1-46.7; sections 46.8 (Advanced humanoid dynamics and contact mechanics) and 46.9 (Boston Dynamics-style loco-manipulation research track) are appended and NOT in the part index. Platform coverage is current (Unitree G1/H1, Figure, Optimus, 1X, electric Atlas, Apptronik). This is the most audience-relevant chapter for the Boston Dynamics readership.

#### Section 46.1: Why humanoids became the focus - GOOD
**Lens 1**: PASS. The data/morphology/hardware-cost convergence argument is well-motivated and the "economic boundary" open question is sophisticated.
**Lens 2**: PASS.
**Lens 3**: Epigraph + "does walking like us buy enough useful work to pay for itself?" Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 46.2: Platforms - GOOD
**Lens 1**: PASS for a survey section; tradeoffs across vendor stacks framed as iteration speed vs inherited assumptions.
**Lens 2**: PASS, current platform list.
**Lens 3**: "not the one with the most cinematic trailer" Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS. Risk: platform lists date fast; flag for the content-currency pass.

#### Section 46.3: Whole-body and operational-space control - GOOD
**Lens 1**: PASS. OSC / WBC as a QP with task-priority null-space projection; this is the technical heart of the chapter. Verify the equation shows the prioritized null-space projection, not just a single task.
- Fix: ensure the hierarchy $\tau = J_1^+ \ddot x_1 + N_1(J_2 N_1)^+(\ddot x_2 - J_2 J_1^+ \ddot x_1)$ or an equivalent stacked-QP form is present, with one line on strict vs soft priorities.
**Lens 2**: PASS (optimization WBC + learned target generation / residual policies).
**Lens 3**: "Operational space is the wish. Whole-body control is the bill." is the single best epigram in the part; preserve at all costs.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 46.4: Learning from humans (HumanPlus, OmniH2O/HOVER, retargeting) - GOOD
**Lens 1**: PASS. Motion retargeting under embodiment mismatch; intent preservation framed precisely.
**Lens 2**: PASS, current named systems (HumanPlus, OmniH2O, HOVER). Strong, alive frontier.
**Lens 3**: "an organism with different bones, muscles, and excuses" Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 46.5: Teleoperation for humanoids - GOOD
**Lens 1**: PASS. Shared-autonomy + local-stabilizer framing.
**Lens 2**: PASS (predictive interfaces, dataset extraction for foundation models).
**Lens 3**: "needs a grown-up in the room" Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 46.6: Dual-system humanoid foundation models (tie-back to Ch. 35) - GOOD
**Lens 1**: PASS. Slow-semantic / fast-motor split, with the cross-reference to Ch. 35 done right.
**Lens 2**: PASS (vendor VLA stacks, whole-body references; interpretability open problem).
**Lens 3**: "The planner should be the navigator, not the ankle servo." Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS. Good explicit tie-back.

#### Section 46.7: Safety for human-scale robots - GOOD
**Lens 1**: PASS. Stop-and-recover framing; force/energy limits for human-scale contact.
**Lens 2**: PASS (formal safety filters, learned risk predictors, intention estimation).
**Lens 3**: "know exactly when to stop and how to recover" Memory Hook; preserve.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 46.8: Advanced humanoid dynamics and contact mechanics - GOOD
**Lens 1**: PASS, carries 2 equations (deepest in the chapter). Centroidal dynamics / contact-wrench-cone material. Genuinely graduate-level.
**Lens 2**: PASS.
**Lens 3**: Shares the duplicated epigraph "A robot earns trust one recovered disturbance at a time." (see cross-chapter issue). Memory Hook present.
- Fix: give it a unique epigraph, e.g. "Humanoid dynamics is bookkeeping for momentum the floor is allowed to refuse."
**Lens 4**: PASS.
**Lens 5**: PASS, but this section is invisible in the part index.

#### Section 46.9: Boston Dynamics-style loco-manipulation research track - GOOD
**Lens 1**: PASS. Underactuated, contact-rich, human-scale loco-manipulation as one closed loop. Directly on-target for the stated audience.
**Lens 2**: PASS.
**Lens 3**: Duplicated epigraph (same as 46.8); needs its own.
- Fix: e.g. "Loco-manipulation is where the legs and the hands stop pretending they have separate budgets."
**Lens 4**: PASS, real-systems framing (Atlas-class behavior).
**Lens 5**: PASS, but invisible in the part index.

### Chapter 47: Drones and Aerial Embodied AI
**Quality**: NEEDS WORK (split: 47.6-47.8 GOOD; 47.1-47.5 POOR template)

Eight sections (47.1-47.8). The index lists 47.1-47.5; the genuinely good content is in the appended 47.6-47.8 (Quadrotor dynamics and flight control; Trajectory generation and GPS-denied missions; PX4 to hardware). The five "syllabus" sections 47.1-47.5 are template-generated.

#### Section 47.1: Why aerial agents are special - POOR
**Lens 1**: FAIL. Theory paragraph is a fill-in-the-blank: "In Why aerial agents are special, the important state variables are six degree of freedom state, thrust limits, wind, battery, and airspace rules, while the action interface is to separate flight stabilization from mission-level autonomy." The section title is grammatically slotted into a generic sentence. No derivation, no regime of validity. The "$o_t, \hat s_t, a_t$" POMDP boilerplate is identical across every 47.x and 48.x main section.
- Fix: rewrite from scratch. Replace with the actual reason aerial agents differ: no safe stop state, $T \propto \omega^2$ thrust nonlinearity, underactuation (4 inputs, 6 DOF), and the energy-time coupling that makes hover itself expensive. Open with the crafted epigraph from the deep sections' style, not the template.

**Lens 2**: FAIL (as frontier writing). The Research Frontier callout exists but is generic. Tools list (PX4, ROS 2, MAVLink, gym-pybullet-drones, Aerial Gym, safe-control-gym) is correct and current, which is the one redeeming element.

**Lens 3**: FAIL. Epigraph is the template "Why aerial agents are special matters when the next action changes the evidence you thought you had." Figure caption is the template "Section 47.1: ... is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation." No real fun.

**Lens 4**: FAIL. The worked example is the forbidden `SkillEvidence` dataclass filler: a generic dataclass whose only topic content is string literals (`section="47.1"`, `tool_route="PX4 and ROS 2"`). This is exactly the "plan = [skill for skill in skills]" anti-pattern the lean contract bans. No from-scratch-then-library payoff.

**Lens 5**: FAIL. No genuine build; the "Practical Recipe" is the same five generic bullets in every template section.

#### Sections 47.2 Flight dynamics intuition, 47.3 Perception/navigation/obstacle avoidance, 47.4 Coverage/inspection/multi-drone, 47.5 Safety/regulation/simulation - all POOR
Identical template to 47.1: slotted-title theory, template epigraph, template figure caption, `SkillEvidence` worked example, generic recipe. 47.2 in particular is a wasted opportunity: "Flight dynamics intuition" should contain the quadrotor force/moment model and it instead contains the generic POMDP sentence. The real flight-dynamics content lives in 47.6, which makes 47.2 redundant.
- Fix (all four): rewrite with topic-specific theory and a real snippet, OR merge into the deep sections (see Structure Suggestions). 47.2 should be merged into 47.6; 47.3 needs real VIO/obstacle-avoidance content (e.g., a depth-to-ESDF or a minimal collision-check rollout); 47.4 needs a real coverage-path or lawnmower/boustrophedon snippet; 47.5 needs real geofence/failsafe logic.

#### Section 47.6: Quadrotor dynamics and flight control - GOOD
**Lens 1**: PASS, 2 equations. Real rigid-body quadrotor model (thrust/moment allocation, attitude control). This is what 47.2 should have been.
**Lens 2**: PASS.
**Lens 3**: Carries the duplicated "recovered disturbance" epigraph; give it a unique one.
**Lens 4**: PASS, topic-specific code.
**Lens 5**: PASS.

#### Section 47.7: Trajectory generation and GPS-denied missions - GOOD
**Lens 1**: PASS, 2 equations. Minimum-snap / polynomial trajectory and GPS-denied (VIO) estimation. Real content.
**Lens 2**: PASS.
**Lens 3**: Duplicated epigraph; needs its own.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 47.8: PX4 To Hardware: SITL, HITL, Logs, And Flight-Test Evidence - GOOD
**Lens 1**: PASS, 3 equations. SITL/HITL promotion ladder with flight-test evidence; strongest practitioner section in the chapter and precisely the kind of evidence-loop the part promises.
**Lens 2**: PASS, frontier callout is specific (disciplined promotion to hardware under uncertainty as the unsolved problem).
**Lens 3**: Has its own (non-duplicated) epigraph and a real frontier note.
**Lens 4**: PASS, PX4/SITL tool path is named and versioned in spirit.
**Lens 5**: PASS.

### Chapter 48: Autonomous Driving as Embodied AI
**Quality**: NEEDS WORK (split: 48.7-48.9 GOOD; 48.1-48.6 POOR template)

Nine sections (48.1-48.9). The index lists 48.1-48.6; the genuinely good content is in the appended 48.7-48.9 (Vehicle kinematics/dynamics/control; Route/behavior/scenario-based planning; Closed-loop driving evaluation and safety assurance). Sections 48.1-48.6 are template-generated, including 48.6 which also uses the `SkillEvidence` filler.

#### Sections 48.1-48.6 - POOR
Same template pathology as 47.1-47.5 plus 48.6. Confirmed example, 48.3 Theory: "In Detection, lane and behavior prediction, the important state variables are objects, lanes, intents, trajectories, and uncertainty, while the action interface is to predict likely motions for agents that react to the ego vehicle." Title slotted into a fixed sentence; worked example is the `SkillEvidence` dataclass. Tool lists (CARLA, CommonRoad, nuScenes-style stacks) are correct, the one salvageable element.
- Fix: rewrite each with real driving content. 48.1 needs the actual perception->prediction->planning->control decomposition with a concrete metric chain; 48.2 needs a real sensor-fusion equation (e.g., EKF/late-fusion covariance); 48.3 needs a real trajectory-prediction loss (minADE/minFDE) and a snippet; 48.4 needs a real lattice/hybrid-A* or frenet-frame planner snippet; 48.5 needs a real end-to-end / world-model training-loop sketch; 48.6 needs real scenario-coverage / ISO 21448 SOTIF safety-case structure.

#### Section 48.7: Vehicle kinematics, dynamics, and control - GOOD
**Lens 1**: PASS, 2 equations. Real kinematic bicycle model with a runnable constant-curvature rollout (verified: `psi += (v/L)*tan(delta)*dt`). This is what 48.4 should reference.
**Lens 2**: PASS.
**Lens 3**: Duplicated "recovered disturbance" epigraph; needs its own.
**Lens 4**: PASS, genuinely runnable topic-specific code.
**Lens 5**: PASS.

#### Section 48.8: Route, behavior, and scenario-based planning - GOOD
**Lens 1**: PASS, 2 equations. Real planning-hierarchy content (route/behavior/scenario layers).
**Lens 2**: PASS.
**Lens 3**: Duplicated epigraph; needs its own.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 48.9: Closed-Loop Driving Evaluation And Safety Assurance - GOOD
**Lens 1**: PASS, 3 equations. Closed-loop evaluation (vs open-loop), safety-case/assurance argument; the strongest section in the chapter.
**Lens 2**: PASS, frontier callout is specific and current (world-model sim, interaction-realistic agent generation, assurance arguments, the open problem of generative realism hiding unvalidated assumptions).
**Lens 3**: Has its own epigraph.
**Lens 4**: PASS.
**Lens 5**: PASS.

## Cross-Chapter Issues in This Part

1. **Template-generated "syllabus" sections in chapters 47 and 48 (11 sections).** 47.1-47.5 and 48.1-48.6 slot the section title into fixed sentences, use a template epigraph, a template figure caption, and the banned `SkillEvidence` dataclass as the "worked example". These fail the non-substitutability rule outright. By contrast, the appended deep sections of the same chapters (47.6-47.8, 48.7-48.9) are real, topic-specific, runnable. This is the dominant quality problem in the part and the reason chapters 47-48 score NEEDS WORK while 42-46 score GOOD.

2. **Duplicated epigraph across six sections.** "A robot earns trust one recovered disturbance at a time." (attributed "A Field-Tested Control Loop") appears in 46.8, 46.9, 47.6, 47.7, 48.7, 48.8. Each needs a unique, topic-locked epigraph in the style of chapters 42-45.

3. **Template figure captions in ten sections** (47.1-47.5, 48.1-48.5): "Section X: [title] is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation." Pure boilerplate.

4. **Stale part index.** `part-9-.../index.html` lists chapters 44-48 only (omits 42 and 43 entirely) and lists no section beyond the original syllabus (omits 46.8-46.9, 47.6-47.8, 48.7-48.9). The chapter cards and section lists must be regenerated to match the 7 chapters / 48 sections that actually exist.

5. **Universal "Reader Pathway" / "What This Section Develops" / "Action Is The Test" scaffold** in all 48 sections. The lean contract explicitly bans the "Reader Pathway" and "What This Section Develops" boilerplate. Even in the GOOD sections these are removable template furniture; fold their content into the opening frame paragraph.

6. **Worked examples in the GOOD sections are mostly illustrative scorers, not runnable system code.** 42.5 (policy-family if-else) and 43.2 (hand-choice weighted score) are the weakest. The contract wants at least one real, topic-specific runnable example per section; the deep sections (46.8, 47.6-47.8, 48.7-48.9) already meet this and are the model to follow.

7. **Chapter-final sections' "What's Next" points back to the chapter index** rather than the next chapter (e.g., 44.5). Minor navigation polish.

## Top 10 Highest-Priority Fixes for This Part

1. **Rewrite 48.1-48.6 from template into real content.** Files: `module-48-autonomous-driving-as-embodied-ai/section-48.1.html` ... `section-48.6.html`. Remove the `SkillEvidence` dataclass and the slotted-title theory; add per-section equations (perception->prediction->planning chain; fusion covariance; minADE/minFDE; frenet/hybrid-A*; world-model loop; SOTIF safety case) and one runnable snippet each. Cross-link 48.4 to the real bicycle model in 48.7.

2. **Rewrite 47.1-47.5 from template into real content.** Files: `module-47-drones-and-aerial-embodied-ai/section-47.1.html` ... `section-47.5.html`. Same surgery. Merge 47.2 ("Flight dynamics intuition") into 47.6 ("Quadrotor dynamics and flight control") since 47.6 already contains the real model; give 47.3/47.4/47.5 real VIO/coverage/failsafe content.

3. **Replace the 6 duplicated epigraphs.** Files: 46.8, 46.9, 47.6, 47.7, 48.7, 48.8. Draft replacements: 46.8 "Humanoid dynamics is bookkeeping for momentum the floor is allowed to refuse."; 46.9 "Loco-manipulation is where the legs and the hands stop pretending they have separate budgets."; 47.6 "A quadrotor is four numbers arguing about six degrees of freedom."; 47.7 "A trajectory is a promise about acceleration the rotors must keep."; 48.7 "The controller does not steer the car, the tires do, and they negotiate."; 48.8 "Planning is choosing which future to be wrong about most cheaply."

4. **Replace the 10 template figure captions** (47.1-47.5, 48.1-48.5) with captions that describe the actual diagram content per section.

5. **Regenerate the part index.** File: `part-9-.../index.html`. Add chapter cards for 42 and 43; update chapter 46/47/48 cards to list 46.8-46.9, 47.6-47.8, 48.7-48.9. Fix "Chapters: 7" already states 7 but cards show only 5.

6. **Add the capture-point / ZMP equation to 45.2.** File: `module-45-locomotion-and-mobility/section-45.2.html`. Add $x_{cap} = x_{com}+\dot x_{com}\sqrt{z/g}$ with the LIP assumption and its breakdown regime.

7. **Verify and strengthen the OSC null-space hierarchy equation in 46.3.** File: `module-46-.../section-46.3.html`. Ensure the prioritized null-space projection (or stacked QP) is shown, with one line on strict vs soft task priority.

8. **Replace the two weakest worked examples** in 42.5 (policy-family selector) and 43.2 (hand chooser) with real API snippets (robomimic/LeRobot dataset+action-space inspection; a MoveIt gripper/grasp config), so each carries one runnable topic-specific example.

9. **Strip the "Reader Pathway" + "What This Section Develops" + "Action Is The Test" scaffold** across all 48 sections, folding the substance into the opening frame paragraph per the lean contract.

10. **Add 2-3 Paper Spotlight callouts to chapters 43 and 46** (e.g., dexterous in-hand RL sim-to-real in 43.4; HumanPlus/HOVER in 46.4) with the actual result numbers, to make the frontier "alive" rather than gestured at.

## Structure Suggestions for This Part

- **Merge 47.2 into 47.6.** "Flight dynamics intuition" (template, empty) is fully subsumed by "Quadrotor dynamics and flight control" (real). Keep the deep section, retitle it "Flight dynamics and quadrotor control", delete the template stub.
- **Reorder chapters 47 and 48 so the deep sections lead or interleave.** Currently the template stubs (47.1-47.5, 48.1-48.6) come first and the real content (47.6-47.8, 48.7-48.9) is appended at the end. After rewriting the stubs, interleave so each concept's intuition and its real mechanism sit together (e.g., merge 48.4 route/local planning with 48.8 route/behavior/scenario planning; merge 48.1 perception/prediction/planning/control overview with 48.7 vehicle control rather than leaving a generic overview and a real-control section far apart). Several pairs are near-duplicates by title: 48.4 vs 48.8 (planning), and the overview 48.1 partially overlaps 48.7/48.9.
- **Surface 46.8 and 46.9 in the syllabus.** They are strong, on-audience (Boston Dynamics loco-manipulation) sections that are currently invisible in the index; promote them to first-class chapter sections.
- **No chapter should be dropped.** The seven-chapter scope is correct for the audience; the fix is content, not structure removal, except the 47.2/47.6 merge.
