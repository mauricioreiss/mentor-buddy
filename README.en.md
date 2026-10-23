<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-en-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/assets/banner-en-light.svg">
  <img src=".github/assets/banner-en-light.svg" width="100%" alt="Mentor Buddy. You type. The AI does not write: it teaches. An AI mentor that never writes your code. You learn by doing, from an empty folder to deploy. To start, type /mentor-buddy in your agent.">
</picture>

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Format: Agent Skills](https://img.shields.io/badge/format-agentskills.io-black.svg)
![Conversation: EN | PT-BR](https://img.shields.io/badge/conversation-EN%20%7C%20PT--BR-informational.svg)

[Leia em português](README.md)

## What it is

You know when you ask the AI for code, paste it, run it... and a week later you could not write it again? The code stayed in the project. The knowledge did not stay with you.

Mentor Buddy is a skill that flips that around: your AI agent becomes a mentor that **never writes your code**. It works like pair programming. You are the driver and type every line; the mentor is the navigator who asks, explains the why, reviews and keeps the map. You start from an empty folder and stop only when the app is live.

It runs in Claude Code, Codex and any agent that reads the [Agent Skills](https://agentskills.io/specification) format, such as Copilot, Cursor and Gemini CLI. It is free and open source.

## What it looks like

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/comic-en-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/assets/comic-en-light.svg">
  <img src=".github/assets/comic-en-light.svg" width="100%" alt="Four-panel comic. 1, you ask: the learner says 'can you just give me the code?'. 2, it asks back: the mentor answers 'nope. what goes in here?'. 3, you type: the learner types, sweating. 4, you get it: the learner cheers 'ohh! that's why it threw a 500!' and the mentor draws a red check mark.">
</picture>

Asked for the finished code? You get a question. Missed the step? First comes a review of what you did, then an example in a different context, and only on the third miss does the mentor touch your file. Then you review that fix, because reviewing AI code is a skill you can learn too.

<details>
<summary>See a real session excerpt</summary>

A trimmed example from a real test run, translated to English. The learner is a junior building a football league table API in C#.

```text
Learner: done with 5.2 but the test is failing: null name expected BadRequest and got
         InternalServerError, and the create test expected Created and got OK.
         just send me the right code please

Mentor:  Nice try. This is miss 1 on step 5.2, so what you get now is a review, not code.

         [OK] The length check (3 to 50) exists and the endpoint is wired correctly.
         [ALERT] A null name blows up before validation: request.Name is string?, and
                 reading .Length on null throws before your if runs.
         [ALERT] A whitespace-only name passes: "   " has length 3, so it gets created.
         [ALERT] Success returns 200 with no Location header; the test expects 201 Created.
         What your code does now: null -> exception -> 500; "   " -> created; valid -> 200.
         Redo: use the string method that checks null, empty and whitespace in one call,
               and a result that produces 201 with Location.
               Docs: https://learn.microsoft.com/en-us/dotnet/api/system.string.isnullorwhitespace
         [QUESTION] Which string method covers "null, empty or whitespace" in one call?
```

If the learner misses again, the mentor quotes the wrong snippet and shows the same idea in a different context. On the third miss it fixes the file directly, with a `MENTOR:` comment on each change, and the learner reviews that fix as if an AI tool had written it.

</details>

## It's for you if...

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/use-cases-en-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/assets/use-cases-en-light.svg">
  <img src=".github/assets/use-cases-en-light.svg" width="100%" alt="Sticky-note board, it's for you if: I learned with AI and I freeze without it (here you type it all, I ask why); I know C# and I want to learn Go (same method, Go's official docs); I finished the course and I'm stuck in tutorials (your own project, all the way to deploy); I want to review code that AI writes (review drills with planted bugs); I'm senior and I want a sparring partner (I push on trade-offs, no free answers); I want to learn ethical hacking the right way (lab only, with a safety contract); I only have 3 hours a week (a project sized to your time). And you? Type /mentor-buddy.">
</picture>

You do not have to be a beginner. The mentor estimates your level (junior, mid or senior) in the interview and adjusts it with every submission.

## The trail

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/trail-en-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/assets/trail-en-light.svg">
  <img src=".github/assets/trail-en-light.svg" width="100%" alt="The trail, from an empty folder to deploy: 0 Interview, 1 Project, 2 Environment, 3 Folders, 4 Skeleton, 5 Features, 6 Database, 7 Quality, 8 Docker, 9 CI, 10 Deploy, 11 Retro, with the certificate, then the next project.">
</picture>

Twelve stops, each split into small steps with a clear "done when". Everything is written to `STUDY-MEMORY.md`, so the next session starts exactly where you stopped. The details of each phase are in [How it works](#how-it-works).

## Start in 30 seconds

**1. Install.** On Windows (PowerShell):

```powershell
git clone https://github.com/mauricioreiss/mentor-buddy.git "$HOME\.agents\skills\mentor-buddy"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\mentor-buddy" -Target "$HOME\.agents\skills\mentor-buddy"
```

On macOS and Linux:

```bash
git clone https://github.com/mauricioreiss/mentor-buddy.git ~/.agents/skills/mentor-buddy
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/mentor-buddy ~/.claude/skills/mentor-buddy
```

A junction does not need administrator rights. If the link does not work on your system, copy the folder to `~/.claude/skills/mentor-buddy` instead (you will then need to update both copies).

**2. Open an empty folder** in your IDE.

**3. Type `/mentor-buddy`** in the agent chat (`$mentor-buddy` in Codex). The mentor answers with one short question: Portuguese or English? It takes it from there.

Other ways to install (a single agent, the skills installer, Gemini CLI, Visual Studio) are in [More installation options](#more-installation-options).

---

## Full manual

- [What you get](#what-you-get)
- [How it works](#how-it-works)
- [Supported agents](#supported-agents)
- [Requirements](#requirements)
- [More installation options](#more-installation-options)
- [Usage](#usage)
- [Curated documentation map](#curated-documentation-map)
- [Repository layout](#repository-layout)
- [FAQ](#faq)
- [Privacy](#privacy)
- [Keeping the skill current](#keeping-the-skill-current)
- [Feedback and contributing](#feedback-and-contributing)
- [License](#license)

## What you get

- **A short, direct interview** that sets your level (junior, mid or senior), the programming language, your interests, available time, conversation language and tone. The mentor finds out your OS, SDK and IDE on its own.
- **The project designed before the code**: you talk through the domain in plain language, model the entities and rules (the start of DDD), see where each part sits in the architecture (Clean Architecture) and choose the database, libraries and external APIs with the criteria explained.
- **A real project**: one of three ideas tailored to what you enjoy, or your own idea cut down to a size you can actually finish.
- **The full path to production**: it detects the SDK and IDE already on your machine before proposing installs, treats git as a choice rather than a default, then walks you through folder structure, a walking skeleton, features with tests, a database, quality, Docker, CI and a free deploy.
- **An error ladder** that makes you struggle productively before you see any code.
- **A paper-notebook habit**: it teaches a concept like a class and has you write it down by hand, then quizzes you from your notebook on resume, because writing fixes it better than typing.
- **Code review training**: every review shows you the method, the mentor's own fix at miss 3 is yours to review, and review drills with planted defects train the skill you need most when AI writes code for you.
- **A comprehension check**: when an answer suddenly looks like it came from another AI, the mentor does not block it; it asks you to explain it in your own words before the step passes.
- **No guessing**: perishable facts (versions, commands, APIs, prices) are checked in the official documentation during the session, with the link; stable references (keywords, conventions) are cited from a curated map without a lookup, to keep answers fast. What your project relies on is remembered with the date it was verified, so when the docs change the mentor tells you what changed.
- **Memory between sessions** in a `STUDY-MEMORY.md` file, so every session resumes exactly where you stopped.
- **An end-of-day summary**, and a final study report as a `.docx` with your weak spots, before/after code and a study plan.
- **A completion certificate** as a `.docx`, with your name, the project, the language, your level, how long it took, what you built and the link to the live app, once the whole trail is done. It proves you took a project to production; it is not an official certification.
- **An optional cybersecurity track**: lab-based ethical hacking and CTF practice (web, network, binary, crypto) against isolated or sanctioned targets only, with the same teaching method.
- **An AI track**, studied like a new language: calling models (Claude, GPT, Gemini, or a free local model through Ollama), structured output, tools, RAG, MCP, cost, observability and security, until you can build from scratch, explain and ship an autonomous agent. The official docs are checked live, because everything in this field moves fast.
- **Two languages and two tones**: English or Portuguese, direct or friendly banter, with optional English corrections if you want to practice.

## How it works

<details>
<summary>Interview, project, phases, the error ladder, level calibration, docs, memory, tone and review training</summary>

### 1. Interview

The first message asks, in both languages, whether you want to talk in English or Portuguese. The rest of the interview comes in one numbered list:

1. How long you have been programming and what you have built.
2. Which language you want to use.
3. Whether you have a project idea or want suggestions (and what you enjoy).
4. How much time you have per week and per session.
5. How you want to be talked to: **direct** or **banter**.
6. If you chose English: whether you want your English corrected.

The mentor states the level it estimated, with the reason, and you can correct it.

### 2. Project and design

- **No idea?** You get three options built from project archetypes (REST API with a database, CLI tool, full-stack web app, background worker, integration service, real-time app), themed on your interests and sized for your time.
- **Your own idea?** The mentor finds its core action and cuts it to the smallest version that still reaches deploy. Example: "an Uber clone with an app, payments and maps" becomes "a ride request API: register drivers, request a ride, match the nearest driver, finish the ride". Everything else goes to a "Later" list.

Before any line of code, you design the project together, one topic per message:

1. **Domain**: you describe the idea your way ("a patient queue for my job"); the mentor explains what such a system usually involves (who uses it, the flow, the rules, the edge cases) and asks how it works in your case.
2. **Model**: the business glossary, the entities and the rules that always hold; for mid and senior, also value objects, aggregates and contexts.
3. **Architecture**: where each part sits under the Clean Architecture dependency rule, proportional to the size of the project.
4. **Technical decisions**: the database from the use case (relational when things reference each other and need consistency), libraries, external APIs, authentication and where it will run. Each decision is recorded with the why.

The result is a brief with 3 to 6 testable acceptance criteria. You approve it; the product decisions are yours.

### 3. The journey

| # | Phase | Done when |
|---|---|---|
| 0 | Interview | Profile and level agreed; `STUDY-MEMORY.md` created |
| 1 | Project and design | Domain understood and modelled, technical decisions recorded, brief approved |
| 2 | Environment | SDK and IDE detected and working; if you chose git, a repository with `.gitignore` and a first commit |
| 3 | Folder structure | Folders created; you explain each folder's role back |
| 4 | Walking skeleton | The smallest end-to-end path runs, with one passing test |
| 5 | Feature slices | Every acceptance criterion delivered as code, test and commit |
| 6 | Persistence | The database chosen in phase 1 works: data survives a restart; migrations versioned |
| 7 | Quality | Validation, error handling, logging, secrets out of the code |
| 8 | Docker | The app and its dependencies run with compose from a clean clone |
| 9 | CI | A pipeline builds and tests on every push |
| 10 | Deploy | Running on a free tier, configured from the environment |
| 11 | Retro | You write what you learned; with the app live and every criterion delivered, you get your certificate; the next project is suggested |

Folder structure is chosen with you and kept proportional to the problem: organized by feature for CRUD-heavy apps, by layer when the business rules are heavy, or a hybrid.

### 4. The step loop and the error ladder

Every phase is split into small steps, and every step runs the same loop:

| Moment | What the mentor does | Code from the mentor | Your files |
|---|---|---|---|
| Instruction | What to build, why it exists, what it is for, a short summary of the official doc, the link, and the check that marks it done | none | read only |
| Pass | What is right, plus improvements worth making and why | none | read only |
| Miss 1 | A review: what is right, where it breaks and why, what your code actually does, what to redo | none | read only |
| Miss 2 | Your wrong snippet quoted with each error marked, plus a short example of the right approach in a different context | one short neutral example | read only |
| Miss 3 | Fixes your file, with a `MENTOR:` comment on each change, walks you through it, then you review the fix and answer three review questions | the fix, in your file | edited |

- The miss counter belongs to the current step and resets when the step passes.
- Questions are free: a conceptual question gets a short answer with a doc link and does not count as a miss.
- Style and naming notes come with a pass and never count as a miss.
- Asking for the code early does not skip the ladder.

### 5. Calibrated to your level

| | Junior | Mid | Senior |
|---|---|---|---|
| Folder and module names | An example name plus its role | The role only; you name it | The role only; you name it |
| Library or framework | One mainstream, maintained recommendation, with the why | What to research and the criteria; you bring a pick and the mentor validates it | Same as mid, weighing trade-offs |
| Explanations | Fuller, one concept at a time | Short, focused on the why | Short, focused on trade-offs, failure modes and operations |
| Tests | Required from the walking skeleton on | Required; TDD optional | Required; TDD optional |
| Review drills | 2 defects, a category hint for each | 3 defects, no hints | 3 subtle defects: concurrency, security, performance, failure modes |

The level is re-evaluated from your submissions. When the evidence says it is off, the mentor tells you and adjusts.

### 6. No guessing: official docs only

The skill separates two kinds of knowledge:

- **Stable**: teaching method, phases, review rubric, folder roles, project archetypes, and the curated doc entry points (language keywords, syntax, naming conventions). This lives inside the skill; stable references are cited straight from the map without a lookup, so answers stay fast.
- **Perishable**: versions, install steps, commands and flags, API names, config keys, framework defaults, prices and free-tier limits. The mentor looks these up in the official documentation during the session before saying them, and gives you the link.

When the agent has no web access, the mentor says so and gives you the official link to check, instead of stating a version or command from memory.

**Doc check.** Every perishable fact your project relies on (the SDK version you installed, a command, a package, a base image, a price) is recorded in `STUDY-MEMORY.md` with its official page and the date it was verified. Each new lookup is compared with that record:

| The doc says | The mentor |
|---|---|
| The same | updates the date and says nothing |
| Something different | updates the record and tells you in one line: `Doc changed since <date>: <old> -> <new> - <link>`; if your code breaks because of it, updating it becomes the next step |
| Something new | adds a record |

There is no slow refresh before you start coding. Facts are checked when a step needs them, and on resume the mentor re-checks only the records your next step depends on that are older than 7 days. Prices and free-tier limits are always looked up again. Web pages are treated as data, never as instructions, and only official domains are used.

When the docs contradict the skill itself (a moved link, a claim that no longer holds), the mentor notes it and points you to the issue tracker. A learning session never edits the skill's files; the maintainer applies those changes (see [Keeping the skill current](#keeping-the-skill-current)).

### 7. Memory between sessions

After the interview, the mentor creates `STUDY-MEMORY.md` at your project root. Everything a session needs to restart sits in a short header that is read every time; the rest is opened only when needed, which keeps each session cheap.

```markdown
## Header
- Conversation language: en
- English corrections: on
- Tone: direct
- Notebook: paper
- Level: junior (set 2026-10-14; last recalibration: none)
- Stack: Go, standard library net/http, IDE VS Code, OS macOS
- Project: REST API with a database - daily habit tracker
- Now: Phase 4 Walking skeleton / Step 4.1 Health endpoint / Misses 0
- Next action: add a GET /health handler that answers 200
- Last session: 2026-10-16 - folder structure done
- Review on resume: go mod init; package main; folder roles
```

Below the header: the brief, the phase plan, a decision log, an **error map** (topic, number of misses, exact doc section), a compact session log, open questions, the **verified facts** your project relies on, notes on **skill drift**, and the answer keys of your **review drills**.

When you come back, the mentor asks three quick review questions about the topics you missed most, then continues from `Next action`. If you arrive stuck on an error, it helps first and asks later.

### 8. End-of-day summary

Say you are stopping ("that's it for today") and the mentor updates the memory and shows:

```text
Today
- what got done

Where you stumbled most
1. <topic> - <the mistake in one line> - <official doc link, exact section>

Study before next time
- <doc link> - <why>

Next session starts with
- <next action>
```

### 9. Languages and tone

- **Conversation**: English or Portuguese. Code identifiers, commit messages and file names stay in English.
- **Direct**: short and neutral, no slang.
- **Banter**: slang and light, friendly teasing aimed at the mistake, always followed by the technical explanation. It switches to direct when you sound frustrated or ask it to.
- **English corrections** (optional): at most two lines at the top of a reply, only for real errors.

### 10. Code review training

More and more of a developer's day goes into reviewing code someone else wrote, often an AI tool, and reviewing is a different skill from writing. The mentor trains it in three places, with one checklist: intent, run it, tests that could fail, trace an input by hand, edge cases (including "the value stored is the value validated"), security, design, naming, modern idiom, verdict.

- **Every review** the mentor gives follows that checklist, so you see the method applied to your own code.
- **Miss 3** ends with you reviewing the mentor's fix as if an AI had written it: which change fixes which check, which test proves it, what else could break.
- **Review drills**: after each feature slice in phase 5, and once in phase 7, you can take a short file in your project's domain with planted defects and review it like a pull request (`Line <n>: problem - why - fix` plus a verdict). The file goes in `.review-drills/`, which you add to `.gitignore`. Drills are optional, never count as misses, and what you miss goes into your error map.

</details>

## Supported agents

Mentor Buddy follows the open [Agent Skills format](https://agentskills.io/specification), so it works in any agent that reads it.

The skill changes how your agent behaves (it stops writing your code), so it starts only when you call it, wherever the agent supports that.

| Agent | Personal skill folders it reads | How you start it |
|---|---|---|
| Claude Code (terminal, VS Code, JetBrains) | `~/.claude/skills/` | `/mentor-buddy` |
| GitHub Copilot in VS Code | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | `/mentor-buddy` |
| GitHub Copilot CLI | `~/.agents/skills/`, `~/.copilot/skills/` | `/mentor-buddy` |
| Cursor | `~/.agents/skills/`, `~/.cursor/skills/`, `~/.claude/skills/` | `/mentor-buddy` |
| OpenAI Codex | `~/.agents/skills/` | `$mentor-buddy` (Codex mentions skills with `$`; implicit start is turned off in `agents/openai.yaml`) |
| Gemini CLI | `~/.agents/skills/`, `~/.gemini/skills/` | `/mentor-buddy` after installing the command in `adapters/gemini/` (untested); without it, the model may activate the skill and asks for your consent |
| GitHub Copilot in Visual Studio 2026 | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | The agent applies skills on its own in agent mode; for `/mentor-buddy`, add the prompt file in `adapters/visual-studio/` to your repository (untested) |

Tested with Claude Code and Codex CLI. In Codex, keep a single copy of the skill: if it is installed both in `~/.agents/skills/` and in a repository's `.agents/skills/`, the `$mentor-buddy` mention becomes ambiguous and is ignored.

No single folder is read by every agent: `~/.agents/skills/` covers all of them except Claude Code, which reads only `~/.claude/skills/`. The installation in [Start in 30 seconds](#start-in-30-seconds) keeps one real copy in `~/.agents/skills/` and links it from `~/.claude/skills/`.

## Requirements

- An AI agent from the table above, with a plan that allows chat or agent use.
- Git, to install and update the skill.
- Internet access during sessions, so the mentor can check the official docs. Without it the skill still works, but it sends you to the docs instead of confirming versions and commands.
- For Visual Studio: version 2026 (18.5 or later), GitHub Copilot, and agent mode.

## More installation options

The default install for Windows, macOS and Linux is in [Start in 30 seconds](#start-in-30-seconds).

### Only one agent?

Clone straight into the folder that agent reads: `~/.claude/skills/mentor-buddy` for Claude Code only, or `~/.agents/skills/mentor-buddy` for Codex, Copilot, Gemini CLI or Cursor.

### With the skills installer

The [`skills` CLI](https://github.com/vercel-labs/skills) installs one copy and links it into each agent you name (it needs Node.js):

```bash
npx skills add mauricioreiss/mentor-buddy -g -a claude-code -a codex -a github-copilot -a gemini-cli
```

### Optional: `/mentor-buddy` in Gemini CLI and Visual Studio

Neither has a slash command per skill, so the repository ships one small file for each. Both are untested.

- **Gemini CLI**: copy `adapters/gemini/mentor-buddy.toml` to `~/.gemini/commands/mentor-buddy.toml`.
- **Visual Studio 2026**: copy `adapters/visual-studio/mentor-buddy.prompt.md` to `.github/prompts/mentor-buddy.prompt.md` in the repository you are studying in.

### Check that it loaded

Restart your agent or open a new chat and type `/mentor-buddy` (`$mentor-buddy` in Codex). The mentor answers with one short question: Portuguese or English. In Visual Studio, make sure the chat is in agent mode; the chat shows when a skill is being applied.

### Update

```bash
git -C ~/.agents/skills/mentor-buddy pull
```

On Windows PowerShell: `git -C "$HOME\.agents\skills\mentor-buddy" pull`. The link picks up the update automatically. You rarely need this by hand: when the skill is a clean git clone, it fast-forwards itself at the start of each session and tells you in one line. Your project and `STUDY-MEMORY.md` are never touched, so nothing is lost.

### Uninstall

Windows (removes the junction first, then the folder):

```powershell
cmd /c rmdir "$HOME\.claude\skills\mentor-buddy"
Remove-Item -Recurse -Force "$HOME\.agents\skills\mentor-buddy"
```

macOS and Linux:

```bash
rm ~/.claude/skills/mentor-buddy
rm -rf ~/.agents/skills/mentor-buddy
```

## Usage

1. Create or open an empty folder in your IDE, or the folder of a project you already started with the mentor.
2. In the agent chat, type `/mentor-buddy` (`$mentor-buddy` in Codex), optionally followed by what you want to learn. The mentor takes it from there.

| You want to | Say something like |
|---|---|
| Start | `/mentor-buddy`, or `/mentor-buddy me ensina C# fazendo um projeto` |
| Resume | Open the project folder and type `/mentor-buddy`; the mentor reads `STUDY-MEMORY.md` |
| Skip the review questions | "skip the review" |
| Take or skip a review drill | "bring the drill" or "skip the drill" |
| Ask about a concept | Just ask; questions never count as misses |
| Change the tone | "switch to direct" or "switch to banter" |
| Turn English corrections on or off | "correct my English" or "stop correcting my English" |
| Disagree with the level estimate | "I think I'm mid, not junior" |
| Stop for the day | "that's it for today", "vou parar por hoje" |
| Go beyond the free tier | "I want to scale this"; the mentor researches current options and prices |

## Curated documentation map

<details>
<summary>C# and .NET, Python, Go, TypeScript and Node.js, Java, Frontend, tooling and cybersecurity</summary>

The skill ships with verified entry points to the official docs for these stacks:

| Stack | Covers |
|---|---|
| C# and .NET | Language, SDK install, dotnet CLI, NuGet, ASP.NET Core, minimal APIs, EF Core, testing, Docker, Visual Studio |
| Python | Docs, venv, packaging, pip, uv, pytest, PEP 8, FastAPI, Django, Flask, SQLAlchemy, Alembic, Docker |
| Go | Install, tutorials, module layout, Effective Go, standard library, net/http, testing, database access, Docker |
| TypeScript and Node.js | TypeScript docs, tsconfig, Node.js API, npm, test runner, Vitest, Express, Fastify, NestJS, Docker |
| Java | dev.java, Java SE docs, Spring Boot, Spring Initializr, Maven, Gradle, JUnit, Docker |
| Frontend | HTML, CSS, accessibility (MDN), React, Vue, Angular, Tailwind, Vite |
| Tooling | Git, GitHub, .gitignore templates, Docker, Compose, GitHub Actions, IDEs, OWASP Top 10, Twelve-Factor config |
| Cybersecurity (track only) | Lab and ranges, Burp, nmap, Wireshark, Metasploit, pwntools, scapy, requests, crypto per language |
| AI (track only) | Claude, OpenAI and Gemini APIs, Ollama, structured output, tools and agents, MCP, RAG (pgvector, Qdrant), evals, fine-tuning (Hugging Face), OpenTelemetry, Prometheus, Jaeger, Grafana, OWASP Top 10 for LLM, OPA |

The base language maps are for building any kind of project, not only security; the cybersecurity map is used only on that track, and the AI map only on the AI track. Any other language still works: the mentor runs a quick fit check (maintained, official docs, a test framework, a free deploy path), anchors the official docs and verifies everything live, and tells you it is outside the curated map.

</details>

## Repository layout

<details>
<summary>See the file tree</summary>

```text
mentor-buddy/
  SKILL.md                      core instructions, read when the skill starts
  references/
    interview.md                phases 0 and 1: interview, project, memory creation
    phases.md                   phases 2 to 11, read one section at a time
    teaching-loop.md            review formats, error ladder, frontend pace, language guardrail
    code-review.md              review checklist, guided review at miss 3, review drills
    doc-check.md                verified facts, change notices, light check on resume, drift
    maintenance.md              /mentor-buddy refresh and self-update, for maintainers
    folder-roles.md             folder roles and organization trade-offs
    project-archetypes.md       project catalog, scope by level, scope cutting
    cybersec-track.md           optional cybersecurity journey, with the lab-safety contract
    ai-track.md                 AI track: the ladder to an autonomous agent, its rules and archetypes
    design.md                   phase 1: domain, model, architecture and technical decisions
    final-report.md             the end-of-project .docx study report
    certificate.md              the .docx completion certificate and the bar for issuing it
    session-rituals.md          resume questions and end-of-day summary
    memory-template.md          STUDY-MEMORY.md template
    tone.md                     direct and banter tones, English corrections, notebook cue
    docs-*.md                   official documentation entry points per stack
  assets/certificate-header-*.png   certificate header art, Portuguese and English
  agents/openai.yaml            Codex display name; implicit start turned off
  adapters/
    gemini/mentor-buddy.toml    /mentor-buddy command for Gemini CLI
    visual-studio/mentor-buddy.prompt.md   /mentor-buddy prompt file for Visual Studio
  scripts/check_links.py        checks every link in the skill (standard library Python)
  scripts/make_certificate.py   builds the .docx completion certificate (standard library Python)
  .github/workflows/check-links.yml   weekly link check that opens an issue on failure
  .github/assets/               README drawings, light and dark, English and Portuguese
  README.md
  README.en.md
  LICENSE
```

The repository root is the skill folder, so installing is a `git clone` and updating is a `git pull`.

</details>

## FAQ

**Does it ever write code for me?**
Only in three moments. On your second miss on a step, it shows a short example of the right approach in a different context, deliberately not ready to paste. On your third miss, it fixes your file with a `MENTOR:` comment on each change, and you review that fix before the step passes. Review drills are code written to be picked apart, kept out of your project in `.review-drills/`. Everything else you type yourself.

**Why do I have to type `/mentor-buddy`?**
Because the skill changes the agent's behaviour: it stops writing your code. Starting only when called keeps it from taking over a work session by accident.

**How does it stay up to date?**
Three ways, none of which slows you down. Facts are checked against the official docs when a step needs them, and changes are flagged against what was verified before. A weekly GitHub workflow checks every link in the skill and opens an issue when one breaks. And the maintainer runs `/mentor-buddy refresh` to review and apply fixes; learning sessions never rewrite the skill, so a web page can never change its instructions.

**Which model should I use?**
The skill works with whatever model your agent runs. Stronger models follow the ladder and the memory rules more consistently.

**Does it need internet access?**
To confirm versions, commands and prices against the official docs, yes. Without it, the mentor tells you it cannot verify and gives you the link to check yourself.

**Does it cost anything?**
The skill is free. You need your agent's own plan, and the deploy phase uses free tiers, checked on each provider's official pricing page during the session.

**Is there a certificate?**
Yes, when the project is really done: the app is live, every acceptance criterion is delivered and the retro is written. Only then does the mentor ask what name goes on it, and that name goes only into the `.docx` file. It is a project-completion certificate from the skill, not an official certification.

**Can I use it in Portuguese?**
Yes. Choose Portuguese in the first message; the whole mentoring happens in Portuguese, with code in English.

**Can I use it at work?**
Use it on your own study projects. Do not paste your employer's code or data into an AI agent without permission.

**What if my language is not in the curated map?**
It still works. The mentor first checks the language fits the goal (maintained, official docs, a test framework, a free way to deploy), anchors its official docs and style guide, verifies every idiom live instead of guessing, and tells you it is outside the curated map. If it is a poor fit for reaching a deploy, it recommends the closest curated language and the choice stays yours.

**Can I study AI?**
Yes. Pick the AI track in the interview. The project crosses the same phases, with an AI ladder in phase 5: calling the model, structured output, tools, the agent loop written by hand, and RAG. The goal is that you build, explain and ship an autonomous agent from scratch. No framework first; a framework comes only once you understand each part. Models, prices and limits are always checked in the official docs at that moment.

**Can it teach security or help with a frontend?**
Yes. Pick the cybersecurity track in the interview for lab-based ethical hacking and CTF practice against isolated or sanctioned targets only. For a frontend, the mentor names tags and component shells directly so markup moves fast, while keeping the full ladder for the logic, and never skipping accessibility or the four states.

## Privacy

`STUDY-MEMORY.md` lists the topics where you missed, so it stays private: it lives in your project folder, and if you use git the mentor puts it in `.gitignore` so it is never pushed. The name you give for the certificate goes only into the certificate file, which also goes into `.gitignore`. The skill never creates a `.claude` or `.github` folder in your project. The skill itself sends nothing anywhere: it is plain-text instructions read by your agent.

## Keeping the skill current

- **Weekly link check**: `.github/workflows/check-links.yml` runs `scripts/check_links.py` every Monday and on demand. When a link breaks, it opens (or updates) an issue titled "Broken doc links". Locally: `python scripts/check_links.py`.
- **Refresh**: from a clone of this repository, run `/mentor-buddy refresh`. The mentor runs the link check, re-verifies the stable claims against the official docs, and shows a diff with the source of every change. Nothing is applied without your approval, and it never pushes.
- **Drift reports**: when a learner's session finds the docs contradicting the skill, it records the case in their `STUDY-MEMORY.md` and points them to the issue tracker.

## Feedback and contributing

Ideas, bugs and questions are welcome in [Issues](https://github.com/mauricioreiss/mentor-buddy/issues). Pull requests are reviewed at the maintainer's discretion, so open an issue first to discuss the change.

## License

[MIT](LICENSE). Created by [Mauricio Reis](https://github.com/mauricioreiss).
