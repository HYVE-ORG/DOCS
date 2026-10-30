# 14 — Aplicativo desktop Windows

**Estado em 24/10/2026, documentação v0.16 / aplicativo 0.2.1:** um único Forma para Admin, Coordenador e Usuário. Landing e download pertencem somente ao site. O desktop abre login/cadastro ou o espaço de trabalho, sem página de apresentação ou instalador dentro do próprio app. Configurações inclui Verificar e atualizar, reutilizando o fluxo nativo com IPC restrito.

## Produto e distribuição

O instalador Windows x64 usa NSIS/electron-builder. Instala para o usuário atual, cria atalhos Forma e desinstalador e preserva o perfil. Não exige Node/npm ou elevação. O site mantém Baixar para Windows, apontando a /downloads/installers/Forma-Setup-0.2.1-x64.exe sem login. O formato portátil continua como alternativa técnica.

Não existe aplicativo de usuário separado do de Admin. Cargos, convites, gestão de equipe, configuração do Studio e moderação funcionam na interface compartilhada, autorizados pelo backend conforme o cargo e o contexto. A criação de Studios pela administração da plataforma continua uma atribuição distinta do cargo Admin de uma equipe.

## Builds separados

npm run build compila o site em dist e a interface desktop em dist-desktop, além dos bundles NestJS. Vite no modo desktop não importa LandingPage e não copia public/downloads; o login não tem Conhecer o Forma. Rotas de marketing, inclusive #landing, não renderizam marketing nesse build.

O empacotador valida ausência de chunks da landing e diretório de downloads antes de copiar dist-desktop para resources/app/dist. No desenvolvimento, Electron serve dist-desktop. Uma página de landing não é incluída e apenas escondida: seu componente e CSS não entram no build desktop.

npm run desktop:installer usa a pasta limpa do aplicativo, preserva runtime/licenças e gera o EXE e seu SHA-256 em release/downloads. Essa pasta é externa ao payload. Nest a serve como attachment em /downloads/installers e Vite encaminha a mesma rota; Range permite retomada, arquivo ausente retorna 404 e arquivos ocultos são negados. Build usa publish never, sem publicação externa.

## Administração na mesma janela

O antigo atalho Forma - Administrar Studio e o launcher Administrar-Studio.cmd foram removidos. A flag --admin-studio não inicia uma aplicação ou modo separado. O instalador remove o atalho legado durante a atualização.

Para preparar o primeiro Studio local:

1. Cadastre a conta no próprio Forma.
2. Pressione Alt e abra Forma > Administração desta instalação.
3. O operador autorizado confirma sua atribuição e informa o e-mail de uma conta existente e o nome do Studio.
4. Selecione Voltar ao Forma, na mesma janela, e abra Meus Studios.

O menu nativo pausa a API, apresenta o formulário nativo na janela existente e mantém IPC restrito a essa página/frame. O provisionamento cria Studio, área Geral, projeto Primeiros passos, chat, participação Admin e auditoria. Não cria senha/conta. Voltar ao Forma reinicia a API e carrega a interface, sem exigir encerrar/reabrir nem executar outro app.

Essa ação não é um endpoint público nem uma capacidade de qualquer conta pessoal. **Fronteira operacional desta prévia:** o operador Windows com acesso de escrita à base controla a instalação local. Menu e confirmação não autenticam um administrador remoto. Um usuário com controle desse mesmo perfil Windows tem esse acesso operacional; separar administração remota exige arquitetura central antes da oferta comercial.

## Dados e segurança

Perfil padrão %APPDATA%/Forma: data/state.json, uploads, armazenamento Chromium, window.json, appearance.json e desktop.log. É separado da base .data do localhost do projeto. Dispositivos não sincronizam; contas/convites pertencem à mesma base local. Não apontar dois processos/máquinas para um diretório de dados compartilhado.

O main inicia sua própria API Nest em 127.0.0.1, porta livre, com caminho estático explícito e independente do CWD. Não adota servidores existentes. Fechar a janela encerra sua API; a administração só grava após a API parar, e o encerramento aguarda uma operação administrativa em andamento. Base inválida não é recriada vazia. Janela única, foco na segunda abertura, menus de edição/zoom/ajuda e estado da janela/tema persistentes.

Node desligado no renderer; contextIsolation, sandbox e webSecurity ativos. Navegação, novas janelas/webviews e downloads são restritos. Permissões de câmera/microfone dependem da origem local e do sistema. A prévia de mídia continua local, sem chamadas multipessoa. A aplicação de regras de negócio permanece no backend.

