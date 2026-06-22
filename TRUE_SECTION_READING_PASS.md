# True Section Reading Pass

This file records the manual section-by-section reading pass requested by the user. The helper script only strips HTML for readability; entries here are based on direct reading of the section text.

## Batch 001, Sections 1.1-1.4

Status: read and edited.

- `section-1.1.html`, Static prediction vs. embodied interaction
  - Read: core explanation, formal distinction, worked example, callouts, builder deep dive, implementation recipe, lab, bibliography.
  - Weakness found: generic production-depth layer repeated a schema example instead of teaching closed-loop consequences.
  - Change made: replaced it with an embodied error ledger, practical tool guidance, a concrete compounding-error diagnostic, and a sharper failure-analysis pattern.

- `section-1.2.html`, Why intelligence needs a world; the perception-action loop
  - Read: loop theory, belief update, worked loop skeleton, callouts, builder deep dive, implementation recipe, bibliography.
  - Weakness found: title-pasted prose and generic evidence-record material; expected-output sentence did not describe the actual loop code.
  - Change made: replaced the depth layer with timing-budget analysis, ROS 2 and behavior-tree tool advice, stale-edge diagnostic code, and corrected the reader pathway and expected-output prose.

- `section-1.3.html`, Agents, environments, observations, actions, rewards, constraints
  - Read: constrained POMDP framing, split-view worked example, tool shortcut, callouts, builder deep dive, implementation recipe, bibliography.
  - Weakness found: grammatical epigraph, missing "and" in the core term list, generic tool table, and a generic exercise.
  - Change made: rewrote the epigraph, tightened the term list, replaced generic tool advice with Gymnasium spaces, PettingZoo, and Safety Gymnasium, added a privileged-state leak test, and made the exercise concrete.

- `section-1.4.html`, Physical vs. simulated embodiment
  - Read: sim-real theory, matched sim and hardware example, callouts, builder deep dive, implementation recipe, bibliography.
  - Weakness found: generic epigraph, generic tool table, schema-only code, and a generic exercise.
  - Change made: rewrote the epigraph, replaced tool advice with MuJoCo, Isaac Lab, and ROS 2 bag log guidance, added sim-real gap decomposition code, and made the exercise about reproducing hardware failure labels.

## Batch 002, Sections 1.5-1.8

Status: read and edited.

- `section-1.5.html`, The Physical AI framing and why 2023-2026 changed the field
  - Read: Physical AI framing, transfer abstraction, VLA and LeRobot callouts, production-depth layer, exercise, bibliography.
  - Weakness found: title-pasted epigraph, generic tool table, schema-only code, and generic transfer exercise.
  - Change made: rewrote the epigraph, replaced generic tools with Open X-Embodiment, OpenVLA, and LeRobot guidance, added a representation-versus-control transfer audit, and made the exercise about gripper transfer evidence fields.

- `section-1.6.html`, Examples: vacuum, drone, autonomous vehicle, manipulator, humanoid, game agent
  - Read: embodiment tuple, six-body comparison example, callouts, production-depth layer, exercise, bibliography.
  - Weakness found: title-pasted epigraph, overly cute callout, generic tool table, schema-only code, and generic exercise.
  - Change made: rewrote the epigraph, replaced the callout with command-to-contract framing, added Nav2, AirSim/PX4/Isaac Sim, CARLA, MuJoCo, and Isaac Lab guidance, added an embodiment matrix with reset-cost analysis, and made the exercise a two-body comparison matrix.

- `section-1.7.html`, Why embodied AI is hard
  - Read: hardness formula, worked hardness profile, callouts, production-depth layer, hands-on lab, exercise, bibliography.
  - Weakness found: title-pasted epigraph, generic tool table, schema-only code, and copied lab steps that did not build the hardness profile.
  - Change made: rewrote the epigraph, added hardness-specific tools, added dominant-mitigation code, rebuilt the lab around a hardness ledger and stress test, and made the exercise target costly resets.

- `section-1.8.html`, Map of the book
  - Read: routing theory, failure-to-part router, callouts, production-depth layer, exercise, bibliography.
  - Weakness found: title-pasted epigraph, generic tool table, schema-only code, and generic exercise.
  - Change made: rewrote the epigraph, replaced the tool table with artifact-routing packets, added a failure router that returns the chapter cluster and required artifact, and made the exercise ask for three project-specific failure labels.

## Batch 003, Sections 2.1-2.4

Status: read and edited.

- `section-2.1.html`, Agents and environments formally
  - Read: formal interface explanation, Gymnasium-style reset and step semantics, worked transition example, callouts, production-depth layer, exercise, bibliography.
  - Weakness found: generic reader pathway, repeated production-depth contract prose, generic tool advice, schema-only code, and generic failure analysis.
  - Change made: rewrote the pathway around reset and step ownership, added an interface audit for transition records, specialized tool advice for Gymnasium, PettingZoo, and ROS 2, and replaced generic failure analysis with transition-boundary checks.

- `section-2.2.html`, State, observation, hidden variables, partial observability
  - Read: state-observation distinction, belief update example, callouts, production-depth layer, exercise, bibliography.
  - Weakness found: generic pathway, title-pasted expected-output sentence, repeated production-depth contract prose, generic tool table, and schema-only code.
  - Change made: rewrote the pathway around visibility classes, corrected expected output, added a privileged-state leak test, specialized tool advice for filters, factor graphs, simulator state, and ROS 2 logs, and made the failure pattern about missing sensors, stale belief, uncertainty, and leakage.

- `section-2.3.html`, Action types
  - Read: action representation theory, action-space comparison code, callouts, production-depth layer, hands-on lab, exercise, bibliography.
  - Weakness found: generic pathway, generic production-depth layer, schema-only code, and a copied lab that did not audit action interfaces.
  - Change made: rewrote the pathway around units, frames, bounds, clipping, and recovery; added an action-interface audit; specialized tool advice for Gymnasium spaces, ROS 2 controllers, LeRobot, and VLA adapters; rebuilt the lab around action contract completeness, clipping, and chunk commitment.

- `section-2.4.html`, Rewards, goals, costs, constraints
  - Read: reward, goal, cost, and constraint distinction, scoring example, callouts, production-depth layer, exercise, bibliography.
  - Weakness found: generic pathway, title-pasted expected-output sentence, repeated production-depth contract prose, generic tool advice, schema-only code, and generic failure pattern.
  - Change made: rewrote the pathway around goal, reward, costs, and constraints; corrected expected output; added a reward-hacking audit; specialized tool advice for Gymnasium metric fields, Safety Gymnasium, safe RL tooling, control barrier functions, and runtime assurance.
