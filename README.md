# Coding Agent Harness

The self-contained kit is in **harness/**. It contains no application code and does not choose languages or frameworks.

Copy that directory into your project and follow [harness/HARNESS_GUIDE.md](harness/HARNESS_GUIDE.md). The operating rules are in [harness/HARNESS_RULES.md](harness/HARNESS_RULES.md); compact machine-readable state, tasks, and checks are in the same kit.

For a guided project setup, also copy [PROJECT_START_PROMPT.md](PROJECT_START_PROMPT.md), fill in its project and technology placeholders, and give it to the agent as the first instruction.

The mandatory software engineering requirements in [harness/HARNESS_RULES.md](harness/HARNESS_RULES.md) cover SOLID, KISS, DRY, YAGNI, separation of concerns, contracts, testability, reliability, and security. Apply them proportionally and use their completion criteria to verify each implementation; the optional validator checks harness consistency, not design quality.

The rules prohibit branch changes and Git write operations without specific authorization. They are not technical enforcement: also configure branch protections and tool approvals as explained in the guide.

[AGENTS.md](AGENTS.md) at the root is an entry-point reference for agents opening this repository. These two root documents support discovery; the complete reusable kit stays inside harness/.
