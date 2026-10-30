# Exportação administrativa de trabalho

26/10/2026. Implementada no código e no Supabase Forma. Dentro do Studio online,
o Admin encontra Exportar dados na barra superior. A janela explica o conteúdo,
o formato e os limites antes de Baixar dados. Interromper cancela a coleta;
uma nova exportação pode ser iniciada depois. Recurso ausente no instalador0.2.1.

## Conteúdo

Arquivo forma-studio-UUID.ndjson, UTF-8, uma linha JSON por registro. A primeira
linha é o manifesto (formato/versão/Studio/início/escopo), seguida por registros
identificados por seção e chave. A última linha complete registra fim e contagens.
Só há download após a coleta completa. Conteúdo de código permanece texto literal.

Inclui Studio, membros com nome/handle/cargo/estado, áreas e projetos inclusive
arquivados, acessos, tarefas/atribuições, conversas, mensagens não apagadas,
documentos/revisões, metadados de arquivos prontos e vínculos de anexos válidos.
Não inclui Auth, senhas, sessões, e-mails privados, bio/localização, convites,
Inbox, finanças, chaves, auditoria, conteúdo apagado, paths/tokens de Storage
ou bytes dos anexos. Baixe cada anexo pelo fluxo autenticado de Arquivos.

## Autorização e integridade

POST /api/central/studios/:id/export, corpo {} estrito, origem permitida e sessão.
CentralDomain chama forma_studio_export_page com o JWT atual. A função pública
é invoker; o leitor privado usa search_path vazio, colunas explícitas e exige
actor_id válido e studio_role=admin. Cada página e uma última leitura antes
de entregar os bytes revalidam sessão/cargo. Coordenador, Usuário, ex-membro e
responsável financeiro sem membership não recebem o trabalho. As verificações
também protegem o acesso RPC direto. Cobertura vencida não bloqueia esta leitura.

Paginação por chave estável: UUID, pares de UUID ou documento/versão com padding.
Documentos/revisões usam uma linha por página; mensagens/tarefas cinco; demais
seções25. Isso mantém cada resposta dentro do limite de leitura do adapter.
O backend limita a20MiB,120 segundos e2.000 páginas, com duas exportações
simultâneas por processo. Falha, revogação, cursor inválido ou estouro não
entrega arquivo parcial. Cache-Control:no-store e Content-Disposition:attachment.

Interromper aborta a requisição e impede próxima página/download. Uma RPC que já
iniciou pode aguardar seu timeout de até10 segundos; não há job persistente em
segundo plano. Limites são por processo, sem coordenação distribuída nesta beta.

## Limites operacionais

A coleta não é snapshot transacional entre páginas. Alterações simultâneas podem
aparecer durante a exportação; o manifesto informa isso. Para cópia estável,
coordene uma pausa de alterações na equipe. Exportação não é backup restaurável:
não inclui Auth nem objetos binários, não há importação/restauração automática.
Backup PostgreSQL/Storage e ensaio de recuperação continuam pendentes.

O arquivo contém conteúdo da equipe. O operador deve definir armazenamento,
acesso, retenção e atendimento aos titulares conforme a operação real. A função
implementa controles de engenharia existentes JUR-03/04/05; não certifica
conformidade nem substitui análise jurídica. Nenhum snapshot legal foi alterado.

## Validação

129 testes Node e builds web/desktop/API passaram. Testes novos verificaram
paginação completa, limite, cursor repetido, falha intermediária, cancelamento,
sessão, origem, DTO e cabeçalhos. SQL real com rollback cobriu56 tarefas sem
perdas/duplicação, isolamento, campos excluídos, espaços arquivados, seção/cursor
inválidos, Admin com cobertura vencida, cargos inferiores e sessão expirada.
As contas e Studios fictícios não persistiram. JSON local manteve o hash anterior.

QA browser com provedor fictício confirmou janela, interrupção e reabertura,
download com manifesto/complete e ausência de object_key/access_token/refresh_token.
Revisão independente estática não encontrou P1/P2 no escopo; não substitui teste
com equipe real em duas máquinas. Advisors mantiveram apenas os12 INFO esperados
das tabelas privadas sem policy, nenhum WARN/ERROR.

Fonte técnica consultada: [funções e privilégios Supabase](https://supabase.com/docs/guides/database/functions).
Context7 indisponível nesta sessão; documentação oficial consultada pelo plugin.
