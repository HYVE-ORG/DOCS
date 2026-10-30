# Cloudflare — borda gratuita da beta

Estado em 24/10/2026: código implementado e testado localmente; Worker privado
de validação enviado à conta, sem URL pública. Interface completa não publicada.
Usuário autorizou usar Cloudflare com restrição de não usar serviços pagos.

## Validação privada na conta

Após as verificações iniciais abaixo, o usuário confirmou Workers Free pelo
painel. Foi enviado pelo plugin o módulo apps/edge/staging.ts compilado, como
forma-beta-edge-staging, deployment ab9e49c9ca4f4e7aa9d62ef1dafa3074.
Cloudflare aceitou o módulo, startup1ms. Sem assets, bindings, segredos, banco,
cron, domínio, Logpush ou observabilidade. Nenhuma assinatura/plano foi alterado.
GET de subdomain confirmou enabled:false e previews_enabled:false após configurá-los.

O artefato privado responde503 de preparação, validado no bundle local para /
e /api/status; não foi exercitado por HTTP remoto porque acesso público está
desativado. Não confundir upload aceito com colaboração/mídia ou deploy do site.
Workers Free foi confirmado pelo usuário, não por leitura de faturamento OAuth.
O campo usage_model:standard da API não significa adesão ao plano Workers Paid.
Inspeção e retomada: nome forma-beta-edge-staging em Workers & Pages; manter
desabilitado até integrar backend central e revisar o pacote completo.

## Arquitetura

apps/edge/worker.ts serve assets do site e encaminha /api, /socket.io e
/downloads/installers a um único backend HTTPS configurado por API_ORIGIN.
Isso preserva cookies da mesma origem, corpo de requisição, Range e streaming.
Não armazena contas ou arquivos no Worker nem substitui NestJS, banco e mídia.

Origem ausente/insegura retorna503; falha ou redirect do backend retorna502.
Mutações e upgrade WebSocket exigem Origin da interface. Polling inicial GET/HEAD
sem Origin só é aceito com Sec-Fetch-Site:same-origin; proxy define Origin público
para a autorização Socket.IO do backend. Headers de encaminhamento do
cliente são removidos; respostas dinâmicas usam no-store. O backend deve configurar
APP_ORIGIN com a URL pública exata, SECURE_COOKIE=true e não confiar em IP repassado
arbitrariamente. Cookies precisam ser host-only, como já são no MVP.

WebSocket é encaminhado com a resposta101 original; o teste atual valida guardas,
mas handshake end-to-end com NestJS remoto ainda não foi exercitado. Não declarar
chat compartilhado pronto a partir deste incremento.

## Preparar e conferir

Na raiz do MVP, npm run cloudflare:prepare compila somente o site e cria um
candidato novo em release/cloudflare/candidate-*/. Inclui arquivos públicos
permitidos, recusa dotfiles/symlinks/extensões indevidas e arquivos acima de25MiB.
Não inclui executáveis, .data, segredos, runtime Electron ou node_modules.
O instalador Windows é maior que o limite estático; sua rota exige backend de
distribuição disponível. Não habilitar R2 faturável para contornar esse limite.

Wrangler4.152.0 é dependência local de desenvolvimento, fixada no lockfile.
O comando de preparação não executa deploy. Para validar um candidato, com
telemetria desativada via WRANGLER_SEND_METRICS=false:

```powershell
node node_modules/wrangler/bin/wrangler.js deploy --config CAMINHO_DO_CANDIDATO/wrangler.json --dry-run --no-autoconfig
node node_modules/wrangler/bin/wrangler.js dev --config CAMINHO_DO_CANDIDATO/wrangler.json --local
```

Configuração tem somente ASSETS, sem banco, R2, Containers, cron, analytics ou
bindings de produtos pagos. Configuração não comprova o plano da conta.

## Conexão verificada pelo plugin

O plugin Cloudflare autenticou em24/10/2026 e listou uma conta e zero Workers.
Consulta ao subdomínio retornou404: workers.dev ainda não foi inicializado.
A consulta GET de subscriptions retornou403: OAuth não cobre esse endpoint;
o servidor exige Billing Read/Write via outro tipo de credencial. Não solicitar
nem colar token de faturamento no chat. Não mudar permissões de forma ampla.

Na primeira verificação nenhum POST/PUT/DELETE remoto foi executado. O envio
privado posterior está registrado acima. Não se criou subdomínio, assinatura
ou domínio. A conexão do plugin não autentica automaticamente Wrangler;
whoami local informou não autenticado. Preferir plugin ao operar a conta.

Workers Free já confirmado pelo usuário. Antes de publicar: inicializar workers.dev sem
upgrade, definir backend HTTPS e validar a release completa. Se a conta tiver
plano pago, não presumir que quota incluída garante custo zero. Alertas de
consumo não são teto financeiro. Limite atingido deve interromper funcionalidade,
sem autorizar upgrade ou cobrança. Mídia gerenciada também requer plano gratuito
e limite verificados antes de ativar; LiveKit não foi provisionado.

## Evidência e pendências

83 testes passaram. Build completo inicial aprovado; bundle Worker revalidado
após a correção de polling. Os oito testes novos
cobrem proxy, guards e staging. Wrangler dry-run aprovou o candidato AZSPPB;
workerd local respondeu200 para site e503/no-store para API e instalador sem
backend, sem recursos remotos. Runtime local foi encerrado após a verificação.
Não houve publicação nem teste de sessão/WebSocket em origem pública.

Auditoria npm sinalizou multer2.4.0 e undici7.29.1 transitivos. Overrides restritos
para multer2.5.0 e undici7.30.1 corrigiram os avisos, sem downgrade automático do
NestJS/Wrangler. npm audit e produção retornaram zero vulnerabilidades conhecidas
na checagem. O instalador0.2.0 antigo não foi regravado; futuras releases precisam
ser recompiladas para incluir a árvore atualizada.

Próximos bloqueios da beta: identidade/banco/Storage centrais, backend hospedado,
conexão segura do desktop e LiveKit real. Cloudflare na borda não resolve esses
itens sozinho. Dados locais e perfis continuam preservados.

Controles relacionados: JUR-05/06/08/10 do capítulo12. Nenhum dado real foi
transferido a serviços novos. Antes de publicação, revisar fluxo de fornecedores,
região, logs e retenção; não há declaração de conformidade jurídica.

Fontes oficiais consultadas também pelo plugin:
[limites](https://developers.cloudflare.com/workers/platform/limits/),
[preços](https://developers.cloudflare.com/workers/platform/pricing/),
[roteamento de assets](https://developers.cloudflare.com/workers/static-assets/routing/worker-script/).