IPC de administração exige estado aberto por menu nativo, API parada, janela/frame principal e URL local exata. Não há IPC genérico de filesystem/comando. IPC de aparência aceita somente light/dark/hybrid da interface principal. FORMA_DESKTOP_PROFILE é override operacional/teste; FORMA_DESKTOP_URL é apenas desenvolvimento em loopback e não deve usar o build do site como interface desktop.

Não há criptografia própria em repouso. Proteja usuário Windows, disco e backups. Feche o app antes de copiar o perfil completo; preserve o conjunto atual antes de restaurar backup consistente. Desinstalar o aplicativo não elimina o perfil. Direitos de titulares e eliminação seguem o capítulo 12; log técnico não inclui conteúdo de chats ou senhas.

## Verificação e limites

63 testes, build e tipagem aprovados. Regressões cobrem rotas desktop sem landing, build sem downloads/marketing, políticas de URL/frame, isolamento, janela/tema, API dinâmica e provisionamento. Smoke real do Electron exercita abertura, pausa da API, administração, retorno e reabertura na mesma instância com perfil fictício. Revisão independente identificou bloqueio do botão Voltar durante gravação: corrigido com desabilitação temporária, aceite/rejeição explícita do IPC e teste de regressão. Revisão posterior sem novos achados importantes.

O script verify-installer.mjs extrai o próprio instalador, confere hashes do manifesto e valida ausência da landing/launcher, depois executa os smokes do desktop e administração com perfis isolados. Prévia visual do build desktop em navegador também confirmou login sem acesso de marketing, inclusive em #landing; isso não é QA visual da janela nativa.

A evidência do artefato atual fica no guia desktop do MVP e no relatório installer-report.json. Não foram testados assistente nativo, atalhos/registro durante upgrade, desinstalação, leitor de tela, dispositivos físicos ou Windows limpo. O teste do payload não substitui esses aceites.

Instalador 0.1.1: 133.446.407 bytes; SHA-256 ccb2d6f98912c7cb160ca6b3dbb8cef0b57e217872429b48211bcd52b8c9c8f0. Download local completo com hash idêntico; 10.106 hashes do payload conferidos. Smokes session-Qguc9T e operator-xDzB3z aprovados com API e perfis temporários.

Sem assinatura digital Windows, macOS/Linux, sincronização ou hospedagem externa. Ícone/metadados do executável ainda herdam parcialmente o Electron. Antes da produção: validar instalação/upgrade/desinstalação em máquina limpa, acessibilidade, assinatura/rollback, licenças e arquitetura de colaboração compartilhada. Não declarar conformidade jurídica a partir deste pacote.

## Atualizador 0.2.0

Após instalar uma vez esta versão, Alt > Atualizações permite verificar,
baixar e instalar/reiniciar manualmente. A opção automática vem ativada,
persiste no perfil, verifica 15 segundos após abrir e a cada seis horas,
baixa em segundo plano e instala ao fechar normalmente. O usuário pode
desativá-la. A API encerra antes de instalar e o perfil é preservado.
Encerramento da sessão Windows inibe a instalação automática.

Somente NSIS instalado habilita o atualizador. O feed está fixado no servidor
local em localhost:5173/downloads/installers/; mantenha npm run dev ativo.
Sem servidor, o app continua funcionando e a busca manual informa falha.
Não há distribuição remota nesta etapa, conforme decisão do usuário.

O manifesto tem assinatura Ed25519 com chave pública fixada no app; o fluxo
valida versão crescente, metadata, nome, tamanho e SHA512 do instalador.
A chave privada fica fora dos pacotes, Docker e documentos distribuídos.
Essa assinatura de integridade não é Authenticode. Leia o [guia operacional
do atualizador](../software-mvp/docs/updates.md) para publicar novas versões
localmente, preservar a chave e consultar evidências e limites do QA.

## Histórico e fontes

v0.9: primeira pasta portátil e ferramenta administrativa separada. v0.10: instalador/download direto. v0.11 substitui o launcher administrativo por menu na mesma janela e separa os builds do site e desktop. Artefatos anteriores são históricos e não representam a interface atual.

Fontes técnicas oficiais consultadas em 23/10/2026: [Electron Security](https://www.electronjs.org/docs/latest/tutorial/security), [Application distribution](https://www.electronjs.org/docs/latest/tutorial/application-distribution), [NSIS electron-builder](https://www.electron.build/docs/nsis/). Context7 indisponível. Dependências, runtime e licenças são preservados; snapshots legais não foram alterados.

