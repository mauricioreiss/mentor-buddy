# Project archetypes

Archetypes guarantee the project crosses every phase, from folders to deploy, at a size the learner can finish. The theme comes from what the learner enjoys; the archetype stays.

## Catalog

| Archetype | Practices | Levels | Persistence | Deploy shape |
|---|---|---|---|---|
| REST API with a database | HTTP, validation, data access, tests | junior to senior | yes | container web service |
| CLI tool | argument parsing, file I/O, error handling, packaging | junior | file or embedded database | published release artifact |
| Frontend app (SPA or static site) | components, state, forms, the four states, accessibility, design tokens | junior to senior | optional (a public API or none) | static site |
| Full-stack web app | API plus a simple frontend, CORS, forms | mid to senior | yes | web service plus static site |
| Background worker with a queue | async processing, retries, idempotency | mid to senior | yes | container worker plus a queue |
| Integration service | consuming a public API, webhooks, resilience, caching | mid to senior | optional | container web service |
| Real-time app | WebSockets, broadcast, connection state | senior | optional | container web service |

A learner who wants offensive security, ethical hacking or CTF practice instead of building an app does not use this catalog: route them to the cybersecurity track in [cybersec-track.md](cybersec-track.md), which has its own journey and lab-safety gate.

## Scope by level (REST API example; scale the others the same way)

- **Junior**: one or two resources, full create-read-update-delete, one real business rule, input validation, unit tests.
- **Mid**: related resources, pagination and filtering, integration tests against a real database, structured logs.
- **Senior**: authentication with tokens verified server-side, idempotent writes, concurrency control, observability, rate limiting.

## Themes by interest

| Interest | Ideas |
|---|---|
| Sports | league table, workout tracker, match scheduler |
| Finance | expense splitter, monthly budget, subscription tracker |
| Games | inventory, leaderboard, tournament bracket |
| Music | playlist manager, practice log |
| Books and films | watchlist, reading tracker with reviews |
| Pets | vet appointments, feeding schedule |
| Study | flashcards with spaced repetition, study planner |

## Offering three options

For each option give: name, one-line pitch, archetype, what they will practice, rough size in sessions given their available time. Vary the archetypes when the level allows, so the choice is real.

## Cutting the learner's own idea

1. Find the core action: the one thing a user does that gives the app its point.
2. Keep only what that action needs to work end to end.
3. Map it to the closest archetype so every phase applies.
4. Size it to the learner's time: the walking skeleton should run within the first sessions after setup.
5. Everything else goes to "Later" in the brief, with a word that it can come back after the deploy.

Example: "an Uber clone with an app, payments and maps" for a junior becomes "a ride request API: register drivers, request a ride, match the nearest available driver by simple distance, finish the ride". Payments, maps and the mobile app go to Later.
