from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")


def bib_section(entries: list[tuple[str, str, str]]) -> str:
    cards = []
    for href, ref, note in entries:
        cards.append(
            f"""<div class="bib-entry-card">
<p class="bib-ref"><a href="{href}" rel="noopener" target="_blank">{ref}</a></p>
<p class="bib-annotation">{note}</p>
<span class="bib-meta">Paper or Documentation</span>
</div>"""
        )
    return """<section class="bibliography">
<div class="bibliography-title">Bibliography and Further Reading</div>
<div class="bib-category">Primary Sources and Tools</div>
""" + "\n".join(cards) + "\n</section>"


def comparison_rows(rows: list[tuple[str, str, str]]) -> str:
    body = []
    for tool, role, advice in rows:
        body.append(
            f"<tr><td>{tool}</td><td>{role}</td><td>{advice}</td></tr>"
        )
    return "\n".join(body)


def section_payload(
    *,
    sid: str,
    chapter_title: str,
    topic: str,
    checklist_1: str,
    checklist_2: str,
    big_picture: str,
    pathway: str,
    develops: str,
    key_question: str,
    insight: str,
    theory_1: str,
    theory_2: str,
    mechanism: str,
    worked_intro: str,
    code_1: str,
    output_1: str,
    caption_1: str,
    shortcut: str,
    recipe_items: list[str],
    warning: str,
    practical_example: str,
    fun_note: str,
    frontier: str,
    self_check: str,
    deep_dive_1: str,
    deep_dive_2: str,
    table_title: str,
    table_rows: list[tuple[str, str, str]],
    implementation_intro: str,
    implementation_items: list[str],
    code_2: str,
    output_2: str,
    caption_2: str,
    teaching_move: str,
    failure_analysis: str,
    takeaway: str,
    exercise: str,
    bibliography_entries: list[tuple[str, str, str]],
) -> str:
    recipe_html = "\n".join(f"<li>{item}</li>" for item in recipe_items)
    implementation_html = "\n".join(
        f"<li>{item}</li>" for item in implementation_items
    )
    return f"""<section class="agent-checklist-synthesis" id="agent-checklist-{sid.replace('.', '-')}">
<h2>Agent Checklist Synthesis</h2>
<p><strong>Depth and self-containment.</strong> {checklist_1}</p>
<p><strong>Production and evaluation contract.</strong> {checklist_2}</p>
<div class="callout key-insight"><div class="callout-title">Checklist Memory Anchor</div><p>Name the language interface, the grounded world state, the executable action contract, and the evidence artifact before trusting any claimed improvement.</p></div>
<div class="callout exercise"><div class="callout-title">Mini Audit Exercise</div><p>Write one row that records instruction, world state estimate, chosen action, verifier result, and failure label. Then explain which field would change first if the agent misunderstood the command.</p></div>
</section>
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>{big_picture}</p>
</div>
<div class="callout pathway">
<div class="callout-title">Reader Pathway</div>
<p>{pathway}</p>
</div>
<h2>What This Section Develops</h2>
<p>{develops}</p>
<p>{key_question}</p>
<div class="callout key-insight">
<div class="callout-title">Action Is The Test</div>
<p>{insight}</p>
</div>
<h2>Theory</h2>
<p>{theory_1}</p>
<p>{theory_2}</p>
<div class="callout under-the-hood">
<div class="callout-title">Mechanism</div>
<p>{mechanism}</p>
</div>
<h2>Worked Example</h2>
<p>{worked_intro}</p>
<pre><code class="language-python">{code_1}</code></pre>
<div class="code-output">{output_1}</div>
<div class="code-caption"><strong>Code Fragment 1:</strong> {caption_1}</div>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>{shortcut}</p>
</div>
<h2>Practical Recipe</h2>
<ol>
{recipe_html}
</ol>
<div class="callout warning">
<div class="callout-title">Common Failure Mode</div>
<p>{warning}</p>
</div>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>{practical_example}</p>
</div>
<div class="callout fun-note">
<div class="callout-title">Memory Hook</div>
<p>{fun_note}</p>
</div>
<div class="callout research-frontier">
<div class="callout-title">Research Frontier</div>
<p>{frontier}</p>
</div>
<div class="callout self-check">
<div class="callout-title">Self Check</div>
<p>{self_check}</p>
</div>
<section class="production-depth-expansion">
<h2>Builder's Deep Dive</h2>
<p>{deep_dive_1}</p>
<p>{deep_dive_2}</p>
<div class="comparison-table">
<div class="comparison-table-title">{table_title}</div>
<table>
<thead><tr><th>Tool or Library</th><th>Role in the Topic</th><th>Builder Advice</th></tr></thead>
<tbody>
{comparison_rows(table_rows)}
</tbody>
</table>
</div>
<h2>Implementation Recipe</h2>
<p>{implementation_intro}</p>
<ol>
{implementation_html}
</ol>
<pre><code class="language-python">{code_2}</code></pre>
<div class="code-output">{output_2}</div>
<div class="code-caption"><strong>Code Fragment 2:</strong> {caption_2}</div>
<div class="callout tip"><div class="callout-title">Teaching Move</div><p>{teaching_move}</p></div>
<h2>Failure Analysis Pattern</h2>
<p>{failure_analysis}</p>
</section>
<div class="callout key-takeaway">
<div class="callout-title">Key Takeaway</div>
<p>{takeaway}</p>
</div>
<div class="callout exercise"><div class="callout-title">Exercise {sid}.1</div><p>{exercise}</p></div>
{bib_section(bibliography_entries)}
"""


