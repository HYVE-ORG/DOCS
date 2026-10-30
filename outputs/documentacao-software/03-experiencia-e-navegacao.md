# 03 · Experiência, páginas e jornadas

A navegação de gestão integrada está no [capítulo 13](13-gestao-integrada-e-expansao.md). Clientes e Comercial já aparecem no MVP para Admin/Coordenador, com registros filtrados pelas áreas autorizadas. Formulários cobrem cadastro, oportunidades, propostas versionadas e aceite confirmado; Horas, Pessoas administrativas e Financeiro permanecem planejados. Não há menus simulados dessas etapas futuras.

## 1. Leitura da referência visual

A referência inicial e sua composição em recortes mostram uma aplicação de trabalho com sidebar fixa, breadcrumb superior, título de projeto, cartões de indicadores, alternância Calendar/Board/List e kanban. Os cartões de tarefa apresentam prioridade, nome, data, anexos, etiquetas, responsáveis, comentários e percentual de progresso. A linguagem visual usa superfícies claras, bordas suaves, cantos arredondados, bastante espaço em branco e laranja como destaque. As cinco imagens posteriores complementam essa direção para equipe, perfis, atividade e etiquetas.

Esses elementos são referência de composição e densidade. Textos, marca “Mova”, percentuais e números da imagem não são requisitos funcionais. O plano de fundo paisagístico pode ser explorado como ambientação opcional; legibilidade e área útil vêm primeiro. Assets e identidade finais devem ser próprios ou licenciados.

Na imagem, “Ready to Build” não significa conclusão. O produto proposto usa estados semanticamente explícitos, incluindo Concluída. O dashboard não copiará números estáticos da referência. Os quatro recortes não representam quatro rotas independentes: são enquadramentos para comunicar a interface e orientar a implementação.

### Evidência visual observada

| Região | Elementos observados | Decisão para o produto |
|---|---|---|
| Sidebar | Marca, controle de recolher, grupo Main, itens Home/My Tasks/Calender/Team/Docs/Reports, workspaces aninhados, Add Project, Add Workspace e Support | Usar grupos com estado expandido/recolhido; corrigir o rótulo para `Calendar` na interface final |
| Cabeçalho | Breadcrumb `Workspace > Product & Technology > Green Campaign` e título/subtítulo do projeto | Breadcrumb deve ser navegável e refletir o escopo autorizado |
| Métrica | Cartão branco, ícone de pasta, menu, número grande, “completed”, barra segmentada laranja, total concluído, variação semanal verde e nota | Componente de métrica reutilizável; números vêm da API e mostram período/filtro |
| Quadro | Seletor Calendar/Board/List, colunas Backlog e In Progress, contador, adicionar, menu e cartões | Kanban deve manter rolagem horizontal e alternativa em lista em janelas menores |
| Cartão | Badge de prioridade, título, prazo, anexos, chips de área, avatares, comentários e progresso circular | Conteúdo acessível por texto; cor nunca é o único indicador |
| Ambiente | Paisagem ao redor, moldura branca translúcida e painel claro | Tratar cenário como direção visual opcional; não depender de imagem externa para legibilidade |

### Cinco referências adicionais · cargos e equipe

Imagens fornecidas pelo usuário em 22/10/2026, preservadas como referência documental. Sua inclusão não comprova licença para reutilizar fotos, marcas ou assets no software. O pedido textual define permissões; botões e textos presentes nas imagens não concedem capacidades extras.

