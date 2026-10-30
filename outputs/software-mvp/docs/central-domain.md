# Conta central e convites — incremento 3

24/10/2026. Implementado no código e no projeto Supabase Forma separado. Prévia
web: http://127.0.0.1:5173/#central. O servidor local precisa receber o .env e ser
reiniciado. Não confundir esta prévia com a beta completa ou com o instalador0.2.1.

## Modelo aplicado

Schema privado forma: profiles, studios, memberships e invitations. Conta é
auth.users; membership relaciona conta/Studio, com cargo e estado atuais. Não há
trigger que conceda Studio ao cadastrar. Criar Studio continua operação exclusiva
da plataforma com acesso administrativo ao banco; não existe RPC pública para isso.
Nenhuma conta real, Studio ou associação foi criada automaticamente.

Migrações em supabase/migrations, com versões alinhadas ao histórico remoto:

- 20261024235219_central_identity.sql
- 20261024235419_invitation_membership_policy.sql
- 20261025000734_invitation_expiry_lock.sql
- 20261025000814_expired_invitation_visibility.sql

O CLI oficial gerou os arquivos antes da escrita; o plugin atribuiu os timestamps
remotos, aos quais os nomes locais foram alinhados. Não reaplicar manualmente as
migrações num projeto já migrado. Em outro ambiente, aplicar na ordem e executar
o teste SQL. Não copiar .env, senhas ou sessões locais para o banco.

RLS habilitada/forçada nas quatro tabelas, grants limitados a colunas editáveis,
chaves estrangeiras, checks, unicidade e índices de acesso. Nenhum blob State.
Não adicionar forma à lista de schemas expostos do Data API.

## Autorização

RPCs públicas SECURITY INVOKER só executáveis por authenticated. Helpers no
schema privado usam SECURITY DEFINER exclusivamente para ler conta/sessão,
papel e elegibilidade sem recursão RLS; search_path vazio e execução revogada
de PUBLIC/anon. can_accept também bloqueia a linha do emissor com FOR SHARE,
ordenando aceite com suspensão/remoção; não modifica dados privilegiadamente.

actor_id exige auth.uid associado ao session_id real em auth.sessions, e-mail
confirmado, conta não removida/bloqueada e sessão não vencida. Cargos não vêm
de metadata do cliente. studio_role consulta a associação atual. Remover sessão
impede acesso pelas RPCs mesmo que o JWT ainda não tenha expirado.

Admin convida cargos de seu Studio; Coordenador convida somente Usuário.
Convites têm sete dias, destinatário por e-mail atual do Auth e uma pendência
por Studio/e-mail. Convite expirado pode ser substituído por gestor autorizado.
Coordenador não revoga convite válido de outro gestor. O aceite bloqueia o
convite, confere autoridade atual do emissor e insere associação na mesma
transação. Associação existente nunca é promovida ou reativada por convite.
Revogar/aceitar em paralelo usa o mesmo lock do convite. A nova associação
não concede projetos implicitamente; escopos de projeto serão outro incremento.

## HTTP e sessão

O Nest chama RPCs com publishable key e JWT do próprio usuário. Isto substitui,
neste domínio, a role PostgreSQL direta inicialmente proposta. Não usa senha
de banco ou service_role. O banco continua autorizando cada operação mesmo se
um cliente chamar a RPC diretamente; a API valida DTO/origem e limita tentativas.

| Rota /api/central | Comportamento |
|---|---|
| GET status | Disponibilidade e recorte; sem segredos |
| POST register | Cadastro Auth; usuário confirma e-mail, depois entra |
| POST login | Senha validada pelo Auth; sessão só em cookies HttpOnly |
| POST refresh | Renova pelo refresh cookie e substitui ambos os cookies |
| POST logout | Revoga sessão atual; renova acesso se necessário antes de sair |
| GET account | Perfil próprio, Studios ativos e convites recebidos válidos |
| POST profile | Nome, @ único, bio, título profissional e local próprios |
| POST invitations | Convite autorizado; não envia e-mail por este domínio |
| POST invitations/:id/respond | accept/decline atômico do destinatário |
| POST invitations/:id/revoke | Revogação pelo gestor autorizado |

