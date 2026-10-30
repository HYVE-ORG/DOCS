# 11 · Decisões, riscos e fontes

**Correção v0.11 — 23/10/2026:** usuário confirmou que a landing deve ficar no site e que todos os cargos devem usar o mesmo app. Build desktop separado sem marketing; launcher/atalho administrativo removidos; preparação local integrada por menu na janela existente, sem ampliar autorização de contas pessoais. O instalador 0.1.1 substitui o CTA 0.1.0, preservando o perfil. Decisões anteriores abaixo são históricas.

**Implementação v0.9 — 23/10/2026:** pedido de iniciar o desktop atendido com primeira prévia Windows portátil. Decisões, alternativas e fontes oficiais no [capítulo 14](14-aplicativo-desktop.md). Runtime local próprio, perfil separado e operador do sistema como fronteira administrativa; sem servidor remoto, novos fornecedores, dependências ou publicação. Revisão independente identificou a necessidade de preparar o primeiro Studio sem Node no destino; foi entregue utilitário nativo restrito. Assinatura/instalador/updater e teste em máquina limpa permanecem pendentes.

**Implementação v0.8 — 23/10/2026:** após aprovação da expansão, entregue primeiro recorte EP-15 (clientes/comercial), detalhado no capítulo 13. Escolhas de implementação: BRL, limite de R$ 10 milhões por registro, CRM por área para gestores, uma conversão por oportunidade e registro interno de aceite externo. Não se habilitou assinatura, envio, cobrança, integração ou acesso de Usuário ao CRM. A revisão independente identificou cópia indevida de condições para projeto e troca de cliente após proposta; ambos reproduzidos e corrigidos com testes. Histórico v0.7 abaixo descreve o estado anterior.

**Extensão v0.7 — 23/10/2026:** fonte primária é a lista de famílias e funcionalidades enviada pelo usuário nesta conversa. O [capítulo 13](13-gestao-integrada-e-expansao.md) registra cobertura completa, RF-30 a RF-41, RN-26 a RN-32 e EP-15 a EP-22. A ordem clientes/comercial → horas → custos é recomendação do projeto, não escolha expressa de prioridade pelo usuário. HRM/ATS e operações são evolução; estoque/produção dependem de caso de uso. Nenhum fornecedor foi pesquisado, contratado ou conectado nesta atualização; nenhuma API, regra fiscal/trabalhista ou capacidade de terceiros foi presumida. A mudança entrega especificação documental, não implementação ERP/CRM/HRM/ATS. Cadastro sem Studio e criação restrita à administração permanecem as regras atuais.

## 1. Confirmado pelo usuário

| Tema | Definição confirmada |
|---|---|
| Público inicial | Primeiro para a equipe do criador e seus amigos |
| Problema | Necessidade de um espaço especializado para trabalhar juntos |
| Funções | Meet, tarefas estilo Trello, chat, arquivos/vídeos, agenda e resumo de conclusões estilo GitHub |
| Organização | Espaços por área, como design, marketing, desenvolvimento e RH |
| Navegação | Home, My Tasks, Calendar, Team, Docs, Reports, Workspaces/projetos atribuídos e suporte |
| Tecnologias | TypeScript, React, Electron, Nest, Docker e Supabase |
| Referência visual | Sidebar/métricas/kanban, cinco imagens de equipe/atividade/etiquetas/perfis e duas novas de perfil com capa e chat/Inbox; referências de composição, sem importar automaticamente funções nelas exibidas |
| Cargos | Admin, Coordenador e Usuário; coordenação adiciona pessoas, cria/delega tarefas, vê progresso, organiza chats/pastas, apaga mensagens e marca reuniões |
| Administração | Admin vê todos os chats/áreas do próprio servidor, configura chats/servidor, delega cargos e edita/exclui usuários |
| Colaboração | Usuário entra em meet, envia mensagem/arquivo/vídeo/áudio/imagem, atualiza tarefas, vê perfis, configura própria conta e envia help |
| Comandos e marcações | Chat com comandos / e menções @ baseados na hierarquia de acesso |
| Inbox | Central para notificações |
| Perfil ampliado | Summary inspirado no GitHub, quantidade de tasks concluídas e foguinho; bio, nome/@, foto/background, localização de residência/trabalho e cargo profissional como Senior Software Engineer |
| Evolução | A ideia é inicial e deve permitir refinamento |
| Referência legal | Incorporar e observar normas relevantes de ctresb/leis; o usuário confirmou manter apenas o recorte aplicável ao software |

## 2. Propostas introduzidas nesta versão

