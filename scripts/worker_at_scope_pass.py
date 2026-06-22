from pathlib import Path


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


SECTIONS = {
    "58.1": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.1.html",
        "topic": "Scaling laws and data engines for robots",
        "bridge": "A robot scaling claim matters only if extra data changes closed-loop behavior on new embodiments, new scenes, or longer horizons. The practical problem is that robot datasets differ in embodiment, sensor stack, action rate, and intervention policy, so a bigger corpus can look impressive while still teaching the policy the wrong invariances.",
        "problem": "Treat the data engine as the real object of study: which states are sampled, which failures are collected, and how new data is prioritized after deployment. This section therefore moves from headline scaling claims to the artifact that a lab can actually build, namely a collection, filtering, labeling, and replay loop tied to a fixed evaluation panel.",
        "formula": r"Let $D=\{(o_t,a_t,r_t,m_t)\}_{t=1}^N$ be a robot dataset with metadata $m_t$ for embodiment, task, and intervention source. A useful scaling view is $\mathcal{E}(N,H,B)=\mathbb{E}_{(e,h,b)\sim p_{\text{eval}}}[\ell(\pi_\theta; e,h,b)]$, where $H$ is horizon, $B$ is embodiment family, and the evaluation loss is measured on a fixed panel rather than on a moving benchmark.",
        "intuition": "The key term is the panel distribution $p_{eval}$. If you silently change the evaluated horizons or embodiments while increasing $N$, you are no longer measuring scaling, you are measuring a different task. The section therefore asks for growth curves indexed by data count, intervention count, and embodiment coverage at the same time.",
        "algorithm_title": "Algorithm: Build a robot data engine rather than a static dataset",
        "algorithm_steps": [
            "Start from a fixed benchmark panel with nominal, perturbation, and rare-failure scenes.",
            "Collect demonstrations, teleoperation traces, and autonomous rollouts with metadata for embodiment, camera setup, and controller rate.",
            "Mine failures and near-failures into a priority queue instead of sampling only successful trajectories.",
            "Retrain or fine-tune the policy, then re-evaluate on the unchanged panel with the same metric script.",
            "Promote new data only if it improves panel coverage or reduces a named failure cluster."
        ],
        "table_title": "Data-Engine Design Questions",
        "table_rows": [
            ("Data source", "Teleoperation, scripted policies, fleet logs, or synthetic augmentation", "It determines covariate shift and label quality."),
            ("Coverage axis", "Task family, embodiment family, horizon length, or perturbation family", "It prevents a single aggregate curve from hiding blind spots."),
            ("Refresh trigger", "Failure cluster, low-confidence state, or new hardware deployment", "It turns data collection into an active systems process."),
            ("Evidence artifact", "Scaling curve plus panel manifest and failure taxonomy", "It makes the claim reproducible across labs."),
        ],
        "code": """# Evidence schema for a robot data-engine experiment.\nartifact = {\n    \"panel\": \"kitchen-v2-fixed-panel\",\n    \"data_hours\": [50, 100, 200],\n    \"embodiments\": [\"widowx\", \"aloha\", \"mobile-manipulator\"],\n    \"metrics\": [\"success_rate\", \"interventions_per_hour\", \"rare_failure_recall\"],\n    \"refresh_trigger\": \"new failure cluster: mug-handle occlusion\",\n}\nprint(artifact)""",
        "output": "{'panel': 'kitchen-v2-fixed-panel', 'data_hours': [50, 100, 200], 'embodiments': ['widowx', 'aloha', 'mobile-manipulator'], 'metrics': ['success_rate', 'interventions_per_hour', 'rare_failure_recall'], 'refresh_trigger': 'new failure cluster: mug-handle occlusion'}",
        "output_interp": "The expected output is not a trained model. It is an experiment card that fixes the panel, names the data scales, and records why more data is being collected. A reader should reject any scaling plot that cannot be traced back to this kind of card.",
        "tools": "LeRobot, Open X-Embodiment, DROID, robomimic, Weights &amp; Biases, Hugging Face datasets",
        "practical": "A strong semester project uses a small tabletop benchmark with one intentionally difficult perturbation, such as specular objects or camera offset, then shows how targeted data refresh improves the perturbation without regressing the nominal cases. That is a better research artifact than a single average success number reported after a large unstructured data scrape.",
        "frontier": "The frontier question is whether robot scaling laws can be made conditional: how much extra data is needed for a new embodiment, a longer horizon, or a new sensor package? A convincing answer will likely combine foundation-policy pretraining with active failure mining and better panel design, not just a larger generic corpus.",
        "xref": '<a href="../../part-5-imitation-learning-datasets-and-policy-learning/module-24-robot-datasets-and-data-quality/index.html">Chapter 24 on robot datasets</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html">Chapter 52 on evaluation</a>',
    },
    "58.2": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.2.html",
        "topic": "Generalist vs. specialist policies",
        "bridge": "The generalist-specialist question appears every time a team chooses between one policy that covers many tasks and several policies that optimize one niche. The hard part is that the tradeoff is not abstract: it shows up as latency, calibration, recoverability, and deployment complexity in the robot loop.",
        "problem": "A useful comparison therefore needs a routing rule and a budget, not just two model names. This section asks when shared representations improve transfer and when narrow policies remain the better engineering choice because they are easier to certify, debug, or constrain.",
        "formula": r"Suppose a router chooses among policies $\pi_1,\dots,\pi_K$ and a generalist $\pi_g$. The operational objective is $\min_{\rho,\Pi}\; \mathbb{E}[\ell(\rho(o_t),\Pi,o_t)] + \lambda\,\text{latency} + \mu\,\text{ops\_cost}$, where $\rho$ may route to a specialist or keep the request inside the generalist policy.",
        "intuition": "The extra terms matter because a slightly stronger specialist that doubles maintenance cost or introduces brittle routing may lose in practice. Likewise, a generalist that avoids router errors can win even when its peak precision on one microtask is lower.",
        "algorithm_title": "Algorithm: Compare policy families under one deployment contract",
        "algorithm_steps": [
            "Define the task mix, latency limit, and safety envelope for deployment.",
            "Measure one generalist policy and one specialist baseline per task on the same panel.",
            "Add a router only if the generalist misses the latency or precision target on named tasks.",
            "Audit failure attribution: model error, router error, stale calibration, or controller mismatch.",
            "Choose the smallest policy set that meets the system contract."
        ],
        "table_title": "When Each Policy Family Wins",
        "table_rows": [
            ("Generalist policy", "Shared representation, multi-task coverage, fewer deployment artifacts", "Cross-task transfer and simpler orchestration."),
            ("Specialist policy", "Narrow task contract, tighter latency, easier certification", "Precision workloads and regulated settings."),
            ("Hybrid router", "One generalist front end plus specialist fallbacks", "Useful when only a few tasks need special treatment."),
            ("Evidence artifact", "Task-by-task matrix plus router-confusion report", "Shows whether the added complexity is paying off."),
        ],
        "code": """# Compare one generalist and two specialists under a shared contract.\nresults = {\n    \"task_mix\": [\"drawer-open\", \"mug-pick\", \"switch-toggle\"],\n    \"generalist_success\": 0.79,\n    \"specialist_mean_success\": 0.84,\n    \"router_error_rate\": 0.11,\n    \"latency_ms\": {\"generalist\": 84, \"specialists\": 41, \"hybrid\": 68},\n}\nprint(results)""",
        "output": "{'task_mix': ['drawer-open', 'mug-pick', 'switch-toggle'], 'generalist_success': 0.79, 'specialist_mean_success': 0.84, 'router_error_rate': 0.11, 'latency_ms': {'generalist': 84, 'specialists': 41, 'hybrid': 68}}",
        "output_interp": "The expected output should force a decision. If the specialist edge is small and router error is nontrivial, the generalist may still be the better system. The interpretation depends on the deployment contract, not on average success alone.",
        "tools": "OpenVLA, GR00T, SmolVLA, PyTorch, Triton inference servers, ROS 2 routing nodes",
        "practical": "A good capstone compares one generalist manipulation policy against two specialist policies for grasping and placement, then measures where the router actually misclassifies state. Students learn quickly that a hybrid system can fail because the wrong policy was selected, even when each policy looks good in isolation.",
        "frontier": "The frontier problem is conditional specialization: can a policy expose specialist skill at test time without fragmenting the deployment stack? Mixture-of-experts for embodied control, retrieval-augmented policy memories, and modular latent skills are all attempts to answer that question.",
        "xref": '<a href="../../part-7-language-vision-and-vision-language-action-models/module-34-vla-models-openvla-pi0-gr00t-and-beyond/index.html">Chapter 34 on VLA models</a> and <a href="../../part-6-skills-world-models-and-3d-representation/module-26-skills-hierarchy-and-task-graphs/index.html">Chapter 26 on skills and hierarchy</a>',
    },
    "58.3": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.3.html",
        "topic": "World models in the robot loop",
        "bridge": "World models promise sample efficiency because the agent can imagine futures before touching hardware. The open problem is that imagination only helps if the latent model stays aligned with the contact dynamics, sensing artifacts, and control delays that matter for the robot's actual decisions.",
        "problem": "The section therefore treats a world model as a decision module, not just a predictive loss. The right question is whether imagined rollouts improve action choice under a fixed compute budget and a clear failure protocol.",
        "formula": r"A latent world model defines $z_{t+1}\sim p_\theta(z_{t+1}\mid z_t,a_t)$ and reward or cost heads $\hat r_t=r_\theta(z_t,a_t)$. Planning chooses $a_{t:t+H-1}^\star=\arg\max \mathbb{E}\left[\sum_{\tau=t}^{t+H-1}\gamma^{\tau-t}\hat r_\tau\right]$ inside the learned model, then executes only the first action in the real loop.",
        "intuition": "The useful intuition is model-predictive control in latent space. The policy is not trusting a fantasy forever; it is repeatedly proposing short-horizon plans, re-observing the world, and correcting the latent state before error compounds too far.",
        "algorithm_title": "Algorithm: Use a world model as a short-horizon planner",
        "algorithm_steps": [
            "Encode the current observation into a latent state with uncertainty if available.",
            "Roll out candidate action sequences inside the latent dynamics for a short horizon.",
            "Score each sequence with task reward, safety cost, and model-uncertainty penalty.",
            "Execute the first action only, then re-encode the real observation and replan.",
            "Log model mismatch whenever real next-state evidence diverges from predicted outcomes."
        ],
        "table_title": "World-Model Failure Tests",
        "table_rows": [
            ("Dynamics mismatch", "Contacts, slip, cable interactions, or unmodeled delay", "The planner becomes overconfident in impossible futures."),
            ("Observation aliasing", "Two latent states explain the same camera view", "Planning commits to the wrong hidden state."),
            ("Long horizon", "Predictions drift after several imagined steps", "A short MPC horizon becomes necessary."),
            ("Evidence artifact", "Prediction-vs-reality replay with uncertainty and intervention labels", "This reveals whether the planner helps or hallucinates."),
        ],
        "code": """# Short-horizon world-model planning card.\ncard = {\n    \"latent_horizon\": 8,\n    \"objective\": [\"task_reward\", \"safety_cost\", \"uncertainty_penalty\"],\n    \"replan_every_steps\": 1,\n    \"drift_metric\": \"latent rollout error at horizon 4 and 8\",\n}\nprint(card)""",
        "output": "{'latent_horizon': 8, 'objective': ['task_reward', 'safety_cost', 'uncertainty_penalty'], 'replan_every_steps': 1, 'drift_metric': 'latent rollout error at horizon 4 and 8'}",
        "output_interp": "The expected output should read like a planner contract. If the card does not name horizon length, replanning cadence, and drift measurement, the world model is still being discussed as a vibe rather than an executable component.",
        "tools": "DreamerV3, TD-MPC2, mbrl-lib, MuJoCo, Isaac Lab, JAX or PyTorch",
        "practical": "In a capstone, students can keep the control problem simple, such as pushing an object to a goal, then compare a model-free baseline against a world-model planner under limited interaction budget. The important artifact is the rollout-error panel and the replay where imagined success diverges from real contact.",
        "frontier": "The frontier is not just better video prediction. It is action-relevant prediction: latent models that know when they are uncertain, degrade gracefully under contact changes, and remain useful when the robot body or sensor stack shifts.",
        "xref": '<a href="../../part-8-world-models-model-based-rl-and-planning/module-38-world-models/index.html">Chapter 38 on world models</a> and <a href="../../part-8-world-models-model-based-rl-and-planning/module-37-model-predictive-control-and-planning/index.html">Chapter 37 on model-predictive planning</a>',
    },
    "58.4": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.4.html",
        "topic": "The open-vs-closed model divide",
        "bridge": "Teams building embodied systems constantly face the open-versus-closed decision: do you rely on a vendor API or a local model stack that you can inspect, tune, and reproduce? The answer affects not only cost and convenience, but also debugging depth, benchmark transparency, safety review, and long-term maintenance.",
        "problem": "This section frames the divide as a systems governance problem. The right model choice is the one whose assumptions, interfaces, and operational risks match the evidence requirements of your project.",
        "formula": r"Let utility be $U = \alpha\,\text{capability} - \beta\,\text{latency} - \chi\,\text{cost} + \delta\,\text{inspectability} + \eta\,\text{reproducibility}$. Open and closed model choices change all five terms, so the decision cannot be reduced to benchmark accuracy alone.",
        "intuition": "A closed model often buys stronger default capability and managed infrastructure. An open model buys inspectability, repeatability, and the ability to run ablations. Embodied AI cares about both because hardware debugging rarely succeeds when the decision process is a black box.",
        "algorithm_title": "Algorithm: Choose a model regime for embodied deployment",
        "algorithm_steps": [
            "Define the latency, privacy, reproducibility, and fine-tuning requirements of the task.",
            "Score one open and one closed candidate on the same workload and evidence panel.",
            "Record which claims depend on provider-side hidden components, such as unknown training data or runtime filtering.",
            "Choose the smallest model regime that satisfies the deployment contract.",
            "Keep a migration plan in case the chosen regime becomes unavailable or too expensive."
        ],
        "table_title": "Open vs. Closed Decision Matrix",
        "table_rows": [
            ("Closed model", "High default capability, vendor tooling, managed inference", "Opaque failure analysis and weaker reproducibility."),
            ("Open model", "Local inspection, weight access, custom fine-tuning", "More infrastructure burden and potentially weaker default performance."),
            ("Hybrid strategy", "Closed planner with open local executor or monitor", "Useful when privacy and capability must be balanced."),
            ("Evidence artifact", "Cost, latency, reproducibility, and failure analysis table", "Prevents branding from replacing engineering judgment."),
        ],
        "code": """# Governance card for open-vs-closed decisions.\ngovernance = {\n    \"task\": \"household planning plus manipulation\",\n    \"privacy\": \"camera frames cannot leave the site\",\n    \"reproducibility_need\": \"high\",\n    \"closed_model_role\": \"optional planner prototype\",\n    \"open_model_role\": \"primary deployed executor\",\n}\nprint(governance)""",
        "output": "{'task': 'household planning plus manipulation', 'privacy': 'camera frames cannot leave the site', 'reproducibility_need': 'high', 'closed_model_role': 'optional planner prototype', 'open_model_role': 'primary deployed executor'}",
        "output_interp": "The expected output should reveal why the model choice was made. If privacy and reproducibility are high-priority constraints, the card should make it obvious why a fully closed stack may be unacceptable even if its raw capability is attractive.",
        "tools": "OpenVLA, LeRobot, local VLM stacks, provider APIs, Triton, vLLM, MLflow",
        "practical": "A good project prototype may begin with a closed planner to move quickly, then migrate to an open VLA or smaller local VLM for the deployed path. Students should explicitly record which artifacts remain reproducible after the migration and which capabilities were lost or gained.",
        "frontier": "The frontier question is whether open robot foundation models can close enough of the capability gap while preserving inspectability. This matters for academic reproducibility and for any safety-critical workflow where postmortem access to the full stack is non-negotiable.",
        "xref": '<a href="../../part-7-language-vision-and-vision-language-action-models/module-34-vla-models-openvla-pi0-gr00t-and-beyond/index.html">Chapter 34 on open and closed VLA ecosystems</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-55-deployment-architecture/index.html">Chapter 55 on deployment architecture</a>',
    },
    "58.5": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.5.html",
        "topic": "What is still unsolved (long-horizon reasoning, reliability, real-world RL)",
        "bridge": "This section names the failures that still separate strong demos from dependable embodied systems. Long-horizon reasoning, reliability under shift, and real-world reinforcement learning remain difficult because they require the agent to preserve credit assignment, memory, safety, and calibration over many interacting decisions.",
        "problem": "The useful move is to turn each broad complaint into a measurable failure mode. Instead of saying that robots struggle with long horizons, specify whether the failure comes from memory decay, cumulative localization drift, mistaken subgoal commitment, or reward sparsity.",
        "formula": r"Reliability over a deployment horizon $H$ can be summarized as $R(H)=\Pr(\text{task success and no safety violation for all } t\le H)$. This is stricter than average success because a policy that succeeds 90 percent of short episodes may still have a poor $R(H)$ once failures compound across time.",
        "intuition": "The difference between success rate and reliability is temporal composition. A system can be good at isolated moves and still bad at staying good for twenty minutes, across new homes, with intermittent sensing, or after one awkward recovery step.",
        "algorithm_title": "Algorithm: Convert open problems into a reliability panel",
        "algorithm_steps": [
            "Choose one long-horizon task with meaningful recovery opportunities.",
            "Label failure families: memory, grounding, planning, control, safety, and evaluation.",
            "Run nominal, shifted, and interruption-heavy episodes with a fixed metric script.",
            "Measure both task success and reliability-over-time, including intervention frequency.",
            "Keep the problem statement attached to the dominant failure family rather than to a generic headline."
        ],
        "table_title": "Open Problems and Measurement Targets",
        "table_rows": [
            ("Long-horizon reasoning", "Subgoal persistence, memory freshness, recovery after interruption", "Task completion over long episodes with error decomposition."),
            ("Reliability", "Repeatability across homes, tools, and human variation", "Reliability curve plus safety-intervention rate."),
            ("Real-world RL", "On-hardware sample efficiency and safe exploration", "Improvement per interaction hour and incident count."),
            ("Evidence artifact", "Failure-labeled replay suite and reliability ledger", "Turns vague frontier talk into actionable experiments."),
        ],
        "code": """# Reliability ledger for an open-problem study.\nledger = {\n    \"episode_minutes\": [5, 10, 20],\n    \"reliability\": [0.84, 0.61, 0.33],\n    \"dominant_failure\": \"memory stale after interrupted subgoal\",\n    \"interventions_per_hour\": 2.4,\n}\nprint(ledger)""",
        "output": "{'episode_minutes': [5, 10, 20], 'reliability': [0.84, 0.61, 0.33], 'dominant_failure': 'memory stale after interrupted subgoal', 'interventions_per_hour': 2.4}",
        "output_interp": "The expected output should show degradation with horizon, not just one aggregate success score. That degradation curve is the point: it tells the researcher where the loop stops being dependable.",
        "tools": "LeRobot, OpenVLA, ROS 2 logging, Dreamer-style planners, CleanRL, safety monitors, hardware replay tools",
        "practical": "A semester team can study reliability without expensive hardware by injecting interruptions, stale maps, and delayed observations in simulation, then tracing which subsystems fail first. The deliverable should be a replay suite and a ledger, not only a discussion paragraph.",
        "frontier": "The frontier problem is compositional reliability: can an embodied agent remain competent after many small mismatches rather than one catastrophic shift? Progress will probably come from better memory systems, stronger recovery policies, and evaluation protocols that treat repeated deployment as first-class evidence.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-45-locomotion-and-legged-robots/index.html">Chapter 45 on locomotion reliability</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">Chapter 54 on safety</a>',
    },
    "58.99": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.99.html",
        "topic": "Frontier Watch",
        "bridge": "Frontier-watch work is less about predicting winners and more about preserving judgment while the field moves quickly. New robot model releases, simulator announcements, and benchmark numbers should be treated as incoming hypotheses that must pass through the same evidence filter as any internal experiment.",
        "problem": "Without that filter, teams end up rewriting roadmaps around marketing velocity. This section therefore gives the reader a lightweight protocol for tracking frontier claims without confusing novelty, accessibility, and scientific support.",
        "formula": r"Assign each claim a watch score $W = s_{\text{artifact}} + s_{\text{independent eval}} + s_{\text{deployment evidence}} - s_{\text{ambiguity}}$. High scores indicate claims that merit replication or curricular inclusion; low scores stay on the watchlist until more evidence arrives.",
        "intuition": "The watch score is intentionally simple. It does not certify truth; it helps the lab decide which frontier claims deserve engineering time this month and which ones should remain annotated links in a reading list.",
        "algorithm_title": "Algorithm: Maintain a frontier watchlist",
        "algorithm_steps": [
            "Record every incoming claim with source type, model family, supported artifacts, and claimed capability.",
            "Separate first-party demos from independent evaluations and real deployment reports.",
            "Score each claim for artifact quality, independent support, and ambiguity.",
            "Schedule replication effort only for claims above a chosen threshold.",
            "Revisit low-scoring entries when new evidence appears."
        ],
        "table_title": "Frontier Watchlist Fields",
        "table_rows": [
            ("Claim", "What capability or benchmark improvement is being advertised", "Prevents vague enthusiasm from spreading across the lab."),
            ("Artifact", "Weights, code, logs, eval script, or only a video", "Determines whether replication is even possible."),
            ("Independent support", "Third-party benchmark, user report, or deployment note", "Separates launch theater from scientific traction."),
            ("Decision", "Teach now, replicate now, or watch only", "Turns the watchlist into action."),
        ],
        "code": """# Frontier-watch manifest.\nwatch_item = {\n    \"claim\": \"new VLA improves zero-shot kitchen tasks\",\n    \"artifact_level\": \"weights + eval script\",\n    \"independent_eval\": False,\n    \"deployment_report\": \"none yet\",\n    \"decision\": \"watch, do not rewrite syllabus yet\",\n}\nprint(watch_item)""",
        "output": "{'claim': 'new VLA improves zero-shot kitchen tasks', 'artifact_level': 'weights + eval script', 'independent_eval': False, 'deployment_report': 'none yet', 'decision': 'watch, do not rewrite syllabus yet'}",
        "output_interp": "The expected output is a judgment record. A frontier-watch item is useful only if another reader can see why the claim stayed on the watchlist instead of being promoted into the main build path.",
        "tools": "GitHub release trackers, arXiv alerts, benchmark dashboards, internal replication sheets, issue trackers",
        "practical": "An instructor or lab lead can turn this section into a weekly five-minute ritual: one student presents a new frontier claim, another student checks artifacts and independent support, and the class decides whether it is teach-now, replicate-now, or watch-only material.",
        "frontier": "The meta-frontier is evaluation literacy. As embodied AI moves faster, the scarce skill is not finding announcements, it is deciding which ones deserve integration into real systems, courses, and research agendas.",
        "xref": '<a href="../../part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.4.html">Section 60.4 on the research-seminar track</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html">Chapter 52 on evaluation discipline</a>',
    },
}


