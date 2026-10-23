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

One A4 page, landscape, in the conversation's language.

1. **Header image**, full width at the top: `assets/certificate-header-pt.png` or `assets/certificate-header-en.png` from this skill's folder. It carries the title, so do not repeat the title as text.
2. "Certificamos que" / "This certifies that", then the **name**, large and bold.
3. "construiu do zero e colocou no ar o projeto" / "built from scratch and shipped the project", then the **project name** and the one-line problem from the brief.
4. A small two-column table: Stack; Nível / Level; Período / Period (first to last session date); Sessões / Sessions (counted from the session log); No ar em / Live at (the live address, as a link).
5. "Trilha completa: 12 de 12 paradas" / "Full trail: 12 of 12 stops", then the twelve phase names on one line, separated by " · ".
6. Signature block: "Mentor Buddy" and the issue date.
7. Footer in small grey type: "Certificado de conclusão de projeto emitido pela skill Mentor Buddy (github.com/mauricioreiss/mentor-buddy). Não é uma certificação oficial." / "Project-completion certificate issued by the Mentor Buddy skill (github.com/mauricioreiss/mentor-buddy). It is not an official certification."

Typography: a serif such as Georgia for the name and the project, a sans such as Calibri or Arial for the rest. Do not depend on a handwritten font being installed; the handwriting lives in the header image.

File name: `certificado-<project>-<YYYY-MM-DD>.docx` (`certificate-...` in English), in the learner's project folder. If they use git, add it to `.gitignore`: it carries their name, and publishing it is their call. Tell them it is theirs to print or share.

## How to assemble it

1. Run the three checks; ask for the name only once they pass.
2. Read the brief, the phase plan, the decisions (for the live address) and the session log from the memory.
3. Invoke the `docx` skill with the layout above, embedding the header image from this skill's `assets/` folder.
4. Add one line to the session log: certificate issued, with the date and without the name.
5. Tell the learner where the file is in one line, in their tone.

Where this session cannot write files or cannot run the `docx` skill, say so, put the certificate text in chat, and point them to the header image so they can assemble it in Word or Google Docs. Do not hand over a half-built file.
