# Plataforma de trabalho colaborativo

**Documentação de produto e engenharia · versão 0.30 · 27 de outubro de 2026**

Versão0.30: [UX de navegação](../software-mvp/docs/navigation-team.md), com Spaces
acessíveis pelo nome, ações rápidas contextuais, abas endereçáveis e navegação mobile.

Versão0.29: [redesign do aplicativo](../software-mvp/docs/design-system.md), com
paleta neutra inspirada na landing, Home compacta, componentes consistentes e temas
claro/escuro/híbrido revisados.

Versão0.28: [painel do Space](../software-mvp/docs/spaces.md), com resumo,
conversas recentes, membros, documentos e abas de trabalho no contexto da área.

Versão0.27: sala de reunião como página navegável em #meeting/ID, com menu do
Forma, contexto do projeto e saída para Reuniões. Sem modal para a chamada.

Versão0.26: [criação e edição de Spaces](../software-mvp/docs/spaces.md), com
identidade, capa predefinida, membros, prévia e configuração por abas. Fluxo local
responsivo com persistência e controle de alterações concorrentes.

Versão0.25: [estrutura ampla de reunião](../software-mvp/docs/meeting-room.md),
com palco/grade, miniaturas, contexto lateral e chat/arquivos/tarefas/documentos
do projeto. Sem IA, gravação ou nova publicação do instalador.

Versão0.24: [refinamento das telas do aplicativo](03-experiencia-e-navegacao.md):
perfil com contexto e agenda, workspace com busca e indicadores, resumo do Studio
e controles da sala de reunião. Sem mudanças de permissões ou novas integrações.

Versão0.23: [nova landing do Forma](../software-mvp/docs/landing-page.md), inspirada
na composição visual Labrina, com identidade própria, animações GSAP e smooth
scroll. Produto, planos, rotas e download preservados; sem publicação remota.

Versão0.22: [sala real LiveKit no piloto local](../software-mvp/docs/meeting-room.md)
com participantes e transmissão real de áudio/vídeo. Acesso entre máquinas pela
internet e domínio de reuniões Supabase continuam pendentes; sem cobrança ativada.

Versão0.21: Reunir agora no ambiente local, sem agendamento, com convite e abertura
imediata da prévia. Videoconferência multipessoa continua dependente do serviço de mídia.

Versão0.20: [exportação de trabalho do Studio](../software-mvp/docs/studio-export.md)
por Admin atual, com paginação e limites, disponível mesmo após cobertura vencida.
Índice dos anexos incluído; bytes, Auth e finanças excluídos. Não é backup restaurável.

Preparação comercial aprovada: Essencial R$79/mês e Pro R$149/mês por Studio,
com propostas empresariais privadas editáveis por operadores. Catálogo, cobrança,
conciliação, provisionamento e cotas estão implementados; vendas desativadas até
os aceites externos. Guia: [assinaturas](../software-mvp/docs/billing.md).

Status: arquitetura de referência e requisitos do produto, com um MVP local chamado Forma em `outputs/software-mvp`. Público inicial: equipe do criador. React/NestJS e JSON local permanecem preservados. A prévia online tem contas, convites, áreas, projetos, tarefas, chats, documentos e arquivos privados no Supabase separado. A integração ainda exige teste com conta real; mídia remota não está pronta. Veja o [relatório da beta](../software-mvp/docs/beta-status-report.md) e o [trabalho online](../software-mvp/docs/central-work.md).

## A ideia central

Um espaço especializado para trabalhar em equipe: organizar projetos e tarefas, conversar, reunir-se por áudio e vídeo, compartilhar materiais e acompanhar entregas sem perder o contexto do trabalho. Design, marketing, desenvolvimento e RH podem ter espaços próprios, preservando uma visão pessoal do que cada usuário precisa fazer.

## Como ler

| Documento | O que resolve |
|---|---|
| [01 — Visão e escopo](01-visao-e-escopo.md) | Problema, público, objetivos, premissas e limites do primeiro lançamento |
| [02 — Requisitos e regras](02-requisitos-e-regras.md) | Funcionalidades identificadas, permissões, regras e critérios de aceite |
| [03 — Experiência e navegação](03-experiencia-e-navegacao.md) | Páginas, jornadas e interpretação da referência visual |
| [04 — Arquitetura e decisões](04-arquitetura-e-decisoes.md) | React, Electron, NestJS, Docker, Supabase e reuniões |
| [05 — Modelo de dados](05-modelo-de-dados.md) | Entidades, relações, integridade, acesso e índices |
| [06 — API e eventos](06-api-e-eventos.md) | Operações propostas, erros, concorrência e tempo real |
| [07 — Segurança e privacidade](07-seguranca-e-privacidade.md) | Autorização, sessões, arquivos, desktop e dados sensíveis |
| [08 — Qualidade e operação](08-qualidade-e-operacao.md) | Testes, ambientes, entrega, observabilidade e recuperação |
| [09 — Backlog e evolução](09-backlog-e-evolucao.md) | Épicos, dependências, fases e condições de lançamento |
| [10 — Guia de uso e suporte](10-guia-de-uso-e-suporte.md) | Manual previsto para usuários e administração |
| [11 — Decisões e fontes](11-decisoes-e-fontes.md) | O que está confirmado, o que é proposto e o que depende de decisão |
| [12 — Legislação e aplicabilidade](12-legislacao-e-aplicabilidade.md) | Recorte legal solicitado, controles, direitos, licenciamento e critérios de revisão |
| [13 — Gestão integrada e expansão](13-gestao-integrada-e-expansao.md) | Plano modular e estado real: primeiro incremento CRM/comercial entregue; demais módulos planejados |
| [14 — Aplicativo desktop](14-aplicativo-desktop.md) | Prévia portátil Windows: execução, dados, administração, segurança, pacote e limites |

