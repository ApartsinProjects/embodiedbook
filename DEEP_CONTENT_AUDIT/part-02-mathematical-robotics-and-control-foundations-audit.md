# Part 2 Content Audit: Mathematical, Robotics, and Control Foundations

## Part Overview

Part 2 covers exactly the right curriculum for a Boston Dynamics / embodied-AI-research audience (frames, kinematics, dynamics, control, sensing) and the topic ordering is sound. The problem is not coverage, it is execution: the part was clearly generated from a single section template and only partly remediated. Chapter 4 has been genuinely upgraded (sections 4.4 to 4.7 carry real SE(3) algebra, runnable code with verified printed output, and topic-specific debugging), but Chapters 5, 6, 7, and 8 are still mostly template shells. Across 32 of the 36 sections the worked example is non-runnable filler that the lean section contract explicitly bans (`plan = [skill for skill in skills]`, `EmbodiedStep("...", "act", "observe consequence")`, or a `points_camera = points_world - camera_offset` snippet that is pasted verbatim into a LiDAR section, a tactile section, a Kalman-filter section, and a sensor-fusion section). Every section also carries an identical ~120-line "production-depth-expansion" boilerplate block (same `EvidenceRecord` dataclass, same five-row library table, same "Implementation Recipe") whose text is unchanged except for the slotted topic name. The single highest-value action for this part is to replace template worked examples and template Theory blocks with real, topic-specific math and runnable code, and to delete or radically shrink the repeated production block.

A blunt summary of the substitutability test: in Chapters 5, 6, and 8, swapping the section title leaves almost every paragraph unchanged. That is the definition of boilerplate.

## Fun Elements to Preserve

Most "fun" callouts in this part are mechanically templated and should NOT be preserved as-is (see Cross-Chapter Issues). The genuinely good, topic-specific lines worth keeping are concentrated in Chapter 4's first three sections:

- **4.1 fun-note ("Mental Model")**: "A robot log is a lab notebook that does not get tired. Give it frame names, timestamps, and residuals, and it will remember exactly where the story stopped making sense." Genuine, memorable, topic-true. KEEP.
- **4.2 fun-note ("Mental Model")**: "If every length-three array looks like a coordinate, the robot is reading a spreadsheet with the column headers removed." Excellent, accurate analogy for the points-vs-vectors-vs-poses confusion. KEEP.
- **4.3 fun-note ("Mental Model")**: "Euler angles are excellent for telling a human what happened. They are less excellent as the robot's long-term memory of orientation." Accurate, witty, captures the real engineering tradeoff. KEEP.
- **4.1 key-insight ("Action Is The Test")** and **4.7 warning** ("retrain the detector when the actual bug is geometric"): not jokes, but genuine "aha" framings that should survive edits.
- **Part II Memory Anchor (index.html)**: "Geometry says where, kinematics says what motion is possible, dynamics says what motion costs, control says how errors are corrected, and estimation says what the agent can know on time." Strong one-line spine for the whole part. KEEP and consider repeating at chapter openings.

Bespoke named callouts in Chapter 7 are also worth preserving because they carry real content, even though the surrounding section is templated: "PID Tuning Recipe" (7.3), "LQR Tuning Is Cost Design" (7.4), "MPC Deadline Rule" (7.5), "Priority Is A Safety Contract" (7.6), "Safety Filter Before Deployment" (7.7). These are the only topic-specific engineering insight in those sections.

Everything else under `fun-note` is one of four rotating template sentences (see below) and is NOT a fun element to preserve; several are grammatically broken by the lowercased topic injection.

## Chapter-by-Chapter Analysis

### Chapter 4: Spatial Representation and Coordinate Frames
**Quality**: GOOD (4.4 to 4.7) mixed with NEEDS WORK (4.1 to 4.3)

This is the strongest chapter in the part. Sections 4.4 to 4.7 are the model the rest of Part 2 should be rewritten toward: real SE(3) math, runnable code with actual printed output, and topic-specific failure analysis. Sections 4.1 to 4.3 still run on the older "Reader Pathway / What This Section Develops" template with generic non-runnable worked examples.

#### Section 4.1: Why space is the substrate of embodiment - NEEDS WORK
**Lens 1 (Deep Explanation)**: The frame-plus-quantity contract (value, frame_id, timestamp, units, validity) is a genuinely useful idea and is stated clearly. But the "Theory" is thin: one line of notation ($p^A$, $T_{AB}$) and no derivation. For an opening section this is acceptable as motivation; the weakness is the template scaffolding around it ("Reader Pathway", "What This Section Develops") which the lean contract bans.
- Fix: Cut the "Reader Pathway" callout and the "What This Section Develops" heading. Open directly with the mug/gripper scenario already present in paragraph 1.

**Lens 2 (Research Frontier)**: The VLA callout ("Large vision-language-action models increasingly predict spatial actions directly") is current and correct but bare. No paper named, no open question.
- Fix: Name RT-2 / OpenVLA / pi-0 and state one open question: "Open question: when a VLA emits an end-effector pose directly, in which frame is that pose defined, and how should a deployed stack validate frame consistency when the model never sees an explicit transform tree?"

