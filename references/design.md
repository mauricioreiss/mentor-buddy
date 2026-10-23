# Project and design (phase 1)

Before any code, the learner understands the problem, the domain and the technical shape of the project, and makes the decisions. It is also their first contact with domain-driven design (DDD) and Clean Architecture, used at the size of their project instead of taught as theory.

Pace: one topic per message, in plain words, short. You bring knowledge and options; the learner decides. Record each decision the moment it is made (section 3 of the memory), so a later session resumes mid-phase. When the learner wants to start coding sooner, compress: a short 1.1, the data store decision and the brief are the minimum.

## 1.1 Understand the domain

The learner describes the idea in their own words ("uma fila de pacientes pro meu trabalho"). Reply with what a system like that usually involves, as a short plain-language list, then ask how it works in their case and adjust:

- **who** uses it (actors);
- the **main flow**, from start to end, and the states something goes through;
- the **rules** that decide what happens;
- the **edge cases** that real use runs into.

Example, a patient queue: reception, triage, the doctor and the patient; arrival, check-in, triage with a priority, waiting, called, seen or gave up; risk priority comes before arrival order, a call can be repeated, a patient is never in the queue twice; what happens when two doctors call at once.

Use the words the learner uses for things; they become the project's vocabulary. When the data is regulated (health, finance, children, biometrics), say so in one line with the official source, verified live (in Brazil, the LGPD treats health data as sensitive).

## 1.2 Model the domain (DDD, at their size)

From the conversation, name with the learner:

| Level | What you model together |
|---|---|
| Junior | A glossary of 5 to 10 terms; the entities (things with identity that change over time: `Patient`, `Visit`); the rules that must always hold ("a patient is never in the queue twice") |
| Mid | The above, plus value objects (values without identity: `Priority`, `ArrivalTime`) and aggregates (what must change together in one consistent step) |
| Senior | The above, plus bounded contexts when the domain has more than one model of the same word (reception versus clinical), and how they talk |

The learner names things; you check that each name says what it is in the domain. Code stays in English, so agree on the English term for each word in the glossary.

## 1.3 See the architecture (Clean Architecture, at their size)

Explain the dependency rule in two lines: the domain is at the centre and knows nothing about the database or HTTP; use cases orchestrate one action each; infrastructure (database, external APIs, framework) plugs in from the outside. Then place their model on it: where `Patient` lives, where "call the next patient" lives, where the database sits.

Keep it proportional. A small CRUD does not need layers, and saying so is part of the lesson. The folder organization itself is chosen in phase 3 ([folder-roles.md](folder-roles.md)); here the learner only sees the shape.

## 1.4 Make the technical decisions

One decision per message. Teach the criterion, then let them decide: a junior gets one recommendation with the why; a mid or senior decides and justifies, and you validate it or name the mismatch.

- **Data store.** Ask about the use case: do the things reference each other (a visit belongs to a patient)? Does a change need to be all-or-nothing? Do they need queries across them? Then it is relational, and the default is PostgreSQL (SQLite for a CLI or a single-user tool). When the data is documents of varying shape read whole, with no relations, or simple key-value, a non-relational store fits. Versions and free tiers are checked live in phase 6 and 10, not now.
- **Libraries.** Ask which ones they already know. For each need the project has (web framework, data access, validation, tests), name the category and what to look for: actively maintained, clear license, official docs, real adoption. A junior gets one mainstream option per need, verified live.
- **External APIs.** Does the project call any service (payments, maps, messaging, an AI model)? For each: what it is for, how it authenticates, whether it has a sandbox or test mode, its limits and price (verified live), and what the app does when it fails. Keys always come from the environment.
- **Authentication.** Needed now, or "Later"? For a first project it is often Later.
- **Where it will run.** Only the kind: a web service, a static site, a CLI release. The provider is chosen in phase 10.

On the AI track the decisions also cover the provider, the tools the agent may use and how success is measured; see [ai-track.md](ai-track.md).

Each decision goes into section 3 of the memory as one row: date, decision, why, doc. Phase 6 implements the data store chosen here instead of choosing again.

## 1.5 The brief

Write the brief from the conversation and ask for approval:

```
Project: <name>
Problem: <two lines>
Users: <who uses it>
Acceptance criteria:
1. <testable behaviour>
2. ...
(3 to 6 items)
Out of scope / Later: <items>
Archetype: <from project-archetypes.md>
```

Below it, in section 1 of the memory, keep the design: the glossary, the entities with their rules, and the main flow, a few lines each. The brief is a product decision, so it belongs to the learner: adjust it until they approve. A large idea still gets cut to the smallest version that crosses every phase up to the deploy within their time, following the scope cut in [project-archetypes.md](project-archetypes.md); the rest goes to "Later".

Offer once, without insisting: writing `docs/design.md` in their own words (glossary, entities and rules, flow, decisions), reviewed like code. It is what a real project keeps and it shows well in a portfolio. Skip it when they would rather start coding.

Done when the domain and the model are agreed, the decisions are recorded and the brief is approved.
