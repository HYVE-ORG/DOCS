# 06 · API e eventos propostos

Implementação parcial em25/10/2026: rotas reais sob `/api/central` documentadas
no [guia de trabalho online](../software-mvp/docs/central-work.md). Usam sessão
central HttpOnly, mutações tipadas e JWT do usuário no provedor. Os prefixos e
eventos abaixo continuam como intenção arquitetural para evolução futura.

Contratos de intenção para a expansão de gestão integrada constam no [capítulo 13](13-gestao-integrada-e-expansao.md). O prefixo futuro `/api/v1/studios/:studioId` não documenta endpoints disponíveis hoje. Autorização, idempotência, controle de versão, paginação e eventos pós-persistência deverão ser definidos e testados por incremento.

## 1. Convenções

Base `/v1`. Rotas abaixo são propostas para implementação, não endpoints em funcionamento. OpenAPI executável será gerada e validada a partir dos DTOs/controllers na implementação. JSON em UTF-8; instantes RFC 3339 UTC; datas civis `YYYY-MM-DD`; UUIDs para identificadores. Autenticação via `Authorization: Bearer <access_token>` emitido pelo Supabase Auth. Nunca enviar refresh token para endpoints de domínio.

Todas as rotas organizacionais começam em `/v1/organizations/:orgId`. Referências a projeto, arquivo ou usuário são verificadas nessa organização e no escopo real. Retornar 404 para recurso inexistente/inacessível, 401 para autenticação inválida e 403 para operação proibida em recurso que o usuário já pode conhecer.

Listas usam `cursor` opaco e `limit` proposto de 30, máximo 100. Resposta: `{ data: [...], page: { nextCursor, hasMore } }`. Ordem inclui desempate por ID. Filtros aceitos são documentados por endpoint e desconhecidos são rejeitados. Limites e rate limiting retornam 429 com orientação de retry.

## 2. Catálogo de operações

Prefixo organizacional omitido na tabela, exceto onde indicado.

| Área | Operações propostas |
|---|---|
| Identidade | `GET /v1/me`; `PATCH /v1/me`; `GET /v1/me/organizations`; recuperação/credenciais pelo provedor |
| Servidor | `GET /settings`; `PATCH /settings` apenas Admin, com nome/descrição/imagem; nenhum acesso ao host |
| Convites | `POST /invitations`; `GET /invitations` para admins; `DELETE /invitations/:id`; `POST /v1/invitations/accept` com token no body |
| Membros e perfis | `GET /members`; `GET /members/:userId/profile`; `PATCH /members/:userId`; `PATCH /members/:userId/role`; `POST /members/:userId/suspend`; `DELETE /members/:userId` remove associação local, apenas Admin |
| Workspaces | `GET/POST /workspaces`; `GET/PATCH /workspaces/:id`; `POST /workspaces/:id/archive`; `POST /workspaces/:id/restore`; `GET/POST /workspaces/:id/members`; `DELETE /workspaces/:id/members/:userId` |
| Projetos | `GET/POST /workspaces/:id/projects`; `GET/PATCH /projects/:id`; `POST /projects/:id/archive`; `POST /projects/:id/restore`; `GET/POST /projects/:id/members`; `PATCH/DELETE /projects/:id/members/:userId` |
| Tarefas | `GET/POST /projects/:id/tasks`; `GET/PATCH /tasks/:id`; `POST /tasks/:id/move`; `POST /tasks/:id/archive`; `GET /my-tasks`; `GET /tasks/:id/events` |
| Checklist | `POST /tasks/:id/checklist`; `PATCH/DELETE /tasks/:id/checklist/:itemId` |
| Etiquetas | `GET/POST /projects/:id/labels`; `PATCH/DELETE /projects/:id/labels/:labelId` |
| Comentários | `GET/POST /tasks/:id/comments`; `PATCH/DELETE /tasks/:id/comments/:commentId` |
| Chat | `GET/POST /conversations`; `POST /conversations/direct`; `GET/PATCH /conversations/:id`; `POST /conversations/:id/archive`; `GET /projects/:id/conversations`; `GET /workspaces/:id/conversations`; `GET/POST /conversations/:id/messages`; `PATCH/DELETE /messages/:id`; `POST /conversations/:id/read` |
| Arquivos | `POST /files/upload-intents`; `POST /files/:id/complete`; `GET /files/:id/download`; `DELETE /files/:id`; `GET /projects/:id/files` |
| Pastas | `GET/POST /folders?scopeType=&scopeId=`; `PATCH /folders/:id`; `POST /folders/:id/archive`; `GET/POST /folders/:id/files`; `DELETE /folders/:id/files/:fileId` remove só vínculo |
| Agenda | `GET/POST /calendar/events`; `GET/PATCH/DELETE /calendar/events/:id`; `POST /calendar/events/:id/respond` |
| Reuniões | `GET /meetings`; `POST /projects/:id/meetings`; `POST /meetings/:id/join-token`; `POST /meetings/:id/end`; `POST /meetings/:id/participants/:userId/remove` |
| Docs | `GET/POST /projects/:id/documents`; `GET/PATCH /documents/:id`; `POST /documents/:id/archive`; `GET /documents/:id/revisions` |
| Notificações | `GET /notifications`; `POST /notifications/:id/read`; `POST /notifications/read-all`; `GET/PATCH /notification-preferences` |
| Métricas | `GET /projects/:id/report`; `GET /reports/overview`; `GET /reports/contributions?userId=&from=&to=&timezone=` |
| Busca | `GET /search?q=&type=&projectId=` |
| Suporte | `GET/POST /support/requests`; `GET/PATCH /support/requests/:id`; `GET/POST /support/agents`; `DELETE /support/agents/:userId` |
| Auditoria | `GET /audit-logs` para papéis administrativos autorizados, sem conteúdo privado |

