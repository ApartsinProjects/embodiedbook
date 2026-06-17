from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CH11 = ROOT / "part-3-simulation-tooling-and-the-modern-stack" / "module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis"
CH34 = ROOT / "part-7-language-vision-and-action" / "module-34-vision-language-action-models"


LINK_REPLACEMENTS = {
    "../../part-1-foundations-of-embodied-ai/module-2-the-agent-environment-interface/index.html":
        "../../part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/index.html",
    "../../part-1-foundations-of-embodied-ai/module-2-agent-environment-interface/index.html":
        "../../part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/index.html",
    "../../part-2-mathematical-robotics-and-control-foundations/module-4-spatial-representation-and-coordinate-frames/index.html":
        "../../part-2-mathematical-robotics-and-control-foundations/module-04-spatial-representation-and-coordinate-frames/index.html",
    "../../part-2-mathematical-robotics-and-control-foundations/module-6-dynamics-and-simulation-math/index.html":
        "../../part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/index.html",
    "../../part-2-mathematical-robotics-and-control-foundations/module-7-control-for-ai-practitioners/index.html":
        "../../part-2-mathematical-robotics-and-control-foundations/module-07-control-for-ai-practitioners/index.html",
    "../module-9-why-simulation-is-central/index.html":
        "../module-09-why-simulation-is-central/index.html",
}


