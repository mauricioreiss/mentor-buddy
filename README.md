# Mentor Amigo

[Português](#português) | [English](#english)

---

## Português

Uma skill para agentes de IA que transforma o agente num **mentor que não escreve o seu código**. Você escolhe a linguagem, ele entende o seu nível (júnior, pleno ou sênior), monta um projeto com você e te guia passo a passo, da organização das pastas na IDE até testes, Docker, CI e deploy gratuito. Quem digita é você.

Feita para quem quer aprender programação com IA **na prática**, com a mão no teclado, em vez de colar código pronto.

### Como funciona

- **Entrevista curta**: idioma (português ou inglês), tempo de programação, linguagem, ideia de projeto, tempo disponível, IDE e o jeito que você quer ser tratado (direto ou na zoeira).
- **Projeto real**: o mentor sugere três ideias com base no que você curte, ou corta a sua ideia até um tamanho que dá para levar até o deploy.
- **Trilha completa**: ambiente, pastas, esqueleto andando, funcionalidades com teste, banco, qualidade, Docker, CI, deploy e retrospectiva.
- **Escada de erros**: o mentor explica o que fazer e por quê, com o link da documentação oficial. Se você errar, ele revisa. No segundo erro, mostra um exemplo em outro contexto. Só no terceiro erro ele mexe no seu arquivo, com comentários explicando cada mudança.
- **Sem achismo**: versão, comando, API e preço são sempre conferidos na documentação oficial na hora. Sem acesso à web, ele avisa e te passa o link em vez de chutar.
- **Memória**: um arquivo `STUDY-MEMORY.md` na raiz do projeto guarda onde você parou, as decisões e onde você mais erra. Na próxima sessão ele faz umas perguntas rápidas de revisão e continua de onde parou. Ao encerrar o dia, mostra um resumo com os pontos para estudar e os links.

### Onde funciona

Qualquer agente que leia o padrão aberto de skills ([agentskills.io](https://agentskills.io/specification)):

| Agente | Pasta pessoal lida |
|---|---|
| Claude Code (terminal, VS Code, JetBrains) | `~/.claude/skills/` |
| GitHub Copilot no Visual Studio 2026 (18.5+, agent mode) | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` |
| GitHub Copilot no VS Code | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` |
| GitHub Copilot CLI | `~/.agents/skills/`, `~/.copilot/skills/` |
| OpenAI Codex | `~/.agents/skills/` |
| Gemini CLI | `~/.agents/skills/`, `~/.gemini/skills/` |
| Cursor | `~/.agents/skills/`, `~/.cursor/skills/`, `~/.claude/skills/` |

Nenhuma pasta é lida por todos. Por isso a instalação abaixo deixa a cópia real em `~/.agents/skills/` e cria um link em `~/.claude/skills/`.

### Instalação

Windows (PowerShell):

```powershell
git clone https://github.com/mauricioreiss/mentor-amigo.git "$HOME\.agents\skills\mentor-amigo"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\mentor-amigo" -Target "$HOME\.agents\skills\mentor-amigo"
```

macOS e Linux:

```bash
git clone https://github.com/mauricioreiss/mentor-amigo.git ~/.agents/skills/mentor-amigo
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/mentor-amigo ~/.claude/skills/mentor-amigo
```

Se o link não funcionar no seu sistema, copie a pasta para `~/.claude/skills/mentor-amigo` em vez de criar o link.

Atualizar: `git -C ~/.agents/skills/mentor-amigo pull`

### Como usar

1. Abra uma pasta vazia na sua IDE (ou a pasta de um projeto que você já começou com o mentor).
2. No chat do agente, diga algo como "quero estudar com o mentor amigo" ou "me ensina C# fazendo um projeto". No Claude Code, no Copilot e no Cursor também dá para digitar `/mentor-amigo`.
3. Responda a entrevista e comece a digitar.

Para encerrar o dia, diga "vou parar por hoje".

### Privacidade

O `STUDY-MEMORY.md` entra no git do seu projeto por padrão e mostra os pontos onde você errou. Se o seu repositório for público e você preferir guardar isso para você, coloque o arquivo no `.gitignore`. Use a skill nos seus projetos de estudo; não cole código nem dados da sua empresa num agente de IA sem autorização.

### Feedback

Sugestões e problemas pelas [Issues](https://github.com/mauricioreiss/mentor-amigo/issues).

### Licença

[MIT](LICENSE).

---

## English

A skill for AI agents that turns the agent into a **mentor that does not write your code**. You pick the language, it figures out your level (junior, mid or senior), plans a project with you, and guides you step by step from the folder structure in your IDE to tests, Docker, CI and a free deploy. You do the typing.

Built for people who want to learn programming with AI **hands-on**, keyboard under their own fingers, instead of pasting generated code.

### How it works

- **Short interview**: language (Portuguese or English), experience, programming language, project idea, available time, IDE, and how you want to be talked to (direct or banter).
- **A real project**: the mentor offers three ideas based on what you enjoy, or cuts your own idea down to something you can take all the way to deploy.
- **The full path**: environment, folders, walking skeleton, features with tests, database, quality, Docker, CI, deploy and a retrospective.
- **Error ladder**: the mentor explains what to build and why, with the official doc link. When you miss, it reviews. On the second miss it shows an example in a different context. Only on the third miss does it edit your file, with comments explaining each change.
- **No guessing**: versions, commands, APIs and prices are always checked in the official documentation during the session. Without web access, it says so and gives you the link instead of guessing.
- **Memory**: a `STUDY-MEMORY.md` file at the project root keeps where you stopped, your decisions and where you miss most. Next session starts with a few quick review questions and picks up where you left off. When you stop for the day, you get a summary with what to study and the links.

### Where it works

Any agent that reads the open skill format ([agentskills.io](https://agentskills.io/specification)). See the table in the Portuguese section above: no single folder is read by every agent, so the install keeps the real copy in `~/.agents/skills/` and links it from `~/.claude/skills/`.

### Install

Windows (PowerShell):

```powershell
git clone https://github.com/mauricioreiss/mentor-amigo.git "$HOME\.agents\skills\mentor-amigo"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\mentor-amigo" -Target "$HOME\.agents\skills\mentor-amigo"
```

macOS and Linux:

```bash
git clone https://github.com/mauricioreiss/mentor-amigo.git ~/.agents/skills/mentor-amigo
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/mentor-amigo ~/.claude/skills/mentor-amigo
```

If the link does not work on your system, copy the folder to `~/.claude/skills/mentor-amigo` instead.

Update: `git -C ~/.agents/skills/mentor-amigo pull`

### Usage

1. Open an empty folder in your IDE (or the folder of a project you already started with the mentor).
2. In the agent chat, say something like "I want to study with mentor amigo" or "teach me Go by building a project". In Claude Code, Copilot and Cursor you can also type `/mentor-amigo`.
3. Answer the interview and start typing.

To stop for the day, say "that's it for today".

### Privacy

`STUDY-MEMORY.md` goes into your project's git by default and lists where you missed. If your repository is public and you would rather keep that private, add the file to `.gitignore`. Use the skill on your study projects; do not paste your employer's code or data into an AI agent without permission.

### Feedback

Ideas and problems go to [Issues](https://github.com/mauricioreiss/mentor-amigo/issues).

### License

[MIT](LICENSE).