Webhook de mídia é endpoint separado, por exemplo `POST /v1/webhooks/media`, sem autenticação de usuário e com assinatura/autenticidade verificadas conforme o SDK do provedor. Endpoints de liveness/readiness não expõem segredos ou conteúdo.

### Autorização das operações

RN-04 é a fonte de permissão por ação. Papel atual vem do domínio, não do corpo/JWT editável. `POST /invitations` aceita Coordenador, mas rejeita cargo superior a Usuário e destino fora do seu escopo. Somente Admin muda cargo, cadastro administrativo, suspensão/exclusão de associação e configurações do servidor. Proibir excluir/suspender/rebaixar último Admin, inclusive sob concorrência.

Criar/editar/delegar tarefas, criar/configurar canais/pastas e agendar/iniciar reuniões exige Admin ou Coordenador no escopo. Para Usuário, `/tasks/:id/move` aceita apenas tarefa atribuída e transição RN-05; PATCH de checklist só permite marcar/desmarcar `done` de item existente da própria tarefa, sem editar estrutura/título/prazo/responsáveis. PATCH de mensagem é do autor; DELETE admite autor ou moderador de RN-14 com motivo de moderação. `PATCH /v1/me` nunca aceita role/organização; perfil de colega retorna somente campos profissionais compartilháveis.

Admin pode ler todos os chats do próprio servidor pela mesma política de acesso; resposta identifica `accessMode: administrative` quando não participa e gera trilha de inspeção sem conteúdo. Esse modo não marca lidas em nome alheio, não envia mensagem nem insere associação. Coordenador/Usuário recebem só seus chats. Não permitir filtro `all=true` ou troca de orgId como atalho de autorização. Alterar destinatários de direto exige nova conversa.

Mensagem de áudio/imagem usa `kind` e anexos de Files disponíveis, sem URL externa arbitrária. Upload/download e organização de pastas usam a mesma checagem atual de escopo; Admin inspeciona anexos ligados a chats do próprio servidor, sem tornar buckets públicos. GET de atividade recente, se adotado, filtra autorização antes de paginação/agregação e respeita mensagem removida.

## 3. Exemplo de tarefa

`POST /v1/organizations/:orgId/projects/:projectId/tasks`

```json
{
  "title": "Criar proposta visual da campanha",
  "description": "Usar o briefing aprovado no documento do projeto.",
  "status": "todo",
  "priority": "high",
  "assigneeIds": ["<uuid-do-membro>"],
  "dueDate": "2026-11-05",
  "labelIds": []
}
```

Resposta 201 com representação canônica, `id`, `version: 1` e timestamps. Os valores entre `<...>` são ilustrativos, não UUIDs válidos para envio. DTO rejeita campos privilegiados como `organizationId`, `createdBy` e `completedAt` no corpo: são derivados do contexto e operação.

`POST /tasks/:id/move` recebe `status`, `beforeTaskId`/`afterTaskId` opcionais e `expectedVersion`. O servidor valida vizinhos, coluna e permissão e realiza atualização, registro de evento, primeira conclusão e outbox em uma transação. Falha de qualquer etapa não deve deixar conclusão parcial.

## 4. Concorrência e idempotência

PATCH de tarefa, projeto, evento e documento exige `expectedVersion`. Versão atual diferente retorna 409 `VERSION_CONFLICT` com versão atual e orientação para recarregar; cliente preserva rascunho. Não resolver documento concorrente por sobrescrita automática.

Criação de tarefas, mensagens, reuniões, eventos e suporte aceita `Idempotency-Key` obrigatória no cliente oficial. Janela proposta: 24h para mutações gerais; mensagem mantém `clientMessageId` único durável. Mesma chave/corpo retorna resultado anterior; chave reutilizada com corpo diferente retorna 409. Retry após timeout consulta/repete com a mesma chave. Checar autorização de novo antes de devolver resposta armazenada.

