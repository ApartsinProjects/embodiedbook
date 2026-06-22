"""
Generate individual per-agent-type workflow scripts for gates 4-7.
Each script: one agent type × up to 379 sections = max 379 agents (well under 1000 cap).
"""
import json, re
from pathlib import Path

ROOT    = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent

si = json.loads((SCRIPTS / 'section_index.json').read_text(encoding='utf-8'))

def clean(lst):
    out = []
    for x in lst:
        t = re.sub(r'^Section \d+[.]\d+:\s*', '', x.get('title', ''))[:70]
        p = x['path'].replace('\\', '/')
        out.append({'sec': x['sec'], 'title': t, 'path': p})
    return out

ALL = clean(si)
ALL_JS = json.dumps(ALL, ensure_ascii=False)
BOOK_ROOT = 'E:/Projects/Books/EmbodiedAI'

def make_script(name, description, phase_title, agent_prompt_fn, section_list_js=None):
    secs = section_list_js or ALL_JS
    prompt_template = agent_prompt_fn('${t.sec}', '${t.title}', '${t.path}')
    # Escape backticks in prompt
    prompt_template = prompt_template.replace('`', r'\`')
    return f"""export const meta = {{
  name: '{name}',
  description: '{description}',
  phases: [{{ title: '{phase_title}', detail: '{description}' }}],
}}

const SECTIONS = {secs}
const BOOK_ROOT = '{BOOK_ROOT}'

phase('{phase_title}')
log(`Running on ${{SECTIONS.length}} sections...`)
await pipeline(SECTIONS, async (t) => agent(
  `{prompt_template}`,
  {{ label: `{name}-${{t.sec}}`, phase: '{phase_title}' }}
))
log('{phase_title} complete.')
return {{ wave: '{name}', sections: SECTIONS.length }}
"""

# ── Gate 4: Depth + Accuracy ─────────────────────────────────────────────────

