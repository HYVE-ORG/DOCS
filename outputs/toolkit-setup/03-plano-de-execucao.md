# Adoção do Vibe Coding Toolkit · plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking. Recomendação para este projeto: execução nativa nesta conversa, com revisão independente ao final. O método depende da revisão do usuário.

**Goal:** Entregar um ambiente documental de desenvolvimento assistido por IA, com instruções úteis, ferramentas compatíveis e manutenção portátil e verificável.

**Architecture:** Preservar os capítulos canônicos e as referências legais. Um script Python de biblioteca padrão centraliza checagem e geração; o comando antigo continua como entrada compatível. Integrações do cliente ficam separadas das ferramentas de manutenção e recebem evidência própria.

**Tech Stack:** Python 3.12 e biblioteca padrão, PowerShell, Markdown/JSON, Codex e RTK existentes; MCP Context7 local se suportado. Não há dependência de aplicação a instalar nesta etapa.

**Spec:** [Desenho aprovado](01-brainstorming-e-design.md), aprovado em 22/10/2026; [matriz de cobertura](02-matriz-de-cobertura.md).

**Status:** execução nativa aprovada e realizada em 22/10/2026, com revisão independente. Checkboxes indicam etapas tratadas; observações indisponíveis (reinício, descoberta nativa, pausa/retomada) permanecem explicitamente não executadas no setup e na avaliação.

## Global Constraints

- “A implementação da aplicação é uma etapa de produto distinta, que não será criada como efeito colateral deste setup.”
- “Memória global do usuário não será alterada.”
- “O setup preservará permissões atuais; exemplos de acesso irrestrito existentes em guias não serão adotados.”
- “Não há autorização para produção, custos, publicação, push, mensagens, hooks Git ou atualização geral da máquina.”
- “Backups recuperáveis das configurações relevantes serão criados antes de alterações.”
- “Instalação, configuração em arquivo, descoberta pelo cliente e execução funcional serão registradas separadamente.”
- Revisão do toolkit fixada em `790a895304e0c08b70a5b215c9d334f1c86b816c`; usar guias/templates dessa revisão.
- Preservar os 13 snapshots legais e seu manifesto; não recalcular o manifesto para esconder alteração nos bytes.
- Preservar a invocação `python work/finalizar_documentacao.py`, exigida nas instruções atuais.
- Sem Git do produto: não criar repositório, commits ou worktree. Revisar arquivos contra backups explícitos.
- Caminhos abaixo são relativos à raiz do projeto; resolver a raiz pelo arquivo executado, nunca por caminho pessoal ou pelo diretório de trabalho.
- Um escritor por arquivo. Revisores são somente leitura; o coordenador mantém configurações, geração de artefatos e integração.

## Review Focus

1. Diretório clonado/extraído em outro caminho, com espaços ou acentos: os mesmos comandos devem funcionar sem editar código — T2/T6.
2. Crescimento da documentação: aceitar capítulo novo contíguo, mas recusar remoção de capítulo obrigatório e requisitos ausentes — T2.
3. Snapshot legal alterado ou manifesto apontando para fora da raiz: falhar sem escrever outputs nem “corrigir” hashes — T2.
4. Pacote isolado: instruções e comandos precisam funcionar com os arquivos realmente incluídos; não depender do checkout original — T6.
5. Hook ou MCP existente, confiança/reinício ausentes: preservar configuração e distinguir presença, descoberta e execução — T4/T7.

## Arquivos e responsabilidades

| Arquivo | Responsabilidade |
|---|---|
| `scripts/documentacao.py` | CLI portátil e funções de validação/geração, sem dependências externas |
| `work/finalizar_documentacao.py` | Entrada compatível que encaminha para o script canônico, preservando os argumentos |
| `tests/test_documentacao.py` | Casos sintéticos de falha, portabilidade, pacote e ausência de escrita em check |
| `outputs/documentacao-software/manifesto-documentacao.json` | Capítulos obrigatórios e IDs RF/RN esperados, retirando números mágicos do código |
| `README.md`, `AGENTS.md`, `CLAUDE.md`, `RTK.md` | Entrada, instruções concisas, ponte Claude e referência RTK compatível |
| `outputs/toolkit-setup/document-map.json` | Mapeamento dos nove destinos para fontes canônicas reais |
| `outputs/toolkit-setup/onboarding.md`, `quality.md`, `setup.md` | Uso local, critérios de checagem, fontes e evidências |
| `.codex/config.toml` | Context7 local, somente se não existir equivalente e houver suporte confirmado |
| `outputs/toolkit-setup/02-matriz-de-cobertura.md` | Estado final por componente, evidência e próximo gatilho |
| `outputs/documentacao-software/README.md` | Versão editorial 0.4 e registro da manutenção; escopo funcional preservado |