# Chapter 59 mappings
SECTIONS.update({
    "59.1": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.1.html",
        "topic": "Object search in a simulated home",
        "bridge": "This capstone looks simple on the surface, find an object in a home, but it exercises nearly every embodied-system interface at once: semantic grounding, navigation, memory, and stopping logic. The core difficulty is that success depends on when the agent decides it has enough evidence to stop searching.",
        "problem": "A capstone design should therefore avoid grading only final discovery. It should also measure false positives, wasted path length, collision budget, and how quickly the agent replans after negative evidence.",
        "formula": r"Let $T_{find}$ be time to discovery, $C$ collisions, $L$ path length ratio to an oracle, and $F$ false declarations. A simple capstone score is $J = \mathbb{1}[\text{found}] - \lambda_T T_{find} - \lambda_C C - \lambda_L L - \lambda_F F$.",
        "intuition": "The penalty terms prevent the project from gaming the task by rushing, colliding, or declaring success too early. Instructors should publish the weights and keep them fixed across all teams.",
        "algorithm_title": "Algorithm: Design the object-search capstone loop",
        "algorithm_steps": [
            "Choose a simulator, such as Habitat or AI2-THOR, and define a fixed house panel.",
            "Implement a baseline policy with map memory and semantic object hypotheses.",
            "Add a learned perception or planning component only after the baseline can be debugged by replay.",
            "Log time to discovery, wrong declarations, collisions, and replan count on every episode.",
            "Submit one replay case where the agent had to recover from an early false belief."
        ],
        "table_title": "Deliverables for the Object-Search Project",
        "table_rows": [
            ("Task contract", "Target object set, house panel, sensor package, stopping rule", "Lets other teams run the same task."),
            ("Baseline", "Heuristic frontier exploration plus semantic memory", "Gives the project a debuggable floor."),
            ("Improvement", "Learned detector, language query, or memory reranker", "Shows the real research contribution."),
            ("Evidence", "Replay, metrics, and one failure case", "Makes grading about systems evidence, not demo polish."),
        ],
        "code": """# Minimal evidence card for object search.\ncard = {\n    \"houses\": 12,\n    \"targets\": [\"mug\", \"remote\", \"towel\"],\n    \"stop_rule\": \"declare found after 3 consistent views\",\n    \"metrics\": [\"time_to_find\", \"false_declarations\", \"path_length_ratio\"],\n}\nprint(card)""",
        "output": "{'houses': 12, 'targets': ['mug', 'remote', 'towel'], 'stop_rule': 'declare found after 3 consistent views', 'metrics': ['time_to_find', 'false_declarations', 'path_length_ratio']}",
        "output_interp": "The expected output is a clear task card. If the stop rule is missing, the project is under-specified because success can be declared arbitrarily.",
        "tools": "Habitat, AI2-THOR, ROS 2, CLIP-style detectors, SAM 2, Hydra, Weights &amp; Biases",
        "practical": "A good undergraduate or graduate team can finish this project with a small number of houses if the evidence protocol is strict. The interesting result often comes from failure clustering, for example repeated confusion between mugs and cups in cluttered kitchen shelves.",
        "frontier": "The research extension is language-conditioned search under uncertainty: letting the user say 'find the blue mug I used this morning' and forcing the system to combine semantics, temporal memory, and exploration.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-30-navigation-and-path-planning/index.html">Chapter 30 on navigation</a> and <a href="../../part-6-skills-world-models-and-3d-representation/module-27-perception-and-active-perception/index.html">Chapter 27 on active perception</a>',
    },
    "59.2": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.2.html",
        "topic": "Language-guided navigation with replanning",
        "bridge": "Language-guided navigation becomes a capstone when the language instruction remains active throughout movement rather than only at the start. The hard cases happen when the instruction is underspecified, the map changes, or the original route becomes impossible and replanning must preserve the user intent.",
        "problem": "That makes the project more than shortest-path planning. It is a grounding and recovery system whose score should reward progress under changing conditions, not only arrival at a goal point.",
        "formula": r"Given instruction $g$, belief state $b_t$, and map $m_t$, the planner chooses $a_t \sim \pi(a_t\mid b_t,m_t,g)$ while minimizing $\sum_t c_{\text{travel}}(a_t)+\lambda c_{\text{instruction}}(b_t,g)+\mu c_{\text{replan}}(t)$.",
        "intuition": "The instruction cost penalizes routes that technically reach a location but violate the language intent, such as taking an unsafe path or missing the requested landmark sequence. Replanning cost matters because constant replanning can look intelligent while actually indicating instability.",
        "algorithm_title": "Algorithm: Build a language-guided replanning benchmark",
        "algorithm_steps": [
            "Define instruction categories, such as landmark following, room finding, and constraint-aware movement.",
            "Implement a classical baseline with symbolic grounding and a map planner.",
            "Add a learned language-grounding module or multimodal planner.",
            "Inject map changes or blocked passages that require replanning while preserving instruction intent.",
            "Score navigation success, replans, path inflation, and instruction-constraint violations together."
        ],
        "table_title": "Replanning Questions the Project Must Answer",
        "table_rows": [
            ("Grounding", "How are words mapped to places, objects, or constraints?", "This is the first source of failure."),
            ("Replanning trigger", "Blocked path, uncertainty spike, or new observation", "Prevents arbitrary rerouting."),
            ("Evaluation", "Same panel of instructions and perturbations for all methods", "Keeps comparisons honest."),
            ("Deliverable", "Replay with instruction text, map state, and replan reasons", "Lets graders inspect why replanning happened."),
        ],
        "code": """# Instruction-aware navigation project card.\ncard = {\n    \"instruction\": \"Go to the kitchen, avoid the wet floor, then stop near the blue fridge\",\n    \"blocked_corridor\": True,\n    \"metrics\": [\"success\", \"replans\", \"constraint_violations\", \"path_inflation\"],\n}\nprint(card)""",
        "output": "{'instruction': 'Go to the kitchen, avoid the wet floor, then stop near the blue fridge', 'blocked_corridor': True, 'metrics': ['success', 'replans', 'constraint_violations', 'path_inflation']}",
        "output_interp": "The expected output should make the perturbation explicit. If a project does not reveal what forced replanning, the reader cannot tell whether the algorithm solved a real problem or merely reran the planner unnecessarily.",
        "tools": "Nav2, Habitat, ROS 2, sentence encoders, CLIP, costmaps, OMPL",
        "practical": "A robust capstone includes at least one instruction with a soft constraint, such as avoiding a room or preferring a landmark, because those cases expose whether the language layer affects planning or is only decorative text around a geometric path planner.",
        "frontier": "An active frontier is instruction-conditioned recovery, where the robot explains why it is replanning and asks for clarification only when its belief becomes too uncertain. That moves the project toward mixed-initiative embodied interaction.",
        "xref": '<a href="../../part-7-language-vision-and-vision-language-action-models/module-31-language-for-embodied-agents/index.html">Chapter 31 on language for embodied agents</a> and <a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-30-navigation-and-path-planning/index.html">Chapter 30 on planning</a>',
    },
    "59.3": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.3.html",
        "topic": "Vision-based robotic pick-and-place (IL + RL)",
        "bridge": "Pick-and-place is a classic capstone because the task is legible and measurable, yet still rich enough to expose sensing, contact, imitation, exploration, and reward design. The combination of imitation learning and reinforcement learning is not a buzzword pair here; it is a staged training plan.",
        "problem": "Imitation gives the project a competent initialization. Reinforcement learning then improves robustness or recovery. The capstone should grade whether that second stage actually helps under perturbation rather than merely increasing training time.",
        "formula": r"Train a behavior cloning policy with $\mathcal{L}_{BC}=\sum_t \lVert a_t-\pi_\theta(o_t)\rVert^2$, then fine-tune with a policy-gradient or actor-critic objective on a reward that includes grasp success, placement success, and safety penalties.",
        "intuition": "The point of the two-stage design is to separate competence from robustness. A policy that already knows how to grasp can use RL budget on recovery and edge cases instead of wasting samples on the basic motion primitive.",
        "algorithm_title": "Algorithm: Stage an IL plus RL capstone",
        "algorithm_steps": [
            "Collect or reuse a small demonstration set with successful grasps and placements.",
            "Train a behavior-cloning baseline and verify its nominal success by replay.",
            "Define perturbations, such as distractor objects, pose offsets, or lighting changes.",
            "Fine-tune with RL only after the perturbation panel is fixed.",
            "Compare before and after on the same scenes, with failure labels for grasp, lift, transport, and placement."
        ],
        "table_title": "Evidence Needed for the Manipulation Project",
        "table_rows": [
            ("Dataset card", "Demonstration count, object set, camera layout, action interface", "Clarifies what the imitation prior actually contains."),
            ("RL objective", "Success rewards and safety penalties", "Shows which behaviors are being promoted."),
            ("Perturbation panel", "Object pose jitter, clutter, camera shift, distractor texture", "Tests whether RL improved robustness."),
            ("Replay suite", "One nominal and one recovery success, one stubborn failure", "Makes the training story inspectable."),
        ],
        "code": """# Two-stage manipulation project summary.\nsummary = {\n    \"demonstrations\": 250,\n    \"bc_success\": 0.71,\n    \"bc_plus_rl_success\": 0.83,\n    \"perturbation_panel\": \"clutter plus camera shift\",\n    \"dominant_failure_after_rl\": \"late placement drift\",\n}\nprint(summary)""",
        "output": "{'demonstrations': 250, 'bc_success': 0.71, 'bc_plus_rl_success': 0.83, 'perturbation_panel': 'clutter plus camera shift', 'dominant_failure_after_rl': 'late placement drift'}",
        "output_interp": "The expected output should show both stages on the same perturbation panel. If only the final model is reported, the reader cannot tell whether RL actually improved the system or whether the baseline was simply undertrained.",
        "tools": "ManiSkill, robomimic, Diffusion Policy, Isaac Lab, MuJoCo, LeRobot",
        "practical": "A strong team keeps the object set small and diverse rather than large and shallow. Three to five objects with careful failure analysis usually teach more than twenty objects with weak logging.",
        "frontier": "A good extension is cross-embodiment transfer: train on one arm and test whether fine-tuning on a second arm preserves the learned visual skill. That turns a standard manipulation project into a modern policy-transfer question.",
        "xref": '<a href="../../part-5-imitation-learning-datasets-and-policy-learning/module-21-imitation-learning/index.html">Chapter 21 on imitation learning</a> and <a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-42-robotic-manipulation/index.html">Chapter 42 on manipulation</a>',
    },
    "59.4": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.4.html",
        "topic": "Fine-tune an open VLA on a custom task (LeRobot)",
        "bridge": "This capstone puts the reader directly into the current open robot-foundation-model ecosystem. The value is not just using a modern VLA; it is learning how to define a narrow custom task, prepare the evidence card, and fine-tune without losing sight of action interfaces and evaluation discipline.",
        "problem": "A common failure is treating fine-tuning as a black-box recipe. This section instead asks what the dataset, embodiment, and action-tokenization assumptions are, and which metric should prove that task adaptation really happened.",
        "formula": r"Let $\pi_\theta(a_{1:H}\mid o_{1:T},g)$ be the open VLA and fine-tune by minimizing $\mathcal{L}(\theta)=\mathbb{E}_{(o,g,a)\sim D_{custom}}[-\log \pi_\theta(a\mid o,g)]$ on a custom dataset while freezing or adapting chosen backbone layers.",
        "intuition": "The loss is familiar, but the embodied stakes are different: tokenization, action discretization, and embodiment mismatch can dominate the outcome. Fine-tuning is therefore a systems adaptation problem as much as a machine-learning one.",
        "algorithm_title": "Algorithm: Fine-tune a VLA without losing the system contract",
        "algorithm_steps": [
            "Choose one narrow custom task with a stable action interface.",
            "Create a dataset card with camera layout, teleoperation method, and success definition.",
            "Fine-tune the smallest open model that fits the compute budget and deployment plan.",
            "Evaluate on nominal, shifted-camera, and unseen-object splits with the same script.",
            "Inspect whether gains come from language grounding, visual adaptation, or action-token improvements."
        ],
        "table_title": "Checklist for the Open-VLA Capstone",
        "table_rows": [
            ("Task scope", "One clear household or tabletop behavior", "Keeps the data collection burden realistic."),
            ("Dataset card", "Episode count, operator, camera, embodiment, label policy", "Makes fine-tuning assumptions explicit."),
            ("Compute plan", "Batch size, precision, frozen layers, runtime budget", "Fits the capstone to real student resources."),
            ("Evaluation", "Same task panel before and after fine-tuning", "Shows whether adaptation actually helped."),
        ],
        "code": """# Fine-tuning manifest for a LeRobot-based capstone.\nmanifest = {\n    \"base_model\": \"open-vla-small\",\n    \"custom_task\": \"fold towel corner and place on rack\",\n    \"episodes\": 180,\n    \"frozen_backbone\": True,\n    \"eval_splits\": [\"nominal\", \"camera_shift\", \"unseen_textures\"],\n}\nprint(manifest)""",
        "output": "{'base_model': 'open-vla-small', 'custom_task': 'fold towel corner and place on rack', 'episodes': 180, 'frozen_backbone': True, 'eval_splits': ['nominal', 'camera_shift', 'unseen_textures']}",
        "output_interp": "The expected output should be a reproducible fine-tuning manifest, not a notebook with hidden state. If a reader cannot recover the task, split, and freeze policy from the printed card, the capstone is not yet reproducible.",
        "tools": "LeRobot, OpenVLA, Hugging Face datasets, PyTorch, Accelerate, Weights &amp; Biases",
        "practical": "This project is ideal for a course because it exposes current tooling while keeping the task local. The most instructive result often comes from a small adaptation that helps one camera setup but hurts another, forcing students to reason about generalization instead of celebrating one headline win.",
        "frontier": "The frontier challenge is adaptation efficiency: how little task-specific data is needed to retarget a foundation policy to a new embodiment or household setup while preserving broad competence?",
        "xref": '<a href="../../part-7-language-vision-and-vision-language-action-models/module-34-vla-models-openvla-pi0-gr00t-and-beyond/index.html">Chapter 34 on VLAs</a> and <a href="../../part-5-imitation-learning-datasets-and-policy-learning/module-24-robot-datasets-and-data-quality/index.html">Chapter 24 on data quality</a>',
    },
    "59.5": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.5.html",
        "topic": "Learned locomotion with sim-to-real analysis",
        "bridge": "Locomotion is attractive as a capstone because the physics is dramatic and the reward is visible. It is also treacherous because a controller that looks heroic in simulation can fail immediately when friction, latency, or state estimation shift on hardware.",
        "problem": "The section therefore treats sim-to-real analysis as part of the project definition, not as a final bonus slide. A locomotion capstone succeeds only if it records what changed between simulation and hardware, and which gap was large enough to matter.",
        "formula": r"Let $J_{sim}$ and $J_{real}$ be the same reward computed in simulation and hardware under matched terrains. The transfer gap $\Delta_{sr}=J_{sim}-J_{real}$ should be reported together with estimator drift, recovery count, and falls per minute.",
        "intuition": "A single transfer gap number is not enough, but it is a forcing device. It makes the team explain which part of the stack failed: dynamics mismatch, sensing, actuation delay, or contact uncertainty.",
        "algorithm_title": "Algorithm: Structure the locomotion transfer study",
        "algorithm_steps": [
            "Train a locomotion policy in simulation with a clearly documented reward and curriculum.",
            "Build a hardware test panel with matched terrains and safety fallbacks.",
            "Measure estimator drift, latency, falls, and recovery behavior on the same maneuver set.",
            "Adjust one sim-to-real factor at a time, such as friction randomization or actuator delay.",
            "Report which factor reduced the transfer gap and which failures remained."
        ],
        "table_title": "Locomotion Project Deliverables",
        "table_rows": [
            ("Training spec", "Reward, curriculum, terrain distribution, randomization ranges", "Makes the simulator assumptions visible."),
            ("Hardware panel", "Terrain list, speed commands, safety harness rules", "Prevents selective deployment stories."),
            ("Transfer metrics", "Falls, recovery, velocity tracking, cost of transport", "Captures both performance and stability."),
            ("Postmortem", "One matched sim and real replay with commentary", "Forces honest transfer analysis."),
        ],
        "code": """# Sim-to-real analysis card for locomotion.\ntransfer = {\n    \"sim_reward\": 0.92,\n    \"real_reward\": 0.67,\n    \"falls_per_minute\": 0.8,\n    \"largest_gap_factor\": \"state-estimator delay\",\n}\nprint(transfer)""",
        "output": "{'sim_reward': 0.92, 'real_reward': 0.67, 'falls_per_minute': 0.8, 'largest_gap_factor': 'state-estimator delay'}",
        "output_interp": "The expected output must identify a real transfer bottleneck. If the printed record cannot point to the dominant mismatch, the sim-to-real analysis is still too vague to guide the next experiment.",
        "tools": "Isaac Lab, MuJoCo, Unitree SDKs, ROS 2, skrl, rl_games, safety harness logging",
        "practical": "Even a simulator-only course can teach this project well by asking students to produce a transfer plan with expected failure factors before they ever touch hardware. That planning discipline is exactly what many flashy locomotion demos hide.",
        "frontier": "A strong research extension is morphology-aware transfer: whether the same latent skill or policy family can move across quadrupeds, humanoids, or payload changes without retraining from scratch.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-45-locomotion-and-legged-robots/index.html">Chapter 45 on locomotion</a> and <a href="../../part-4-simulation-and-synthetic-data/module-13-domain-randomization-curricula-and-sim-to-real/index.html">Chapter 13 on sim-to-real</a>',
    },
    "59.6": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.6.html",
        "topic": "World-model-based planning agent",
        "bridge": "This capstone takes the world-model theory from earlier chapters and turns it into a concrete project with a clear planning loop. The interesting question is not whether a learned model predicts visuals nicely, but whether it helps the agent choose better actions under limited interaction budget.",
        "problem": "A clean capstone therefore compares a planner with and without the world model on the same task family, horizon, and safety constraints. The evidence has to reveal whether imagined futures improved the real loop or merely produced attractive latent rollouts.",
        "formula": r"The planner chooses $a_{t:t+H-1}^{\star}=\arg\max \mathbb{E}\left[\sum_{\tau=t}^{t+H-1}\gamma^{\tau-t}\hat r(z_\tau,a_\tau)-\lambda u(z_\tau)\right]$, where $u(z_\tau)$ is a model-uncertainty penalty. The uncertainty term matters because the best imagined path may live in a part of latent space the model has barely seen.",
        "intuition": "The uncertainty penalty is the bridge from research idea to system design. It is what stops the capstone from rewarding beautiful model hallucinations that would be dangerous on a real robot.",
        "algorithm_title": "Algorithm: Evaluate a world-model capstone honestly",
        "algorithm_steps": [
            "Choose a task with nontrivial planning horizon, such as object pushing with obstacles.",
            "Train or reuse a latent dynamics model and expose its uncertainty estimate.",
            "Run an MPC-style planner inside the model, then execute one step and replan.",
            "Compare against a model-free or scripted baseline on the same panel.",
            "Save at least one replay where latent prediction drift causes an action mistake."
        ],
        "table_title": "World-Model Capstone Checklist",
        "table_rows": [
            ("Latent state", "Encoder, stochasticity, and uncertainty representation", "Defines what the planner is really optimizing over."),
            ("Planning horizon", "Short enough to stay calibrated, long enough to matter", "Controls the value of the model."),
            ("Baselines", "Scripted MPC, model-free policy, or heuristic planner", "Prevents a one-model story."),
            ("Evidence", "Drift plots, replay, and task metrics", "Shows whether the model helped the loop."),
        ],
        "code": """# World-model planning evidence card.\ncard = {\n    \"task\": \"push object around occluding blocker\",\n    \"planning_horizon\": 10,\n    \"uncertainty_penalty\": 0.4,\n    \"baseline\": \"model-free actor-critic\",\n    \"key_failure\": \"drift after contact change\",\n}\nprint(card)""",
        "output": "{'task': 'push object around occluding blocker', 'planning_horizon': 10, 'uncertainty_penalty': 0.4, 'baseline': 'model-free actor-critic', 'key_failure': 'drift after contact change'}",
        "output_interp": "The expected output should reveal the planning assumptions and failure mode before any score is shown. Without that information the grader cannot tell why the world model succeeded or failed.",
        "tools": "DreamerV3, TD-MPC2, mbrl-lib, MuJoCo, JAX or PyTorch, Hydra",
        "practical": "A great capstone report includes one page where the student lines up real observations, predicted latent rollouts, and the chosen action. That single page often teaches more than a long appendix of aggregate numbers.",
        "frontier": "A natural extension is multimodal world models that combine vision, proprioception, and language constraints, then expose enough uncertainty for planning and safety monitors to cooperate.",
        "xref": '<a href="../../part-8-world-models-model-based-rl-and-planning/module-38-world-models/index.html">Chapter 38 on world models</a> and <a href="../../part-8-world-models-model-based-rl-and-planning/module-39-model-based-rl/index.html">Chapter 39 on model-based RL</a>',
    },
    "59.7": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.7.html",
        "topic": "Safety-shielded embodied agent",
        "bridge": "A safety-shielded capstone asks whether a learning or planning system can stay productive while an explicit monitor rejects unsafe actions. This is a strong course project because it forces the student to specify the safety envelope rather than treating safety as a vague afterthought.",
        "problem": "The project fails if the shield is decorative or if it blocks almost every action and the nominal controller never really works. The grading should therefore reward both task completion and meaningful safe intervention statistics.",
        "formula": r"Let $\pi(a_t\mid s_t)$ propose an action and let a shield $\sigma(s_t,a_t)\in\{0,1\}$ accept or replace it. The deployed action is $\tilde a_t = a_t$ if $\sigma=1$, otherwise $\tilde a_t = a_t^{safe}$, and the capstone should report both task return and blocked-action rate.",
        "intuition": "Blocked-action rate is not automatically good. A high rate may mean the base controller is dangerous or the shield is too conservative. The student should interpret that number together with success and recovery metrics.",
        "algorithm_title": "Algorithm: Build a shielded-agent project",
        "algorithm_steps": [
            "Name the unsafe state or action families before choosing the policy architecture.",
            "Implement a nominal controller or policy that is allowed to fail in simulation.",
            "Add a shield that either vetoes, clips, or replaces unsafe actions.",
            "Measure task success, intervention count, blocked-action rate, and false alarms together.",
            "Present one replay where the shield clearly helped and one where it was overly conservative."
        ],
        "table_title": "Safety-Shield Metrics",
        "table_rows": [
            ("Unsafe-action definition", "Collision, joint limit, human zone, battery floor, or no-fly region", "Defines what the shield is trying to prevent."),
            ("Intervention policy", "Veto, clip, projection, or safe replacement", "Changes both control feel and task success."),
            ("Evaluation", "Success, blocked actions, false alarms, recovery delay", "Shows the cost of safety."),
            ("Artifact", "Safety replay plus incident ledger", "Makes the monitor behavior inspectable."),
        ],
        "code": """# Safety-shield evaluation card.\ncard = {\n    \"unsafe_region\": \"human workspace cylinder\",\n    \"interventions\": 17,\n    \"false_alarm_rate\": 0.09,\n    \"task_success\": 0.78,\n}\nprint(card)""",
        "output": "{'unsafe_region': 'human workspace cylinder', 'interventions': 17, 'false_alarm_rate': 0.09, 'task_success': 0.78}",
        "output_interp": "The expected output must expose the tradeoff. If the task succeeds but the intervention count is extreme, the next engineering step is to improve the nominal controller, not to celebrate the shield.",
        "tools": "ROS 2, control barrier function toolkits, shielded RL baselines, MuJoCo, runtime monitors",
        "practical": "This project works well with drones, manipulators, or mobile robots because the shield can be simple and still meaningful, for example a workspace cylinder or joint-limit barrier. Simplicity is an advantage because students can reason about false positives and false negatives.",
        "frontier": "The research extension is learned safety monitors that remain auditable. A frontier-worthy project combines formal safety structure with a learned uncertainty signal rather than replacing explicit constraints entirely.",
        "xref": '<a href="../../part-11-evaluation-safety-robustness-and-deployment/module-54-safety-in-embodied-ai/index.html">Chapter 54 on safety</a> and <a href="../../part-3-dynamics-control-and-state-estimation/module-07-control-for-embodied-ai/index.html">Chapter 7 on control</a>',
    },
    "59.8": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.8.html",
        "topic": "LLM-based household task planner",
        "bridge": "This project asks the student to separate planning language from embodied execution. That separation is the educational value: the capstone should show exactly which part of the task is solved by language reasoning and which part still depends on grounding, affordances, and controller feedback.",
        "problem": "The common mistake is grading only a beautiful text plan. This section instead requires plan validity, affordance consistency, and execution outcome under a fixed household task panel.",
        "formula": r"Let a language planner produce subgoals $g_{1:K}$ and let an executor return success probabilities $p_k$. The project should track $\Pr(\text{task success})=\prod_{k=1}^{K} p_k$ only after each subgoal has passed a grounding and affordance check, otherwise the multiplication hides impossible steps behind optimistic language.",
        "intuition": "The multiplicative view is a reminder that one impossible drawer-open action can collapse the whole task. Long plans are therefore fragile unless the project has explicit replanning and affordance validation.",
        "algorithm_title": "Algorithm: Turn an LLM plan into an executable capstone",
        "algorithm_steps": [
            "Define a small set of household tasks with object and affordance annotations.",
            "Generate a text plan, then ground each step into robot-executable operators.",
            "Reject or repair steps that violate object availability, reachability, or safety constraints.",
            "Execute or simulate the grounded plan and log replans with reasons.",
            "Grade the project on plan validity, execution success, and explanation quality."
        ],
        "table_title": "Planner Project Evidence",
        "table_rows": [
            ("Text plan", "Ordered subgoals from the LLM", "Shows high-level reasoning."),
            ("Grounded plan", "Robot operators with object IDs and affordance checks", "Shows whether the plan is executable."),
            ("Execution trace", "Successes, failures, and replans", "Reveals how language and embodiment interact."),
            ("Failure note", "At least one impossible or unsafe subgoal", "Prevents cherry-picked polished demos."),
        ],
        "code": """# Household planning evidence card.\ncard = {\n    \"task\": \"set the table for one person\",\n    \"subgoals\": 6,\n    \"invalid_subgoals_before_grounding\": 2,\n    \"replans\": 1,\n    \"final_success\": True,\n}\nprint(card)""",
        "output": "{'task': 'set the table for one person', 'subgoals': 6, 'invalid_subgoals_before_grounding': 2, 'replans': 1, 'final_success': True}",
        "output_interp": "The expected output should reveal where the text planner overreached. Invalid subgoals are not embarrassing here, they are the main evidence that grounding checks are doing real work.",
        "tools": "OpenAI-style function calling or local LLMs, VoxPoser-style planners, ROS 2 task graphs, scene graphs, Habitat or AI2-THOR",
        "practical": "Students should submit both the raw language plan and the grounded operator list. The mismatch between them is usually where the intellectual value of the capstone lives.",
        "frontier": "A strong extension is mixed-initiative planning where the robot asks a short clarification question only when ambiguity or affordance failure is high. That exposes whether language should drive action directly or act as a negotiation layer.",
        "xref": '<a href="../../part-7-language-vision-and-vision-language-action-models/module-31-language-for-embodied-agents/index.html">Chapter 31 on language</a> and <a href="../../part-7-language-vision-and-vision-language-action-models/module-33-vlm-planning-tool-use-and-code-as-policies/index.html">Chapter 33 on tool use and planning</a>',
    },
    "59.9": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.9.html",
        "topic": "Drone inspection planner",
        "bridge": "Drone inspection is a natural capstone because it combines planning, control, sensing, and operating-domain constraints in a way that is immediately legible. The project becomes serious once battery, line of sight, wind, and inspection coverage are treated as state variables that drive route choice.",
        "problem": "The capstone should therefore grade coverage and safety together. An inspection route that finds all defects but violates battery reserve or no-fly rules is not a successful embodied system.",
        "formula": r"Let route cost be $J=\sum_{t} c_{\text{flight}}(x_t,u_t)+\lambda c_{\text{missed coverage}}+\mu c_{\text{safety}}$, where $c_{\text{safety}}$ includes reserve battery, geofence, and visibility penalties. The planner wins only if coverage improves without breaking the safety envelope.",
        "intuition": "Coverage and safety push in opposite directions. The interesting designs are the ones that make that tradeoff explicit instead of letting the route optimizer quietly ignore one of the terms.",
        "algorithm_title": "Algorithm: Structure the inspection-planner capstone",
        "algorithm_steps": [
            "Choose an inspection asset and define the coverage objective, sensor footprint, and safety constraints.",
            "Implement a geometric baseline route with explicit battery reserve and return-home logic.",
            "Add a learned planner or perception-driven rerouting module.",
            "Evaluate on matched weather or wind scenarios with the same mission script.",
            "Save one replay that shows why the route changed and how the safety monitor reacted."
        ],
        "table_title": "Drone Project Deliverables",
        "table_rows": [
            ("Mission card", "Asset geometry, no-fly zones, launch point, reserve battery floor", "Defines the operating domain."),
            ("Perception model", "Defect detector or coverage estimator", "Clarifies what drives adaptive routing."),
            ("Control stack", "PX4, simulator, controller rates, fallback behavior", "Makes the action interface concrete."),
            ("Evidence", "Coverage map, battery trace, and safety events", "Lets graders inspect the whole mission."),
        ],
        "code": """# Inspection mission card.\nmission = {\n    \"asset\": \"bridge underside bay B\",\n    \"reserve_battery\": 0.22,\n    \"coverage_target\": 0.95,\n    \"wind_perturbation\": \"crosswind 5 m/s\",\n    \"safety_events\": 0,\n}\nprint(mission)""",
        "output": "{'asset': 'bridge underside bay B', 'reserve_battery': 0.22, 'coverage_target': 0.95, 'wind_perturbation': 'crosswind 5 m/s', 'safety_events': 0}",
        "output_interp": "The expected output should show why the mission is safe to grade. Reserve battery and perturbation are not optional metadata; they are the conditions under which the route claim is meaningful.",
        "tools": "PX4 SITL, ROS 2, Gazebo, AirSim, OpenCV, COLMAP, route planners",
        "practical": "A student project can stay simulator-first and still be excellent if the evidence artifact is strong: one route card, one safety trace, one adaptive reroute, and one failure replay under wind or occlusion.",
        "frontier": "A compelling extension is active inspection, where perception uncertainty reshapes the path online. That moves the project from route planning to information-gathering control.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-47-drones-and-aerial-robotics/index.html">Chapter 47 on drones</a> and <a href="../../part-3-dynamics-control-and-state-estimation/module-08-sensing-and-state-estimation/index.html">Chapter 8 on estimation</a>',
    },
    "59.10": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.10.html",
        "topic": "Multi-agent search and rescue",
        "bridge": "Multi-agent search and rescue is an excellent advanced capstone because it forces students to reason about communication, deconfliction, and shared belief rather than only about single-agent competence. Team performance can improve dramatically, or collapse, depending on bandwidth and stale maps.",
        "problem": "The project should therefore define what is shared, when it is shared, and how stale information is handled. Without that, multi-agent behavior becomes a story about many animated robots rather than a controlled systems experiment.",
        "formula": r"Let each agent $i$ carry belief $b_t^{(i)}$ and share messages $m_t^{(i\rightarrow j)}$. Team objective can be written as $\max \mathbb{E}\left[\sum_t r_t^{team} - \lambda \sum_{i,j}\text{comm\_cost}(m_t^{(i\rightarrow j)})\right]$, so communication is useful only when the information gain exceeds the bandwidth cost.",
        "intuition": "This objective keeps the project honest about communication. Unlimited messaging can hide poor coordination design, while zero messaging can make the team duplicate work. The capstone should explore that tradeoff explicitly.",
        "algorithm_title": "Algorithm: Build a coordinated rescue project",
        "algorithm_steps": [
            "Define the disaster map, victim model, communication budget, and role assignments.",
            "Implement a non-communicating or centrally scripted baseline.",
            "Add belief sharing or task allocation under explicit bandwidth limits.",
            "Evaluate team success, duplicate coverage, communication load, and rescue latency together.",
            "Submit one replay where stale information caused a coordination failure."
        ],
        "table_title": "Search-and-Rescue Team Artifacts",
        "table_rows": [
            ("Role policy", "Scout, carrier, mapper, relay, or symmetric team", "Defines what each agent is trying to optimize."),
            ("Communication protocol", "Periodic, event-driven, or uncertainty-triggered sharing", "Shapes bandwidth use and coordination quality."),
            ("Map update policy", "How local beliefs become shared beliefs", "Controls stale-information risk."),
            ("Evidence", "Coverage map, message log, and victim timeline", "Shows whether teamwork really helped."),
        ],
        "code": """# Multi-agent SAR evidence card.\ncard = {\n    \"agents\": 4,\n    \"bandwidth_kbps\": 80,\n    \"rescues\": 7,\n    \"duplicate_room_entries\": 3,\n    \"stale_map_failure\": True,\n}\nprint(card)""",
        "output": "{'agents': 4, 'bandwidth_kbps': 80, 'rescues': 7, 'duplicate_room_entries': 3, 'stale_map_failure': True}",
        "output_interp": "The expected output should expose both coordination success and waste. Duplicate room entries are not trivia; they show whether the shared-belief protocol is paying for itself.",
        "tools": "PettingZoo, ROS 2, Habitat, AirSim, MARL baselines, centralized logging",
        "practical": "An effective team project gives each subgroup ownership of one subsystem, such as mapping, allocation, or communications, but still requires one integrated evidence artifact. That mirrors real research collaboration while preserving accountability.",
        "frontier": "The extension is heterogeneous teaming with drones and ground robots. Once the bodies differ, role allocation and belief fusion become much more interesting than raw policy learning.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-47-drones-and-aerial-robotics/index.html">Chapter 47 on aerial agents</a> and <a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-30-navigation-and-path-planning/index.html">Chapter 30 on navigation</a>',
    },
    "59.11": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.11.html",
        "topic": "Open-ended research project",
        "bridge": "The open-ended capstone is where the book stops prescribing topics and starts prescribing research hygiene. The challenge is not choosing the flashiest domain; it is formulating a question with an evidence loop that can survive contact with deadlines, limited compute, and incomplete intuition.",
        "problem": "Students often over-scope these projects. This section therefore narrows the problem by asking for one clear thesis, one baseline, one perturbation panel, and one failure narrative that justifies the next iteration.",
        "formula": r"An open-ended project can be summarized by $(Q,B,P,A)$: a question $Q$, baseline $B$, perturbation panel $P$, and artifact set $A$. If any element is missing, the project tends to become either a broad survey or a tool-demo rather than a real embodied experiment.",
        "intuition": "This tuple is intentionally minimal. It forces the student to say what is being tested, against what, under which stressors, and with which evidence. Everything else, including model choice, is downstream.",
        "algorithm_title": "Algorithm: Turn an idea into a tractable research capstone",
        "algorithm_steps": [
            "Write the research question in one sentence with a measurable outcome.",
            "Choose the simplest baseline that could disprove the fancy method.",
            "Define a perturbation panel that will expose failure if the idea is weak.",
            "Specify the artifact bundle: code, config, metrics, replay, and one failure note.",
            "Freeze scope before implementation and only reopen it if the evidence requires it."
        ],
        "table_title": "Open-Ended Project Scoping Gates",
        "table_rows": [
            ("Question", "One hypothesis about perception, planning, control, or adaptation", "Prevents tool collection from masquerading as research."),
            ("Baseline", "A simple alternative that could win", "Creates a real decision problem."),
            ("Perturbation panel", "Shift, noise, latency, horizon, or embodiment change", "Tests whether the hypothesis generalizes."),
            ("Artifact bundle", "Metrics, replay, config, and postmortem", "Makes the work gradeable and publishable."),
        ],
        "code": """# Open-ended project charter.\ncharter = {\n    \"question\": \"Does retrieval-augmented policy memory reduce long-horizon kitchen failures?\",\n    \"baseline\": \"same policy without retrieval memory\",\n    \"perturbation_panel\": [\"delayed observations\", \"object moved mid-task\"],\n    \"artifact_bundle\": [\"config\", \"metrics\", \"replay\", \"failure_note\"],\n}\nprint(charter)""",
        "output": "{'question': 'Does retrieval-augmented policy memory reduce long-horizon kitchen failures?', 'baseline': 'same policy without retrieval memory', 'perturbation_panel': ['delayed observations', 'object moved mid-task'], 'artifact_bundle': ['config', 'metrics', 'replay', 'failure_note']}",
        "output_interp": "The expected output should make the project falsifiable. If the charter cannot be disproved by a baseline on a defined panel, it is still an interest area, not yet a research project.",
        "tools": "Hydra, Git, Weights &amp; Biases, LeRobot, ROS 2, Habitat, MuJoCo, Jupyter",
        "practical": "This section works well as a proposal defense. A five-minute live review of the charter often reveals missing baselines or missing perturbations before any compute has been wasted.",
        "frontier": "The frontier extension is meta-research on embodied evaluation itself. Some of the strongest student projects ask whether our current benchmarks actually predict field performance.",
        "xref": '<a href="../../part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/index.html">Chapter 58 on open problems</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html">Chapter 52 on evaluation</a>',
    },
    "59.12": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.12.html",
        "topic": "Application Track Capstone Templates",
        "bridge": "This section is the synthesis layer for the whole capstone chapter. Instead of one project, it offers reusable track templates that cover the main embodied-application families and make their hidden systems assumptions visible before a team starts coding.",
        "problem": "The design problem is curricular and technical at the same time: how do you give students enough structure to build something real without flattening the differences between drones, autonomous driving, humanoids, household robots, and industrial fleets?",
        "formula": r"For each application track define a template $T=(\text{ODD},\text{state},\text{actions},\text{safety},\text{metrics},\text{artifacts})$. The template succeeds when teams can instantiate it to different domains without changing the evidence logic.",
        "intuition": "The power of the template is invariance. The operating domain and controller differ across tracks, but every good embodied capstone still needs a task card, a safety envelope, a metric panel, and replayable evidence.",
        "algorithm_title": "Algorithm: Instantiate an application-track template",
        "algorithm_steps": [
            "Select a domain, such as household manipulation, drone inspection, autonomous driving, or warehouse autonomy.",
            "Fill in the operating-domain card, state variables, action interface, and safety constraints.",
            "Choose a baseline stack and one proposed improvement path.",
            "Commit to one metric panel and one failure taxonomy before implementation.",
            "Deliver the track-specific artifact bundle plus a common evidence card."
        ],
        "table_title": "Top Application Tracks",
        "table_rows": [
            ("Household manipulation", "LeRobot, ManiSkill, ROS 2, tabletop or home scene", "Success, retries, object damage, recovery quality."),
            ("Drone inspection", "PX4 SITL, ROS 2, perception stack, route planner", "Coverage, battery reserve, geofence events, missed defects."),
            ("Autonomous driving", "CARLA, CommonRoad, planner, controller", "Route completion, comfort, infractions, fallback quality."),
            ("Humanoid or mobile manipulation", "Isaac Lab, MuJoCo, whole-body control stack", "Task success, balance loss, recovery, safety stops."),
        ],
        "code": """# Track-instantiation summary.\ntrack = {\n    \"domain\": \"autonomous driving research prototype\",\n    \"odd\": \"campus roads, daylight only, 20 km/h max\",\n    \"safety_constraint\": \"geofenced route plus emergency stop\",\n    \"artifact_bundle\": [\"scenario panel\", \"metrics\", \"replay\", \"incident note\"],\n}\nprint(track)""",
        "output": "{'domain': 'autonomous driving research prototype', 'odd': 'campus roads, daylight only, 20 km/h max', 'safety_constraint': 'geofenced route plus emergency stop', 'artifact_bundle': ['scenario panel', 'metrics', 'replay', 'incident note']}",
        "output_interp": "The expected output should feel like a ready-to-use project brief. If the operating domain and artifact bundle are explicit, a team can start building without arguing over what counts as evidence.",
        "tools": "Isaac Lab, MuJoCo, CARLA, CommonRoad, PX4 SITL, Habitat 3.0, ManiSkill, ROS-Industrial, Open-RMF, LeRobot",
        "practical": "Instructors can assign different tracks to different teams while keeping one shared grading rubric because the evidence schema remains common. That is what makes the chapter scalable as a course resource.",
        "frontier": "A useful research extension is cross-track transfer, for example whether a memory or planning module developed in household robotics survives adaptation to drones or warehouse fleets.",
        "xref": '<a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-47-drones-and-aerial-robotics/index.html">Chapter 47 on drones</a>, <a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-48-autonomous-driving/index.html">Chapter 48 on autonomous driving</a>, and <a href="../../part-9-manipulation-locomotion-drones-driving-and-embodied-applications/module-46-humanoids/index.html">Chapter 46 on humanoids</a>',
    },
})