| Referência | Elementos observados | Aplicação proposta |
|---|---|---|
| [1 · Equipe](referencias-visuais/01-equipe.png) | Cards de pessoas, cargo profissional, departamento, busca/filtros, alternância grade/lista e agenda | Team com filtros por área e cargo de acesso; Novo membro/Nova tarefa só para Admin/Coordenador no escopo. Cargo profissional é diferente de Admin/Coordenador/Usuário; telefone e vínculo empregatício não são campos obrigatórios |
| [2 · Atividade detalhada](referencias-visuais/02-atividade-detalhada.png) | Linha do tempo, menções, upload, reunião, responsável e horário | Direção para atividade recente da Home, com links autorizados; não importar exemplos de clientes, comentários ou backups como regras |
| [3 · Atividade por tipo](referencias-visuais/03-atividade-por-tipo.png) | Tabs Chats/Status/Uploads, eventos e solicitações | Proposta de filtros para atividade. Botões de aprovar ingresso são ilustrativos, sem novo fluxo obrigatório de aprovação. Não confundir feed com auditoria de segurança |
| [4 · Etiquetas de estado](referencias-visuais/04-etiquetas-de-estado.png) | Chips com texto, ícone, cores suaves e estados diversos | Todo=A fazer/Pendente, in_progress=Em andamento, in_review=Em revisão, done=Concluída. Submitted pode ser rótulo de envio para revisão; Failed/Expired são estados de operações/convites, não novas colunas do kanban. Sem depender só de cor |
| [5 · Perfis](referencias-visuais/05-perfis.png) | Diretório em tabela, pesquisa e avatar | Perfil profissional visível no mesmo servidor; sem expor IDs técnicos de analytics como dado principal. Session replay/analytics da imagem não são requisitos nem autorização para monitoramento |

### Perfil e chat · referências adicionais da v0.6

| Referência fornecida | Leitura visual | Aplicação ao produto |
|---|---|---|
| [6 · Perfil com capa](referencias-visuais/06-perfil-com-capa.png) | Capa larga, foto sobreposta, nome, cargo, localização e Edit Profile; indicadores e painéis | Perfil com nome/@, bio, foto/capa e cargo profissional; trocar horas/rating/projetos ilustrativos pelo summary de tarefas pedido. Não importar avaliação por estrelas, selo de verificação, coleta de horas ou clientes da imagem |
| [7 · Chat, Inbox e busca](referencias-visuais/07-chat-com-inbox-e-busca.png) | Sidebar com Inbox e badges, canais, busca central e painel de contexto/membros | Inbox com notificações pessoais; busca autorizada e sugestões de / e @ no compositor. A imagem não define comandos, regras de IA, bot, editor de scripts ou permissões; o catálogo é proposta textual RN-21/22 |

As duas imagens complementam as referências anteriores e estão no ZIP. Marcas, nomes, fotos e números são ilustrativos, sem autorização implícita para reutilizar seus assets no software.

### Tokens visuais iniciais

Os valores abaixo são aproximações de leitura da imagem, úteis para a primeira implementação e sujeitos a validação por screenshot. Não são extraídos de um design system oficial.

| Token | Valor inicial | Uso |
|---|---|---|
| `surface-app` | `#F7F7F5` | Fundo do painel principal |
| `surface-card` | `#FFFFFF` | Cartões, colunas e menus |
| `text-primary` | `#25272B` | Títulos e dados principais |
| `text-secondary` | `#777A80` | Metadados e descrições |
| `accent-orange` | `#F59A22` | Progresso e ação principal |
| `accent-green` | `#20B86A` | Variação positiva e estado de sucesso |
| `border-soft` | `#E3E3E1` | Divisores e contornos |
| `radius-card` | `16px` | Cartões grandes e colunas |
| `radius-control` | `10px` | Botões, tabs e campos |
| `shadow-card` | `0 1px 3px rgba(20,20,20,.08)` | Elevação discreta |

O componente de progresso segmentado deve expor valor textual e aria-label. O progresso circular do cartão é um resumo da tarefa e não altera a regra de progresso do projeto descrita no documento de requisitos.

## 2. Navegação lateral proposta

```text
Seletor de organização
Principal
  Home
  My Tasks
  Calendar
  Team
  Docs
  Reports
  Inbox [badge de não lidas]
Comunicação
  Chat
  Reuniões
Workspaces
  Design
    Projeto Site
  Marketing
    Campanha
  Desenvolvimento
    Plataforma
  RH [membros atribuídos e Admin do servidor]
Suporte
  Ajuda e suporte
  Configurações
Perfil e presença
```