**Lens 3 (Fun/Engagement)**: Good lab-notebook fun-note (preserve). Opening epigraph "A robot without frames has many coordinates and no agreement" is genuinely witty and shared with 4.2/4.3.
- Opportunity: none needed; this section's hooks are fine.

**Lens 4 (Examples/Analogies)**: Worked example is real and runnable (camera-to-base homogeneous transform) but trivial. No verified output shown (only "Expected output: a three-value target position"). Compare to 4.4 which prints actual numbers.
- Fix: Add the real printed output `[0.45 0.35 1.35]` (or whatever the matrix yields) so the reader can self-check, matching the 4.4-4.7 style.

**Lens 5 (Teaching Flow)**: Good as a part opener. The duplicated production block at the end is dead weight that breaks pacing.

#### Section 4.2: Points, vectors, poses, frames - NEEDS WORK (close to GOOD)
**Lens 1**: Strong. The point-vs-vector transform rule ($p^A=R_{AB}p^B+t_{AB}$ vs $v^A=R_{AB}v^B$) with the homogeneous-coordinate 1-vs-0 trailing coordinate is exactly the right depth and is correct.
- Minor: state the assumption that this holds only for rigid transforms (no scale/shear).

**Lens 2**: Robot-foundation-model callout is current but generic.
- Fix: name one concrete object-centric representation (e.g. keypoint affordances, NOCS) rather than "spatial tokens, keypoints, or object-centric features".

**Lens 3**: Excellent "spreadsheet with headers removed" fun-note. KEEP. Epigraph reused from 4.1.

**Lens 4**: Worked example (point vs vector under a transform with translation) is topic-perfect and runnable. PASS. Add printed output to match 4.4-4.7.

**Lens 5**: PASS, except the template scaffolding and production block.

#### Section 4.3: Rotations (matrices, Euler, axis-angle, quaternions) - NEEDS WORK (close to GOOD)
**Lens 1**: Good. Invariants ($R^TR=I$, $\det R=1$, unit quaternion) stated, and the "valid under a different convention" framing (xyzw vs wxyz, degrees vs radians, zyx vs xyz, active vs passive) is exactly the practitioner pain point.
- Fix: Add one sentence of derivation intuition for why quaternions avoid gimbal lock (Euler representation is a chart on SO(3) with coordinate singularities; the unit quaternion double-covers SO(3) smoothly).

**Lens 2**: 6D rotation representation callout is current (Zhou et al. 2019 continuity result).
- Fix: cite it: "Zhou et al. (2019) showed that 3D and 4D rotation parameterizations are discontinuous and that a 6D representation is continuous, which is why pose regressors increasingly predict 6D." Add open question on rotation representation for diffusion policies.

**Lens 3**: Excellent Euler-angles fun-note. KEEP.

**Lens 4**: Worked example uses `scipy.spatial.transform.Rotation` properly (real library, real conversion, orthogonality check). PASS. This is the best of the 4.1-4.3 trio.

**Lens 5**: PASS.

#### Section 4.4: Rigid transforms, homogeneous coordinates, SE(3) - GOOD
**Lens 1**: Strong. Full $p_A=R_{AB}p_B+t_{AB}$, the 4x4 homogeneous form, composition $T_{BC}=T_{BW}T_{WC}$, and the group structure (identity, inverse, $T_{AB}T_{BA}=I$). Assumptions stated (rigid frames, matching units, appropriate timestamp). This meets graduate depth.
- Minor gap: no mention of the Lie-algebra side (se(3), the exponential/log map) even though the section title says SE(3) and later sections (5.1 twists, 5.7 Jacobians) need it. Add a 3-sentence bridge to twists.

**Lens 2**: Research Frontier callout here is pure template ("treat frontier claims as hypotheses until they expose enough detail..."). This is the weakest part of an otherwise strong section.
- Fix: replace with real content, e.g. "Open question: learned SE(3)-equivariant networks (e.g. equivariant point-cloud and diffusion models) promise pose predictions that respect the group structure by construction. When does enforcing equivariance beat simply augmenting data with random transforms?"

**Lens 3**: Memory-hook fun-note is templated and grammatically broken by lowercased topic ("rigid transforms, homogeneous coordinates, se(3) visible twice"). Replace with a topic-specific line, e.g. "SE(3) multiplication is not commutative: rotate-then-translate lands somewhere different from translate-then-rotate. The robot will happily reach the wrong place with full confidence."

**Lens 4**: PASS. Worked example composes two transforms, applies to a point, AND verifies with a round-trip inverse, with real printed output (`base point: [0.8, 0.1, 1.45]`, `round trip: [0.3, 0.1, 0.2]`). This is exactly the right-tool-payoff pattern.

**Lens 5**: PASS. Good build from 4.2/4.3.

#### Section 4.5: 2D and 3D transformations; transform trees (tf in ROS) - GOOD
**Lens 1**: Strong. Tree as DAG with one parent per child, path composition $T_{map,camera}=T_{map,odom}T_{odom,base}T_{base,camera}$, SE(2) vs SE(3) distinction, and the crucial point that a tf lookup needs both a path AND a time. PASS.

**Lens 2**: Template frontier callout. Same fix as 4.4. A real frontier note here: factor-graph / sliding-window estimators (GTSAM) increasingly replace the static tf model for time-varying calibration; state that as an open direction.

