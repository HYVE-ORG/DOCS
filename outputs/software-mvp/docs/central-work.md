# Trabalho online — incremento de 25/10/2026

Atualização26/10: Admin ativo pode baixar dados estruturados do Studio, com
histórico e índice de anexos, pelo botão Exportar dados. Não inclui Auth, finanças
ou bytes; [guia e limites](studio-export.md). Autorização verificada no banco
por página/final, inclusive com cobertura vencida. Não cria backup restaurável.

## Estado e acesso

O código em desenvolvimento amplia `#central` com áreas, projetos, tarefas,
conversas, documentos e arquivos no projeto Supabase Forma. O ambiente local
continua separado e não foi importado. O instalador0.2.1 não contém este incremento.
Abra http://127.0.0.1:5173/#central, cadastre e confirme a conta. O cadastro não
cria Studio. Em Meus Studios, Abrir Studio navega para `#central/studio/UUID`.

Vexo ainda não foi provisionado: o usuário confirmou em25/10 que vai cadastrar
o e-mail escolhido. A operação do primeiro Admin só pode ocorrer depois de
confirmar identidade, e-mail e sessão reais. Não criar usuário Auth por SQL,
usar senha provisória nem promover uma conta local como substituto.

## Fluxos implementados

- Admin cria áreas/projetos e concede acesso aos projetos. Coordenador gerencia
  trabalho no seu escopo; Usuário altera status das tarefas atribuídas a ele.
- Tarefas têm quadro com arrastar/soltar e seletor acessível, lista, calendário
  mensal, busca, filtro pessoal, responsáveis, prazo e prioridade. Carregamento
  em páginas de50; filtros atuam sobre as tarefas já carregadas. Animação de
  entrada respeita preferência de movimento reduzido.
- Canais pertencem à área ou ao projeto. Mensagens, edição, exclusão e anexos
  ficam no contexto escolhido. Há paginação de50 mensagens e atualização por
  consulta a cada12 segundos; não é entrega instantânea por Realtime.
- Documentos têm revisões e controle de versão. Conflito409 mantém o formulário
  e o rascunho. Histórico pode ser consultado sem sobrescrever a revisão atual.
- Arquivos privados podem ser enviados, baixados, visualizados e retirados.
  Código aparece como texto, sem executar HTML/JavaScript. Prévia de código
  limitada a500KiB/5.000 linhas; upload limitado a15MiB com tipos permitidos.
- Equipe tem20 membros por página. Aceitar convite de Studio não concede
  acesso automático a todos os projetos.

Comandos slash, menções/notificações de trabalho, reuniões, CRM, checklists e
demais recursos do MVP local ainda não foram portados para este domínio online.
Não existe migração automática nem sincronização do JSON com a base central.

## Implementação e contratos

Schema privado `forma`: workspaces/workspace_access, projects/project_access,
tasks/task_assignees, conversations/messages, documents/document_revisions,
files/message_attachments, work_requests e upload_verifiers. Chaves compostas
impedem associações entre Studios/projetos incompatíveis. RLS verifica vínculo,
cargo e sessão atuais; metadata editável pelo cliente não concede poderes.
Funções públicas são SECURITY INVOKER; helpers privilegiados são privados,
restritos e usados apenas nas verificações necessárias.

As migrações locais em `supabase/migrations` correspondem ao histórico remoto:
20261025003622 central_work, 20261025003938 central_work_actor_lock,
20261025004308 central_work_retry_scope, 20261025004630 central_storage_revocation
e20261025120209 central_work_navigation, após as quatro migrações de identidade.
Não editar migrações aplicadas: criar a próxima para qualquer mudança.

Backend: central-domain.ts, central-work.ts e central-work-controller.ts em
`apps/api/src`. Contratos em `packages/contracts/central-work.ts`; UI em
CentralStudio.tsx e OnlineTasks/Chat/Documents/Files. As chamadas usam sessão
central HttpOnly e JWT do usuário no provedor, sem service_role.

