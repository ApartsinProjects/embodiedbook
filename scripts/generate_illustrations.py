"""
Wave 4: Generate illustrations for 56 sections missing class="illustration" figures.

Phase 1 - Generate images in parallel (6 concurrent) via Gemini API.
Phase 2 - Embed <figure class="illustration"> tags in HTML right after the epigraph.

Usage: python scripts/generate_illustrations.py [--embed-only] [--start N] [--dry-run]
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent.parent
TASKS_FILE = Path(__file__).parent / "illustration_tasks.json"
DONE_FILE = Path(__file__).parent / "illustration_done.json"
GEN_SCRIPT = "C:/Users/apart/.claude/skills/gemini-imagegen/scripts/generate_image.py"
PYTHON = "C:/Python314/python"

# Section-specific illustration prompts keyed by section number
PROMPTS = {
    # Module 01: From Static AI to Embodied AI
    "1.6": "Four distinct robots lined up side by side: a Roomba vacuuming a floor, a drone hovering outdoors, a self-driving car on a road, and a robotic arm sorting objects on a conveyor belt. Each robot is labeled with its task type. Flat isometric illustration, warm muted tones, clean educational style.",
    "1.7": "A wide-eyed robot standing at the boundary between a clean orderly simulation world and a chaotic messy real world. On the left: perfect grid, clear labels, instant rewards. On the right: fog, unpredictable physics, sparse reward stars floating far away. The robot looks overwhelmed but determined. Educational humorous style, warm tones.",
    "1.8": "A hand-drawn style road map showing twelve numbered chapters as milestones along a winding path, with small icons at each stop: a brain for foundations, gears for math, a simulator screen for tools, and a robot arm for advanced topics. The map is viewed from above like a game board. Warm flat-design colors, clean linework.",

    # Module 02: Agent-Environment Interface
    "2.6": "A robot in a dark room receiving a glowing mathematical formula from the sky: the Bellman equation written as a visual tree with arrows showing state-to-value recursion. The robot is solving it with a calculator. Split scene: left shows the MDP graph with nodes and transition arrows, right shows the Bellman backup illustrated as a chess-like lookahead tree. Educational diagram style.",
    "2.7": "A robot navigating a foggy maze, seeing only a small cone of light around itself. Above its head floats a probability cloud labeled 'belief state' showing multiple possible positions. A small thought bubble shows the true maze layout versus what the robot actually perceives. Clean flat illustration, muted blues and warm yellows, slightly whimsical.",
    "2.8": "A summary infographic showing the hierarchy of decision-making frameworks: MDP at the base, POMDP in the middle, constrained MDP at the top, connected by arrows. Each level is illustrated with a small robot icon showing increasing complexity. Clean flat design, book-summary style.",

    # Module 03: Embodied System Architectures
    "3.6": "A side-by-side comparison of three robot architecture styles: a simple reactive robot with direct sensor-to-actuator wires, a deliberative robot with a large planning computer in the middle, and a layered hybrid robot combining both. Each style shows an abstract robot shape with internal components highlighted. Educational comparison diagram style.",
    "3.7": "A timeline showing the evolution of robot architectures: 1960s block diagram, 1980s subsumption architecture with layered boxes, 2000s hybrid planning, 2020s neural end-to-end. Each era has a small robot illustration above it. Clean chronological infographic style.",
    "3.8": "A modular robot assembly diagram showing plug-and-play components: perception module, world model, planner, controller, each as a labeled gear or puzzle piece clicking together. Arrows show data flow between modules. Educational flat design, gear-and-pipeline aesthetic.",

    # Module 04: Spatial Representation
    "4.6": "A robot arm and a camera mounted in a room. Multiple overlapping coordinate frames are drawn as colorful 3D axes (RGB = XYZ) at different positions: one at the robot base, one at the gripper, one at the camera, one at the object. Arrows show the chain of transforms from world to camera to robot to gripper. Clean technical illustration with a slightly playful color scheme.",
    "4.7": "Three representations of the same 3D rotation side by side: a rotation matrix as a 3x3 grid of numbers, a quaternion as four spheres labeled w,x,y,z, and an Euler angle diagram showing a gimbal lock situation with a red X. A robot head in the center looks between all three options looking thoughtful. Educational comparison illustration.",

    # Module 05: Kinematics
    "5.6": "A 6-DOF robot arm shown in two positions: on the left the forward kinematics path (given joint angles → find end-effector position, shown as arrow flow from base to tip), on the right the inverse kinematics path (given target position → find joint angles, shown with multiple possible arm configurations). Flat technical diagram, warm and cool color split.",
    "5.7": "A robot arm performing a pick-and-place task. Overlaid on the motion are smooth curves showing joint angle trajectories over time, velocity profiles, and a trapezoidal acceleration/deceleration shape. The path through space is shown as a smooth arc with waypoints. Motion planning education diagram.",
    "5.8": "A workspace analysis diagram: a robot arm at the center surrounded by two colored regions - a large reachable workspace in light blue and a smaller dexterous workspace in warm orange. The boundary between them is labeled. Small icons show tasks possible in each region. Clean isometric style.",

    # Module 06: Dynamics and Simulation
    "6.6": "A falling robot illustrated with physics annotations: gravity arrow pointing down, mass labeled at center of mass, moment of inertia shown as a rotational arrow, and contact forces shown at the feet as upward arrows. The Euler-Lagrange equation floats above like a caption. Educational physics diagram, clean linework.",

    # Module 07: Control
    "7.6": "A control loop diagram transformed into a friendly illustration: a robot (plant) at center, a controller on the left holding a setpoint sign, an error signal shown as the gap between desired and actual, and a feedback arrow looping back. The whole thing is drawn like a circuit board with friendly robot characters at each node. Educational systems diagram.",
    "7.7": "A PID controller visualized: three tuning knobs labeled P, I, D with a robot adjusting them by hand. Below is a response curve showing underdamped (P too high), critically damped (PID tuned), and overdamped (D too high) behaviors. Warm colors for good behavior, red for bad. Practical tuning illustration.",

    # Module 08: Sensors and State Estimation
    "8.6": "A landscape of different robot sensors arranged in a museum-display style: a camera with pixel grid, a LiDAR spinning disk with point cloud, an IMU cube with accelerometer arrows, a GPS satellite overhead, and a tactile sensor glove. Each is labeled with its measurement type. Clean educational illustration, museum catalog style.",
    "8.7": "A Kalman filter visualized as a blending operation: two Gaussian bells (prior prediction in blue, sensor measurement in green) merge into a narrower combined estimate in orange. A small robot holds the merged bell triumphantly. State estimation concept illustration.",
    "8.8": "A robot navigating with multiple sensor fusion shown: camera cone, LiDAR arcs, IMU drift cloud, GPS circle all overlapping around the robot's true position. A probability distribution centered on the position tightens as more sensors combine. Educational probability visualization.",

    # Module 10: Gymnasium and PettingZoo
    "10.6": "A software package diagram showing the Gymnasium API as a clean interface between an agent and an environment. A robot agent on the left receives observation and reward packages, sends action commands. On the right the environment renders a game or simulation. The API call names (reset, step, render) float on the connecting arrows. Technical documentation illustration.",
    "10.7": "A multi-agent grid world with four differently colored robots, each with its own observation cone showing only their local view. Some robots cooperate (arrows between them), some compete (boxing gloves). The PettingZoo logo style with a playful menagerie of animal-robot characters. Educational multi-agent concept illustration.",

    # Module 11: Physics Simulators
    "11.6": "A split-screen showing three physics simulators side by side: MuJoCo with a humanoid in mid-jump, Isaac Lab with a robot hand grasping an object, Genesis with a soft body deforming. Each frame has its logo style and speedometer showing simulation speed in Hz. Simulator comparison illustration.",
    "11.7": "A GPU server rack with robot simulations running in thousands of tiny parallel windows, each showing a different robot arm trajectory. Arrows from all simulations converge to a single neural network being trained. The concept of massively parallel RL training visualized. Dark-themed with warm data-flow colors.",
    "11.8": "A sim-to-real transfer diagram: a clean virtual robot in a pristine simulation on the left, the same robot policy running in a messy real workshop on the right, connected by a bridge labeled 'domain randomization'. The real robot stumbles slightly but succeeds. The sim has random color and texture variations. Educational transfer learning illustration.",

    # Module 12: Benchmarks
    "12.6": "A leaderboard scoreboard showing different robot tasks as events in a sports competition: locomotion, manipulation, navigation, and multi-task as different athletic events with robot teams competing. Scores are shown on a board. Gold, silver, bronze medals for top methods. Playful sports-meets-robotics illustration.",

    # Module 13: Domain Randomization
    "13.6": "A robot training montage: the same robot arm practicing a grasping task across sixteen thumbnail panels, each with random variations (different object colors, sizes, lighting, table textures, physics noise). All panels feed into a single trained policy. Educational grid illustration showing diversity of training data.",

    # Module 15: Policy Gradient and PPO
    "15.6": "A gradient descent visualization for a policy: a robot standing on a bumpy loss landscape with arrows showing the gradient direction. Multiple rollout trajectories are shown as colored paths. The policy updates shown as the robot taking one small step downhill. REINFORCE/PPO concept illustration, smooth isometric style.",

    # Module 17: Massively Parallel GPU RL
    "17.6": "A massive GPU compute cluster visualization: rows of GPU chips at the bottom, thousands of parallel environment windows in the middle, gradient arrows flowing up to a central policy network at the top. A speedometer shows 1 million steps per second. Clean data-center meets robotics illustration.",

    # Module 18: Reward Design
    "18.6": "A robot in front of a reward design whiteboard. On the board: a desired behavior (stack blocks) on the left and three reward function proposals with pros and cons on the right, including one with a reward hacking robot finding a loophole (sitting on blocks to maximize height). Playful illustration of the reward specification problem.",

    # Module 22: Action Chunking and Diffusion
    "22.6": "A diffusion policy illustrated as a denoising process: on the left a cloud of random action trajectories (noise), in the middle progressively cleaner action paths emerging, on the right a single clean robot arm trajectory. A noise level gauge shows the denoising steps T, T-1, ..., 0. Clean gradient visual.",
    "22.7": "Action chunking illustrated: a robot arm shown with a timeline below. The timeline is divided into chunks of 10 timesteps, each chunk planned all-at-once as a colored block rather than one step at a time. Comparison shows single-step reactive control vs chunk-based smooth motion. Educational timing diagram.",

    # Module 23: Teleoperation
    "23.6": "A human operator wearing a VR headset and haptic gloves controlling a robot arm in a remote environment. Data streams flow: video feed from robot camera to headset, joint commands from gloves to robot. A recording icon shows demonstrations being captured. Friendly teleoperation system illustration.",

    # Module 27: Visual Perception for Action
    "27.6": "A robot visual processing pipeline: camera input on the left, convolutional feature maps in the middle shown as colored activation grids, and action outputs (gripper pose arrows) on the right. The robot is reaching for an object with confidence heatmaps overlaid on the scene. Educational deep learning pipeline illustration.",
    "27.7": "A robot grasping task showing affordance detection: the scene image on the left, affordance heatmap overlay in the middle (warm colors on graspable regions), and selected grasp pose on the right with approach and close-finger arrows. Clean perception-to-action illustration.",

    # Module 28: 3D Perception
    "28.6": "A 3D reconstruction pipeline: RGB images from multiple viewpoints on the left, a point cloud in the middle, and a clean mesh/NeRF reconstruction on the right. A robot is shown looking at the 3D reconstruction to plan manipulation. Educational 3D vision pipeline.",
    "28.7": "A NeRF scene representation: multiple camera icons arranged in a hemisphere pointing toward a center scene. Rays are shown going through the volume. The reconstructed 3D object glows in the center. A robot arm plans its reach path using the neural scene model. Educational neural radiance field concept illustration.",

    # Module 29: SLAM
    "29.6": "A SLAM cartoon: a robot holding a map and compass, simultaneously mapping a room (adding new features to the map as it discovers them) and localizing itself (checking its position against known features). The map grows as the robot moves. Clean educational illustration of simultaneous localization and mapping.",
    "29.7": "A loop closure event in SLAM: a robot has traveled a loop and returns to a previously visited place. The map shows accumulated drift as a dashed line with uncertainty ellipses, then a before/after showing the map snapping into alignment when the loop is closed. Educational SLAM concept diagram.",

    # Module 30: Navigation
    "30.6": "A top-down view of a robot navigating through an obstacle-filled room. Overlaid: a global path planner showing the planned path as a smooth blue curve, and a local planner showing a tiny adjustment window around the robot for dynamic obstacles. Two levels of planning shown simultaneously. Educational navigation architecture diagram.",

    # Module 31: Language-Guided Agents
    "31.6": "A robot receiving spoken language instructions from a human ('pick up the red cup near the window') with the instruction parsed into visual grounding steps: highlight cup, highlight window, plan trajectory. Text tokens on one side, visual scene on the other, connected by an attention mechanism shown as colored linking lines. Language-to-action grounding illustration.",

    # Module 32: Vision-Language Models
    "32.6": "A VLM (Vision-Language Model) architecture shown as a bridge: image features on the left (processed by a vision encoder showing image patches), language tokens on the right (processed by a language model), meeting in a cross-attention fusion layer in the middle. A robot uses the combined representation for task planning. Educational VLM architecture diagram.",

    # Module 33: LLMs as Planners
    "33.6": "An LLM as a robot planner: a large language model brain on the left receives a natural language task description, outputs a step-by-step plan as code/pseudocode, which a robot executive on the right executes. Feedback arrows show how execution results loop back to the LLM for replanning. Clean planning loop illustration.",
    "33.7": "A code-writing LLM generating a robot control script. On the left: the LLM receives 'make coffee' as input. On the right: it outputs executable Python code with steps like navigate_to('kitchen'), pick_up('kettle'), pour_water(). A robot arm executes each line. Code-generation for robotics concept illustration.",
    "33.8": "The chain-of-thought planning process: a robot facing a cluttered kitchen. Above it, a thought cloud shows the LLM's step-by-step reasoning: 'First I need to clear the counter. Then place the mug. Then operate the espresso machine.' Each reasoning step connects to a robot action. Educational CoT-for-robots illustration.",

    # Module 34: Vision-Language-Action Models
    "34.6": "A VLA model architecture: camera images enter from the left, language instructions enter from the top, both feed into a transformer block in the center, and robot action commands (joint angles, gripper state) exit from the right. The transformer is shown as a large attention matrix. Clean VLA architecture diagram.",
    "34.7": "A robot learning from internet data: a collage of YouTube cooking videos, text recipes, and human hand demonstrations on the left flows into a VLA model training pipeline. The trained model on the right controls a robot arm cooking in a kitchen. Scale and data diversity illustration.",
    "34.8": "RT-2 style generalization: two scenes side by side. Left: the VLA was trained on tasks with standard objects. Right: the same VLA performs a novel task described in language ('put the stone on the green star') with completely new objects. The connecting arrow is labeled 'emergent generalization'. Educational generalization concept illustration.",

    # Module 35: Robot Foundation Models
    "35.6": "A foundation model concept for robotics: a single large pre-trained model in the center depicted as a glowing sphere. From it branch multiple robot types: a drone, a wheeled robot, a humanoid, a robot arm, each receiving the same weights but adapted with thin fine-tuning arrows. Cross-embodiment learning illustration.",
    "35.7": "A cross-embodiment learning diagram: demonstrations from five different robot morphologies (arm, quadruped, drone, humanoid, gripper) all funnel into a single shared representation space shown as a colorful embedding cloud. Each robot type clusters together but overlaps with others. Transfer learning across robot bodies illustrated.",

    # Module 59: Capstone Projects
    "59.4": "A project sprint board: post-it notes arranged on a Kanban board showing stages (Research, Design, Implement, Test, Present) for a robotics capstone project. Small robot icons work on different tasks. Clean project management meets robotics illustration.",
    "59.5": "A student presenting a robot project: a screen showing robot arm demo video, a poster with architecture diagram, and the robot itself on a table. An audience of professors and peers watches. Academic presentation illustration, clean and encouraging.",
    "59.6": "A navigation capstone project: a wheeled robot in a simulated apartment floor plan with a planned path shown, obstacle avoidance maneuvers illustrated, and a success flag at the goal. Code snippets float beside the robot. Practical capstone project illustration.",
    "59.7": "A manipulation capstone: a robot arm sorting objects by color and shape on a conveyor belt. Camera feeds show real-time object detection bounding boxes. A metrics dashboard shows success rate over training episodes. Educational project showcase illustration.",
    "59.8": "A multi-robot coordination capstone: three robots working together to assemble a structure. Communication links shown as dotted lines between robots. A task allocation chart shows which robot handles which subtask. Collaborative robotics capstone illustration.",
    "59.9": "A graduation ceremony for AI robots: a class of different robot types (arm, quadruped, drone) wearing tiny graduation caps, holding diplomas. Behind them a screen shows their capstone project results. Joyful celebratory illustration marking the end of the course.",
}


def build_prompt(task):
    sec = task["sec_num"]
    if sec in PROMPTS:
        base = PROMPTS[sec]
    else:
        title = task["title"]
        base = f"Educational illustration for a robotics textbook section titled '{title}'. Shows the key concept visually with a slightly humorous and approachable angle. Warm flat-design colors, clean linework, isometric style, no text inside the image."
    return base + " Educational robotics textbook illustration. No text labels inside the image. Warm, approachable flat-design style. Clean linework."


def generate_image(task):
    img_path = ROOT / task["img_path"]
    img_path.parent.mkdir(parents=True, exist_ok=True)

    if img_path.exists():
        return {"sec": task["sec_num"], "status": "already_exists", "img_path": str(img_path)}

    prompt = build_prompt(task)
    cmd = [
        PYTHON, GEN_SCRIPT,
        "--prompt", prompt,
        "--output", str(img_path),
        "--aspect-ratio", "16:9",
        "--image-size", "1K",
        "--model", "gemini-3.1-flash-image",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode == 0 and img_path.exists():
            return {"sec": task["sec_num"], "status": "ok", "img_path": str(img_path)}
        else:
            err = (result.stderr or result.stdout)[:300]
            return {"sec": task["sec_num"], "status": "error", "error": err}
    except subprocess.TimeoutExpired:
        return {"sec": task["sec_num"], "status": "timeout"}
    except Exception as e:
        return {"sec": task["sec_num"], "status": "exception", "error": str(e)}


def embed_figure(task):
    sec = task["sec_num"]
    html_path = ROOT / task["path"]
    img_filename = task["img_filename"]

    with open(html_path, encoding="utf-8") as f:
        content = f.read()

    # Skip if illustration already present
    if 'class="illustration"' in content:
        return {"sec": sec, "status": "already_embedded"}

    img_abs = ROOT / task["img_path"]
    if not img_abs.exists():
        return {"sec": sec, "status": "image_missing"}

    # Build figure HTML
    title_text = re.sub(r"^Section \d+\.\d+:\s*", "", task["title"])
    alt_text = f"Illustration for Section {sec}: {title_text}"
    caption = f"<strong>Figure {sec}A</strong>: {title_text}"
    figure_html = (
        f'\n<figure class="illustration">\n'
        f'<img alt="{alt_text}" loading="lazy" src="images/{img_filename}"/>\n'
        f'<figcaption>{caption}</figcaption>\n'
        f'</figure>\n'
    )

    # Insert right after the epigraph </blockquote>
    epigraph_pat = re.compile(
        r'(<blockquote class="epigraph">.*?</blockquote>)',
        re.DOTALL
    )
    m = epigraph_pat.search(content)
    if m:
        insert_pos = m.end()
        new_content = content[:insert_pos] + figure_html + content[insert_pos:]
    else:
        # Fallback: after the <h1>
        h1_m = re.search(r'</h1>', content)
        if h1_m:
            insert_pos = h1_m.end()
            new_content = content[:insert_pos] + figure_html + content[insert_pos:]
        else:
            return {"sec": sec, "status": "no_insert_point"}

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return {"sec": sec, "status": "embedded"}


def main():
    embed_only = "--embed-only" in sys.argv
    dry_run = "--dry-run" in sys.argv
    start_idx = 0
    for i, arg in enumerate(sys.argv):
        if arg == "--start" and i + 1 < len(sys.argv):
            start_idx = int(sys.argv[i + 1])

    with open(TASKS_FILE, encoding="utf-8") as f:
        tasks = json.load(f)

    tasks = tasks[start_idx:]
    print(f"Processing {len(tasks)} tasks (start={start_idx})")

    if dry_run:
        for t in tasks:
            print(f"  {t['sec_num']}: {t['title'][:60]}")
            print(f"    img: {t['img_path']}")
            print(f"    prompt: {build_prompt(t)[:80]}...")
        return

    # Phase 1: Generate images
    if not embed_only:
        print("\n=== PHASE 1: Generating images ===")
        done = {}
        if DONE_FILE.exists():
            with open(DONE_FILE) as f:
                done = {d["sec"]: d for d in json.load(f)}

        to_generate = [t for t in tasks if t["sec_num"] not in done or done[t["sec_num"]]["status"] not in ("ok", "already_exists")]
        print(f"  {len(to_generate)} images to generate ({len(done)} already done)")

        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = {pool.submit(generate_image, t): t for t in to_generate}
            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                done[result["sec"]] = result
                status = result["status"]
                err = result.get("error", "")[:60] if "error" in result else ""
                print(f"  [{i}/{len(to_generate)}] {result['sec']}: {status} {err}")
                # Save progress after each image
                with open(DONE_FILE, "w") as f:
                    json.dump(list(done.values()), f, indent=2)

        ok = sum(1 for d in done.values() if d["status"] in ("ok", "already_exists"))
        errors = [d for d in done.values() if d["status"] not in ("ok", "already_exists")]
        print(f"\nGeneration complete: {ok} ok, {len(errors)} errors")
        if errors:
            for e in errors:
                print(f"  ERROR {e['sec']}: {e.get('error', e['status'])}")

    # Phase 2: Embed figures
    print("\n=== PHASE 2: Embedding figures ===")
    embed_results = []
    for t in tasks:
        r = embed_figure(t)
        embed_results.append(r)
        print(f"  {r['sec']}: {r['status']}")

    embedded = sum(1 for r in embed_results if r["status"] == "embedded")
    skipped = sum(1 for r in embed_results if r["status"] == "already_embedded")
    missing = sum(1 for r in embed_results if r["status"] == "image_missing")
    print(f"\nEmbedding complete: {embedded} embedded, {skipped} already done, {missing} image missing")


if __name__ == "__main__":
    main()