SECTIONS: dict[str, str] = {}


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.1.html"] = section_payload(
    sid="31.1",
    chapter_title="Language-Guided Embodied Agents",
    topic="Why language matters in embodied AI",
    checklist_1="Language does useful work only if it compresses task intent into variables the robot can actually act on: predicates, object references, temporal qualifiers, and safety constraints. A reader should leave this section able to say which parts of an instruction belong in perception, planning, control, and clarification.",
    checklist_2="The minimum artifact for this topic is an instruction trace linked to a grounded scene graph or semantic map, a proposed skill sequence, and a verifier outcome. If those four elements are not logged together, the system cannot tell whether a failure came from language, grounding, or control.",
    big_picture="<strong>Why language matters in embodied AI</strong> is that language turns a raw control problem into a structured decision problem: it adds goals, constraints, and repair signals that would otherwise have to be hard-coded or inferred from reward alone.",
    pathway="Read the section in three passes: first as an argument for language as a control interface, then as a grounding problem, then as an engineering contract for logs and verifiers.",
    develops="This section explains why language is not decoration on top of robotics, but a high-bandwidth interface for specifying intent, exceptions, preferences, and corrections under partial observability.",
    key_question="The practical question is which parts of a task should be carried in language rather than geometry, reward, or low-level feedback, and what extra failure modes that choice introduces.",
    insight="Language pays off when it shrinks search over goals and recovery actions without pretending to replace perception, state estimation, or feedback control.",
    theory_1="Let the hidden world state be $s_t$, the observation be $o_t$, the language context be $x$, and the action be $a_t$. A language-guided embodied policy factors as $$\\pi(a_t \\mid h_t, x), \\qquad h_t = f(h_{{t-1}}, o_t, a_{{t-1}}),$$ where the history state $h_t$ must bind words such as <em>red mug</em>, <em>top shelf</em>, or <em>do not spill</em> to executable state features.",
    theory_2="Language matters most when the task reward is sparse or underspecified. Instead of learning only from scalar success, the agent receives semantic structure: subgoals, object roles, temporal order, and repair instructions. That structure reduces ambiguity in planning, but only if grounding resolves the words into entities, relations, and constraints that are valid in the current scene.",
    mechanism="A useful mental model is to treat language as a typed side channel. It carries variables that ordinary sensor fusion does not infer cheaply: intent, forbidden states, user preferences, and explanation-worthy corrections. The policy is better because the search space is narrower, not because text magically substitutes for physics.",
    worked_intro="Code Fragment 1 builds the smallest possible trace showing how language can reduce task ambiguity. The example scores candidate objects against a text query and a task constraint, then exposes the grounded target that the controller will receive.",
    code_1="""# Ground a short instruction into an executable object choice.
# The score combines language relevance with a simple spatial constraint.
# A robot policy should consume the chosen object id, not the raw sentence.
import numpy as np

objects = [
    {"name": "red mug", "on_top_shelf": False, "lang": 0.95},
    {"name": "blue mug", "on_top_shelf": True, "lang": 0.71},
    {"name": "red bowl", "on_top_shelf": False, "lang": 0.42},
]

scores = []
for obj in objects:
    constraint_bonus = 0.30 if not obj["on_top_shelf"] else -0.40
    total = obj["lang"] + constraint_bonus
    scores.append((obj["name"], round(total, 2)))

choice = max(scores, key=lambda row: row[1])
print(scores)
print(choice)""",
    output_1="""[('red mug', 1.25), ('blue mug', 0.31), ('red bowl', 0.72)]
('red mug', 1.25)""",
    caption_1="This fragment turns a sentence-level preference into an executable object choice by combining language compatibility with the shelf constraint. Notice that the highest language score is not enough by itself; the grounded action target depends on whether the object satisfies the task rule in the current scene.",
    shortcut="In production, the same grounding pattern takes a few lines with a detector plus a text-conditioned grounding model such as Grounding DINO or OWL-ViT. Those libraries absorb proposal generation, batching, and image feature extraction internally, leaving the engineer to define the task-specific constraint logic and verifier.",
    recipe_items=[
        "Write the instruction in a typed form: task verb, object reference, spatial relation, and safety constraint.",
        "Choose a world representation that can host those types, such as a semantic map, object table, or scene graph.",
        "Define a verifier that can reject grounded targets that are unreachable, unsafe, or inconsistent with the instruction.",
        "Log the unresolved ambiguity explicitly instead of silently picking a candidate.",
        "Re-run the grounding step after every action that changes visibility or object pose.",
    ],
    warning="Teams often report instruction-following success while evaluating on scenes where the relevant object is already obvious. That hides the real question, which is how the system behaves when multiple candidates match the words but only one satisfies the task constraints.",
    practical_example="In warehouse picking, an operator may say, 'take the damaged carton but leave the sealed one.' The useful representation is not the sentence itself, but the resolved pair of object identities, the exclusion mask, and the audit trail showing why the forbidden object was rejected.",
    fun_note="Language is the only part of the stack that can say, 'that one, not the other one, and hurry because the soup is hot.' Controllers are brave, but they rarely volunteer that sentence on their own.",
    frontier="Current embodied-language work pushes from fixed instruction following toward richer dialogue, multilingual commands, and continuous correction loops. Benchmarks such as TEACh and EmbodiedBench make the research frontier less about one-shot understanding and more about whether the agent can ask, recover, and justify.",
    self_check="Can you point to one decision in your system that becomes cheaper because the instruction rules out most of the action space, and one failure mode that appears only because the instruction still needs grounding?",
    deep_dive_1="A precise way to separate language value from policy value is to ask what posterior the words change. If the policy already knows the unique goal from state alone, language is redundant. If the words collapse a large latent goal set into one or two plausible targets, language creates measurable decision value because it changes the planner's belief before any motion occurs.",
    deep_dive_2="That view also explains why static vision-language metrics are not enough. The real quantity is not just text-image similarity, but whether the grounded belief update leads to safer or shorter closed-loop execution. A grounding module that is 2 percent better on retrieval but 20 percent worse at downstream recovery can still be the wrong engineering choice.",
    table_title="Practical Tool Choices For Language Interfaces",
    table_rows=[
        ("Habitat and VLN-CE", "Language-conditioned navigation with explicit maps and episode logs.", "Use it when you need reproducible instruction traces and navigation success metrics tied to continuous control."),
        ("ALFRED and TEACh", "Household manipulation, dialogue, and clarification under partial observability.", "Use them when the instruction must bind to object state changes rather than only route choice."),
        ("Grounding DINO plus SAM 2", "Open-vocabulary object localization and mask extraction.", "Use this pair when the instruction names objects or regions not covered by a closed detector label set."),
        ("ROS 2 actions", "Typed execution contracts for language-selected skills.", "Use actions when the planner must observe progress, preemption, and failure rather than fire and forget."),
        ("LangGraph or a small state machine", "Clarification and recovery loops around language decisions.", "Use it when the agent must ask before acting or escalate uncertainty to a human."),
    ],
    implementation_intro="A robust implementation stores language context alongside the world state estimate. Code Fragment 2 shows an evidence record that makes the separation explicit: one field says what was asked, another says how the world was grounded, and the verifier explains whether execution preserved the intended constraint.",
    implementation_items=[
        "Create a task card containing instruction text, typed slots, and the latest grounding confidence.",
        "Attach every proposed action to the grounded entities or map cells that justify it.",
        "Run a verifier before execution and after execution, because grounding can drift when occlusion or motion changes the scene.",
        "Record clarification requests as first-class events rather than as failed episodes.",
        "Compare systems only when instruction set, embodiment, and verifier are held fixed in one evaluation run.",
    ],
    code_2="""# Record one language-grounding decision as an auditable artifact.
# The artifact links words, grounded entities, and verifier outcomes.
# Keeping these fields together makes recovery analysis much easier.
from dataclasses import asdict, dataclass

@dataclass
class LanguageDecision:
    instruction: str
    grounded_target: str
    excluded_target: str
    action_api: str
    verifier: str

decision = LanguageDecision(
    instruction="pick the red mug, not the blue one",
    grounded_target="object_17:red_mug",
    excluded_target="object_21:blue_mug",
    action_api="pick(object_17)",
    verifier="constraint_preserved=True",
)
print(asdict(decision))""",
    output_2="""{'instruction': 'pick the red mug, not the blue one', 'grounded_target': 'object_17:red_mug', 'excluded_target': 'object_21:blue_mug', 'action_api': 'pick(object_17)', 'verifier': 'constraint_preserved=True'}""",
    caption_2="This artifact keeps the natural-language instruction tied to the grounded object identity and the post-action verifier result. The important detail is that the executable API call, `pick(object_17)`, is stored next to the excluded object, so later debugging can tell whether the failure came from grounding or execution.",
    teaching_move="Ask readers to edit only one field at a time: first the instruction, then the grounded object, then the verifier. The exercise makes it obvious which mistakes are semantic and which are physical.",
    failure_analysis="When this interface fails, first ask whether the wrong object was grounded, the right object was grounded but unreachable, or the motion succeeded while violating an unlogged constraint. That decomposition prevents 'language failure' from becoming a meaningless bucket for every downstream error.",
    takeaway="Language helps embodied agents by shaping the latent task they solve, not by exempting them from grounding, control, or verification.",
    exercise="Choose a task where reward alone would be sparse or ambiguous, then design a language interface that adds exactly two useful typed variables and one verifier check. Explain how each field changes the downstream action search.",
    bibliography_entries=[
        ("https://arxiv.org/abs/1912.01734", 'Shridhar et al. (2020). "ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks." CVPR.', "ALFRED is the canonical household benchmark showing that language understanding is only useful when it stays coupled to visual grounding and action execution."),
        ("https://arxiv.org/abs/2110.00534", 'Padmakumar et al. (2022). "TEACh: Task-driven Embodied Agents that Chat." AAAI.', "TEACh adds clarification dialogue and hidden state, which makes it a strong reference for language that must repair ambiguity during execution."),
        ("https://arxiv.org/abs/2004.02857", 'Krantz et al. (2020). "Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments." ECCV.', "VLN-CE shows how instruction following changes when the agent must control a continuous body rather than hop between symbolic graph nodes."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.2.html"] = section_payload(
    sid="31.2",
    chapter_title="Language-Guided Embodied Agents",
    topic="Instructions, goals, constraints",
    checklist_1="This section must distinguish a free-form instruction from the executable goal and constraint objects that planners consume. Readers should finish knowing which parts of a sentence are optimization targets, which are hard constraints, and which are preferences that can be traded off.",
    checklist_2="A publishable artifact here records the instruction parse, the goal predicate, the forbidden predicates, and the scalar objective used during planning. Without that split, two systems can appear comparable while optimizing different notions of success.",
    big_picture="<strong>Instructions, goals, constraints</strong> is where language becomes a planning problem. The words are valuable only after the system separates what must happen, what must never happen, and what would be nice if time permits.",
    pathway="Read from semantics to optimization: parse the utterance, convert it into goal and constraint objects, then decide how the planner should trade soft preferences against hard rules.",
    develops="This section turns natural-language directives into a control objective that a symbolic planner, MPC stack, or policy can actually optimize.",
    key_question="The practical question is which clauses in the instruction should become equalities, inequalities, or preference weights in the downstream planner.",
    insight="A planner is only as safe as the strongest constraint it refuses to violate. Preferences can slide; forbidden states cannot.",
    theory_1="Suppose an instruction induces a goal variable $g$, a set of hard constraints $\\mathcal C$, and a preference score $r_\\text{pref}$. A planner can then solve $$\\max_{\\tau} \\; \\mathbb E\\left[\\sum_t r(s_t, a_t; g) + \\lambda r_\\text{pref}(s_t, a_t, x)\\right] \\quad \\text{s.t.} \\quad c_k(s_t, a_t, x) \\le 0 \\; \\forall k \\in \\mathcal C.$$ The language front end decides what enters the reward and what enters the constraint set.",
    theory_2="This distinction matters because optimization behaves differently under each choice. If 'do not tip the cup' is encoded as a mild reward penalty, a planner may accept spills when the goal is otherwise attractive. If it is encoded as a hard constraint or shield, the system must seek an alternative path or ask for clarification.",
    mechanism="A good parser emits typed slots such as `goal=deliver(red_mug, user)`, `constraint=keep_upright(red_mug)`, and `preference=avoid_left_shelf`. Those slots are much more stable engineering interfaces than raw prompts because verifiers and controllers can inspect them directly.",
    worked_intro="Code Fragment 1 shows a compact parser that turns a single sentence into hard and soft task elements. The important detail is not the string matching itself, but the separation between mandatory and negotiable parts of the instruction.",
    code_1="""# Split one instruction into a goal, a hard constraint, and a soft preference.
# Real systems use learned parsing, but the typed output contract is the same.
# The planner should inspect these slots directly instead of re-reading the sentence.
instruction = "bring the red mug, keep it upright, avoid the left shelf"

goal = "deliver(red_mug)"
hard_constraints = ["keep_upright(red_mug)"]
preferences = ["avoid(left_shelf)"]

print({"goal": goal, "hard": hard_constraints, "soft": preferences})""",
    output_1="""{'goal': 'deliver(red_mug)', 'hard': ['keep_upright(red_mug)'], 'soft': ['avoid(left_shelf)']}""",
    caption_1="This parser emits a typed contract that later modules can inspect without guessing which clauses are negotiable. The crucial distinction is that `keep_upright(red_mug)` is preserved as a hard rule, while `avoid(left_shelf)` remains a soft preference that a planner may relax only if necessary.",
    shortcut="Libraries such as Pydantic, JSON schema tool calling, and structured-output APIs turn the same pattern into a few lines by forcing the LLM to emit typed fields. They handle validation, missing keys, and schema checks internally, so the planner receives machine-readable goals rather than brittle free text.",
    recipe_items=[
        "Write one schema for goals, one for hard constraints, and one for preferences.",
        "Define a parser failure state for instructions that cannot populate the schema reliably.",
        "Make the verifier inspect hard constraints before any preference score is reported.",
        "Assign explicit units to every numeric threshold extracted from text, such as speed or distance.",
        "Treat underspecified slots as a clarification trigger, not as permission to improvise.",
    ],
    warning="A common mistake is to overfit to clean lab instructions where every constraint is stated explicitly. Real instructions omit quantities, reference hidden user preferences, and conflict with the geometry of the scene. Silent default choices can look intelligent while actually violating the user's intent.",
    practical_example="A home assistant that hears 'bring me the soup, but do not spill it and do not wake the baby' should parse one delivery goal, one fluid-stability constraint, and one acoustic preference. The last item may reshape route choice and speed even when the delivery target stays the same.",
    fun_note="Natural language loves to hide a legal department inside one comma. 'Bring the mug, but not that mug, and be quick, but be careful' is still one sentence to the human and three optimization problems to the robot.",
    frontier="Recent work on structured outputs, semantic parsers for robotics, and constrained policy optimization increasingly blurs the line between natural-language tasking and formal task specifications. The open question is how much of the structure should be learned end to end and how much should stay explicit for safety and debugging.",
    self_check="If you remove the sentence and keep only the parsed task object, can the downstream planner still tell what is mandatory and what is merely preferred?",
    deep_dive_1="This section is where language touches control theory most directly. Once the utterance becomes a constrained optimization problem, the usual machinery of feasibility, receding-horizon planning, and safety filtering applies. The LLM is useful because it proposes the task object; it is not the final judge of whether the task object is physically or ethically valid.",
    deep_dive_2="The best engineering pattern is therefore asymmetric: let language be flexible at proposal time and rigid at execution time. Proposal modules may entertain multiple parses, but execution modules should consume one validated, typed contract whose semantics are stable across seeds, prompts, and model versions.",
    table_title="Tool Choices For Typed Instruction Interfaces",
    table_rows=[
        ("Pydantic or dataclasses", "Typed task-object validation.", "Use them to reject malformed parses before the planner sees them."),
        ("OpenAI or Anthropic structured outputs", "Schema-constrained LLM parsing.", "Use them when free-form prompts are too brittle for production tasking."),
        ("BehaviorTree.CPP", "Execution logic with explicit success and failure branches.", "Use it when a parsed constraint should trigger fallback or clarification instead of silent retries."),
        ("MoveIt Task Constructor", "Constraint-aware manipulation planning.", "Use it when language specifies goal poses, collision exclusions, or grasp requirements."),
        ("ROS 2 actions", "Long-running skill invocation with cancelation and feedback.", "Use actions when language goals may be revised mid-execution."),
    ],
    implementation_intro="Code Fragment 2 scores candidate plans against one hard constraint and one preference to make the distinction visible numerically. The hard constraint prunes infeasible plans first; only then does the preference score choose between survivors.",
    implementation_items=[
        "Generate several candidate plans from the same typed instruction object.",
        "Reject every candidate that violates a hard rule before computing preference scores.",
        "Score the surviving candidates with a transparent preference model.",
        "If no candidate is feasible, ask a clarification question tied to the missing slot or impossible constraint.",
        "Save both the feasible set and the rejected set so later audits can separate parser and planner failures.",
    ],
    code_2="""# Filter plans by hard constraints, then rank them by soft preference.
# This mirrors the planner discipline that language interfaces should induce.
# A low-cost plan is still invalid if it violates the keep-upright rule.
plans = [
    {"name": "short_path", "upright": False, "pref_cost": 1.0},
    {"name": "wide_turn", "upright": True, "pref_cost": 1.5},
    {"name": "quiet_route", "upright": True, "pref_cost": 0.8},
]

feasible = [p for p in plans if p["upright"]]
best = min(feasible, key=lambda p: p["pref_cost"])
print(feasible)
print(best["name"])""",
    output_2="""[{'name': 'wide_turn', 'upright': True, 'pref_cost': 1.5}, {'name': 'quiet_route', 'upright': True, 'pref_cost': 0.8}]
quiet_route""",
    caption_2="This ranking stage makes the constraint hierarchy explicit. `short_path` is discarded before the preference score is even considered, and the final choice comes from the feasible set rather than from the global minimum cost over invalid actions.",
    teaching_move="Have readers intentionally encode the same rule once as a penalty and once as a hard constraint. The changed behavior is a quick way to internalize why constraint placement matters.",
    failure_analysis="If execution violates intent, inspect the failure in order: parsing, constraint typing, feasibility filtering, then preference ranking. Many so-called planning errors are actually parse errors where a soft preference was accidentally promoted or a hard rule was accidentally softened.",
    takeaway="Language-guided planning improves when instructions are converted into typed goals and constraints whose semantics survive the transition from text to control.",
    exercise="Take one household instruction with at least two clauses and express it as a typed goal object with one hard rule and one soft preference. Then explain how your planner should behave when the hard rule makes all current plans infeasible.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2204.01691", 'Ahn et al. (2022). "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances." arXiv.', "SayCan is a key example of separating linguistic plausibility from executable feasibility, which is exactly the distinction between semantic intent and constraint satisfaction."),
        ("https://docs.ros.org/en/foxy/Tutorials/Intermediate/Creating-an-Action.html", "ROS 2 Documentation. 'Creating an action.'", "ROS 2 actions illustrate how long-running goals become typed contracts with feedback, cancelation, and result states."),
        ("https://www.behaviortree.dev/docs/ros2_integration", "BehaviorTree.CPP Documentation. 'Integration with ROS2.'", "Behavior trees provide a practical execution language for turning parsed constraints into retry, fallback, and verification structure."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.3.html"] = section_payload(
    sid="31.3",
    chapter_title="Language-Guided Embodied Agents",
    topic="Grounding language in perception; referring expressions",
    checklist_1="This section must explain how words like 'the mug beside the kettle' become probabilities over visible entities. Readers need both the matching objective and the failure cases created by occlusion, symmetry, and stale state estimates.",
    checklist_2="The evaluation artifact is not a generic retrieval score. It should log the scene, the referring expression, the candidate set, the chosen referent, and whether the downstream action succeeded with that choice.",
    big_picture="<strong>Grounding language in perception</strong> is the bridge between words and scene variables. Referring expressions are useful only when the robot can resolve them into one object or region under the current viewpoint and state uncertainty.",
    pathway="Read the section as a Bayesian filtering problem over objects: language narrows the candidate set, perception scores the scene, and action reveals whether the choice was actually right.",
    develops="This section shows how embodied agents resolve names, attributes, and relations such as color, position, containment, and ownership into specific entities visible to the robot.",
    key_question="The practical question is how to combine visual evidence with relational language when several objects share the same category or attribute.",
    insight="Referring expressions are not labels; they are filters over a candidate set. The right target emerges only after the system scores attributes and relations jointly.",
    theory_1="Given objects $z_1, \\ldots, z_n$ extracted from perception and a referring expression $x$, the grounding problem is $$\\hat z = \\arg\\max_i \\; p(z_i \\mid x, o_t) \\propto p(x \\mid z_i, o_t)\\, p(z_i \\mid o_t).$$ The perceptual prior says what objects are present; the language likelihood says which of those objects best matches the expression.",
    theory_2="Relational language makes the problem harder because the referent depends on other objects. In 'the mug beside the kettle,' the target score depends on both the mug's own features and the probability that a nearby kettle exists and is correctly localized. Grounding therefore inherits every weakness of the detector and every ambiguity of the language model.",
    mechanism="A robust system scores three kinds of evidence: unary attributes such as color or category, binary relations such as left-of or inside, and dialogue context such as the last mentioned object. The winner is the object whose combined evidence stays strongest after these factors are multiplied or summed.",
    worked_intro="Code Fragment 1 scores three candidate objects against color, category, and spatial relation. It is deliberately tiny, but it exposes the same reasoning pattern used by larger grounding models and dialogue systems.",
    code_1="""# Resolve a referring expression using attribute and relation evidence.
# Each candidate receives unary scores and a relation score to the kettle.
# The selected object is the one with the highest combined grounding score.
candidates = [
    {"id": "obj_1", "label": "mug", "color": "red", "near_kettle": True},
    {"id": "obj_2", "label": "mug", "color": "blue", "near_kettle": True},
    {"id": "obj_3", "label": "bowl", "color": "red", "near_kettle": False},
]

scores = {}
for obj in candidates:
    unary = 0.7 if obj["label"] == "mug" else 0.1
    color = 0.4 if obj["color"] == "red" else 0.0
    relation = 0.5 if obj["near_kettle"] else -0.2
    scores[obj["id"]] = round(unary + color + relation, 2)

print(scores)
print(max(scores, key=scores.get))""",
    output_1="""{'obj_1': 1.6, 'obj_2': 1.2, 'obj_3': 0.3}
obj_1""",
    caption_1="This resolver shows that grounding depends on relations as much as on object category. `obj_1` wins because the relation to the kettle reinforces the unary mug and color evidence, while `obj_2` loses despite matching the category.",
    shortcut="In practice, Grounding DINO, OWL-ViT, SAM 2, and open-vocabulary VLMs provide the candidate boxes or masks in a few lines. Those tools replace manual proposal generation and feature extraction, but the system still needs explicit relation reasoning and a downstream verifier.",
    recipe_items=[
        "Detect or segment a candidate set before asking the language model to choose among them.",
        "Score attributes and relations separately so you can diagnose which signal failed.",
        "Keep the candidate set visible to the planner instead of passing only the winning object id.",
        "When the top two candidates are close, trigger a clarification question or an active view change.",
        "Re-ground after any action that changes visibility, object pose, or scene layout.",
    ],
    warning="A common benchmark shortcut is to evaluate referring-expression accuracy on still images while downstream execution uses a moving camera and partial views. That mismatch makes grounding look solved even when the live system loses the referent after one arm motion.",
    practical_example="A service robot hearing 'hand me the notebook under the lamp' must localize both the notebook and the lamp, reason about the support relation, and preserve that relation after viewpoint changes. If the lamp leaves the frame, the system needs either memory or a new view, not blind confidence.",
    fun_note="Referring expressions are what happen when humans assume everyone in the room is already looking at the same scene. Robots are polite enough to pretend they are, right up until they pick the wrong mug.",
    frontier="Recent grounding work couples open-vocabulary detectors with segmentation, 3D scene memory, and dialogue. The active frontier is not just better box selection, but whether the agent can decide when to move the camera, query the user, or use past context to disambiguate the referent.",
    self_check="Can your system explain which attribute or relation eliminated the runner-up candidate, and what it would do if that evidence disappeared after a viewpoint change?",
    deep_dive_1="Referring expressions are a clean example of embodied partial observability. The agent may know the words but not the full scene, or it may see the scene but lack one relational anchor. Good systems therefore maintain uncertainty over the referent rather than forcing a premature point estimate.",
    deep_dive_2="This is also why closed-loop evaluation matters. A target selection model can have strong top-1 accuracy and still be a poor embodied component if it never signals uncertainty and therefore never triggers clarification or camera motion. The value of grounding lies in the final action outcome, not only in the static matching score.",
    table_title="Tool Choices For Referring Expression Grounding",
    table_rows=[
        ("Grounding DINO", "Open-vocabulary region proposals from text prompts.", "Use it when object categories are not fixed ahead of time."),
        ("SAM 2", "Mask refinement and object persistence across frames.", "Use it when manipulation requires accurate support surfaces or object boundaries."),
        ("OWL-ViT", "Zero-shot text-conditioned detection.", "Use it when you need fast category queries without training a custom detector."),
        ("RTAB-Map or a semantic map", "Persistent world memory for entities and relations.", "Use it when the referent may leave the current camera frame."),
        ("TEACh or ALFRED", "Embodied datasets where referents matter for action.", "Use them when static phrase grounding metrics are too weak for the downstream task."),
    ],
    implementation_intro="Code Fragment 2 records the grounding result as an auditable object. The important field is not just the chosen referent, but the score margin over the runner-up, because that margin is what should drive clarification or active sensing.",
    implementation_items=[
        "Store the candidate list, the winning id, and the runner-up gap in one record.",
        "Tie the winner to the current camera frame or map timestamp so stale groundings are detectable.",
        "Route low-margin groundings to clarification or view-planning instead of execution.",
        "Log whether the downstream action preserved the intended relation after grasp or motion.",
        "Benchmark on scenes with distractors, occlusion, and viewpoint change, not only on clean still images.",
    ],
    code_2="""# Save the grounding decision with a confidence margin for later control logic.
# Small margins should trigger clarification or an active perception step.
# The planner should never treat all grounding wins as equally trustworthy.
decision = {
    "expression": "the red mug beside the kettle",
    "winner": "obj_1",
    "runner_up": "obj_2",
    "margin": round(1.6 - 1.2, 2),
    "action_gate": "clarify" if (1.6 - 1.2) < 0.5 else "execute",
}
print(decision)""",
    output_2="""{'expression': 'the red mug beside the kettle', 'winner': 'obj_1', 'runner_up': 'obj_2', 'margin': 0.4, 'action_gate': 'clarify'}""",
    caption_2="This artifact turns grounding uncertainty into control logic. Because the winner only beats the runner-up by `0.4`, the section's policy routes the decision to clarification instead of immediate execution.",
    teaching_move="Ask readers to make the margin threshold smaller and larger, then observe when the system becomes reckless versus indecisive. The trade-off is easier to feel than to memorize.",
    failure_analysis="When grounding fails, separate detector failures, relation failures, stale-memory failures, and confidence-calibration failures. Different fixes apply to each: better proposals, explicit relation modeling, view planning, or threshold tuning.",
    takeaway="Embodied grounding succeeds when words, scene evidence, and uncertainty are represented in the same decision loop.",
    exercise="Design a grounding record for the phrase 'the box under the table near the door.' List the unary and relational scores you would log, and say which ambiguity should trigger an active view change.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2303.05499", 'Liu et al. (2023). "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection." arXiv.', "Grounding DINO is a widely used reference for text-conditioned region proposals that can serve embodied grounding pipelines."),
        ("https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/", "Meta AI (2024). 'SAM 2: Segment Anything in Images and Videos.'", "SAM 2 is useful when object masks and persistence matter more than coarse boxes, especially for manipulation."),
        ("https://arxiv.org/abs/2110.00534", 'Padmakumar et al. (2022). "TEACh: Task-driven Embodied Agents that Chat." AAAI.', "TEACh is a strong reference for grounding in the presence of dialogue and hidden world state."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.4.html"] = section_payload(
    sid="31.4",
    chapter_title="Language-Guided Embodied Agents",
    topic="Object- and region-centric grounding",
    checklist_1="This section must distinguish object-centric grounding, where actions attach to discrete entities, from region-centric grounding, where the target is a mask, point cloud subset, or continuous workspace region. Readers should know when each abstraction breaks.",
    checklist_2="The useful artifact is a grounding record that contains object ids or region masks, confidence, spatial frame, and the action primitive that consumes them. That makes it possible to compare grasping, placing, and navigation pipelines fairly.",
    big_picture="<strong>Object- and region-centric grounding</strong> decides what kind of world representation language should land on. Some instructions name discrete objects; others name continuous areas, support surfaces, or forbidden zones.",
    pathway="Read from representation choice to downstream control: decide whether the language should bind to an object token, a mask, a voxel region, or a waypoint set, then ask which action primitive can consume that representation cleanly.",
    develops="This section explains why embodied systems often need both object-level and region-level grounding, especially when manipulation targets involve support surfaces, free space, or contact zones rather than only category labels.",
    key_question="The practical question is which representation best matches the next controller call: object id, pose, mask, affordance region, or continuous map cell set.",
    insight="Choose the representation that matches the action primitive. If the gripper needs a mask edge or a free-space corridor, an object label alone is too coarse.",
    theory_1="Let $z_i$ denote discrete object hypotheses and $R_j \\subset \\mathbb R^3$ denote grounded regions. A language-conditioned action interface should choose $$u = g(x, o_t) \\in \\{z_1, \\ldots, z_n, R_1, \\ldots, R_m\\},$$ then pass either the discrete object handle or the continuous region geometry to the planner. The right choice depends on whether the downstream skill needs identity or geometry.",
    theory_2="Object-centric grounding works well for pick, handover, or inspect actions where a discrete entity is the action subject. Region-centric grounding is better for 'wipe this spill,' 'place the bowl in the free space beside the plate,' or 'avoid the wet area,' because the relevant target is a spatial extent rather than a named object.",
    mechanism="A practical system often composes both. It may first resolve an object category, then derive a contact region or free region from a mask, depth map, or occupancy estimate. Language therefore selects not just a target, but the representation layer at which the target should be expressed.",
    worked_intro="Code Fragment 1 compares an object-centric and region-centric interpretation of the same scene. The point is not the geometry itself, but the controller contract each interpretation enables.",
    code_1="""# Compare object-centric and region-centric action targets.
# The object handle is enough for a simple pick, but placement needs a region.
# The chosen representation should match the action primitive downstream.
scene = {
    "target_object": "red_mug",
    "free_region_area_cm2": 128.0,
    "forbidden_region_area_cm2": 42.0,
}

pick_target = {"mode": "object", "handle": scene["target_object"]}
place_target = {"mode": "region", "free_area": scene["free_region_area_cm2"]}

print(pick_target)
print(place_target)""",
    output_1="""{'mode': 'object', 'handle': 'red_mug'}
{'mode': 'region', 'free_area': 128.0}""",
    caption_1="The first target is a discrete object handle suitable for grasp selection, while the second is a continuous region summary suitable for placement planning. The representation changes because the action primitive changes, even though both arise from the same scene and instruction.",
    shortcut="With SAM 2, Grounding DINO, point-cloud libraries, and occupancy-map toolkits, the same object-to-region pipeline becomes a handful of calls. The shortcut removes mask extraction and geometry bookkeeping so the engineer can concentrate on task semantics and safety checks.",
    recipe_items=[
        "Map every skill primitive to the representation it expects before choosing a grounding model.",
        "Use object ids for identity-sensitive tasks such as pick, inspect, and handover.",
        "Use masks, surfaces, or free-space regions for placement, wiping, or collision avoidance.",
        "Convert between object and region views explicitly, for example from mask to support surface.",
        "Log the representation type in every evaluation trace so later comparisons stay construct matched.",
    ],
    warning="It is easy to benchmark grounding at the wrong abstraction level. A detector that identifies the right object category can still fail the actual task if the region needed for contact, placement, or avoidance is poor.",
    practical_example="A kitchen robot hearing 'put the mug on the clear part of the counter' cannot stop at object detection. It must convert the counter mask into a free-space region after subtracting occupied or unsafe areas, then pass that region to the placement planner.",
    fun_note="Robots love nouns because nouns fit nicely into tables. Regions are messier. Unfortunately, countertops and spills do not reorganize themselves just because the software team prefers object ids.",
    frontier="The frontier increasingly combines open-vocabulary grounding, segmentation, and 3D scene representations so language can name not only objects, but contact patches, affordance zones, and movable free space. That trend connects this chapter directly to the 3D perception material in <a href=\"../../part-6-embodied-perception/module-28-3d-perception-and-neural-scene-representations/section-28.2.html\">Section 28.2</a> and <a href=\"../../part-6-embodied-perception/module-29-localization-and-mapping-slam/section-29.3.html\">Section 29.3</a>.",
    self_check="Can you explain why the phrase 'the clear spot on the counter' should produce a region target rather than a single object id, and which controller needs that geometry?",
    deep_dive_1="Representation choice is one of the most under-reported design decisions in embodied language work. Papers often compare models while quietly changing what the downstream planner receives. An object token and a signed-distance field are not interchangeable interfaces, even if both originate from the same image and command.",
    deep_dive_2="The clean engineering pattern is to keep the language layer honest about this choice. If the command names a surface, the grounding module should output a surface representation. If the skill needs a free-space region, the pipeline should expose that region directly rather than pretending an object label is a sufficient proxy.",
    table_title="Tool Choices For Object and Region Grounding",
    table_rows=[
        ("Grounding DINO or OWL-ViT", "Text-conditioned object proposals.", "Use them when the action requires discrete object identities."),
        ("SAM 2", "Mask extraction for contact and support regions.", "Use it when a controller needs fine geometry rather than a category label."),
        ("Open3D", "Point-cloud slicing and surface extraction.", "Use it when a language-grounded region must become a 3D workspace constraint."),
        ("Occupancy or cost maps", "Free-space and forbidden-region planning.", "Use them for navigation and placement tasks where language names safe and unsafe areas."),
        ("MoveIt Planning Scene", "Collision-aware geometry for manipulation.", "Use it when region grounding must become an executable motion-planning constraint."),
    ],
    implementation_intro="Code Fragment 2 records both representation type and frame. That detail matters because a region mask without its coordinate frame is not an actionable object for a planner.",
    implementation_items=[
        "Store whether the grounded target is an object, mask, point set, or free-space region.",
        "Record the spatial frame and timestamp used to derive the target.",
        "Pass discrete and continuous targets to different validator functions.",
        "After execution, log whether the chosen representation was sufficient or needed refinement.",
        "Compare systems only when they expose the same target representation to the same downstream skill.",
    ],
    code_2="""# Save the target representation together with the frame used for control.
# Region grounding without a frame is not executable in a robot stack.
# This record makes later planner failures much easier to diagnose.
grounding_record = {
    "instruction": "place the mug on the clear part of the counter",
    "target_type": "region",
    "frame": "map",
    "region_cells": 37,
    "consumer_skill": "place_on_surface",
}
print(grounding_record)""",
    output_2="""{'instruction': 'place the mug on the clear part of the counter', 'target_type': 'region', 'frame': 'map', 'region_cells': 37, 'consumer_skill': 'place_on_surface'}""",
    caption_2="This record highlights the fields that let the planner reproduce the grounding decision later. `target_type='region'` and `frame='map'` tell the execution stack that the command refers to geometry, not merely to an object category.",
    teaching_move="Ask students to redesign one object-only benchmark so that success requires region grounding. The exercise reveals how quickly controller contracts change once geometry matters.",
    failure_analysis="When region-centric tasks fail, inspect whether the wrong representation was chosen, whether the mask or surface was poor, or whether the planner consumed the geometry in the wrong frame. Treat these as distinct failure classes rather than as generic grounding errors.",
    takeaway="Language grounding should produce the representation the downstream skill truly needs, even if that representation is a mask or workspace region instead of a neat object label.",
    exercise="Pick one command for grasping and one for placement. For each, specify the best grounding representation, the coordinate frame, and the first verifier you would run before execution.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2303.05499", 'Liu et al. (2023). "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection." arXiv.', "Grounding DINO is a strong reference for object-centric text grounding."),
        ("https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/", "Meta AI (2024). 'SAM 2: Segment Anything in Images and Videos.'", "SAM 2 is a practical reference for turning grounded object proposals into masks and temporally persistent regions."),
        ("https://moveit.picknik.ai/", "MoveIt 2 Documentation.", "MoveIt 2 is the manipulation planning reference for turning grounded geometry into motion-planning constraints and executable trajectories."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.5.html"] = section_payload(
    sid="31.5",
    chapter_title="Language-Guided Embodied Agents",
    topic="Task planning from language; ambiguity and clarification",
    checklist_1="This section must explain when a language-guided agent should act, when it should ask, and how ambiguity propagates into plan quality. The reader needs a formal test for whether clarification is worth the latency.",
    checklist_2="The minimum artifact records candidate interpretations, plan value under each interpretation, the clarification question if one was asked, and the post-clarification plan revision. Without that record, ambiguity handling cannot be audited.",
    big_picture="<strong>Task planning from language</strong> becomes credible only when the agent can tell the difference between missing information and a difficult plan. Clarification is not an admission of weakness; it is a control action that buys information.",
    pathway="Read from ambiguity detection to information value: enumerate plausible parses, estimate how much execution quality changes across them, then decide whether a clarification turn is worth the time.",
    develops="This section connects language planning to active information gathering by showing how an embodied agent should ask before acting when multiple interpretations lead to different risks or trajectories.",
    key_question="The practical question is not 'can the model generate a plan?' but 'should the agent trust the top plan without first reducing ambiguity?'",
    insight="Clarification is rational whenever the expected value of disambiguation exceeds the cost of asking and waiting.",
    theory_1="Let $m \\in \\mathcal M$ be a latent meaning of the instruction, and let $V(\\pi, m)$ be the value of executing plan $\\pi$ under that meaning. If the agent can ask a question $q$ with cost $c(q)$, the value of clarification is $$\\operatorname{VoI}(q) = \\mathbb E_{y \\sim p(y \\mid q)}\\left[\\max_\\pi \\mathbb E_{m \\mid y, q} V(\\pi, m)\\right] - \\max_\\pi \\mathbb E_m V(\\pi, m) - c(q).$$ Ask when this quantity is positive.",
    theory_2="In practice, the agent approximates this computation with confidence gaps, risk heuristics, or plan disagreement. The deeper lesson is that ambiguity should be represented in the planner's state rather than hidden inside the prompt. Otherwise the robot executes one interpretation while the human assumes another.",
    mechanism="A clean clarification loop has four steps: detect multiple plausible task objects, estimate how much the best plan changes across them, ask the smallest question that splits the candidate set, then replan under the updated belief. This is active perception applied to language.",
    worked_intro="Code Fragment 1 computes a tiny expected-value test for whether to ask before acting. The numbers are synthetic, but the control logic is the same in household dialogue, warehouse dispatch, and mobile manipulation.",
    code_1="""# Ask for clarification when plan value changes sharply across meanings.
# The cost of asking should be compared against the value of better execution.
# A small confidence gap does not matter unless it changes the chosen plan.
candidate_meanings = {
    "bring_red_mug": {"best_plan_value": 0.92},
    "bring_blue_mug": {"best_plan_value": 0.41},
}
ask_cost = 0.05
no_question_value = 0.5 * 0.92 + 0.5 * 0.41
after_question_value = max(0.92, 0.41)
voi = round(after_question_value - no_question_value - ask_cost, 2)

print({"no_question": round(no_question_value, 2), "after_question": after_question_value, "voi": voi})
print("ask" if voi > 0 else "act")""",
    output_1="""{'no_question': 0.67, 'after_question': 0.92, 'voi': 0.2}
ask""",
    caption_1="This calculation shows why ambiguity should be treated as a planning variable, not only as a language score. Because the expected value gain from disambiguation exceeds the asking cost, the rational action is to clarify before moving.",
    shortcut="Dialogue managers, LangGraph state machines, and tool-calling APIs implement the same loop with a few nodes: detect ambiguity, ask, validate the reply, and replan. They hide the bookkeeping around state transitions and logging so the engineer can focus on the ambiguity test itself.",
    recipe_items=[
        "Maintain more than one candidate task object whenever the parse is not decisive.",
        "Measure plan disagreement, risk difference, or verifier difference across those candidates.",
        "Ask the smallest clarification question that collapses the uncertainty the most.",
        "Treat the user's reply as a state update, then rerun grounding and planning.",
        "Log the pre-question and post-question plan so ambiguity handling is auditable.",
    ],
    warning="A common failure mode is to ask too late, after the robot has already committed to a costly motion. Another is to ask too vaguely, which forces the human to restate the whole task instead of resolving the one missing variable.",
    practical_example="In a hospital room, 'bring me the chart on the table' may refer to several documents. If walking to the wrong side of the room is costly or disruptive, a two-second clarification question can save a minute of motion and a socially awkward recovery.",
    fun_note="Humans call it a clarifying question. Robots call it avoiding a future apology tour.",
    frontier="Research is shifting from one-shot instruction following toward mixed-initiative systems that decide when to ask, point, move for a better view, or request confirmation. The hard open problem is calibrating these interventions so they improve task success without becoming annoying or slow.",
    self_check="Can you name one task where the top-1 parse confidence looks high, but the difference between the top two meanings still justifies asking because the wrong choice would be costly or unsafe?",
    deep_dive_1="Clarification is best understood as a control action that changes the information state. It belongs in the same conceptual family as camera motion for better visibility or probing contact to reduce pose uncertainty. The agent spends time now to improve policy value later.",
    deep_dive_2="This framing also clarifies evaluation. A system that asks more questions is not automatically worse. It is worse only if those questions do not buy enough downstream value, such as safer execution, lower path length, or fewer catastrophic failures.",
    table_title="Tool Choices For Clarification and Replanning",
    table_rows=[
        ("LangGraph", "Stateful dialogue and replanning loops.", "Use it when ambiguity resolution spans several tool calls and planner updates."),
        ("BehaviorTree.CPP", "Execution trees with question, wait, and fallback branches.", "Use it when clarification is one branch among several recovery actions."),
        ("TEACh", "Benchmark for dialogue during embodied execution.", "Use it when you need a dataset where asking and acting are intertwined."),
        ("ROS 2 actions", "Cancelable skills during clarification.", "Use actions when the robot may need to pause or preempt a running behavior while asking."),
        ("Pydantic task objects", "Structured storage of multiple candidate meanings.", "Use them when ambiguity should survive across planner and verifier modules."),
    ],
    implementation_intro="Code Fragment 2 stores the ambiguity state and the chosen clarification question in one artifact. The planner can then compare the original and revised plan without losing the reason the question was asked.",
    implementation_items=[
        "Store the top candidate meanings instead of only the winner.",
        "Attach a question template to the specific slot that needs disambiguation.",
        "Pause or gate dangerous actions until the reply is received or a timeout fires.",
        "After the reply, re-run grounding and planning from the updated task object.",
        "Audit whether clarification improved success, safety, or efficiency on the same episode set.",
    ],
    code_2="""# Save ambiguity and the chosen clarification prompt for a single episode.
# The record links planner uncertainty to the intervention that resolves it.
# That makes later ablations on dialogue policy much cleaner.
clarification_record = {
    "slot": "target_object",
    "candidates": ["red_mug", "blue_mug"],
    "question": "Do you mean the red mug or the blue mug?",
    "action_gate": "wait_for_answer",
}
print(clarification_record)""",
    output_2="""{'slot': 'target_object', 'candidates': ['red_mug', 'blue_mug'], 'question': 'Do you mean the red mug or the blue mug?', 'action_gate': 'wait_for_answer'}""",
    caption_2="This record keeps the clarification event tied to the ambiguous slot and the paused action policy. The benefit is that later audits can ask whether the question targeted the right uncertainty and whether it improved the eventual plan.",
    teaching_move="Ask students to design one good and one bad clarification question for the same ambiguity. The contrast makes the information-value idea concrete very quickly.",
    failure_analysis="If the clarification loop underperforms, check whether ambiguity was detected too late, whether the wrong slot was queried, or whether the user reply failed to update the internal task object. These are distinct bugs with different remedies.",
    takeaway="Ambiguity handling is part of planning, not just part of conversation.",
    exercise="Construct a two-interpretation task where acting immediately is cheaper but risky, while asking first is slower but safer. Estimate the value of information and decide which policy you would deploy.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2110.00534", 'Padmakumar et al. (2022). "TEACh: Task-driven Embodied Agents that Chat." AAAI.', "TEACh is a key source for dialogue-driven clarification and task progress in embodied settings."),
        ("https://langchain-ai.github.io/langgraph/", "LangGraph Documentation.", "LangGraph is a practical reference for stateful LLM control loops with explicit replanning and tool routing."),
        ("https://arxiv.org/abs/2502.09560", 'Wang et al. (2025). "EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models as Embodied Agents." arXiv.', "EmbodiedBench is useful for thinking about evaluation protocols in embodied LLM systems, including interaction and replanning."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-31-language-guided-embodied-agents/section-31.6.html"] = section_payload(
    sid="31.6",
    chapter_title="Language-Guided Embodied Agents",
    topic="Human-agent interaction",
    checklist_1="This section must move beyond command following to mixed-initiative interaction, where the human and robot jointly shape the task state. Readers should know how corrections, preferences, and trust signals enter the loop.",
    checklist_2="The important artifact is an interaction trace containing user command, agent proposal, human correction, confidence or trust cue, and final action. Without that record, human-agent interaction becomes anecdotal rather than reproducible.",
    big_picture="<strong>Human-agent interaction</strong> is where language-guided embodiment becomes collaborative rather than merely obedient. The robot must maintain task progress while staying interruptible, legible, and easy to correct.",
    pathway="Read from command following to shared autonomy: represent user intent, expose the agent's current belief, and keep the interaction loop cheap enough that humans will actually use it.",
    develops="This section explains how embodied agents should communicate uncertainty, accept corrections, and trade autonomy against user oversight during ongoing tasks.",
    key_question="The practical question is how much authority to give the robot before it must surface uncertainty or defer to the human.",
    insight="Good interaction design minimizes correction cost. A system that is powerful but expensive to repair will quickly lose user trust.",
    theory_1="Let $u_t$ denote a human input at time $t$, such as a command, correction, or approval. A shared-control policy can be written as $$a_t \\sim \\pi(a_t \\mid h_t, x, u_{0:t}),$$ where the interaction history updates both task intent and trust calibration. The agent should not treat all human inputs equally: a correction signal often carries more control value than a new high-level command.",
    theory_2="Interaction quality depends on observability in both directions. The robot must observe the user's intent, but the user must also observe enough of the robot's internal state to predict what it will do next. Explanations, preview actions, and confidence signals therefore become part of the control interface, not just user-interface decoration.",
    mechanism="A useful design pattern is proposal, preview, confirm, execute, and revise. The agent proposes a plan or target, previews the risky part, accepts approval or correction, then executes while staying interruptible. This keeps autonomy high when things are clear and correction cost low when they are not.",
    worked_intro="Code Fragment 1 shows a simple interaction gate that chooses between direct execution and confirmation. The policy uses both uncertainty and action risk, because even a confident proposal may deserve review if the consequence is expensive.",
    code_1="""# Ask for confirmation when uncertainty or action risk is high.
# Human interaction is a control channel, not just a cosmetic interface.
# The gate should consider both confidence and consequence.
proposal_confidence = 0.58
action_risk = 0.72

need_confirmation = proposal_confidence < 0.7 or action_risk > 0.6
decision = "confirm" if need_confirmation else "execute"

print({"confidence": proposal_confidence, "risk": action_risk, "decision": decision})""",
    output_1="""{'confidence': 0.58, 'risk': 0.72, 'decision': 'confirm'}""",
    caption_1="This gate treats human confirmation as a principled control action triggered by uncertainty and consequence. The policy does not ask because it is weak; it asks because the expected cost of an unreviewed action is too high.",
    shortcut="Shared-autonomy interfaces in ROS 2, behavior trees, and GUI-based teleoperation stacks already provide approval, cancelation, and intervention hooks. Those tools remove interface plumbing so the system designer can focus on calibration, timing, and legibility.",
    recipe_items=[
        "Expose the agent's next intended action in a form the human can inspect quickly.",
        "Define explicit interrupt and override channels for high-risk actions.",
        "Treat corrections as informative state updates, not as episodic failure labels only.",
        "Measure user effort: confirmations, overrides, and repair time are core metrics.",
        "Tune the autonomy threshold on realistic tasks, because overly cautious systems become unusable.",
    ],
    warning="Human feedback loops fail when the robot asks too often, hides its state, or makes correction too expensive. All three issues can degrade trust even if raw task success remains high in short demos.",
    practical_example="In assistive manipulation, a user may allow the robot to fetch a bottle autonomously but demand confirmation before it moves near a fragile glass. A good interface lets that boundary be expressed and updated during the task, not only in a setup menu.",
    fun_note="Humans are remarkably patient with robots that ask sensible questions and remarkably unforgiving of robots that confidently carry the soup in the wrong direction.",
    frontier="The frontier here spans shared autonomy, interactive VLA systems, and socially aware embodied agents. Current benchmarks increasingly ask whether the agent can be corrected mid-task, explain risky choices, and preserve user preference over long horizons instead of only finishing one episode.",
    self_check="If a user interrupts the robot halfway through a task, can your system say which part of the internal plan changed and whether earlier assumptions were invalidated or merely updated?",
    deep_dive_1="Human-agent interaction is a good example of why embodied AI cannot be judged only by single-episode reward. The human is part of the loop, so the system should optimize for correction cost, legibility, and trust calibration in addition to nominal task success.",
    deep_dive_2="That perspective also changes how to think about demonstrations. A correction is not just a label saying 'wrong'; it is a structured intervention revealing where the human expected the robot's internal state to differ. Strong systems preserve that information for future planning and personalization.",
    table_title="Tool Choices For Human-Agent Interaction",
    table_rows=[
        ("ROS 2 actions and services", "Interruptible execution with feedback and cancelation.", "Use them when the human may need to pause, modify, or abort a running skill."),
        ("BehaviorTree.CPP", "Approval gates and fallback logic.", "Use it when confirmation and correction should be explicit branches in execution."),
        ("TEACh", "Dialogue-rich embodied task benchmark.", "Use it when interaction quality is part of the evaluation target."),
        ("LeRobot or teleoperation logs", "Correction traces and demonstration capture.", "Use them when interaction should feed back into learning from human guidance."),
        ("Shared-control GUI or web dashboard", "Preview and intervention surface.", "Use it when operator trust depends on seeing the next action before commitment."),
    ],
    implementation_intro="Code Fragment 2 stores a minimal interaction event with proposal, human response, and final execution decision. That event is the unit you need for studying trust, intervention rate, and correction efficiency.",
    implementation_items=[
        "Log the robot proposal before the user responds.",
        "Record whether the user approved, corrected, or overrode the action.",
        "Update the task state or policy threshold after the interaction, not only after episode end.",
        "Track intervention frequency together with success rate and completion time.",
        "Replay interaction traces to measure whether the same misunderstanding recurs across tasks.",
    ],
    code_2="""# Save one interaction event so trust and correction effort are measurable.
# The trace should show what the robot proposed and how the human changed it.
# That makes shared-autonomy audits much more concrete.
interaction_event = {
    "proposal": "pick(glass_3)",
    "human_feedback": "use the bottle instead",
    "updated_target": "bottle_2",
    "final_decision": "pick(bottle_2)",
}
print(interaction_event)""",
    output_2="""{'proposal': 'pick(glass_3)', 'human_feedback': 'use the bottle instead', 'updated_target': 'bottle_2', 'final_decision': 'pick(bottle_2)'}""",
    caption_2="This trace keeps the robot's mistaken proposal visible instead of overwriting history with the corrected action only. That makes it possible to measure how often interaction rescued the task and what kinds of misunderstandings users actually had to repair.",
    teaching_move="Have readers compare a system that logs only final actions with one that logs the interaction trace above. The missing information becomes obvious immediately.",
    failure_analysis="When interaction fails, separate perception or planning errors from interface design errors. A system may have good low-level control yet still be unusable because correction is too slow, too opaque, or too expensive for the human.",
    takeaway="Human-agent interaction is successful when autonomy and correction cost are balanced in the same control loop.",
    exercise="Design an interaction trace schema for an assistive robot that must ask before risky actions but otherwise stay autonomous. Include at least one metric for user effort and one for task progress.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2110.00534", 'Padmakumar et al. (2022). "TEACh: Task-driven Embodied Agents that Chat." AAAI.', "TEACh is a natural reference for interaction that updates hidden task state during execution."),
        ("https://pages.nist.gov/ARIAC_docs/en/2023.5.0/tutorials/tutorial_8.html", "ARIAC Tutorial. 'Move Robots with ROS2 Actions.'", "This tutorial is a practical reference for interruptible, feedback-rich action execution in ROS 2."),
        ("https://arxiv.org/abs/2503.16545", 'Zhou et al. (2025). "EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?" arXiv.', "EmpathyAgent shows how interaction quality and embodied action can be evaluated together in socially meaningful tasks."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.1.html"] = section_payload(
    sid="33.1",
    chapter_title="LLMs as Planners and Controllers",
    topic="What LLMs can and cannot do in embodied tasks",
    checklist_1="This section must separate semantic strengths from physical weaknesses. Readers should know exactly which parts of embodied competence can be offloaded to an LLM and which parts still demand grounded state, typed tools, and control feedback.",
    checklist_2="The artifact here is a planner trace with prompt state, proposed subgoals, tool calls, verifier outcomes, and latency. Without those fields, it is impossible to tell whether the LLM contributed real control value or just plausible narration.",
    big_picture="<strong>What LLMs can and cannot do in embodied tasks</strong> is a question about interface boundaries. LLMs are excellent at semantic decomposition, error explanation, and API selection, but weak at direct state estimation, tight feedback control, and physical constraint satisfaction.",
    pathway="Read by boundary setting: identify what the LLM proposes, what typed tools execute, what verifiers check, and what remains firmly in the domain of control and estimation.",
    develops="This section builds a clear contract for when an LLM should sit inside an embodied loop and when it should stay outside as an advisor or parser.",
    key_question="The practical question is not whether the LLM can describe the right action sequence, but whether that description can be turned into safe, low-latency, grounded behavior.",
    insight="Use the LLM for semantic search over plans and interfaces, not as a substitute for state estimation or servo control.",
    theory_1="A convenient decomposition is $$\\pi(a_t \\mid h_t) = \\kappa\\bigl(\\phi_\\text{LLM}(x_t, m_t), \\hat s_t\\bigr),$$ where $\\phi_\\text{LLM}$ proposes a symbolic or programmatic plan from language context $x_t$ and memory $m_t$, while $\\kappa$ is the grounded executor that consumes the proposal together with the current state estimate $\\hat s_t$. The executor, not the LLM, owns physical validity.",
    theory_2="This split explains both the promise and the limits. LLMs compress broad semantic priors into a small number of candidate subtasks or tool sequences. They do not directly measure friction, occlusion, latency, or actuator saturation. When papers claim strong embodied performance, the key question is how much the grounded stack contributes beyond the language model itself.",
    mechanism="Treat the LLM as a high-level search policy over task decompositions, code sketches, or tool calls. Every proposal must pass through typed interfaces, state checks, and local controllers that know the robot's embodiment and current scene.",
    worked_intro="Code Fragment 1 implements the smallest planner boundary: the LLM proposes one symbolic subgoal, but the executor only accepts it if the required tool and state preconditions are satisfied.",
    code_1="""# Accept an LLM proposal only when the grounded stack can execute it.
# The executor checks state and tool availability before acting.
# This boundary keeps semantic planning separate from physical validity.
proposal = {"step": "pick(red_mug)", "required_tool": "grasp"}
state = {"target_visible": True, "toolbox": {"grasp", "place"}}

can_execute = state["target_visible"] and proposal["required_tool"] in state["toolbox"]
decision = "execute" if can_execute else "replan"

print({"proposal": proposal["step"], "can_execute": can_execute, "decision": decision})""",
    output_1="""{'proposal': 'pick(red_mug)', 'can_execute': True, 'decision': 'execute'}""",
    caption_1="This boundary keeps the language model in the role it is good at, proposing a semantically meaningful step, while the grounded stack decides whether the current world state can support it. The important field is `can_execute`, because a plausible textual plan is worthless if the target is not visible or the tool is unavailable.",
    shortcut="Modern tool-calling APIs and structured-output runtimes turn the same boundary into a few lines by forcing the LLM to emit typed action objects. They absorb prompt formatting, JSON validation, and retry logic so the engineer can focus on the execution contract and verifier design.",
    recipe_items=[
        "Write down which variables the LLM sees and which variables only the grounded stack sees.",
        "Require every LLM proposal to map into a typed action or code object.",
        "Attach a verifier to every proposal so textual plausibility never counts as success by itself.",
        "Measure latency separately for planning, execution, and recovery.",
        "Benchmark against strong non-LLM baselines on the same task contract before claiming an embodied gain.",
    ],
    warning="A frequent failure mode is to confuse descriptive competence with control competence. An LLM may explain how to pour safely while still lacking any grounded estimate of the cup pose, liquid dynamics, or actuator limits needed to perform the action.",
    practical_example="In mobile manipulation, an LLM can select the sequence 'navigate to sink, grasp sponge, wipe spill,' but it should not be the module that estimates whether the sponge is currently visible or whether the arm can reach it without collision. Those checks belong to perception and planning tools that expose measurable state.",
    fun_note="Large language models are fantastic interns for whiteboard planning. They are much less convincing when asked to be gravity, friction, and depth sensors all at once.",
    frontier="Current embodied LLM work is moving from prompt-only planners toward typed tool use, verifier loops, and benchmark suites such as EmbodiedBench. The hard scientific question is whether LLMs add embodied value beyond semantic decomposition once strong world models, VLMs, and classic planners are already in place.",
    self_check="Can you point to one subproblem in your stack that genuinely benefits from broad language priors, and one subproblem where replacing a grounded estimator with an LLM would be irresponsible or pointless?",
    deep_dive_1="A useful scientific discipline is to evaluate LLM contribution at the intervention boundary. Replace the LLM planner with a hand-written planner, a behavior tree, or a retrieval baseline while keeping execution fixed. If performance barely changes, the embodied value comes from the grounded stack, not from the language model.",
    deep_dive_2="This also reframes the hype around end-to-end embodied agents. The core question is not whether a model can emit an action token, but whether it can maintain a physically valid internal state, meet timing budgets, and recover from embodiment-specific failures. Most current systems still rely heavily on specialized modules for those responsibilities.",
    table_title="Tool Choices Around the LLM Boundary",
    table_rows=[
        ("Structured tool calling", "Typed action proposals from the LLM.", "Use it when free-form text would make execution or evaluation ambiguous."),
        ("ROS 2 actions", "Execution of long-running robot skills with feedback.", "Use actions when the LLM proposes skills rather than continuous controls."),
        ("BehaviorTree.CPP", "Explicit fallback and retry logic.", "Use it when LLM proposals need a deterministic execution skeleton."),
        ("MoveIt 2", "Grounded motion planning and collision checking.", "Use it to execute geometric subgoals that an LLM can describe but not validate."),
        ("LangGraph", "Memory and planner state transitions.", "Use it when the planner must maintain multi-step conversational or tool context."),
    ],
    implementation_intro="Code Fragment 2 saves a planner trace with the fields needed for real evaluation. The key idea is that every proposal is logged alongside its verifier result and latency, so semantic fluency cannot hide execution failure.",
    implementation_items=[
        "Record the prompt context or task card that generated the proposal.",
        "Store the typed action, the verifier result, and the state preconditions checked before execution.",
        "Measure planning latency separately from skill-execution latency.",
        "Tag failures as semantic, state-estimation, tool-interface, or controller failures.",
        "Compare planner variants on the same execution stack and episode set.",
    ],
    code_2="""# Save one embodied planner step with a verifier result and latency.
# A semantic proposal counts only if the verifier can endorse execution.
# These fields are the minimum needed for construct-matched evaluation.
trace = {
    "planner_output": "pick(red_mug)",
    "verifier": "target_visible=True, grasp_available=True",
    "latency_ms": 184,
    "result": "executed",
}
print(trace)""",
    output_2="""{'planner_output': 'pick(red_mug)', 'verifier': 'target_visible=True, grasp_available=True', 'latency_ms': 184, 'result': 'executed'}""",
    caption_2="This trace turns a language-model step into an auditable control event. The important engineering discipline is that `planner_output`, `verifier`, and `latency_ms` are co-recorded, which makes it possible to compare semantic quality and execution cost in one artifact.",
    teaching_move="Ask readers to relabel each failure in a planner trace as semantic, grounded-state, or low-level control. The exercise quickly exposes how much of embodied performance sits outside the LLM.",
    failure_analysis="If an embodied LLM system underperforms, first ask whether the LLM chose the wrong subgoal, whether the tool interface was incomplete, or whether the grounded stack could not realize an otherwise good plan. Those are very different scientific conclusions.",
    takeaway="LLMs help embodied systems most when they are boxed into a typed planning role and surrounded by grounded verifiers and controllers.",
    exercise="Pick one embodied task and write a boundary contract for an LLM planner. List exactly which inputs it sees, which outputs it may emit, and which module rejects invalid proposals before execution.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2204.01691", 'Ahn et al. (2022). "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances." arXiv.', "SayCan is the cleanest starting point for understanding how an LLM can propose while grounded affordances dispose."),
        ("https://arxiv.org/abs/2502.09560", 'Wang et al. (2025). "EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models as Embodied Agents." arXiv.', "EmbodiedBench is a recent reference for evaluating embodied language systems across navigation and manipulation settings."),
        ("https://www.behaviortree.dev/docs/ros2_integration", "BehaviorTree.CPP Documentation. 'Integration with ROS2.'", "This documentation is a practical reference for surrounding language proposals with explicit execution logic and recovery branches."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.2.html"] = section_payload(
    sid="33.2",
    chapter_title="LLMs as Planners and Controllers",
    topic="SayCan: affordance-grounded planning",
    checklist_1="Readers should leave with the exact factorization used by SayCan and a clear view of why language plausibility alone is insufficient for robot planning. The section must also clarify where the affordance score comes from and what it assumes.",
    checklist_2="The artifact must record candidate skills, language-model probabilities, affordance values, the combined score, and the selected action. Only then can one audit whether the planner failed semantically or physically.",
    big_picture="<strong>SayCan</strong> is the canonical pattern for combining language priors with physical affordances. It lets the LLM suggest what sounds right while a grounded value function asks what is actually executable now.",
    pathway="Read the method as score composition: generate candidate skills, score them semantically, score them physically, then combine the two scores before execution.",
    develops="This section explains why affordance grounding is the natural antidote to free-text planning in robotics and why the combination is stronger than either source of evidence alone.",
    key_question="The practical question is how to combine semantic relevance and executability without letting one wash out the other.",
    insight="SayCan works because semantic plausibility and physical feasibility answer different questions. One says what the human probably wants next; the other says what the robot can actually do now.",
    theory_1="SayCan scores each candidate skill $k$ with a language prior and an affordance value: $$k^* = \\arg\\max_k \\; p_\\text{LLM}(k \\mid x, h_t) \\cdot V_k(s_t).$$ The language term prefers semantically appropriate next steps, while the value term estimates whether the robot can execute that step successfully in the current state.",
    theory_2="The multiplication matters. A skill with high semantic probability but near-zero affordance should be rejected, and a highly executable skill with no semantic relevance should not dominate just because it is easy. The method therefore depends on score calibration and on the quality of the candidate skill library.",
    mechanism="A good mental model is product-of-experts planning. The LLM narrows the skill search to task-consistent options, and the affordance model removes options that are impossible or low value in the current world state.",
    worked_intro="Code Fragment 1 implements the core SayCan score on three skills. The example is tiny, but it makes the product structure visible and shows how the selected action can differ from the highest language score alone.",
    code_1="""# Combine semantic plausibility with grounded affordance values.
# The best skill is not the one with the largest language score alone.
# Product scoring removes semantically attractive but infeasible actions.
skills = {
    "pick_sponge": {"p_llm": 0.55, "affordance": 0.92},
    "turn_on_sink": {"p_llm": 0.30, "affordance": 0.95},
    "wipe_spill": {"p_llm": 0.80, "affordance": 0.18},
}

combined = {name: round(v["p_llm"] * v["affordance"], 3) for name, v in skills.items()}
print(combined)
print(max(combined, key=combined.get))""",
    output_1="""{'pick_sponge': 0.506, 'turn_on_sink': 0.285, 'wipe_spill': 0.144}
pick_sponge""",
    caption_1="This score composition shows why `wipe_spill` loses even though it has the strongest semantic score. The current world state makes it a poor next action, so the product favors `pick_sponge`, which is both relevant and executable.",
    shortcut="The same idea can be implemented with a few lines using an LLM API plus an affordance model wrapped behind a typed tool interface. Those libraries remove prompt and schema boilerplate, but they do not remove the need to calibrate the affordance score and the candidate skill set.",
    recipe_items=[
        "Define a compact skill library whose actions expose clear preconditions and effects.",
        "Generate only semantically plausible skill candidates rather than scoring the entire API surface.",
        "Estimate affordance or value in the current state before execution, not from a stale scene snapshot.",
        "Normalize or calibrate the two scores so one term does not dominate by scale alone.",
        "Inspect failure cases where the right long-horizon plan starts with a low-probability semantic step.",
    ],
    warning="SayCan can fail if the candidate skill set is too narrow, the value functions are poorly calibrated, or the semantic model overprefers narratively obvious steps that are not optimal for the current embodiment.",
    practical_example="In kitchen cleanup, 'wipe the spill' sounds like the right next step, but the robot may first need to pick the sponge or move a blocking bowl. Affordance grounding keeps the planner from issuing impossible or premature skills.",
    fun_note="SayCan is the polite adult in the room. It lets the language model dream big, then asks whether the robot can actually reach the sponge before promising heroics.",
    frontier="Recent work extends the SayCan idea with better search, richer world models, and longer-horizon credit assignment, sometimes adding heuristic planners or learned payoff estimates on top of the original language-times-affordance product.",
    self_check="If a skill has the highest language score but the lowest affordance, do you know where that skill should still appear in the diagnostic trace and why it should not win execution?",
    deep_dive_1="The scientific subtlety in SayCan is calibration. The product formula is simple, but only meaningful if the two terms are roughly comparable in their interpretation. A miscalibrated value model can dominate the semantic term and reduce the planner to greedily choosing whichever skill is easiest right now.",
    deep_dive_2="The method also inherits the classic option-discovery problem from hierarchical RL. It can only select among skills it already knows. If the correct subtask is missing from the library, no amount of language fluency will recover it, which is why skill design and affordance learning remain central.",
    table_title="Tool Choices Around SayCan-style Planning",
    table_rows=[
        ("LLM API with structured outputs", "Candidate skill proposal.", "Use it when the skill library is large enough that language can prune it meaningfully."),
        ("RL or success-value model", "Affordance estimate for each skill.", "Use it when executability depends on the current scene and embodiment."),
        ("BehaviorTree.CPP", "Execution shell for chosen skills.", "Use it when each skill needs explicit retry and failure handling."),
        ("ROS 2 actions", "Typed skill invocation.", "Use actions when each selected skill is long running and needs feedback."),
        ("EmbodiedBench or task-specific simulator", "Construct-matched evaluation.", "Use a matched benchmark when comparing SayCan-style planners against simpler baselines."),
    ],
    implementation_intro="Code Fragment 2 stores the separate scores as an audit artifact rather than only the winning skill. This is the minimum needed to understand whether the semantic prior or the affordance estimator caused a bad decision.",
    implementation_items=[
        "Log the candidate skills and both scores for each decision point.",
        "Keep the value-estimation state snapshot or seed so scores can be reproduced.",
        "Store the chosen skill and the first rejected alternative for debugging.",
        "Measure how often the affordance term changes the top language choice.",
        "Benchmark with the same skill library and same execution stack when comparing alternatives.",
    ],
    code_2="""# Save both score terms so planner errors are attributable.
# The audit should show whether semantics or affordance dominated the decision.
# Storing only the winning skill hides the most useful evidence.
audit = {
    "chosen_skill": "pick_sponge",
    "semantic_score": 0.55,
    "affordance_score": 0.92,
    "combined_score": 0.506,
}
print(audit)""",
    output_2="""{'chosen_skill': 'pick_sponge', 'semantic_score': 0.55, 'affordance_score': 0.92, 'combined_score': 0.506}""",
    caption_2="This audit record keeps the two terms of the SayCan product separate, which is essential for failure analysis. If the planner chose poorly, this trace tells you whether the semantic prior, the affordance model, or their calibration was at fault.",
    teaching_move="Have students compare the same decision under product, sum, and lexicographic scoring. The differences make score-combination assumptions much easier to see.",
    failure_analysis="If the chosen skill is poor, first check candidate generation, then affordance calibration, then library coverage. SayCan errors often come from what is missing from the candidate set, not only from how the final score is computed.",
    takeaway="SayCan succeeds by treating language and affordance as complementary experts rather than competing controllers.",
    exercise="Construct a three-skill example where the top semantic choice is not executable and the top affordance choice is semantically irrelevant. Show how the product rule resolves the conflict and when it might still fail.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2204.01691", 'Ahn et al. (2022). "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances." arXiv.', "This is the primary SayCan source and the definitive reference for the language-times-affordance factorization."),
        ("https://arxiv.org/abs/2308.12682", 'Li et al. (2023). "SayCanPay: Heuristic Planning with Large Language Models using Learnable Domain Knowledge as Heuristics." arXiv.', "SayCanPay is a useful follow-on showing how the original idea can be extended with heuristic planning and payoff estimates."),
        ("https://moveit.picknik.ai/", "MoveIt 2 Documentation.", "MoveIt is relevant because many SayCan-style systems still hand off chosen subgoals to classical geometric planning stacks."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.3.html"] = section_payload(
    sid="33.3",
    chapter_title="LLMs as Planners and Controllers",
    topic="Code as Policies: LLMs that write robot code",
    checklist_1="This section must explain why generating code can be a better interface than generating free-text plans, and what extra safety and verification obligations that choice creates.",
    checklist_2="The key artifact is the generated program, the typed API surface it is allowed to call, the unit tests or runtime checks applied to it, and the execution result on the same episode.",
    big_picture="<strong>Code as Policies</strong> treats the LLM as a program synthesizer rather than as a pure step selector. The gain is compositionality; the cost is that unsafe or underspecified code can execute surprisingly fast.",
    pathway="Read from DSL design to verification: define the safe API surface, generate code against it, test the code, then execute only after the verifier passes.",
    develops="This section shows why code generation is attractive for embodied control and why it only works when the runtime interface is narrow, typed, and testable.",
    key_question="The practical question is what kind of code the model should be allowed to write and how that code should be checked before touching the robot.",
    insight="Generated code is powerful because it can bind perception, memory, and action in one program. It is dangerous for exactly the same reason.",
    theory_1="Instead of selecting one symbolic action, the model emits a program $P$ over a robot API $\\mathcal A$. The control loop becomes $$P = \\phi_\\text{LLM}(x, h_t), \\qquad a_{t:t+H} = \\operatorname{Exec}(P, \\mathcal A, \\hat s_t),$$ where safety now depends on the allowed API, runtime guards, and verification suite as much as on the model's semantic quality.",
    theory_2="Code generation helps when tasks require loops, conditionals, and compositional reuse across subtasks. A free-text planner may say 'repeat until the drawer is closed'; a generated program can actually encode the loop condition. The downside is that the model can also generate brittle logic or unsafe API sequences if the execution environment is too permissive.",
    mechanism="A good mental model is constrained program synthesis. The LLM writes a small controller inside a sandbox, not arbitrary Python with unrestricted side effects. The narrower the API and the clearer its contracts, the more useful and safer the generated code becomes.",
    worked_intro="Code Fragment 1 generates a tiny skill program over a restricted API and then validates that every called function is allowed. The point is to make the interface boundary concrete, not to celebrate raw text generation.",
    code_1="""# Validate that generated code calls only approved robot API functions.
# Program generation is useful only when the execution surface is constrained.
# A whitelist is the smallest possible runtime guard.
generated_calls = ["detect('red_mug')", "pick('red_mug')", "place('tray')"]
allowed = {"detect", "pick", "place", "wait"}

safe = all(call.split("(")[0] in allowed for call in generated_calls)
print({"calls": generated_calls, "safe": safe})""",
    output_1="""{'calls': ["detect('red_mug')", "pick('red_mug')", "place('tray')"], 'safe': True}""",
    caption_1="This whitelist check shows the minimum discipline required for code generation in robotics. The generated program is only useful if every call lands inside an approved API surface whose side effects and failure modes are already known.",
    shortcut="Program-of-thought runtimes, sandboxed Python interpreters, and tool-calling APIs can wrap the same pattern in a few lines. They remove the string plumbing and schema parsing, but they do not remove the need for runtime guards, unit tests, and state-based verification.",
    recipe_items=[
        "Expose a narrow API that names only the skills and queries the robot is allowed to call.",
        "Generate code into a sandbox or DSL rather than into unrestricted Python.",
        "Run static and runtime checks before sending any call to the robot.",
        "Log the generated program and the verifier result together.",
        "Treat repair and regeneration as first-class parts of the loop rather than as exceptional events.",
    ],
    warning="The most common mistake is to let the generated code touch too much of the runtime surface. The model does not need file system access, shell access, or arbitrary network calls to solve a tabletop manipulation task.",
    practical_example="A generated policy may combine `detect`, `pick`, and `place` with a retry loop that re-detects after slippage. That compositional pattern is much easier to express in code than as a list of flat symbolic actions, but only if the allowed functions are clean and testable.",
    fun_note="Free-text plans make optimistic promises. Generated code makes those promises executable, which is either progress or a very efficient way to meet your safety team.",
    frontier="Recent work pushes from unrestricted code generation toward safer DSLs, repair loops, and verifier-guided synthesis. The open question is how expressive the language can be before the safety and debugging burden outweigh the compositional benefit.",
    self_check="If your model generated a loop or conditional, could you explain which runtime guard proves that the code will terminate or fail safely under missing detections?",
    deep_dive_1="Code generation changes the abstraction level of planning. Instead of choosing the next action only, the model can synthesize local control flow and data flow. That is why program-based interfaces often generalize better than step-wise prompts on long tasks with repeated patterns.",
    deep_dive_2="The cost is that verification must move closer to software engineering. You need typed signatures, unit tests, API whitelists, and runtime contracts, not just high-level task metrics. A generated program is a real artifact, and it deserves real software scrutiny before it reaches hardware.",
    table_title="Tool Choices For Programmatic Robot Policies",
    table_rows=[
        ("Sandboxed Python or a DSL", "Generated control logic surface.", "Use it when free-form text is too weak but unrestricted code is too risky."),
        ("Pydantic or JSON schema", "Validation of generated arguments.", "Use it when the generated program must pass typed objects to robot APIs."),
        ("ROS 2 actions", "Execution target for generated procedures.", "Use actions when generated code should call long-running, feedback-rich skills."),
        ("MoveIt 2", "Safe motion-planning backend.", "Use it when generated code specifies high-level manipulation goals rather than trajectories."),
        ("Unit tests and replay harnesses", "Program verification before execution.", "Use them to catch invalid calls or wrong control flow before the robot moves."),
    ],
    implementation_intro="Code Fragment 2 stores the generated program and its verifier result in one record. That is the right unit for ablations because it lets you compare program quality, execution success, and repair frequency together.",
    implementation_items=[
        "Save the generated program text or AST in the experiment artifact.",
        "Run signature checks, whitelist checks, and simple execution tests before deployment.",
        "Keep the generated program short enough that a human can audit it during development.",
        "If verification fails, route the error message back into a regeneration step rather than guessing a patch silently.",
        "Compare program-generation systems on the same API surface and same robot backend.",
    ],
    code_2="""# Save the generated program together with the verification outcome.
# This artifact supports code-quality and embodiment-quality analysis at once.
# Repair loops are much easier to study when the failed program is preserved.
program_record = {
    "program": "detect('red_mug'); pick('red_mug'); place('tray')",
    "verification": "passed_api_whitelist",
    "execution_result": "success",
}
print(program_record)""",
    output_2="""{'program': "detect('red_mug'); pick('red_mug'); place('tray')", 'verification': 'passed_api_whitelist', 'execution_result': 'success'}""",
    caption_2="This record preserves the generated program as a first-class experimental artifact. That is essential because code-based failures are often easier to fix from the original program than from a bare task-success label.",
    teaching_move="Ask readers to intentionally generate one unsafe call and watch the verifier reject it. The rejection is a better teaching moment than another successful demo.",
    failure_analysis="When code-based planners fail, separate semantic plan errors from software-interface errors. The model may understand the task but still misuse an argument order, forget a termination condition, or violate a runtime precondition.",
    takeaway="Generated code is a strong embodied-planning interface only when the API surface is narrow, typed, and aggressively verified.",
    exercise="Design a five-function robot DSL for a tabletop domain and explain why each function belongs in the allowed set. Then list two functions that should remain unavailable to the LLM and why.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2209.07753", 'Liang et al. (2022). "Code as Policies: Language Model Programs for Embodied Control." arXiv.', "This is the primary reference for using LLM-generated programs as embodied-control policies."),
        ("https://docs.ros.org/en/foxy/Tutorials/Intermediate/Creating-an-Action.html", "ROS 2 Documentation. 'Creating an action.'", "ROS 2 actions are a practical target interface for generated high-level code in robot systems."),
        ("https://www.behaviortree.dev/docs/ros2_integration", "BehaviorTree.CPP Documentation. 'Integration with ROS2.'", "Behavior trees are a strong comparison point when deciding whether generated code or explicit execution graphs are the better abstraction."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.4.html"] = section_payload(
    sid="33.4",
    chapter_title="LLMs as Planners and Controllers",
    topic="VoxPoser: composing 3D value maps",
    checklist_1="Readers should understand how VoxPoser turns language into spatial value and constraint maps, and why this is stronger than free-text action selection for manipulation.",
    checklist_2="The artifact should contain the language instruction, the generated value maps, the optimized trajectory or pose, and the execution outcome. Otherwise the spatial grounding step disappears inside the demo.",
    big_picture="<strong>VoxPoser</strong> grounds language into 3D value maps that a motion planner can optimize over. The representation is powerful because it converts semantic preferences and constraints into a geometry the planner already understands.",
    pathway="Read from language to geometry: the LLM proposes what map to build, the VLM and scene model construct that map, and the optimizer converts it into a feasible end-effector trajectory.",
    develops="This section shows how an LLM can stay useful in manipulation once its outputs become spatial maps instead of free text or brittle symbolic steps.",
    key_question="The practical question is how language should shape a 3D objective without bypassing geometric planning and collision reasoning.",
    insight="Spatial value maps are a natural interface between semantic intent and classical optimization.",
    theory_1="VoxPoser represents language-conditioned objectives as voxelized value and constraint maps. A planner then searches for a trajectory $\\tau$ that maximizes integrated value while respecting constraints, for example $$\\tau^* = \\arg\\max_\\tau \\sum_{t=0}^{T} V_x(p_t) - \\lambda C_x(p_t),$$ where $p_t$ are end-effector poses, $V_x$ is a language-conditioned affordance map, and $C_x$ is a constraint or collision cost map.",
    theory_2="This matters because free-text plans like 'move above the mug, then approach from the side' are hard to execute directly. A value map expresses the same semantics in the planner's native language: spatial preference over poses. The optimizer can then handle smoothness, collision, and dynamics with standard tools.",
    mechanism="Think of VoxPoser as translation between description space and optimization space. The LLM and VLM identify which regions should be attractive or forbidden, and the motion planner solves the rest.",
    worked_intro="Code Fragment 1 builds a one-dimensional toy value map and shows how the best pose changes when language and constraints are composed. The toy numbers are not the point; the compositional interface is.",
    code_1="""# Compose a small value map with a constraint penalty.
# The optimizer should favor high-value cells that remain physically safe.
# This is the essence of the VoxPoser interface in miniature.
value = [0.1, 0.4, 0.9, 0.6, 0.2]
constraint = [0.0, 0.0, 0.7, 0.1, 0.0]

score = [round(v - c, 2) for v, c in zip(value, constraint)]
best_cell = max(range(len(score)), key=lambda i: score[i])

print(score)
print(best_cell)""",
    output_1="""[0.1, 0.4, 0.2, 0.5, 0.2]
3""",
    caption_1="This toy map shows why the peak of the raw value map is not always the best execution target. Cell `2` had the highest value before penalties, but the composed score favors cell `3` because the original peak violated the stronger constraint.",
    shortcut="Libraries for voxel processing, point clouds, and motion planning collapse most of the representation plumbing into a few calls. The real engineering work then becomes map design, calibration, and deciding which semantic cues should affect value versus hard constraints.",
    recipe_items=[
        "Build a scene representation that supports language-conditioned voxel or point-based scoring.",
        "Separate attractive maps from forbidden or high-cost maps instead of mixing them too early.",
        "Compose maps before optimization so the planner sees one coherent objective.",
        "Hand the result to a classical motion planner or MPC stack rather than bypassing geometry checks.",
        "Visualize the maps during debugging, because silent spatial mistakes are easy to miss in text logs alone.",
    ],
    warning="The easiest way to oversell VoxPoser is to show successful scenes with perfect maps. Real systems fail when object localization is off, masks are incomplete, or the language-generated constraints are too weak to carve out unsafe regions.",
    practical_example="For 'put the apple into the bowl without touching the knife,' the system can build a positive map over the bowl interior and a negative map near the knife. The resulting trajectory optimization problem is far more stable than trying to execute a free-text explanation directly.",
    fun_note="VoxPoser is what happens when an LLM learns that the motion planner speaks fluent geometry and would prefer fewer speeches.",
    frontier="Recent 3D grounding work combines voxel maps, Gaussian splats, and keypoint constraints with language-conditioned planners. The open problem is how to keep these spatial objectives stable under clutter, viewpoint change, and contact-rich dynamics.",
    self_check="Can you explain why a map-based interface lets a classical optimizer do the hard geometric work, and why that is often better than asking the LLM for an explicit trajectory?",
    deep_dive_1="VoxPoser is a good example of respecting abstraction boundaries. The LLM handles semantic decomposition and map composition. The planner handles feasibility, smoothness, and collision. Each module speaks in the representation where it is strongest.",
    deep_dive_2="This also suggests a clean evaluation strategy: compare map quality separately from planner quality, then compare the full stack. If the planner is fixed and performance changes, the value probably comes from better spatial grounding rather than from hidden execution tweaks.",
    table_title="Tool Choices For Spatial Language Planning",
    table_rows=[
        ("VoxPoser reference code", "Language-to-value-map composition.", "Use it when you want a concrete implementation of the map interface."),
        ("Open3D or voxel libraries", "Scene discretization and point-cloud processing.", "Use them when the planner needs explicit spatial support from RGB-D data."),
        ("MoveIt or MPC stack", "Trajectory optimization under geometry and collision constraints.", "Use them when the value map should shape but not replace motion planning."),
        ("SAM 2 or open-vocabulary VLM", "Object localization feeding map composition.", "Use them when language must be grounded before the value map is built."),
        ("Nerfstudio or 3D scene representation tools", "Richer spatial context for long-horizon manipulation.", "Use them when static depth snapshots are too weak for the task."),
    ],
    implementation_intro="Code Fragment 2 stores the language-conditioned spatial objective as an audit record. That record is the right place to compare map composition strategies, because it preserves the chosen target cell and the planner-facing score.",
    implementation_items=[
        "Save the positive and negative map summaries alongside the chosen pose or trajectory.",
        "Record the scene frame and resolution so map quality is reproducible.",
        "Visualize planner decisions against the underlying map before touching hardware.",
        "Benchmark with the same motion planner when comparing mapping strategies.",
        "Log whether execution failed because the map was wrong or because the optimizer could not realize a good map.",
    ],
    code_2="""# Record the spatial objective that the optimizer actually consumed.
# The chosen pose is meaningful only together with the map summary behind it.
# This keeps semantic grounding and motion planning tied together in one artifact.
spatial_record = {
    "instruction": "place the mug on the clear part of the table",
    "target_cell": 3,
    "score_at_target": 0.5,
    "planner": "mppi",
}
print(spatial_record)""",
    output_2="""{'instruction': 'place the mug on the clear part of the table', 'target_cell': 3, 'score_at_target': 0.5, 'planner': 'mppi'}""",
    caption_2="This record keeps the chosen spatial target attached to the language-conditioned score the optimizer actually saw. That is crucial when comparing better language grounding against better motion planning, because the trace exposes which layer changed.",
    teaching_move="Have readers move the penalty map and watch the target cell migrate. The exercise builds immediate intuition for how constraints reshape a planner-facing objective.",
    failure_analysis="If VoxPoser-style systems fail, separate scene-model failures, map-composition failures, and optimizer failures. These layers interact, but they should still be debugged as distinct interfaces.",
    takeaway="VoxPoser is compelling because it translates language into the spatial objective that motion planners already know how to optimize.",
    exercise="Design a positive map and a negative map for the command 'grasp the mug by the handle while avoiding the hot soup surface.' State which source module provides each map and which planner consumes the result.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2307.05973", 'Huang et al. (2023). "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models." CoRL.', "This is the primary VoxPoser source and the reference for language-conditioned 3D value-map composition."),
        ("https://github.com/nerfstudio-project/gsplat", "gsplat Documentation and Repository.", "gsplat is relevant for efficient 3D scene representations that can support richer spatial grounding."),
        ("https://moveit.picknik.ai/", "MoveIt 2 Documentation.", "MoveIt remains a practical execution backend for many manipulation pipelines that use language-conditioned spatial targets."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.5.html"] = section_payload(
    sid="33.5",
    chapter_title="LLMs as Planners and Controllers",
    topic="ReKep: relational keypoint constraints",
    checklist_1="Readers should understand why keypoint relations can express tasks more compactly than dense maps or free-text constraints, and what assumptions that representation makes about perception quality.",
    checklist_2="The artifact should include the keypoints, the relational constraints, the cost value, and the executed trajectory so one can see whether failure came from perception or optimization.",
    big_picture="<strong>ReKep</strong> uses relational keypoints to express manipulation goals in a form that optimizers can understand directly. It is a middle ground between symbolic steps and dense spatial maps.",
    pathway="Read from perception to optimization: detect task-relevant keypoints, express the task as relations among them, then optimize a trajectory that satisfies those relations.",
    develops="This section explains how language-guided agents can turn a command into a small set of geometric constraints over keypoints and then solve the resulting optimization problem.",
    key_question="The practical question is when relational keypoints are expressive enough to encode the task and when they become too brittle under clutter or contact.",
    insight="Keypoint constraints are powerful because they capture geometry with far less state than a full scene map, but they rely on the keypoints being the right abstraction.",
    theory_1="Let keypoints be $k_1, \\ldots, k_n$ and let a task be encoded by costs over relations among them. A trajectory optimizer can solve $$\\tau^* = \\arg\\min_\\tau \\sum_j w_j c_j\\bigl(k_{a_j}(\\tau), k_{b_j}(\\tau)\\bigr),$$ where each $c_j$ measures a relation such as distance, alignment, or ordering implied by the language command.",
    theory_2="This representation is attractive because it compresses a task into a few geometric relations that classical optimizers handle well. It is risky because errors in keypoint detection or object identity propagate directly into the objective, which can yield confident but wrong trajectories.",
    mechanism="A good mental model is language to geometric predicates. The LLM or VLM identifies which relations matter, the vision system instantiates the keypoints, and the optimizer pushes the robot toward states that satisfy those relations.",
    worked_intro="Code Fragment 1 evaluates a tiny relational cost between two keypoints. The specific numbers are simple, but they show how the language-derived objective becomes a concrete quantity an optimizer can minimize.",
    code_1="""# Compute a simple relational keypoint cost for a grasp target.
# The task prefers the gripper keypoint to align closely with the mug handle.
# Small geometric costs are what the optimizer ultimately tries to drive down.
gripper = (0.42, 0.18)
handle = (0.47, 0.21)

cost = round(abs(gripper[0] - handle[0]) + abs(gripper[1] - handle[1]), 3)
print({"l1_alignment_cost": cost})""",
    output_1="""{'l1_alignment_cost': 0.08}""",
    caption_1="This cost turns a language-grounded relation, align the gripper with the handle, into a concrete optimization target. Once the relation is instantiated geometrically, a standard optimizer can work with it without reading the original sentence again.",
    shortcut="Keypoint detectors, VLM-grounded correspondences, and optimization libraries can produce the same pipeline in a few lines. The shortcut removes most of the tensor and geometry plumbing, but it cannot remove the need to decide which relations matter for the task.",
    recipe_items=[
        "Choose keypoints that correspond to task-relevant geometry such as handles, rims, hinges, or contact patches.",
        "Translate the command into a small set of relational costs rather than a bag of verbal hints.",
        "Estimate keypoint confidence and reject tasks whose geometry is too uncertain for safe optimization.",
        "Use a planner or optimizer that can expose the final cost breakdown for debugging.",
        "Compare keypoint-based and map-based formulations on the same task to see which abstraction is more stable.",
    ],
    warning="Relational keypoints can look elegant in sparse scenes and fragile in clutter. If the wrong point is chosen or a keypoint disappears under occlusion, the optimizer may happily satisfy the wrong relation.",
    practical_example="For 'open the drawer by the handle,' a keypoint formulation can attach one point to the drawer handle and another to the gripper target, then optimize the relative pose. This is often far lighter than maintaining a dense 3D objective over the entire scene.",
    fun_note="Keypoints are the minimalist's answer to scene understanding: why carry the whole kitchen in memory if three strategically chosen points already tell you where the handle is?",
    frontier="Recent relational-manipulation work explores stronger keypoint discovery, temporally stable correspondences, and hybrid systems that switch between keypoints and denser scene maps when clutter or contact demands it.",
    self_check="Can you explain which keypoints in your task are semantically meaningful and which ones are merely easy for a detector to find but irrelevant for control?",
    deep_dive_1="ReKep is appealing because it lets language specify relations rather than every detail of a trajectory. That makes it a strong bridge between semantic tasking and numeric optimization, especially for manipulation tasks with a few dominant geometric constraints.",
    deep_dive_2="The limit is representational mismatch. Some tasks really are low dimensional in terms of keypoints. Others depend on extended surfaces, fluids, or occluded contacts. A strong engineer knows when the compact representation is a help and when it is a trap.",
    table_title="Tool Choices For Relational Keypoint Planning",
    table_rows=[
        ("ReKep paper and code", "Reference implementation of keypoint-constrained planning.", "Use it when you want a concrete manipulation example built around relational costs."),
        ("Keypoint or correspondence detector", "Instantiates task-relevant geometric anchors.", "Use a temporally stable detector when the task spans several viewpoints."),
        ("Optimization library or MPC", "Consumes the relational cost.", "Use it when the keypoint objective should become a physically feasible trajectory."),
        ("MoveIt 2", "Motion-planning shell around relational goals.", "Use it when keypoint constraints need collision-aware trajectory generation."),
        ("Open3D", "Coordinate transforms and geometry utilities.", "Use it when keypoints must be reconciled across frames or sensors."),
    ],
    implementation_intro="Code Fragment 2 saves the keypoint relation and its cost value as part of the experiment record. This is the right level of detail for deciding whether failure came from the vision front end or the optimizer.",
    implementation_items=[
        "Log keypoint identities, coordinates, confidence, and frame.",
        "Store the relational costs that define the objective, not only the final trajectory.",
        "Record whether the keypoints were visible, predicted, or carried from memory.",
        "Compare optimizer output against the same keypoints under repeated seeds or perturbations.",
        "Fallback to clarification or a denser representation when keypoint confidence collapses.",
    ],
    code_2="""# Preserve the relational objective that guided optimization.
# This makes it possible to compare perception and optimization failures cleanly.
# A trajectory label alone is too coarse for debugging.
rekep_record = {
    "keypoints": ["gripper_tip", "mug_handle"],
    "relation": "align_and_approach",
    "cost": 0.08,
    "planner": "trajopt",
}
print(rekep_record)""",
    output_2="""{'keypoints': ['gripper_tip', 'mug_handle'], 'relation': 'align_and_approach', 'cost': 0.08, 'planner': 'trajopt'}""",
    caption_2="This record makes the geometric abstraction explicit: the optimizer is not trying to satisfy the whole language command directly, but the relation `align_and_approach` over a small keypoint set. That clarity is essential for debugging the perception-planning interface.",
    teaching_move="Ask readers to rewrite one dense map objective as a keypoint relation and one keypoint relation as a dense map. The conversion reveals the strengths and blind spots of both abstractions.",
    failure_analysis="If ReKep-style planning fails, inspect keypoint quality first, then relation design, then trajectory optimization. It is easy to blame the optimizer for what is actually a mis-specified or unstable geometric abstraction.",
    takeaway="Relational keypoints are a strong language-to-optimization interface when the task geometry is low dimensional and the keypoints are semantically meaningful.",
    exercise="Choose a manipulation task and propose three keypoints plus two relational costs that express it. Then describe one scene variation where this abstraction would likely break and need a denser representation.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2409.01652", 'Huang et al. (2024). "ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation." arXiv.', "This is the primary ReKep reference for expressing manipulation tasks through relational keypoint constraints."),
        ("https://moveit.picknik.ai/", "MoveIt 2 Documentation.", "MoveIt is relevant when relational constraints must become collision-aware robot trajectories."),
        ("https://github.com/isl-org/Open3D", "Open3D Documentation and Repository.", "Open3D is a practical geometry toolkit for point and keypoint manipulation across frames."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.6.html"] = section_payload(
    sid="33.6",
    chapter_title="LLMs as Planners and Controllers",
    topic="Tool use, action APIs, plan verification, replanning",
    checklist_1="This section must explain how an LLM chooses among tools, how typed action APIs constrain execution, and how verifier failures trigger replanning rather than silent drift.",
    checklist_2="The minimum artifact records the selected tool, its arguments, the verifier output, the replanning trigger, and the new plan. Without these fields, tool-use claims are impossible to audit.",
    big_picture="<strong>Tool use and replanning</strong> is where embodied LLM systems stop being chatbots with access to robots and become control architectures. Typed APIs and verifiers make the difference.",
    pathway="Read as a loop: choose a tool, execute through a typed interface, verify the result, then either continue or replan from the updated state.",
    develops="This section connects LLM planning to the practical machinery of action APIs, typed arguments, postconditions, and replanning under failure.",
    key_question="The practical question is not only which tool to call, but what evidence should force the planner to abandon the current plan and synthesize a new one.",
    insight="A tool call without a verifier is just a wish. Replanning starts when the verifier says the wish did not come true.",
    theory_1="Let $u_i$ be typed tools and let $v_i(s_t, a_t)$ be a verifier for the postcondition of tool $u_i$. An embodied planner executes a loop $$u_t, \\theta_t = \\phi_\\text{LLM}(h_t), \\qquad y_t = u_t(\\theta_t), \\qquad b_t = v_t(y_t, s_{t+1}),$$ then continues only if the boolean or scalar verifier signal $b_t$ passes a threshold.",
    theory_2="This structure matters because embodied actions are long running and failure prone. A free-text chain of thought may say 'now place the mug on the tray,' but the actual robot needs a typed `place(target='tray')` call, a completion signal, and a postcondition check such as `object_on_tray=True` before the next reasoning step can be trusted.",
    mechanism="The clean mental model is planner, tool, verifier, replan. Every transition should be explicit and typed. If the verifier fails, the planner does not merely continue with reduced confidence; it reasons over a new state that includes the failure evidence.",
    worked_intro="Code Fragment 1 models a single tool-call decision with verification and replanning. The point is to expose the contract between textual planning and executable interfaces.",
    code_1="""# Verify every tool call before advancing the high-level plan.
# Failed postconditions should trigger replanning from the new world state.
# This is the smallest useful embodied tool-use loop.
tool_call = {"tool": "pick", "args": {"target": "red_mug"}}
postcondition = {"grasp_success": False}

next_step = "replan" if not postcondition["grasp_success"] else "continue"
print({"tool": tool_call["tool"], "postcondition": postcondition, "next_step": next_step})""",
    output_1="""{'tool': 'pick', 'postcondition': {'grasp_success': False}, 'next_step': 'replan'}""",
    caption_1="This loop makes the replanning trigger explicit. The planner does not advance just because the `pick` tool returned; it advances only if the postcondition confirms the intended world change actually happened.",
    shortcut="Structured tool-calling runtimes and workflow frameworks like LangGraph implement most of this control shell in a few lines. They absorb message passing and state updates, but the engineer still owns typed arguments, verifier design, and failure semantics.",
    recipe_items=[
        "Define each tool with typed arguments, explicit preconditions, and explicit postconditions.",
        "Run a verifier after every consequential tool call.",
        "Store tool failures as state updates, not as logging afterthoughts.",
        "Replan from the updated state rather than repeating the old chain of thought verbatim.",
        "Keep tool sets small and semantically distinct so tool choice remains learnable and auditable.",
    ],
    warning="Many demos treat tool return values as if they were proof of world change. In robotics that is unsafe: the API may report completion while the gripper is empty, the object slipped, or the robot timed out mid-motion.",
    practical_example="A mobile manipulator may call `navigate(goal='sink')`, then `pick(target='sponge')`, then `wipe(region='spill')`. Each tool should expose a verifiable postcondition. If the sponge is not actually grasped, it is meaningless to continue the scripted sequence.",
    fun_note="The robot's favorite fiction genre is the API that says 'completed successfully' while the mug is still on the table.",
    frontier="The frontier here is not just more tools, but better contracts between language models and robot middleware: typed schemas, richer failure reports, stronger verifiers, and planning systems that treat errors as informative state rather than as dead ends.",
    self_check="Can you name one postcondition in your stack that is currently assumed rather than measured, and what kind of false progress that assumption could create?",
    deep_dive_1="Tool use in embodied settings differs sharply from tool use in text-only agents. A web-search call either returned a result or did not; a robot-skill call may return while the world remains in the wrong state. That is why postcondition verification is structurally central, not merely best practice.",
    deep_dive_2="Replanning also deserves a precise meaning. It is not simply re-prompting the model. It is re-prompting on an updated state that includes fresh observations, failure evidence, elapsed time, and possibly depleted resources or changed safety margins.",
    table_title="Tool Choices For Typed Embodied Action Loops",
    table_rows=[
        ("LangGraph", "Planner state, tool routing, and retry loops.", "Use it when you want explicit graph structure around LLM tool use."),
        ("ROS 2 actions", "Typed skill invocation with feedback and cancelation.", "Use actions when tools map to robot skills rather than instant function calls."),
        ("BehaviorTree.CPP", "Fallback and recovery orchestration.", "Use it when verifier failures should branch into deterministic recovery logic."),
        ("MoveIt 2", "Geometric planning behind action APIs.", "Use it when high-level tools need reliable motion generation."),
        ("Pydantic or JSON schema", "Argument validation for tool calls.", "Use them to reject malformed plans before any execution request leaves the planner."),
    ],
    implementation_intro="Code Fragment 2 preserves the tool call, verifier outcome, and replanning reason in one record. That is the correct unit for comparing agent frameworks because it captures whether failures were caught early enough to matter.",
    implementation_items=[
        "Log each tool call with arguments and timestamps.",
        "Store the verifier result and the specific violated postcondition.",
        "Pass the verifier message into the replanning prompt or state graph.",
        "Track how often replanning fixed the task versus only delaying failure.",
        "Evaluate tool-use agents on the same tool set and verifier suite when making comparisons.",
    ],
    code_2="""# Save one failed tool call and the reason replanning was triggered.
# This record is the bridge between execution logs and planner reasoning.
# Without it, failure analysis stays vague.
tool_record = {
    "tool": "pick",
    "args": {"target": "red_mug"},
    "verifier": "grasp_success=False",
    "replan_reason": "target slipped during closure",
}
print(tool_record)""",
    output_2="""{'tool': 'pick', 'args': {'target': 'red_mug'}, 'verifier': 'grasp_success=False', 'replan_reason': 'target slipped during closure'}""",
    caption_2="This record keeps the replanning trigger concrete by naming the failed postcondition and its explanation. That makes later comparisons between agent frameworks much more meaningful than a bare task-failure label would be.",
    teaching_move="Ask students to redesign one tool in their stack so it exposes a better postcondition. The exercise often improves the whole architecture more than tuning the prompt does.",
    failure_analysis="If tool-using agents underperform, inspect whether the tool schema is weak, the verifier is weak, or the replanning state update is weak. Those three interfaces are where most embodied LLM loops actually break.",
    takeaway="Typed tools, postcondition verifiers, and explicit replanning are the core of practical embodied LLM control loops.",
    exercise="Design one typed action API and one postcondition verifier for a robot skill of your choice. Then describe the replanning information that should be passed back to the LLM if the verifier fails.",
    bibliography_entries=[
        ("https://langchain-ai.github.io/langgraph/", "LangGraph Documentation.", "LangGraph is a practical reference for explicit stateful tool-use loops around LLM planners."),
        ("https://docs.ros.org/en/foxy/Tutorials/Intermediate/Creating-an-Action.html", "ROS 2 Documentation. 'Creating an action.'", "ROS 2 actions are a canonical typed interface for embodied tools with feedback and cancelation."),
        ("https://www.behaviortree.dev/docs/ros2_integration", "BehaviorTree.CPP Documentation. 'Integration with ROS2.'", "Behavior trees provide a well-tested execution shell for tool verification and recovery."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.7.html"] = section_payload(
    sid="33.7",
    chapter_title="LLMs as Planners and Controllers",
    topic="Memory, state tracking, and hallucination in physical tasks",
    checklist_1="This section must explain why memory in embodied systems is a state-estimation problem, not only a long-context problem. Readers should leave knowing which facts must be grounded and refreshed from sensors.",
    checklist_2="The artifact should record remembered facts, their source, freshness, and whether they were later verified or contradicted by perception. Otherwise hallucination remains a vague label.",
    big_picture="<strong>Memory and hallucination</strong> in embodied agents is about keeping world state synchronized with words. The agent must remember object identities, task progress, and user preferences without turning stale guesses into confident plans.",
    pathway="Read from memory schema to verification: decide what the agent stores, how it stores confidence and freshness, and how new observations can revise or delete old facts.",
    develops="This section shows how LLM memory should be paired with explicit state tracking so that past context helps planning without silently overriding new sensor evidence.",
    key_question="The practical question is which memories should live as symbolic facts, which should live as scene state, and how hallucinated memories should be caught before action.",
    insight="Embodied memory is only useful if it carries provenance and freshness. A remembered object location with no timestamp is not memory; it is a latent bug.",
    theory_1="Let memory items be facts $m_i = (f_i, c_i, t_i)$ with content, confidence, and timestamp. A planner should reason over a belief state $$b_t = p(s_t \\mid o_{1:t}, a_{1:t-1}, m_{1:t}),$$ not over free-floating text summaries alone. New observations should update or erase memory items whose confidence is no longer justified.",
    theory_2="Hallucination in embodied tasks often means one of three things: inventing an object or tool, asserting a stale state as current, or carrying a wrong relational fact across scene changes. The fix is rarely 'better prompting' alone. It is usually a better contract between memory, observation, and verification.",
    mechanism="A good memory system separates semantic memory, such as user preference, from dynamic world state, such as object location. The first may persist across episodes; the second should expire quickly or be refreshed from sensors before use.",
    worked_intro="Code Fragment 1 stores two memories with different freshness and shows how the planner should gate them before use. The example demonstrates why timestamps belong in the memory schema.",
    code_1="""# Reject stale world-state memory while keeping durable preference memory.
# Embodied memory should store freshness and source, not just text.
# This keeps old observations from masquerading as current state.
memory = [
    {"fact": "user_prefers_blue_mug", "age_s": 600, "durable": True},
    {"fact": "red_mug_is_on_counter", "age_s": 45, "durable": False},
]

usable = [m["fact"] for m in memory if m["durable"] or m["age_s"] < 10]
print(usable)""",
    output_1="""['user_prefers_blue_mug']""",
    caption_1="This gating rule preserves long-lived preference memory while rejecting stale world-state memory. The key lesson is that not all remembered text should have equal planning authority once the physical scene may have changed.",
    shortcut="State stores, graph memories, and vector memories can all hold the facts, but they are only safe in robotics when coupled to freshness metadata and sensor-side verification hooks. The library can manage retrieval; it cannot decide which physical facts are still true.",
    recipe_items=[
        "Store memory items with source, timestamp, confidence, and type.",
        "Separate durable preferences from dynamic world-state facts.",
        "Refresh or invalidate dynamic facts before high-consequence actions.",
        "Never let retrieved text bypass a verifier when the action depends on current geometry.",
        "Log contradictions between memory and observation as first-class events.",
    ],
    warning="The easiest hallucination to miss is not a novel object. It is a plausible but stale memory, such as believing the mug is still on the counter after another agent already moved it.",
    practical_example="A household robot may remember that the user prefers tea in the blue mug across many days, but it should not remember that the blue mug is on the left shelf unless that fact was refreshed by recent perception. One memory is durable preference; the other is dynamic scene state.",
    fun_note="Embodied hallucination is often just nostalgia with a manipulator attached.",
    frontier="Current research explores memory graphs, learned world models, and verifier-guided long-horizon planning for embodied agents. The open challenge is keeping memories useful across long tasks without allowing stale facts to outrank fresh sensor evidence.",
    self_check="Can you list one fact in your system that should persist across sessions and one that should expire within seconds unless perception reconfirms it?",
    deep_dive_1="This section connects directly to classical filtering and SLAM. The novelty is that language memories and symbolic task facts must join the same belief-management discipline as geometric state. Otherwise the planner treats a ten-minute-old caption and a ten-millisecond-old sensor reading as equally authoritative.",
    deep_dive_2="That is also why hallucination should be decomposed. A model may hallucinate semantically, but many embodied 'hallucinations' are actually stale-state propagation errors. Better memory schemas, not bigger models, are often the right fix.",
    table_title="Tool Choices For Embodied Memory and State Tracking",
    table_rows=[
        ("LangGraph or explicit state graph", "Planner-visible memory state.", "Use it when memory items should change planner behavior in transparent ways."),
        ("Semantic map or object tracker", "Grounded dynamic world state.", "Use it when remembered object locations must be refreshed from sensors."),
        ("Vector store with metadata", "Retrieval of durable semantic context.", "Use it for user preferences or long-range task summaries, not raw geometry."),
        ("Pydantic schemas", "Typed memory records with freshness fields.", "Use them to prevent planner logic from consuming untyped memory blobs."),
        ("Verifier layer", "Checks remembered facts against observation.", "Use it whenever an action depends on the present physical world."),
    ],
    implementation_intro="Code Fragment 2 stores a memory record with provenance and freshness. This is the minimum structure needed to talk coherently about embodied hallucination instead of merely complaining that the agent 'made something up.'",
    implementation_items=[
        "Tag each memory by type: preference, world state, task progress, or explanation.",
        "Attach timestamps and evidence sources to every remembered fact.",
        "Force memory retrieval to pass through a fact-validity gate before execution.",
        "Record contradiction events when perception and memory disagree.",
        "Evaluate memory systems on tasks with delayed execution and hidden state changes.",
    ],
    code_2="""# Preserve provenance and freshness for one remembered world-state fact.
# This record makes hallucination analysis much more precise.
# The planner can inspect whether the fact is still fresh enough to trust.
memory_record = {
    "fact": "blue_mug_on_left_shelf",
    "source": "camera_frame_104",
    "age_s": 32,
    "valid_for_execution": False,
}
print(memory_record)""",
    output_2="""{'fact': 'blue_mug_on_left_shelf', 'source': 'camera_frame_104', 'age_s': 32, 'valid_for_execution': False}""",
    caption_2="This memory record is useful because it keeps provenance and freshness visible. The planner can see that the fact came from `camera_frame_104` and is too old for direct execution, which is a much sharper diagnosis than the generic label 'hallucination.'",
    teaching_move="Ask readers to retrofit timestamps into an existing memory schema. The change is small in code and large in conceptual clarity.",
    failure_analysis="When memory-rich agents fail, check whether the wrong fact was retrieved, whether the fact was stale, or whether the verifier failed to challenge it. Those paths lead to very different architectural fixes.",
    takeaway="Embodied memory is valuable only when it behaves like a state-estimation aid rather than an untyped bag of text.",
    exercise="Design a memory schema for an embodied assistant that stores both user preferences and object locations. Include the fields needed to keep one durable and the other freshness-limited.",
    bibliography_entries=[
        ("https://arxiv.org/abs/2502.09560", 'Wang et al. (2025). "EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models as Embodied Agents." arXiv.', "EmbodiedBench is useful for evaluating long-horizon embodied tasks where memory and replanning matter."),
        ("https://langchain-ai.github.io/langgraph/", "LangGraph Documentation.", "LangGraph is a practical reference for explicit stateful agent memory rather than opaque prompt concatenation."),
        ("https://gtsam.org/", "GTSAM Documentation.", "GTSAM is a classical reference for state-estimation discipline, useful here as a conceptual comparison for how embodied memory should treat uncertainty and updates."),
    ],
)


SECTIONS["part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.8.html"] = section_payload(
    sid="33.8",
    chapter_title="LLMs as Planners and Controllers",
    topic="Safe LLM-agent interfaces",
    checklist_1="This section must turn 'safety' into concrete interface rules: typed permissions, state guards, action filters, and human escalation. Readers should leave with a real control surface, not a slogan.",
    checklist_2="The artifact must log the proposed action, the active safety checks, the blocked or modified result, and the escalation path. Without those fields, safety claims are impossible to reproduce.",
    big_picture="<strong>Safe LLM-agent interfaces</strong> are not about making the model morally eloquent. They are about preventing semantically plausible but physically unsafe proposals from crossing the boundary into execution.",
    pathway="Read from permissions to shielding: define what the planner may propose, what the shield may block or rewrite, and when a human must be brought back into the loop.",
    develops="This section explains how embodied systems should interpose safety logic between LLM proposals and robot action so that language never becomes direct authority over hazardous motion.",
    key_question="The practical question is which safety properties can be checked automatically at interface time and which require escalation or hard-coded limits in the controller.",
    insight="The safest place to catch a bad plan is before it becomes an actuator command. Interface safety is cheaper than recovery.",
    theory_1="Let the LLM propose action object $u_t$, and let a safety filter $\\sigma$ map that proposal and state estimate to an allowed action: $$a_t = \\sigma(u_t, \\hat s_t), \\qquad \\sigma : \\mathcal U \\times \\mathcal S \\to \\mathcal A \\cup \\{\\text{block}, \\text{escalate}\\}.$$ The filter may pass, modify, block, or escalate the action depending on geometric, task, or policy constraints.",
    theory_2="This formulation matters because it places safety at the interface boundary, where the planner is still symbolic and the controller still has time to refuse. Once an unsafe instruction has already become continuous motion, the system has fewer and more expensive options.",
    mechanism="A practical shield checks permissions, geometry, resource bounds, and human-approval rules. The LLM proposes. The shield decides whether that proposal is admissible now, admissible only after modification, or inadmissible without escalation.",
    worked_intro="Code Fragment 1 applies a tiny safety shield to a proposed action. The important point is that the shield can return `block` or `escalate` rather than pretending every proposal must map to some executable motion.",
    code_1="""# Block high-risk actions that require human approval.
# A safety shield sits between symbolic planning and execution.
# The planner may propose; the shield may refuse.
proposal = {"action": "pick(glass)", "risk": 0.81}
approval_required = proposal["risk"] > 0.7
decision = "escalate" if approval_required else "execute"

print({"proposal": proposal["action"], "decision": decision})""",
    output_1="""{'proposal': 'pick(glass)', 'decision': 'escalate'}""",
    caption_1="This shield keeps a semantically plausible proposal from crossing directly into execution. The key fact is that the interface can return `escalate`, which means the planning stack must treat safety review as a legitimate next action rather than as an exception.",
    shortcut="Policy engines, typed tool-calling runtimes, behavior trees, and ROS 2 middleware can implement most of the blocking and escalation shell in a few lines. The shortcut handles routing, but it does not choose the safety thresholds or define the protected state variables for you.",
    recipe_items=[
        "Define a typed proposal object whose fields are visible to the safety layer.",
        "Check permissions, geometry, resource limits, and human-approval rules before execution.",
        "Allow the shield to modify, block, or escalate, not only pass or fail.",
        "Log blocked actions because they are evidence of what the planner tends to propose unsafely.",
        "Keep low-level controller safeguards active even when high-level interface shielding is strong.",
    ],
    warning="The most dangerous architecture is one where safety is written only in the prompt. Prompt text may shape planner behavior, but it is not an enforceable interface contract when hardware is involved.",
    practical_example="A domestic robot may be allowed to pick up towels autonomously but not knives, boiling containers, or medicine bottles without confirmation. The safety interface should encode those classes directly, not hope the language model remembers them every time.",
    fun_note="Prompting the model to 'be careful' is roughly as enforceable as telling gravity to please take the afternoon off.",
    frontier="Current research explores action shielding, conformal risk bounds, and richer embodied-policy evaluators, but the most reliable practice today is still layered safety: typed interfaces, hard constraints, controller-level limits, and human escalation for the remaining uncertainty.",
    self_check="If your planner proposed a forbidden action, could your system say which rule blocked it and whether the next best move should be automatic replanning or human escalation?",
    deep_dive_1="Safety interfaces are where symbolic AI and control engineering meet most directly. The LLM's proposal is high level and semantically rich; the shield translates that richness into admissibility checks over geometry, resources, and policy. This is one reason typed action objects are so valuable: they expose the fields the shield actually needs.",
    deep_dive_2="A second lesson is that safety is layered. Interface shields catch semantic and policy-level mistakes early, while low-level controllers catch timing, force, and dynamics violations later. Neither layer can safely replace the other.",
    table_title="Tool Choices For Safe Embodied Interfaces",
    table_rows=[
        ("BehaviorTree.CPP", "Explicit block, fallback, and escalation branches.", "Use it when safety review should be part of the execution graph rather than an ad hoc patch."),
        ("ROS 2 actions", "Cancelable execution and feedback hooks.", "Use actions when a proposed skill may need to be stopped after new evidence arrives."),
        ("MoveIt 2", "Collision and kinematic feasibility checks.", "Use it to reject geometrically invalid high-level proposals before motion."),
        ("Typed schemas and policy engine", "Argument-level safety checks.", "Use them to reject malformed or unauthorized action requests before middleware sees them."),
        ("Human approval interface", "Final review for high-risk classes.", "Use it when consequence exceeds what automatic shields can certify."),
    ],
    implementation_intro="Code Fragment 2 stores the blocked proposal and the rule that blocked it. This is the right artifact for improving both the shield and the planner, because it preserves what the model wanted to do and why the system refused.",
    implementation_items=[
        "Log proposed actions before the shield rewrites or blocks them.",
        "Store the specific safety rule and state evidence that fired.",
        "Differentiate automatic replanning from human escalation in the planner state.",
        "Audit blocked-action frequency by class to see where the planner needs stronger guidance.",
        "Keep the same shield active during evaluation and deployment so safety metrics remain meaningful.",
    ],
    code_2="""# Preserve the blocked action and the rule that stopped it.
# Safety improvements start from knowing what unsafe proposals recur.
# This record supports both planner tuning and shield tuning.
safety_record = {
    "proposal": "pick(glass)",
    "decision": "escalate",
    "rule": "fragile_objects_require_human_approval",
    "state": "risk_score=0.81",
}
print(safety_record)""",
    output_2="""{'proposal': 'pick(glass)', 'decision': 'escalate', 'rule': 'fragile_objects_require_human_approval', 'state': 'risk_score=0.81'}""",
    caption_2="This safety record preserves the blocked proposal, the governing rule, and the state evidence that activated it. That makes it possible to improve the planner without weakening the shield and to improve the shield without losing traceability.",
    teaching_move="Ask readers to write one safety rule that a prompt could suggest but only a typed shield could actually enforce. The contrast usually lands immediately.",
    failure_analysis="If safe interfaces fail, check whether the proposal schema hid a crucial field, whether the wrong state variable drove the shield, or whether escalation policies were too weak for the task class. Safety bugs usually live at these boundaries, not in generic model capability.",
    takeaway="Safe embodied LLM systems rely on enforceable interface contracts, not on prompt wording alone.",
    exercise="Design a safety shield for a mobile manipulator that handles fragile objects and restricted areas. Specify one automatic block rule, one rewrite rule, and one escalation rule.",
    bibliography_entries=[
        ("https://www.behaviortree.dev/docs/ros2_integration", "BehaviorTree.CPP Documentation. 'Integration with ROS2.'", "Behavior trees are a practical way to encode explicit safety, fallback, and escalation paths."),
        ("https://moveit.picknik.ai/", "MoveIt 2 Documentation.", "MoveIt provides the geometry and feasibility checks that many safe manipulation interfaces depend on."),
        ("https://docs.ros.org/en/foxy/Tutorials/Intermediate/Creating-an-Action.html", "ROS 2 Documentation. 'Creating an action.'", "ROS 2 actions are important for safe cancelation, monitoring, and interruption of risky skills."),
    ],
)


def replace_body(path: Path, new_block: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<section class="agent-checklist-synthesis".*?</section>\s*<div class="callout big-picture">.*?<nav class="chapter-nav">',
        re.DOTALL,
    )
    replacement = new_block + '\n<nav class="chapter-nav">'
    text, count = pattern.subn(lambda _m: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Could not replace section body in {path}")
    path.write_text(text, encoding="utf-8")


def update_index_31(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    roadmap = """<ul class="sections-list"><li><span class="section-num">31.1</span> <a href="section-31.1.html"><span class="section-title">Why language matters in embodied AI</span></a><span class="section-desc">Define language as a control interface for goals, constraints, and recovery signals rather than as decorative narration.</span></li><li><span class="section-num">31.2</span> <a href="section-31.2.html"><span class="section-title">Instructions, goals, constraints</span></a><span class="section-desc">Turn free-form utterances into typed task objects with hard constraints and soft preferences.</span></li><li><span class="section-num">31.3</span> <a href="section-31.3.html"><span class="section-title">Grounding language in perception; referring expressions</span></a><span class="section-desc">Resolve words into visible entities, relations, and uncertainty-aware action targets.</span></li><li><span class="section-num">31.4</span> <a href="section-31.4.html"><span class="section-title">Object- and region-centric grounding</span></a><span class="section-desc">Choose whether language should bind to object identities, masks, free-space regions, or support surfaces.</span></li><li><span class="section-num">31.5</span> <a href="section-31.5.html"><span class="section-title">Task planning from language; ambiguity and clarification</span></a><span class="section-desc">Compute when to ask before acting and how clarification changes downstream plan value.</span></li><li><span class="section-num">31.6</span> <a href="section-31.6.html"><span class="section-title">Human-agent interaction</span></a><span class="section-desc">Design mixed-initiative loops that keep correction cheap and autonomy legible.</span></li></ul>"""
    text = re.sub(r'<ul class="sections-list">.*?</ul>', roadmap, text, count=1, flags=re.DOTALL)
    text = re.sub(
        r'<section class="lab" id="lab-31">.*?</section>',
        """<section class="lab" id="lab-31">
<h2>Hands-On Lab: Build a Clarifying Language Interface</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 75 minutes</span><span class="lab-difficulty">Difficulty: Intermediate</span></div>
<div class="lab-objective"><h3>Objective</h3><p>Build a small language-guided task interface that grounds object references, separates hard constraints from soft preferences, and asks a clarification question when ambiguity would change the plan.</p></div>
<div class="lab-steps"><h3>Steps</h3><ol><li>Create a typed task schema with goal, hard constraints, and preferences.</li><li>Ground two ambiguous object references against a small scene table.</li><li>Compute a simple value-of-information score for asking before acting.</li><li>Run the same task with and without clarification and compare failure modes.</li><li>Replace your hand-built resolver with one maintained grounding library and document what complexity disappeared.</li></ol></div>
</section>""",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace(
        "This chapter uses the right-tool principle. Build the mechanism once, then reach for maintained tools such as OpenCV, PyTorch, Detectron2, Ultralytics, Segment Anything, DINOv2, SigLIP, and Gaussian Splatting tools when the task moves from learning exercise to working system.",
        "This chapter uses the right-tool principle. Build one grounding and clarification loop from scratch, then reach for maintained tools such as Grounding DINO, OWL-ViT, SAM 2, Habitat, TEACh, ROS 2 actions, and LangGraph when the task moves from pedagogy to robust execution."
    )
    text = text.replace(
        '<p>The practical thread uses OpenCV, PyTorch, Detectron2, Ultralytics, Segment Anything, DINOv2, SigLIP, and Gaussian Splatting tools where appropriate, while the theory thread keeps the mechanism visible. The reader should leave with both a mental model and a build path.</p>',
        '<p>The practical thread focuses on grounding libraries, semantic maps, dialogue-capable embodied benchmarks, and execution frameworks that keep language tied to perception and recovery. The reader should leave with both a mathematical mental model and a concrete build path for instruction following, clarification, and human correction.</p>'
    )
    path.write_text(text, encoding="utf-8")


def update_index_33(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    roadmap = """<ul class="sections-list"><li><span class="section-num">33.1</span> <a href="section-33.1.html"><span class="section-title">What LLMs can and cannot do in embodied tasks</span></a><span class="section-desc">Draw a firm boundary between semantic planning strengths and grounded-control responsibilities.</span></li><li><span class="section-num">33.2</span> <a href="section-33.2.html"><span class="section-title">SayCan: affordance-grounded planning</span></a><span class="section-desc">Combine language priors with executability estimates so plausible plans do not outrun the robot.</span></li><li><span class="section-num">33.3</span> <a href="section-33.3.html"><span class="section-title">Code as Policies: LLMs that write robot code</span></a><span class="section-desc">Use constrained program synthesis and verification rather than free-text action scripts.</span></li><li><span class="section-num">33.4</span> <a href="section-33.4.html"><span class="section-title">VoxPoser: composing 3D value maps</span></a><span class="section-desc">Translate language into planner-facing spatial objectives instead of directly into motion.</span></li><li><span class="section-num">33.5</span> <a href="section-33.5.html"><span class="section-title">ReKep: relational keypoint constraints</span></a><span class="section-desc">Express manipulation goals as compact geometric relations that optimizers can solve.</span></li><li><span class="section-num">33.6</span> <a href="section-33.6.html"><span class="section-title">Tool use, action APIs, plan verification, replanning</span></a><span class="section-desc">Design explicit loops for typed tool calls, postcondition checks, and plan revision.</span></li><li><span class="section-num">33.7</span> <a href="section-33.7.html"><span class="section-title">Memory, state tracking, and hallucination in physical tasks</span></a><span class="section-desc">Treat memory as a grounded state-estimation problem with freshness and provenance.</span></li><li><span class="section-num">33.8</span> <a href="section-33.8.html"><span class="section-title">Safe LLM-agent interfaces</span></a><span class="section-desc">Interpose shields, permissions, and escalation logic between symbolic plans and hardware.</span></li></ul>"""
    text = re.sub(r'<ul class="sections-list">.*?</ul>', roadmap, text, count=1, flags=re.DOTALL)
    text = re.sub(
        r'<section class="lab" id="lab-33">.*?</section>',
        """<section class="lab" id="lab-33">
<h2>Hands-On Lab: Build a Verified LLM Planner Loop</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 90 minutes</span><span class="lab-difficulty">Difficulty: Intermediate to Advanced</span></div>
<div class="lab-objective"><h3>Objective</h3><p>Build a small embodied planning loop where an LLM proposes typed actions, a verifier checks postconditions, and the system replans or escalates when execution evidence disagrees with the proposal.</p></div>
<div class="lab-steps"><h3>Steps</h3><ol><li>Define a minimal typed action API for a tabletop or navigation domain.</li><li>Generate candidate actions from a prompt or local mock planner.</li><li>Run a verifier after each action and store the planner trace.</li><li>Add one repair loop for failed tool calls and one safety escalation rule.</li><li>Swap your hand-built planner shell for LangGraph or a behavior tree and compare what complexity disappeared.</li></ol></div>
</section>""",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace(
        "This chapter uses the right-tool principle. Build the mechanism once, then reach for maintained tools such as OpenCV, PyTorch, Detectron2, Ultralytics, Segment Anything, DINOv2, SigLIP, and Gaussian Splatting tools when the task moves from learning exercise to working system.",
        "This chapter uses the right-tool principle. Build one verified planning loop from scratch, then reach for maintained tools such as ROS 2 actions, BehaviorTree.CPP, MoveIt 2, LangGraph, and structured tool-calling runtimes when the task moves from pedagogy to deployment."
    )
    text = text.replace(
        '<p>The practical thread uses OpenCV, PyTorch, Detectron2, Ultralytics, Segment Anything, DINOv2, SigLIP, and Gaussian Splatting tools where appropriate, while the theory thread keeps the mechanism visible. The reader should leave with both a mental model and a build path.</p>',
        '<p>The practical thread focuses on typed tool interfaces, program synthesis, spatial value maps, verifier loops, and safety shields. The reader should leave with both a mental model of why these architectures work and a concrete build path for planner traces that survive real execution.</p>'
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for rel, payload in SECTIONS.items():
        replace_body(ROOT / rel, payload)
    update_index_31(ROOT / "part-7-language-vision-and-action/module-31-language-guided-embodied-agents/index.html")
    update_index_33(ROOT / "part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/index.html")


if __name__ == "__main__":
    main()