**Lens 3**: Templated memory-hook (the "next frame of video" variant). Replace with tf-specific humor: "tf2's most common error message, 'extrapolation into the future,' is the robot politely refusing to guess where it was before it knew."

**Lens 4**: PASS. Worked example builds named edges and composes a path with real output `[3.7, 1.0, 0.8]`. Honestly notes the rotation is omitted for inspectability, which is a fair teaching choice.
- Opportunity: add a second variant WITH a rotation edge so readers see direction bugs, since the section's whole point is direction/order errors.

**Lens 5**: PASS.

#### Section 4.6: Camera, body, and world frames - GOOD
**Lens 1**: Strong. Real pinhole model ($u=f_x X/Z + c_x$), back-projection, and the genuinely important OpenCV (x-right, y-down, z-forward) vs robotics body (x-forward, y-left, z-up) convention clash. Assumptions stated (calibrated, distortion-corrected, synchronized depth). PASS.

**Lens 2**: Template frontier callout.
- Fix: real note on metric-depth foundation models (Depth Anything v2, UniDepth, 2024) and the open question of whether monocular metric depth is reliable enough to skip a depth sensor for manipulation reach.

**Lens 3**: Templated fun-note. Replace with camera-specific line.

**Lens 4**: PASS. Worked example back-projects one pixel and shifts to body frame with real output. Good, minimal, topic-specific.
- Note: the body-frame step only adds a translation; given the section explicitly raises the optical-vs-body axis flip, the example should apply the rotation that realizes that flip, otherwise it under-demonstrates its own point.

**Lens 5**: PASS.

#### Section 4.7: Common frame mistakes and how to debug them - GOOD
**Lens 1**: Strong and practical. Inverse check ($T_{AB}T_{BA}\approx I$), distance preservation, determinant check for reflections/handedness, and the "shrink the episode" debugging method. PASS.
- This is the best debugging section in the part.

**Lens 2**: Template frontier callout (weakest part).

**Lens 3**: Templated control-room-label fun-note; serviceable but generic. The warning ("retrain the detector when the actual bug is geometric") is the real memorable insight; promote it.

**Lens 4**: PASS. Worked example runs determinant + round-trip residual checks with real output (`determinant: 1.0`, `round-trip residual: 0.0`).

**Lens 5**: PASS. Good chapter capstone.

### Chapter 5: Kinematics and Robot Motion
**Quality**: NEEDS WORK (5.5, 5.6 partial) to POOR (rest)

Every section uses the closed-loop-template Theory ("Formally, [TOPIC] should be placed inside the closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$..."). Most worked examples are the banned `plan = [skill for skill in skills]` filler. Only 5.5 (one real FK equation) and 5.6 (real IK prose) have any topic-specific theory. This is a kinematics chapter that, for the most part, contains no kinematics math.

#### Section 5.1: Position, velocity, acceleration; twists - POOR
**Lens 1**: FAIL. The section title promises twists (the se(3) screw representation), which is the load-bearing concept for 5.7 (Jacobians) and Chapter 6 (dynamics). The Theory block contains zero twist math, only the template closed-loop sentence. No definition of a twist $\xi=(v,\omega)$, no spatial-vs-body twist, no screw axis.
- Fix: Add real theory: "A twist stacks linear and angular velocity, $\xi=(v,\omega)\in\mathbb{R}^6$, and is the velocity element of se(3). The body twist $\xi_b$ and spatial twist $\xi_s$ are related by the adjoint, $\xi_s=\mathrm{Ad}_{T_{sb}}\xi_b$. Differentiating a pose gives $\dot T T^{-1}=[\xi_s]$, the matrix form of the spatial twist." Then a worked example that numerically differentiates a moving frame and recovers its twist.

**Lens 2**: Template frontier callout.

**Lens 3**: Templated fun-note (the "visible twice" variant), grammatically broken.

**Lens 4**: FAIL. Worked example is `instruction/skills/plan` filler with no relation to twists.

**Lens 5**: FAIL as a prerequisite supplier. 5.7 and Chapter 6 assume twists that this section never delivers.

#### Section 5.2: Holonomic vs. non-holonomic motion - POOR
**Lens 1**: FAIL. No definition of a non-holonomic constraint (a non-integrable velocity constraint, $A(q)\dot q=0$ that cannot be reduced to a position constraint). This is THE concept of the section.
- Fix: state the rolling-without-slipping constraint for a unicycle ($\dot x \sin\theta - \dot y\cos\theta = 0$), explain why it is non-integrable, and contrast with a holonomic constraint that reduces dimensionality of configuration space.

**Lens 2-5**: Template throughout; worked example is filler.

#### Section 5.3: Differential-drive and car-like robots - POOR
**Lens 1**: FAIL. No kinematic model. A differential-drive section must contain $\dot x = \frac{r}{2}(\omega_L+\omega_R)\cos\theta$, etc., and the car-like (bicycle) model $\dot\theta=\frac{v}{L}\tan\delta$.
- Fix: add both models with the worked example integrating one of them forward over a few timesteps and plotting/printing the path.

