# Toolkit · matriz de cobertura e resultado

**Fonte:** catálogo da revisão `790a895304e0c08b70a5b215c9d334f1c86b816c` · **Estado:** decisões executadas para a base documental · **Data:** 22/10/2026.

As 23 entradas foram avaliadas. A tabela de decisões preserva o raciocínio do desenho; a tabela de resultados abaixo registra o que ocorreu. “Reutilizado” não afirma validação funcional de todos os comandos do componente. Itens futuros têm um gatilho de reavaliação, sem dependência preventiva.

| Guia / componente | Necessidade e estado observado | Ação e escopo propostos | Dependência, risco e critério de validação |
|---|---|---|---|
| 01 Superpowers | Skills descobertas; brainstorming já utilizado | Reutilizar distribuição do cliente | Evitar cópias duplicadas; evidenciar etapas de desenho, plano e execução |
| 02 Subagentes | Ferramentas nativas disponíveis; um revisor executou baseline somente leitura | Reutilizar delegação pontual | Um escritor por arquivo; revisão independente de mudanças relevantes; registrar modelo apenas quando observável |
| 03 RTK | Binário 0.48.0; hook global referenciado; RTK.md local ausente | Reutilizar binário e conciliar referência local após dry-run | CLI difere do guia; sem atualização global; testar comando suportado sem dupla execução e documentar limite de observação do hook |
| 04 Ponytail | Skill/plugin disponível na sessão | Reutilizar no trabalho de implementação, intensidade `full`, preservando requisitos, segurança e acessibilidade | Nenhum proxy novo; confirmar instrução carregada ao aplicar o fluxo |
| 05 Caveman | Skills disponíveis | Reutilizar comunicação concisa em português, preservando clareza | Texto técnico e documentos em linguagem normal; não inferir economia de tokens |
| 06 ESLint/Biome | Sem fonte JS/TS ou lint existente | Inaplicável agora; usar checks de documentos e scripts existentes | Quando houver app TS, medir e adotar perfil compatível; não instalar lint sem código-alvo |
| 07 Graphify | CLI e ferramenta não observados; poucos scripts, grande parte conteúdo documental/gerado | Não instalar agora por ausência de necessidade estrutural demonstrada | Reavaliar com código ou busca relacional difícil; eventual CLI global pede autorização; sem API semântica ou grafo alegado |
| 08 Obsidian | Nenhum vault/destino solicitado | Inaplicável | Documentos canônicos locais cobrem contexto; não exportar dados |
| 09 Memória Claude | Cliente ativo é Codex; documentação já registra decisões | Equivalente: índice curto e documentos versionáveis | Não editar memória global; comprovar recuperação por instruções e referências reais |
| 10 Hooks | Configuração global existente com referência RTK | Reutilizar e não duplicar | Nenhum hook Git; alterações globais fora do escopo; configuração não prova trust/carregamento |
| 11 agent-browser | Sem aplicação/interface executável | Inaplicável agora; ferramentas de browser já existem na sessão | Reavaliar quando houver interface local; não instalar outro browser para preencher checklist |
| 12 Context7 | Ferramentas não descobertas; sem seção global detectada na leitura limitada | Propor MCP local, após verificar suporte oficial e ausência de equivalente | Pode exigir trust/autenticação/reinício; validar consulta real; sem segredos em query |
| 13 Artifact skills | Skills de documentos, PDF, planilhas e slides já disponíveis | Reutilizar quando o artefato exigir | Nenhum Word/PDF/planilha solicitado neste setup; não duplicar catálogos |
| 14 Chrome DevTools MCP | Sem runtime de interface para diagnosticar | Inaplicável agora | Escolher ferramenta já disponível na futura lacuna de console/rede/performance |
| 15 Codex | App em uso, CLI 0.162.1 identificada, configuração existente | Reutilizar cliente, autenticação e permissões | Arquivos locais conforme formato suportado; não aplicar exemplos de acesso irrestrito |
| 16 Vercel skills / find-skills | Plugins Vercel/Supabase disponíveis; React é stack futura, não instalada | Reutilizar equivalentes; avaliar writing-guidelines e find-skills locais somente se preencherem lacuna real | Checar fonte, licença, nome e descoberta; sem instalar conjunto Next/Vercel por antecipação |
| 17 next-dev-loop / bundle optimizer | Não há Next.js, bundler ou servidor | Inaplicável | Só reavaliar se essa stack for adotada separadamente; não trocar React/Electron/Nest por Next |
| 18 PostgreSQL | PostgreSQL/Supabase propostos no produto; skill best-practices já descoberta | Reutilizar skill para futuras mudanças de schema/SQL | Sem banco/DDL aqui; não afirmar teste de RLS, pool ou consulta real |
| 19 gh-fix-ci | Sem Git, remoto, PR ou GitHub Actions do produto | Inaplicável | Reavaliar ao existir CI autorizado com falha; nenhuma consulta de conta necessária agora |
| 20 Segurança diferencial | Skills de segurança disponíveis; sem histórico Git para comparar | Equivalente: revisão manual de snapshots e prompt de segurança versionado | Revisar scripts/artefatos efetivos; relatório sensível fora do projeto quando necessário; sem inventar base/head |
| 21 shadcn | UI e kit ainda não implementados/escolhidos | Inaplicável | Não selecionar um design system só por disponibilidade da skill |
| 22 Sentry MCP | Nenhum serviço ou conta de Sentry escolhido | Inaplicável ao estado atual | Reavaliar após escolha de observabilidade e autorização de organização/projeto; não instalar SDK |
| 23 Harness2 | Nenhuma dependência necessária ao método nativo | Integrar adaptação nativa e procedimento reutilizável, com casos descartáveis relevantes | Uma comparação candidata para falha observada; sem CLI oficial, benchmark/API, novo provedor ou permissões alteradas |

