# Forma Desktop — aplicativo único

Versão atual 0.2.1, Windows x64. Admin, Coordenador e Usuário usam o mesmo aplicativo e login. Permissões do backend definem as funções de equipe. A landing fica somente no site; o desktop abre autenticação ou o espaço de trabalho. Configurações inclui Verificar e atualizar.

## Instalação e dados

Na landing, Baixar para Windows entrega Forma-Setup-0.2.1-x64.exe sem conta. Execute e abra o atalho Forma. Não exige Node/npm. A instalação é por usuário, com desinstalador, sem elevação. O formato portátil continua disponível como alternativa técnica.

Dados em %APPDATA%/Forma, separados de .data do ambiente web. Sem sincronização entre computadores. Não compartilhe a mesma pasta entre processos/máquinas; feche o app antes de copiar o perfil completo para backup. Desinstalar preserva o perfil.

## Administração no próprio app

O atalho administrativo separado e Administrar-Studio.cmd não são mais distribuídos. --admin-studio não abre outro modo/app. O instalador remove o atalho legado.

Configuração de Studio, equipe/cargos e moderação permanecem na interface normal, conforme o cargo. Para a preparação operacional do primeiro Studio: cadastre a conta; pressione Alt > Forma > Administração desta instalação; o operador autorizado informa e-mail existente e nome; selecione Voltar ao Forma, na mesma janela.

A API para antes da gravação e reinicia ao voltar. IPC só aceita formulário nativo, frame/janela atuais e estado autorizado pelo menu do sistema. Não há endpoint público para criar Studios. Controle do usuário Windows/base é a fronteira administrativa local, não autenticação de operador remoto.

## Desenvolvimento e distribuição

```powershell
npm test
npm run build
npm run desktop
npm run desktop:package
npm run desktop:installer
node scripts/smoke-desktop.mjs
node scripts/smoke-desktop-operator.mjs
node scripts/verify-installer.mjs
```

Build web: dist. Build desktop: dist-desktop (Vite --mode desktop), sem LandingPage, CSS de marketing, link Conhecer o Forma ou public/downloads. Pacote: resources/app/dist recebe somente dist-desktop. validateDesktopBuild impede incluir landing/downloads no payload.

Installer: electron-builder.json + apps/desktop/installer.nsh; EXE final e SHA-256 em release/downloads, fora de dist e do próprio pacote. API serve attachment em /downloads/installers, Vite encaminha a rota. Sem publicação externa. Bump de versão evita substituir release público com o mesmo nome/cache.

Smokes usam work/desktop-smoke e perfis temporários. O teste administrativo abre a interface, pausa API, prepara Studio e volta ao app na mesma instância, sem flag/atalho separado. verify-installer extrai e verifica o payload real antes de executá-los; não instala/desinstala no Windows real. A ferramenta 7zip vem do build electron-builder.

## Limites

Sem assinatura Windows, criptografia própria, sincronização, macOS/Linux ou mídia remota. Política de navegação/IPC e sandbox permanecem. Ícone/metadados ainda herdam o runtime Electron. QA de instalação, upgrade/remoção de atalho legado, desinstalação e Windows limpo pendente; prévia em navegador do build desktop não equivale a QA visual nativo.

## Atualizações 0.2.0

O novo instalador habilita atualização manual e automática pelo menu nativo
Atualizações. É necessário instalá-lo uma vez sobre a versão anterior.
Feed local, assinatura do manifesto, preferência e procedimentos completos:
[guia de atualização](updates.md). A evidência 0.1.1 abaixo é histórica.

63 testes, build e tipagem aprovados. A revisão identificou retorno desabilitado após clique durante gravação; correção e teste de regressão aprovados, sem novos achados relevantes. Decisões e operação completas no [capítulo 14](../../documentacao-software/14-aplicativo-desktop.md). Versões 0.1.0 anteriores são históricas.

## Evidência 0.1.1

Instalador: 133.446.407 bytes; SHA-256 ccb2d6f98912c7cb160ca6b3dbb8cef0b57e217872429b48211bcd52b8c9c8f0. Download completo por localhost:5173 validado com hash idêntico.

Payload extraído em work/installer-smoke/payload-oEetw2: 10.106 arquivos do manifesto conferidos, sem LandingPage, downloads ou launcher administrativo. Smokes session-Qguc9T (abertura) e operator-xDzB3z (administração e retorno/reabertura); o relatório operator.json registra unifiedAdministration true. Arquivos e perfis fictícios estão em work/desktop-smoke. Prévia visual do build sem landing em work/desktop-login-unificado.png, sem QA visual da janela nativa ou do assistente de instalação.