**Lens 4**: FAIL. Filler worked example.
- This is a high-value, concrete, easy-to-make-runnable topic; the current emptiness is a missed opportunity.

#### Section 5.4: Robot arms, joints, the kinematic chain - POOR
**Lens 1**: FAIL. No DH parameters, no joint-type taxonomy (revolute/prismatic), no product-of-exponentials. Just the template.
- Fix: define the chain as a sequence of joint transforms, introduce either DH or PoE convention, and state assumptions (rigid links, ideal joints).

**Lens 4**: FAIL. Filler worked example.

#### Section 5.5: Forward kinematics - NEEDS WORK
**Lens 1**: Partial. Contains ONE real result: the planar 2-link FK ($x=l_1\cos q_1+l_2\cos(q_1+q_2)$, $y=l_1\sin q_1+l_2\sin(q_1+q_2)$) and the product-of-transforms framing. That is genuinely topic-specific.
- Fix: the rest of the Theory is template; remove the closed-loop boilerplate sentences and expand the FK derivation to a 3-link or include the homogeneous-transform spatial version.

**Lens 4**: FAIL. Despite real theory, the worked example is STILL the `plan = [skill for skill in skills]` filler. This is the clearest single illustration of the part's core defect: a section that derived a 2-link FK closed form and then refused to run it.
- Fix: replace the filler with the 5 lines that actually compute the 2-link FK from the equations just derived and print the end-effector position.

**Lens 5**: Weak. FK is the "baseline oracle" for IK (5.6); the prose says so but the code does not demonstrate it.

#### Section 5.6: Inverse kinematics (analytic, numerical/Jacobian, learned) - NEEDS WORK
**Lens 1**: Partial-good. Real taxonomy (analytic closed-form, numerical Jacobian iteration, learned), and the important nuance that a learned IK prediction "can be confident and infeasible at the same time" and still needs FK + constraint checks. Good practitioner framing.
- Fix: add the actual Jacobian-update IK step: $\Delta q = J^{\dagger}(x_{des}-f(q))$, the damped-least-squares variant near singularities ($J^T(JJ^T+\lambda^2 I)^{-1}$), and state convergence assumptions.

**Lens 2**: Template frontier callout. Real frontier: learned IK / neural IK for redundant and continuum robots; open question on guaranteeing feasibility of learned solutions.

**Lens 4**: FAIL. Filler worked example. Should be a numerical IK loop on the 2-link arm from 5.5.

**Lens 5**: Builds on 5.5 conceptually but neither section shares runnable code, so the FK-as-oracle-for-IK connection is asserted not shown.

#### Section 5.7: Jacobians, singularities, manipulability - POOR
**Lens 1**: FAIL. No Jacobian definition, no singularity condition ($\det J=0$ or rank loss), no manipulability ellipsoid / Yoshikawa measure ($w=\sqrt{\det(JJ^T)}$). These are all standard, derivable, and central to a Boston Dynamics audience.
- Fix: derive $\dot x = J(q)\dot q$, define singularities as rank-deficiency of $J$, define the manipulability ellipsoid from the SVD of $J$, and give the Yoshikawa index. Worked example: compute $J$ for the 2-link arm and show $w$ collapsing as the arm straightens.

**Lens 4**: FAIL. Filler.

#### Section 5.8: Motion constraints - POOR
**Lens 1**: FAIL. No constraint taxonomy (equality/inequality, holonomic/non-holonomic, joint limits, velocity/acceleration limits, collision). Template only.

**Lens 4**: FAIL. Filler.

### Chapter 6: Dynamics and Simulation Math
**Quality**: POOR

This is the weakest chapter for theory depth. A dynamics chapter for embodied-AI practitioners that does not write the manipulator equation in its body text is not doing its job. Every Theory block is the closed-loop template; every worked example is the `EmbodiedStep("topic", "act", "observe consequence")` filler. The topics here (manipulator equation, contact/friction cones, integrator stability, differentiable physics, GPU-parallel sim) are exactly what this audience cares about and are currently almost entirely empty of substance.

#### Section 6.1: From kinematics to dynamics (forces, torques, inertia) - POOR
**Lens 1**: FAIL. No Newton-Euler, no relation $\tau = I\dot\omega + \omega\times I\omega$, no inertia tensor definition. Template only.
- Fix: introduce force/torque, the inertia tensor, and Newton-Euler for a single rigid body as the bridge the title promises.

**Lens 4**: FAIL. `EmbodiedStep` filler.

#### Section 6.2: Rigid-body dynamics; the manipulator equation - POOR
**Lens 1**: FAIL. This section's entire reason to exist is the manipulator equation $M(q)\ddot q + C(q,\dot q)\dot q + g(q) = \tau$, and it is not in the Theory body. This is the most important single omission in Part 2.
- Fix: write the manipulator equation, name each term (mass matrix, Coriolis/centrifugal, gravity), state structural properties (M symmetric positive-definite; $\dot M - 2C$ skew-symmetric), and give the regime of validity (rigid links, ideal actuators, no contact). Worked example: compute $M(q)$ for the 2-link arm and verify positive-definiteness.

**Lens 2**: Real frontier: spatial-vector algebra and Featherstone's articulated-body algorithm ($O(n)$ forward dynamics), as implemented in Pinocchio; open question on autodiff through ABA for trajectory optimization.