## Itens transversais e adicionais avaliados

| Item | Decisão proposta | Evidência / condição |
|---|---|---|
| Nove documentos do manifesto | Mapear equivalentes e criar entradas factuais faltantes | Mapa no desenho; capítulos de produto continuam canônicos |
| Templates de Next/Drizzle/Zod/Pino | Inaplicáveis à base atual | Não existe app nem seleção de ORM executada |
| Perfil typed lint e quality-gate JS | Adiar até existir código compatível | Scripts atuais Python/PowerShell demandam checks próprios |
| Vercel deploy, optimize e tokens | Sem necessidade de ativação local agora | Hospedagem não escolhida; nenhuma publicação autorizada |
| React Native/Expo | Inaplicável | Desktop Electron solicitado; móvel fora do primeiro lançamento |
| Transições React | Sem tarefa de animação/runtime | Não habilitar APIs experimentais ou dependências por catálogo |
| Skill creation | Sem lacuna recorrente que justifique skill própria | Preferir scripts determinísticos e documentação atual |
| Plugins oficiais adicionais / aia-harness | Não instalar | Recursos existentes atendem diagnóstico, edição, revisão e artefatos |
| Hooks do cliente | Preservar configuração existente | Integração precisa de prova de trust e funcionamento; nada global neste setup |
| Migração de stack ou dependências | Fora do desenho | Tecnologias solicitadas e fontes existentes preservadas |
| Memória externa/global | Não alterar | Usar índice e fontes canônicas locais; nenhum vault ou exportação |
| CI / proteções / Git | Não criar repositório, branch obrigatória ou hook | Não há Git; check explícito local será suficiente nesta fase |
| Inicialização do produto | Etapa posterior de desenvolvimento | Sem servidor/app, não há fluxo browser/API/dados a certificar |

## Resultados observados

| Componente | Estado final e evidência / próximo gatilho |
|---|---|
| 01 Superpowers | **Reutilizado**: brainstorming, plano, execução e verificação aplicados; arquivos de desenho/plano e testes registram as etapas |
| 02 Subagentes | **Validado**: três contextos de ensaio e revisão independente; escopos explícitos e preservação por hashes |
| 03 RTK | **Validado na CLI**: dry-run/init locais, referência lida, `rtk git status` e `rtk proxy git status` saíram 0 em checkout externo; hook não observado |
| 04 Ponytail | **Reutilizado**: skill integral lida, intensidade full; stdlib e reaproveitamento de fontes preservados |
| 05 Caveman | **Equivalente aplicado**: comunicação concisa em português; modo de voz/registro especial não ativado, sem alegação de economia medida |
| 06 ESLint/Biome | **Inaplicável**: sem app JS/TS; testes Python e checker documental usados. Reavaliar com app |
| 07 Graphify | **Não selecionado por falta de necessidade**: sem lacuna relacional demonstrada; reavaliar com crescimento do código |
| 08 Obsidian | **Inaplicável**: nenhum vault solicitado; fontes locais mantidas |
| 09 Memória Claude | **Equivalente aplicado**: índice AGENTS e mapa local, sem edição de memória global; instruções recuperadas nos contextos de teste |
| 10 Hooks | **Reutilizado sem alteração**: referência global preexistente preservada; carregamento/reescrita não comprovados. Observar em próxima sessão antes de prefixar duas vezes |
| 11 agent-browser | **Inaplicável**: sem interface executável; browser já disponível no cliente, sem nova instalação |
| 12 Context7 | **Serviço validado; descoberta nativa pendente**: TOML local válido, initialize/tools/list/resolve/query reais por HTTP público, biblioteca retornada `/python/cpython`. Recarregar sessão confiável e repetir pela ferramenta nativa |
| 13 Artifact skills | **Reutilização disponível**: catálogo existente atende documentos; nenhum novo Word/PDF foi necessário ou validado |
| 14 Chrome DevTools MCP | **Inaplicável**: sem runtime UI; reavaliar com diagnóstico real de rede/console |
| 15 Codex | **Reutilizado**: cliente e CLI existentes; config local de projeto, sem mudança de auth/modelo/permissões |
| 16 Vercel / find-skills | **Reutilizado por equivalência**: catálogo Vercel/Supabase e skills documentais já descobertos; writing-guidelines/find-skills não instalados porque não há lacuna concreta de escrita ou busca |
| 17 next-dev-loop / bundle optimizer | **Inaplicável**: sem Next/bundle; stack pedida preservada |
| 18 PostgreSQL | **Inaplicável à execução atual**: skill disponível para futura modelagem; nenhum SQL, banco ou RLS executado |
| 19 gh-fix-ci | **Inaplicável**: sem CI/Git/PR; usar quando houver falha autorizada |
| 20 Segurança diferencial | **Equivalente aplicado**: comparação contra backups e revisão read-only dos scripts; prompts versionados em quality; sem base/head inventados |
| 21 shadcn | **Inaplicável**: nenhuma UI ou kit escolhido |
| 22 Sentry MCP | **Inaplicável**: serviço/organização não escolhidos; reavaliar na implementação da observabilidade |
| 23 Harness2 | **Adaptação nativa validada no escopo**: dois fixes 7/7, revisão sem mutação e candidato de manutenção relocada; ver avaliação. Framework oficial não executado |

Os itens transversais mantêm as decisões da tabela anterior: nove destinos implementados no mapa; nenhuma instalação adicional, migração, deploy, memória externa, Git ou inicialização do produto. Configuração presente, descoberta pelo cliente e resposta funcional são evidências distintas.