Backups e ensaios ficam em `work/toolkit-setup/`. Essas pastas não entram no pacote. Fontes externas do toolkit e fixtures de avaliação ficam fora da raiz do projeto. Não copiar caches de plugins, credenciais ou configuração global para outputs.

## T1 · Preservar baseline e registrar o escopo efetivo

**Files:** criar `work/toolkit-setup/baseline.json`, backups explícitos e `outputs/toolkit-setup/setup.md`.

**Depends-on:** aprovação do plano e definição do método de execução.

**Interfaces:** produzir baseline com caminhos relativos, SHA-256, versão do toolkit, comandos observados e lista de arquivos pertencentes à tarefa. Dados técnicos locais sensíveis permanecem em work; relatório compartilhável usa apenas versões e caminhos relativos.

- [x] Revalidar árvore, instruções locais e revisão do checkout do toolkit; não presumir que o estado continua igual ao diagnóstico anterior.
- [x] Fazer backup de AGENTS, scripts de manutenção, índice e artefatos atuais; se houver configuração local, inspecionar apenas campos relevantes e preservar backup privado sem copiar segredos para outputs.
- [x] Verificar links, bytes/hashes legais e conteúdo do ZIP v0.3 somente por leitura. Registrar a saída e o código de retorno; não reescrever manifesto.
- [x] Registrar no setup o estado inicial, o desenho aprovado, os nove destinos e a revisão fixada. Falhas anteriores à tarefa ficam separadas de falhas introduzidas.

**Aceite:** os arquivos preservados têm os mesmos hashes da baseline. Nenhum conteúdo de snapshot legal mudou. Existe rota de restauração por arquivo; não há operação de limpeza ampla ou Git implícito.

## T2 · Criar checagem portátil e corrigir o regenerador

**Files:** criar `scripts/documentacao.py`, `tests/test_documentacao.py` e `outputs/documentacao-software/manifesto-documentacao.json`; modificar `work/finalizar_documentacao.py`.

**Depends-on:** T1.

**Interfaces produzidas em `scripts/documentacao.py`:**

- `check_project(root: Path) -> list[str]`: lista vazia para fontes válidas; diagnósticos com caminhos relativos para erros. Sem escrita ou acesso de rede.
- `generate_project(root: Path) -> Path`: valida antes de escrever; gera consolidado e ZIP e devolve caminho do ZIP; erro de validação gera `ValueError` e preserva artefatos anteriores.
- `main(argv: Sequence[str] | None = None) -> int`: CLI com `--check` e `--root`; ausência de `--check` gera. Exit 0 para sucesso e 1 para falha de validação.
- Entrada antiga encaminha argumentos usando `runpy.run_path` para `scripts/documentacao.py`; mantém código de saída e raiz determinada pelo script canônico.

- [x] Escrever testes primeiro com `TemporaryDirectory`: `test_relocated_project_and_unrelated_cwd`, `test_check_does_not_write`, `test_missing_required_rf_fails`, `test_missing_required_rn_fails`, `test_new_contiguous_chapter_is_accepted`, `test_missing_required_chapter_fails`, `test_broken_local_link_fails`, `test_legal_checksum_mismatch_fails` e `test_manifest_escape_is_rejected`.
- [x] Conferir assertions centrais: fixture válida retorna `[]`; alteração de snapshot retorna erro que menciona o caminho; remoção de RF-23 falha; capítulo 13 contíguo é aceito; hashes e árvore antes/depois de `--check` são iguais.
- [x] Executar `python -m unittest discover -s tests -p "test_*.py" -v` e observar a falha inicial esperada pela implementação ausente. Não aceitar erro de importação não investigado como prova de reprodução do defeito de portabilidade.
- [x] Implementar as interfaces. Manifesto documental lista capítulos mínimos 01–12 e IDs RF-01 a RF-23/RN-01 a RN-20; capítulos adicionais contíguos são descobertos por nome. O script não depende das contagens 13, 14 ou 31. Requisitos novos exigem atualização editorial intencional do manifesto.
- [x] Validar UTF-8, links locais pertinentes, cercas de código, JSON, requisitos e manifesto legal. Não validar exemplos de links dentro de blocos de código como destinos reais. Rejeitar escapes de caminhos nos manifestos. Não seguir links de rede durante check.
- [x] Preparar conteúdo de saída antes da publicação; usar escrita temporária/substituição por arquivo para evitar arquivos truncados. Se houver interrupção entre consolidado/ZIP, a checagem de artefatos em T6 detecta a inconsistência; não prometer atomicidade do par.
- [x] Reexecutar os testes e `python work/finalizar_documentacao.py --check`. Resultado esperado: exit 0 com resumo das verificações efetivas; sem escrita em fontes ou artefatos.

