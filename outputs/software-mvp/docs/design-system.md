# Sistema visual do Forma

Revisão visual de 29/10/2026. O usuário ampliou o redesign Hive às páginas,
modais e áreas restantes. Esta ampliação substitui a restrição anterior de
aplicar o shell apenas a Home, Inbox, tarefas e calendário.

## Direção

Google Sans Flex, canvas cinza frio, cartões brancos, superfícies secundárias em
azul suave e ações principais azuis. Temas escuro e híbrido usam tokens próprios.
Prioridades e estados preservam cores semânticas. Não foram adicionadas bibliotecas.

## Ampliação para o sistema

`HiveShell` cobre as rotas privadas locais de Spaces, área/projeto, equipe,
perfil, chat, documentos, arquivos, reuniões/sala, relatórios, configurações,
suporte, clientes e comercial, além das quatro rotas iniciais. O menu Mais
ferramentas disponibiliza documentos, arquivos, relatórios e, conforme cargo,
clientes/comercial. Ações rápidas usam a rota completa para preservar contexto.

`hive-system.css` concentra os ajustes por domínio: superfícies, cartões,
tabelas, formulários, abas, estados vazios, chat, sala, CRM, autenticação,
conta pessoal e área online. A área online conserva sua navegação e contratos.
`Modal` usa o estilo Hive compartilhado em todos os formulários, mantendo
Escape, foco nativo do dialog, erros, envio e cancelamento. Detalhes de tarefa
continuam em drawer. Landing mantém sua apresentação própria.

Verificação desta ampliação: 157 testes passaram, incluindo renderização das
rotas privadas com os três cargos; typecheck e builds web/desktop/API passaram.
Inspeção visual no navegador não concluída: o controle da aba retornou
indisponível. Os testes de renderização não substituem comparação visual.

A Home substitui a ilustração grande por uma chamada compacta e atalhos funcionais
para tarefas, Spaces e reunião imediata para gestores. Indicadores, agenda e
próximas entregas continuam reais e autorizados. Não há nova regra de negócio.

## Componentes

Navegação lateral em cinza discreto, seleção suave, ícones finos, títulos com
hierarquia clara e barra superior branca. Botões, campos, cartões, tabelas e
modais compartilham cantos de8–15px, bordas sutis e sombras mínimas. Conteúdo tem
mais espaçamento; rótulos e metadados se diferenciam dos títulos sem cores fortes.

Tarefas, calendário, equipe, chat, Spaces, perfil, documentos e configurações usam
tratamento comum. A sala de reunião continua uma página; vídeo e controles de
mídia conservam a apresentação específica. Formulários ainda podem abrir em modal.
Controles de foco/teclado e redução de movimento existentes são preservados.

## Temas e implementação

Tokens em apps/web/src/design-system.css definem text, muted, line, surface, bg,
app-nav, app-selected, app-focus, app-ink e app-inverse. A camada é importada após
os estilos base em main.tsx. Os componentes antigos de styles.css, pages.css, dialogs.css e
chat.css passam a usar surface no lugar de fundos brancos fixos, evitando texto
claro sobre cartões brancos no modo escuro. Adaptadores explícitos cobrem cores
antigas de navegação, botões e seleção. Não remover os estilos de domínio: eles
continuam responsáveis por disposição, estados e interações.

Claro usa conteúdo claro; Escuro usa cinzas escuros com botões claros; Híbrido
mantém conteúdo claro com navegação escura. A preferência continua local ao
dispositivo. Capas e cores escolhidas pelo usuário não são sobrescritas.

A landing mantém composição e animações próprias, com seletores escopados. A camada
comum também fornece paleta aos contêineres da conta/Studio online; o trabalho
Supabase e a autenticação continuam separados, sem migração ou publicação.

## Verificação e limites

A conferência usa fixture local com pessoas e dados fictícios, sem tocar no Studio
real. Verificações: Home, tarefas, calendário, equipe, chat, Spaces, configurações,
modal de tarefa, Claro/Escuro/Híbrido e telas menores. Typecheck e builds
web/desktop/API verificam integração; testes existentes verificam regressões.
A conferência visual online autenticada e hardware real não fazem parte da prova.

O código web e as fontes desktop estão atualizados. O instalador0.2.1 anterior
não é substituído automaticamente. Não houve novo serviço, custo, deploy ou
alteração de permissões. Controles aplicados: JUR-05, JUR-08 e JUR-09. Isto registra
medidas de engenharia, sem declarar certificação de acessibilidade ou conformidade.