# Chapter 60 mappings
SECTIONS.update({
    "60.1": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.1.html",
        "topic": "One-semester graduate course (14 weeks)",
        "bridge": "A graduate version of the book should feel like a research apprenticeship, not a long reading list. The rhythm must make theory, implementation, evaluation, and paper discussion reinforce one another every week.",
        "problem": "The main design problem is pacing depth without exhausting students. That means each week should have one load-bearing idea, one executable artifact, and one discussion prompt that pushes beyond engineering procedure.",
        "formula": r"Model weekly load as $L_k = \alpha T_k + \beta C_k + \gamma P_k$, where $T_k$ is theory depth, $C_k$ is coding burden, and $P_k$ is paper-reading burden. A stable graduate schedule keeps $\max_k L_k$ bounded while letting the capstone load rise over the semester.",
        "intuition": "The load model is not precise accounting. It is a design check that prevents instructors from stacking a proof-heavy week, a heavy lab, and several frontier papers all at once.",
        "algorithm_title": "Algorithm: Build a 14-week graduate sequence",
        "algorithm_steps": [
            "Open with foundations, state estimation, and control so later papers have a common language.",
            "Pair each conceptual week with one reproducible artifact, such as a simulator run or evaluation notebook.",
            "Move from perception and policies into planning, world models, and deployment once students can debug the loop.",
            "Introduce capstone milestones early: proposal, baseline, panel, midterm failure review, final artifact.",
            "Reserve the last weeks for frontier synthesis and project defense rather than new core prerequisites."
        ],
        "table_title": "Suggested Weekly Arc for Graduate Teaching",
        "table_rows": [
            ("Weeks 1 to 3", "Agent loop, geometry, dynamics, control, estimation", "Common technical floor."),
            ("Weeks 4 to 7", "Simulation, RL, imitation learning, datasets", "How policies are trained and tested."),
            ("Weeks 8 to 11", "Language, VLAs, planning, world models", "Modern embodied stacks."),
            ("Weeks 12 to 14", "Safety, deployment, frontier watch, capstones", "Research synthesis and project completion."),
        ],
        "code": """# Graduate-course planning card.\nplan = {\n    \"weeks\": 14,\n    \"artifacts_per_week\": 1,\n    \"paper_discussion_every_week\": True,\n    \"capstone_milestones\": [\"proposal\", \"baseline\", \"failure_review\", \"final_demo\"],\n}\nprint(plan)""",
        "output": "{'weeks': 14, 'artifacts_per_week': 1, 'paper_discussion_every_week': True, 'capstone_milestones': ['proposal', 'baseline', 'failure_review', 'final_demo']}",
        "output_interp": "The expected output should reveal the teaching rhythm. If the course card lacks milestone structure, the semester will drift toward unscaffolded final projects.",
        "tools": "Jupyter, MuJoCo, Isaac Lab, LeRobot, GitHub Classroom, lightweight CI, paper discussion sheets",
        "practical": "A good graduate offering uses the same lab artifact for both grading and seminar discussion. Students should be able to show a replay, defend one design choice, and connect it to a paper claim in the same class meeting.",
        "frontier": "The frontier teaching question is how much foundation-model content can be added without crowding out control, estimation, and evaluation. This chapter argues for integration rather than replacement.",
        "xref": '<a href="../../part-1-foundations-of-embodied-ai/index.html">Part I foundations</a> and <a href="../../part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/index.html">Chapter 59 on capstones</a>',
    },
    "60.2": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.2.html",
        "topic": "One-semester advanced undergraduate course (lighter theory, more labs)",
        "bridge": "An advanced undergraduate version should preserve the honesty of embodied AI without assuming mature mathematical fluency from day one. The design goal is to keep the system loop visible while shifting some formal depth into guided experiments, diagrams, and reflection.",
        "problem": "The challenge is not simplification for its own sake. It is choosing which abstractions students must derive themselves and which ones they should experience empirically through well-designed labs.",
        "formula": r"Let mastery be approximated by $M_k = w_c C_k + w_l L_k + w_r R_k$, where $C_k$ is conceptual understanding, $L_k$ is lab completion quality, and $R_k$ is reflective explanation. Undergraduate adaptation should raise $L_k$ and $R_k$ when formal derivation time is reduced.",
        "intuition": "If you lighten theory without increasing experiments and reflection, students only lose depth. The substitution works only when each removed derivation is replaced by a concrete artifact or visual diagnosis that teaches the same mechanism from another angle.",
        "algorithm_title": "Algorithm: Adapt the book for advanced undergraduates",
        "algorithm_steps": [
            "Keep the full loop structure but reduce theorem density in the first half of the term.",
            "Replace some derivations with numeric traces, visual diagnostics, and guided notebooks.",
            "Use smaller project scopes with tightly specified deliverables and shorter feedback cycles.",
            "Require students to explain failure cases in prose, not just submit working code.",
            "Offer optional deeper readings for students who want the graduate-level derivations."
        ],
        "table_title": "Undergraduate Adaptation Levers",
        "table_rows": [
            ("Math load", "Shorter derivations, more intuition boxes and diagrams", "Maintains momentum without hiding mechanisms."),
            ("Lab structure", "More scaffolding, smaller TODO blocks, faster checkpoints", "Supports students who are still learning the tooling stack."),
            ("Assessment", "Frequent low-stakes artifacts plus one smaller capstone", "Reduces last-minute project collapse."),
            ("Discussion", "Reflection on debugging and system behavior", "Builds engineering judgment early."),
        ],
        "code": """# Undergraduate-course adaptation card.\nplan = {\n    \"formal_derivation_weeks\": 4,\n    \"guided_lab_weeks\": 10,\n    \"weekly_reflection\": True,\n    \"capstone_scope\": \"narrow simulator-first project\",\n}\nprint(plan)""",
        "output": "{'formal_derivation_weeks': 4, 'guided_lab_weeks': 10, 'weekly_reflection': True, 'capstone_scope': 'narrow simulator-first project'}",
        "output_interp": "The expected output should show what replaced theory load, not just that theory was reduced. Guided labs and reflection are the replacement mechanism.",
        "tools": "Jupyter, Colab, MuJoCo Playground, Gymnasium, LeRobot notebooks, GitHub Classroom",
        "practical": "This version of the course works best when every lab ends with a short explanation of what failed and what changed after debugging. That habit is more valuable than squeezing in one extra advanced topic superficially.",
        "frontier": "A live teaching question is how to introduce foundation models without letting them overshadow embodied fundamentals. Undergraduate courses need stronger anti-magic scaffolding than graduate seminars do.",
        "xref": '<a href="../../part-3-dynamics-control-and-state-estimation/index.html">Part III on control and estimation</a> and <a href="../../part-4-simulation-and-synthetic-data/index.html">Part IV on simulation</a>',
    },
    "60.3": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.3.html",
        "topic": "Two-semester sequence",
        "bridge": "A two-semester sequence is where the book can fully breathe. The first term can establish the physics, estimation, simulation, and policy-learning foundations; the second can move into language, world models, safety, and longer capstones without compressing everything into one overloaded arc.",
        "problem": "The course-design challenge is coherence across the handoff. Students should feel that the second term extends the same loop rather than starting a second disconnected subject.",
        "formula": r"Let semester one build foundation set $F$ and semester two build extension set $E$. The sequence works when prerequisite edges form a sparse DAG from $F$ to $E$, not a tangled graph that forces constant review of forgotten assumptions.",
        "intuition": "This is why the first semester should overinvest in frames, interfaces, data cards, and evaluation discipline. Those concepts quietly support everything interesting that happens later.",
        "algorithm_title": "Algorithm: Split the book across two terms",
        "algorithm_steps": [
            "Use term one for perception, dynamics, control, state estimation, simulation, RL, and imitation.",
            "End term one with a modest integrative project that proves students can close the loop.",
            "Open term two with a brief refresh, then add language, VLAs, planning, 3D representation, and deployment topics.",
            "Run a larger second-term capstone that can draw from both terms without re-teaching prerequisites.",
            "Keep one shared evidence schema across both semesters so artifacts remain comparable."
        ],
        "table_title": "Recommended Two-Term Split",
        "table_rows": [
            ("Term one", "Foundations, control, state estimation, simulation, RL, imitation", "Technical floor and first integrative project."),
            ("Interterm artifact", "Baseline system plus replay and postmortem", "Prevents term-two amnesia."),
            ("Term two", "Language, planning, world models, safety, deployment, frontier topics", "Advanced synthesis."),
            ("Final deliverable", "Research-grade capstone with proposal and defense", "Uses both halves of the sequence."),
        ],
        "code": """# Two-term sequence card.\nsequence = {\n    \"term_one_project\": \"simulator-based mobile manipulation baseline\",\n    \"term_two_project\": \"language-conditioned embodied capstone\",\n    \"shared_evidence_schema\": True,\n}\nprint(sequence)""",
        "output": "{'term_one_project': 'simulator-based mobile manipulation baseline', 'term_two_project': 'language-conditioned embodied capstone', 'shared_evidence_schema': True}",
        "output_interp": "The expected output should reveal continuity across terms. If the evidence schema changes between semesters, students will struggle to connect the advanced work back to the foundations.",
        "tools": "Same book stack plus course project repositories, CI, shared data cards, simulator presets",
        "practical": "The strongest two-term designs keep term-one artifacts alive as baselines for term two. That makes progress legible and reduces the temptation to discard hard-won infrastructure every semester.",
        "frontier": "A frontier teaching opportunity is to let term-two students reproduce or stress-test a current research claim using the infrastructure they built in term one. That is how the sequence becomes a research pipeline instead of two classes.",
        "xref": '<a href="../../part-5-imitation-learning-datasets-and-policy-learning/index.html">Part V</a> and <a href="../../part-8-world-models-model-based-rl-and-planning/index.html">Part VIII</a>',
    },
    "60.4": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.4.html",
        "topic": "Research-seminar track",
        "bridge": "The seminar version of the book should teach students how to read frontier embodied-AI claims skeptically without draining the subject of excitement. The seminar is where Chapter 58's frontier-watch discipline becomes a weekly habit.",
        "problem": "A seminar fails when it becomes a loose paper club. It succeeds when students repeatedly connect a claim to the system loop, identify the missing evidence, and propose a tractable replication or ablation.",
        "formula": r"Each seminar week can be modeled as $(p,a,q)$: one primary paper $p$, one artifact audit $a$, and one forward-looking question $q$. The trio keeps the discussion balanced between understanding, skepticism, and synthesis.",
        "intuition": "The audit is what changes the energy of the room. Students stop performing summary and start performing judgment once they must say which artifact would convince them.",
        "algorithm_title": "Algorithm: Run the book as a research seminar",
        "algorithm_steps": [
            "Choose one paper or system release that connects clearly to the current book chapters.",
            "Assign one student to explain the mechanism and another to audit the evidence.",
            "Discuss one missing experiment, one hidden assumption, and one teachable systems idea.",
            "End with a frontier-watch verdict: teach-now, replicate-now, or watch-only.",
            "Capture the verdict in a shared seminar ledger."
        ],
        "table_title": "Seminar Deliverables",
        "table_rows": [
            ("Primary reading", "Paper, release note, or benchmark report", "Anchors the week."),
            ("Artifact audit", "Claim, evidence, missing piece, replication priority", "Builds scientific skepticism."),
            ("Mini response", "One-page synthesis or stress test design", "Prevents passive attendance."),
            ("Ledger", "Semester-long frontier watchlist", "Accumulates judgment, not only notes."),
        ],
        "code": """# Seminar ledger item.\nitem = {\n    \"paper\": \"foundation policy for mobile manipulation\",\n    \"verdict\": \"replicate-now\",\n    \"missing_evidence\": \"independent evaluation on shifted embodiments\",\n    \"student_owner\": \"week_7_pair\",\n}\nprint(item)""",
        "output": "{'paper': 'foundation policy for mobile manipulation', 'verdict': 'replicate-now', 'missing_evidence': 'independent evaluation on shifted embodiments', 'student_owner': 'week_7_pair'}",
        "output_interp": "The expected output should be actionable. A seminar card that cannot lead to replication, deferral, or integration is only a summary note.",
        "tools": "Paper discussion sheets, issue trackers, reproducibility ledgers, shared notebooks, GitHub",
        "practical": "This format works especially well for graduate students who are already choosing research directions. It turns the seminar into a low-cost scouting engine for future capstones or theses.",
        "frontier": "The seminar frontier is methodological literacy: learning to distinguish a strong embodied-system claim from an attractive but under-supported demo. That skill transfers across every future subfield shift.",
        "xref": '<a href="../../part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.99.html">Section 58.99 on frontier watch</a> and <a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html">Chapter 52 on evaluation</a>',
    },
    "60.5": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.5.html",
        "topic": "Lab infrastructure and compute budgeting for instructors",
        "bridge": "This section turns course logistics into a first-class design topic. Embodied AI courses fail unnecessarily when infrastructure assumptions remain implicit, such as hidden GPU requirements, fragile installs, or labs that have no fallback path for students with weak hardware.",
        "problem": "The goal is not luxury compute, it is predictable compute. Instructors need a budgeting and fallback framework that keeps the course moving when a heavy job, a broken simulator, or a cloud quota limit appears in the middle of the semester.",
        "formula": r"For lab $i$, estimate total compute demand as $C_i = n_s(t_{cpu}+g_i t_{gpu}) + c_i t_{cloud}$, where $n_s$ is student count, $g_i$ is the fraction needing GPU, and $c_i$ is the fraction offloaded to cloud. The point is not exact accounting; it is seeing where bottlenecks can form before the assignment ships.",
        "intuition": "The budget model reveals which labs are fragile. A lab is risky when it requires most students to run long GPU jobs locally or when it has no cheap substitute that still teaches the mechanism.",
        "algorithm_title": "Algorithm: Design a resilient lab infrastructure plan",
        "algorithm_steps": [
            "Classify each lab as CPU-safe, local-GPU, or cloud-first before the term begins.",
            "Provide one maintained environment per class, such as a pinned Colab or container image.",
            "Publish fallback routes, including smaller models, shorter horizons, or prerecorded logs for analysis.",
            "Track cloud budget, queue times, and peak usage weeks alongside assignment release dates.",
            "Run one dry-run audit on fresh machines before assigning the lab."
        ],
        "table_title": "Infrastructure Planning Grid",
        "table_rows": [
            ("Environment", "Pinned notebooks, containers, simulator presets", "Prevents environment drift."),
            ("Compute tier", "CPU, local GPU, or cloud offload", "Makes hidden hardware assumptions visible."),
            ("Fallback path", "Smaller model, shorter run, or analysis-only mode", "Keeps learning moving during outages."),
            ("Support artifact", "Install log, runtime expectation, and dry-run screenshot", "Reduces avoidable support load."),
        ],
        "code": """# Compute-budget card for one lab.\nbudget = {\n    \"lab\": \"diffusion-policy imitation lab\",\n    \"students\": 32,\n    \"local_gpu_fraction\": 0.25,\n    \"cloud_budget_usd\": 48,\n    \"fallback\": \"short-horizon pretrained checkpoint analysis\",\n}\nprint(budget)""",
        "output": "{'lab': 'diffusion-policy imitation lab', 'students': 32, 'local_gpu_fraction': 0.25, 'cloud_budget_usd': 48, 'fallback': 'short-horizon pretrained checkpoint analysis'}",
        "output_interp": "The expected output should let an instructor decide whether the lab is safe to assign. If no fallback path is visible, the lab is still operationally fragile.",
        "tools": "Colab, VS Code dev containers, Docker, MuJoCo Playground, cloud notebooks, GitHub Classroom, CI",
        "practical": "A practical rule is to make the most expensive labs optional extensions unless they teach a core mechanism that cannot be seen any other way. Students remember the concept, not the heroic setup time.",
        "frontier": "The frontier teaching challenge is that embodied AI increasingly depends on heterogeneous infrastructure, from local simulators to cloud inference to robot teleoperation. Good course design must absorb that complexity without hiding it.",
        "xref": '<a href="../../part-4-simulation-and-synthetic-data/module-11-simulator-landscape-mujoco-isaac-lab-genesis-newton-drake-and-gazebo/index.html">Chapter 11 on simulators</a> and <a href="../../part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/index.html">Chapter 59 on capstones</a>',
    },
    "60.6": {
        "path": ROOT / "part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.6.html",
        "topic": "Assessment, rubrics, and academic-integrity notes for code assignments",
        "bridge": "Assessment design determines what students actually learn. In embodied AI, grading only a final score or a polished video pushes students toward opaque hacks, while grading the evidence trail pushes them toward reproducible systems thinking.",
        "problem": "The section therefore separates task framing, implementation, evidence quality, failure analysis, and reflection. Academic integrity is handled through artifact transparency and oral or written explanation checks rather than through brittle suspicion alone.",
        "formula": r"A rubric can be written as $G = w_t T + w_i I + w_e E + w_f F + w_r R$, where $T$ is task framing, $I$ implementation, $E$ evidence quality, $F$ failure analysis, and $R$ reflection. Keeping the components separate prevents students from hiding weak understanding behind one high metric.",
        "intuition": "The failure-analysis term is especially important. Once it carries real weight, students gain incentive to document debugging honestly instead of treating errors as something to hide.",
        "algorithm_title": "Algorithm: Grade embodied-AI assignments for understanding",
        "algorithm_steps": [
            "Publish the rubric before the assignment starts, including evidence and reflection expectations.",
            "Require one common artifact bundle: code, config, metrics, replay, and a failure note.",
            "Sample oral or written spot checks that ask students to explain one design choice and one failure case.",
            "Permit assistance tools with disclosure, while grading the student's understanding of the resulting system.",
            "Penalize missing evidence and unexplainable code more heavily than modest performance gaps."
        ],
        "table_title": "Recommended Rubric Components",
        "table_rows": [
            ("Task framing", "Clear contract, assumptions, and success definition", "Shows whether the student understood the problem."),
            ("Implementation", "Runnable code and correct interfaces", "Checks engineering execution."),
            ("Evidence", "Construct-matched metrics, replay, and logs", "Rewards reproducibility and honesty."),
            ("Failure analysis", "Specific diagnosis and next-step proposal", "Builds research maturity."),
        ],
        "code": """# Example weighted rubric card.\nrubric = {\n    \"task_framing\": 0.20,\n    \"implementation\": 0.30,\n    \"evidence\": 0.25,\n    \"failure_analysis\": 0.15,\n    \"reflection\": 0.10,\n}\nprint(rubric)""",
        "output": "{'task_framing': 0.2, 'implementation': 0.3, 'evidence': 0.25, 'failure_analysis': 0.15, 'reflection': 0.1}",
        "output_interp": "The expected output should reveal assessment priorities immediately. A rubric with no explicit evidence or failure-analysis weight will teach the wrong habits.",
        "tools": "GitHub Classroom, nbgrader, Gradescope-style rubrics, Jupyter, replay exporters, CI",
        "practical": "A strong integrity policy allows disclosed use of coding assistants but requires students to defend the produced system. That shifts the course from policing text authorship to evaluating actual engineering understanding.",
        "frontier": "The frontier question is how assessment changes when students can obtain increasingly capable generated code. Embodied AI may be unusually resilient here because replay, failure explanation, and system integration remain hard to fake convincingly.",
        "xref": '<a href="../../part-11-evaluation-safety-robustness-and-deployment/module-52-evaluating-embodied-systems/index.html">Chapter 52 on evaluation</a> and <a href="../../part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/index.html">Chapter 59 on capstone deliverables</a>',
    },
})


