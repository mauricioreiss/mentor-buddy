# Completion certificate (.docx)

The certificate is the learner's proof that a real project reached production with them at the keyboard. Issue it only when that is true. It is a project-completion certificate from this skill, not an official certification, and it says so.

## When to issue it

At phase 11 Retro, once the retro is written and reviewed, check all three:

1. **The app is live.** Open the live address recorded in Decisions during phase 10 (for a CLI, the published artifact). A free-tier app may be asleep: when the first request times out or fails, try once more. Without web access, or when it still does not answer, ask the learner to open it and tell you what they see; issue only once it works.
2. **Every acceptance criterion in the brief is delivered.**
3. **The retro is written.**

When one fails, there is no certificate yet: name what is missing in one line and say the certificate comes as soon as it is done. Never issue it for an unfinished project, even when the learner asks for it "just to have it": it is worth something because it means the project shipped. The study report ([final-report.md](final-report.md)) does not wait for this; offer it either way.

On the cybersecurity track the bar is CS7: the writeup reviewed and passed. The certificate then lists the CS phases instead of the twelve stops, and the live-address check does not apply.

## The name

Ask one question when the checks pass: "Qual nome vai no certificado?" / "What name goes on the certificate?". Use it exactly as typed. It goes into the .docx and nowhere else: not in STUDY-MEMORY.md, not in the session log. If they would rather not give one, leave the name line blank so they can type it in Word.

## What goes in

The layout is fixed in `scripts/make_certificate.py`, so every certificate looks the same whatever agent builds it: one A4 landscape page with the header drawing from `assets/`, the name and the project centred, four highlights (language, level, duration, sessions), what was built next to the live address and the full trail, the Mentor Buddy signature, and the disclaimer in the page footer. You only gather the data, from the memory and the conversation:

| Field | Where it comes from |
|---|---|
| `language` | the conversation language: `pt` or `en` |
| `name` | the learner's answer, exactly as typed (`""` leaves the line blank) |
| `project`, `problem` | the brief: the project name and its one-line problem |
| `programming_language` | the header's Stack, the language only (`C#`, `Python`, `Go`) |
| `stack_detail` | the rest of the Stack: framework and version |
| `level` | the header's Level, in the conversation language (`Júnior`, `Pleno`, `Sênior` / `Junior`, `Mid`, `Senior`) |
| `first_session` | the oldest date in the session log |
| `issued_on` | today |
| `sessions` | the number of entries in the session log |
| `built` | the acceptance criteria as delivered, rewritten as up to six short lines in plain words |
| `live_url` | the live address in Decisions (left out on the cybersecurity track) |
| `stops` | only on the cybersecurity track: the CS phase names |

The script works out the duration itself, from the first session to today counting both days, so do not compute it.

File name: `certificado-<project>-<YYYY-MM-DD>.docx` (`certificate-...` in English), in the learner's project folder. If they use git, add it to `.gitignore`: it carries their name, and publishing it is their call. Tell them it is theirs to print or share.

## How to assemble it

1. Run the three checks; ask for the name only once they pass.
2. Read the brief, the header, the decisions and the session log from the memory, and fill the fields above.
3. Write them as UTF-8 JSON to `certificate-data.json` in the project folder, then run this skill's script with whatever Python 3 the machine has (`python`, `python3` or `py -3`):
   `python <skill folder>/scripts/make_certificate.py --data certificate-data.json --out certificado-<project>-<YYYY-MM-DD>.docx`
   Pass the data as a file, never through a pipe: on Windows, PowerShell pipes text as ASCII and the accents in the name would be lost.
4. Delete `certificate-data.json` right away: it holds the learner's name.
5. Add one line to the session log: certificate issued, with the date and without the name.
6. Tell the learner where the file is in one line, in their tone.

When the script stops with a message about the data, fix that field and run it again. Where the machine has no Python, build the same page with the `docx` skill, embedding `assets/certificate-header-<pt|en>.png`. Where this session cannot write files at all, say so, put the certificate text in chat and point them to the header image. Do not hand over a half-built file.