| Endpoint sob /api/central | Uso |
|---|---|
| GET studios/:id/work | Studio, áreas, projetos, canais e equipe autorizados |
| GET projects/:id/content?after=UUID | Tarefas paginadas, documentos e arquivos |
| GET conversations/:id/messages?before=UUID | Histórico e anexos autorizados |
| GET documents/:id?version=N | Documento atual ou revisão |
| POST studios/:id/actions | Mutação tipada com UUID de idempotência |
| POST studios/:id/files | Bytes, nome, escopo e requestId; reserva/inspeção/publicação |
| GET files/:id | Download autorizado, hash e Range |
| POST studios/:id/files/:id/delete | Retirada e tentativa verificada de limpeza |
| POST studios/:id/uploads/:requestId/cancel | Cancela a reserva/publicação |

Mutações validam DTO estrito. Retry com a mesma chave só aceita o mesmo conteúdo
e revalida acesso atual. Atualizações usam versão otimista, retornando409 em
conflito. Revogar um membro/projeto bloqueia novas leituras/mutações e objetos
retirados; não pode apagar cópias já baixadas no dispositivo do destinatário.

## Armazenamento e operação

Bucket `forma-private`, privado. Chave do objeto contém UUIDs de Studio/arquivo,
sem nome pessoal. O Nest inspeciona bytes, tamanho e MIME, calcula SHA256 e
atesta o resultado por HMAC. `FORMA_UPLOAD_VERIFIER` é segredo exclusivo do
servidor, correspondente ao registro privado do banco; nunca incluir em bundle,
desktop, logs, captura ou ZIP. Não rotacionar um lado isoladamente.

O objeto é imutável após o envio. Só arquivo validado pode ser publicado em uma
mensagem. Anexo do chat não é exibido à equipe antes dessa publicação. Código
não é executado; inspeção de assinatura não equivale a antivírus.

Retirada marca tombstone e tenta excluir pela API Storage, verificando ausência.
Falha mostra limpeza pendente e permite tentar novamente. Cancelamento impede
publicação tardia, mas um upload que termine depois da limpeza pode deixar um
objeto órfão. Reconciliação/GC operacional e retenção ainda são necessários
antes da abertura da beta. Não declarar eliminação física quando o provedor
não a confirmou. Não retornar URL pública ou token do Storage ao cliente.

## Validação e limites

108 testes Node passaram, incluindo contrato HTTP, armazenamento, idempotência,
cancelamento e preservação de anexos que chegam durante o envio da mensagem.
Teste PostgreSQL real `supabase/tests/central_work.sql`, com BEGIN/ROLLBACK,
cobriu isolamento, cargos, sessão, conflitos, revisões,52 tarefas em50+2,
arquivo imutável/prova inválida, revogação, cancelamento e arquivo retirado.
Fixtures .invalid foram revertidas; nenhum usuário real foi criado nesses testes.

QA no navegador com provedor fictício cobriu quadro/lista/calendário, tarefa,
conversas separadas, envio/prévia de código, histórico, conflito de documento e
equipe20+3. A sessão fictícia foi removida; a prévia fica em host isolado
127.0.0.2 para não substituir cookies do aplicativo em127.0.0.1.
Não houve login completo com conta real nem transferência real de bytes com
um usuário no Storage remoto. Isso permanece aceite de integração, assim como
duas máquinas/redes, QA móvel e acessibilidade com leitor de tela.

Não houve publicação pública, serviço pago nem novo instalador. LiveKit,
recuperação de senha, operação/auditoria do primeiro Studio, HTTPS central,
desktop remoto, backup/restauração e distribuição remota continuam pendentes.

Controles aplicados do capítulo12: menor privilégio, isolamento, minimização
de metadados, arquivos privados e retirada verificável. Evidência técnica não
constitui certificação de conformidade jurídica.

Referências técnicas: [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security),
[download autenticado](https://supabase.com/docs/guides/storage/serving/downloads)
e [API oficial de Storage](https://github.com/supabase/supabase-js/blob/master/packages/core/storage-js/src/packages/StorageFileApi.ts).
