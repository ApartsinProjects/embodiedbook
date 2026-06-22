from pathlib import Path
import re

ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


REPLACEMENTS = {
    "part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.1.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$J(\Pi)=\mathbb E\!\left[\sum_{t=0}^{T-1}\gamma^t r(s_t,a_t)\right],\quad \Pi=\{\pi_1,\ldots,\pi_n\},\quad a_t^{\mathrm{joint}}=[a_t^1,\ldots,a_t^n]$</p><p>Choosing one agent versus many is a factorization decision. A centralized policy $\pi(a^{\mathrm{joint}}\mid o)$ can coordinate globally but grows with the joint action space. A decentralized family $\{\pi_i(a_i\mid o_i,m_i)\}$ scales better and matches physical deployment, but it only works if local observations and messages preserve the action-critical information.</p></div>
<div class="callout algorithm"><div class="callout-title">Centralized-versus-decentralized decomposition audit</div><ol>
<li>Write the task graph: bodies, actuators, communication links, and shared bottlenecks.</li>
<li>Measure whether the joint action is low-rank, for example by checking whether a small message or latent variable predicts most coordination choices.</li>
<li>Train or hand-code one centralized baseline and one decentralized baseline on the same environment seeds.</li>
<li>Compare task return, message rate, wall-clock latency, and graceful degradation when one agent is delayed or removed.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">When One Controller Should Split Into Many</div><table><thead><tr><th>Question</th><th>Centralized Answer</th><th>Multi-Agent Answer</th></tr></thead><tbody>
<tr><td>Who sees the full scene?</td><td>One planner fuses all observations.</td><td>Each robot sees a partial slice and may share summaries.</td></tr>
<tr><td>Where does latency hurt?</td><td>At the single planner and network uplink.</td><td>At local message passing and arbitration points.</td></tr>
<tr><td>What failure is easiest to miss?</td><td>Single point of failure in the planner.</td><td>Hidden dependence on one informative teammate.</td></tr>
<tr><td>What metric matters beyond reward?</td><td>End-to-end compute and recovery time.</td><td>Partner substitution, coordination cost, and loss after dropout.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Audit whether decentralized execution preserves the key coordination decision.
# Expected: coordination is robust only if the summary message tracks the bottleneck.
episodes = [
    {"planner": "centralized", "success": 0.96, "latency_ms": 82, "dropout_success": 0.94},
    {"planner": "decentralized", "success": 0.92, "latency_ms": 24, "dropout_success": 0.61},
]

for row in episodes:
    gap = round(row["success"] - row["dropout_success"], 2)
    print(row["planner"], "coordination_gap", gap, "latency_ms", row["latency_ms"])</code></pre>
<div class="code-output"><pre>centralized coordination_gap 0.02 latency_ms 82
decentralized coordination_gap 0.31 latency_ms 24</pre></div>
<div class="code-caption">Code Fragment 49.1.T compares nominal performance with partner-dropout performance to reveal whether the team decomposition is robust or only fast.</div>
<p>The output is the interpretation step, not decoration. The decentralized system is faster, but its coordination gap is much larger, which means the factorization discarded action-critical context. In practice this suggests a hybrid design, such as centralized training with decentralized execution, a shared world model, or a tighter intent message.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>A one-versus-many design fails when a team is declared modular even though one robot silently carries the global plan. The diagnostic is an ablation that removes or delays that robot and checks whether the others can still produce coherent joint behavior.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.2.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$u_i(a_i,a_{-i},s)=r_i(s,a_i,a_{-i})-\lambda\,c(m_i),\quad m_i\in\mathcal M,\quad \pi_i(a_i,m_i\mid o_i)$</p><p>Communication is worthwhile only when the message changes a joint action enough to justify its cost. Cooperation, competition, and communication are therefore tied by information economics: agents trade bandwidth, delay, and observability against the value of coordinated behavior or strategic concealment.</p></div>
<div class="callout algorithm"><div class="callout-title">Value-of-message audit</div><ol>
<li>Define the game outcome with zero messages, bounded messages, and unrestricted broadcast.</li>
<li>Measure the marginal improvement in return per transmitted bit or per message slot.</li>
<li>Stress the system with delayed, dropped, and adversarially corrupted messages.</li>
<li>Separate cooperative gains from exploitative gains by reporting both team and per-agent utility.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Communication Design Questions</div><table><thead><tr><th>Choice</th><th>What It Buys</th><th>What It Risks</th></tr></thead><tbody>
<tr><td>Broadcast state</td><td>High observability, simple debugging.</td><td>Bandwidth blowup and stale data.</td></tr>
<tr><td>Intent-only messages</td><td>Small message budget, faster arbitration.</td><td>Ambiguity under changing goals.</td></tr>
<tr><td>Learned emergent code</td><td>Compact signaling for repetitive tasks.</td><td>Opaque semantics and poor partner transfer.</td></tr>
<tr><td>No communication</td><td>Strong robustness and deployment simplicity.</td><td>Missed coordination opportunities and local deadlocks.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Compare team gain against communication cost.
results = [
    {"policy": "silent", "team_return": 78, "messages": 0},
    {"policy": "intent_bit", "team_return": 96, "messages": 12},
    {"policy": "full_broadcast", "team_return": 99, "messages": 140},
]

baseline = results[0]["team_return"]
for row in results[1:]:
    gain = row["team_return"] - baseline
    gain_per_msg = round(gain / row["messages"], 3)
    print(row["policy"], "gain", gain, "gain_per_message", gain_per_msg)</code></pre>
<div class="code-output"><pre>intent_bit gain 18 gain_per_message 1.5
full_broadcast gain 21 gain_per_message 0.15</pre></div>
<div class="code-caption">Code Fragment 49.2.T shows that the best communication policy is often the one with the best return-per-message ratio, not the largest raw score.</div>
<p>This trace says the extra 128 broadcasts buy only three additional reward points. That is often a poor systems trade, especially on real robots where messages contend with state estimation, safety traffic, and network jitter. The compact intent signal is therefore the more credible embodiment choice.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>A communication scheme fails when it wins only under perfect synchronization. Always rerun the task with bounded bandwidth, clock skew, and packet loss, then check whether the same coordination policy still chooses sensible actions.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.3.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$\min_{x_{ij}\in\{0,1\}}\sum_{i=1}^N\sum_{j=1}^M c_{ij}x_{ij},\quad \sum_j x_{ij}\le 1,\quad \sum_i x_{ij}=1$</p><p>Shared perception and task allocation couple estimation with combinatorial decision making. The team first decides what the world contains and where uncertainty lives, then it solves who should do which job given travel time, skill compatibility, battery budget, and collision constraints.</p></div>
<div class="callout algorithm"><div class="callout-title">Map-fusion and assignment pipeline</div><ol>
<li>Fuse detections into a shared object graph with timestamps, confidence, and frame transforms.</li>
<li>Prune stale observations and reconcile duplicates before any task is assigned.</li>
<li>Build an agent-task cost matrix from reachability, travel time, and manipulation affordance.</li>
<li>Solve the assignment, then replan whenever the fused map changes beyond a threshold.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Allocation Inputs That Change Team Behavior</div><table><thead><tr><th>Input</th><th>Typical Source</th><th>Why It Must Be Logged</th></tr></thead><tbody>
<tr><td>Pose confidence</td><td>Multi-view perception stack</td><td>Low confidence often explains bad task claims better than bad control.</td></tr>
<tr><td>Travel-time estimate</td><td>Navigation map and planner</td><td>Prevents assigning the closest-looking robot instead of the fastest one.</td></tr>
<tr><td>Skill label</td><td>Manipulator or tool capability model</td><td>Explains why some jobs are infeasible, not merely low reward.</td></tr>
<tr><td>Reassignment count</td><td>Execution monitor</td><td>Reveals whether the allocator is stable under scene change.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># A tiny task-allocation audit using a cost matrix.
agents = ["base_bot", "arm_bot"]
tasks = ["inspect_bin", "pick_box"]
cost = {
    ("base_bot", "inspect_bin"): 2.0,
    ("base_bot", "pick_box"): 7.5,
    ("arm_bot", "inspect_bin"): 4.0,
    ("arm_bot", "pick_box"): 1.5,
}

assignment = {"base_bot": "inspect_bin", "arm_bot": "pick_box"}
total = sum(cost[(agent, task)] for agent, task in assignment.items())
print(assignment)
print("total_cost", total)</code></pre>
<div class="code-output"><pre>{'base_bot': 'inspect_bin', 'arm_bot': 'pick_box'}
total_cost 3.5</pre></div>
<div class="code-caption">Code Fragment 49.3.T turns fused perception into an explicit assignment artifact that can be audited after the run.</div>
<p>The useful part is the explicit cost decomposition. If the team later fails, you can ask whether the wrong robot was assigned because the object pose was wrong, the travel-time estimate was stale, or the capability model claimed a skill the robot did not really have.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Allocation fails when the shared map is treated as ground truth. Always perturb timestamps, duplicate one detection, and move one target object after assignment to test whether the fusion-and-assignment loop can recover without thrashing.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.4.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$Q_i(o_i,a_i,h_i;\phi_i),\quad \nabla_\theta J(\theta)=\mathbb E\!\left[\nabla_\theta \log \pi_\theta(a\mid o)\,\hat A(o,a)\right]$</p><p>Multi-agent RL adds three coupled difficulties beyond single-agent RL: non-stationarity from other learning agents, credit assignment for shared outcomes, and partner generalization when teammates or opponents change. PettingZoo helps expose these issues because it forces the environment API to name who acts when and what each agent can observe.</p></div>
<div class="callout algorithm"><div class="callout-title">CTDE training and partner-holdout evaluation</div><ol>
<li>Choose an environment API, AEC when turn order matters, parallel when actions are simultaneous.</li>
<li>Train with centralized critics or value decomposition while keeping decentralized policies executable on each robot.</li>
<li>Evaluate on same-partner, held-out-partner, and changed-goal panels with fixed seeds.</li>
<li>Report per-agent reward, collision rate, intervention count, and policy entropy, not only team return.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">PettingZoo-Centered MARL Decisions</div><table><thead><tr><th>Decision</th><th>Good Default</th><th>Audit Question</th></tr></thead><tbody>
<tr><td>AEC vs parallel API</td><td>AEC for negotiation or speaking turns.</td><td>Does action order change the optimal policy?</td></tr>
<tr><td>Shared vs separate replay</td><td>Shared replay with agent identifiers.</td><td>Can the critic disambiguate who caused the reward?</td></tr>
<tr><td>Team vs individual reward</td><td>Mix sparse team reward with local shaping.</td><td>Does one agent exploit shaping while harming the team?</td></tr>
<tr><td>Partner sampling</td><td>Curriculum over diverse partners.</td><td>Does performance collapse outside the training clique?</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Same policy family, two evaluation panels.
scores = {
    "same_partner": {"team_return": 112, "collisions": 1, "entropy": 0.42},
    "held_out_partner": {"team_return": 71, "collisions": 6, "entropy": 0.11},
}

for panel, stats in scores.items():
    print(panel, stats["team_return"], stats["collisions"], stats["entropy"])</code></pre>
<div class="code-output"><pre>same_partner 112 1 0.42
held_out_partner 71 6 0.11</pre></div>
<div class="code-caption">Code Fragment 49.4.T exposes partner overfitting by comparing the same learned policy on familiar and held-out teammates.</div>
<p>The held-out partner panel is the important one. The lower entropy and higher collision count show that the policy is not merely weaker, it is brittle and overconfident. That typically motivates stronger partner randomization, explicit communication channels, or an opponent-modeling auxiliary loss.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>A MARL result fails when it reports one high team score without showing partner generalization, intervention, or safety metrics. In embodied settings that usually means the policy learned one narrow coordination script rather than a reusable teamwork skill.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.5.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$v_i^{t+1}=w v_i^t + c_1(f_i-x_i^t)+c_2(n_i-x_i^t),\quad \Phi=\frac{1}{N}\left\|\sum_{i=1}^N \frac{v_i}{\|v_i\|}\right\|$</p><p>Swarm behavior emerges from local update rules, but evaluation must stay global. Coverage, connectivity, collision rate, evacuation time, and resilience to agent dropout are the quantities that determine whether an emergent pattern is useful or merely visually interesting.</p></div>
<div class="callout algorithm"><div class="callout-title">Local-rule robustness sweep</div><ol>
<li>Specify the local neighborhood, communication radius, and update frequency.</li>
<li>Run a density sweep, an obstacle-layout sweep, and an agent-dropout sweep.</li>
<li>Measure order parameters such as alignment, dispersion, and connected-component count together with the task metric.</li>
<li>Check whether the same rule set remains safe when one local assumption is violated.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Evaluating Emergent Team Behavior</div><table><thead><tr><th>Metric</th><th>Why It Matters</th><th>Typical Failure Signal</th></tr></thead><tbody>
<tr><td>Coverage ratio</td><td>Shows whether the swarm reaches the workspace.</td><td>High clustering leaves blind regions untouched.</td></tr>
<tr><td>Alignment score</td><td>Tracks coherent movement when motion consensus matters.</td><td>Over-alignment can create congestion at exits.</td></tr>
<tr><td>Connected components</td><td>Tests whether communication stays intact.</td><td>Fragmentation hides isolated agents from the controller.</td></tr>
<tr><td>Recovery time after dropout</td><td>Measures resilience rather than appearance.</td><td>Emergence disappears when one or two agents fail.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># A compact emergent-behavior audit.
panels = [
    {"density": "low", "coverage": 0.74, "collisions": 0, "recovery_s": 1.9},
    {"density": "medium", "coverage": 0.93, "collisions": 2, "recovery_s": 2.7},
    {"density": "high", "coverage": 0.88, "collisions": 11, "recovery_s": 7.8},
]

for row in panels:
    print(row["density"], row["coverage"], row["collisions"], row["recovery_s"])</code></pre>
<div class="code-output"><pre>low 0.74 0 1.9
medium 0.93 2 2.7
high 0.88 11 7.8</pre></div>
<div class="code-caption">Code Fragment 49.5.T shows why emergent behavior must be judged on a density sweep, not on one impressive trajectory video.</div>
<p>The medium-density panel is the best regime here. High density looks more collective, but the collision count and recovery time reveal that the same local rule becomes unsafe and sticky under congestion. That is the kind of result that should drive controller redesign or spacing constraints.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Swarm evaluation fails when emergence is inferred from one visualization. Always report whether the pattern survives changed density, communication radius, and body dropout, otherwise the claimed collective intelligence may be a narrow simulator artifact.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.1.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$J(\tau)=\sum_t \ell_{\mathrm{task}}(x_t,u_t)+\lambda_1 \ell_{\mathrm{prox}}(x_t,h_t)+\lambda_2 \ell_{\mathrm{legibility}}(u_t)$</p><p>A robot among humans optimizes a multi-objective cost. It must achieve the task while staying outside protected interpersonal zones, remaining legible about what it will do next, and preserving a human's ability to intervene. This is why HRI lives at the boundary between control, perception, and human factors.</p></div>
<div class="callout algorithm"><div class="callout-title">Human-aware hallway audit</div><ol>
<li>Represent each nearby person with position, velocity, field of view, and personal-space radius.</li>
<li>Generate a nominal path, then score it for task efficiency, clearance, and intent legibility.</li>
<li>Trigger a conservative fallback whenever a person hesitates, steps into the path, or occludes the robot.</li>
<li>Log both robot metrics and human-facing metrics such as intervention, startle events, and comfort rating.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">What Changes When Humans Enter The Loop</div><table><thead><tr><th>Signal</th><th>Pure Navigation Reading</th><th>HRI Reading</th></tr></thead><tbody>
<tr><td>Minimum distance</td><td>Collision proxy</td><td>Comfort and perceived respect for space</td></tr>
<tr><td>Stop duration</td><td>Delay cost</td><td>May increase trust if the pause is legible</td></tr>
<tr><td>Path curvature</td><td>Control effort</td><td>Communicates yielding or asserting right of way</td></tr>
<tr><td>Operator takeover</td><td>Failure count</td><td>Evidence that the robot was not understandable enough</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Compare a fast path with a human-aware path.
paths = [
    {"planner": "shortest_path", "travel_s": 11.2, "min_clearance_m": 0.34, "comfort": 2.1},
    {"planner": "human_aware", "travel_s": 12.4, "min_clearance_m": 0.79, "comfort": 4.5},
]

for row in paths:
    print(row["planner"], row["travel_s"], row["min_clearance_m"], row["comfort"])</code></pre>
<div class="code-output"><pre>shortest_path 11.2 0.34 2.1
human_aware 12.4 0.79 4.5</pre></div>
<div class="code-caption">Code Fragment 50.1.T shows the core HRI trade: a slightly slower route can be much safer and more acceptable to nearby people.</div>
<p>The extra 1.2 seconds is easy to justify because the human-aware planner nearly doubles clearance and strongly improves comfort. This is the kind of output interpretation readers need to practice: not every efficiency loss is a systems loss when the deployment context includes real people.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Hallway interaction fails when the planner is tuned only on distance and time. Run occlusion, doorway, and sudden-crossing cases, then inspect whether the robot remains legible before the person has to guess or flee.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.2.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$p(g,z\mid w,o)\propto p(w\mid g)\,p(g\mid z,o)\,p(z\mid o)$</p><p>Natural-language interaction and social navigation require a grounding model, not merely a language model. The robot must infer a goal $g$, a social constraint set $z$, and the visual evidence $o$ that makes the utterance actionable in the current scene.</p></div>
<div class="callout algorithm"><div class="callout-title">Instruction grounding under social constraints</div><ol>
<li>Parse the utterance into action, object, destination, and soft social constraints such as "quietly" or "do not block the nurse".</li>
<li>Bind noun phrases to scene entities and reject bindings whose geometry or affordances are impossible.</li>
<li>Translate social constraints into path or timing costs, then plan.</li>
<li>Ask a clarification question when multiple bindings remain or when the safe action set is empty.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Grounding Errors That Matter In The Hallway</div><table><thead><tr><th>Error Type</th><th>Example</th><th>Corrective Action</th></tr></thead><tbody>
<tr><td>Referent ambiguity</td><td>"Take this to the room" with two trays nearby.</td><td>Ask which tray or which room.</td></tr>
<tr><td>Affordance mismatch</td><td>Object named correctly but impossible to grasp.</td><td>Switch to a tool or ask for help.</td></tr>
<tr><td>Social constraint omission</td><td>Shortest path cuts through a waiting group.</td><td>Replan with a human-space penalty.</td></tr>
<tr><td>Temporal mismatch</td><td>Instruction assumes immediate action during a busy crossing.</td><td>Delay execution and announce intent.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Choose between execution and clarification.
candidates = [
    {"goal": "deliver tray to room_12", "prob": 0.52, "safe": True},
    {"goal": "deliver tray to room_14", "prob": 0.44, "safe": True},
]

margin = candidates[0]["prob"] - candidates[1]["prob"]
decision = "clarify" if margin < 0.15 else "execute"
print("margin", round(margin, 2), "decision", decision)</code></pre>
<div class="code-output"><pre>margin 0.08 decision clarify</pre></div>
<div class="code-caption">Code Fragment 50.2.T shows that the correct HRI action may be to ask a question instead of pretending the language grounding is certain enough.</div>
<p>The small probability margin is the important number. In a social setting the cost of a wrong confident action is usually larger than the cost of one short clarification question, especially when the robot would otherwise navigate into busy shared space.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Language-grounded navigation fails when the text parser is evaluated separately from the motion planner. Always test end-to-end cases where words change the path shape, stop condition, or social exclusion zone.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.3.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$b_{t+1}(i)\propto p(o_t\mid i)\,b_t(i),\quad \mathrm{trust\ error}=|\hat p_{\mathrm{success}}-p_{\mathrm{success}}|$</p><p>Intent recognition is a sequential inference problem. Trust calibration is an estimation problem layered on top: does the human's belief about the robot's capability match the robot's actual conditional success rate in the current context?</p></div>
<div class="callout algorithm"><div class="callout-title">Intent inference and trust-calibration loop</div><ol>
<li>Track a belief over human intents using pose, gaze, dialogue, and task history.</li>
<li>Estimate robot capability under the inferred intent and current scene uncertainty.</li>
<li>Expose uncertainty through the interface, for example with confidence, delay, or a help request.</li>
<li>Update trust models after interventions, surprises, and successful recoveries.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Calibrated Versus Miscalibrated Trust</div><table><thead><tr><th>Case</th><th>Observed Behavior</th><th>Why It Is Dangerous</th></tr></thead><tbody>
<tr><td>Overtrust</td><td>Human stops monitoring despite low robot confidence.</td><td>Late intervention increases harm radius.</td></tr>
<tr><td>Undertrust</td><td>Human constantly overrides competent behavior.</td><td>System becomes slow and fatiguing.</td></tr>
<tr><td>Context drift</td><td>Old reliability estimate reused in a new environment.</td><td>Trust lags behind actual capability.</td></tr>
<tr><td>Hidden uncertainty</td><td>Robot acts crisp while its belief is diffuse.</td><td>People infer competence that does not exist.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Compare displayed confidence with actual success.
episodes = [
    {"displayed_conf": 0.9, "actual_success": 0},
    {"displayed_conf": 0.6, "actual_success": 1},
    {"displayed_conf": 0.7, "actual_success": 1},
]

calibration_error = sum(abs(row["displayed_conf"] - row["actual_success"]) for row in episodes) / len(episodes)
print("mean_calibration_error", round(calibration_error, 2))</code></pre>
<div class="code-output"><pre>mean_calibration_error 0.53</pre></div>
<div class="code-caption">Code Fragment 50.3.T measures trust calibration by comparing what the interface suggests with what the robot actually achieves.</div>
<p>A calibration error above 0.5 is severe. The robot is not just sometimes wrong, it is systematically teaching the user the wrong lesson about when to rely on it. That is exactly the condition under which overtrust and abrupt interventions start to dominate the interaction.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Intent and trust systems fail when they infer what the human wants but never expose how uncertain they are. Evaluate whether users change their intervention pattern after the robot communicates uncertainty, not only whether intent labels look accurate offline.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.4.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$e_t=\operatorname{arg\,topk}_{k}\, \Delta V_k,\quad \Delta V_k = V(s_t)-V(s_t \setminus \text{factor}_k)$</p><p>Explainable robot behavior means selecting which internal factors actually changed the decision. A useful explanation is sparse, causally tied to the chosen action, and matched to the user's horizon: immediate motion, local obstacle, or higher-level task reason.</p></div>
<div class="callout algorithm"><div class="callout-title">Counterfactual event-trace explanation</div><ol>
<li>Log the policy input, selected action, safety checks, and active planner constraints.</li>
<li>Compute which factors most changed the action score or feasibility set.</li>
<li>Render the explanation at the same abstraction level as the user's question.</li>
<li>Verify usefulness by measuring whether the explanation changes the next human decision.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Good Robot Explanations</div><table><thead><tr><th>Form</th><th>Useful When</th><th>Weakness</th></tr></thead><tbody>
<tr><td>Rule-based event trace</td><td>Safety stop or mode switch happened.</td><td>Can miss learned-policy nuance.</td></tr>
<tr><td>Counterfactual statement</td><td>User asks "why not that way?"</td><td>Needs a faithful local model.</td></tr>
<tr><td>Saliency overlay</td><td>Visual attention matters.</td><td>Often descriptive, not causal.</td></tr>
<tr><td>Task-level summary</td><td>Longer collaborative workflows.</td><td>May hide the immediate trigger.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Pick the factors that most changed the stop decision.
delta = {"person_in_crosswalk": 0.62, "wet_floor_zone": 0.18, "shorter_path": -0.07}
explanation = sorted(delta.items(), key=lambda item: abs(item[1]), reverse=True)[:2]
print(explanation)</code></pre>
<div class="code-output"><pre>[('person_in_crosswalk', 0.62), ('wet_floor_zone', 0.18)]</pre></div>
<div class="code-caption">Code Fragment 50.4.T produces a minimal explanation set: the factors that most changed the chosen behavior.</div>
<p>The ranking matters because it keeps the explanation actionable. A human hearing "I stopped because a person entered the crosswalk and the floor zone narrowed my alternatives" can decide whether to wait, redirect the robot, or clear the path. A heatmap alone would not support that decision.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>An explanation system fails when it explains the model instead of the robot's action. Ask whether the explanation predicts the next behavior change under a counterfactual scene edit; if not, it is probably decorative rather than operational.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.5.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$u_t=\alpha_t u_t^{\mathrm{human}} + (1-\alpha_t)u_t^{\mathrm{robot}},\quad \alpha_t=f(\sigma_t,\rho_t,\kappa_t)$</p><p>Shared autonomy is an authority-allocation problem. The blending weight $\alpha_t$ should depend on human confidence, robot uncertainty, and risk. Good systems vary authority over time instead of freezing the human and robot into one static control split.</p></div>
<div class="callout algorithm"><div class="callout-title">Dynamic authority arbitration</div><ol>
<li>Estimate robot uncertainty $\sigma_t$, risk $\rho_t$, and operator workload $\kappa_t$.</li>
<li>Blend commands only inside a safety envelope; outside it, trigger clarification or stop modes.</li>
<li>Log who had authority at each timestep and why the mode changed.</li>
<li>Evaluate task success together with takeover rate, recovery speed, and operator fatigue.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Shared-Autonomy Control Modes</div><table><thead><tr><th>Mode</th><th>Who Leads</th><th>When To Use</th></tr></thead><tbody>
<tr><td>Manual</td><td>Human</td><td>Novel scene, unreliable autonomy, or user preference.</td></tr>
<tr><td>Assistive</td><td>Human with robot filtering</td><td>High-rate motor task with low-level hazards.</td></tr>
<tr><td>Supervisory</td><td>Robot with human veto</td><td>Routine operation with rare but costly edge cases.</td></tr>
<tr><td>Protective override</td><td>Safety controller</td><td>Constraint violation or imminent collision.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Blend authority based on uncertainty and risk.
states = [
    {"uncertainty": 0.15, "risk": 0.20, "alpha_human": 0.25},
    {"uncertainty": 0.55, "risk": 0.80, "alpha_human": 0.90},
]

for state in states:
    mode = "assistive" if state["alpha_human"] < 0.5 else "human_led"
    print(mode, state["alpha_human"], state["uncertainty"], state["risk"])</code></pre>
<div class="code-output"><pre>assistive 0.25 0.15 0.2
human_led 0.9 0.55 0.8</pre></div>
<div class="code-caption">Code Fragment 50.5.T shows that authority should migrate toward the human when uncertainty and risk rise, not stay fixed.</div>
<p>The second line is the crucial one. The same interface that feels efficient in a routine scene becomes unsafe in a high-risk scene unless control authority shifts. Readers should connect this directly to interface design, logging, and study design, not treat it as a purely control-theoretic detail.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Shared autonomy fails when the robot blends commands smoothly but does not tell the human when authority changed. Always test surprise takeovers and delayed interventions, because trust collapses when people cannot predict who is currently in charge.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.6.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$\min_\pi \mathbb E[\ell_{\mathrm{task}}] \quad \text{subject to} \quad \mathbb E[\ell_{\mathrm{privacy}}]\le \epsilon_1,\ \mathbb E[\ell_{\mathrm{harm}}]\le \epsilon_2,\ \mathbb E[\ell_{\mathrm{exclusion}}]\le \epsilon_3$</p><p>Ethical concerns become operational when they are translated into constraints, audit artifacts, and escalation policies. Embodied systems can cause physical, social, and informational harm at the same time, which is why ethics has to enter during design rather than after deployment.</p></div>
<div class="callout algorithm"><div class="callout-title">Embodied-AI ethics review loop</div><ol>
<li>List stakeholders, data types, control modes, and plausible harm channels.</li>
<li>Map each harm channel to a measurable proxy and an owner who must respond when it spikes.</li>
<li>Instrument the system to log consent state, intervention, privacy-relevant events, and exclusion cases.</li>
<li>Block launch when a critical risk lacks a mitigation, rollback, or disclosure path.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Ethics Risks That Must Reach The Design Spec</div><table><thead><tr><th>Risk</th><th>Design Lever</th><th>Evidence Artifact</th></tr></thead><tbody>
<tr><td>Privacy leakage</td><td>On-device processing, retention limits, masking.</td><td>Data-flow map and deletion log.</td></tr>
<tr><td>Accessibility exclusion</td><td>Alternative interfaces, multimodal cues.</td><td>User-group coverage matrix.</td></tr>
<tr><td>Physical harm</td><td>Speed caps, force limits, stop logic.</td><td>Hazard analysis and incident replay.</td></tr>
<tr><td>Manipulative persuasion</td><td>Disclosure and consent controls.</td><td>Interaction transcript audit.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># A minimal risk register summary.
risk_register = [
    {"risk": "privacy", "severity": "high", "mitigation": "camera masking", "owner": "deployment_lead"},
    {"risk": "startle_near_children", "severity": "medium", "mitigation": "speed cap and audio cue", "owner": "controls_lead"},
]

for item in risk_register:
    print(item["risk"], item["severity"], item["owner"])</code></pre>
<div class="code-output"><pre>privacy high deployment_lead
startle_near_children medium controls_lead</pre></div>
<div class="code-caption">Code Fragment 50.6.T shows the minimum ethical artifact that can actually change a deployment decision: a risk, a mitigation, and an accountable owner.</div>
<p>This output matters because it creates accountability. An ethics paragraph without a named owner is not a control surface. A serious embodied deployment should be able to point from each risk to the code path, operating procedure, or launch gate that addresses it.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Ethics work fails when it stays qualitative while the system is quantitative. Force the team to name measurable proxies, owners, and rollback conditions; otherwise known risks will remain visible in prose but invisible in the deployment pipeline.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.1.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$f_\theta(o)\to (\hat y,\hat p),\quad \text{act if } \max_k \hat p_k \ge \tau,\quad \text{otherwise abstain and query}$</p><p>The defining difference between closed-world and open-world tasks is not model size, it is the right to abstain. In a closed-world benchmark the label space and task graph are fixed. In open-world embodiment the agent must detect when the current observation lies outside that contract and choose a safe fallback.</p></div>
<div class="callout algorithm"><div class="callout-title">Open-set action gate</div><ol>
<li>Train the base policy on the known task set, then calibrate confidence on held-out known data.</li>
<li>Create novelty panels with unseen objects, scene layouts, instructions, and interaction partners.</li>
<li>Choose a threshold $\tau$ that balances false alarms against unsafe confident errors.</li>
<li>Define the abstention action: ask, slow down, hand off, or switch to exploration mode.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Closed-World Success Versus Open-World Competence</div><table><thead><tr><th>Evaluation Item</th><th>Closed-World Reading</th><th>Open-World Reading</th></tr></thead><tbody>
<tr><td>High success rate</td><td>Policy solves the benchmark.</td><td>Only meaningful if novelty detection is also measured.</td></tr>
<tr><td>Confidence score</td><td>Convenient ranking statistic.</td><td>Launch gate for safe action or abstention.</td></tr>
<tr><td>Replay trace</td><td>Debugging artifact.</td><td>Evidence for recovery after distribution shift.</td></tr>
<tr><td>Failure</td><td>One more bad episode.</td><td>Potential proof that the task contract was violated.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Decide whether to act or abstain.
confidence = {"known_mug": 0.91, "unknown_object": 0.42}
threshold = 0.70

for item, score in confidence.items():
    decision = "act" if score >= threshold else "query_or_fallback"
    print(item, score, decision)</code></pre>
<div class="code-output"><pre>known_mug 0.91 act
unknown_object 0.42 query_or_fallback</pre></div>
<div class="code-caption">Code Fragment 51.1.T captures the core open-world move: the policy must sometimes refuse to pretend the benchmark still applies.</div>
<p>The second line is the one readers should remember. Open-world embodiment is not defined by solving new cases immediately; it is defined by detecting that a new case arrived and choosing a controllable recovery path rather than an overconfident action.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>An open-world system fails when confidence is reported but never connected to action gating. Always test whether low confidence changes behavior, because a detector that does not alter control is only a dashboard ornament.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.2.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$a_t=\pi(o_t,\phi(x_t),g_t),\quad \phi(x_t)=\text{affordance embedding of the novel object or scene}$</p><p>Novel objects and instructions become manageable when the agent reasons through affordances and relational structure, not only object names. The same object category shift can require different recovery behavior depending on whether the new item changes grasp geometry, visibility, friction, or language grounding.</p></div>
<div class="callout algorithm"><div class="callout-title">Affordance-first novelty handling</div><ol>
<li>Detect whether novelty came from appearance, language, dynamics, or layout.</li>
<li>Map the new object or phrase into an affordance representation, such as graspable, pourable, movable, or blocked.</li>
<li>Reuse the known policy only if the required affordances remain supported.</li>
<li>Otherwise ask for clarification, collect a new demonstration, or fall back to a safer manipulation primitive.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Kinds Of Novelty And Their Correct Responses</div><table><thead><tr><th>Novelty Type</th><th>Example</th><th>Preferred Response</th></tr></thead><tbody>
<tr><td>Visual novelty</td><td>Transparent cup instead of opaque mug.</td><td>Re-estimate pose and grasp affordance.</td></tr>
<tr><td>Instruction novelty</td><td>"Stow the sample" instead of "put it away".</td><td>Ground synonyms and confirm the destination.</td></tr>
<tr><td>Layout novelty</td><td>Shelf moved after training.</td><td>Update map and replan before execution.</td></tr>
<tr><td>Dynamics novelty</td><td>Object is heavier or slippery.</td><td>Switch controller gains or lower force and speed.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Choose a response based on novelty source.
novelty = {"type": "visual", "affordance_supported": False, "confidence": 0.48}

if novelty["confidence"] < 0.6 and not novelty["affordance_supported"]:
    action = "ask_or_collect_demo"
else:
    action = "reuse_policy"
print(novelty["type"], action)</code></pre>
<div class="code-output"><pre>visual ask_or_collect_demo</pre></div>
<div class="code-caption">Code Fragment 51.2.T shows that novelty handling should branch on affordance support, not only on whether the object label is known.</div>
<p>The key interpretation is that visual novelty alone is not the decisive variable. If the learned policy still has the right affordance support, reuse may be sensible. If not, the safe path is to query, demonstrate, or switch primitives before acting.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Novel-object handling fails when a benchmark counts every successful transfer equally. Separate appearance novelty from dynamics novelty and measure whether the recovery path changed appropriately, not only whether the final goal was eventually reached.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.3.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$V^\pi(s_t,g_{1:H})=\mathbb E\!\left[\sum_{k=t}^{T}\gamma^{k-t}r_k \mid s_t,g_{1:H}\right],\quad g_{1:H}=\text{subgoal sequence}$</p><p>Long-horizon open-world tasks stress memory, replanning, and delayed credit. The agent must preserve a subgoal structure while admitting that intermediate observations, object availability, and human instructions can change long after the initial plan was formed.</p></div>
<div class="callout algorithm"><div class="callout-title">Receding-horizon subgoal audit</div><ol>
<li>Decompose the task into subgoals with explicit completion tests and fallback conditions.</li>
<li>Cache the assumptions behind each subgoal, such as object availability or map reachability.</li>
<li>Revalidate those assumptions at every horizon boundary and replan only the affected suffix.</li>
<li>Report success not only at the final task level, but also by subgoal completion, repair count, and time lost to replans.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Why Long-Horizon Tasks Break Short-Horizon Policies</div><table><thead><tr><th>Pressure</th><th>Short-Horizon Policy Behavior</th><th>Needed Upgrade</th></tr></thead><tbody>
<tr><td>Delayed reward</td><td>Overfocuses on immediate progress.</td><td>Subgoal values or planning lookahead.</td></tr>
<tr><td>Scene change mid-task</td><td>Commits to stale plan prefixes.</td><td>Assumption checks and replanning.</td></tr>
<tr><td>Instruction revision</td><td>Treats new command as noise.</td><td>Task-memory update and authority switch.</td></tr>
<tr><td>Sparse failure signal</td><td>Finds out too late that one subgoal failed.</td><td>Intermediate completion tests.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Track subgoal completion and repair events.
trace = [
    {"subgoal": "find_cart", "done": True, "repair": 0},
    {"subgoal": "reach_lab", "done": False, "repair": 1},
    {"subgoal": "reroute_around_closed_door", "done": True, "repair": 1},
]

completed = sum(step["done"] for step in trace)
repairs = sum(step["repair"] for step in trace)
print("completed", completed, "repairs", repairs)</code></pre>
<div class="code-output"><pre>completed 2 repairs 2</pre></div>
<div class="code-caption">Code Fragment 51.3.T makes long-horizon behavior inspectable by logging subgoal completion and repair operations, not only the final binary outcome.</div>
<p>The final task might still succeed, but two repair events tell a very different story about competence and deployment cost. In long-horizon embodiment, this intermediate trace often carries more design information than the final success bit.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Long-horizon evaluation fails when all adaptation is hidden inside one end score. Always log which subgoal assumptions broke and how often replanning occurred, otherwise open-world brittleness disappears inside a single aggregate success rate.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.4.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$\theta_{t+1}=\theta_t-\eta\nabla_\theta\big(\ell_{\mathrm{new}}+\beta\,\ell_{\mathrm{retention}}\big),\quad \ell_{\mathrm{retention}}=\|\theta-\theta^\star\|_{\Omega}^2$</p><p>Continual learning is not just about getting better on the next task. It is an optimization problem with a retention term that protects previously useful behavior. Catastrophic forgetting is what happens when the gradient signal from the new task overwhelms that retention mechanism.</p></div>
<div class="callout algorithm"><div class="callout-title">Retention-aware adaptation loop</div><ol>
<li>Keep a reference snapshot or sufficient statistics for important old-task parameters.</li>
<li>Update on the new task while penalizing changes to parameters with high old-task importance.</li>
<li>Replay old experiences or distilled summaries on every adaptation window.</li>
<li>Trigger rollback or slower learning when old-task metrics cross a retention threshold.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">Common Anti-Forgetting Strategies</div><table><thead><tr><th>Strategy</th><th>Main Idea</th><th>Embodied Tradeoff</th></tr></thead><tbody>
<tr><td>Replay buffer</td><td>Mix old and new experience.</td><td>Storage and distribution-shift bias.</td></tr>
<tr><td>Regularization</td><td>Protect important parameters.</td><td>Can slow useful adaptation.</td></tr>
<tr><td>Modular expansion</td><td>Add new capacity per regime.</td><td>Grows memory and routing complexity.</td></tr>
<tr><td>Policy distillation</td><td>Compress previous competence into a new model.</td><td>Teacher errors can be fossilized.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Check whether adaptation harmed old skills.
scores = {
    "before_new_task": {"old_task": 0.88, "new_task": 0.21},
    "after_adaptation": {"old_task": 0.63, "new_task": 0.74},
}

old_drop = round(scores["before_new_task"]["old_task"] - scores["after_adaptation"]["old_task"], 2)
print("old_task_drop", old_drop)</code></pre>
<div class="code-output"><pre>old_task_drop 0.25</pre></div>
<div class="code-caption">Code Fragment 51.4.T makes forgetting visible by reporting how much old competence was spent to buy new competence.</div>
<p>A 0.25 drop is large enough that a deployment team should ask whether the adaptation is acceptable, whether replay coverage is weak, or whether a slower modular route is needed. Continual learning is only successful when the gain on the new task justifies the retention cost.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Continual learning fails when only the new task is monitored during adaptation. In embodied systems that can quietly erase safety reflexes or navigation habits that were never included in the adaptation objective.</p></div>
""",
    "part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.5.html": r"""
<div class="callout under-the-hood"><div class="callout-title">Formal Object</div><p>$\mathcal M_t=\{e_k\}_{k=1}^{K},\quad e_k=(o_k,a_k,r_k,o'_k,\text{context}_k),\quad q_t=\operatorname{Retrieve}(\mathcal M_t,o_t,g_t)$</p><p>Memory and replay are only useful when retrieval is selective and evaluation is open-world. A robot that remembers everything but cannot decide what is stale, unsafe, or irrelevant will often adapt worse than a smaller system with disciplined memory hygiene.</p></div>
<div class="callout algorithm"><div class="callout-title">Memory-hygiene and replay audit</div><ol>
<li>Store each episode with context tags: task, scene, partner, hardware mode, and safety status.</li>
<li>Retrieve by current goal and context, not by raw similarity alone.</li>
<li>Downweight or quarantine stale memories after environment, hardware, or policy changes.</li>
<li>Evaluate memory by retrieval precision, adaptation gain, and retained old-task performance on an open-world panel.</li>
</ol></div>
<div class="comparison-table"><div class="comparison-table-title">What A Good Embodied Memory Should Filter</div><table><thead><tr><th>Memory Type</th><th>Keep When</th><th>Discard Or Quarantine When</th></tr></thead><tbody>
<tr><td>Successful routine episode</td><td>Context still matches deployment.</td><td>Sensor stack or map changed materially.</td></tr>
<tr><td>Rare failure case</td><td>Useful for safety replay and recovery practice.</td><td>Failure came from obsolete hardware.</td></tr>
<tr><td>Human correction trace</td><td>Clarifies preferences or hidden constraints.</td><td>User intent was later revised.</td></tr>
<tr><td>Near-duplicate experiences</td><td>Needed for calibration only.</td><td>They crowd out diverse evidence.</td></tr>
</tbody></table></div>
<pre><code class="language-python"># Audit whether retrieved memories still help.
retrievals = [
    {"memory": "old_layout_episode", "relevant": False, "gain": -0.12},
    {"memory": "recent_shift_episode", "relevant": True, "gain": 0.18},
]

for row in retrievals:
    print(row["memory"], row["relevant"], row["gain"])</code></pre>
<div class="code-output"><pre>old_layout_episode False -0.12
recent_shift_episode True 0.18</pre></div>
<div class="code-caption">Code Fragment 51.5.T shows that replay quality depends on relevance; one stale memory can actively hurt open-world adaptation.</div>
<p>The negative gain on the stale episode is exactly why memory systems need filtering and provenance. Retrieval should improve the current decision boundary, not simply increase the amount of past data touched during inference or adaptation.</p>
<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>Replay systems fail when they are scored only by sample efficiency. In open-world embodiment, the harder question is whether the retrieved memories still belong to the current world, task, and safety envelope.</p></div>
""",
}


def replace_block(text: str, new_block: str) -> str:
    pattern = re.compile(
        r'(<section class="technical-core-expansion">.*?<figure class="technical-figure".*?</figure>\s*)(<div class="callout under-the-hood">.*?<div class="callout warning"><div class="callout-title">Failure Mode To Test</div><p>.*?</p></div>)',
        re.DOTALL,
    )
    new_text, count = pattern.subn(lambda m: m.group(1) + new_block.strip(), text, count=1)
    if count != 1:
        raise ValueError("expected one technical core block replacement")
    return new_text


def main() -> None:
    changed = []
    for rel, block in REPLACEMENTS.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        new_text = replace_block(text, block)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.append(rel)
    print(f"changed={len(changed)}")
    for rel in changed:
        print(rel)


if __name__ == "__main__":
    main()
