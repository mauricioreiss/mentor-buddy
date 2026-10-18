# STUDY-MEMORY.md template

Copy the block below into `STUDY-MEMORY.md` at the repository root and fill it in. Rules that keep it cheap to read:

- Everything a session needs to restart sits above `<!-- END HEADER -->`, in under 40 lines. Sessions read only that part, then open one section when a step needs it.
- Only the current phase is expanded into steps. Future phases stay one line each until they start.
- The session log keeps the last five sessions; fold older ones into one line each under "Earlier".
- The error map is the learner's study guide: one row per topic, counted, with the exact doc section.

```markdown
# STUDY-MEMORY - <project name>
<!-- Maintained by the mentor-buddy skill. Read the header every session; open sections only when needed. -->

## Header
- Conversation language: <pt | en>
- English corrections: <on | off | n/a>
- Tone: <direct | banter>
- Level: <junior | mid | senior> (set <YYYY-MM-DD>; last recalibration: <date and reason, or none>)
- Stack: <language and runtime>, <framework or none yet>, IDE <name>, OS <name>
- Project: <archetype> - <one-line pitch>
- Now: Phase <n> <name> / Step <n.m> <title> / Attempt <0-3>
- Next action: <exactly what the learner does next>
- Last session: <YYYY-MM-DD> - <one line>
- Review on resume: <topic 1>; <topic 2>; <topic 3>

## Index
1. Brief
2. Phase plan
3. Decisions
4. Error map
5. Session log
6. Open questions
<!-- END HEADER -->

## 1. Brief
Problem: ...
Users: ...
Acceptance criteria:
1. ...
Out of scope / Later: ...

## 2. Phase plan
- [x] 0 Interview
- [x] 1 Project
- [ ] 2 Environment
  - [ ] 2.1 <step> - done when <check>
  - [ ] 2.2 ...
- [ ] 3 Folder structure
- [ ] 4 Walking skeleton
- [ ] 5 Feature slices
- [ ] 6 Persistence
- [ ] 7 Quality
- [ ] 8 Docker
- [ ] 9 CI
- [ ] 10 Deploy
- [ ] 11 Retro

## 3. Decisions
| Date | Decision | Why | Doc |
|---|---|---|---|

## 4. Error map
| Topic | Misses | Last seen | Doc (exact section) |
|---|---|---|---|

## 5. Session log
- <YYYY-MM-DD>: <done>; <where they stumbled>
Earlier: <one line per older session>

## 6. Open questions
- ...
```
