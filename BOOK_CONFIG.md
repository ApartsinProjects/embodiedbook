# Building Embodied AI Book Configuration

## Identity

Title: **Building Embodied AI**

Subtitle: **From Perception to Autonomous Action**

Series: **Hands-On AI Science**

Series position: fifth volume, following **Building Language AI**, **Building Vision AI**, **Building Temporal AI**, and **Building Scalable AI**.

Edition target: 2026 web first edition, with EPUB and KPF production after HTML source is complete.

Canonical plan: `building_embodied_ai_book_plan.md`

Archived prior plan: `archive/building_embodied_ai_book_plan_v1_ARCHIVED.md`

## Series Promise

This book belongs to **Hands-On AI Science**, the series pattern used by **Building Vision AI**. The series promise is:

1. Serious scientific depth, from first principles to the research frontier.
2. Serious building, with runnable code, labs, recipes, and production tools.
3. Self-contained teaching, suitable for advanced undergraduate study, graduate study, self-study, and focused seminars.
4. A paired teaching rhythm: from-scratch mechanism first, library shortcut second.
5. Current practice, with maintained tools, version caveats, and deprecated tools marked clearly.

## Source Of Truth For Visual Format

Match the local Vision book source exactly where possible:

Reference root: `E:\Projects\Books\VisionAI`

Copied reusable assets:

Main stylesheet: `styles/book.css`, copied from `E:\Projects\Books\VisionAI\styles\book.css`.

Syntax stylesheet: `styles/pygments.css`, copied from `E:\Projects\Books\VisionAI\styles\pygments.css`.

Callout icons: `styles/icons/`, copied from `E:\Projects\Books\VisionAI\styles\icons/`.

Runtime JS: `scripts/book.js`, copied from `E:\Projects\Books\VisionAI\scripts\book.js`.

HTML templates: `templates/`, copied from `E:\Projects\Books\VisionAI\templates/`.

KaTeX vendor assets: `vendor/katex/`, copied from `E:\Projects\Books\VisionAI\vendor\katex/`.

Prism vendor assets: `vendor/prism/`, copied from `E:\Projects\Books\VisionAI\vendor\prism/`.

Do not invent a new visual system. New HTML must reuse VisionAI page structure, classes, typography, callout types, footer pattern, navigation pattern, KaTeX setup, Prism setup, and Pagefind search hooks.

## Required Page Skeleton

Every generated page should follow the VisionAI skeleton:

1. `<!DOCTYPE html>` and `<html lang="en">`.
2. Analytics block only if the production target uses the same analytics policy.
3. Responsive viewport and page description.
4. `styles/book.css`, `styles/pygments.css` when code appears, KaTeX when math appears, Prism when code appears, `scripts/book.js`, and Pagefind hooks when search is built.
5. `<a class="skip-link" href="#main-content">Skip to main content</a>` on content pages.
6. `<header class="chapter-header">` with `.header-nav`, `.book-title-link`, `.toc-link`, `.header-search`, `.part-label`, `.chapter-label`, and `<h1>`.
7. `<main class="content" id="main-content">`.
8. Optional `<blockquote class="epigraph">` immediately after the header.
9. One opening `.callout.big-picture`.
10. Overview, prerequisites, roadmap, sections or lab as appropriate.
11. Bibliography using VisionAI card style.
12. `<nav class="chapter-nav">`.
13. `<footer>` with footer title, copyright, contents link, and last updated line.

## Callout System

Use the VisionAI callout classes and icon system from `styles/book.css`.

Core callouts:

`big-picture`: open the chapter or section with the conceptual frame.

`key-insight`: highlight a durable idea the reader should keep.

`note`: clarify detail, notation, or scope.

`warning`: mark failure modes, safety issues, or traps.

`practical-example`: show a realistic applied scenario.

`fun-note`: add light, concept-reinforcing humor.

`research-frontier`: mark current research and open problems.

`algorithm`: explain an algorithm or procedure.

`tip`: give practical advice.

`exercise`: provide conceptual or coding work.

`key-takeaway`: summarize a section.

`library-shortcut`: show the maintained tool that replaces hand code.

`pathway`: give reading or implementation route guidance.

`self-check`: prompt quick reader verification.

`lab`: frame hands-on work.

`looking-back`: connect to prior chapters.

`whats-next`: point to the next chapter or section.

`cross-ref`: link related material.

`postmortem`: analyze production failures.

`production-pattern`: capture a deployable engineering pattern.

`under-the-hood`: explain internals beneath an API.

Every callout needs a `.callout-title` unless the VisionAI pattern for that class explicitly omits it.

## Required Teaching Pattern

Every chapter follows:

1. Motivation anchored in a real embodied system.
2. Concept map on the perception-action loop.
3. Theory and formalism.
4. Worked miniature example.
5. From-scratch implementation.
6. Library shortcut using a maintained tool.
7. Practical recipe and default settings.
8. Failure modes and debugging.
9. Hands-on lab.
10. Conceptual exercises, derivation exercises, coding exercises, and project extension.
11. Bibliography and further reading.
12. What is next.

## Right Tool Principle

Every substantial from-scratch implementation must be followed by a `library-shortcut` callout that states:

1. The hand-built line count or complexity.
2. The library call that replaces it.
3. What the library handles internally.
4. When the hand-built version is still useful for learning or debugging.

## Chapter Map

### Front Matter

F1. Foreword
F2. About the Authors
F3. About the Hands-On AI Science Series
F4. Who Should Read This Book
F5. How to Use This Book
F6. What This Book Covers
F7. Look Inside Preview
F8. Copyright and Legal

### Part I, Foundations of Embodied AI

1. From Static AI to Embodied AI
2. The Agent-Environment Interface
3. Embodied System Architectures

### Part II, Mathematical, Robotics, and Control Foundations

4. Spatial Representation and Coordinate Frames
5. Kinematics and Robot Motion
6. Dynamics and Simulation Math
7. Control for AI Practitioners
8. Sensors, Perception Hardware, and State Estimation

### Part III, Simulation, Tooling, and the Modern Stack

9. Why Simulation Is Central
10. Environments with Gymnasium and PettingZoo
11. Physics Simulators: MuJoCo, MJX, Isaac Lab, Genesis
12. Benchmarks and Task Suites
13. Domain Randomization and Synthetic Data

### Part IV, Reinforcement Learning for Embodied Agents

14. Reinforcement Learning Refresher
15. Policy Gradient Methods and PPO
16. Value-Based and Off-Policy Methods
17. Massively Parallel and GPU RL
18. Reward Design and Goal Specification
19. Exploration in Embodied Worlds
20. Sim-to-Real Transfer

### Part V, Imitation Learning, Demonstrations, and Robot Data

21. Imitation Learning Foundations
22. Action Chunking, Diffusion Policy, and Flow Matching
23. Teleoperation and Data Collection
24. Robot Datasets and Data Scaling Laws
25. Offline RL and Dataset-Based Robot Learning
26. Skills, Hierarchy, and Task Decomposition

### Part VI, Embodied Perception

27. Visual Perception for Action
28. 3D Perception and Neural Scene Representations
29. Localization and Mapping
30. Navigation and Path Planning

### Part VII, Language, Vision, and Action

31. Language-Guided Embodied Agents
32. Vision-Language Models for Embodiment
33. LLMs as Planners and Controllers
34. Vision-Language-Action Models
35. Robot Foundation Models and Cross-Embodiment Learning

### Part VIII, World Models and Model-Based Embodied AI

36. Predicting the Future
37. Model-Based RL and MPC
38. Latent World Models
39. Generative and Video World Models
40. Predictive Representations and Self-Supervised World Models
41. Diffusion and Generative Planning

### Part IX, Manipulation, Locomotion, and Embodied Skills

42. Robotic Manipulation
43. Grasping and Dexterous Manipulation
44. Tactile and Visuo-Tactile Learning
45. Locomotion and Mobility
46. Humanoid Robots and Whole-Body Control
47. Drones and Aerial Embodied AI
48. Autonomous Driving as Embodied AI

### Part X, Multi-Agent and Human-Centered Embodiment

49. Multi-Agent Embodied AI
50. Human-Robot Interaction
51. Open-World and Lifelong Embodiment

### Part XI, Evaluation, Safety, Robustness, and Deployment

52. Evaluating Embodied Systems
53. Robustness and Uncertainty
54. Safety in Embodied AI
55. Deployment Architecture

### Part XII, Frontiers, Capstones, and Course Design

56. Embodied Agents with Memory
57. Continual and Lifelong Learning
58. Frontier and Open Problems
59. Capstone Projects
60. Teaching with This Book

### Appendices

A. Linear Algebra and 3D Geometry Refresher
B. Probability, Estimation, and Optimization Refresher
C. The Embodied AI Toolbox
D. PyTorch and JAX for Embodied AI
E. Compute Recipes
F. Datasets and Benchmarks Catalog
G. Reproducibility and Experiment Hygiene
H. Notation and Glossary
I. Citing the Frontier

## Directory Naming Plan

Use VisionAI-style directories:

`part-N-slug/module-XX-slug/index.html`

Individual chapter sections use:

`part-N-slug/module-XX-slug/section-XX.Y.html`

Front matter uses:

`front-matter/<name>.html`

Appendices use:

`appendices/appendix-a-slug/index.html`

## Production Status

Current state: planning and preparation only.

Do not generate the HTML book until explicitly requested.