**Lens 4**: FAIL. Filler.

#### Section 6.3: Contact, friction, and why contact-rich sim is hard - POOR
**Lens 1**: FAIL. No friction cone, no complementarity formulation (LCP / the Stewart-Trinkle model), no explanation of WHY contact is hard (non-smooth dynamics, stiff systems, the choice between hard and soft contact). The title literally asks "why is it hard" and the section does not answer.
- Fix: introduce the Coulomb friction cone, the linear complementarity formulation of contact, and the soft-contact (compliant, MuJoCo-style) alternative; explain non-uniqueness and indeterminacy of rigid contact.

**Lens 2**: Strong real frontier available: MuJoCo's convex contact model, the contact-gradient problem for differentiable sim (6.5), and the sim-to-real contact gap. Currently template.

**Lens 4**: FAIL. Filler.

#### Section 6.4: Numerical integration and stability - POOR
**Lens 1**: FAIL. No integrators (explicit/semi-implicit Euler, RK4), no stability region, no stiffness discussion, no timestep-vs-stiffness tradeoff. This is directly derivable and concrete.
- Fix: give explicit Euler, semi-implicit (symplectic) Euler, and RK4; show why semi-implicit Euler is the simulation default (energy behavior); state the stability bound for a stiff spring ($\Delta t < 2/\omega$). Worked example: integrate a spring-mass with two integrators and show one diverging.

**Lens 4**: FAIL. Filler.

#### Section 6.5: Differentiable physics: what it buys you - POOR
**Lens 1**: FAIL. No definition of differentiable simulation, no gradient-through-dynamics, no discussion of where gradients break (contact discontinuities). Template only.
- Fix: define $\partial(\text{state}_{t+1})/\partial(\text{action}_t)$ through the simulator, contrast analytic vs autodiff gradients, and explain the contact-gradient pathology (zero or exploding gradients at contact events).

**Lens 2**: Current frontier is rich here: Brax, MJX, Warp, DiffTaichi, the "do differentiable-sim gradients actually help RL?" debate (often they do not, due to chaotic/contact-discontinuous landscapes). This is a live, citable controversy and a strong open question. Currently template.

**Lens 4**: FAIL. Filler.

#### Section 6.6: Why GPU-parallel simulation changed robot learning - POOR
**Lens 1**: FAIL. No throughput argument (thousands of parallel envs, on-GPU physics avoiding CPU-GPU transfer), no mention of the specific systems. Template only.
- Fix: explain the architecture (vectorized envs, physics + policy both on GPU), the empirical step-count jump (Isaac Gym / Isaac Lab achieving millions of steps/sec), and why this enabled domain-randomized sim-to-real (ANYmal, in-hand cube). State the assumption/limit: parallelism helps when the bottleneck is sample count, not when it is contact fidelity.

**Lens 2**: This should be the most "alive" section in Chapter 6 (Isaac Lab, MJX, the 2022-2024 sim-to-real wave) and is currently the emptiest. Name OpenAI Dactyl, ETH ANYmal, NVIDIA Eureka. Open question: how far does massively-parallel sim transfer to contact-rich manipulation versus locomotion?

**Lens 4**: FAIL. Filler.

### Chapter 7: Control for AI Practitioners
**Quality**: NEEDS WORK

The best-remediated of Chapters 5 to 8 on theory: every section has one real topic-specific theory paragraph AND one bespoke named callout with genuine engineering content (PID tuning order, LQR cost design, MPC deadline discipline, whole-body priority, safety filtering). The fatal gap is identical to the rest: every worked example is the `instruction/skills/plan` filler. So readers get correct intuition and then a code block that demonstrates nothing about control.

#### Section 7.1: Open-loop vs. closed-loop control - NEEDS WORK
**Lens 1**: Good intuition. Real formalization: open-loop $a_{0:T-1}=g(r_{0:T-1},\hat s_0)$ vs closed-loop $a_t=\pi(\hat s_t,r_t)$, with the validity condition (open-loop works when model + disturbances are predictable). PASS on theory.
**Lens 4**: FAIL. Filler worked example. Should simulate a first-order plant under open vs closed loop with a disturbance and print the divergence.
**Lens 3**: Bespoke callout "Open Loop Is A Promise, Closed Loop Is A Conversation" is a genuinely good line. KEEP.

#### Section 7.2: Feedback, error, stability, overshoot, oscillation - NEEDS WORK
**Lens 1**: Good. Error $e_t=r_t-y_t$, bounded-disturbance stability, overshoot, phase/gain framing. PASS on theory.
- Fix: add a pole/eigenvalue stability statement (discrete: $|\lambda|<1$) so "stability" has a checkable criterion.
**Lens 4**: FAIL. Filler.

#### Section 7.3: PID control, intuition and tuning - NEEDS WORK
**Lens 1**: Good. P/I/D roles explained, and the "PID Tuning Recipe" callout (raise $K_p$, add $K_d$, add $K_i$ last, clamp integral on saturation) is real, ordered, and correct.
**Lens 4**: FAIL. Filler. This is an egregious miss: a PID section with no PID loop. Should be ~15 lines simulating a PID controller on a plant with anti-windup, printing the step response.
**Lens 3**: "PID Tuning Recipe" callout. KEEP.

