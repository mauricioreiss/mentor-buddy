# Maintenance: /mentor-buddy refresh

For whoever maintains a copy of this skill. Learning sessions only report drift; this mode applies it, with the maintainer approving every change.

1. Confirm the working folder is the skill's repository: `SKILL.md` and `references/` at the root, inside a git checkout. If it is not, say so in one line and stop; refresh edits files, and those edits belong in a checkout the maintainer can review.
2. Run `python scripts/check_links.py` (Python 3.10 or newer, standard library only). It prints a Markdown report with three lists: broken, moved (redirected to another page) and blocked (the site refuses automated requests; open those by hand).
3. For each broken or moved link, find the current official page and propose the replacement.
4. Check the stable claims that name a tool, a default or a practice in `phases.md`, `folder-roles.md`, `teaching-loop.md` and `code-review.md` against the official docs. Propose a change only with the official page that supports it.
5. Check each drift report the maintainer brings (an issue, or a learner's `8. Skill drift` section) the same way.
6. Show the proposed diff file by file, with the source of each change. Apply only what the maintainer approves, and update the "Links checked on" date of every file you verified.
7. Commit only when the maintainer asks. Pushing is always theirs.

The weekly workflow `.github/workflows/check-links.yml` runs the same script on GitHub and opens or updates an issue titled "Broken doc links" when a link breaks, so most refreshes start from that issue.
