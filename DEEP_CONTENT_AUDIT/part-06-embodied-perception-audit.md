# Part 6 Content Audit: Embodied Perception

## Part Overview

Part VI covers the perception layer (Chapters 27 to 30: visual perception for action, 3D and neural scene representations, SLAM, navigation and path planning) across 29 sections. The technical substance is mostly correct and the topic-specific math and code are real: back-projection through intrinsics, log-odds occupancy, stereo disparity, particle weights with effective sample size, differential-drive kinematics, factor-graph weighted least squares, A* admissibility, RRT steering, DWA scoring. The single largest problem is that the part is built from two rigid templates that produce heavy, non-substitutable boilerplate. Chapters 27 and 28 share one template ("Patient Embodied AI Agent" epigraph, identical 5-box SVG "contract" figure in every section, a verbatim "Memory Hook" sentence, and the Reader Pathway / Action Is The Unit Of Meaning callouts). Chapters 29 and 30 share a second, noticeably better template (witty epigraph personas, Problem First / Formal Model / Worked Diagnostic / Tool Workflow, with per-section memory hooks). The result is internally inconsistent across the part, and several passages are pure template fill that fail the non-substitutability rule. Two concrete copy-paste defects exist (literally duplicated paragraphs in 28.1 and 28.5), one boilerplate Big Picture sentence is misapplied (graph-search framing pasted onto a learned-policy section in 30.5), and every chapter ends in the exact "evidence artifact toy lab" the lean contract forbids (`[{"section": s, ...} for s in sections]` filler).

The strongest chapter is 29 (SLAM): real per-section mechanism, good failure taxonomies, current systems named (ORB-SLAM3, RTAB-Map, OpenVINS, Kimera, Cartographer). The weakest is 27: every section uses the same generic contract figure and the identical Memory Hook text, so the chapter reads as one template instantiated seven times.

## Fun Elements to Preserve

Chapters 29 and 30 carry almost all the wit; preserve these:

- **Epigraph personas** (29 and 30 only): "A Loop Closure That Came Back With Receipts" (all of Ch 29) and "A Local Planner With Commitment Issues" (all of Ch 30). These are genuinely funny and topic-true. Keep them.
- **29.3 epigraph**: "A particle filter is a map of competing explanations, not just a pose estimate."
- **29.5 epigraph and memory hook**: "SLAM is memory under cross-examination by geometry."
- **29.2 epigraph**: "Dead reckoning is useful because it admits how fast it is becoming unsure."
- **29.4 epigraph**: "A grid cell is a decision about where the robot may spend risk."
- **29.6 / 29.7 epigraph**: "A map is a promise that every future footstep will ask you to keep."
- **29.8 memory hook**: "SLAM is the robot version of walking into a room and saying, 'I remember this place,' then checking whether the memory improves the next step instead of merely sounding confident."
- **30.7 memory hook**: "A planner that ignores dynamics is a cartographer with excellent handwriting and no driver license." (best line in the part)
- **30.6 epigraph**: "A plan is only smart if the wheels, floor, people, and clock all agree to it."
- **30.4 memory hook**: "Obstacle avoidance is not a path drawing problem; it is a timed command-selection problem."
- **28.5 illustration caption**: "A beautiful render is not a collision certificate." (sharp, keep it)
- **28.6 failure-mode framing**: floaters/holes "render a scene convincingly" but fail contact planning.
- **27.x figure captions**: the dashed-feedback-path idea ("perception quality is judged by action consequences") is a good recurring motif even though the figure itself is over-reused.

Counted distinct fun elements worth preserving: 13.

Note: Chapters 27 and 28 use the bland persona "A Patient Embodied AI Agent" for every epigraph and an identical Memory Hook sentence in every section. This is the opposite of fun and should be diversified, not preserved.

## Chapter-by-Chapter Analysis

### Chapter 27: Visual Perception for Action
**Quality**: NEEDS WORK

Every section instantiates one template: "Patient Embodied AI Agent" epigraph, Big Picture, Reader Pathway, "Problem First: Why This Representation Exists", the SAME 5-box SVG contract figure (Image/State/Action/Safety/Replay relabeled per section), Mathematical Core (one formula), Worked Miniature (tiny NumPy), Library Shortcut, Failure Mode, Practical Example, an IDENTICAL Memory Hook sentence, Debugging, Research Frontier, Self Check, Key Takeaway, Exercise. The topic-specific math/code is correct but minimal, and the framing prose is highly substitutable.

