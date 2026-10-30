# Forma — MVP local

Separação para os quatro repositórios HYVE-ORG e preparação Vercel:
[revisão da beta e publicação](docs/github-beta.md). Fontes preparadas localmente;
envio remoto é rastreado pelos commits em cada repositório. Builds/testes locais não
substituem o aceite da colaboração remota.

UX: navegação principal simplificada, ações rápidas por contexto, abas de Space
com endereço próprio e navegação inferior mobile. Veja [operação](docs/navigation-team.md).

Redesign visual Hive: Google Sans Flex, rail compartilhado em todas as páginas
privadas locais, cartões claros, ações azuis, tabelas e formulários unificados.
Conta, autenticação e áreas online recebem a mesma linguagem visual.
Veja [sistema visual e limites de verificação](docs/design-system.md).

Sala de reunião em página própria: `#meeting/ID`, com navegação do Forma e
retorno para Reuniões ao sair. Veja [operação da sala](docs/meeting-room.md).

Spaces: painel contextual com abas e conteúdos da área em `#workspace/ID`; listagem em `#spaces`, criação com prévia e edição por abas em
`#workspace-settings/ID`, disponíveis ao Admin no ambiente local.
Veja [criação, acesso e limites](docs/spaces.md).

Conta online em preparação: http://127.0.0.1:5173/#central. Perfil, Inbox,
convites e trabalho por Studio usam Supabase com sessões próprias protegidas.
Áreas, projetos, tarefas, chats, documentos e arquivos privados têm fluxo online
separado do local. Veja [operação e aceites](docs/central-work.md).
Esta mudança está no código; o instalador0.2.1 anterior não foi substituído.

App0.2.1: botão Configurações → Verificar e atualizar. Projeto Supabase Forma
gratuito criado e Auth verificado; isso ainda não migra o JSON nem as sessões.
Veja [integração](docs/supabase.md) e [relatório de pendências da beta](docs/beta-status-report.md).

Cloudflare: borda com assets e proxy preparados, sem deploy ou serviço pago.
Use npm run cloudflare:prepare; consulte [operação e limites](docs/cloudflare.md).

Preparação da beta, incremento 1: backend aceita persistência injetada por contrato,
mantendo JSON e arquivos locais como padrão. Veja [escopo e testes](docs/beta-backend.md).
Isso ainda não conecta computadores nem habilita chamadas remotas.

Se estiver lendo este guia no ZIP documental, as fontes da aplicação e os instaladores não acompanham esse arquivo; os comandos de desenvolvimento exigem a árvore completa do MVP.

Revisão da estrutura, correções e prioridades: [relatório técnico](docs/structure-review.md). Builds separados: npm run build:web, npm run build:desktop e npm run build:api; npm run build valida e gera todos. O Compose mantém dados no volume existente e lê instaladores de release/downloads em volume somente leitura. Docker não foi executado nesta revisão.

Desktop 0.2.0: um único aplicativo para todos os cargos, sem landing. Builds separados em dist (site) e dist-desktop (app); preparação operacional do primeiro Studio pelo menu Forma > Administração desta instalação, na mesma janela. Atualização manual/automática pelo menu Atualizações, após instalar uma vez esta versão. Servidor de releases local por enquanto: veja [operação do atualizador](docs/updates.md).

Desktop Windows com API própria, instalador direto na landing e alternativa portátil: [guia de execução, administração e build](docs/desktop.md). Com dependências instaladas, use npm run desktop:installer para gerar e disponibilizar o EXE; npm run desktop:package continua gerando a pasta portátil e o ZIP. Dados em %APPDATA%/Forma, separados da base web; sem sincronização remota.

Clientes e Comercial já estão disponíveis em `#clients` e `#sales` para gestores
autorizados: contatos por área, pipeline, propostas versionadas e conversão de
aceite registrado em projeto/chat. Veja [guia e limites do CRM](docs/crm.md).
O [plano de gestão integrada](../documentacao-software/13-gestao-integrada-e-expansao.md)
mantém horas, custos, HRM, ATS, metas e operações como próximas etapas.

O caminho no topo permite navegar entre Home, área e projeto. A equipe tem
paginação de 20 membros por página, em grade e lista, integrada à busca e
ao filtro de cargo. Veja [navegação e paginação](docs/navigation-team.md).