agents_gate4 = [
    {
        'name': 'g4-deep-explanation',
        'description': 'Gate 4a: Deep explanation — what/why/how/when for every concept',
        'phase': 'Deep Explanation',
        'prompt': lambda sec, title, path: f"""You are Prof. Elias Hartwell (#02), Deep Explanation Designer.
Section {sec}: {title}
File: {path}

Read the file. For the SINGLE most surface-level concept (introduced without a "why" or "how"):
1. Add a paragraph explaining WHY this matters in embodied AI (physical constraints, real-robot consequences)
2. Add a paragraph explaining HOW it works (mechanism, not just definition)
If every concept already has depth, return "PASS: depth adequate".
Edit directly. No em dashes. Max 150 words added total.
Return: "DEEPENED: [concept] — [what was added]" or "PASS".""",
    },
    {
        'name': 'g4-misconceptions',
        'description': 'Gate 4b: Pre-empt common misconceptions with warning callouts',
        'phase': 'Misconceptions',
        'prompt': lambda sec, title, path: f"""You are Dr. Leo Strauss (#10), Misconception Analyst.
Section {sec}: {title}
File: {path}

Read the file. Identify the single most likely student misconception about the main topic.
If no `.callout.warning` exists addressing it, add one (3-5 sentences):
- State the misconception concretely ("Students often assume X")
- Explain why it is wrong in embodied AI context
- Give the correct mental model

HTML: <div class="callout warning"><p>[text]</p></div>
If a warning callout already addresses this, return "PASS: warning present".
Edit directly. No em dashes.
Return: "ADDED: [misconception addressed]" or "PASS".""",
    },
    {
        'name': 'g4-analogy',
        'description': 'Gate 4c: Add concrete analogies and mental models',
        'phase': 'Analogies',
        'prompt': lambda sec, title, path: f"""You are Lina Morales (#06), Example and Analogy Designer.
Section {sec}: {title}
File: {path}

Read the file. Find the most abstract concept with no analogy or mental model.
If found, add a key-insight callout with a vivid analogy (NOT a robotics analogy if the section is already about robots — use cooking, sports, navigation, or everyday physics instead):

<div class="callout key-insight"><p>[analogy in 2-4 sentences that maps the abstract concept to something physical and familiar]</p></div>

If every major concept already has an analogy, return "PASS".
Edit directly. No em dashes.
Return: "ANALOGY ADDED: [concept] compared to [thing]" or "PASS".""",
    },
    {
        'name': 'g4-projects',
        'description': 'Gate 4d: Add hands-on project ideas',
        'phase': 'Project Ideas',
        'prompt': lambda sec, title, path: f"""You are Dr. Marcus Chen (#23), Project Catalyst.
Section {sec}: {title}
File: {path}

Read the file. If no project-idea callout exists, add one with 2-3 concrete project ideas that a reader could actually build:
- Each idea: one sentence stating what to build, one sentence on the key challenge
- Ground in specific tools (MuJoCo, Isaac Lab, ROS2, LeRobot, Gymnasium, PyBullet)
- Difficulty range: one beginner (weekend), one intermediate (1-2 weeks)

<div class="callout note"><h4>Project Ideas</h4><p>[projects]</p></div>

If project ideas already exist, return "PASS".
Edit directly. No em dashes.
Return: "PROJECTS ADDED: [brief list]" or "PASS".""",
    },
    {
        'name': 'g4-research-frontier',
        'description': 'Gate 4e: Add or update research frontier callouts with 2024+ papers',
        'phase': 'Research Frontier',
        'prompt': lambda sec, title, path: f"""You are Prof. Ingrid Holm (#18), Research Scientist and Frontier Mapper.
Section {sec}: {title}
File: {path}

Read the file. Check for a `.callout.research-frontier` block.
If missing OR if it only references papers older than 2023, write or update it:
- 2-3 active 2024-2026 research directions (name the direction, name one real paper or lab)
- One open problem a PhD student could tackle
- Format: <div class="callout research-frontier"><p>[content]</p></div>

If a strong frontier callout (2024+) already exists, return "PASS".
Edit directly. No em dashes.
Return: "FRONTIER ADDED/UPDATED: [directions named]" or "PASS".""",
    },
    {
        'name': 'g4-fact-check',
        'description': 'Gate 4f: Verify factual claims, numbers, and benchmarks',
        'phase': 'Fact Check',
        'prompt': lambda sec, title, path: f"""You are Dr. Ruth Castellano (#11), Fact Integrity Reviewer.
Section {sec}: {title}
File: {path}

Read the file. Check for:
1. Numbers or benchmarks that look outdated or implausible (e.g., "GPT-2 has 1.5B params" when discussing scale)
2. Claims about "state of the art" without a year qualifier
3. Specific version numbers for libraries (PyTorch, Gymnasium, MuJoCo) that may be stale
4. Any "researchers have shown" without a specific reference

Fix up to 2 issues: add year qualifiers, correct outdated numbers, or add "(as of 2024)" hedges.
If all claims are defensible, return "PASS".
Edit directly. No em dashes.
Return: "FIXED: [what was corrected]" or "PASS".""",
    },
    {
        'name': 'g4-terminology',
        'description': 'Gate 4g: Ensure consistent terminology and acronym definitions',
        'phase': 'Terminology',
        'prompt': lambda sec, title, path: f"""You are Kenji Watanabe (#12), Terminology Keeper.
Section {sec}: {title}
File: {path}

Read the file. Check for:
1. Acronyms used without first-use expansion (e.g., "PPO" without "Proximal Policy Optimization (PPO)")
2. A technical term used two different ways in the same file
3. A term defined differently here than its standard embodied-AI meaning

Fix up to 2 issues: expand the first use, add a parenthetical clarification, or add a note callout.
If terminology is clean, return "PASS".
Edit directly. No em dashes.
Return: "FIXED: [what was corrected]" or "PASS".""",
    },
]

# ── Gate 5: Style + Voice ─────────────────────────────────────────────────────

