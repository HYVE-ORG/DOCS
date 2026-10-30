# Adoção do Vibe Coding Toolkit · desenho para revisão

**Data do desenho:** 21/10/2026 · **Estado:** aprovado pelo usuário em 22/10/2026; plano preparado, aguardando aprovação para execução.

Este documento registra o desenho aprovado do setup. A aprovação autoriza preparar o plano, que terá revisão própria antes da implementação. Nenhuma instalação ou mudança de configuração do projeto foi feita nesta etapa. A documentação do produto continua na versão 0.3.

## Objetivo entendido

Executar o Prompt 12 do Vibe Coding Toolkit para preparar este projeto para desenvolvimento assistido por IA: instruções claras, contexto recuperável, ferramentas compatíveis, comandos reproduzíveis, revisão e evidências. O usuário pediu expressamente começar com brainstorming.

O produto pretendido continua sendo a plataforma de trabalho para a equipe: TypeScript, React, Electron, NestJS, Docker e Supabase. O setup atual será adaptado à documentação e às ferramentas que existem neste diretório. A implementação da aplicação é uma etapa de produto distinta, que não será criada como efeito colateral deste setup.

## Estado observado

- Raiz: diretório `cha` informado pelo usuário; contém `AGENTS.md`, `LEIS.md`, `work/` e `outputs/`.
- Existem 12 capítulos de documentação, índice, consolidado, ZIPs e referências legais. Não há aplicação, `package.json`, lockfile de aplicação, CI, banco configurado ou servidor local.
- `git rev-parse --show-toplevel` retorna que a raiz não pertence a um repositório Git. Não há branch, diff ou histórico do produto para revisar nesta etapa.
- Node.js 24.14.0, npm 11.9.0, Python 3.12.10, Git 2.53.0.windows.2 e RTK 0.48.0 foram observados por comandos locais.
- A CLI Codex identificada retorna 0.162.1; essa versão não determina a versão do aplicativo desktop. O comando passou com avisos de acesso ao diretório temporário de aliases, sem falha do projeto.
- Há skills de Superpowers, Ponytail, Caveman, segurança, documentos e Supabase descobertas nesta sessão. Não foram encontradas ferramentas Context7 ou Graphify na lista da sessão. O executável Graphify não foi localizado no PATH.
- A configuração global contém referência a RTK em um grupo `PreToolUse`. Isso comprova presença da configuração, mas não observação de reescrita nesta superfície. Não adicionar outro hook sem verificar esse funcionamento.
- `RTK.md` não existe na raiz nem nos caminhos de instruções consultados. `rtk init --codex --dry-run` indica que criaria o arquivo local, sem escrever nada.

### Baseline verificada independentemente

Um subagente nativo realizou uma rodada somente leitura, sem instalar ou executar scripts geradores:

| Verificação | Resultado |
|---|---|
| Links locais nos documentos canônicos, inventário legal e LEIS.md | 36 destinos, nenhum quebrado |
| Manifesto legal | 13 snapshots com tamanho e SHA-256 correspondentes |
| ZIP v0.3 | 31 entradas lidas e comparadas aos arquivos locais; nenhuma divergência |
| Produto executável | Ausente; lint/typecheck/build/E2E de aplicação não se aplicam ainda |

Limites: não houve consulta de vigência jurídica nesta tarefa, execução de browser, teste de banco, consulta Context7 ou reinício do cliente. O contexto do revisor foi um subagente, não uma sessão reiniciada do Codex. Não foram medidos custos ou economia de tokens.

## Abordagens consideradas

| Abordagem | Consequência | Avaliação |
|---|---|---|
| Setup adaptado ao projeto documental | Mantém fontes atuais, corrige manutenção e prepara ferramentas no menor escopo | Recomendada |
| Instalar o catálogo e gerar uma aplicação agora | Introduz dependências e produto ainda ausentes, exigindo decisões adicionais de implementação | Não selecionada para este setup |
| Apenas registrar recomendações | Não entrega configuração nem verificações posteriores | Insuficiente ao pedido completo |

## Desenho recomendado

### 1. Contexto e fontes canônicas

Criar uma entrada curta na raiz e mapear os nove destinos do manifesto para fontes existentes ou complementos factuais. Preservar os capítulos atuais; não duplicar PRD e arquitetura em documentos concorrentes. Distinguir sempre arquitetura proposta do produto de arquivos realmente implementados.

| Destino do manifesto | Fonte/destino proposto |
|---|---|
| README.md | Nova entrada curta da raiz, apontando para documentação e comandos efetivos |
| PRODUCT.md | Preservar equivalentes: capítulos 01 e 02 como fontes de escopo e requisitos; registrar mapeamento |
| AGENTS.md | Conciliar arquivo atual com comandos, mapa e acordos essenciais, preservando encaminhamento legal |
| CLAUDE.md | Ponte mínima para AGENTS, sem configurar ou instalar Claude como efeito colateral |
| docs/architecture.md | Capítulo 04 permanece arquitetura proposta; setup descreve apenas o estado real das ferramentas |
| docs/design.md | Capítulo 03 permanece fonte visual e de acessibilidade |
| docs/onboarding.md | Novo equivalente em `outputs/toolkit-setup/onboarding.md`, com uso real do repositório documental |
| docs/quality.md | Novo equivalente em `outputs/toolkit-setup/quality.md` para checks do setup; capítulo 08 continua metas do produto |
| docs/setup.md | Novo equivalente em `outputs/toolkit-setup/setup.md`, com catálogo, versões, evidências e pendências |

