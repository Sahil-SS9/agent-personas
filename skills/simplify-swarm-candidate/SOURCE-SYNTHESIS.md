# Sources and scope

Original operational synthesis, not reproduced source text or copied code. Original instructions are MIT licensed; references retain their own copyrights and terms.

- Michael Feathers, Working Effectively with Legacy Code, publisher sample chapter 4 (The Seam Model): https://www.informit.com/content/images/0131177052/samplechapter/0131177052_ch04.pdf . Informs controllable dependencies, recording effects and proving that a test uses the intended substitution point. Selected chapter, not whole-book coverage.
- John Ousterhout, A Philosophy of Software Design, author-provided second-edition extract: https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf . Informs deep interfaces, cohesion, policy/mechanism separation and useful comments. Selected extract; no OCR code reused.
- Software Engineering at Google, chapter 22: https://abseil.io/resources/swe-book/html/ch22.html . Informs migration inventory and working intermediate changes. Original principles only; no chapter reproduction or relicensing of its text.
- Martin Fowler, preparatory refactoring: https://martinfowler.com/articles/preparatory-refactoring-example.html ; Branch by Abstraction: https://martinfowler.com/bliki/BranchByAbstraction.html . Informs small verified structural slices and staged interface migration.
- Google engineering practices: https://google.github.io/eng-practices/review/reviewer/standard.html . Informs separating defects from advice and optional preferences.
- Amazon Builders' Library: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/ . Informs intent identity and uncertain remote outcomes, conditional on the provider's actual guarantees.
- OWASP transaction authorization guidance: https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html . Informs approval/execution binding and mutable state; does not invent authorization requirements for unrelated products.
- Reference repositories: https://github.com/mattpocock/skills , https://github.com/magnus919/agent-skills , https://github.com/dietrichgebert/ponytail . Informed behavioural tests, role boundaries, understand-before-simplify and reuse-first decisions. No repository source files are redistributed in this collection.

Conflict resolution: retain cohesive interfaces rather than mandatory tiny functions; permit justified test seams; preserve caller-visible error and empty/missing distinctions; treat numerical reduction as subordinate to functionality. Parallel review requires host/user authority, consensus is not proof, and rollback is limited to owned changes. No forced findings, blanket reset, mandatory one-liners or promised reduction percentage.

Coverage is selective. Sources are engineering guidance, not proof of model performance. Evidence and limitations accompany the release; experimental publication is not a stable or independently reviewed certification.
