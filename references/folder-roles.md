# Folder roles

The phase-3 reference. Roles are stable across languages; names and layout conventions differ by ecosystem, so check the language's doc map and the official template before naming anything.

## Pick the organization with the learner

Structure should be proportional to the problem. Present the trade-off; a junior gets a recommendation, a mid or senior chooses and justifies.

| Organization | Fits | Cost |
|---|---|---|
| **By feature** (vertical slice): each feature folder holds its endpoint or command, input and output models, validation and data access | Many independent features with light rules, CRUD-heavy apps | Needs discipline so real business rules are shared instead of copied between features |
| **By layer** (clean / hexagonal): domain, application, infrastructure, presentation; dependencies point inward to the domain | Heavy business rules that must be tested without database or HTTP | More files and mapping between layers |
| **Hybrid**: feature folders on top of a shared domain | Medium projects that grow | Two conventions to keep clear |

## Roles

The third column is for juniors only. A mid or senior gets the role and names the folder.

| Role | What lives there | Example names (junior) |
|---|---|---|
| Entry point | Startup, dependency wiring, configuration loading | `Program`, `main`, `app` |
| Presentation | Routes, controllers or handlers, request and response models. Translates HTTP or CLI input into calls; holds no business rules | `Controllers`, `Endpoints`, `handlers`, `routes` |
| Application | Use cases: one action each, orchestrating validation, domain calls and persistence | `Services`, `UseCases`, `Features/<Feature>` |
| Domain | Entities, value objects, business rules. Knows nothing about the database or HTTP | `Domain`, `Entities`, `model` |
| Infrastructure | Database access, repositories, migrations, clients for external APIs | `Infrastructure`, `Data`, `Persistence` |
| Configuration | Settings files and environment variable mapping | `config`, `appsettings` |
| Tests | Unit tests near the code or in a test project; integration tests with real dependencies | `tests`, `<Project>.Tests`, `test` |
| Ops | Dockerfile, compose file, CI workflow | repository root, `.github/workflows` |
| Docs | README, decision notes | `docs` |

A catch-all folder (`utils`, `helpers`, `misc`) usually means a role was not found yet; ask which role the code really plays.

## Sketches by archetype

Roles only; names come from the ecosystem.

REST API, by feature:
```
<repo root>
  <source root>
    <feature A>/   presentation + application + data access for A
    <feature B>/
    <shared domain>/   rules used by more than one feature
    <entry point>
  <tests>
  Dockerfile, compose file, CI workflow, README
```

REST API, by layer:
```
<repo root>
  <domain>          entities, rules
  <application>     use cases
  <infrastructure>  database, external clients
  <presentation>    HTTP endpoints, entry point
  <tests>
  Dockerfile, compose file, CI workflow, README
```

CLI tool: entry point, command parsing (presentation), core logic (application and domain), storage (infrastructure), tests.

Background worker: entry point, message consumer (presentation), handlers (application), domain, broker and database clients (infrastructure), tests.

Full-stack web app: the API as above, plus a separate frontend folder with its own conventions, verified live in its framework's docs.

## Ecosystem conventions to verify live

- .NET: solution with one project per layer, or one project with feature folders; the official templates set the starting layout.
- Go: the official "Organizing a Go module" guide.
- Python: package layout per the Python Packaging User Guide; framework docs for app structure.
- Java: the Maven or Gradle standard directory layout; Spring Boot docs for packages.
- TypeScript and Node: framework conventions (no single official layout); confirm in the chosen framework's docs.
