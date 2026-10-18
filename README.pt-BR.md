# Mentor Buddy

**Uma skill para agentes de IA que transforma o seu assistente de código num mentor que não escreve o seu código.** Você digita cada linha. Ele te entrevista, monta um projeto de verdade com você e te guia passo a passo, da pasta vazia até a aplicação no ar.

![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-blue.svg)
![Formato: Agent Skills](https://img.shields.io/badge/formato-agentskills.io-black.svg)
![Conversa: EN | PT-BR](https://img.shields.io/badge/conversa-EN%20%7C%20PT--BR-informational.svg)

[Read in English](README.md)

---

## Sumário

- [Por que existe](#por-que-existe)
- [O que você ganha](#o-que-você-ganha)
- [Uma sessão, em resumo](#uma-sessão-em-resumo)
- [Como funciona](#como-funciona)
- [Agentes compatíveis](#agentes-compatíveis)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Mapa de documentação curado](#mapa-de-documentação-curado)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Perguntas frequentes](#perguntas-frequentes)
- [Privacidade](#privacidade)
- [Feedback e contribuição](#feedback-e-contribuição)
- [Licença](#licença)

---

## Por que existe

Aprender programação com IA costuma virar copiar e colar: você pede, o assistente escreve o código, roda, e uma semana depois você não conseguiria escrever de novo. O código fica no projeto; o conhecimento não fica com você.

O Mentor Buddy inverte os papéis. Funciona como pair programming em que a IA é o **navegador** e você é o **piloto**: você digita cada linha e cada comando, e o mentor explica, pergunta, revisa e guarda o mapa. Ele só mexe no seu código depois que você errou três vezes no mesmo passo, e mesmo assim explica cada mudança.

É para quem quer aprender na prática com um agente de IA: iniciantes que já sabem o básico, devs migrando de linguagem e seniores que querem um sparring que cobre trade-off em vez de entregar resposta pronta.

## O que você ganha

- **Uma entrevista curta** que define o seu nível (júnior, pleno ou sênior), a linguagem, os seus interesses, o tempo disponível, a IDE, o idioma da conversa e o tom.
- **Um projeto de verdade**: uma de três ideias feitas sob medida para o que você curte, ou a sua própria ideia cortada até um tamanho que dá para terminar.
- **O caminho completo até produção**: ambiente, estrutura de pastas, esqueleto andando, funcionalidades com teste, banco de dados, qualidade, Docker, CI e deploy gratuito.
- **Uma escada de erros** que faz você bater cabeça do jeito certo antes de ver qualquer código.
- **Sem achismo**: versão, comando, API e preço são conferidos na documentação oficial durante a sessão, com o link.
- **Memória entre sessões** num arquivo `STUDY-MEMORY.md`, para cada sessão continuar exatamente de onde você parou.
- **Um resumo no fim do dia** com os temas onde você mais errou e a seção exata da doc para estudar.
- **Dois idiomas e dois tons**: português ou inglês, direto ou na zoeira, com correção de inglês opcional para quem quer praticar.

## Uma sessão, em resumo

Um trecho real de teste, encurtado. O aluno é júnior e está fazendo uma API de tabela de campeonato em C#, com o tom de zoeira.

```text
Aluno:  fiz o 5.2 mas o teste ta quebrando: Rejects_invalid_names(name: null) esperava
        BadRequest e veio InternalServerError, e o Creates_team_with_location esperava
        Created e veio OK. so me manda o codigo certo logo pfv

Mentor: Nem vem, bobão. Você tá na tentativa 1 do 5.2, então o que rola agora é revisão,
        não código.

        [OK] A validação de tamanho (3 a 50) existe e o endpoint já está plugado certo.
        [ALERTA] Nome null estoura antes de validar: request.Name é string?, e ler .Length
                 de null lança exceção antes do seu if rodar.
        [ALERTA] Nome só com espaço passa: "   " tem tamanho 3, então o time é criado.
        [ALERTA] O sucesso devolve 200 sem Location; o teste espera 201 Created.
        O que o seu código faz hoje: null -> exceção -> 500; "   " -> criado; válido -> 200.
        Refaça: use o método de string que checa null, vazio e espaço numa chamada só,
                e um resultado que gere 201 com Location.
                Doc: https://learn.microsoft.com/en-us/dotnet/api/system.string.isnullorwhitespace
        [PERGUNTA] Qual método de string resolve "null, vazio ou só espaço" numa chamada só?
```

Se o aluno errar de novo, o mentor cita o trecho errado e mostra a mesma ideia em outro contexto. No terceiro erro ele corrige o arquivo direto, com um comentário `MENTOR:` em cada mudança, e pede para o aluno explicar a correção com as próprias palavras.

## Como funciona

### 1. Entrevista

A primeira mensagem pergunta, nos dois idiomas, se você quer conversar em português ou em inglês. O resto da entrevista vem numa lista numerada só:

1. Há quanto tempo você programa e o que já construiu.
2. Qual linguagem quer usar.
3. Se já tem ideia de projeto ou quer sugestões (e do que você gosta).
4. Quanto tempo tem por semana e por sessão.
5. Sistema operacional e IDE.
6. Como quer ser tratado: **direto** ou **zoeira**.
7. Se escolheu inglês: se quer correção do seu inglês.

O mentor diz o nível que estimou, com o motivo, e você pode corrigir.

### 2. Projeto

- **Sem ideia?** Você recebe três opções montadas a partir de arquétipos de projeto (API REST com banco, ferramenta de linha de comando, aplicação web full stack, worker com fila, serviço de integração, aplicação em tempo real), com tema baseado no que você curte e tamanho de acordo com o seu tempo.
- **Tem a sua ideia?** O mentor acha a ação central e corta até a menor versão que ainda chega ao deploy. Exemplo: "um clone do iFood com app, pagamento, mapa e chat" vira "uma API de pedidos: cadastrar restaurante e cardápio, fazer pedido, acompanhar o status até a entrega". O resto vai para uma lista de "Depois".

O resultado é um brief com 3 a 6 critérios de aceitação testáveis. Você aprova; as decisões de produto são suas.

### 3. A trilha

| # | Fase | Pronto quando |
|---|---|---|
| 0 | Entrevista | Perfil e nível combinados |
| 1 | Projeto | Brief aprovado; `STUDY-MEMORY.md` criado |
| 2 | Ambiente | SDK, IDE e git funcionando; repositório com `.gitignore` e primeiro commit |
| 3 | Estrutura de pastas | Pastas criadas; você explica o papel de cada uma |
| 4 | Esqueleto andando | O menor caminho de ponta a ponta roda, com um teste passando |
| 5 | Funcionalidades | Cada critério de aceitação entregue com código, teste e commit |
| 6 | Persistência | Os dados sobrevivem a um restart; migrations versionadas |
| 7 | Qualidade | Validação, tratamento de erro, log, segredos fora do código |
| 8 | Docker | A aplicação e as dependências sobem com compose a partir de um clone limpo |
| 9 | CI | Um pipeline faz build e teste a cada push |
| 10 | Deploy | No ar num plano gratuito, configurado por variáveis de ambiente |
| 11 | Retrospectiva | Você escreve o que aprendeu; o próximo projeto é sugerido |

A estrutura de pastas é escolhida com você e fica proporcional ao problema: por funcionalidade em aplicações com muito CRUD, por camada quando as regras de negócio são pesadas, ou um meio-termo.

### 4. O ciclo de cada passo e a escada de erros

Cada fase é dividida em passos pequenos, e todo passo segue o mesmo ciclo:

| Momento | O que o mentor faz | Código do mentor | Seus arquivos |
|---|---|---|---|
| Instrução | O que construir, por que existe, para que serve, um resumo curto da doc oficial, o link e o critério de pronto | nenhum | só leitura |
| Acertou | O que está certo, mais as melhorias que valem a pena e por quê | nenhum | só leitura |
| Erro 1 | Revisão: o que está certo, onde quebra e por quê, o que o seu código faz de verdade, o que refazer | nenhum | só leitura |
| Erro 2 | O seu trecho errado citado com cada erro marcado, mais um exemplo curto do jeito certo em outro contexto | um exemplo curto e neutro | só leitura |
| Erro 3 | Corrige o seu arquivo, com um comentário `MENTOR:` em cada mudança, e te explica | a correção, no seu arquivo | editados |

- O contador de erros é do passo atual e zera quando o passo passa.
- Perguntar é de graça: uma dúvida conceitual recebe resposta curta com link da doc e não conta como erro.
- Observações de estilo e de nome vêm junto com o acerto e nunca contam como erro.
- Pedir o código antes da hora não pula a escada.

### 5. Ajustado ao seu nível

| | Júnior | Pleno | Sênior |
|---|---|---|---|
| Nome de pasta e módulo | Um nome de exemplo e o papel | Só o papel; você dá o nome | Só o papel; você dá o nome |
| Biblioteca ou framework | Uma recomendação popular e mantida, com o porquê | O que pesquisar e os critérios; você traz uma escolha e o mentor valida | Igual ao pleno, pesando trade-offs |
| Explicações | Mais completas, um conceito por vez | Curtas, focadas no porquê | Curtas, focadas em trade-off, modos de falha e operação |
| Testes | Obrigatórios a partir do esqueleto | Obrigatórios; TDD opcional | Obrigatórios; TDD opcional |

O nível é reavaliado a cada entrega. Quando a evidência mostra que está errado, o mentor avisa e ajusta.

### 6. Sem achismo: só documentação oficial

A skill separa dois tipos de conhecimento:

- **Estável**: método de ensino, fases, régua de revisão, papel das pastas, arquétipos de projeto. Isso fica dentro da skill e só muda quando o repositório é atualizado.
- **Perecível**: versões, passos de instalação, comandos e flags, nomes de API, chaves de configuração, padrões de framework, preços e limites de plano gratuito. O mentor confere na documentação oficial durante a sessão antes de dizer, e te passa o link.

Quando o agente não tem acesso à web, o mentor avisa e te dá o link oficial para conferir, em vez de afirmar versão ou comando de memória.

### 7. Memória entre sessões

Depois da entrevista, o mentor cria o `STUDY-MEMORY.md` na raiz do seu projeto. Tudo que uma sessão precisa para recomeçar fica num cabeçalho curto, lido toda vez; o resto só é aberto quando necessário, o que deixa cada sessão barata.

```markdown
## Header
- Conversation language: pt
- English corrections: n/a
- Tone: banter
- Level: junior (set 2026-10-12; last recalibration: none)
- Stack: C# / .NET, ASP.NET Core minimal APIs, IDE Visual Studio 2026, OS Windows 11
- Project: REST API with a database - football league table
- Now: Phase 5 Feature slices / Step 5.3 Register match result / Attempt 0
- Next action: create POST /matches that stores home team, away team and both scores
- Last session: 2026-10-16 - step 5.2 passed after 2 misses; started 5.3
- Review on resume: IsNullOrWhiteSpace versus IsNullOrEmpty; 201 Created with Location
```

Abaixo do cabeçalho: o brief, o plano de fases, um registro de decisões, um **mapa de erros** (tema, quantas vezes errou, seção exata da doc), um diário de sessões compacto e as dúvidas em aberto.

Quando você volta, o mentor faz três perguntas rápidas de revisão sobre os temas em que você mais errou e continua do `Next action`.

### 8. Resumo do fim do dia

Diga que vai parar ("vou parar por hoje") e o mentor atualiza a memória e mostra:

```text
Hoje
- o que foi feito

Onde você mais tropeçou
1. <tema> - <o erro em uma linha> - <link da doc oficial, seção exata>

Estudar antes da próxima
- <link da doc> - <por quê>

A próxima sessão começa com
- <próxima ação>
```

### 9. Idiomas e tom

- **Conversa**: português ou inglês. Nomes no código, mensagens de commit e nomes de arquivo ficam em inglês.
- **Direto**: curto e neutro, sem gíria.
- **Zoeira**: gíria e provocação leve de amigo, mirando o erro, sempre seguida da explicação técnica. Muda para o direto quando você parece frustrado ou pede.
- **Correção de inglês** (opcional): no máximo duas linhas no topo da resposta, só para erros de verdade.

## Agentes compatíveis

O Mentor Buddy segue o formato aberto [Agent Skills](https://agentskills.io/specification), então funciona em qualquer agente que leia esse formato.

| Agente | Pastas pessoais de skill que ele lê | Como a skill começa |
|---|---|---|
| Claude Code (terminal, VS Code, JetBrains) | `~/.claude/skills/` | Automaticamente pela descrição, ou `/mentor-buddy` |
| GitHub Copilot no Visual Studio 2026 | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | Automaticamente no agent mode |
| GitHub Copilot no VS Code | `~/.agents/skills/`, `~/.claude/skills/`, `~/.copilot/skills/` | Automaticamente, ou `/mentor-buddy` |
| GitHub Copilot CLI | `~/.agents/skills/`, `~/.copilot/skills/` | Automaticamente, ou `/mentor-buddy` |
| OpenAI Codex | `~/.agents/skills/` | Automaticamente, ou `$mentor-buddy` |
| Gemini CLI | `~/.agents/skills/`, `~/.gemini/skills/` | O modelo ativa e pede o seu consentimento |
| Cursor | `~/.agents/skills/`, `~/.cursor/skills/`, `~/.claude/skills/` | Automaticamente, ou `/mentor-buddy` |

Nenhuma pasta é lida por todos: `~/.agents/skills/` cobre todos menos o Claude Code, que só lê `~/.claude/skills/`. A instalação abaixo deixa uma cópia real em `~/.agents/skills/` e um link em `~/.claude/skills/`.

## Requisitos

- Um agente de IA da tabela acima, com um plano que permita uso de chat ou agente.
- Git, para instalar e atualizar a skill.
- Acesso à internet durante as sessões, para o mentor conferir a documentação oficial. Sem isso a skill continua funcionando, mas te manda para a doc em vez de confirmar versão e comando.
- No Visual Studio: versão 2026 (18.5 ou mais nova), GitHub Copilot e agent mode.

## Instalação

### Windows (PowerShell)

```powershell
git clone https://github.com/mauricioreiss/mentor-buddy.git "$HOME\.agents\skills\mentor-buddy"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.claude\skills\mentor-buddy" -Target "$HOME\.agents\skills\mentor-buddy"
```

Junction não precisa de permissão de administrador.

### macOS e Linux

```bash
git clone https://github.com/mauricioreiss/mentor-buddy.git ~/.agents/skills/mentor-buddy
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/mentor-buddy ~/.claude/skills/mentor-buddy
```

Se o link não funcionar no seu sistema, copie a pasta para `~/.claude/skills/mentor-buddy` (aí você vai precisar atualizar as duas cópias).

### Usa um agente só?

Clone direto na pasta que ele lê: `~/.claude/skills/mentor-buddy` se for só o Claude Code, ou `~/.agents/skills/mentor-buddy` para Codex, Copilot, Gemini CLI ou Cursor.

### Conferir se carregou

Reinicie o agente ou abra um chat novo e diga: "quero estudar com o mentor buddy". Onde houver comandos com barra, `/mentor-buddy` também deve aparecer. No Visual Studio, confira se o chat está em agent mode; o chat mostra quando uma skill está sendo aplicada.

### Atualizar

```bash
git -C ~/.agents/skills/mentor-buddy pull
```

No PowerShell do Windows: `git -C "$HOME\.agents\skills\mentor-buddy" pull`. O link já enxerga a atualização.

### Desinstalar

Windows (remove primeiro o junction, depois a pasta):

```powershell
cmd /c rmdir "$HOME\.claude\skills\mentor-buddy"
Remove-Item -Recurse -Force "$HOME\.agents\skills\mentor-buddy"
```

macOS e Linux:

```bash
rm ~/.claude/skills/mentor-buddy
rm -rf ~/.agents/skills/mentor-buddy
```

## Como usar

1. Crie ou abra uma pasta vazia na sua IDE, ou a pasta de um projeto que você já começou com o mentor.
2. No chat do agente, diga o que quer aprender. O mentor conduz a partir daí.

| Você quer | Diga algo como |
|---|---|
| Começar | "quero estudar com o mentor buddy", "me ensina C# fazendo um projeto", "teach me Go by building a project" |
| Retomar | Abra a pasta do projeto e dê um oi; o mentor lê o `STUDY-MEMORY.md` |
| Pular as perguntas de revisão | "pula a revisão" |
| Tirar uma dúvida | É só perguntar; pergunta nunca conta como erro |
| Mudar o tom | "muda pro direto" ou "muda pra zoeira" |
| Ligar ou desligar a correção de inglês | "corrige meu inglês" ou "para de corrigir meu inglês" |
| Discordar do nível estimado | "acho que sou pleno, não júnior" |
| Parar por hoje | "vou parar por hoje", "that's it for today" |
| Ir além do plano gratuito | "quero escalar isso"; o mentor pesquisa as opções e os preços atuais |

## Mapa de documentação curado

A skill já vem com pontos de entrada verificados para a documentação oficial destas stacks:

| Stack | Cobre |
|---|---|
| C# e .NET | Linguagem, instalação do SDK, dotnet CLI, NuGet, ASP.NET Core, minimal APIs, EF Core, testes, Docker, Visual Studio |
| Python | Documentação, venv, empacotamento, pip, uv, pytest, PEP 8, FastAPI, Django, Flask, SQLAlchemy, Alembic, Docker |
| Go | Instalação, tutoriais, organização de módulo, Effective Go, biblioteca padrão, net/http, testes, acesso a banco, Docker |
| TypeScript e Node.js | Documentação do TypeScript, tsconfig, API do Node.js, npm, test runner, Vitest, Express, Fastify, NestJS, Docker |
| Java | dev.java, documentação do Java SE, Spring Boot, Spring Initializr, Maven, Gradle, JUnit, Docker |
| Ferramentas | Git, GitHub, modelos de .gitignore, Docker, Compose, GitHub Actions, IDEs, OWASP Top 10, configuração Twelve-Factor |

Qualquer outra linguagem também funciona: o mentor acha a documentação oficial ao vivo e avisa que ela está fora do mapa curado.

## Estrutura do repositório

```text
mentor-buddy/
  SKILL.md                      instruções principais, lidas quando a skill começa
  references/
    interview.md                fases 0 e 1: entrevista, projeto, criação da memória
    phases.md                   fases 2 a 11, lidas uma seção por vez
    teaching-loop.md            formatos de revisão, escada de erros, escolha de biblioteca
    folder-roles.md             papel das pastas e trade-offs de organização
    project-archetypes.md       catálogo de projetos, escopo por nível, corte de escopo
    session-rituals.md          perguntas da volta e resumo do fim do dia
    memory-template.md          modelo do STUDY-MEMORY.md
    tone.md                     tons direto e zoeira, correção de inglês
    docs-*.md                   pontos de entrada da documentação oficial por stack
  README.md
  README.pt-BR.md
  LICENSE
```

A raiz do repositório é a própria pasta da skill: instalar é um `git clone` e atualizar é um `git pull`.

## Perguntas frequentes

**Ele alguma vez escreve código para mim?**
Só em dois momentos. No segundo erro num passo, ele mostra um exemplo curto do jeito certo em outro contexto, de propósito não pronto para colar. No terceiro erro, ele corrige o seu arquivo com um comentário `MENTOR:` em cada mudança e pede para você explicar a correção. Todo o resto você digita.

**Qual modelo devo usar?**
A skill funciona com o modelo que o seu agente usa. Modelos mais fortes seguem a escada e as regras de memória com mais consistência.

**Precisa de internet?**
Para confirmar versão, comando e preço na documentação oficial, sim. Sem internet, o mentor avisa que não consegue verificar e te passa o link para você conferir.

**Custa alguma coisa?**
A skill é gratuita. Você precisa do plano do seu agente, e a fase de deploy usa planos gratuitos, conferidos na página oficial de preços de cada provedor durante a sessão.

**Posso usar em português?**
Pode. Escolha português na primeira mensagem; a mentoria inteira acontece em português, com o código em inglês.

**Posso usar no trabalho?**
Use nos seus projetos de estudo. Não cole código nem dados da sua empresa num agente de IA sem autorização.

**E se a minha linguagem não estiver no mapa curado?**
Funciona do mesmo jeito. O mentor pesquisa a documentação oficial ao vivo e avisa que a linguagem está fora do mapa curado.

## Privacidade

O `STUDY-MEMORY.md` entra no git do seu projeto por padrão e lista os temas em que você errou. Se o seu repositório for público e você preferir guardar isso para você, coloque o arquivo no `.gitignore`. A skill em si não envia nada para lugar nenhum: são instruções em texto lidas pelo seu agente.

## Feedback e contribuição

Ideias, bugs e dúvidas são bem-vindos nas [Issues](https://github.com/mauricioreiss/mentor-buddy/issues). Pull requests são avaliados a critério do mantenedor, então abra uma issue antes para discutir a mudança.

## Licença

[MIT](LICENSE). Criado por [Mauricio Reis](https://github.com/mauricioreiss).
