# Code review: the checklist and how to train it

A developer who can write code but cannot review it will merge whatever an AI tool hands them. This file is the review method the mentor uses on every submission and teaches the learner to use on any code: their own, a colleague's or an AI's.

Contents: 1. The checklist · 2. Signs of AI-written code · 3. Guided review at miss 3 · 4. Review drills · 5. The learner's review format

## 1. The checklist

Follow it in this order. Keep each review short: name only the items that apply.

1. **Intent**: what was this supposed to do? Read the step's `Done when` or the acceptance criterion before reading the code.
2. **Run it**: the build and the tests, actually run (the driver runs them). A review that only reads is a guess.
3. **Tests**: do they check behaviour, and would they fail if the code were wrong? A test that cannot fail proves nothing.
4. **Trace**: follow one normal input and one edge input through the code by hand.
5. **Edge cases**: empty, null, whitespace, boundaries (0, 1, the maximum), duplicates, concurrency, malicious input. Check that the value that gets stored is the value that was validated: normalize first (trim, case), validate that, store that. Validating the raw `"  ab  "` (6 characters) and storing the trimmed `"ab"` (2) slips past a 3-character minimum.
6. **Security**: input validated at the boundary, queries parameterized, no secrets in code or logs, error responses that do not leak internals.
7. **Complexity**: when it matters, the Big O and why.
8. **Design**: one responsibility per unit, the right folder for the role, coupling.
9. **Naming and readability**: names reveal intent; comments explain why, not what.
10. **Modern idiom**: when the current official docs show a built-in or newer syntax that replaces what was hand-written, name it with the doc link and why seniors prefer it (fewer branches, intent visible). The learner rewrites it themselves.
11. **Verdict**: approve, or request changes with the reason for each.

## 2. Signs of AI-written code

Code from an AI tool, including your own fix at miss 3, gets these extra checks:

- An API, flag or config key that does not exist, or no longer does: confirm it on the official page.
- Outdated syntax or a deprecated API where the current docs show a replacement.
- Edge handling that looks right and is not: the trim gap above, an off-by-one, a null check placed after the value was already used.
- Errors swallowed by a catch-all, or logged and ignored.
- Tests that mirror the implementation or assert nothing.
- Abstraction for a single use, or code the task never asked for.
- Names and patterns that ignore the conventions already in the codebase.
- Hard-coded configuration or secrets.

## 3. Guided review at miss 3

After you fix their file ([teaching-loop.md](teaching-loop.md) section 6), the learner reviews your fix as if an AI tool had written it, because that is the review they will do at work. Ask three questions about this specific fix, one line each:

1. Which change fixes which failing check? Point to the line.
2. Which test proves it, and would that test fail without the change?
3. What else could break here: an edge case the fix still misses, or why there is none?

Grade each answer in one line. A wrong answer gets the explanation and the question again; it is not a new miss. The step passes when the tests pass and the three answers hold. Then they delete the `MENTOR:` comments, before committing.

## 4. Review drills

**When**: after each feature slice passes in phase 5, and one larger drill in phase 7 on that phase's topics. Offer it in one line; when the learner skips, note it in the session log and move on.

**Build the drill**:
- A short file, 15 to 40 lines (up to 80 in phase 7), in the learner's language and their project's domain, that looks like plausible AI output: it compiles, reads well and carries a test or two.
- Planted defects by level: junior 2, each with a category hint ("one is about input validation"); mid 3, no hints; senior 3 subtle ones (concurrency, security, performance, failure modes), no hints.
- At least one defect comes from their error map, so the drill presses on a known weak spot.
- No defect a compiler or linter would catch; real review finds what builds.
- The drill covers a feature already done or one outside the brief, never a step still ahead, so it cannot become a shortcut.

**Where**: save it as `.review-drills/<nn>-<topic>.<ext>` at the project root. The leading dot keeps it out of builds and test runs (Go, for one, skips folders starting with a dot). The first time, if the project uses git, the learner adds `.review-drills/` to `.gitignore` themselves. Where you cannot write files, show it in chat.

**Answer key**: write it in section `9. Review drills` of the memory before showing the drill, so grading survives the end of a session. Do not reveal it until they submit.

**Grading**: compare their findings with the key: found, missed, false alarms. Then show the key, one line per defect (line, problem, why, fix in words, doc link). Each missed category adds or increments an error-map row named `Review: <category>`. A drill is never a miss on the ladder.

## 5. The learner's review format

Teach it at the first drill; it is how a pull request comment reads:

```
Line <n>: <problem> - <why it matters> - <fix, in words>
Verdict: approve | request changes
```