Cookies forma_central_access/refresh têm HttpOnly, SameSite=Strict e
Path=/api/central; SECURE_COOKIE=true é obrigatório em HTTPS. Access Max-Age
segue o provedor; refresh tem limite local de30dias. São diferentes do cookie
forma_session do piloto local. Não há token no localStorage/JS da interface.
As chamadas da interface compartilham uma renovação simultânea, sem repetir
login/cadastro/logout automaticamente. POST exige origem conhecida.

Timeout10s, redirects bloqueados, corpo JSON remoto limitado1MiB inclusive em
erro; mensagens internas SQL/Auth não chegam ao usuário. Falha central não
abre base JSON nem tenta senha local. Se o provedor ficar indisponível durante
logout, cookies são removidos mas a revogação remota não é afirmada como sucesso.

## Interface e limites de operação

#central oferece login/cadastro, perfil, Inbox, aceite/recusa e envio de convites
pelos gestores de um Studio existente. Informa explicitamente o recorte online.
Cadastro não faz login automaticamente. A confirmação pertence ao Supabase Auth;
Site URL, redirecionamentos permitidos, templates, entrega de e-mail e limites
do serviço precisam ser configurados/testados antes da beta pública. Não se
executou signup real nem enviou e-mail nesta validação. Recuperação de senha
ainda não está implementada na UI/API central.

Para o primeiro Studio central: o operador deve verificar uma conta Auth já
confirmada e criar Studio + membership Admin numa transação administrativa.
Não transformar Admin local em operador remoto, não vincular por simples e-mail
e não distribuir acesso administrativo ao aplicativo. Esse processo ainda não
tem comando operacional automatizado/testado nem trilha completa de auditoria.

Atualização de25/10: projetos/tarefas/chat/documentos e arquivos têm implementação
online separada, descrita em [trabalho online](central-work.md). CRM e Socket.IO
do MVP continuam locais. Não há sincronização/importação. O desktop instalado
mantém perfil/API local sem credenciais embutidas; não houve novo instalador.
HTTPS central/desktop remoto, aceites reais de Storage e mídia continuam
bloqueios. Cloudflare privado não foi publicado por este incremento.

## Evidência

supabase/tests/central_identity.sql roda dentro de BEGIN/ROLLBACK com contas
fictícias .invalid. Verificou Studio separado, conta sem Studio, Inbox,
perfil sem vínculo invisível, aceite/cargo correto, duplicidade, proibição de
Studio público, metadata forjada sem poder, autopromoção negada, emissor
suspenso, sessão removida, anon negado e reenvio expirado de outro gestor.
Todo dado fictício foi revertido; as quatro tabelas permaneceram vazias.

O teste detectou recursão RLS na primeira política de aceite e o teste de
expiração detectou o conflito de unicidade e a visibilidade da imagem nova no
UPDATE. As migrações seguintes corrigem esses casos, sem apagar histórico.
Revisão independente identificou expiração/reenvio e logout sem access cookie;
ambos ganharam regressão e foram corrigidos.

Testes Node usam provedor fictício para login/cookies/HTTP, DTO/origem, erros,
renovação concorrente e logout expirado. npm run supabase:check-central real
confirmou RPC existente negando anon com401/42501. Advisors de segurança sem
avisos. Isso não comprova login/recuperação reais, concorrência entre duas
conexões SQL ou revisão completa de segurança. UI verificada no navegador
somente sem autenticar: estados e alternância login/cadastro.

Controles JUR-01/02/04/05/06/10: autorização testada, sem transferência automática
de dados locais; retenção, direitos, fornecedores, backup e avisos operacionais
continuam precisando de validação antes do uso externo. Não é certificação.