Resultado:147 testes Node e18 documentais aprovados; typecheck e builds
web/desktop/API concluídos. QA visual cobriu Home, quadro, calendário, equipe,
Space/chat, configurações e detalhe de tarefa. Claro, Escuro e Híbrido foram
conferidos; Home em390px e320px não apresentou transbordamento horizontal.
Revisão estática pontual não identificou regressão material nos fluxos alterados.

## Adaptação do Via Sync — 27/10/2026

Referência local: outputs/via-sync-app/src/styles.css e App.tsx do projeto
Via Sync. O Forma adota navegação lateral azul-marinho de 224px, seleção e
ações primárias azuis, fundo cinza frio, painéis brancos de 12px, cabeçalho de
66px e tipografia compacta. A identidade Forma e os fluxos de colaboração são
preservados. Não foram transferidos módulos de frota, dados ou credenciais.

A arquitetura permanece React/TypeScript: tokens em design-system.css,
estrutura compartilhada em main.tsx/AppNavigation.tsx, apresentação do shell
em operation-shell.css e layouts de domínio nos componentes existentes.
Isso adapta a separação do Via Sync entre navegação, contexto e páginas sem
substituir a autorização e os contratos específicos do Forma.

O botão Atualizar dados chama o refresh existente, bloqueia cliques enquanto
carrega e respeita redução de movimento. Ele atualiza os dados da tela;
a atualização do aplicativo continua em Configurações. Claro e Híbrido usam
conteúdo claro com navegação escura; Escuro mantém conteúdo escuro com azul.
O menu e a navegação inferior continuam responsivos. A landing permanece com
sua composição própria. Fontes e assets novos não são baixados.

Typecheck, builds web/desktop/API e 151 testes Node passaram. Os testes HTTP
e de persistência exigiram execução fora do sandbox Windows por restrições
de loopback e renomeação de temporários. O instalador anterior não é regenerado.

### Refinamento pelas referências claras do Via Sync

As capturas fornecidas em seguida substituem a referência de menu escuro no
modo Claro. A navegação local inicia em trilho de ícones de 76px, com nomes
acessíveis e dicas nativas. O botão Expandir navegação no cabeçalho revela o
menu completo, incluindo árvores de Spaces e Ferramentas. No celular permanece
o menu completo em gaveta e a barra inferior. Escuro e Híbrido preservam a
navegação escura. O estado compacto dura apenas a sessão da tela.

reference-refinement.css concentra o refinamento: superfícies claras, títulos
maiores, tabelas espaçadas e formulários com cabeçalho e rodapé destacados.
O Studio online recebe a mesma linguagem de painéis, cabeçalhos e seleção azul;
sua árvore permanece visível para manter acesso às áreas. A conta central recebe
campos consistentes. Não foram copiados dados, funções de frota ou textos sobre
SQLite. Reuniões continuam como página; detalhes de tarefa continuam em painel.

## Estrutura clara por contexto — 28/10/2026

As novas referências de tarefas e Inbox orientam uma evolução visual do Forma,
sem copiar arquivos, conteúdo ou recursos do Figma. A implementação original
fica em `apps/web/src/hive-structure.css`, carregada após as camadas anteriores.

- O trilho compacto passa a ter 72px em desktop, ícones amplos e foco azul;
  quando expandido, preserva a árvore de Spaces, projetos e ferramentas.
- O topo explicita a hierarquia de ação: `Criar` é a ação primária, enquanto
  atualização, Inbox e perfil são controles circulares. A busca pelo atalho de
  teclado continua disponível no produto.
- Minhas tarefas reúne os controles e o quadro em uma única superfície branca.
  Quadro, Lista, Calendário, arrastar e alterações de status continuam
  funcionando como antes.
- A Inbox preserva sua separação pessoal e autorização de recursos, mas ganha
  filtros em pílulas, itens mais legíveis e uma superfície de conteúdo mais
  calma. O atalho de convites pessoais continua abrindo a conta pessoal, sem
  expor dados de Studio sem autorização.
- Escuro, híbrido, rotas, permissões, dados locais, conteúdo online e
  comportamento mobile não são substituídos por essa camada. As próximas telas
  recebem composição própria a partir das referências que forem enviadas.

## Tipografia — 28/10/2026

