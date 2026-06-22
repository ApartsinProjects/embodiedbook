# Book Agent Sweep Run

Run id: 20260621-42agent-bookwide

Target: all section HTML files and chapter index files

Mode: implement

This directory contains instantiated prompts for all 42 local book-writers agent specifications.

Next steps:

1. Dispatch each prompt to the main context or a generic worker according to the gate order in `AGENT_EXECUTION_PROTOCOL.md`.
2. Update `agent-ledger.csv` after each agent finishes.
3. Store each agent final report in `agent-reports/`.
4. Run the final ledger completeness check before calling the pass complete.