Nomes podem ser traduzidos para Início, Minhas tarefas, Calendário, Equipe, Documentos e Relatórios. A decisão de rótulos finais não muda as rotas. Só aparecem espaços/projetos autorizados; Admin tem visão de todas as áreas do próprio servidor. “Meus projetos” é filtro de associação, sem criar cópias por usuário. Configurações separa Minha conta (todos) e Servidor/Cargos/Usuários (Admin); ocultar controles não substitui autorização na API.

## 3. Mapa de páginas

| Rota de interface proposta | Conteúdo e ação principal |
|---|---|
| `/sign-in` | Entrar e recuperar acesso |
| `/invite/:token` | Aceitar convite após autenticação |
| `/o/:orgId/home` | Prioridades pessoais, próximos eventos, atividade recente e acesso rápido à reunião |
| `/o/:orgId/my-tasks` | Lista consolidada por responsável e filtros |
| `/o/:orgId/calendar` | Agenda pessoal e eventos de projetos; visão mês/semana |
| `/o/:orgId/team` | Membros, áreas e papéis; administração conforme permissão |
| `/o/:orgId/team/:userId` | Perfil profissional de colega do mesmo servidor, com campos compartilháveis |
| `/o/:orgId/inbox` | Todas/Não lidas, filtro por tipo e links autorizados; estado de leitura pessoal |
| `/o/:orgId/docs` | Documentos acessíveis agrupados por projeto |
| `/o/:orgId/reports` | Indicadores e mapa de contribuições com período e escopo |
| `/o/:orgId/chat/:conversationId` | Histórico, texto/áudio/imagens/anexos e não lidas; aviso de acesso administrativo |
| `/o/:orgId/meetings` | Reuniões agendadas e recentes acessíveis |
| `/o/:orgId/workspaces/:workspaceId` | Visão da área, projetos, canal e membros |
| `/o/:orgId/projects/:projectId` | Resumo e abas Quadro, Lista, Calendário, Chat, Arquivos, Docs e Reuniões |
| `/o/:orgId/tasks/:taskId` | Link estável para tarefa; painel sobre contexto ou página direta |
| `/o/:orgId/meetings/:meetingId` | Prévia de dispositivos e sala |
| `/o/:orgId/support` | Ajuda e solicitações próprias |
| `/o/:orgId/settings` | Perfil, notificações e administração autorizada |
| `/o/:orgId/settings/server` | Nome, imagem e descrição do servidor; apenas Admin |
| `/o/:orgId/settings/members` | Cargos, edição e exclusão de associações; apenas Admin |

Rotas diretas revalidam associação. Recurso inexistente ou inacessível mostra estado genérico sem confirmar existência. A URL deve preservar filtros úteis sem incluir tokens ou dados sensíveis.

## 4. Tela de projeto

O topo mantém breadcrumb, título, descrição, membros e ação de convite autorizada. Indicadores propostos: progresso, tarefas em andamento e itens que precisam de atenção. Cada indicador abre sua lista filtrada. Abaixo: seletor de visão, busca e filtro; Nova tarefa e criação rápida só aparecem para Admin/Coordenador do escopo. Usuário responsável movimenta suas tarefas por mouse/teclado conforme RN-05; os outros cartões são de leitura. Arquivos permite navegar em pastas e enviar material; criação/organização das pastas exige coordenação.

Cartão exibe título, prioridade por texto e cor, prazo, número de anexos, responsáveis e checklist quando existir. Comentários e bloqueios têm rótulo acessível. Detalhe abre descrição, histórico, checklist, comentários e arquivos sem esconder o contexto do projeto. Busca, filtros e ordenação operam sobre o mesmo conjunto nas três visões.

## 5. Jornadas essenciais

### Entrada na equipe

Admin ou Coordenador convida → pessoa abre convite → entra ou cria credencial no provedor → confirma identidade → aceita → vê os espaços atribuídos. Coordenador convida sempre como Usuário e apenas para seu escopo. Antes de aceitar, a pessoa é informada de que Admin pode acessar chats de trabalho, inclusive diretos. Conta com e-mail diferente não consome convite; conta sem convite válido não recebe acesso.

### Uma entrega

Admin/Coordenador cria projeto → adiciona membros → registra briefing → cria e delega tarefa → Usuário responsável inicia → comenta e anexa material → submete à revisão opcional ou marca concluída → evento atualiza métricas/mapa. Usuário sem atribuição não altera status; reabrir tarefa exige coordenação. Erro preserva texto digitado.