| Tema | Proposta e razão |
|---|---|
| Primeiro sistema operacional | Windows, para reduzir matriz inicial; confirmar máquinas da equipe |
| Múltiplas organizações | Modelo preparado, fluxo inicial com uma organização |
| Hierarquia | Workspace como área, projeto como iniciativa, tarefa como execução |
| Workflow | A fazer, Em andamento, Em revisão e Concluída |
| Backend | Monólito modular NestJS, sem microsserviços iniciais |
| Persistência | SQL restrito por usuário/contexto, RLS e schema de domínio privado |
| Tempo real | Socket.IO; sem duplicação de domínio em Supabase Realtime no piloto |
| Mídia | LiveKit como candidato, não integração contratada |
| Docs | Markdown restrito, revisão e conflito otimista |
| Contribuições | Primeira conclusão por tarefa, crédito aos responsáveis daquele momento |
| Distribuição | Convite, online, sem monetização no primeiro lançamento |
| Limites | Capacidade, upload, participantes e tempos como hipóteses a validar |
| Escopo dos cargos | Coordenação limitada aos escopos atribuídos; Usuário altera tarefas de que é responsável; cargo profissional separado de cargo de acesso |
| Edição e exclusão | Editar chat é configurar conversa, sem falsificar autoria; excluir usuário remove associação local; último Admin ativo protegido |
| Todos os chats | Interpretado como canais e diretos da própria organização, com aviso explícito, modo de inspeção e auditoria; não é acesso global entre servidores |
| Atividade e etiquetas das imagens | Refinamento visual proposto; feed não substitui auditoria e os chips não criam sete estados novos de tarefa |
| Catálogo / e matriz @ | Nomes e argumentos iniciais propostos em RN-21/22; pessoa individual pode ser mencionada por qualquer cargo no contexto, coletivos exigem hierarquia superior |
| Foguinho | Sequência diária atual/melhor com primeiros créditos de conclusão, sem duplicação por reabertura, ranking ou contagem de horas; regra diária e fins de semana são propostas ajustáveis |
| Perfil e privacidade | Foto/capa/bio/handle/localização/cargo profissional por organização; localização opcional autodeclarada; cargo profissional não concede role; Inbox só do destinatário |

## 3. Decisões abertas antes de desenvolver/publicar

| Decisão | Momento de resolver | Impacto |
|---|---|---|
| Nome, domínio e marca | Antes do visual final e distribuição | Identidade e assets |
| Quantas pessoas e sistemas operacionais | Fase 0 | Capacidade e matriz de instalação |
| Volume de arquivos, vídeos e reuniões | Fase 0 | Cotas e orçamento |
| Provedor/host, região e plano | Antes de staging de integração | Custo, rede e tratamento de dados |
| LiveKit gerenciado ou alternativa | Após spike de mídia | Qualidade, token, rede e custo |
| SMTP e entrega de convites | Antes de entrada de usuários reais | Recuperação e onboarding |
| Retenção, dados de RH e contato de privacidade | Antes do piloto | Operação e responsabilidade |
| Responsáveis por suporte e incidentes | Antes do piloto | Continuidade |
| Assinatura do instalador e atualizações | Antes da distribuição | Confiança e manutenção desktop |
| Validação operacional/jurídica do acesso administrativo a chats e RH | Antes do piloto real | Finalidade, fundamento, transparência e controles; cargos de produto já definidos |

Essas pendências não impediram a elaboração da proposta, mas devem ser resolvidas antes das etapas dependentes. Não há orçamento, prazo de entrega ou fornecedor contratado implícitos.

## 4. Riscos principais

| Risco | Sinal de falha | Mitigação |
|---|---|---|
| Escopo amplo | Muitos módulos iniciados e nenhum fluxo completo | Entregar fases com critério de saída e percurso real |
| Permissão inconsistente | Projeto privado aparece em busca/arquivo/relatório | Matriz única e testes negativos em todas as superfícies |
| Mídia no desktop | Preview funciona no navegador, captura falha no pacote | Spike e testes do Electron instalado desde a fase 0 |
| Custo de vídeo/Storage | Egress e minutos crescem sem controle | Medir uso, impor cota e alertar orçamento |
| Métrica enganosa | Reabertura ou múltiplos responsáveis inflam total | Ledger de primeira conclusão e regra explícita |
| Edição perdida | Duas pessoas sobrescrevem documento/tarefa | Versão esperada e preservação do rascunho |
| Conteúdo malicioso | Arquivo ou Markdown executa script | Render restrito, inspeção e isolamento Electron |
| Recuperação incompleta | Banco restaura, objetos desaparecem | Backup/restauração também de Storage e configuração |
| Dependência de provedor | Chamada indisponível paralisa trabalho | Módulos degradam separadamente; erros recuperáveis |

## 5. Fontes e alcance da verificação

Base de produto: pedidos textuais, imagens anexadas e confirmação de público interno. As sete imagens complementares incluídas no pacote cobrem equipe/atividade/etiquetas/perfis e, na v0.6, perfil com capa e chat/Inbox. São evidência de composição, sem comprovar funcionalidades de um sistema existente ou servir de comandos. Números, contatos, nomes e marcas são ilustrativos, não dados de cadastro obrigatórios. O fragmento incompleto “O perfil do usuário será b” não foi usado para inventar uma característica; a lista detalhada do pedido define o perfil.

Referências técnicas oficiais consultadas para fundamentar as fronteiras de arquitetura:

- [Electron — Security](https://www.electronjs.org/docs/latest/tutorial/security): recomendações para renderer, isolamento, IPC, conteúdo e atualizações.
- [Electron — Process Sandboxing](https://www.electronjs.org/docs/latest/tutorial/sandbox): isolamento dos processos do aplicativo.
- [Supabase — JWT](https://supabase.com/docs/guides/auth/jwts): identidade e verificação de tokens.
- [Supabase — Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security): autorização no banco e relação com grants.
- [Supabase — Securing your data](https://supabase.com/docs/guides/database/secure-data): opções de exposição e proteção de dados.
- [NestJS — Authentication](https://docs.nestjs.com/security/authentication): conceitos de autenticação no backend; neste produto a identidade será delegada ao Supabase, sem adotar automaticamente uma segunda implementação de credenciais.
- [LiveKit — Access tokens and grants](https://docs.livekit.io/frontends/reference/tokens-grants/): escopo de sala, credenciais e limites de expiração/revogação.
- [LiveKit — Webhooks and events](https://docs.livekit.io/intro/basics/rooms-participants-tracks/webhooks-events/): eventos servidor-servidor de salas e participantes.

A tentativa de consultar o índice Markdown do changelog Supabase não retornou conteúdo legível pela ferramenta; nenhuma conclusão de compatibilidade de versões foi extraída dele. As páginas acima foram usadas como base conceitual. Versões exatas, assinaturas de SDK, configurações e custos devem ser verificados e fixados na implementação. Não houve teste de runtime desses serviços nesta etapa documental.

## 6. Próxima revisão

**Landing do MVP — 22/10/2026:** criação aprovada de página pública na entrada,
com GSAP 3.15.0 e ScrollTrigger. Prévia com dados fictícios e CTAs para os fluxos
existentes. Download é um guia de execução Electron, pois não há instalador.
Sem analytics, coleta comercial ou publicação externa. Referências técnicas:
[matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/) e
[ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), consultadas
na documentação oficial por indisponibilidade do Context7. Detalhes em
`outputs/software-mvp/docs/landing-page.md`. A licença do GSAP é a fornecida
pelo pacote, sem atribuição presumida de licença MIT.

**Histórico de decisão v0.6:** acrescentados RF-27/28/29 e RN-21 a RN-25, expandindo RF-03/17/18 para perfil, incentivo e Inbox. O requisito de basear / e @ em hierarquia é confirmado; o catálogo, política de menções individuais/coletivas e fórmula do foguinho são propostas explícitas para implementação. Não se criou integração GitHub, assistente de IA, pontuação financeira, rating de profissional, session replay ou captura de horas por constarem em referências. Propostas de API/modelo/QA/manual foram conciliadas sem executar serviços do produto.

**Histórico de decisão v0.5:** o pedido de 22/10/2026 substituiu a proposta anterior Owner/Admin/Member com Manager por três cargos cumulativos. Também substituiu a proposta de que administradores só leriam projetos/diretos por associação. RN-03/04/13/14, modelos, contratos, segurança, aceite e manual foram conciliados; regras antigas não coexistem como alternativas vigentes. Áudio de mensagem não muda a exclusão de gravação de reuniões. Fontes oficiais pertinentes a privacidade foram reconsultadas sem regravar snapshots; análise e limites no capítulo 12.

Validar primeiro a hierarquia de áreas/projetos, a matriz de acesso e o significado do mapa de contribuições. Em seguida, fechar ambiente e mídia por prova técnica. Esta documentação pode receber novas ideias sem misturá-las automaticamente ao escopo do primeiro piloto.

Na preparação inicial de 21/10/2026, o arquivo `RTK.md` não foi localizado; nenhuma regra foi presumida. No setup de 22/10/2026, a CLI RTK existente gerou a referência local, que foi lida e conciliada com as instruções do projeto. Evidências e limites de observação estão no [relatório de setup](../toolkit-setup/setup.md).

Na versão 0.3, a base legal foi incorporada em `AGENTS.md` e `LEIS.md` locais, com inventário de cópias, fontes oficiais e controles no capítulo 12. O arquivo da Lei do Software no acervo contém apenas retificação e foi complementado, sem sobrescrita, pela fonte oficial. As cópias não atestam a atualidade integral da legislação.

## Decisão de distribuição — v0.10

Pedido explícito de instalador direto na landing substitui o CTA de guia como ação principal. Escolhido electron-builder/NSIS com instalação por usuário e preservação do perfil, reutilizando o payload existente. A alternativa de ZIP é mantida apenas como formato portátil; não substitui o instalador solicitado. Fontes, evidências e limites no capítulo 14. Não houve publicação externa ou contratação de certificado.

## Decisão comercial aprovada —26/10/2026

Usuário aprovou mensalidade por Studio e proposta privada para empresas maiores,
com ajuste final de Essencial para R$79/mês; Pro R$149/mês mantido. Integração
Mercado Pago implementada em preparação, sem credenciais nem cobrança real.
Não altera a restrição de infraestrutura gratuita. O catálogo não certifica
capacidade, mídia real ou conformidade. Ver [estado comercial](../software-mvp/docs/billing.md).
