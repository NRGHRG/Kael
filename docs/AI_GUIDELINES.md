# AI Guidelines

These rules apply to AI-generated suggestions, code, documentation, reviews,
and repository changes in Project Kael.

## Collaboration

- Memo makes the final product and architecture decisions.
- Never claim work is complete without verifying it.
- Clearly distinguish facts, assumptions, proposals, and unresolved questions.
- Do not invent repository state; inspect the relevant files and Git history.
- Keep changes within the requested scope.
- Do not begin a new sprint without Memo's approval.

## Engineering

- Prefer clear, simple code over premature abstraction.
- Keep modules independent and responsibilities explicit.
- Add type hints to Python functions and methods.
- Use descriptive, consistent names.
- Do not introduce a dependency without explaining and justifying it.
- Avoid hidden side effects at import time.
- Read configuration from the configuration system instead of duplicating
  values in code.
- Handle expected failure modes with useful error messages.
- Preserve compatibility with the project's supported environment, currently
  Python on Windows.

## Quality

- Run the smallest meaningful verification for every change.
- Add automated tests when behavior becomes substantial enough to regress.
- Never commit generated artifacts such as `__pycache__` or `.pyc` files.
- Review the final diff for accidental or unrelated changes.
- Record meaningful architectural decisions in project documentation.
- Keep commits focused and use clear conventional commit messages.

## Safety and privacy

- Follow the permission and privacy principles in `KAEL_FOUNDATION.md`.
- Ask before destructive, irreversible, sensitive, or externally visible
  actions unless Memo explicitly authorized them for the current task.
- Never expose secrets, credentials, private data, or personal files.
- Do not weaken security or permission checks for convenience.

## Definition of done

A task is complete only when:

1. The requested behavior or document exists.
2. Relevant verification passes.
3. The diff contains no unrelated changes.
4. Documentation and project state remain accurate.
5. Memo has enough information to review the result.

A sprint additionally requires Memo's review and approval before the next
sprint begins.
