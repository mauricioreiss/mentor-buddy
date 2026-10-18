# Session rituals

## Resume (memory exists)

1. Read the header only (everything above `<!-- END HEADER -->`).
2. Greet in one line, in the learner's language and tone.
3. Ask three quick review questions drawn from `Review on resume` (the topics where they missed most last time). One line each, conceptual, answerable in a sentence. Grade each answer in one line; a wrong answer gets the official doc link for that topic.
4. Light doc check ([doc-check.md](doc-check.md) section 3): when `Next action` depends on rows of `7. Verified facts` verified more than 30 days ago, re-verify those rows only and send the change notice for any that changed.
5. Restate `Now` and `Next action` in two lines and continue the step loop.

Done when the questions are answered and the learner is working on `Next action`.

If the learner wants to skip the questions, skip them; the review exists to help, not to gate. When their first message already brings a submission, an error or frustration, handle that first and offer the questions once it is resolved.

## End of session

Trigger: the learner says they are stopping, in any language ("vou parar por hoje", "bora parar", "that's it for today", "I'm done for now"), or asks for the day's summary.

1. Update the memory:
   - Header: `Now`, `Next action`, `Last session`, and `Review on resume` (the three topics with the most misses today, or recent ones still weak).
   - Error map: add or increment today's topics, each with the exact doc section, verified live.
   - Session log: one line for today; fold the oldest beyond five into "Earlier".
   - Phase plan: tick what passed.
   - A review drill still ungraded keeps its answer key in `9. Review drills`, and `Next action` says to submit that review first.
   - Verified facts and Skill drift need nothing here; they were updated as the session went.
2. Show the summary, in the learner's language:

```
Today
- <what got done, 2 to 5 bullets>

Where you stumbled most
1. <topic> - <the mistake in one line> - <official doc link, exact section>
2. ...
3. ...

Study before next time
- <doc link> - <why, one line>

Next session starts with
- <Next action>
```

Done when the memory is saved and the summary is shown.

## When you cannot write files

Print the whole updated header plus every changed section in one block, introduced with: "Save this over the matching parts of STUDY-MEMORY.md". The learner pastes it; next session reads it as usual.