#### Section 7.4: State-space control, LQR - NEEDS WORK
**Lens 1**: Good. $x_{t+1}=Ax_t+Bu_t$, the quadratic cost, and "LQR Tuning Is Cost Design" ($Q$ and $R$ encode which errors and which actuators matter). PASS on theory.
- Fix: write the optimal gain $u=-Kx$ with $K$ from the discrete algebraic Riccati equation, and state the assumptions (linearization near operating point, full-state feedback, controllability).
**Lens 4**: FAIL. Filler. Should solve LQR for a cart-pole linearization with `scipy.linalg.solve_discrete_are` or `python-control`.

#### Section 7.5: MPC as receding-horizon optimization - NEEDS WORK
**Lens 1**: Good. Receding horizon, execute-first-command-then-replan, constraints-as-first-class. "MPC Deadline Rule" (a plan after the deadline has failed; log solve time, status, fallback) is excellent and practitioner-true.
- Fix: write the finite-horizon QP (cost + dynamics + constraints) explicitly.
**Lens 4**: FAIL. Filler. Should set up a small QP with CasADi or do-mpc and print the first command.
**Lens 3**: "MPC Deadline Rule" callout. KEEP.

#### Section 7.6: Operational-space and whole-body control - NEEDS WORK
**Lens 1**: Good. Task-space motion, $\dot x = J(q)\dot q$, whole-body prioritization, and "Priority Is A Safety Contract". This is the right preview for humanoids.
- Fix: add the operational-space dynamics ($\Lambda(q)=(J M^{-1} J^T)^{-1}$, the task-space inertia) at least by name, and null-space projection for secondary tasks.
**Lens 4**: FAIL. Filler.

#### Section 7.7: Controllers vs. policies; when learning helps / makes control unsafe - GOOD (theory) / NEEDS WORK (code)
**Lens 1**: Strong and the most important conceptual section for this audience. Classical vs learned tradeoff, hybrid with learned policy wrapped by a safety filter ("Safety Filter Before Deployment"). PASS on theory.
**Lens 2**: Real frontier available: control barrier functions, runtime assurance / safety shields, residual policies. Name them; currently the frontier callout is template.
**Lens 4**: FAIL. Filler. Should demonstrate a learned action being clamped by a CBF/limit filter.
**Lens 3**: "Safety Filter Before Deployment" callout. KEEP.

### Chapter 8: Sensors, Perception Hardware, and State Estimation
**Quality**: POOR

The weakest chapter overall. Every Theory block is the bare two-sentence closed-loop template with NO topic-specific math (verified for 8.1, 8.2, 8.4, 8.5, 8.6, 8.7, 8.8). Every worked example is the identical irrelevant snippet `points_camera = points_world - camera_offset` regardless of whether the topic is LiDAR, tactile sensing, noise models, Kalman filtering, or sensor fusion. Each section's only topic-specific content is one bespoke named callout (e.g. "Noise model fitting recipe", "Fusion pipeline audit"). A state-estimation chapter with no Kalman filter equations and no covariance math fails its core promise.

#### Section 8.1: What sensors provide and what they cost - POOR
**Lens 1**: FAIL. No sensor taxonomy with quantitative cost axes (rate, latency, noise, range, power, $). Template only. Bespoke callout "Sensor selection audit" is the only real content.
- Fix: build a real comparison table (camera, depth, LiDAR, IMU, encoder, F/T, tactile) with rate, latency, noise, failure mode.
**Lens 4**: FAIL. Irrelevant `points_camera` snippet.

#### Section 8.2: Cameras, depth (stereo/structured light/ToF), LiDAR - POOR
**Lens 1**: FAIL. No stereo disparity-to-depth ($Z=fB/d$), no ToF/structured-light tradeoffs, no LiDAR range model. These are standard and central.
- Fix: give the disparity equation, the failure regimes of each depth modality (stereo on textureless surfaces, ToF on specular/transparent, structured light in sunlight), LiDAR sparsity.
**Lens 4**: FAIL. Irrelevant snippet (and this is the one section where `points_camera` would almost fit, yet it still does not back-project from disparity).

#### Section 8.3: IMU, wheel odometry, joint encoders, proprioception - POOR
**Lens 1**: FAIL. No IMU model (bias + random walk + noise), no odometry integration, no encoder resolution. Template only.
- Fix: write the gyro/accel measurement model with bias, the dead-reckoning drift growth, and why proprioception is high-rate but drifting.
**Lens 4**: FAIL. Irrelevant snippet.

#### Section 8.4: Tactile and force/torque sensing (GelSight, DIGIT) - POOR
**Lens 1**: FAIL. Template Theory. Bespoke "Contact sensing calibration recipe" callout is the only real content. The named hardware (GelSight, DIGIT) appears only in the title, not explained.
- Fix: explain optical tactile sensing (gel deformation imaged by a camera, photometric-stereo normal reconstruction), F/T sensor strain-gauge model, and what tactile buys for manipulation (slip detection, contact localization).
**Lens 4**: FAIL. Irrelevant snippet.