## 5. Fluxo de upload

1. Cliente solicita intenção com nome, tamanho, MIME, finalidade e destino existente autorizado. Arquivos de mensagens usam conversa como escopo antes da criação da mensagem.
2. API valida permissão/cota, cria reserva com escopo imutável e retorna mecanismo assinado de upload com validade proposta de 15 minutos.
3. Cliente transfere diretamente ao bucket privado, com progresso e cancelamento. Arquivos grandes usam fluxo retomável compatível com o provedor.
4. Cliente confirma; API verifica objeto, tamanho real, tipo detectado e vínculo. Publicação depende de aprovação do processamento/checagem de segurança, com estado `pending`, `checking`, `available`, `rejected` ou `deleted`.
5. Apenas arquivos `available` podem ser anexados/baixados. Rotina remove reservas vencidas e órfãos. Worker de inspeção e tipos permitidos precisam estar definidos antes do piloto.

Download exige checagem atual de acesso e retorna URL assinada de curta duração, proposta de 60 segundos. A revogação não elimina uma URL já emitida até sua expiração; não prometer bloqueio instantâneo de uma cópia já baixada. Vídeo exige testar range requests e expiração durante reprodução.

## 6. Formato de erro

```json
{
  "error": {
    "code": "VERSION_CONFLICT",
    "message": "Esta tarefa foi atualizada. Recarregue antes de salvar.",
    "requestId": "<id-de-correlacao>",
    "details": { "currentVersion": 8 }
  }
}
```

| HTTP | Exemplos de códigos |
|---|---|
| 400 | `INVALID_INPUT`, `INVALID_CURSOR` |
| 401 | `UNAUTHENTICATED`, `SESSION_EXPIRED` |
| 403 | `ACTION_FORBIDDEN`, `MEMBERSHIP_SUSPENDED` |
| 404 | `RESOURCE_NOT_FOUND` |
| 409 | `VERSION_CONFLICT`, `IDEMPOTENCY_CONFLICT`, `LAST_ADMIN` |
| 413 | `FILE_TOO_LARGE` |
| 415 | `FILE_TYPE_NOT_ALLOWED` |
| 422 | `INVALID_TRANSITION`, `INACTIVE_ASSIGNEE` |
| 429 | `RATE_LIMITED`, `QUOTA_EXCEEDED` |
| 503 | `MEDIA_UNAVAILABLE`, `DEPENDENCY_UNAVAILABLE` |

Nunca retornar stack trace, SQL, tokens ou existência de recurso privado em mensagem de erro.

## 7. Socket e eventos

Handshake autenticado; token em campo de autenticação, não em query de URL que possa ir a logs. Salas são calculadas no servidor: usuário, workspace, projeto e conversa. Pedir assinatura de um ID não prova permissão. Revalidar em assinatura, renovação e alteração de acesso; desconectar/remove rooms após suspensão. Presença expira sem heartbeat.

Envelope proposto:

```json
{
  "eventId": "<uuid>",
  "type": "task.updated",
  "organizationId": "<uuid>",
  "resourceId": "<uuid>",
  "resourceVersion": 8,
  "occurredAt": "2026-10-21T18:00:00Z",
  "data": { "changedFields": ["status"] }
}
```

Eventos: `task.created`, `task.updated`, `task.completed`, `task.reopened`, `message.created`, `message.updated`, `message.deleted`, `file.available`, `document.updated`, `calendar.updated`, `notification.created`, `membership.changed` e `meeting.ended`.

Entrega pode repetir; consumidor deduplica por `eventId`. Evento anterior à versão local é ignorado. Se houver lacuna, reconectar ou suspeita de perda, refazer consulta canônica; a API não promete replay universal de todo evento. Payload só contém o mínimo necessário e passa por autorização na entrega, inclusive no worker da outbox.

## 8. Extensões: perfil, `/`, `@` e Inbox

Prefixo organizacional continua obrigatório; as operações abaixo são propostas de contrato, sem endpoints implementados.