**Aceite:** os testes provam os defeitos e falhas relevantes; ambos os pontos de entrada funcionam de outro diretório. Sem instalação de framework de testes ou dependência de aplicação.

## T3 · Conciliar instruções, mapa e comandos

**Files:** criar README, CLAUDE, document-map.json, onboarding e quality; modificar AGENTS e setup. Preservar LEIS e capítulos canônicos.

**Depends-on:** T2, que fornece comandos verificáveis.

**Interfaces consumidas:** `python work/finalizar_documentacao.py --check`, comando sem flag para geração e suíte unittest. Mapear exatamente as nove chaves do manifesto upstream para arquivos existentes ou complementos aprovados.

- [x] Criar entrada da raiz com estado real: documentação e setup; app, banco e servidor ainda ausentes. Apontar para índice canônico e comandos implementados.
- [x] Enxugar AGENTS preservando a obrigação de ler LEIS e capítulo 12. Adicionar comandos, fontes canônicas, uso proporcional das skills, Ponytail full e limites de autorização. Não copiar o template inteiro nem exigir nova stack/branch.
- [x] Criar CLAUDE como import mínimo de AGENTS, sem alegar que Claude foi instalado/testado.
- [x] Preencher mapa dos nove destinos e onboarding. Registrar Python mínimo 3.11 para `tomllib` se usado, sem alterar o runtime já instalado. Sem comandos falsos `npm run dev/build`.
- [x] Registrar em quality a invocação versionada dos prompts 13–15 e o protocolo de relatório de segurança privado; não copiar todo o toolkit. Distinguir critérios futuros do produto dos checks atuais do setup.
- [x] Executar checagem de links/estrutura com o comando de T2; mapear documentação nova no coletor. Não deixar placeholders de template ou fontes duplicadas de regras.

**Aceite:** novo leitor encontra instruções, fonte de requisitos, arquitetura proposta e comando real sem precisar do histórico da conversa. As nove chaves do mapa têm destino existente. As obrigações legais locais não foram enfraquecidas.

## T4 · Configurar ferramentas compatíveis, sem duplicação

**Files:** RTK.md; `.codex/config.toml` se aplicável; AGENTS e setup; matriz de cobertura. Skills locais/lockfile apenas se a avaliação justificar instalação.

**Depends-on:** T3; serializar com qualquer edição de AGENTS ou setup.

**Interfaces:** configuração TOML limitada a servidor Context7 e URL pública suportada; nenhuma chave, cookie, modelo, provider, permissão ou nova autenticação gravados no projeto. RTK usa o binário observado, não comandos presumidos do guia.

- [x] Ler a skill openai-docs e verificar a documentação oficial de configuração local/trust do cliente. Reinspecionar catálogo de ferramentas e configuração relevante antes de adicionar servidor. Se já existir conexão equivalente, reutilizar.
- [x] Após backup, repetir `rtk init --codex --dry-run`; se efeitos continuarem limitados aos arquivos aprovados, executar `rtk init --codex`, revisar diferenças e conciliar AGENTS. Ler integralmente RTK.md produzido antes de adotar suas orientações.
- [x] Testar um comando RTK suportado e seguro pelo `--help` atual; usar o checkout externo conhecido como alvo se o comando precisar de Git. Comparar saída resumida/original sem executar uma mutação duas vezes. Registrar hook como não observado se o cliente não expuser a reescrita.
- [x] Configurar Context7 no escopo do projeto quando suportado e ausente. Validar sintaxe com `tomllib`. Confirmar descoberta quando o host permitir e fazer uma consulta pública focada em Python `pathlib`, usando identificador realmente retornado por resolve-library-id.
- [x] Se trust, reinício, autenticação ou limite externo impedir a consulta, registrar causa e intervenção exata; usar fonte oficial como fallback. Nenhum registro “funcional” somente por arquivo presente; não alterar config global para contornar a restrição.
- [x] Avaliar writing-guidelines/find-skills contra skills já disponíveis. Instalar localmente apenas uma lacuna concreta, por mecanismo suportado, com origem, revisão e licença; se não houver lacuna, registrar equivalência. Não duplicar Supabase/Vercel globais ou instalar conjunto para app inexistente.
- [x] Fechar cada uma das 23 linhas da matriz com ação efetiva, evidência ou gatilho de reavaliação. Manter Graphify/Obsidian/Next/shadcn/Sentry/CI no status justificado pelo desenho.