#### Section 8.5: Sensor noise and uncertainty models - POOR
**Lens 1**: FAIL. No Gaussian model, no covariance, no bias-vs-noise distinction. For a section literally about uncertainty models this is the core omission.
- Fix: define additive Gaussian noise, covariance matrix, bias, drift; show how to estimate noise covariance from static data. This is the prerequisite for 8.6.
**Lens 4**: FAIL. Irrelevant snippet. Should sample from a noise model and fit its covariance.

#### Section 8.6: Bayesian filtering: Kalman, EKF, particle filters - POOR
**Lens 1**: FAIL. This is the flagship state-estimation section and it contains NO filter math: no predict/update equations, no Kalman gain, no EKF linearization, no particle resampling. This is the second-most-serious omission in Part 2 after the manipulator equation.
- Fix: write the linear KF predict ($\hat x^-=A\hat x$, $P^-=APA^T+Q$) and update ($K=P^-H^T(HP^-H^T+R)^{-1}$, etc.), state the EKF Jacobian linearization, and contrast particle filters for non-Gaussian/multimodal beliefs. Worked example: a 1D constant-velocity KF tracking a noisy position, printing the shrinking covariance.
**Lens 2**: Frontier: learned/differentiable filters, factor-graph smoothing (GTSAM), invariant EKF for legged robots. Currently template.
**Lens 4**: FAIL. The irrelevant `points_camera` snippet in a Kalman-filter section is the single clearest non-substitutability failure in the part.