As cópias das normas e fontes oficiais ficam no [inventário legal](../referencia-legal/README.md), com procedência e limitações registradas.

O [setup de desenvolvimento assistido](../toolkit-setup/setup.md) registra ferramentas, comandos e evidências reais. O pacote inclui gerador e testes para manutenção offline após extração.

O arquivo **DOCUMENTACAO-COMPLETA.md** reúne os documentos em sequência. Os arquivos separados são a fonte editorial; o consolidado é uma cópia de distribuição e deve ser regenerado após alterações.

## Convenções

- **Confirmado:** solicitado diretamente pelo usuário ou respondido nesta conversa.
- **Proposto:** definição concreta para tornar a versão inicial discutível e implementável; ainda sujeita a revisão.
- **Posterior:** fora do primeiro lançamento.
- **RF:** requisito funcional; **RN:** regra de negócio; **RNF:** requisito não funcional; **AC:** critério de aceite.

Datas usam o calendário local do usuário; instantes são armazenados em UTC. Nomes de rotas e campos técnicos estão em inglês; conteúdo do produto começa em português do Brasil. Números de capacidade e desempenho são metas propostas, não resultados medidos.

## Resumo das escolhas propostas

Aplicativo Electron para Windows com interface React e TypeScript; backend NestJS como autoridade das regras; Supabase para autenticação, PostgreSQL e armazenamento privado; Socket.IO para eventos da aplicação; LiveKit como candidato para áudio, vídeo e compartilhamento de tela; Docker para ambientes reproduzíveis dos serviços. Lançamento inicial por convite, online e para uma única equipe, com modelo de dados capaz de separar organizações.

## Controle de alterações

| Versão | Data | Alteração |
|---|---|---|
| 0.12 | 2026-10-23 | Revisão estrutural: prioridades para colaboração remota, builds por destino, exclusões de artefatos/segredos, instaladores via volume Docker de leitura e guias incluídos no ZIP documental |
| 0.13 | 2026-10-23 | Atualizador desktop manual/automático, feed local, manifesto assinado, preferência persistente e documentação operacional |
| 0.14 | 2026-10-24 | Preparação da beta: contrato de persistência injetável no backend, com JSON padrão preservado; sem ativação de banco central ou mídia remota |
| 0.15 | 2026-10-24 | Cloudflare: proxy e assets testados localmente, conexão do plugin verificada, restrição de custo zero e bloqueios de publicação documentados |
| 0.16 | 2026-10-24 | Botão de atualização no app0.2.1, projeto Supabase gratuito conectado, backend de verificação de identidade e relatório de bloqueios da beta |
| 0.11 | 2026-10-23 | Desktop sem landing, build separado do site e um único app por cargo; preparação local do Studio na mesma janela, sem atalho administrativo separado |
| 0.10 | 2026-10-23 | Instalador Windows NSIS e download direto público pela landing; instalação por usuário, atalhos e preservação do perfil |
| 0.9 | 2026-10-23 | Primeira entrega desktop Windows: runtime próprio, perfil separado, ferramenta administrativa local e pacote portátil; critérios e limites no capítulo 14 |
| 0.8 | 2026-10-23 | Primeiro incremento EP-15 no MVP: clientes por área, pipeline, propostas versionadas e conversão única para projeto/chat; limites e evidências no capítulo 13 |
| 0.7 | 2026-10-23 | Plano modular de gestão integrada: cobertura ERP/CRM/HRM/ATS, RF-30 a RF-41, RN-26 a RN-32, EP-15 a EP-22, dependências e aceites; sem implementação dos novos módulos |
| 0.1 | 2026-10-21 | Primeira especificação, baseada no pedido, imagem e confirmação de uso interno |
| 0.2 | 2026-10-21 | Nova referência visual: composição em recortes, evidências por região e tokens visuais iniciais |
| 0.3 | 2026-10-21 | Incorporação do recorte legal ctresb/leis, fontes oficiais, controles de privacidade e instruções locais |
| 0.4 | 2026-10-22 | Setup do toolkit, comandos portáteis de checagem/geração, testes e distribuição autossuficiente; escopo funcional preservado |
| 0.5 | 2026-10-22 | Cargos Admin/Coordenador/Usuário e matriz cumulativa; gestão do servidor e usuários, moderação, pastas, áudio/imagens, perfil e referências visuais de equipe/atividade/estados; contratos e critérios de segurança conciliados |
| 0.6 | 2026-10-22 | Comandos / e menções @ por hierarquia, Inbox pessoal, perfil com bio/handle/capa/localização/cargo profissional e resumo de tarefas com foguinho; duas novas referências visuais e critérios de autorização/contagem |

Cada alteração futura deve registrar motivação, requisitos afetados, impacto nos dados e critérios de validação. Uma decisão arquitetural substituída deve permanecer no histórico com referência à nova decisão.

Versão0.18 (2026-10-25): trabalho online com domínio relacional, RLS, Storage
privado, UI por contexto e revisões; base local/instalador preservados, ativação
do Vexo dependente do cadastro confirmado e aceites remotos ainda pendentes.
