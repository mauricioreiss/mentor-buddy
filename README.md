# Mentor Buddy

**An AI agent skill that turns your coding assistant into a mentor who never writes your code.** You type every line. It interviews you, plans a real project with you, and guides you step by step from an empty folder to a deployed app.

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Format: Agent Skills](https://img.shields.io/badge/format-agentskills.io-black.svg)
![Conversation: EN | PT-BR](https://img.shields.io/badge/conversation-EN%20%7C%20PT--BR-informational.svg)

[Leia em português](README.pt-BR.md)

---

## Contents

- [Why this exists](#why-this-exists)
- [What you get](#what-you-get)
- [A session, in short](#a-session-in-short)
- [How it works](#how-it-works)
- [Supported agents](#supported-agents)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Curated documentation map](#curated-documentation-map)
- [Repository layout](#repository-layout)
- [FAQ](#faq)
- [Privacy](#privacy)
- [Feedback and contributing](#feedback-and-contributing)
- [License](#license)

---

## Why this exists

Learning to program with AI usually turns into copy and paste: you ask, the assistant writes the code, it runs, and a week later you could not write it again. The code stays in the project; the knowledge does not stay with you.

Mentor Buddy flips the roles. It works like pair programming where the AI is the **navigator** and you are the **driver**: you type every line and every command, and the mentor explains, asks, reviews and keeps the map. It only touches your code after you have missed three times on the same step, and even then it explains every change.

It is built for anyone who wants to learn hands-on with an AI agent: beginners who know the basics, developers moving to a new language, and seniors who want a sparring partner that pushes on trade-offs instead of handing out answers.

## What you get

- **A short interview** that sets your level (junior, mid or senior), the programming language, your interests, available time, IDE, conversation language and tone.
- **A real project**: one of three ideas tailored to what you enjoy, or your own idea cut down to a size you can actually finish.
- **The full path to production**: environment, folder structure, walking skeleton, features with tests, database, quality, Docker, CI and a free deploy.
- **An error ladder** that makes you struggle productively before you see any code.
- **No guessing**: versions, commands, APIs and prices are checked in the official documentation during the session, with the link.
- **Memory between sessions** in a `STUDY-MEMORY.md` file, so every session resumes exactly where you stopped.
- **An end-of-day summary** with the topics where you missed most and the exact doc sections to study.
- **Two languages and two tones**: English or Portuguese, direct or friendly banter, with optional English corrections if you want to practice.

## A session, in short

A trimmed example from a real test run, translated to English. The learner is a junior building a football league table API in C#.

```text
Learner: done with 5.2 but the test is failing: null name expected BadRequest and got
         InternalServerError, and the create test expected Created and got OK.
         just send me the right code please

Mentor:  Nice try. You're on attempt 1 of step 5.2, so what you get now is a review, not code.

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

If the learner misses again, the mentor quotes the wrong snippet and shows the same idea in a different context. On the third miss it fixes the file directly, with a `MENTOR:` comment on each change, and asks the learner to explain the fix back.

## How it works

### 1. Interview

The first message asks, in both languages, whether you want to talk in English or Portuguese. The rest of the interview comes in one numbered list:

1. How long you have been programming and what you have built.
2. Which language you want to use.
3. Whether you have a project idea or want suggestions (and what you enjoy).
4. How much time you have per week and per session.
5. Your operating system and IDE.
6. How you want to be talked to: **direct** or **banter**.
7. If you chose English: whether you want your English corrected.

The mentor states the level it estimated, with the reason, and you can correct it.

### 2. Project

- **No idea?** You get three options built from project archetypes (REST API with a database, CLI tool, full-stack web app, background worker, integration service, real-time app), themed on your interests and sized for your time.
- **Your own idea?** The mentor finds its core action and cuts it to the smallest version that still reaches deploy. Example: "an Uber clone with an app, payments and maps" becomes "a ride request API: register drivers, request a ride, match the nearest driver, finish the ride". Everything else goes to a "Later" list.

The result is a brief with 3 to 6 testable acceptance criteria. You approve it; the product decisions are yours.

### 3. The journey

| # | Phase | Done when |
|---|---|---|
| 0 | Interview | Profile and level agreed |
| 1 | Project | Brief approved; `STUDY-MEMORY.md` created |
| 2 | Environment | SDK, IDE and git working; repository with `.gitignore` and a first commit |
| 3 | Folder structure | Folders created; you explain each folder's role back |
| 4 | Walking skeleton | The smallest end-to-end path runs, with one passing test |
| 5 | Feature slices | Every acceptance criterion delivered as code, test and commit |
| 6 | Persistence | Data survives a restart; migrations versioned |
| 7 | Quality | Validation, error handling, logging, secrets out of the code |
| 8 | Docker | The app and its dependencies run with compose from a clean clone |
| 9 | CI | A pipeline builds and tests on every push |
| 10 | Deploy | Running on a free tier, configured from the environment |
| 11 | Retro | You write what you learned; the next project is suggested |

Folder structure is chosen with you and kept proportional to the problem: organized by feature for CRUD-heavy apps, by layer when the business rules are heavy, or a hybrid.

### 4. The step loop and the error ladder

Every phase is split into small steps, and every step runs the same loop:

| Moment | What the mentor does | Code from the mentor | Your files |
|---|---|---|---|
| Instruction | What to build, why it exists, what it is for, a short summary of the official doc, the link, and the check that marks it done | none | read only |
| Pass | What is right, plus improvements worth making and why | none | read only |
| Miss 1 | A review: what is right, where it breaks and why, what your code actually does, what to redo | none | read only |
| Miss 2 | Your wrong snippet quoted with each error marked, plus a short example of the right approach in a different context | one short neutral example | read only |
| Miss 3 | Fixes your file, with a `MENTOR:` comment on each change, then walks you through it | the fix, in your file | edited |

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

The level is re-evaluated from your submissions. When the evidence says it is off, the mentor tells you and adjusts.

### 6. No guessing: official docs only

The skill separates two kinds of knowledge:

- **Stable**: teaching method, phases, review rubric, folder roles, project archetypes. This lives inside the skill and changes only when the repository is updated.
- **Perishable**: versions, install steps, commands and flags, API names, config keys, framework defaults, prices and free-tier limits. The mentor looks these up in the official documentation during the session before saying them, and gives you the link.

When the agent has no web access, the mentor says so and gives you the official link to check, instead of stating a version or command from memory.

### 7. Memory between sessions

After the interview, the mentor creates `STUDY-MEMORY.md` at your project root. Everything a session needs to restart sits in a short header that is read every time; the rest is opened only when needed, which keeps each session cheap.

```markdown
## Header
- Conversation language: en
- English corrections: on
- Tone: direct
- Level: junior (set 2026-10-14; last recalibration: none)
- Stack: Go, standard library net/http, IDE VS Code, OS macOS
- Project: REST API with a database - daily habit tracker
- Now: Phase 4 Walking skeleton / Step 4.1 Health endpoint / Attempt 0
- Next action: add a GET /health handler that answers 200
- Last session: 2026-10-16 - folder structure done
- Review on resume: go mod init; package main; folder roles
```

Below the header: the brief, the phase plan, a decision log, an **error map** (topic, number of misses, exact doc section), a compact session log and open questions.

When you come back, the mentor asks three quick review questions about the topics you missed most, then continues from `Next action`.

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

## Supported agents

Mentor Buddy follows the open [Agent Skills format](https://agentskills.io/specification), so it works in any agent that reads it.

| Agent | Personal skill folders it reads | How the skill starts |
|---|---|---|
| Claude Code (terminal, VS Code, JetBrains) | `~/.claude/skills/` | Automatically from the description, or `/mentor-buddy` |
| GitHub Copilot in Visual Studio 2026 | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | Automatically in agent mode |
| GitHub Copilot in VS Code | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | Automatically, or `/mentor-buddy` |
| GitHub Copilot CLI | `~/.agents/skills/`, `~/.copilot/skills/` | Automatically, or `/mentor-buddy` |
| OpenAI Codex | `~/.agents/skills/` | Automatically, or `$mentor-buddy` |
| Gemini CLI | `~/.agents/skills/`, `~/.gemini/skills/` | The model activates it and asks for your consent |
| Cursor | `~/.agents/skills/`, `~/.cursor/skills/`, `~/.claude/skills/` | Automatically, or `/mentor-buddy` |

No single folder is read by every agent: `~/.agents/skills/` covers all of them except Claude Code, which reads only `~/.claude/skills/`. The installation below keeps one real copy in `~/.agents/skills/` and links it from `~/.claude/skills/`.

## Requirements

- An AI agent from the table above, with a plan that allows chat or agent use.
- Git, to install and update the skill.
- Internet access during sessions, so the mentor can check the official docs. Without it the skill still works, but it sends you to the docs instead of confirming versions and commands.
- For Visual Studio: version 2026 (18.5 or later), GitHub Copilot, and agent mode.

## Installation

### Windows (PowerShell)

```powershell
git clone https://github.com/mauricioreiss/mentor-buddy.git "$HOME\.agents\skills\mentor-buddy"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\mentor-buddy" -Target "$HOME\.agents\skills\mentor-buddy"
```

A junction does not need administrator rights.

### macOS and Linux

```bash
git clone https://github.com/mauricioreiss/mentor-buddy.git ~/.agents/skills/mentor-buddy
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/mentor-buddy ~/.claude/skills/mentor-buddy
```

If the link does not work on your system, copy the folder to `~/.claude/skills/mentor-buddy` instead (you will then need to update both copies).

### Only one agent?

Clone straight into the folder that agent reads: `~/.claude/skills/mentor-buddy` for Claude Code only, or `~/.agents/skills/mentor-buddy` for Codex, Copilot, Gemini CLI or Cursor.

### Check that it loaded

Restart your agent or open a new chat, then say: "I want to study with mentor buddy". Where slash commands exist, `/mentor-buddy` should also appear. In Visual Studio, make sure the chat is in agent mode; the chat shows when a skill is being applied.

### Update

```bash
git -C ~/.agents/skills/mentor-buddy pull
```

On Windows PowerShell: `git -C "$HOME\.agents\skills\mentor-buddy" pull`. The link picks up the update automatically.

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
2. In the agent chat, say what you want to learn. The mentor takes it from there.

| You want to | Say something like |
|---|---|
| Start | "I want to study with mentor buddy", "teach me Go by building a project", "me ensina C# fazendo um projeto" |
| Resume | Open the project folder and say hi; the mentor reads `STUDY-MEMORY.md` |
| Skip the review questions | "skip the review" |
| Ask about a concept | Just ask; questions never count as misses |
| Change the tone | "switch to direct" or "switch to banter" |
| Turn English corrections on or off | "correct my English" or "stop correcting my English" |
| Disagree with the level estimate | "I think I'm mid, not junior" |
| Stop for the day | "that's it for today", "vou parar por hoje" |
| Go beyond the free tier | "I want to scale this"; the mentor researches current options and prices |

## Curated documentation map

The skill ships with verified entry points to the official docs for these stacks:

| Stack | Covers |
|---|---|
| C# and .NET | Language, SDK install, dotnet CLI, NuGet, ASP.NET Core, minimal APIs, EF Core, testing, Docker, Visual Studio |
| Python | Docs, venv, packaging, pip, uv, pytest, PEP 8, FastAPI, Django, Flask, SQLAlchemy, Alembic, Docker |
| Go | Install, tutorials, module layout, Effective Go, standard library, net/http, testing, database access, Docker |
| TypeScript and Node.js | TypeScript docs, tsconfig, Node.js API, npm, test runner, Vitest, Express, Fastify, NestJS, Docker |
| Java | dev.java, Java SE docs, Spring Boot, Spring Initializr, Maven, Gradle, JUnit, Docker |
| Tooling | Git, GitHub, .gitignore templates, Docker, Compose, GitHub Actions, IDEs, OWASP Top 10, Twelve-Factor config |

Any other language still works: the mentor finds its official docs live and tells you it is outside the curated map.

## Repository layout

```text
mentor-buddy/
  SKILL.md                      core instructions, read when the skill starts
  references/
    interview.md                phases 0 and 1: interview, project, memory creation
    phases.md                   phases 2 to 11, read one section at a time
    teaching-loop.md            review formats, error ladder, library choice
    folder-roles.md             folder roles and organization trade-offs
    project-archetypes.md       project catalog, scope by level, scope cutting
    session-rituals.md          resume questions and end-of-day summary
    memory-template.md          STUDY-MEMORY.md template
    tone.md                     direct and banter tones, English corrections
    docs-*.md                   official documentation entry points per stack
  README.md
  README.pt-BR.md
  LICENSE
```

The repository root is the skill folder, so installing is a `git clone` and updating is a `git pull`.

## FAQ

**Does it ever write code for me?**
Only in two moments. On your second miss on a step, it shows a short example of the right approach in a different context, deliberately not ready to paste. On your third miss, it fixes your file with a `MENTOR:` comment on each change and asks you to explain the fix back. Everything else you type yourself.

**Which model should I use?**
The skill works with whatever model your agent runs. Stronger models follow the ladder and the memory rules more consistently.

**Does it need internet access?**
To confirm versions, commands and prices against the official docs, yes. Without it, the mentor tells you it cannot verify and gives you the link to check yourself.

**Does it cost anything?**
The skill is free. You need your agent's own plan, and the deploy phase uses free tiers, checked on each provider's official pricing page during the session.

**Can I use it in Portuguese?**
Yes. Choose Portuguese in the first message; the whole mentoring happens in Portuguese, with code in English.

**Can I use it at work?**
Use it on your own study projects. Do not paste your employer's code or data into an AI agent without permission.

**What if my language is not in the curated map?**
It still works. The mentor researches the official docs live and tells you the language is outside the curated map.

## Privacy

`STUDY-MEMORY.md` goes into your project's git by default and lists the topics where you missed. If your repository is public and you would rather keep that private, add the file to `.gitignore`. The skill itself sends nothing anywhere: it is plain-text instructions read by your agent.

## Feedback and contributing

Ideas, bugs and questions are welcome in [Issues](https://github.com/mauricioreiss/mentor-buddy/issues). Pull requests are reviewed at the maintainer's discretion, so open an issue first to discuss the change.

## License

[MIT](LICENSE). Created by [Mauricio Reis](https://github.com/mauricioreiss).