def build_html(section_id: str, data: dict) -> str:
    rows = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in data["table_rows"]
    )
    algo_items = "\n".join(f"<li>{item}</li>" for item in data["algorithm_steps"])
    caption = f"Code Fragment {section_id}.A summarizes the topic-specific evidence card for {data['topic'].lower()}."
    return f"""
<section class="part-xii-agent-enrichment">
<h2>Topic-Native Deepening</h2>
<p>{data['bridge']}</p>
<p>{data['problem']}</p>
<div class="callout key-insight"><div class="callout-title">Why This Section Matters</div><p>{data['topic']} becomes teachable once the student can state the operative variables, the decision boundary, and the evidence artifact. The section should therefore be read together with {data['xref']}, where the same loop is developed from adjacent angles.</p></div>
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>{data['formula']}</p></div>
<p>{data['intuition']}</p>
<div class="callout algorithm"><div class="callout-title">{data['algorithm_title']}</div><ol>
{algo_items}
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">{data['table_title']}</div><table><thead><tr><th>Dimension</th><th>What To Specify</th><th>Why It Matters</th></tr></thead><tbody>
{rows}
</tbody></table></div>
<pre><code class="language-python">{data['code']}</code></pre>
<div class="code-output"><pre>{data['output']}</pre></div>
<div class="code-caption">{caption}</div>
<p>{data['output_interp']}</p>
<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>After the from-scratch contract is clear, the practical route uses <strong>{data['tools']}</strong>. The payoff is that standard interfaces, logging, batching, and replay support move from ad hoc glue code into maintained infrastructure, while the evidence schema stays the same.</p></div>
<div class="callout practical-example"><div class="callout-title">Project Or Teaching Use</div><p>{data['practical']}</p></div>
<div class="callout research-frontier"><div class="callout-title">Research Frontier</div><p>{data['frontier']}</p></div>
<div class="callout self-check"><div class="callout-title">Expected Output Interpretation</div><p>Before leaving this section, the reader should be able to explain what the printed artifact proves, what it leaves uncertain, and what the next experiment would change. If that explanation is missing, the section has not yet become an executable research or teaching plan.</p></div>
</section>
""".strip()


def replace_enrichment(path: Path, html: str) -> None:
    text = path.read_text(encoding="utf-8")
    if '<section class="part-xii-agent-enrichment">' in text:
        start = text.index('<section class="part-xii-agent-enrichment">')
        end = text.index('<section class="bibliography">', start)
        updated = text[:start] + html + "\n" + text[end:]
    else:
        marker = '<section class="bibliography">'
        insert_at = text.index(marker)
        updated = text[:insert_at] + html + "\n" + text[insert_at:]
    path.write_text(updated, encoding="utf-8")


def main():
    for section_id, data in SECTIONS.items():
        replace_enrichment(data["path"], build_html(section_id, data))
        print(f"updated {section_id} -> {data['path'].relative_to(ROOT)}")


if __name__ == "__main__":
    main()