### Reunião com contexto

Admin/Coordenador inicia reunião no projeto → participantes autorizados abrem a prévia, escolhem dispositivos e entram → compartilham tela → registram decisões em Doc → coordenação cria/delega tarefas → anfitrião autorizado encerra. Usuário pode entrar e participar, mas não agendar/iniciar sala por esse cargo. Criar ata/tarefas não exige gravação.

### Agendamento

Admin/Coordenador cria evento de projeto → define início, fim, timezone e convidados → solicita reunião integrada → convidados respondem → lembrete interno → entrada na sala. Usuário mantém lembretes pessoais e responde convites. Reagendar evento de trabalho exige coordenação, avisa convidados e invalida lembretes anteriores.

### Saída ou suspensão

Admin suspende membro → servidor recusa operações → conexões são desconectadas e participação em sala removida → cliente limpa dados de sessão/escopo → projetos preservam autoria histórica → tarefas sem responsável ativo entram em lista de atenção da coordenação.

## 6. Estados de interface obrigatórios

### Perfil ampliado

Cabeçalho: capa de fundo, foto, nome, @handle, cargo profissional, badge separado de cargo de acesso, localização opcional e bio. Editar perfil só no próprio perfil; edição administrativa de cargo fica em Servidor/Usuários, visualmente distinta. Nome/handle vazios ou duplicados recebem erro acionável, sem perder os demais campos. Sem capa/foto, usar fallback próprio; campos opcionais em branco não ganham dados inventados.

Abaixo: total de tarefas concluídas no período, summary anual por padrão com mapa diário inspirado no GitHub, filtro de período/escopo e legenda textual; cada dia abre lista autorizada. Foguinho mostra sequência atual e melhor sequência, com explicação de créditos, timezone e histórico considerado. Tooltip não é a única forma de ler números: fornecer tabela/lista equivalente por teclado/leitor de tela. Não exibir totais globais de projetos privados por trás de um filtro. Perfil próprio e visão de colega podem ter números diferentes conforme acesso; explicar o escopo antes de comparar.

### Compositor de chat

Ao digitar `/` no início do compositor, abrir lista de comandos permitidos com descrição, parâmetros e atalho de teclado; ao digitar `@`, sugerir pessoas/grupos elegíveis no contexto. Setas navegam, Enter seleciona, Esc fecha sem apagar rascunho. Menu usa nomes acessíveis e foco previsível. Comando de mutação abre prévia/formulário conforme RN-21, sem publicar o texto cru como mensagem e depois executar de novo. Texto comum pode incluir barra fora desse início sem ser interpretado como comando.

Menção selecionada vira token com nome/@ e referência interna à pessoa/grupo. Digitação livre não concede autoridade: só tokens reconhecidos/revalidados notificam; desconhecidos ficam como texto. Sugestões coletivas variam por hierarquia. Usuário pode mencionar um Coordenador/Admin participante individual, mas não convocar `@admins` ou `@todos`. Para Coordenador, a prévia de `@todos` explica que inclui apenas Usuários/Coordenadores elegíveis, excluindo Admins. Mudança de cargo/acesso antes de enviar produz erro, preservando rascunho. Não mostrar resultados de busca de outro servidor.

### Inbox

Entrada própria na sidebar e atalho no sino; badge é de notificações não lidas autorizadas, separado de mensagens não lidas por chat. Listar ator quando visível, tipo, data e recurso, com filtros Todas/Não lidas e por tipo. Ações: abrir, marcar lida/não lida e marcar todas como lidas até o cursor da consulta. O visitante não abre Inbox de colega pelo perfil, nem como Admin. Estados: vazio, nenhuma não lida, carregando, falha/retry e recurso que deixou de estar disponível. Abrir o painel não limpa badge automaticamente. Notificações novas após marcar todas permanecem não lidas.

