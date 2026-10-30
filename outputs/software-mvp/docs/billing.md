# Assinaturas do Forma — preparação comercial

26/10/2026. Desenho aprovado: mensalidade por Studio, dois planos públicos e
propostas empresariais privadas. Implementado no código e no Supabase Forma;
vendas continuam desativadas. Nenhuma assinatura ou cobrança real foi criada.

## Catálogo aprovado

| Limite por Studio | Essencial | Pro |
|---|---:|---:|
| Mensalidade em BRL | R$ 79,00 | R$ 149,00 |
| Membros | 10 | 30 |
| Áreas de trabalho | 3 | 10 |
| Projetos | 10 | 50 |
| Arquivos privados, bytes decimais | 100 MB | 250 MB |
| Minutos de participante/mês propostos para chamadas | 300 | 1.000 |
| Participantes simultâneos por sala propostos | 8 | 8 |

Ambos incluem tarefas em quadro/lista/calendário, chat, documentos, perfis,
cargos e Inbox. Chamadas reais ainda dependem do serviço de mídia e não estão
liberadas para venda. Minutos de participante somam o tempo de cada participante;
não equivalem à duração da sala. Não há promessa de recursos ilimitados.

Empresas grandes podem solicitar proposta. Um operador autorizado da plataforma
define preço em centavos, limites, destinatário e validade; cada revisão cria uma
nova versão. Admin de Studio não se torna operador. A oferta aceita preserva o
snapshot de preço e limites, mesmo após alteração do catálogo. Não há terceiro
plano público nem negociação de preço pelo navegador.

## Jornada e acesso

Cadastrar uma conta não cria Studio. Convites continuam na Inbox, independentes
da assinatura. A contratação futura exige conta confirmada, resumo da empresa,
plano e versão, condições comerciais e aceite explícito. Após pagamento aprovado
e conferido no provedor, uma transação provisiona exatamente um Studio, seu
Admin, área, projeto e dois chats de contexto. Retorno do checkout e webhook
isoladamente não concedem acesso.

Cobertura paga e eventual carência de sete dias determinam novas escritas.
Cancelamento da renovação preserva o período já pago; não emite reembolso.
Depois da cobertura/carência, o trabalho fica em leitura conforme a autorização
do membro. O responsável financeiro conserva seus próprios comprovantes mesmo
se sair da equipe, sem ganhar acesso ao conteúdo do Studio. Exportação JSON de
comprovantes não é nota fiscal nem exportação completa dos dados de trabalho.

Em #central → Planos e assinatura há catálogo, contratos, conferência de
pagamento, cancelamento com confirmação, comprovantes e solicitações com protocolo.
Operadores podem criar/revogar propostas privadas e responder solicitações. O
gate fechado mantém os botões de contratação desabilitados. Gestão global de
incidentes e liberação de concessões internas ainda não foram implementadas.

## Backend e isolamento

Contratos compartilhados: packages/contracts/billing.ts. Backend: billing-domain,
mercadopago, billing-reconciler e billing-controller em apps/api/src. O gateway
usa fetch nativo, destino HTTPS fixo, timeout, resposta limitada e nenhum retry
automático do POST que cria recorrência. Uma criação ambígua fica bloqueada até
conciliação por referência. Claim atômico impede POST duplicado concorrente.

Schema privado forma_billing: catálogo versionado, propostas, contratos,
pagamentos, notificações, auditoria, nonces, operadores, solicitações e configuração.
RLS está forçada, sem grants diretos de tabelas aos usuários. RPC pública invoker
encaminha apenas operações estreitas; a mutação financeira exige atestação HMAC,
nonce e timestamp do servidor, sem service_role no aplicativo. A identidade e o
escopo do comprador/operador são conferidos no banco.

Notificações Mercado Pago verificam assinatura e timestamp antes da inbox durável.
O conciliador usa leases e consulta assinatura, fatura e pagamento no provedor,
conferindo recebedor, ambiente, moeda, valor, pagador, referência e período. Ele
executa a cada minuto quando o gateway está configurado; scripts/reconcile-billing.ts
permite conferência manual. Evento repetido não duplica Studio ou pagamento.
Reembolso parcial registra valor sem apagar a cobertura; integral é distinto.
Contrato cancelado permanece conciliável para receber pagamento confirmado tardio.

