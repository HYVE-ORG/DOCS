# 09 · Backlog, fases e evolução

As fases representam sequência de entrega e dependências, sem promessa de prazo. Estimativas exigem tamanho da equipe, disponibilidade, prova de mídia e ambiente escolhido. Já existe um MVP local em `outputs/software-mvp`; estas fases descrevem o alvo completo e não comprovam entrega de cada item. Os limites atuais estão no README do MVP.

A extensão de 23/10/2026 está no [capítulo 13](13-gestao-integrada-e-expansao.md): EP-15 a EP-22 e RF-30 a RF-41 cobrem gestão integrada. Primeiro recorte EP-15 já entregue no MVP, com limites e evidências na seção 9 do capítulo 13. Ordem subsequente proposta: horas → custos/orçamento → pessoas/ATS conforme demanda → integrações/operações. Demais incrementos permanecem planejados, fora do aceite P0 original, sem prazo prometido.

## 1. Épicos e histórias

| Épico | História representativa | Requisitos | Prioridade/dependência |
|---|---|---|---|
| EP-01 Identidade e acesso | Como Admin/Coordenador, adiciono colegas respeitando cargo e escopo | RF-01 a 03, RF-22, RF-26 | P0; base de todos |
| EP-02 Estrutura de trabalho | Como Admin/Coordenador, organizo áreas/projetos atribuídos e participantes | RF-04, RF-05, RF-19, RF-24 | P0; após identidade |
| EP-03 Execução | Como colaborador, vejo minhas tarefas e movo uma entrega até conclusão | RF-06 a 09 | P0; após projetos |
| EP-04 Comunicação | Como Usuário, participo de chats/envio mídia; como coordenação, crio canais e modero | RF-10, RF-18, RF-25 | P0; após associações; anexos após arquivos |
| EP-05 Materiais | Como designer, envio versões/vídeos/imagens/áudio e navego em pastas | RF-11, RF-12, RF-24, RF-25 | P0; após autorização |
| EP-06 Agenda e reunião | Como Admin/Coordenador, agendo revisão; como Usuário, respondo e entro em meet | RF-13, RF-14 | P0; spike de mídia antecipado |
| EP-07 Conhecimento | Como equipe, mantemos briefing e decisões no projeto | RF-15 | P0; após projetos |
| EP-08 Acompanhamento | Como membro, vejo entregas e resumo diário com números confiáveis | RF-16, RF-17 | P0; após histórico de tarefas |
| EP-09 Experiência integrada | Como usuário, encontro contexto nas páginas e na busca | RF-08, RF-19, RF-21 | P0; incrementa com módulos |
| EP-10 Operação e suporte | Como usuário, recupero acesso e consigo ajuda com protocolo | RF-02, RF-20, RF-22 | P0; requisito de lançamento |
| EP-11 Privacidade e direitos | Como titular, solicito acesso/correção e demais providências cabíveis por um canal seguro | RF-23, RN-19/20, JUR-01 a JUR-10 | P0; procedimento manual pode atender o piloto |
| EP-12 Perfil e incentivo | Como usuário, apresento nome/@, bio, foto/capa, localização/cargo profissional e acompanho minhas conclusões/foguinho | RF-03, RF-17, RF-29; RN-23/24 | P0; perfil após identidade, summary após créditos |
| EP-13 Comandos e menções | Como membro, uso atalhos e @ sem ultrapassar meu cargo/escopo | RF-27, RF-28; RN-21/22 | P0; após autorização, chat e ações de domínio |
| EP-14 Inbox | Como usuário, concentro alertas próprios, marco leitura e encontro o contexto autorizado | RF-18; RN-17/25 | P0; após outbox/notificações |

P0 significa necessário ao piloto completo. Não significa desenvolver todos os módulos ao mesmo tempo.

## 2. Sequência recomendada

### Fase 0 — Decisões e provas

Consolidar nomes e vocabulário, inventariar membros/arquivos, definir responsáveis operacionais e orçamento. Provar autenticação segura no Electron, contexto SQL com RLS e pool, vídeo/tela com oito participantes e uploads grandes. Registrar resultados, limites e arquitetura final. Saída: riscos críticos resolvidos e contratos fundamentais revisados.

### Fase 1 — Fundação de acesso

Criar monorepo e pipeline, configurar ambientes, identidade, convites, três cargos cumulativos, servidor, associações, auditoria e shell. Entrega verificável: cada cargo exercitado em escopos distintos, isolamento entre organizações, último Admin protegido, edição/exclusão de associações sem perder autoria. Não basta sidebar com páginas vazias.

### Fase 2 — Núcleo de execução

Implementar projetos, tarefas, kanban/lista, responsáveis, prazos, checklist, comentários, My Tasks e outbox. Entrega: mudança persistida e refletida entre dois clientes, incluindo conflito e reabertura. Começar eventos de conclusão nesta fase para preservar histórico desde o início.