**Aceite:** não há wrappers, skills ou servidores duplicados; configurações não incluem segredos nem mudança de permissões. Recursos que não podem ser observados permanecem explicitamente pendentes, sem bloquear trabalhos independentes.

## T5 · Exercitar o método nativo de avaliação

**Files:** `outputs/toolkit-setup/avaliacao-harness.md`, quality e setup; fixtures e relatórios de teste em diretório dedicado fora do projeto e do toolkit.

**Depends-on:** T3/T4. Ler fixtures/avaliador antes de executá-los; verificar hash/revisão. Revisores não escrevem na fixture original.

**Interfaces:** avaliador upstream `node scripts/validate-harness.mjs <copia-descartavel>`; API da fixture `canReadRecord(actor, record)` permanece inalterada. Fonte e avaliador do commit fixado ficam fora do conjunto de arquivos editáveis dos trabalhadores.

- [x] Criar cópias descartáveis separadas para boundary fix, handoff obsoleto e revisão somente leitura; nunca copiar credenciais ou dados reais. Executar avaliador intacto primeiro; registrar testes efetivamente falhando, sem presumir o número pela narrativa do guia.
- [x] Executar tarefas por contextos nativos independentes quando disponíveis: corrigir conforme instruções locais, verificar uma alegação obsoleta e revisar sem editar, cada qual com arquivos permitidos e limite de uma execução mais correção justificada.
- [x] Rerodar o mesmo avaliador, comparar hashes de instruções/notas e verificar relatório de revisão. Fix exige os sete testes verdes; revisão read-only exige hashes da fixture inalterados e cenário concreto validado pelo coordenador.
- [x] Registrar descoberta de instruções, comandos e skills num contexto limpo quando observável. Não considerar subagente como reinício do aplicativo. Se pausa/retomada real não puder ser exercitada, marcar não executado.
- [x] Para a melhoria candidata de manutenção, usar fixture idêntica relocada e avaliador externo que primeiro inspeciona a raiz alvo por AST. A baseline antiga deve ser rejeitada por apontar para fora da cópia; não executá-la, pois o caminho fixo alcançaria o projeto original. O candidato de T2 deve passar no mesmo critério de isolamento e, então, nos checks de links/hashes da cópia. Registrar “baseline rejeitada no preflight”, sem alegar falha runtime que não foi executada. Uma comparação candidata; não iniciar novas rodadas sem falha nova que as justifique.
- [x] Registrar modo “adaptação nativa inspirada no Harness2”, comandos, inputs, observações e limitações. Sem framework oficial, APIs, benchmark pago ou atribuição de melhorias estatísticas.

**Aceite:** resultados pass/fail/não executado distinguem testes de script e comportamento do agente. Falha de requisito observado será corrigida dentro do escopo ou explicitamente encaminhada; não inventar observação faltante.

## T6 · Empacotar uma entrega autossuficiente e reproduzível

**Files:** script/testes de T2; índice editorial; consolidado; novo `outputs/documentacao-software-v0.4.zip`; setup e quality. Não sobrescrever ZIP v0.3 após iniciar a versão 0.4.

**Depends-on:** T2–T5.

**Interfaces:** pacote inclui fontes canônicas, LEIS, instruções, mapa, documentação de uso, gerador e seus testes. Inclusão por lista explícita/diretórios conhecidos; nunca compactar toda a raiz ou todos os arquivos ocultos.