#### Section 27.1: Seeing to classify vs. seeing to act - NEEDS WORK
**Lens 1 (Deep Explanation)**: The expected-utility object `a* = argmax E[U(a,s)|z]` is stated but never derived or connected to where U comes from; no regime-of-validity. The "code" ranks three hard-coded actions with invented weights (`0.8 * safety_margin_m`), so it teaches a made-up scoring rule, not the math above it. Fix: replace the arbitrary linear combination with a worked example tied to the formula, e.g. a 2-action grasp decision where U is expected task reward minus collision-probability cost, and show that the argmax flips when the safety margin crosses the gripper clearance.
**Lens 2 (Research Frontier)**: Research Frontier callout is generic ("recognition whose uncertainty, timing, and geometry are usable by action policies") with no paper and no precise open problem. Fix: name a concrete result (e.g. closed-loop benchmarks where foundation-model features improve success only after calibration) and state one open question precisely.
**Lens 3 (Fun/Engagement)**: Present: epigraph "A class label is useful only after it changes the robot's next safe action" (good). Memory Hook is the generic shared sentence (cut/replace). Missed: the cup-knocking hook from the chapter card never reappears in the section.
**Lens 4 (Examples/Analogies)**: Warehouse-arm example is decent but generic; no real-system anchor (Boston Dynamics, Waymo).
**Lens 5 (Teaching Flow)**: Reader Pathway callout is boilerplate. No "What's Next" linking to 27.2 (Ch 27 sections lack the What's Next that Ch 29/30 have).

#### Section 27.2: Detection, segmentation, and the Segment Anything family - GOOD
**Lens 1**: The action score `q_act = IoU * p_track * 1[clearance>eps]` is a genuinely useful, topic-specific construct and the code matches it (the safety gate zeroes a high-IoU mask). This is the best worked example in the chapter.
**Lens 2**: SAM 2 cited with streaming-memory context and arXiv link (current, 2024). PASS, though the open problem ("calibrated, persistent, safety-aware action regions") could be sharper.
**Lens 3**: Epigraph good. Memory Hook is the shared generic sentence (replace). Missed opportunity: a surprising fact about SAM 2 video memory drift would land well here.
**Lens 4**: PASS. Box/mask/track three-way distinction is concrete.
**Lens 5**: PASS within the section; still no What's Next.

#### Section 27.3: Depth estimation and metric scale - GOOD
**Lens 1**: Pinhole back-projection plus stereo `z = fB/d` is correct, and the text correctly flags small-disparity error amplification. Worked code back-projects one pixel correctly. PASS.
**Lens 2**: Frontier note ("certifying when depth is good enough for contact") is a real open problem but unsourced for the 2024-2026 monocular-depth wave (Depth Anything v2, Metric3D, UniDepth not mentioned). Fix: cite a current metric-depth model and state the calibration-of-scale open problem.
**Lens 3**: Epigraph good. Drone-landing example adds variety. Memory Hook generic (replace).
**Lens 4**: PASS, transparent-cup / glossy-table failure list is concrete.
**Lens 5**: PASS.

#### Section 27.4: Optical flow and motion cues - GOOD
**Lens 1**: Brightness-constancy `I_x u + I_y v + I_t = 0` plus time-to-contact `tau ~ theta/theta_dot` is correct. The code estimates tau from bounding-box growth (topic-true, runnable). PASS.
**Lens 2**: "Recent video foundation models make long-range tracking easier" is vague. Fix: name a tracker (e.g. CoTracker, RAFT successors) and give the closed-loop low-latency open problem precisely.
**Lens 3**: Epigraph good. Memory Hook generic (replace).
**Lens 4**: PASS, ego-motion-vs-object-motion separation is the right intuition.
**Lens 5**: PASS.

#### Section 27.5: Affordances and graspable regions - GOOD
**Lens 1**: `A(r,a) = P(success | phi(r), a, theta_robot)` and `a* = argmax A - lambda C(a)` is a solid affordance formalization; the code subtracts reach/collision cost and the winning index changes accordingly. PASS.
**Lens 2**: Frontier note (open-vocabulary, language-conditioned, 3D contact-aware) is current in spirit but cites no paper. Fix: anchor to a 2024-2026 affordance/grasp result and state the kinematics-feasibility open problem.
**Lens 3**: Epigraph "An affordance is a possibility, not a permission slip" (good, reused in warning). Memory Hook generic (replace).
**Lens 4**: PASS, dishwasher-loading example is concrete.
**Lens 5**: PASS.

#### Section 27.6: Active and embodied perception - GOOD
**Lens 1**: Information-gain objective `argmax E[H(b_t)-H(b_{t+1})|a] - lambda c(a)` is correct and the next-best-view code matches it, including an "act now" option. The "active perception can become procrastination" failure mode is a real, well-stated trap. PASS.
**Lens 2**: Frontier note (pricing information when sensing disturbs the world) is a genuinely good open problem, but no citation. Fix: add a reference and one named benchmark.
**Lens 3**: Epigraph "Active perception spends action to buy information, so the price must be visible" (good). Memory Hook generic (replace). This is the section where humor about a robot dithering forever would be memorable.
**Lens 4**: PASS, humanoid-shelf example concrete.
**Lens 5**: PASS.

#### Section 27.7: When perception failures become action failures - GOOD
**Lens 1**: The failure indicator `fail = 1[d>eps] OR 1[dt>dt_max] OR 1[Sigma not subset Sigma_allowed]` cleanly separates magnitude, latency, and uncertainty-interface errors, and the code emits distinct labels. The "worst failure label is `bad vision`" point is excellent teaching. PASS.
**Lens 2**: Frontier note (failure attribution as stacks absorb foundation models) is apt; add one reference.
**Lens 3**: Epigraph good. Memory Hook generic (replace). The autonomous-vehicle late-brake example is the strongest in the chapter; keep it.
**Lens 4**: PASS, AV braking attribution is a real-system anchor.
**Lens 5**: Good capstone for the chapter, but it just ends; no bridge to Chapter 28.

#### Chapter 27 Lab: Closed-Loop Visual Evidence Panel - NEEDS WORK
The lab is the contract's forbidden "evidence artifact toy lab": it scores three hard-coded actions and writes a `failure_label` string. It is a fifth restatement of the same NumPy ranking snippet from 27.1/27.2/27.5, not a real perception task. Fix: make the lab load a real image, run SAM 2 or a detector, back-project a mask through depth, and produce a clearance decision, so the "panel" actually consumes perception.

### Chapter 28: 3D Perception and Neural Scene Representations
**Quality**: NEEDS WORK

Same template as Ch 27, plus two copy-paste defects. Topic-specific math is a step up (volume rendering weights, Gaussian footprint, inverse-variance fusion, log-odds), which is why several sections rate GOOD, but the framing prose is the most boilerplate-heavy in the part and two sections share verbatim paragraphs with each other.

#### Section 28.1: Why 3D matters for manipulation and navigation - NEEDS WORK
**Lens 1**: DUPLICATED PARAGRAPH BUG: lines 49-50 are the same sentence twice ("3D perception matters only when it changes reachability, clearance, grasp pose, or navigation risk. The action loop should record...") with the second copy just appending "Treat the representation as a typed state estimate, not as a visualization." Fix: delete the duplicate, keep one paragraph. The predicate formula `a allowed iff d(q,O)>eps AND p in R(q) AND support(p)` is good.
**Lens 2**: No frontier callout visible in the opening; generic.
**Lens 3**: Epigraph is a long declarative sentence ("geometry earns its place when it changes reachability...") not a quotable line; weaker than Ch 29/30 epigraphs.
**Lens 4**: Figure 28.1A caption ("3D matters because bodies need places to fit") is good. The generic 5-box SVG is reused.
**Lens 5**: Opener should motivate the whole chapter; instead it is the same per-section template.

#### Section 28.2: Point clouds and depth maps - GOOD
**Lens 1**: `P_c = z K^-1 [u,v,1]^T`, `P_w = T_wc P_c` correct; the 2x2 back-projection loop is right. PASS. Minor: `cx = cy = 0.5` is an odd principal point for a real camera (suggests a normalized convention not stated); worth a one-line note.
**Lens 2**: No paper; Open3D doc only. Fine for a how-to section but add one reconstruction reference.
**Lens 3**: "A point cloud is a sample, not a solid object" is a good aha; keep. Memory Hook generic (replace).
**Lens 4**: PASS, bin-picking crop-around-grasp example concrete.
**Lens 5**: PASS.

#### Section 28.3: 3D detection and scene reconstruction - GOOD
**Lens 1**: Object-state tuple and inverse-variance fusion `fused = (wa*a + wb*b)/(wa+wb)` is correct and the right intuition (reconstruction as evidence fusion). PASS.
**Lens 2**: No current 3D-detection reference (e.g. no mention of transformer 3D detectors or open-vocab 3D). Fix: add one and a precise multi-view consistency open problem.
**Lens 3**: Forklift pallet-identity example is good and concrete.
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 28.4: Occupancy grids and voxel maps - GOOD
**Lens 1**: Log-odds update `l_t = l_{t-1} + log(p/(1-p)) - l_0` correct; code shows free cells dropping, hit cell rising, unknown staying 0.5. The "unknown is not free" point is well made. PASS.
**Lens 2**: OctoMap/OpenVDB named; frontier note (occupancy plus neural priors vs real-time guarantees) is real. Add a citation.
**Lens 3**: Memory Hook generic (replace).
**Lens 4**: PASS, warehouse-drone inflation example concrete.
**Lens 5**: PASS.

#### Section 28.5: NeRF: implicit radiance fields - NEEDS WORK
**Lens 1**: DUPLICATED PARAGRAPH BUG: lines 49-50 repeat "For NeRF-style fields, the action contract must include camera poses, scale recovery, rendering latency..." twice. Fix: delete the duplicate. Otherwise the volume-rendering integral and the discrete `alpha = 1 - exp(-sigma*delta)`, transmittance cumprod, weights code are correct and well explained. The NeRF math itself is EXCELLENT.
**Lens 2**: Mildenhall 2020 cited (foundational) but no 2024-2026 robotics-NeRF work (e.g. instant-NGP successors, NeRF-for-manipulation). Caption "A beautiful render is not a collision certificate" is the right framing. Fix: add a current reference and state the updateable/metric/conservative open problem precisely.
**Lens 3**: Epigraph is the long-sentence style; the illustration caption is the real gem. Memory Hook generic (replace).
**Lens 4**: PASS, real-estate inspection example concrete.
**Lens 5**: PASS aside from the duplicate paragraph.

#### Section 28.6: 3D Gaussian Splatting: explicit, editable, real-time - GOOD
**Lens 1**: Splat tuple `(mu, Sigma, alpha, theta)` and projected footprint weight correct; 2D footprint code right. PASS. Reader Pathway and the "A static computer-vision system can stop when it names an object..." Problem First paragraph are verbatim generic boilerplate (also appears in 28.7).
**Lens 2**: Kerbl 2023, Nerfstudio Splatfacto, gsplat all cited and current. PASS. Frontier note (dynamic, object-aware, planning-compatible splats) is current and good.
**Lens 3**: Floaters/holes failure framing is memorable. Memory Hook generic (replace).
**Lens 4**: PASS, teleop-view-plus-conservative-collision-layer example is a real pattern.
**Lens 5**: PASS.

#### Section 28.7: Scene representations for robotics: SLAM, real2sim, manipulation - GOOD
**Lens 1**: The query-function map `M = {q_pose, q_free, q_contact, q_object, q_render}` is a genuinely good organizing idea (route each query to the representation that can answer it safely). PASS. But Problem First and Key Insight paragraphs are byte-identical to 28.6 (shared boilerplate).
**Lens 2**: No frontier callout in the portion reviewed; the section is mostly a synthesis, which is fine, but it should name 2024-2026 scene-graph/real2sim systems.
**Lens 3**: Good synthesis chapter-closer concept.
**Lens 4**: PASS, the routing table is concrete.
**Lens 5**: Good capstone for Ch 28.

#### Chapter 28 Lab: Scene-Representation Query Router - GOOD (best lab in the part)
This lab is actually topic-specific and useful: it routes localize/avoid/grasp/render/real2sim queries to representations with matching safety semantics, and the central lesson (collision uses conservative geometry, rendering uses NeRF/splats) is real. Keep this lab as the model; rewrite the Ch 27/29/30 labs to its standard.

### Chapter 29: Localization and Mapping (SLAM)
**Quality**: GOOD (strongest chapter in the part)

Different, better template: witty epigraph persona, Problem First / Formal Model / Worked Diagnostic / Tool Workflow, per-section memory hooks, What's Next bridges, current systems named. Topic-specific math is real and correct throughout. The one recurring defect is a verbatim Big Picture sentence ("is the state-estimation half of embodied autonomy. The robot has partial, noisy, time-stamped evidence...") pasted into 29.1, 29.3, 29.4, 29.5, 29.6, 29.7, 29.8.

#### Section 29.1: Where am I and what does the world look like - GOOD
**Lens 1**: Full SLAM posterior factorization `p(x_{0:T},m|z,u) prop p(x_0) prod p(x_t|x_{t-1},u_t) prod p(z_t|x_t,m)` stated correctly; landmark-innovation code is a real smoke test. PASS.
**Lens 2**: Durrant-Whyte/Bailey and GTSAM cited; frontier (geometry+semantics+neural) current. PASS.
**Lens 3**: Epigraph and "A pose estimate is a contract between memory, sensors, and the next motion command" memory hook (good).
**Lens 4**: PASS, warehouse replay-bundle example concrete.
**Lens 5**: PASS, has What's Next. Fix: vary the duplicated Big Picture sentence.

#### Section 29.2: Odometry and dead reckoning - GOOD
**Lens 1**: Differential-drive update equations correct; the d_left/d_right mismatch code shows compounding heading error. PASS. Covariance-growth point made.
**Lens 2**: Adequate; could name a modern VIO (e.g. OpenVINS appears later in 29.8).
**Lens 3**: Epigraph "Dead reckoning is useful because it admits how fast it is becoming unsure" (excellent).
**Lens 4**: PASS.
**Lens 5**: PASS.

#### Section 29.3: Localization (Monte Carlo / particle filters) - GOOD
**Lens 1**: Particle weight update and mean estimate stated; code computes normalized weights AND effective sample size `1/sum(w^2)` (excellent, the right diagnostic). The corridor-aliasing motivation is exactly right. PASS.
**Lens 2**: Nav2 AMCL named; frontier (robust global localization under aliasing, semantic particle filters) current and precise.
**Lens 3**: Epigraph/memory hook "a map of competing explanations" (excellent).
**Lens 4**: PASS.
**Lens 5**: PASS. Fix: duplicated Big Picture sentence.

#### Section 29.4: Mapping and occupancy grids - GOOD
**Lens 1**: Log-odds map update correct; sigmoid code shows belief evolving across rays. PASS.
**Lens 2**: Adequate.
**Lens 3**: Epigraph "A grid cell is a decision about where the robot may spend risk" (good).
**Lens 4**: PASS.
**Lens 5**: PASS. Fix: duplicated Big Picture sentence.

#### Section 29.5: SLAM: graph-based and visual SLAM - GOOD
**Lens 1**: Nonlinear least-squares `x* = argmin sum ||r_k||^2_Omega` correct; the weighted-residual code demonstrates why one bad loop closure dominates the objective (the key robust-SLAM insight). PASS.
**Lens 2**: GTSAM, Ceres, ORB-SLAM3, RTAB-Map, Kimera named; frontier (robust data association at scale) current and precise. PASS.
**Lens 3**: Epigraph/memory hook "SLAM is memory under cross-examination by geometry" (excellent).
**Lens 4**: PASS.
**Lens 5**: PASS. Fix: duplicated Big Picture sentence.

#### Section 29.6: Neural and Gaussian-splat SLAM - GOOD
**Lens 1**: Photometric bundle-adjustment objective `min sum rho(I_t(p) - I_hat(p;x_t,theta)) + lambda R(theta)` correct; the action-gate code (PSNR AND pose RMSE AND unknown-fraction) is a good multi-gate idea. PASS.
**Lens 2**: Frontier (auditable learned signals when the robot fails) is a real open problem. Add a 2024-2026 neural-SLAM citation (e.g. SplaTAM, GS-SLAM, MonoGS) since the section is specifically about this frontier.
**Lens 3**: Epigraph good. Uses the block-diagram SVG (different from the per-section reuse in Ch 27/28).
**Lens 4**: PASS.
**Lens 5**: PASS. Fix: duplicated Big Picture sentence.

#### Section 29.7: Map uncertainty - GOOD
**Lens 1**: Cell entropy and entropy-augmented planning cost `J(pi) = C(pi) + beta sum H(c)` correct; entropy-cost code right. The "uncertainty is an input to action, not a final error bar" framing is excellent. PASS.
**Lens 2**: Adequate.
**Lens 3**: Epigraph good. Memory Hook should be section-specific (currently shares the "map is a promise" epigraph line).
**Lens 4**: PASS.
**Lens 5**: PASS. Fix: duplicated Big Picture sentence.

#### Section 29.8: Modern SLAM systems and failure modes - GOOD
**Lens 1**: The systems tuple `(sensors, calibration, front end, back end, map, consumer, replay)` and the front-end/back-end/latency failure classifier code are practitioner-grade. PASS. The "Formal Model" header over a tuple-as-equation is a slight stretch but acceptable.
**Lens 2**: ORB-SLAM3, RTAB-Map, OpenVINS, Kimera, Cartographer, GTSAM, Ceres, Nav2 all named with selection criteria (sensor suite, latency, license). PASS, current and concrete.
**Lens 3**: Best memory hook in the chapter (walking into a room). Keep.
**Lens 4**: PASS, warehouse one-replay-bundle example concrete.
**Lens 5**: Good chapter capstone.

#### Chapter 29 Lab: SLAM Evidence Panel - NEEDS WORK
Forbidden toy lab: `manifest = [{"section": s, "metric": "closed_loop_success", "perturbation": "occlusion_or_noise"} for s in sections]`. This is exactly the `[skill for skill in skills]` filler the contract bans. Fix: replace with a runnable MCL or pose-graph episode on a small synthetic map that actually produces convergence-time and wrong-mode numbers.

### Chapter 30: Navigation and Path Planning
**Quality**: GOOD

Mirrors Ch 29's better template with good topic-specific code (A* f=g+h ranking, RRT steering, DWA velocity scoring, learned-vs-classical panel with interventions, degraded-mode policy). Recurring defect: a Big Picture sentence "turns maps and goals into constrained motion. The planner is not searching for a pretty line..." pasted across 30.1, 30.5, 30.6, 30.7, and in 30.5 it is misapplied (a learned policy does not "turn maps and goals into constrained motion" in the search sense).

#### Section 30.1: Navigation as embodied intelligence - GOOD
**Lens 1**: Constrained-optimization form `pi* = argmin sum c(x_t,u_t) s.t. x_{t+1}=f(x_t,u_t), x_t in X_free` correct; the execution-aware run-scoring code (path length plus clearance penalty plus recovery count) is a real planning-audit idea. PASS.
**Lens 2**: Adequate opener.
**Lens 3**: Epigraph "Navigation intelligence is measured in executed motion, recovery behavior, and auditable uncertainty" (good). "A wish drawn on a map" line is memorable.
**Lens 4**: PASS.
**Lens 5**: PASS, has What's Next.

#### Section 30.2: Graph search: BFS, Dijkstra, A* - GOOD
**Lens 1**: `f(n)=g(n)+h(n)`, admissibility `0<=h<=h*` correct; the frontier-ranking code shows B expanding first on lowest f and notes tie-breaking effect. Consistency vs admissibility distinction is made. PASS. This is graduate-correct.
**Lens 2**: LaValle, OMPL, Nav2 cited; frontier (dynamic graph search, learned admissible heuristics, multi-resolution) current.
**Lens 3**: Epigraph/memory hook "a contract between the map discretization and the motion the robot can actually execute" (good).
**Lens 4**: PASS. Integration Checklist (freeze resolution, inflation, heuristic, tie-breaking) is a strong practitioner touch.
**Lens 5**: PASS.

#### Section 30.3: Sampling-based planning: RRT, RRT*, PRM - GOOD
**Lens 1**: One RRT steering step with `eta`-bounded extension correct; the "intermediate state is the one that gets collision-checked" point is the right teaching. PASS. Missing: RRT* rewiring / asymptotic optimality is mentioned in the title but not in the math; add one line on the near-radius rewire.
**Lens 2**: OMPL, MoveIt, Nav2 cited; frontier (learned sampling, neural collision checking, kinodynamic) current.
**Lens 3**: Memory hook good.
**Lens 4**: PASS, narrow-passage failure mode concrete.
**Lens 5**: PASS.

#### Section 30.4: Local planning and obstacle avoidance (DWA, potential fields) - GOOD
**Lens 1**: Velocity-candidate scoring code (goal progress, clearance penalty `1.5/clearance`, speed penalty) demonstrates choosing the slower command near hazards. PASS. Could state the DWA dynamic-window admissible-velocity set formally; currently the formal model is light.
**Lens 2**: Nav2 controllers (MPPI, Regulated Pure Pursuit, DWB) named; frontier (risk-aware MPC, social nav, learned traversability, GPU rollout) current. PASS.
**Lens 3**: "Obstacle avoidance is not a path drawing problem; it is a timed command-selection problem" (excellent).
**Lens 4**: PASS, pedestrian/doorway examples concrete.
**Lens 5**: PASS.

#### Section 30.5: Learned navigation policies - GOOD
**Lens 1**: Policy `pi_theta(a_t|o_{<=t},g)` and return objective correct; the learned-vs-classical panel that penalizes interventions (`success - 0.5*interventions`, learned policy loses despite higher raw success) is a genuinely good evaluation lesson and directly enacts the book's construct-matched-metrics discipline. PASS.
**Lens 2**: Habitat, RoboTHOR, AI2-THOR, Isaac Lab named; frontier (VLN, foundation-model affordance maps, offline nav datasets, distillation into monitored controllers) current. PASS.
**Lens 3**: Epigraph/memory hook "embodied when the policy can recover from the world changing under it" (good).
**Lens 4**: PASS, A_star_plus_DWB baseline is a real comparator.
**Lens 5**: Fix: the Big Picture sentence is the graph-search boilerplate ("turns maps and goals into constrained motion. The planner is not searching for a pretty line"), which is wrong for a learned policy. Rewrite to a policy-specific opener.

#### Section 30.6: Language- and image-goal navigation - GOOD
**Lens 1**: Goal grounding `g* = argmax p(g|language,image,m)` then `pi* = argmin C(pi,g*)` correct; semantic-candidate ranking code (match minus travel cost) is topic-true. The "plan to a viewpoint that can verify the goal" point is good. PASS.
**Lens 2**: Frontier coverage thin for a 2024-2026 topic. Fix: name current VLN/image-goal work (e.g. instruction-following nav, CLIP-on-Wheels-style grounding, image-goal benchmarks) and cite at least one paper; this section currently leans on the same LaValle/OMPL/Nav2 trio that does not cover language grounding.
**Lens 3**: "Find the red mug is not a coordinate" is a good concrete hook.
**Lens 4**: PASS, kitchen/desk/shelf grounding example concrete.
**Lens 5**: Fix: Big Picture is again the graph-search boilerplate; rewrite for goal grounding.

#### Section 30.7: Field navigation under degraded sensing - GOOD
**Lens 1**: Safe-control-set form `u_t in U_safe(b_t)` with belief over hazards correct; degraded-mode policy code (localization, costmap age, clearance, first-violated-bound) is practitioner-grade. PASS.
**Lens 2**: Frontier (multimodal sensing, runtime monitors, fleet-level failure mining, explainable degraded-mode) current and precise. PASS.
**Lens 3**: "A planner that ignores dynamics is a cartographer with excellent handwriting and no driver license" (best line in the part).
**Lens 4**: PASS, delivery-robot log fields concrete; dust/darkness/GPS-denial/glass list is real field experience.
**Lens 5**: Good chapter capstone. Fix: Big Picture boilerplate.

#### Chapter 30 Lab: Navigation Evidence Panel - NEEDS WORK
Same forbidden toy lab as Ch 29 (`manifest = [... for s in sections]`). Fix: replace with a runnable A*-on-a-grid plus DWA-tracking episode that produces real path-cost, clearance, and recovery numbers.

## Cross-Chapter Issues in This Part

1. **Two incompatible templates.** Ch 27-28 use one skeleton (Patient Embodied AI Agent epigraph, identical 5-box SVG contract figure per section, generic Reader Pathway + Action Is The Unit Of Meaning callouts, identical Memory Hook sentence). Ch 29-30 use a better skeleton (persona epigraphs, Problem First / Formal Model / Worked Diagnostic / Tool Workflow, per-section hooks, What's Next). Unify on the Ch 29-30 template; it is strictly better.

2. **Identical "Memory Hook" sentence in every Ch 27 and Ch 28 section.** Verbatim: "For [topic], the perception result must answer what action changed, what uncertainty changed, and what log would reproduce the decision. Otherwise the output is still visualization, not embodied evidence." Swapping the topic name leaves it unchanged: textbook non-substitutable boilerplate. Replace each with a section-specific witty hook (Ch 29-30 already do this well).

3. **The 5-box SVG "contract" figure is reused in all 14 Ch 27-28 sections** with only the box labels changed. It carries little per-topic information. Either make each figure topic-specific or demote it.

4. **Two literal duplicated paragraphs** (28.1 lines 49-50, 28.5 lines 49-50) and **two sections sharing verbatim Problem First / Key Insight paragraphs** (28.6 and 28.7). Copy-paste defects to fix.

5. **Recurring duplicated Big Picture sentences within Ch 29 and within Ch 30**, with one outright misapplication in 30.5 (graph-search framing on a learned policy).

6. **Every chapter lab except Chapter 28's is the forbidden "evidence artifact toy lab"** with `[{...} for s in sections]` filler. The contract names this exact anti-pattern. Chapter 28's query-router lab is the model to copy.

7. **Research grounding is uneven.** Ch 29-30 name real, current systems and benchmarks. Ch 27-28 frontier callouts are mostly generic ("foundation models are improving fast") with few papers and vague open problems; the 2024-2026 monocular-depth, video-tracking, neural-SLAM, and VLN waves are under-cited.

8. **No "What's Next" in Ch 27 and Ch 28 sections**, while Ch 29-30 sections have them. Add bridges to Ch 27-28.

9. **Real-system anchors thin in Ch 27-28.** The brief names Boston Dynamics / Waymo / NVIDIA / DeepMind audience; warehouse-arm and drone examples are generic. The AV-late-brake (27.7) and forklift (28.3) examples show the right level; extend that to other sections.

## Top 10 Highest-Priority Fixes for This Part

1. **Replace the identical Memory Hook in all 14 Ch 27-28 sections** (`part-6-embodied-perception/module-27-*/section-27.*.html`, `module-28-*/section-28.*.html`) with section-specific hooks in the Ch 29-30 style. Example for 27.3: "Depth in pixels lies politely; depth in meters is the one that breaks fingers." For 27.6: "A robot that keeps looking to be sure is a robot that never arrives."

2. **Fix the two duplicated paragraphs.** In `module-28-*/section-28.1.html` delete the repeated "3D perception matters only when it changes reachability..." paragraph (lines 49-50). In `module-28-*/section-28.5.html` delete the repeated "For NeRF-style fields, the action contract must include..." paragraph (lines 49-50).

3. **Rewrite the Ch 27, 29, 30 labs** to remove the `[{"section": s, ...} for s in sections]` filler. Model them on Chapter 28's query-router lab. Ch 27 lab: run a detector/SAM mask, back-project through depth, output a clearance decision. Ch 29 lab: a runnable MCL episode on a synthetic aliased map yielding convergence-time and wrong-mode numbers. Ch 30 lab: A*-on-grid + DWA tracking yielding path-cost, clearance, recovery counts.

4. **Fix the misapplied Big Picture sentence in 30.5** (`module-30-*/section-30.5.html`). Replace "Learned navigation policies turns maps and goals into constrained motion. The planner is not searching for a pretty line..." with a policy-specific opener about mapping observations to actions and the generalization risk.

5. **Diversify Ch 27-28 epigraph personas.** "A Patient Embodied AI Agent" is used for all 14 epigraphs and both indexes. Give Ch 27 and Ch 28 their own persona voices in the Ch 29-30 style (e.g. "A Camera That Learned to Distrust Itself", "A Point Cloud With Trust Issues").

6. **De-duplicate the recurring Big Picture sentence across Ch 29 sections** ("is the state-estimation half of embodied autonomy...") in 29.1/29.3/29.4/29.5/29.6/29.7/29.8, and the Ch 30 sentence across 30.1/30.5/30.6/30.7. Write one per section.

7. **Add current (2024-2026) research grounding to Ch 27-28 frontier callouts.** 27.3: a metric monocular-depth model and the scale-calibration open problem. 27.4: a current point tracker. 28.5/29.6: a current neural/Gaussian-SLAM system (SplaTAM / MonoGS / GS-SLAM class). 30.6: a current VLN / image-goal benchmark and paper.

8. **Add "What's Next" bridges to all Ch 27 and Ch 28 sections** matching the Ch 29-30 pattern, and end 27.7 and 28.7 with a bridge into the next chapter.

9. **Make the 5-box SVG contract figure topic-specific or demote it** across Ch 27-28. At minimum, give each figure one topic-unique element so it is not pure relabeling.

10. **Add real-system anchors to generic Ch 27-28 sections.** Extend the AV-braking (27.7) and forklift (28.3) quality to 27.5 (a named grasp system), 28.4 (a real drone occupancy stack), 28.6 (a deployed teleop-splat workflow).

## Structure Suggestions for This Part

- **The part index lists 6 sections for Chapter 30 and 7 for Chapter 29, but disk has 7 (30.1-30.7) and 8 (29.1-29.8).** Sections 29.8 (Modern SLAM systems and failure modes) and 30.7 (Field navigation under degraded sensing) exist as files and are strong, but are NOT linked from the part index (`part-6-embodied-perception/index.html`). Add them to the part-index chapter cards. (The chapter indexes do list them.)
- **Keep all 29 sections; none should be dropped.** The topic coverage is complete and well sequenced (perception-for-action -> 3D/neural -> SLAM -> navigation).
- **Consider merging 28.5 (NeRF) and 28.6 (3DGS) framing prose** is NOT advised; they are distinct enough. But their shared boilerplate Problem First paragraphs should be made distinct rather than merged.
- **27.7 and 28.7 and 29.8 and 30.7 are all "failure modes / systems" capstones.** This is a good, deliberate pattern; keep it, but ensure each names different, topic-specific failure taxonomies (currently 27.7 and 29.8 do this well; 28.7 leans on synthesis).
- **Chapter 28's query-router lab should be promoted to a part-level pattern** referenced by the other chapter labs.

Structure suggestions count: 5.