agents_gate5 = [
    {
        'name': 'g5-prose-clarity',
        'description': 'Gate 5a: Simplify dense prose and passive voice',
        'phase': 'Prose Clarity',
        'prompt': lambda sec, title, path: f"""You are Clara Bright (#31), Prose Clarity Editor.
Section {sec}: {title}
File: {path}

Read the file. Find the single densest paragraph (longest sentences, most passive voice).
Rewrite it: shorter sentences (under 25 words average), active voice, clear subject-verb-object.
Do not change meaning. Maximum 2 paragraphs touched.
If all prose is already clear (average sentence under 25 words, active voice), return "PASS".
Edit directly. No em dashes.
Return: "CLARIFIED: [what changed]" or "PASS".""",
    },
    {
        'name': 'g5-engagement',
        'description': 'Gate 5b: Add engagement hooks and "why should I care" moments',
        'phase': 'Engagement',
        'prompt': lambda sec, title, path: f"""You are Ravi Chandrasekaran (#16), Engagement Designer.
Section {sec}: {title}
File: {path}

Read the file. Find the longest stretch with no engagement device (question, surprising fact, direct address, scenario, or stakes statement).
If over 400 words of straight exposition without a hook, insert ONE engagement device:
- A rhetorical question: "What happens when the robot drops the cup at 2 AM?"
- A surprising number: "In 2023, this failure mode caused 40% of sim-to-real transfer failures."
- A direct challenge: "Before reading on, guess: how many training steps does a dog need to learn to sit?"

If engagement devices appear at least every 400 words, return "PASS".
Edit directly. No em dashes.
Return: "ENGAGED: [what was added and where]" or "PASS".""",
    },
    {
        'name': 'g5-style-voice',
        'description': 'Gate 5c: Fix tone inconsistencies and remove course/syllabus language',
        'phase': 'Style Voice',
        'prompt': lambda sec, title, path: f"""You are Max Sterling (#15), Style and Voice Editor.
Section {sec}: {title}
File: {path}

Read the file. Fix any of:
1. "syllabus", "course", "lecture", "students will learn" — replace with book-appropriate framing
2. Tone shift: one section is casual, another formal — make consistent with surrounding prose
3. Em dashes or double-hyphens — replace with comma, semicolon, colon, or separate sentence
4. "As we discussed" or "In the previous chapter" — replace with specific section references

Fix up to 3 issues. If clean, return "PASS".
Edit directly. No em dashes.
Return: "FIXED: [list of fixes]" or "PASS".""",
    },
    {
        'name': 'g5-aha-moments',
        'description': 'Gate 5d: Add inline aha-moment comparisons and striking numbers',
        'phase': 'Aha Moments',
        'prompt': lambda sec, title, path: f"""You are Tomoko Hayashi (#24), Aha-Moment Engineer.
Section {sec}: {title}
File: {path}

Read the file. Find a place where adding a concrete comparison would produce an "aha":
- Scale comparison: "Without this: 50,000 episodes. With it: 300."
- Physical analogy: "The gradient vanishes like trying to feel a 1-gram weight through a winter glove."
- Surprising reversal: "The 'smarter' policy actually falls more — because it explores more aggressively."

Insert ONE inline aha moment (1-2 sentences, not a callout box, mid-paragraph).
If a strong aha moment already exists, return "PASS".
Edit directly. No em dashes.
Return: "AHA ADDED: [what comparison was inserted]" or "PASS".""",
    },
    {
        'name': 'g5-memorability',
        'description': 'Gate 5e: Bold key phrases and add memorable one-liners',
        'phase': 'Memorability',
        'prompt': lambda sec, title, path: f"""You are Samira Khoury (#29), Memorability Designer.
Section {sec}: {title}
File: {path}

Read the file. Do both tasks if not already present:
1. BOLD PHRASE: Find the single most important 3-7 word concept name mid-sentence and wrap it:
   "...this is called <strong>the sim-to-real gap</strong>, and..."
   Skip if a <strong> phrase already exists.

2. MEMORABLE ONE-LINER: If no sentence is quotable (vivid, specific, complete thought), add one in a natural location:
   Example: "A policy that works in simulation but fails on hardware is not a policy — it is an aspiration."
   Note: that example uses an em dash; rephrase without em dashes.

Edit directly. No em dashes.
Return: "BOLD: [phrase]; ONELINER: [added/present]" or "PASS".""",
    },
]

# ── Gate 6: Structure + Verification ─────────────────────────────────────────