#### Section 8.7: Sensor fusion intuition and practice - POOR
**Lens 1**: FAIL. No fusion math (inverse-variance weighting, $\hat x = (\sum \Sigma_i^{-1})^{-1}\sum \Sigma_i^{-1} x_i$), no loose-vs-tight coupling, no time-sync discussion. Bespoke "Fusion pipeline audit" callout is the only real content.
- Fix: derive inverse-variance fusion of two estimates, then connect to multi-sensor EKF; emphasize timestamp alignment and covariance honesty (the part's own index warns about "covariance overconfidence" but the section never defines covariance).
**Lens 4**: FAIL. Irrelevant snippet.

#### Section 8.8: Perception as an imperfect window into the world - POOR
**Lens 1**: FAIL. Template. Reasonable as a reflective closing section, but it offers no concrete content beyond the "Perception diagnostic loop" callout.
- Fix: keep it short and reflective but ground it in partial observability (POMDP belief state) and one concrete failure taxonomy.
**Lens 4**: FAIL. Irrelevant snippet.

## Cross-Chapter Issues in This Part

1. **Banned filler worked examples in 32 of 36 sections.** Three filler patterns recur, all explicitly prohibited by the lean section contract: `plan = [skill for skill in skills]` (Chapters 5, 7), `EmbodiedStep("topic", "act", "observe consequence")` (Chapter 6), and `points_camera = points_world - camera_offset` (all of Chapter 8). Only 4.4-4.7 (and partially 4.1-4.3) have real runnable topic-specific examples with printed output. This is the number-one issue.

2. **Template Theory blocks.** Most sections in Chapters 5, 6, and 8 open the Theory with the identical sentence "Formally, [TOPIC] should be placed inside the closed-loop transition $o_t \rightarrow \hat s_t \rightarrow a_t \rightarrow o_{t+1}$..." and contain no further topic-specific derivation. The most important standard equations of the field are missing from the sections named after them: the manipulator equation (6.2), the Kalman filter (8.6), twists (5.1), the Jacobian/manipulability (5.7), friction cones (6.3).

3. **Identical ~120-line "production-depth-expansion" block in every section.** Same `EvidenceRecord` dataclass, same five-row "Library Choices And Verification Checks" table, same "Implementation Recipe", same "Evidence Gate" and "Exercise Extension". The only per-section variation is the slotted topic string. This block roughly doubles each section's length with non-substitutable boilerplate and buries the real content. It should be cut to a short shared sidebar or removed.

4. **Auto-generated epigraphs.** 33 of 36 sections use the formula "[TOPIC] matters when the next action changes the evidence you thought you had." Only 4.1-4.3 share a real epigraph ("A robot without frames has many coordinates and no agreement"). Replace per-chapter with a few real quotes (Murray-Li-Sastry, Featherstone, Kalman, Khatib).

5. **Templated, grammatically broken fun-notes.** Four rotating bodies cycle across all 32 non-4.1-4.3 sections with the topic name injected and lowercased, producing broken phrases like "rigid transforms, homogeneous coordinates, se(3) visible twice". These read as filler and several are ungrammatical. Only the 4.1-4.3 fun-notes are genuine.

6. **Template Research-Frontier callouts.** Outside Chapter 4's 4.1-4.3 (which have real but bare frontier notes), nearly every frontier callout is "treat frontier claims as hypotheses until they expose enough detail to reproduce the result". No papers named, no open questions stated, in a 2024-2026 field that is intensely active (VLAs, MJX/Isaac Lab, differentiable sim, CBFs, foundation depth models). The part currently feels closed and static despite sitting on top of the most dynamic area in robotics.

7. **Prerequisite chain broken by missing content.** 5.1 (twists), 5.5/5.7 (FK/Jacobian), 6.2 (manipulator equation), 8.5/8.6 (noise/Kalman) are prerequisites that later sections and chapters assume, but they do not actually deliver the math. The "What's Next" links exist, but the content they promise upstream is absent.

## Top 10 Highest-Priority Fixes for This Part

1. **Add the manipulator equation to 6.2** (`module-06-dynamics-and-simulation-math/section-6.2.html`). Write $M(q)\ddot q + C(q,\dot q)\dot q + g(q)=\tau$, name each term, state M's positive-definiteness and the skew-symmetry of $\dot M - 2C$, and compute $M(q)$ for a 2-link arm in the worked example. This is the single most important missing equation in Part 2.

2. **Add the Kalman filter to 8.6** (`module-08.../section-8.6.html`). Write predict/update with the Kalman gain, EKF linearization, particle-filter contrast, and a runnable 1D constant-velocity tracker that prints the shrinking covariance. Replace the irrelevant `points_camera` snippet.

3. **Replace all `points_camera = points_world - camera_offset` worked examples across Chapter 8** (8.1-8.8) with topic-specific runnable code: a sensor-cost table (8.1), disparity-to-depth (8.2), IMU dead-reckoning drift (8.3), gel-deformation/normal demo or F/T strain model (8.4), noise sampling + covariance fit (8.5), KF (8.6), inverse-variance fusion (8.7), belief-state demo (8.8).

4. **Replace all `plan = [skill for skill in skills]` worked examples across Chapter 5** (5.1-5.8) with runnable kinematics: differentiate a frame to recover a twist (5.1), unicycle non-holonomic constraint check (5.2), integrate the differential-drive/bicycle model (5.3), build a chain transform (5.4), compute the 2-link FK already derived in 5.5, run a damped-least-squares IK loop (5.6), compute J + manipulability index (5.7), enforce a joint/velocity limit (5.8).

5. **Replace all `EmbodiedStep(...)` worked examples across Chapter 6** (6.1-6.6) with runnable dynamics: Newton-Euler for one body (6.1), $M(q)$ for 2-link (6.2), friction-cone / soft-contact force (6.3), explicit vs semi-implicit Euler on a spring showing divergence (6.4), a tiny autodiff-through-a-step gradient (6.5), a parallel-env throughput count (6.6).

6. **Replace all `instruction/skills/plan` worked examples across Chapter 7** (7.1-7.7) with real control loops: open vs closed loop under disturbance (7.1), pole stability check (7.2), PID with anti-windup step response (7.3), LQR via discrete Riccati (7.4), an MPC QP first-command (7.5), operational-space Jacobian map (7.6), a CBF/limit safety-filter clamp on a learned action (7.7). The theory and named callouts here are already good, so only the code needs replacing.

7. **Cut or drastically shrink the "production-depth-expansion" block in all 36 sections.** Reduce the repeated `EvidenceRecord` + library table + Implementation Recipe to at most a short shared callout, or move it to one per-chapter appendix. This roughly halves each section's length and surfaces the real content.

8. **Add real Theory math to the empty kinematics/dynamics/sensing sections**: twists + adjoint (5.1), non-holonomic constraint (5.2), diff-drive/bicycle models (5.3), DH or PoE chain (5.4), Jacobian + singularity + manipulability (5.7), Newton-Euler (6.1), friction cone + complementarity (6.3), integrators + stability bound (6.4), differentiable-sim gradient definition (6.5), GPU-parallel architecture (6.6), sensor models (8.1-8.5), fusion math (8.7).

9. **Replace template Research-Frontier callouts with named papers + one precise open question per chapter.** Ch4: 6D rotation continuity (Zhou et al. 2019), SE(3)-equivariant nets. Ch5: neural IK feasibility guarantees. Ch6: do differentiable-sim gradients help RL (Brax/MJX/Warp debate). Ch7: control barrier functions / runtime assurance. Ch8: invariant EKF for legged robots, factor-graph smoothing (GTSAM), metric-depth foundation models.

10. **De-template the epigraphs and fun-notes.** Replace the 33 formulaic epigraphs with a handful of real per-chapter quotes, and replace the four rotating broken fun-note bodies with topic-specific lines in the style of the genuine 4.1-4.3 fun-notes (which should be preserved verbatim).

## Structure Suggestions for This Part

- **Keep all five chapters and all 36 sections**; the topic decomposition is correct and well-suited to the audience. The fix is content depth, not structure.
- **Promote Chapter 4 sections 4.4-4.7 as the house style template** for rewriting the rest of the part (real theory + runnable code with printed output + topic-specific failure analysis).
- **Consider merging 5.5 (FK) and 5.6 (IK) worked examples onto one shared 2-link arm** so FK-as-oracle-for-IK is demonstrated, not just asserted.
- **Consider merging 8.5 (noise models) and 8.6 (Bayesian filtering)** more tightly, since the filtering section depends on the covariance machinery the noise section is supposed to provide; at minimum cross-link the equations.
- **Move the repeated production block to a single Part II appendix** ("The Robotics Evidence Contract") referenced once, instead of duplicating ~120 lines into all 36 sections.
- **8.8 (Perception as an imperfect window)** is a fine reflective closer; keep it short and do not pad it with the production block.