Landing pública em `/` e `#landing`, com prévia interativa, GSAP e guia do desktop.
Aplicativo em `#home`. Estrutura, rotas, animações, acessibilidade e manutenção:
[documentação da landing](docs/landing-page.md).

React/TypeScript, NestJS, Electron e persistência JSON. Execute os comandos nesta pasta, com Node 22.12+ e as dependências instaladas.

```powershell
npm run dev
npm test
npm run build
```

Interface: http://127.0.0.1:5173. API: porta 4100. `DATA_DIR` define o diretório de dados; padrão `.data`. Este ambiente permanece local, sem publicação ou serviço de e-mail.

## Contas e Studios

Qualquer pessoa pode cadastrar uma conta pessoal. Cadastro não cria Studio. A tela pessoal tem Inbox de convites, Meus Studios, perfil e aparência. O seletor no canto superior esquerdo do Studio abre essa tela. Convites são vinculados ao e-mail cadastrado e duram sete dias. Admin convida para seu Studio; Coordenador convida Usuários somente dentro dos seus projetos. O destinatário aceita ou recusa na Inbox; quem enviou pode acompanhar e revogar nas configurações.

Somente a administração da plataforma cria Studios. Isso é separado do cargo Admin de uma equipe. No piloto a operação usa a conta autenticada do operador no sistema operacional, com acesso de escrita à base local, e exige a API parada. Nenhuma senha é passada em argumento ou gravada em log:

```powershell
node --import tsx scripts/create-studio.mjs
```

A conta do primeiro Admin deve estar cadastrada previamente. O comando cria Studio, área Geral, projeto Primeiros passos e participação Admin. Não habilita cobrança nem criação pública. A API `/setup` recusa criação pública, inclusive em instalação vazia.

Não há verificação externa de propriedade de e-mail nem recuperação automática de senha. A aceitação exige sessão da conta destinatária, mas uma implantação pública depende da entrega de verificação de identidade/e-mail e revisão operacional antes de receber dados reais externos.

## Migração e recuperação

A primeira escrita em uma base v1 cria `state.v1.pre-migration.json`, que não é substituído pelas transações seguintes. O principal passa a armazenar contas e participações separadamente no schema v2; os IDs legados de tarefas, mensagens e arquivos são preservados. E-mail ou @ duplicado interrompe a migração sem mesclar contas. Um backup prévio idêntico permite retomar após interrupção; backup divergente exige revisão do operador.

Antes de migrar, pare o serviço e copie todo o diretório de dados, inclusive uploads, para armazenamento protegido. Para reverter, pare o serviço, preserve uma cópia da base v2 atual e restaure o conjunto v1 original com a versão anterior do software. Não restaure v1 por cima de novas escritas sem reconciliá-las; o backup antigo não contém essas alterações.

## Colaboração e aparência

- Código: envie TS/TSX, JS/JSX, JSON, HTML, CSS, Python, SQL, YAML ou Markdown no chat. Abra o anexo para ler com numeração e destaque, copiar ou baixar. Conteúdo aparece como texto; nunca é executado. Upload até 15 MB; prévia até 500 KB e 5.000 linhas.
- Tarefas: detalhes abrem em painel lateral; Quadro, Lista e Calendário continuam disponíveis. Transições respeitam redução de movimento do dispositivo.
- Aparência: Claro, Escuro e Híbrido, em configurações e conta pessoal. Híbrido combina navegação escura com conteúdo claro. A preferência fica neste dispositivo.
- Reuniões: `/meet` abre a agenda de reuniões; `/meet criar` abre o agendamento autorizado no contexto. Na prévia de dispositivos, M alterna microfone e C câmera, fora dos campos de texto.
- Studio: Admin altera nome, descrição, ícone e cor da faixa; administra membros, cargos e convites e consulta auditoria. O último Admin ativo permanece protegido.

Chamadas remotas multipessoa, gravação, transcrição, pagamento e envio de OTP/e-mail não estão implementados. Prévia de câmera/microfone é local e não transmite para outros participantes.

## Preparação comercial de26/10/2026

Dois planos por Studio: Essencial R$79/mês e Pro R$149/mês; ofertas empresariais
privadas versionadas por operador. Landing → Planos e conta online → Planos e
assinatura. Guia de arquitetura, configuração e pendências: [assinaturas](docs/billing.md).
Checkout continua desativado; credenciais MP e aceites remotos ainda faltam.
