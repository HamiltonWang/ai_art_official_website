---
trigger: model_decision
description: Enforce explicit user permission before committing code to Git.
---
# Git Commit Policy

- **Never** run `git commit` on your own to finalize tasks.
- **Always** stage changes (`git add`) and ask the user for explicit permission or review before proceeding to commit.
- **Include Issue Number (When Available):** Whenever a commit addresses one or more GitHub issues or ticket numbers, append the issue reference at the end of the commit subject in parentheses:
  - Single issue: `<type>(<scope>): <summary> (#<issue>)` (e.g., `fix(strategy): cap unbooked loss absorption (#12)`)
  - Multiple issues: `<type>(<scope>): <summary> (#<issue1>, #<issue2>)`
  - If no issue number is associated with the change, omit the `(#...)` suffix rather than inventing one.