O aplicativo carrega **Google Sans Flex** pelo Google Fonts no documento web e
usa `Segoe UI`, Arial e sans-serif como fallback. A família é herdada pelos
controles do produto; fontes monoespaçadas continuam reservadas para código e
pré-visualizações técnicas.

## Home pessoal sem Studio — Figma, 29/10/2026

O frame `67:1693` (Home sem Studio), arquivo Hive, foi implementado em
`NoStudioHome.tsx` e `no-studio-home.css`. A composição inclui trilho pessoal,
cabeçalho, saudação vazia e três cards de orientação. Os ícones exportados do
frame ficam em `apps/web/public/assets/figma/no-studio`.

A tela aparece na entrada de contas locais sem participação em Studio.
Entrar em Studio leva à Inbox de convites ou à lista de Studios; perfil,
aparência e saída mantêm as ações da conta. Áreas que dependem de Studio ficam
desabilitadas. Os cards levam ao guia, aos convites e aos planos. Nome e
contador de convites são reais. A saudação acompanha o texto do frame.

Este incremento é restrito ao frame indicado: as demais telas, inclusive
conta online e ambientes com Studio, preservam sua apresentação anterior.
# Hive — revisão de 29/10/2026

Refinamento pelas 13 imagens anexadas: cabeçalho com Studio à direita e navegação recolhível; quadro sobre superfície branca; metadados no topo do drawer; formulários centrais em duas colunas; popover ampliado com fechamento e leitura em lote; Inbox com filtro Lidas; conexão com seis células de código e campo separado para link; confirmação com avatar real. Home coloca membros/materiais na coluna intermediária. Código/link mantém a exigência de convite autorizado. Build web/desktop/API e 156 testes passaram após os ajustes; conferência visual final não realizada porque o controle do navegador retornou indisponível.

As rotas locais `home`, `my-tasks`, `inbox` e `calendar` usam `HiveShell`, com rail de 100px, Google Sans Flex, canvas `#f6f8fb`, azul `#3477e9` e superfície `#e9f0fd`. As outras rotas conservam o shell anterior.

Home usa três colunas responsivas com dados reais de tarefas, agenda, membros e documentos. O menu Criar reutiliza `quickActions` e suas permissões. Inbox mantém notificações e entrada para convites pessoais; marcar todas como lidas usa o cutoff do snapshot. O popover abre o contexto real da notificação.

Os diálogos de tarefa recebem variantes Hive somente quando abertos nessas quatro rotas. Perfil usa formulário de apresentação e confirmação após `profile.update`; a ação de foto/capa/@ mantém o editor anterior disponível. A conexão sem Studio orienta para convites autorizados; código/link sem endpoint não concede acesso.

Ícones e fundo do Figma ficam em `apps/web/public/assets/figma/hive/`. Estes arquivos são locais, sem URLs temporárias no runtime. O comportamento responsivo usa rolagem do rail no celular para manter todos os destinos acessíveis.

Validação funcional: suíte de 156 testes passou antes dos ajustes finais de revisão; build web/desktop/API passou. A conferência visual dos 12 estados ainda precisa ser completada antes de declarar fidelidade integral aos frames.

## Escala de interface e Phosphor — 29/10/2026

Chat dos Spaces: a aba Chat usa um layout dedicado `space-chat-view`, sem a coluna lateral de resumo do Space. Canais e mensagens possuem rolagem independente, e o compositor permanece no rodapé da conversa. A altura acompanha o espaço restante após o cabeçalho e as abas; não depende do antigo limite fixo de 650px. Tipografia de mensagens de 14px, cabeçalho de 17px e canais de 13px. Em telas estreitas, os canais passam para uma faixa horizontal. A seleção continua local ao Space, com o mesmo filtro `inContext`, ações de envio, arquivos, áudio, comandos e moderação. Informações do canal continuam disponíveis pelo botão próprio.

Correção de janela baixa/zoom: a grade reserva ao menos 460px para a área de chat e 220px para o histórico. A página permite rolagem vertical quando o viewport não comporta cabeçalho, abas e conversa, evitando comprimir as mensagens entre o cabeçalho e o compositor. No celular, a reserva também inclui a faixa horizontal de canais. O compositor foi compactado, mantendo sugestões de comandos/menções livres para abrir sobre o histórico.

