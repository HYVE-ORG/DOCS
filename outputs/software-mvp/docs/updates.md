# Atualizações desktop — 0.2.0

## Interface0.2.1

Configurações agora inclui Verificar e atualizar, disponível no app Windows.
Reutiliza o mesmo diálogo do menu nativo: confirma download e reinício, sem URL
arbitrária enviada pela interface. Navegador informa a disponibilidade no app.
IPC verifica origem, janela e frame principal. Nova versão0.2.1 no feed local.
Consulte [relatório desta entrega](beta-status-report.md).

Escopo aprovado: preparar e testar no servidor local. Nenhuma publicação externa.

## Uso

Baixe e instale 0.2.0 uma vez: 0.1.1 não possui atualizador. Alt > Atualizações
oferece verificar, baixar e instalar/reiniciar. A opção automática, ativada por
padrão, persiste em updates.json no perfil do Forma. Verifica após 15 segundos
e a cada seis horas, baixa em segundo plano, notifica e instala ao sair
normalmente. Desativá-la impede instalação automática, inclusive após download.
O botão manual continua disponível. Finalize suas edições antes de reiniciar.

Somente instalação NSIS Windows x64 possui atualizador ativo. O instalador
grava resources/forma-installed.json; portátil e desenvolvimento usam o EXE
manualmente. A API fecha antes da instalação. Encerramento da sessão Windows
inibe instalação automática. Downloads interrompidos não são instalados.

## Servidor e nova release

Na raiz do MVP, npm run dev mantém localhost:5173 e API4100. O feed fixado no
app é http://127.0.0.1:5173/downloads/installers/. A aplicação desktop funciona
sem esse servidor; a verificação fica indisponível. Cada computador precisaria
desse endereço local: isto ainda não distribui atualizações pela internet.

Para produzir a próxima versão, aumente package.json/package-lock.json com
npm version patch --no-git-tag-version e execute npm run desktop:installer.
O pipeline gera EXE, SHA256, latest.yml e release.json em release/downloads.
Atualize também o CTA/versionamento do site e os guias antes do build.
Confira com node scripts/verify-installer.mjs. Não reutilize uma versão já
distribuída. Metadados usam no-store; instaladores versionados têm cache.

No primeiro build do instalador, release-updates.mjs cria uma chave Ed25519
em .release-keys/private.pem e fixa somente sua chave pública e URL em
apps/desktop/update-trust.json. Preserve a chave privada em backup protegido;
ela não vai ao pacote, site, Docker ou ZIP documental. Não a envie ao Git.
Builds futuros exigem a mesma chave; não há rotação silenciosa. Perder a chave
exige migração de confiança via novo instalador e comunicação operacional.

O app verifica assinatura de release.json, versão crescente, nome exato do
EXE, tamanho e SHA512. Confere latest.yml e o binário antes de liberá-lo,
inclusive novamente antes de sair. Rejeita manifesto adulterado, downgrade,
URLs arbitrárias, pacotes web e pedidos de elevação. HTTP só em loopback;
futura origem externa deve usar HTTPS e ser fixada em novo build confiável.
Não altere URL sem planejar migração dos apps já instalados.

A assinatura do manifesto autentica a release; não é Authenticode. O EXE
continua sem assinatura Windows e pode acionar SmartScreen. A chave privada
comprometida compromete o canal. Preserve licenças das dependências; não há
declaração de conformidade jurídica. Sem telemetria ou conteúdo de usuário
no feed. Controles relacionados: capítulo12 (distribuição, privacidade,
segurança e licenciamento); snapshots legais não alterados.

## Validação e limites

Testes cobrem assinatura, origem, downgrade, metadata divergente, adulteração
do binário, preferência, concorrência e encerramento. smoke-updates.cjs usa
Electron e electron-updater reais com versão anterior simulada, perfil isolado,
download do instalador local e instalação explicitamente bloqueada.
Uso: node scripts/smoke-updates.cjs CAMINHO_DO_PAYLOAD/resources.

O payload também é extraído do instalador e os smokes de abertura/administração
executam com perfis fictícios. Isso não testa instalação, atualização do
registro/atalhos, reinício do instalador ou desinstalação no Windows real.
Esse aceite em máquina de teste continua pendente antes de distribuição ampla.

Evidência de 23/10/2026: 69 testes da aplicação e 18 testes documentais passaram,
build completo/tipagem aprovados. Instalador 0.2.0: 133.860.992 bytes, SHA256
97512e4745deab85ed07dc5c47ab6f9f2c5ff2dab2a8d8cc60694c7bc686bf59.
10.419 hashes do payload conferidos em work/installer-smoke/payload-gbAAyx;
smokes session-j8fLFk e operator-nVJTkB aprovados. O smoke de atualização
session-7xeMsL encontrou 0.2.0 a partir de cliente 0.1.1 simulado e baixou
o EXE real, com progresso e validação, sem executar instalação. Download HTTP
completo teve o mesmo hash; ambos os manifestos responderam no-store.
Revisão estática independente sem achados importantes. A base .data/state.json
permaneceu com SHA256 EFA01673C632C05D57B23287DF329F33AE74D944A0268C5F5B091AFA842D790F.

Fontes oficiais: [electron-builder v26 auto-update](https://www.electron.build/v26/docs/features/auto-update/),
[Windows](https://www.electron.build/v26/docs/win/),
[Electron BrowserWindow](https://www.electronjs.org/docs/latest/api/browser-window).
Context7 indisponível nesta sessão. API conferida no electron-updater6.8.9;
documentação de versões futuras pode ter contratos diferentes.