### Fase 3 — Comunicação e materiais

Chat por escopo, diretos, criação/moderação por cargo, inspeção administrativa transparente, notificações, pastas, arquivos/vídeos/imagens/áudio e busca inicial. Entrega: envio persistido, retry idempotente, prévia/cancelamento de áudio, download privado e revogação em cliente conectado.

Nesta fase, acrescentar catálogo `/`, menções individuais/coletivas autorizadas e Inbox pessoal. Os atalhos só são liberados quando a ação real correspondente estiver pronta, sem botões ou comandos que simulem backend. Provar edição de menção, deduplicação e mudança de acesso com dois clientes.

### Fase 4 — Agenda, reuniões e documentos

Agenda interna, respostas, lembretes, sala com dispositivos e compartilhamento, documentos com revisões e conflito. Entrega: reunião a partir de projeto/evento, ata e tarefas vinculadas manualmente ao contexto.

### Fase 5 — Visibilidade e experiência

Home integrada, Team, Reports e mapa de contribuições; estados vazios/erro, atalhos e ajustes visuais. Entrega: indicadores comparados com consultas conhecidas e screenshots avaliadas nos tamanhos definidos.

Perfil ampliado inclui bio, nome/@, foto/capa, localização e cargo profissional. Summary/total/foguinho usam primeiras conclusões e o mesmo filtro autorizado, com sequência atual/melhor e timezone visíveis. Contadores fixos, horas e ratings vistos nas referências não substituem dados reais.

### Fase 6 — Piloto instalado

Suporte interno, segurança, acessibilidade, teste de carga, instalação e recuperação. Entrega: percurso completo por membros reais, backup restaurado e responsável por operação. Corrigir bloqueios do piloto antes de ampliar o público.

## 3. Rastreamento de aceite

Cada história deve guardar: RF/RN relacionados, descrição do comportamento, caminhos de erro, teste/evidência, migração associada, observação visual quando aplicável e estado. Estados do backlog: proposta, pronta para desenvolvimento, em andamento, em revisão, validada e entregue.

Exemplo: `EP-03 / Concluir tarefa` → RF-06/07/17 + RN-05/09/10 → teste de conclusão concorrente e reabertura → captura do quadro atualizado → validação de agregado. Uma história não está entregue quando só existe frontend com dados fictícios.

## 4. Critérios para liberar o piloto

- Convidar usuário real, aceitar e recuperar acesso.
- Restringir RH e outro projeto para Coordenador/Usuário sem atribuição, inclusive em busca/métricas/download; validar visão completa do Admin só no seu servidor e aviso de inspeção.
- Criar, atribuir, mover, reabrir e concluir tarefa com histórico correto.
- Conversar e compartilhar arquivo/vídeo/imagem/áudio entre dois clientes reais, com criação de chats/pastas e moderação por cargo.
- Agendar reunião, entrar, compartilhar tela e revogar participante.
- Salvar documento e resolver edição concorrente sem perda silenciosa.
- Conferir relatório e mapa contra dataset conhecido.
- Instalar em máquinas da equipe, com variáveis e endpoints de produção corretos.
- Ter backup testado, custo limitado, retenção aprovada e canal de suporte.
- Ter canal de privacidade e procedimento exercitado para direitos cabíveis, com responsáveis e fontes legais registrados.

## 5. Evolução após uso real

Priorizar com base no piloto: templates por área, workflow configurável, dependências entre tarefas, recorrência, busca avançada, integração com calendários, web independente, convidados limitados e aplicativo móvel. IA, gravação/transcrição e GitHub podem ser avaliados quando houver necessidade clara e política de dados adequada.

Comercialização futura acrescentará onboarding de organizações, políticas por tenant, billing, cotas comerciais, suporte externo, termos e operação compatível com esse público. O modelo com `organization_id` ajuda, mas não significa que o produto já esteja pronto para SaaS.

## Incremento desktop entregue — v0.9

Primeira execução Windows autônoma e pasta portátil concluídas: runtime próprio, perfil separado, inicialização/erro, menus e utilitário administrativo offline. Detalhes no [capítulo 14](14-aplicativo-desktop.md). Próximos incrementos: testes em Windows limpo, identidade nativa do executável, instalador/assinatura, atualização segura e conexão a backend compartilhado. Mídia remota, sincronização e evolução ERP continuam independentes deste shell.

## Incremento de distribuição entregue — v0.10

Instalador Windows NSIS e download direto na landing entregues, conforme capítulo 14. Instalador deixa de ser pendência da primeira entrega; assinatura, updater, instalação/desinstalação em Windows limpo e colaboração remota permanecem pendentes.