Presença na Home e na equipe: avatar com ponto verde para conexão Online, cinza para Offline e legenda abaixo do nome; a conta atual usa Você. `/state` projeta as conexões Socket.IO autenticadas do mesmo Studio, revalidando a sessão antes de informar presença. O dado é efêmero, não cria histórico de atividade e acompanha a atualização periódica do snapshot. Sessões revogadas não contam como online. Sem informação do servidor, a interface mostra Estado indisponível. Em reunião e Foco não são simulados: ainda não há uma fonte compartilhada para esses estados. A indicação de conexão não mede disponibilidade ou produtividade.

O seletor com nome do Studio na navbar abre `StudioSwitcher`, usando o mesmo modal dos formulários de criação. Lista os vínculos retornados por `/account`, informa o cargo e destaca o Studio atual. A troca chama `/studios/select`, atualiza o snapshot e retorna à Home; o servidor revalida o vínculo. Erros permanecem no modal, e a seleção fica bloqueada enquanto a operação está em andamento. X/Esc/clique no backdrop usam o comportamento compartilhado do modal. O rodapé contém apenas Criar Studio: abre Planos na web e Planos e assinatura da conta online no desktop. O botão não amplia a permissão de criação nem ativa cobranças.

A entrada da conta pessoal abre a Home sem Studio (`NoStudioHome`), inclusive quando a conta já participa de Studios e retorna à área pessoal. Isso não remove vínculos nem altera a sessão: Meus Studios continua permitindo selecionar um Studio. Inbox, perfil e aparência permanecem acessíveis, com um botão Início para voltar à Home pessoal.

O shell da Home pessoal é compartilhado entre Início, Inbox, Meus Studios, Meu perfil e Aparência. Esses destinos ficam habilitados na barra lateral e indicam a tela atual; a navegação horizontal antiga foi removida. Os fluxos de convite, seleção de Studio, edição de perfil e preferência visual continuam usando as ações existentes. Áreas de trabalho que exigem Studio permanecem indisponíveis nesse contexto pessoal.

Chat e sala de reunião ocupam a área integral abaixo da navbar, com rolagem interna e sem o cartão/margem externa. O caminho de navegação retorna à navbar: na Home, Studio → Geral; nas outras telas, o breadcrumb reutiliza os destinos reais do contexto. A fonte do caminho é de 13px no desktop e 12px em telas estreitas. No celular, preserva-se o destino atual para manter os controles acessíveis. O card de boas-vindas mostra tarefas pessoais abertas, prazos vencidos no fuso do perfil, próxima entrega com prazo e próximo encontro, usando somente dados do snapshot autorizado e atalhos existentes.

Correção posterior: os badges numéricos do rail, filtros e cabeçalhos de colunas foram retirados; métricas do conteúdo continuam visíveis. O menu Mais ferramentas fecha ao clicar fora, pressionar Esc ou trocar de rota. Campos de busca usam apenas a borda externa, sem receber o fundo/borda dos formulários.

Esta revisão substitui as dimensões históricas acima. Todas as rotas privadas usam o shell Hive. A camada final `apps/web/src/ux-polish.css` organiza a escala sem alterar contratos, permissões ou persistência:

- Texto de interface de 14px, descrição de 15px, legendas de 12px, seções de 18–20px e títulos de página de 24–30px. Google Sans Flex permanece como família principal.
- Espaçamentos de 4, 8, 12, 16, 24 e 32px; controles de 40–44px; rail de 80px no desktop e navegação inferior no celular. Painéis usam raio de 16px e conteúdo com largura mínima zero para evitar expansão indevida.
- Home com cartões menos altos; quadro com rolagem horizontal restrita às colunas; Inbox com estados vazios compactos; calendário e formulários reorganizados em telas estreitas. O conteúdo tem um contêiner de rolagem, evitando disputa com o shell anterior.
- Modais compartilham escala de título, corpo e rodapé; descrição de tarefa ganha área maior. Drawer de tarefa adapta metadados para duas colunas no celular. A sala de reunião continua em página própria.
- Ícones React passam para `@phosphor-icons/react` 2.1.10, com aliases semânticos e tamanhos coerentes. Lucide foi removido. Rail e conta sem Studio também usam Phosphor; imagens de referência continuam disponíveis como arquivos históricos. Licença MIT preservada em `docs/licenses/phosphor-icons.txt` e na dependência.

Aceite funcional: preservar navegação, ações por cargo, filtros, criação/edição e builds web/desktop/API. Os checks automáticos não substituem a conferência visual de todas as rotas. O controle do navegador esteve indisponível nesta revisão; contraste, teclado e layouts em dispositivos reais ainda exigem conferência visual/manual.