**Chat e conta:** compor áudio requer iniciar/parar, ouvir prévia, descartar ou enviar; sem gravação contínua. Imagem tem prévia e alternativa textual informada pelo autor. Ao inspecionar chat sem participação, Admin vê modo “Acesso administrativo”, sem compositor ou simulação de participação. Remoção moderada mostra marcador, sem revelar texto removido. Team abre perfil profissional; Minha conta permite alterar apenas os próprios dados/preferências; Help gera protocolo acessível ao solicitante.

**Atividade recente, proposta a partir das imagens:** cartões com ator, ação, horário e recurso; filtros por tipo/data. Consultar autorização atual antes de mostrar título, trecho ou anexo, inclusive em totais. Admin pode ver atividade dos recursos sob sua administração; Coordenador/Usuário não veem eventos de escopos sem acesso. A ausência de permissão remove item e prévia, sem contornar isso por menções. Não implementar aprovações, automações ou monitoramento só porque aparecem nas imagens.

| Estado | Comportamento |
|---|---|
| Carregando | Skeleton sem números fictícios; área principal mantém estrutura |
| Vazio inicial | Explica o próximo passo com ação permitida |
| Sem resultado | Mostra filtros ativos e opção de limpar |
| Sem permissão | Mensagem genérica e saída para área acessível |
| Offline | Banner persistente; leitura em memória pode continuar; mutações bloqueadas |
| Reenviando mensagem | Estado pendente com tentativa/repetição e prevenção de duplicidade |
| Conflito | Preserva alteração local e oferece recarregar/comparar |
| Upload falhou | Mantém nome e motivo; permite repetir sem anexo duplicado |
| Sessão expirada | Recupera navegação após login, sem registrar rascunho sensível em disco |
| Serviço de chamada indisponível | Mantém tarefas/chat utilizáveis e permite tentar novamente |

## 7. Acessibilidade e adaptação

Alvo proposto: acessibilidade equivalente aos critérios WCAG 2.2 AA aplicáveis, validada durante implementação. Requisitos: navegação por teclado, foco visível, nomes acessíveis, contraste medido, status sem depender só de cor, `prefers-reduced-motion`, modais com foco controlado e confirmação de ações destrutivas.

Validar desktop em 1440×900, 1920×1080 e janela reduzida 1024×768, com zoom de 200%. Em largura pequena, sidebar vira gaveta e kanban permite rolagem horizontal com alternativa em lista. Não certificar uma versão móvel nesta fase. Captura de tela, áudio e vídeo precisam de validação no Electron instalado, além da interface executada no navegador.

## 8. Critério visual de aceite

Antes do fechamento da interface, comparar screenshots reais com a referência: hierarquia, espaçamento, densidade dos cartões, bordas, tipografia e destaque de ações. A imagem orienta o projeto; ainda não existe compromisso de reprodução pixel a pixel. Aprovação visual e aprovação funcional são verificações separadas.

## 9. Landing pública implementada no MVP

A entrada `/` ou `#landing` apresenta o Forma: finalidade, prévia ilustrativa
com abas Quadro/Conversa/Calendário, recursos, conta sem Studio, convite na
Inbox, orientação para desktop e FAQ. Links para `#login`, `#register` e
`#home` mantêm o fluxo existente. O Electron abre diretamente o aplicativo.

A página tem animações GSAP de entrada e scroll sempre ativas por pedido
explícito do usuário em 23/10/2026, substituindo a preferência automática e
o seletor anterior. ScrollSmoother suaviza o conteúdo no desktop em 1,1 s;
toque mantém acompanhamento direto. Há navegação suave entre seções,
barra de progresso, cartões em sequência e transformações com parallax em
desktop. O motor é encerrado ao sair da landing. Usa dados fictícios
identificados, tema claro temporário e menu
responsivo. Oferece download de um guia real em Markdown; não promete
instalador, planos pagos ativos ou chamadas remotas implementadas.

A especificação técnica, conteúdo, arquivos, manutenção e critérios de aceite
estão em `outputs/software-mvp/docs/landing-page.md`. Essa documentação da
implementação acompanha o MVP; o pacote editorial conserva este resumo.

## 10. Caminho de navegação e equipe no MVP

