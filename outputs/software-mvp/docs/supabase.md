# Supabase — conexão e identidade, incremento 2

Atualização: o [incremento3](central-domain.md) aplicou quatro tabelas privadas,
RLS e RPCs de conta/convites no Forma e adicionou login online separado. As
afirmações de banco vazio abaixo são a evidência histórica do incremento2;
não descrevem o schema atual. Dados pessoais reais continuam não importados.

24/10/2026. Projeto Forma criado separadamente do Menzu, na organização
Softwares Lançados, por escolha explícita do usuário. Plano Free confirmado
pelo serviço, cotação US$0/mês antes da criação. Região sa-east-1 (São Paulo).
Projeto: kkedfzpphxmnegamhmnz. Nenhuma operação no banco Menzu.

## Conexão real verificada

URL e publishable key obtidas pelo plugin, gravadas no .env local ignorado.
Nenhuma chave secret/service_role obtida ou distribuída. npm run supabase:check
usa /auth/v1/settings e retornou authReachable:true, databaseVerified:false.
Esse comando verifica Auth; não equivale a uma conexão SQL da aplicação.

Uma consulta SELECT1 pelo plugin confirmou PostgreSQL17.11. list_tables no
schema public retornou vazio, e os advisors de segurança retornaram zero avisos.
Não foram criadas tabelas ou migrados dados. Credenciais de banco não estão no
backend nesta etapa. Projeto novo não é evidência de conformidade ou RLS implementada.

## Código disponível

SupabaseIdentity, em apps/api/src/supabase-identity.ts, valida tokens consultando
/auth/v1/user no projeto configurado. Exige HTTPS de projeto supabase.co e chave
sb_publishable_; não aceita chave secret ou URL arbitrária. Domínio personalizado
ou Supabase self-hosted ficam fora deste incremento. Timeout8s, redirect bloqueado,
resposta limitada64KiB. Token ausente/inválido retorna401; falha do serviço503.

GET /api/auth/identity recebe Authorization:Bearer e retorna somente provider/id
opaco. Não transforma token Supabase em cookie local, não cria Studio e não
atribui cargos por user_metadata/app_metadata. /api/state continua exigindo a
sessão local existente, até implementar o modelo central com associações reais.
Limite de tentativas reutiliza o backend atual. Não registrar cabeçalhos/tokens.

Somente o entrypoint de servidor apps/api/src/main.ts lê SUPABASE_URL e
SUPABASE_PUBLISHABLE_KEY. O desktop local continua sem credencial/provedor remoto
embutido. Cliente não recebe variáveis via VITE_*. Configuração parcial falha
explicitamente na inicialização, sem escolher outro projeto.

Após configurar o ambiente, reiniciar npm run dev ou npm start para aplicar as
variáveis ao processo. O instalador não autentica usuários no Supabase ainda.
Contas locais não foram transferidas, redefinidas nem vinculadas por e-mail.

## Validação

Testes supabase-identity.test.ts e supabase-http.test.ts usam provedor simulado:
token malformado, configuração insegura, resposta adulterada/grande, indisponibilidade,
falta de sessão local e ausência de promoção a Admin. A checagem Auth real validou
configuração/conectividade sem enviar e-mail, criar conta de teste ou guardar token.
Um login real de usuário Supabase e recuperação de senha ainda não foram exercitados.

## Próximo backend necessário

Schema transacional de organizações, associações, projetos/tarefas/chats/arquivos,
autorização central e RLS; storage privado; autenticação/recuperação web e desktop;
operador de plataforma separado do Admin; migração opt-in dos perfis locais;
outbox/reconciliação de eventos; backups/restauração; prova do pooler restrito.
Não salvar todo State em blob SQL nem chamar o StateStore atual de banco central.

O novo projeto usa identidade gerenciada, mas alterações de domínio devem continuar
na API NestJS. Não habilitar acesso direto público sem policies testadas. Sem
schema aplicado, nenhuma policy de produção deve ser presumida.

Controles relacionados: JUR-01/02/04/05/06/10. Antes de dados reais mapear região de
Auth, logs/backups e mídia, finalidade e retenção. Região de banco não garante todos
os dados no Brasil. Não usar consentimento genérico ou afirmar conformidade.

Fontes oficiais: [validação de usuário](https://supabase.com/docs/reference/javascript/auth-getuser),
[chaves da API](https://supabase.com/docs/guides/getting-started/api-keys).