O manifesto será um mapa de equivalências, não uma obrigação de criar nove arquivos duplicados. Notas temporárias de execução ficam separadas das decisões estáveis. Memória global do usuário não será alterada.

### 2. Ferramentas e compatibilidade

Reutilizar plugins e skills disponíveis. Configurar Context7 no escopo local suportado se não houver conexão equivalente; confirmar suporte e confiança do Codex antes de declarar carregamento. Autenticação, reinício e trust que dependam do usuário ficam registrados com intervenção exata.

Para RTK, usar a instalação existente, inspecionar a integração global sem expor segredos e criar a referência local pelo mecanismo compatível, se necessário. O `--help` observado descreve Codex com AGENTS/RTK.md, diferente do guia que descreve hook nativo. Não substituir a configuração global nem duplicar wrappers por inferência.

Graphify não tem instalação observada; avaliar benefício sobre este acervo pequeno e documental. Não instalar globalmente sem autorização específica, não usar extração semântica paga e não gerar um grafo vazio de aplicação inexistente. Registrar a condição para adoção quando houver código/necessidade estrutural.

A [matriz completa](02-matriz-de-cobertura.md) cobre todas as 23 entradas e os itens adicionais do catálogo. Itens de Next.js, bundle, UI runtime, CI, Sentry e deploy recebem decisões explícitas baseadas no estado atual.

### 3. Qualidade e manutenção

Corrigir o caminho absoluto do regenerador, apoiar a descoberta de capítulos e manter verificação explícita de requisitos. Detectar inconsistências reais sem aceitar ausência silenciosa de requisitos. Separar um comando de checagem sem escrita do comando de geração. Preservar a invocação exigida em AGENTS ou oferecer compatibilidade documentada caso o código seja organizado em `scripts/`.

O pacote entregue deve incluir o necessário para seguir suas próprias instruções de manutenção. Verificar também contexto, links, JSON, checksums e coerência entre fontes, consolidado e ZIP. Não instalar ESLint/Biome/TypeScript em um projeto que ainda contém apenas scripts Python/PowerShell e Markdown.

Nova lógica de validação terá testes pequenos com fixtures sintéticas: link quebrado, arquivo legal alterado, capítulo acrescido e verificação sem modificar arquivos. Esses testes devem provar falhas relevantes; não espelhar cada linha do script.

### 4. Avaliação e revisão

Adotar a adaptação nativa do método Harness2: procedimento local com critérios definidos, sem instalar o framework oficial, alterar modelo, fornecedor ou permissões. Aplicar os casos descartáveis relevantes do toolkit após revisão do código das fixtures e avaliador.

A melhoria candidata proposta é uma única correção de manutenção demonstrada: portabilidade e reprodutibilidade dos comandos. Comparar a mesma fixture antes/depois, sem mudar seu avaliador para fazê-la passar. Resultados de descoberta de instruções, comandos e skills serão separados de testes do script e de reinício do cliente.

Revisão independente será somente leitura, focada nos arquivos efetivamente alterados, scripts de manutenção, privacidade dos artefatos e preservação das instruções legais. O coordenador verifica cada achado e executa os checks afetados. Nenhum número fixo de revisões será usado como prova de qualidade.

## Fontes e limites de autorização

Toolkit obtido fora deste projeto, em checkout de leitura identificado pelo commit **790a895304e0c08b70a5b215c9d334f1c86b816c**. O Prompt 12, catálogo, guias e templates consultados são desse checkout. Referência pública: [Prompt 12 nessa revisão](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/12-existing-project-setup.md).

Instalação, configuração em arquivo, descoberta pelo cliente e execução funcional serão registradas separadamente. O setup preservará permissões atuais; exemplos de acesso irrestrito existentes em guias não serão adotados. Não há autorização para produção, custos, publicação, push, mensagens, hooks Git ou atualização geral da máquina.

Backups recuperáveis das configurações relevantes serão criados antes de alterações. Sem Git no produto, a revisão usará um inventário e snapshots explícitos dos arquivos alterados; inicializar Git ou criar commits não faz parte deste desenho.

## Critérios de conclusão após implementação aprovada

1. Fontes e nove destinos mapeados sem duplicação de conteúdo normativo.
2. Toda linha da matriz tem status e evidência ou condição concreta de retomada.
3. Comandos de checagem/geração portáteis, documentados e testados.
4. Referências legais preservadas e manifesto validado.
5. Consolidado e pacote regenerados com todas as dependências de manutenção necessárias.
6. Integrações testadas quando observáveis; trust/restart/autenticação pendentes descritos sem alegar funcionamento.
7. Avaliação nativa e revisão independente realizadas no escopo definido, com achados resolvidos ou explicitamente encaminhados.
8. Reaplicação segura não duplica instruções, servidores, skills ou hooks.

## Etapa seguinte

O desenho foi aprovado pelo usuário em 22/10/2026. Elaborar e revisar o plano de implementação com arquivos, dependências e comandos de aceite antes das instalações e edições de configuração, conforme o brainstorming solicitado. O pedido completo continua pendente dessas etapas; o diagnóstico não é apresentado como setup concluído.