| Operação | Contrato e autorização |
|---|---|
| `GET /chat-commands?conversationId=` | Catálogo permitido por cargo e contexto; sem revelar comandos/recursos internos não autorizados |
| `POST /chat-commands/execute` | commandId de allowlist, argumentos tipados e conversationId; checar participação/ação; retorna resultado privado ou recurso autorizado. Mutação reutiliza serviço, confirmação e Idempotency-Key; não aceita shell/código livre |
| `GET /mention-candidates?conversationId=&q=` | Somente pessoas/grupos elegíveis; limite/paginação/rate limit. Em comentário, usar contexto autorizado de taskId em vez de conversa, rejeitando contextos ambíguos |
| `POST /conversations/:id/messages`; `PATCH /messages/:id` | Campos estruturados de menção com userIds ou groupKey reservado; validar cargo do remetente e acesso dos destinatários no envio; texto com @ sozinho não concede acesso nem dispara alertas |
| `POST /tasks/:id/comments`; `PATCH /tasks/:id/comments/:commentId` | Mesmo formato de menções autorizado no projeto, com origem de comentário distinta; editar só como autor, mantendo destinatários e deduplicação por origem/pessoa |
| `GET /members/:userId/profile` | Perfil interno de membro visível no mesmo servidor; cargo profissional separado do role; nunca credenciais |
| `GET/PATCH /members/me/profile` | Editar próprios handle/bio/foto/capa/localização/cargo profissional com expectedVersion; não admite role/status ou identidade alheia |
| `GET /members/:userId/summary?from=&to=&timezone=` | Mapa/total filtrados e streak atual/melhor, com escopo, período, timezone do perfil observado e updatedAt; não agrega projetos fora da interseção de acesso de titular/observador |
| `GET /notifications?read=&type=&cursor=` | Inbox exclusivamente do próprio destinatário; totais/badge só de itens ainda autorizados |
| `GET /notifications/unread-count` | Mesmo filtro de acesso da lista; nunca contador bruto de itens inacessíveis |
| `POST /notifications/:id/unread` | Reabre como não lida somente notificação própria ainda acessível |
| `POST /notifications/read-all` | Recebe corte retornado pela consulta; não marca notificações posteriores nem permite escolher recipientId |

`POST /notifications/:id/read` continua pessoal. Ler/alterar Inbox alheia é negado inclusive para Admin. `GET/PATCH /notification-preferences` só altera o próprio destinatário; avisos essenciais de segurança não são silenciados como alertas opcionais. Acesso a chat por inspeção administrativa não libera Inbox do participante.

PATCH /v1/me mantém nome/timezone e preferências de conta; apresentação específica do servidor usa members/me/profile. Handle normalizado duplicado retorna 409 `HANDLE_TAKEN`; nome reservado/formato inválido retorna 400 `INVALID_HANDLE`. Arquivos de perfil são uploads internos com destino organização/usuário, inspecionados antes de vincular. Nenhum texto de bio/localização é interpretado como HTML, comando ou menção notificável.

Em summary, timezone opcional deve coincidir com o timezone informado do perfil observado para comparação com foguinho; rejeitar divergência ou orientar alteração pela preferência própria. O servidor informa que o foguinho usa histórico completo elegível enquanto mapa/total seguem o intervalo. A consulta de reports/contributions para perfil usa a mesma fonte/regra, sem contagem paralela. Sem usuário/escopo autorizado, resposta genérica, sem revelar totais de projetos privados.

Edição de mensagem ou comentário calcula destinatários novos/removidos na mesma transação, com outbox e deduplicação por tipo/ID de origem/pessoa; não renotifica todos a cada edição. Expansão coletiva por Coordenador exclui Admins inclusive em @todos, e o servidor revalida isso sem confiar na prévia do cliente. Não ampliar destinatários antigos quando alguém muda de cargo posteriormente. Eventos adicionais propostos: `profile.updated`, `notification.read-state-changed` e `notification.visibility-changed`, enviados apenas a destinatários permitidos. Rebaixamento/perda de acesso invalida menus, sugestões, summary e Inbox em clientes conectados.

## Rotas efetivas da evolução local

`POST /api/register` cria somente conta. `GET /api/account` retorna identidade própria, Studios e convites pessoais; `POST /api/account/profile` atualiza os campos pessoais. `POST /api/studios/select` seleciona participação ativa. `GET /api/state` exige contexto de Studio.

`POST /api/invitations` cria convite autorizado; `POST /api/invitations/:id/respond` recebe `accept` ou `decline`; `POST /api/invitations/:id/revoke` revoga convite pendente; `GET /api/studio/invitations` lista somente convites no escopo gestor. `/api/setup` não cria Studios por HTTP público. O operador local usa comando com API parada. Socket invalida consultas sem transmitir conteúdo privado; mudança de Studio exige novo snapshot antes de exibir o contexto.

## API comercial implementada —26/10/2026

/api/central/billing oferece catálogo público, conta/recibos/solicitações
privados, checkout, conciliação, cancelamento e propostas privadas. Webhook
assinado persiste evento antes de processamento; o estado do provedor é conferido
antes de conceder cobertura. Criação ambígua não repete POST automaticamente.
Rotas, identidade, versão de preço e controles no
[contrato comercial](../software-mvp/docs/billing.md). Checkout indisponível.