Workspace, área e projeto no topo são links funcionais. Workspace retorna
à Home; a área abre sua visão de projetos ativos visíveis, com links para
conversas e documentos; o projeto abre seu quadro. O último link identifica
a página atual. Área indisponível apresenta estado vazio, sem ampliar acesso.

A equipe exibe até 20 membros ativos por página, tanto em grade quanto em
lista. O 21º membro inicia a página 2. Busca e filtro de cargo são aplicados
antes da paginação e retornam à primeira página ao mudar. Redução da lista
ajusta páginas inexistentes; troca de Studio reinicia o estado. Rodapé informa
intervalo/total e oferece navegação anterior, próxima e por número quando
há mais de uma página. A paginação local usa o snapshot autorizado existente.

Detalhes e evidências: `outputs/software-mvp/docs/navigation-team.md`.


## Refinamento visual com referências — 26/10/2026

O pedido de aproveitar ideias dos nove mockups enviados foi aplicado à base web
local e ao código do aplicativo desktop. Foram aproveitados organização em cartões,
resumo profissional, detalhes laterais e agrupamento dos controles, mantendo marca,
cores, rotas e dados reais do Forma. Não são cópias de fotografias ou assets HYVE.

### Perfil

A identidade, foto/capa e métricas existentes permanecem. Os novos cartões mostram
função profissional, Studio, localização e fuso, com edição pelos controles existentes.
Campos ausentes têm estado vazio, sem inventar skills, aniversário ou presença online.
As áreas compartilhadas levam ao workspace correspondente. Entregas recentes mostram
até quatro tarefas com primeira conclusão creditada ao perfil e projeto ativo em
comum; abrem o detalhe da tarefa. Próximos eventos mostram até três eventos futuros
compartilhados, abrem a prévia e usam o fuso da conta que está consultando. O summary
de contribuições e o foguinho continuam disponíveis; não há ranking de produtividade.

### Workspace

A visão geral apresenta cor/identidade da área, membros ativos visíveis, quantidade
de projetos ativos, tarefas concluídas/total e documentos visíveis. A busca filtra
nome e descrição dos projetos dessa área, com estado vazio e restauração ao limpar.
Abas levam a visão geral, conversas e documentos da mesma área. Não há descoberta
pública de áreas ou entrada sem convite; os dados vêm do snapshot autorizado.

### Configurações do Studio

O formulário existente de nome, descrição, ícone e cor fica acompanhado por uma
prévia e resumo de áreas, projetos, documentos e conversas visíveis. Em telas menores,
o resumo e o formulário se empilham. O acesso continua restrito ao Admin. Convites
e auditoria preservam seus controles. Aparência e atualizador ficam na aba Minha
conta, evitando misturar essas preferências pessoais com a identidade do Studio.
Não foram adicionadas exclusão, exportação local ou integrações fictícias.

### Reuniões

A sala local apresenta conexão real, botão com número de participantes e lista
expansível com nomes do LiveKit, incluindo identificação da própria pessoa. A área
de vídeo permanece escura, com controles agrupados em faixa clara no tema claro:
microfone, câmera, tela e sair. Os controles ficam acessíveis em telas menores e
seguem o tema existente. Câmera e microfone continuam desligados ao entrar.
IA, transcrição, resumo automático e gravação dos mockups não foram implementados
neste recorte. Os limites de mídia/Internet permanecem no guia de reuniões.

### Implementação e verificação

Arquivos: People.tsx, WorkspacePage.tsx, StudioSettings.tsx, MeetingRoom.tsx,
meeting-room.css e reference-ui.css. Reutiliza snapshot, mutações, ícones e LiveKit;
sem novas dependências, banco ou permissões. Controles pertinentes: JUR-05 (escopo),
JUR-08 (origem dos materiais) e JUR-09 (teclado, foco e telas menores).

Validação desta rodada usa fixture isolado com contas fictícias; não altera o Studio
do usuário. Build web/desktop/API e testes existentes verificam regressões. A revisão
estática identificou o fuso dos eventos e a correção foi aplicada. A distribuição
0.2.1 existente não é reempacotada automaticamente por esta mudança de código.


## Criação e edição de Spaces — implementação local 0.26