- [x] Adicionar testes `test_archive_contains_maintenance_dependencies`, `test_archive_excludes_private_state`, `test_extracted_package_validates`, `test_generation_is_repeatable` e `test_invalid_sources_preserve_previous_outputs`.
- [x] Assert pacote inclui `scripts/documentacao.py`, `work/finalizar_documentacao.py` e demais fontes necessárias; não inclui backups, trials, caches, `.git`, configuração global ou arquivos de segredo. Configuração MCP não é necessária para regenerar documentos e fica fora do ZIP; documentar a exclusão.
- [x] Atualizar índice para versão 0.4 em 22/10/2026 com mudança restrita à manutenção/setup. Ler versão e data da fonte editorial; remover data fixa de 21/10/2026 do gerador. Requisitos funcionais e snapshots legais não mudam.
- [x] Executar `python -m unittest discover -s tests -p "test_*.py" -v`, `python work/finalizar_documentacao.py --check` e `python work/finalizar_documentacao.py`.
- [x] Extrair o ZIP em diretório temporário com espaços/acentos; executar nele `python work/finalizar_documentacao.py --check` e a suíte incluída. Validar entradas/CRC e comparação de conteúdo com fontes locais.
- [x] Repetir geração com os mesmos inputs: inventário e bytes finais idênticos. Usar metadados estáveis por entrada ZIP e ordenação explícita para o teste de repetibilidade, sem declarar que todo setup é automaticamente idempotente.
- [x] Alterar uma fonte sintética para inválida e comprovar que a geração falha antes de substituir outputs válidos. O validador checa existência e conteúdo canônico dos artefatos quando estes existem; mensagem distingue artefato desatualizado de fonte inválida para permitir regeneração intencional.

**Aceite:** pacote extraído passa na checagem/testes sem depender do caminho original, toolkit externo, rede ou ambiente global do agente. Os mesmos 13 snapshots legais permanecem byte a byte iguais à baseline.

## T7 · Revisar, verificar reaplicação e entregar evidências

**Files:** setup, quality, matriz, avaliação e notas da tarefa. Achados podem voltar aos arquivos responsáveis das tarefas anteriores.

**Depends-on:** T6.

**Interfaces:** inventário dos arquivos antes/depois, hashes de configurações e comandos de teste de T2/T6; revisão restrita ao conjunto efetivamente alterado, sem range Git inventado.

- [x] Enviar a revisor independente somente leitura o desenho, plano, snapshots iniciais, arquivos finais e critérios. Cobertura: comandos portáteis, pacote, falsos status de integração, preservação legal, segredos e conflitos de instruções. Confirmar achados antes de corrigi-los.
- [x] Aplicar correções necessárias e repetir apenas os checks afetados. Preservar autoria de escrita; não assumir arquivos enquanto um trabalhador ainda os altera.
- [x] Verificar reaplicação em cópia descartável: uma seção por assunto, uma entrada Context7 quando configurada, nenhuma skill/hook duplicada e preservação de notas personalizadas. Não reinstalar plugins ou repetir autenticação para provar idempotência.
- [x] Atualizar matriz/setup com fontes, versões, escopo e resultados. Toda pendência externa identifica causa, intervenção do usuário e teste que comprovará sua resolução.
- [x] Rodar a checagem e geração finais após atualizar evidências, repetir smoke do pacote e registrar hash final. Rever se há referências quebradas ou caminho pessoal em arquivos compartilháveis.
- [x] Entregar links para onboarding, relatório e pacote; listar comandos efetivos e próxima ação útil. Não declarar produto, banco, reunião ou integração pendente como implementados.

**Aceite:** achados relevantes resolvidos ou encaminhados com motivo; checks disponíveis passam; não há instalação global, publicação, mensagens ou mudanças de permissão. Intervenção externa não impede fechar as tarefas locais independentes.

## Ordem e método de execução

Sequência: **T1 → T2 → T3 → T4 → T5 → T6 → T7**. Dependências e arquivos compartilhados favorecem execução nativa pelo agente principal. Usar subagentes para os casos independentes de avaliação e para a revisão final, mantendo uma única autoridade sobre configuração e artefatos. É possível escolher execução dirigida por subagentes na revisão do plano; as mesmas fronteiras e checks continuam valendo.

Sem Git, “frequent commits” do modelo da skill é substituído por checkpoints verificáveis e backups por tarefa. A restrição específica do projeto prevalece sobre o exemplo genérico de commits.

## Auto-revisão do plano

Cobertura conferida: nove destinos (T3), 23 componentes (T4/T7), portabilidade e requisitos (T2), ferramentas (T4), avaliação nativa (T5), distribuição e recuperação (T1/T6), revisão e manutenção (T7). As cinco classes de risco em Review Focus têm testes ou observação prevista nas tarefas responsáveis.

Interfaces de T2 são únicas e consumidas por T3/T6/T7; não há API de aplicativo criada. As observações de T4/T5 que dependem do cliente não são substituídas por asserções estáticas. Este plano não exige acesso a banco, produção ou credenciais e não altera o escopo funcional do produto.

## Revisão do usuário

Desenho, plano e execução nativa aprovados pelo usuário. Execução realizada com executing-plans e revisão independente ao final. Resultado, correções e pendências externas estão no setup; não há nova aprovação de etapas já autorizadas.
