# Phases 2 to 11

Phases 0 and 1 live in [interview.md](interview.md). On entering a phase, read only its section here, expand its steps in the memory (each with a `done when`), and run the step loop for each one. Anything marked *verify live* is perishable: look it up in the official docs for the learner's OS and versions before saying it.

Contents: 2 Environment · 3 Folder structure · 4 Walking skeleton · 5 Feature slices · 6 Persistence · 7 Quality · 8 Docker · 9 CI · 10 Deploy · 11 Retro

## 2. Environment

Find what the learner already has before proposing anything. Do not ask them to confirm, and do not send them to install, what the machine can answer for itself.

Typical steps:
1. **Detect the toolchain.** With their OS, check what is already installed before recommending anything: the SDK or runtime version (for example `dotnet --info`, `python --version`, `go version`, `node --version`, `java -version`) and the IDE they named in the interview. The driver runs the commands and pastes the output. Use what is there. Only when a tool is missing, or too old for the project (*verify live*: the current supported version on the official install page), do you send them to install it.
2. Set up the IDE support the language needs, if it is not already present (*verify live*).
3. **Ask how they want to run the setup: through the IDE or through PowerShell / the terminal.** Record the choice in Decisions and honour it for the rest of the project. If they choose the IDE, tell them to open it and walk them click by click (where the integrated terminal is, where the setting lives, which menu). If they choose the shell, give the exact command to run.
4. **Decide on git. Ask whether this project will use git at all; do not assume it.**
   - **No git**: skip the repository steps, note the decision in Decisions, and move on. The memory file just stays in the project folder.
   - **Git**: install git if missing and set name and email; initialise the repository in the project folder; add a `.gitignore` from the official template for their stack (github/gitignore) and make sure `.env` **and `STUDY-MEMORY.md`** are in it (the study memory is private and never goes up); first commit a README with the project pitch.
5. Optional, only with git and only if they want it: create the remote repository on their own account and push.

Done when the runtime's version output is shared and, if they chose git, `git log` shows the first commit.

Watch for: installing something they already had; build output or IDE folders committed; secrets in any file; `STUDY-MEMORY.md` tracked by git.

## 3. Folder structure

Typical steps:
1. Choose the organization (by feature, by layer or hybrid) using [folder-roles.md](folder-roles.md). A junior gets a recommendation; a mid or senior decides and justifies. Record it in Decisions.
2. Generate the project with the official template or CLI (*verify live*: the current command and template name).
3. Create the folders by role. Junior: example names plus roles. Mid and senior: roles only.
4. The learner explains each folder's role back in one line.

Done when the folder tree matches the chosen organization and every role is explained back correctly.

Watch for: folders without a purpose, a `utils` dumping ground, a layered architecture forced onto a simple CRUD.

## 4. Walking skeleton

Typical steps:
1. The smallest end-to-end path: an API health endpoint that answers, a CLI that runs and prints its version, a worker that consumes one message and logs it.
2. Set up the test framework (*verify live*) and write one test of real behaviour.
3. Run both from the terminal and from the IDE.
4. Commit.

Done when the app runs, the test passes, and both outputs are shared.

Watch for: a test that asserts nothing meaningful; hard-coded configuration.

## 5. Feature slices

Typical steps:
1. Turn each acceptance criterion into one or more vertical slices, ordered by dependency. Record the list in the plan.
2. For each slice: input, logic, output, a test, then a commit with an English message describing the change.
3. After each slice passes, offer a review drill ([code-review.md](code-review.md) section 4). The learner may skip it.

Done when every acceptance criterion has a passing test and its commit.

Watch for: slices too big to review, skipped tests, business rules inside HTTP handlers, duplicated rules across features.

Senior focus where it fits naturally: idempotency, pagination, concurrency, failure modes.

## 6. Persistence

Skip when the archetype stores nothing.

Typical steps:
1. Choose storage proportional to the project: an embedded database or file for a CLI, a server database for an API. Junior: recommendation. Mid and senior: research brief.
2. Read connection settings from the environment.
3. Version the schema with migrations (*verify live*: the tool's current commands).
4. Put data access in its role folder.
5. Integration test against a real database, in a container when the level allows.

Done when data survives a restart, migrations are in git, and every query is parameterized.

Watch for: credentials in code; SQL built by string concatenation; N+1 queries; missing indexes on obvious lookups (mid and senior).

## 7. Quality

Typical steps:
1. Validate input at the boundary with clear error responses.
2. Handle errors in one consistent place instead of scattered try/catch.
3. Logging with useful context (structured logs for mid and senior), without sensitive data.
4. Secrets only from the environment; confirm none is in the repository history.
5. Walk the relevant items of the OWASP Top 10 for this app (injection, broken access control, and so on).
6. One larger review drill on this phase's topics: validation, error handling, logging, secrets ([code-review.md](code-review.md) section 4).

Done when invalid input gets a clear error, logs show useful context, and a search of the repository finds no secret.

Watch for: swallowed exceptions, logging passwords or tokens, validation only on the client.

## 8. Docker

Typical steps:
1. A Dockerfile, multi-stage when the stack compiles (*verify live*: official base image and tags).
2. A `.dockerignore` that keeps `.env`, build output and IDE files out.
3. A compose file with the app and its dependencies, configured through environment variables, with a healthcheck.
4. Run it from a fresh clone.

Done when `docker compose up` from a clean clone serves the app and the image contains no secrets.

Watch for: copying `.env` into the image; running as root (mid and senior); very large images.

## 9. CI

Typical steps:
1. A pipeline on the platform hosting their repository (GitHub Actions by default, *verify live*): on push and pull request, restore dependencies, build, test.
2. Optionally build the container image.
3. Break a test on purpose, watch the pipeline go red, fix it, watch it go green.

Done when a push runs green and the deliberate failure turned it red.

Watch for: secrets written in the workflow file instead of the platform's secret store.

## 10. Deploy

Free path only, until the learner asks to scale.

Typical steps:
1. Research live which providers currently offer a free tier that fits the archetype (container web service, static site, database). Check each limit on the official pricing page: sleep when idle, monthly hours, database expiry. Junior: one recommendation. Mid and senior: two or three options, they choose.
2. The learner creates the account and connects the repository or pushes the image.
3. Configure environment variables and secrets on the platform.
4. Smoke test the live address against the acceptance criteria.

CLI archetype: deploying means publishing a release artifact (for example a release on their repository or an image in a registry; *verify live*).

Done when the live address (or the published artifact) works and all configuration comes from the environment.

Scaling: only on request. Research VPS and cloud options live, with current prices from official pages.

## 11. Retro

Typical steps:
1. The learner writes, in their own words: what they built, three things they learned, the hardest bug, what they would do differently. Review it like code.
2. From the error map, suggest what to study next, with doc links.
3. Suggest the next project: one level harder or a different archetype.
4. Offer the final report as a `.docx` ([final-report.md](final-report.md)): their weak spots with before/after code and a study plan. Generate it when they accept.
5. Mark the project complete in the memory.

Done when the retro is written, the report is offered, and the next project is suggested.