REQUIRED_SNIPPETS = {
    CH11 / "section-11.2.html": [
        ("callout key-insight", '<div class="callout key-insight"><div class="callout-title">State Is The Interface</div><p>The simulator state is not just an implementation detail. It is the contract that links dynamics, observations, logging, replay, and controller debugging.</p></div>\n'),
    ],
    CH11 / "section-11.4.html": [
        ("callout key-insight", '<div class="callout key-insight"><div class="callout-title">Throughput Changes The Experiment</div><p>Parallel simulation is not only faster. It changes which research questions become practical by making sweeps, ablations, and failure replay cheap enough to run routinely.</p></div>\n'),
    ],
    CH11 / "section-11.5.html": [
        ("callout key-insight", '<div class="callout key-insight"><div class="callout-title">Rendering Is Part Of The Policy</div><p>When observations are images, the renderer becomes part of the learning system. Lighting, camera placement, textures, and sensor noise all shape what the policy learns to trust.</p></div>\n'),
    ],
    CH11 / "section-11.7.html": [
        ("callout key-insight", '<div class="callout key-insight"><div class="callout-title">Integration Decides Reality</div><p>A simulator that cannot connect to the robot stack is a sandbox, not a deployment rehearsal. Middleware, clocks, transforms, and logs decide whether simulated success survives contact with hardware.</p></div>\n'),
    ],
    CH11 / "section-11.8.html": [
        ("callout warning", '<div class="callout warning"><div class="callout-title">Do Not Rank Tools From Marketing Claims</div><p>Simulator claims are only meaningful when measured on your robot, your task, your controller frequency, and your observation pipeline. Treat unmatched benchmark numbers as hints, not evidence.</p></div>\n'),
    ],
    CH34 / "section-34.1.html": [
        ("callout warning", '<div class="callout warning"><div class="callout-title">Do Not Confuse Semantics With Control</div><p>A VLA can name an object and still fail the motion. Always evaluate grounding, action accuracy, latency, and recovery as separate properties.</p></div>\n'),
    ],
    CH34 / "section-34.2.html": [
        ("callout library-shortcut", '<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>Use LeRobot or an OpenVLA-style repository before writing a custom robot dataset loader. The maintained stack handles episode schemas, image loading, action normalization, and train-eval splits that otherwise take hundreds of lines to rebuild.</p></div>\n'),
        ("code-caption", '<pre><code class="language-python"># Inspect the fields expected by a VLA dataset before training.\nrequired_fields = ["observation.image", "observation.state", "action", "language_instruction"]\nprint("VLA dataset contract:", ", ".join(required_fields))</code></pre>\n<div class="code-caption"><strong>Code Fragment 34.2.1:</strong> This small contract check names the minimum fields a practical VLA data pipeline must expose before fine-tuning.</div>\n'),
    ],
    CH34 / "section-34.3.html": [
        ("callout warning", '<div class="callout warning"><div class="callout-title">Action Tokens Hide Units</div><p>Discretized action tokens are convenient for transformer training, but the robot still executes metric motion, gripper commands, and timing. Always preserve the conversion back to physical units in the evaluation artifact.</p></div>\n'),
    ],
    CH34 / "section-34.4.html": [
        ("callout library-shortcut", '<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>Use robomimic, Diffusion Policy, or LeRobot policy implementations to prototype action chunking before designing a new architecture. These libraries already manage temporal windows, normalization, batching, and rollout evaluation.</p></div>\n'),
        ("code-caption", '<pre><code class="language-python"># Represent a short action chunk as a batch-ready tensor shape.\nbatch_size, horizon, action_dim = 32, 16, 7\nprint({"batch": batch_size, "horizon": horizon, "action_dim": action_dim})</code></pre>\n<div class="code-caption"><strong>Code Fragment 34.4.1:</strong> The shape summary makes action chunking explicit: a policy predicts several future low-level actions at once.</div>\n'),
    ],
    CH34 / "section-34.5.html": [
        ("callout key-insight", '<div class="callout key-insight"><div class="callout-title">Generalization Needs Metadata</div><p>Cross-embodiment learning works only when the dataset records what changed: robot body, camera view, action convention, control rate, task language, and success definition.</p></div>\n'),
        ("callout warning", '<div class="callout warning"><div class="callout-title">Mixtures Can Hide Failure</div><p>A large robot-data mixture can improve average performance while weakening a specific robot or task family. Report per-embodiment and per-task slices, not only aggregate success.</p></div>\n'),
    ],
    CH34 / "section-34.6.html": [
        ("callout library-shortcut", '<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>Start adaptation from an open checkpoint and its official preprocessing code when available. The shortcut avoids mismatched image normalization, tokenizer settings, action scaling, and camera ordering.</p></div>\n'),
        ("code-caption", '<pre><code class="language-python"># Keep adaptation metadata beside the checkpoint.\nadaptation_card = {\n    "base_model": "reader fill in",\n    "robot": "reader fill in",\n    "control_hz": 10,\n    "action_normalization": "dataset statistics",\n}\nprint(adaptation_card)</code></pre>\n<div class="code-caption"><strong>Code Fragment 34.6.1:</strong> The adaptation card records the details that make a VLA fine-tune reproducible instead of merely runnable.</div>\n'),
    ],
    CH34 / "section-34.7.html": [
        ("callout library-shortcut", '<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>Use prompt suites as data files, not prose buried in notebooks. A simple CSV or JSON prompt panel lets every model variant run on the same goal, object, constraint, and stop-condition cases.</p></div>\n'),
    ],
    CH34 / "section-34.8.html": [
        ("callout library-shortcut", '<div class="callout library-shortcut"><div class="callout-title">Library Shortcut</div><p>Use a shared evaluation harness such as LeRobot evaluation scripts or a Gymnasium-style wrapper around the robot task. Shared wrappers keep prompt, observation, action, video, and success metrics synchronized.</p></div>\n'),
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def insert_after_opening_callout(text: str, html: str) -> str:
    marker = "</div>\n\n<h2"
    index = text.find(marker)
    if index != -1:
        return text[: index + len("</div>\n")] + html + text[index + len("</div>\n") :]
    marker = "</blockquote>"
    index = text.find(marker)
    if index != -1:
        return text[: index + len(marker)] + "\n" + html + text[index + len(marker) :]
    main = '<main class="content" id="main-content">'
    index = text.find(main)
    if index != -1:
        return text[: index + len(main)] + "\n" + html + text[index + len(main) :]
    return text + "\n" + html


def fix_links_and_bibliography(path: Path) -> None:
    text = read(path)
    original = text
    for old, new in LINK_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.replace("References &amp; Further Reading", "Bibliography and Further Reading")
    text = text.replace("📄 Paper", "Paper")
    text = text.replace("🔧 Tool", "Tool")
    if text != original:
        write(path, text)


def add_required_blocks() -> None:
    for path, snippets in REQUIRED_SNIPPETS.items():
        text = read(path)
        original = text
        for snippet, html in snippets:
            if snippet not in text:
                text = insert_after_opening_callout(text, html)
        if text != original:
            write(path, text)


def main() -> None:
    for chapter in (CH11, CH34):
        for path in chapter.glob("*.html"):
            fix_links_and_bibliography(path)
    add_required_blocks()


if __name__ == "__main__":
    main()
