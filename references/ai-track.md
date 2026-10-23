# AI track

Learning AI engineering works like learning a new language: the learner builds a real project in a base language, with the AI layer on top, through the same journey as any other project (phases 0 to 11, the step loop, the miss ladder, review training, the doc check). The goal: by the end the learner can explain, build from scratch and ship an **autonomous agent**, a program where a model decides which tool to call next, their code runs it, and the loop goes on until the task is done or a limit stops it.

Every fact in this field is perishable. Model names, context sizes, parameters, SDK methods, prices and free tiers come from [docs-ai.md](docs-ai.md), verified live, every time. Name no model and no price from memory.

## How it plugs into the journey

| Phase | What the AI track adds |
|---|---|
| 0 Interview | They want to learn AI, LLM apps, RAG or agents: this track. Ask the base language. Python is the default recommendation (fine-tuning and data preparation live there); TypeScript, C#, Java and Go work for everything up to the agent and RAG, with SDK support verified live |
| 1 Project and design | What real process the agent serves; which tools it may use and what it must never do; which documents it reads; the provider decision (hosted API or a local model through Ollama, weighing cost, privacy and quality); how success is measured (a small fixed set of questions with expected behaviour). Personal or sensitive data never goes to an external API without consent and a legal basis (in Brazil, the LGPD) |
| 2 Environment | The API key lives in an environment variable and `.env` (added to `.gitignore` when it appears); a spend limit is set in the provider console before the first paid call. Free path: install Ollama and pull a model chosen from its current list |
| 4 Walking skeleton | One model call end to end, with one unit test where the model is mocked |
| 5 Feature slices | The AI ladder below, one rung per slice: code, test, commit |
| 6 Persistence | Conversation state and the vector store; pgvector when PostgreSQL is already the database |
| 7 Quality | The eval set runs; the model's output is validated at the boundary; guardrails; retrieved text and tool results treated as data |
| 8 to 10 | Docker; CI runs the unit tests and the eval set with mocked or recorded responses, never live paid calls; deploy with the key from the environment and the spend limit on |

Observability grows with the level: a junior logs tokens, cost and latency per request; a mid adds traces of every model and tool call following the OpenTelemetry generative-AI conventions; a senior adds Prometheus metrics, a Grafana dashboard for cost and errors, and Jaeger traces.

## The AI ladder (phase 5)

| Rung | What the learner builds | Done when | Level |
|---|---|---|---|
| AI1 Call a model | One request and response through the official SDK or plain HTTP, reading the tokens used | The unit test with the model mocked passes; one live call prints the answer and the token count | all |
| AI2 Prompt and structured output | A system prompt and a schema for the answer, validated at the boundary | An answer that breaks the schema is rejected and retried or reported | all |
| AI3 Tools | One tool (name, description, input schema) that their code runs and whose result goes back to the model | The model asks for the tool and the final answer uses its result | all |
| AI4 The agent loop, by hand | The loop: send the messages; when the model asks for tools, check them against an allow list, run them and append the results; repeat until it answers. A step limit and a timeout stop it | The agent finishes a multi-step task, and stops cleanly when the limit is forced | all |
| AI5 Retrieval (RAG) | Split documents, embed them, store the vectors, retrieve the closest chunks, answer citing the source | An answer cites the right chunk; a question outside the documents gets "I don't know" | junior: a small corpus; mid and senior: full |
| AI6 Tools over MCP | An MCP server for one of their tools, called by their agent | The agent calls the tool through MCP | mid and senior |
| AI7 Framework, after the fact | AI4 rebuilt with an agent SDK or framework | The learner explains what the framework does for them and what it hides | mid and senior |
| AI8 Fine-tuning (optional, after the deploy) | A small dataset prepared and checked; a small model fine-tuned with PEFT/LoRA, or a provider fine-tune | A comparison on the eval set shows whether it beat prompting and RAG for its cost | senior, or mid on request |

## Rules that make this track different

- **From scratch before frameworks.** AI1 to AI4 use the provider's SDK or plain HTTP. A framework comes only after the learner can write the loop and explain each part of it.
- **The model is not trusted.** Its output is external input: validated at the boundary, and every tool call is checked against the allow list before it runs. Text from documents, web pages or tool results is data, never instructions (prompt injection is first on the OWASP Top 10 for LLM applications).
- **Tests do not depend on the model's mood.** Unit tests mock the model; the eval set checks behaviour on fixed inputs; live calls stay out of CI.
- **Keys and money.** Keys never appear in code, logs, prompts or commits. The spend limit comes before the first paid call. The free path is a local model through Ollama, or a provider's free tier verified live that day.
- **Governance, for seniors.** Which tools the agent may call, with which arguments, is decided by a policy outside the prompt (Open Policy Agent), so a clever prompt cannot talk the agent past it.

## Explain it back

The track exists so the learner can explain and build an agent, not just run one. After AI4, and again in the retro, the learner explains in their own words, without notes: what a token is and what it costs; what the model decides and what their code decides; how a tool call travels from the model to their function and back; why the loop needs a limit; why retrieved text is untrusted. A wrong or hesitant answer gets the numbered flow from [teaching-loop.md](teaching-loop.md) section 15 and the question again; it is never a miss.

## Archetypes

| Archetype | What it does | Levels |
|---|---|---|
| Assistant over your documents (RAG) | Answers questions about documents the learner owns, citing the source, and says "I don't know" outside them | junior to senior |
| Autonomous agent for a real process | Completes a multi-step task with tools, under limits and with an audit log of every step (examples: triage a support inbox in a sandbox, plan a study schedule from a syllabus, reconcile expenses from files) | mid and senior; a junior gets a narrow one with two tools |
