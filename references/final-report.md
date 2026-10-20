# Final report (.docx)

At the end of the project (phase 11 Retro), and whenever the learner asks for it, build a study report as a Word document. It is the thing they keep: where they struggled, the fix, and what to study next. Use the `docx` skill to generate the file; this reference only says what goes in it.

Build it from the memory, not from scratch: the error map, the session log and the review-drill results already hold everything. Verify any doc link is still live before writing it in.

## What goes in

Language: the conversation's language. File name: `relatorio-<project>-<YYYY-MM-DD>.docx` (or `report-...` in English). Save it in the learner's project folder (and add it to `.gitignore` if they use git).

1. **Cover**: project name, the learner's level, dates (first to last session), how many sessions.
2. **What you built**: the brief's acceptance criteria, each marked delivered or not.
3. **Where you struggled most**: the top error-map topics by count. For each:
   - the topic and how many times it came up;
   - a **before / after** code pair taken from the actual sessions where it can be recovered, or a short neutral example in their language when it cannot (wrong snippet, then the corrected one, each labelled);
   - one line on why the wrong version is wrong;
   - the official doc section to read, with the link.
4. **Review training**: how the review drills went (found / missed / false alarms), and the review categories still weak.
5. **Study plan**: an ordered list of what to study next, each with the doc link and one line on why, drawn from the error map and the retro.
6. **Next project**: the suggestion from the retro, one level harder or a different archetype.

A placeholder line invites them to paste their own screenshots under any section where a screen capture would help ("cole aqui um print do erro, se quiser" / "paste a screenshot of the error here if you like"); the mentor cannot capture their screen, so it only embeds images the learner provides.

## How to assemble it

1. Read the whole memory (not just the header) to gather the error map, the session log and the drill results.
2. Recover before/after pairs from the session where each top topic was missed; where the snippet is gone, write a short neutral example in their language that shows the same mistake and its fix.
3. Verify each doc link live before including it.
4. Invoke the `docx` skill with the structure above and save the file in the project folder.
5. Tell the learner where the file is in one line.

Where this session cannot write files or cannot run the `docx` skill, produce the same report as Markdown in chat and tell them to save it, so nothing is lost.
