from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REFS = {
    "module-49-multi-agent-embodied-ai": [
        ("Lowe, R. et al. Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments. NeurIPS, 2017.", "Use for centralized-training, decentralized-execution baselines and communication or coordination failure analysis."),
        ("Terry, J. K. et al. PettingZoo: Gym for Multi-Agent Reinforcement Learning. NeurIPS Datasets and Benchmarks, 2021.", "Use for maintained multi-agent environment interfaces and reproducible API-level examples."),
    ],
    "module-50-human-robot-interaction": [
        ("Goodrich, M. A. and Schultz, A. C. Human-Robot Interaction: A Survey. Foundations and Trends in Human-Computer Interaction, 2007.", "Use for HRI vocabulary, autonomy levels, and human factors framing."),
        ("Dragan, A. D., Lee, K. C. T., and Srinivasa, S. S. Legibility and Predictability of Robot Motion. HRI, 2013.", "Use for motion that communicates intent rather than merely reaching the goal."),
    ],
    "module-51-open-world-and-lifelong-embodiment": [
        ("Parisi, G. I. et al. Continual Lifelong Learning with Neural Networks: A Review. Neural Networks, 2019.", "Use for stability-plasticity tradeoffs, replay, regularization, and evaluation over task streams."),
        ("Kirkpatrick, J. et al. Overcoming catastrophic forgetting in neural networks. PNAS, 2017.", "Use for elastic weight consolidation and the limits of parameter-importance methods."),
    ],
    "module-55-deployment-architecture": [
        ("Quigley, M. et al. ROS: an open-source Robot Operating System. ICRA Workshop, 2009.", "Use for the robotics middleware lineage behind nodes, topics, services, bags, and deployment boundaries."),
        ("OpenTelemetry project documentation. https://opentelemetry.io/docs/", "Use for tracing, metrics, and logs when robot deployment evidence must connect software events to runtime behavior."),
    ],
    "module-56-embodied-agents-with-memory": [
        ("Parisotto, E. and Salakhutdinov, R. Neural Map: Structured Memory for Deep Reinforcement Learning. ICLR, 2018.", "Use for differentiable spatial memory and the distinction between stored geometry and policy state."),
        ("Chaplot, D. S. et al. Neural Topological SLAM for Visual Navigation. CVPR, 2020.", "Use for map-like memory that supports navigation decisions rather than generic retrieval."),
    ],
    "module-57-continual-and-lifelong-learning": [
        ("Kirkpatrick, J. et al. Overcoming catastrophic forgetting in neural networks. PNAS, 2017.", "Use for regularization-based retention and its assumptions."),
        ("Lopez-Paz, D. and Ranzato, M. Gradient Episodic Memory for Continual Learning. NeurIPS, 2017.", "Use for replay-constrained updates and task-stream evaluation."),
    ],
    "module-58-frontier-and-open-problems": [
        ("Open X-Embodiment Collaboration. Open X-Embodiment: Robotic Learning Datasets and RT-X Models. arXiv, 2023.", "Use for cross-embodiment data scaling, RT-X evaluation, and dataset-standardization claims."),
        ("Bardes, A. et al. Revisiting Feature Prediction for Learning Visual Representations from Video. arXiv, 2024.", "Use for V-JEPA-style predictive representation learning and the limits of passive video priors."),
    ],
    "module-59-capstone-projects": [
        ("Savva, M. et al. Habitat: A Platform for Embodied AI Research. ICCV, 2019.", "Use for simulated navigation projects, reproducible scene tasks, and embodied evaluation loops."),
        ("Cadene, R. et al. LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch. GitHub project and technical documentation, 2024.", "Use for dataset conversion, policy training, and capstone projects built around open robot-learning workflows."),
    ],
    "module-60-teaching-with-this-book": [
        ("Biggs, J. Teaching for Quality Learning at University. Open University Press, 1999.", "Use for constructive alignment between learning outcomes, activities, and assessment."),
        ("Anderson, L. W. and Krathwohl, D. R. A Taxonomy for Learning, Teaching, and Assessing. Longman, 2001.", "Use for designing assessments that move from recall to analysis, creation, and evaluation."),
    ],
}


def reference_section(cards: list[tuple[str, str]]) -> str:
    entries = []
    for ref, ann in cards:
        entries.append(
            f'<div class="bib-entry-card"><p class="bib-ref">{ref}</p>'
            f'<p class="bib-annotation">{ann}</p></div>'
        )
    return '<section class="bibliography"><h2>Section References</h2>' + "".join(entries) + "</section>"


def refs_for(path: Path) -> list[tuple[str, str]] | None:
    text = str(path)
    for key, cards in REFS.items():
        if key in text:
            return cards
    return None


def process(path: Path) -> bool:
    cards = refs_for(path)
    if not cards:
        return False
    raw = path.read_text(encoding="utf-8", errors="replace")
    if 'class="bibliography"' in raw:
        return False
    section = reference_section(cards)
    for marker in ['<div class="callout whats-next">', '<div class="whats-next">', '<nav class="chapter-nav">']:
        if marker in raw:
            updated = raw.replace(marker, section + "\n" + marker, 1)
            path.write_text(updated, encoding="utf-8")
            return True
    updated = re.sub(r"(</main>)", section + r"\n\1", raw, count=1)
    if updated != raw:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.glob("part-*/*/section-*.html")):
        if process(path):
            changed += 1
    print(f"changed_files={changed}")


if __name__ == "__main__":
    main()
