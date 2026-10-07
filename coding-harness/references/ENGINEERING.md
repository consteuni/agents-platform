# Engineering Requirements

Software engineering principles are mandatory for every implementation and review. Apply them in proportion to actual requirements and existing architecture; a small change does not require a new framework, layer, or document. Working output alone is insufficient: the result must be understandable, testable, and maintainable.

## Design and Simplicity

- **Separation of concerns, cohesion, and coupling:** keep business rules separate from presentation, persistence, configuration, and external I/O where those responsibilities exist. Give modules a clear purpose and explicit dependencies; avoid hidden global state and circular dependencies.
- **SOLID:** apply these principles where the design has the corresponding responsibilities or interfaces; they do not require object-oriented code.
  - **Single Responsibility:** a component has one cohesive responsibility and a clear reason to change. Split components that mix unrelated policies.
  - **Open/Closed:** use existing extension points for supported variation while preserving contracts; introduce a new abstraction only when a current requirement justifies it.
  - **Liskov Substitution:** implementations must honor the same inputs, outputs, error behavior, and invariants as the contract they replace.
  - **Interface Segregation:** expose small interfaces aligned with consumer needs; do not make callers depend on unrelated capabilities.
  - **Dependency Inversion:** keep core policy independent of concrete infrastructure through explicit contracts or injected functions/dependencies when needed. Do not add a dependency-injection framework by default.
- **KISS (Keep It Simple):** choose the simplest design that satisfies acceptance criteria. Prefer readable control flow, clear names, and small cohesive functions over cleverness.
- **DRY (Don't Repeat Yourself):** maintain one authoritative definition of business rules and contracts. Reuse proven common behavior; similar-looking code with different reasons to change need not share an abstraction.
- **YAGNI (You Aren't Gonna Need It):** implement current requirements only. Do not build speculative extension systems, generic repositories, services, or configuration layers.
- Favor composition when it simplifies change and testing; use inheritance only for a valid substitutable relationship. Fit the project's established architecture rather than imposing a design pattern.

## Contracts, Data, and Reliability

- Define observable success and error behavior before implementation. Validate inputs at trust boundaries, make invariants explicit, and use types or schemas supported by the chosen stack.
- Preserve public contracts and data compatibility. For a required breaking change, document affected consumers and the migration path; keep schema changes and data migrations reviewable and recoverable where applicable.
- Make side effects explicit. Release resources reliably and use transactions or equivalent consistency boundaries for related writes; define behavior after partial failure. Follow the existing timeout, retry, and idempotency rules for external operations.
- Handle expected failures deliberately and preserve useful diagnostic context. Do not silently swallow exceptions, return misleading success, or expose internal errors or sensitive data to users.
- Treat security and privacy as design constraints: validate authorization at the relevant boundary, use least privilege and parameterized queries where applicable, and keep secrets outside code. Log only the information needed for diagnosis.
- Meet stated performance and resource constraints with evidence. Measure before optimizing; avoid adding complexity for an unmeasured bottleneck.

## Testability and Change Review

- Keep deterministic logic independently testable where practical; isolate clocks, randomness, storage, network calls, and other external dependencies when relevant to changed behavior.
- Select checks from acceptance criteria and risk: success, relevant error and boundary cases, regressions, and contract or integration behavior when affected. Test observable behavior rather than mirroring implementation details.
- Use the nearest configured checks for the selected stack. Do not invent coverage targets, mandatory tools, or tests for trivial documentation changes. Mocks do not prove a real integration works.
- Keep changes focused, dependencies justified, and documentation aligned with actual behavior. Record significant design tradeoffs and intentional exceptions in the target project's decision record, including rationale, impact, and any follow-up.

## Engineering Completion Criteria

Before marking an implementation `verified`, confirm and record proportionate evidence in the target project's verification record:

1. Required behavior and relevant failure cases satisfy the task's acceptance criteria.
2. Responsibilities and dependencies are clear; the change adds no unjustified duplication, coupling, abstractions, or dependencies.
3. Affected contracts, data integrity, resource cleanup, security, and compatibility have been checked where applicable.
4. Relevant configured tests and checks pass, with their scope and limitations stated; review findings are resolved or explicitly recorded.
5. Documentation and state match the result, and significant tradeoffs are recorded. Explain material non-applicability or an intentional exception; do not claim compliance without evidence.

Apply these criteria through relevant project checks and explicit review. Instructions alone cannot certify design quality or enforce permissions.