Guards SQL limitam membros ativos/convites pendentes, áreas, projetos e bytes,
inclusive nas chamadas REST diretas. Arquivo retirado mantém reserva até confirmação
física no Storage. Cliente não pode forjar purged_at; tamanho real e MIME do upload
precisam corresponder à reserva. Essas verificações não substituem limpeza de órfãos.

## Endpoints

Base /api/central/billing. GET status é público; GET account, receipts e requests
exigem sessão. POST checkout, checkouts/:id/cancel, checkouts/:id/reconcile,
offers, offers/:id/revoke, requests e requests/:id/respond usam identidade,
validação estrita, controle de origem e limite de requisições. POST webhook usa
assinatura do provedor, sem depender de cookie/origem de navegador. Cancelar exige
confirm:true. Criar checkout exige planVersion e termsVersion atuais.

No Electron, checkout só abre no navegador externo no host e caminho Mercado Pago
permitidos, com preapproval_id válido; não carrega conteúdo remoto dentro do app.
O código novo não foi incluído no instalador0.2.1.

## Configuração segura e ativação futura

.env.example contém nomes, sem credenciais. SUPABASE_URL e chave publicável ficam
no backend; FORMA_BILLING_SECRET é próprio do servidor, gerado por
node scripts/prepare-billing-secret.mjs e configurado de forma privada em
forma_billing.server_keys. Não rotacionar sem plano coordenado. A chave já foi
configurada no Forma; não a copiar para VITE_*, bundle, documentação ou chat.

Ainda faltam MERCADOPAGO_ACCESS_TOKEN, MERCADOPAGO_COLLECTOR_ID,
MERCADOPAGO_WEBHOOK_SECRET, modo validado, FORMA_BILLING_BACK_URL HTTPS e versão
das condições em FORMA_BILLING_TERMS_VERSION. Não enviar segredos pelo chat.
Testar com ambiente/contas de teste compatíveis com o provedor antes de produção.

Três barreiras ficam fechadas: CHECKOUT_RELEASE_READY=false no código,
sales_enabled=false no banco e FORMA_BILLING_SALES_ENABLED desativada no ambiente.
Configurar credenciais não libera venda. Só mudar após comprovar entrega, suporte,
termos, capacidade e testes reais. Até lá a interface informa preparação.

Capacidade conservadora inicial: no máximo três Studios comerciais, com reservas
globais de750 MB e3.000 minutos de participante. Não é garantia de que todo o
serviço gratuito comporte o uso: banco, tráfego, logs e mídia precisam de medição.
Contratos que receberam ID externo continuam reservando capacidade após cancelar;
liberação automática segura de reservas abandonadas ainda está pendente.

## Evidências e pendências

125 testes Node passaram na implementação, assim como tipagem e builds web,
desktop e API. SQL real com rollback cobriu isolamento, atestação/replay,
provisionamento idempotente, quotas, upload maior que reserva, comprovantes sem
membership, pagamento tardio após cancelamento e mudança de versão de preço.
Advisors de segurança de26/10 não indicaram WARN/ERROR: os12 INFO de tabelas sem
policy correspondem às tabelas privadas com negação por padrão. Revisão independente
encerrou os seis achados P1/P2 identificados nesse escopo.

QA de interface usou somente provedor e dados fictícios: catálogo79/149,
solicitação com protocolo, resposta, cancelamento confirmado, criação de proposta,
substituição/revogação e download de comprovantes JSON. A oferta anterior ficou
visível e indisponível após substituição; o fixture não simula o incremento do
número de versão do banco. Isso não comprova integração Mercado Pago em produção
nem transação financeira real. Conta fictícia encerrada e servidor de QA parado.

Antes de vender: testar MP real em ambiente apropriado; HTTPS/backend/webhooks;
mídia gerenciada real e medição; desktop remoto e nova release; recuperação de
conta; backup/restauração; operação de suporte, reembolso e encerramento; exportação
do trabalho; retenção e limpeza de arquivos, nonces e auditoria; capacidade e tráfego.
Exportação textual de trabalho foi adicionada depois desta etapa:
[guia de exportação](studio-export.md). Bytes e restauração continuam pendentes.
Identificação do fornecedor, condições/privacidade e tratamento fiscal exigem
revisão para a operação concreta; este guia não declara conformidade jurídica.

Vexo ainda depende do cadastro confirmado do primeiro Admin. Não há concessão
interna implícita. Não houve publicação, plano de infraestrutura pago, alteração
no Menzu, migração do JSON local ou substituição do instalador existente.