Space representa a área de trabalho dentro do Studio. A listagem em #spaces
permite buscar nome/descrição, filtrar áreas vinculadas e abrir ou configurar uma
área autorizada. A criação pelo Admin tem nome, descrição, ícone, cor, capa
predefinida, seleção de pessoas do Studio e prévia em tempo real. Desktop usa duas
colunas; celular usa Informações, Membros e Configurações em três etapas.

A edição em #workspace-settings/ID possui Geral, Membros, Canais e Permissões,
resumo lateral e salvamento no backend. Geral salva identidade e fuso de referência;
Membros edita vínculos; Canais abre os controles existentes de canais do projeto;
Permissões explica os cargos herdados do Studio. Não há descoberta pública,
integração ou exclusão decorativa. Links exigem conta e autorização.

Adicionar à área não concede seus projetos existentes. Retirar alguém revoga os
projetos daquela área. Versão otimista e comparação da lista original impedem que
um formulário obsoleto sobrescreva acesso novo. Confirmação de senha recente é
exigida nas operações administrativas. Dados antigos permanecem compatíveis.
Controles: JUR-05, JUR-08 e JUR-09. O guia [Spaces](../software-mvp/docs/spaces.md)
detalha operação e limites; o fluxo online e o instalador anterior não foram atualizados.


## Sala em página própria — implementação local0.27

A apresentação modal da chamada foi substituída pela rota #meeting/ID dentro do
layout do Forma, com menu lateral e barra superior. Entradas por reunião imediata,
lista e prévia convergem nessa página. Sair retorna a Reuniões; navegar para outra
página desconecta a mídia. A reentrada começa com dispositivos desligados e exige
novamente sessão e acesso válidos. Erro tem opção de voltar. Chat e contexto do
projeto permanecem na página. No celular, controles ficam na base e navegação no
topo. Veja o [guia da sala](../software-mvp/docs/meeting-room.md).


## Painel contextual do Space — implementação local0.28

Inspirado na composição visual enviada pelo usuário, #workspace/ID apresenta
cabeçalho, abas de conteúdos, saudação, indicadores de entregas e conversas recentes.
Lateral reúne descrição, membros visíveis, documentos recentes e atalhos. Projetos
com busca/progresso permanecem na visão geral. Cada aba opera nos projetos/canais
autorizados da área; o feed exclui mensagens apagadas e conversas diretas. Em telas
menores, lateral empilha e abas/canais rolam horizontalmente. Configuração requer
Admin e criar tarefas/canais/reuniões exige projeto gerenciável. Nenhuma IA ou
presença simulada foi adicionada. Detalhes e limites no [guia de Spaces](../software-mvp/docs/spaces.md).


## Redesign visual — implementação local0.29

A interface aproxima a identidade da landing e referências do usuário: fundos
neutros, contraste tipográfico, botões monocromáticos e acentos discretos em
lavanda/pêssego. Navegação, cartões, formulários e tabelas recebem tratamento
compartilhado. A Home tem chamada compacta e atalhos de trabalho em vez da
ilustração grande. Tarefas, agenda, chat, equipe, Spaces e configurações mantêm
seus fluxos e escopos. Superfícies antigas usam tokens para evitar falhas de
contraste no tema escuro. Claro, Escuro e Híbrido continuam preferências locais.
A sala permanece em página própria. Landing mantém seus estilos e animações.
Veja [sistema visual, manutenção e limites](../software-mvp/docs/design-system.md).


## UX de navegação — implementação local0.30

A navegação principal prioriza o trabalho diário; módulos secundários ficam em
Ferramentas. O nome do Space passa a abrir a área; a seta só expande projetos.
Abas têm endereços próprios em #workspace/ID/TAB, preservados em reload e histórico.
Criar oferece ações compatíveis com cargo e contexto, mostrando o projeto inicial.
No celular, navegação inferior reúne Início, Tarefas, Spaces, Inbox e Perfil, sem
ocupar compositores ou controles de chamada. O breadcrumb identifica área e aba.
As validações do servidor e os formulários existentes permanecem. Guia detalhado:
[UX de navegação](../software-mvp/docs/navigation-team.md).