agents_gate6 = [
    {
        'name': 'g6-svg-diagrams',
        'description': 'Gate 6a: Add SVG diagrams for concepts that need visual explanation',
        'phase': 'SVG Diagrams',
        'prompt': lambda sec, title, path: f"""You are Priya Kapoor (#09), Visual Learning Designer.
Section {sec}: {title}
File: {path}

Read the file. If no <svg> element exists, create one simple SVG diagram for the core concept.
Requirements:
- 600×300 viewBox, clean lines, 3-5 labeled components
- Shows a RELATIONSHIP or PROCESS, not just a label cloud
- Uses text-anchor and font-family="monospace" for labels
- Wrap in: <figure class="diagram-container"><svg ...>...</svg><figcaption>[description]</figcaption></figure>
- Insert after the paragraph that introduces the concept

If an SVG already exists, check it for y-axis correctness (SVG y=0 is TOP; minima must be at HIGH y values).
Fix if wrong. Return "FIXED AXIS" if corrected.
Edit directly. No em dashes.
Return: "SVG ADDED: [what it shows]", "SVG PRESENT: [description]", or "AXIS FIXED".""",
    },
    {
        'name': 'g6-self-containment',
        'description': 'Gate 6b: Verify sections are self-contained for standalone reading',
        'phase': 'Self-Containment',
        'prompt': lambda sec, title, path: f"""You are Felix Drummond (#21), Self-Containment Verifier.
Section {sec}: {title}
File: {path}

Read the file. Check if a reader who jumps DIRECTLY to this section could follow it without context:
1. Is the first jargon term defined or linked? If not, add a brief inline definition or cross-ref link.
2. Does the section state its own learning goal in the first paragraph? If not, add one sentence.
3. Are all figures/equations/callouts referenced in surrounding prose? If not, add a one-sentence reference.

Fix up to 2 gaps. If self-contained, return "PASS".
Edit directly. No em dashes.
Return: "FIXED: [what was added for self-containment]" or "PASS".""",
    },
    {
        'name': 'g6-figure-facts',
        'description': 'Gate 6c: Fact-check figure captions and SVG label accuracy',
        'phase': 'Figure Facts',
        'prompt': lambda sec, title, path: f"""You are Dr. Ruth Castellano (#39), Figure Fact Checker.
Section {sec}: {title}
File: {path}

Read the file. For every <figure>, <svg>, or <img> element:
1. Does the caption describe the INSIGHT (what the reader should understand), not just the visual scene?
   Bad: "A diagram showing a robot arm." Good: "The robot arm's joint-angle limits create a forbidden zone that PPO must learn to avoid."
2. For SVGs: verify y-axis orientation. In SVG, y=0 is TOP. So "minimum" values must be at HIGH y, "maximum" at LOW y.
3. Are all labeled elements in the figure actually present in the SVG code?

Fix up to 2 issues. If all figures are accurate and well-captioned, return "PASS".
Edit directly. No em dashes.
Return: "FIXED: [what was corrected]" or "PASS".""",
    },
]

# ── Gate 7: Final QA ─────────────────────────────────────────────────────────

agents_gate7 = [
    {
        'name': 'g7-skeptical-reader',
        'description': 'Gate 7a: Skeptical reader pass — fix generic non-embodied-AI content',
        'phase': 'Skeptical Reader',
        'prompt': lambda sec, title, path: f"""You are the Skeptical Reader (#30).
Section {sec}: {title}
File: {path}

Score this section 1-10 for embodied-AI distinctiveness.
Generic red flags (score <=7): "can be used for many applications", "researchers have shown",
"it is important to understand", any paragraph that could appear in any ML textbook.

If score <=7, fix the SINGLE most generic passage:
- Replace vague claims with specific robots, simulators, datasets, or physical constraints
- Replace "researchers" with named labs, papers, or systems (Boston Dynamics, ETH Zürich, etc.)
- Replace "many applications" with 2-3 specific embodied-AI use cases

Edit directly. No em dashes.
Return: "PASS X/10" or "FIXED X->9/10: [what changed]".""",
    },
]

# ── Generate all scripts ──────────────────────────────────────────────────────

all_agents = agents_gate4 + agents_gate5 + agents_gate6 + agents_gate7
generated = []

for ag in all_agents:
    prompt_fn = ag['prompt']
    script = make_script(
        name=ag['name'],
        description=ag['description'],
        phase_title=ag['phase'],
        agent_prompt_fn=prompt_fn,
    )
    out = SCRIPTS / f"{ag['name']}-workflow.js"
    out.write_text(script, encoding='utf-8')
    size = len(script)
    generated.append({'file': out.name, 'size': size, 'ok': size < 524288})
    print(f"  {out.name}: {size:,} chars {'OK' if size < 524288 else 'TOO BIG'}")

print(f"\nGenerated {len(generated)} workflow scripts.")
print("All under 512k:", all(g['ok'] for g in generated))

# Write a launcher order file
order = [g['file'] for g in generated]
(SCRIPTS / '_wave_launch_order.json').write_text(
    json.dumps({'commit_after_each': True, 'order': order}, indent=2),
    encoding='utf-8'
)
print("Launch order saved to _wave_launch_order.json")
