# Navegação do topo e paginação da equipe

Atualizado em 23/10/2026. Implementação no MVP local.

## Caminho clicável

O topo é uma navegação identificada como “Caminho de navegação”. Workspace
abre `#home`; o nome da área abre `#workspace/:id`; o nome do projeto abre
`#project/:id`. O último link tem `aria-current="page"`. Links têm foco
visível e funcionam com teclado, histórico e abertura em nova aba.

A visão da área apresenta apenas projetos ativos presentes no snapshot
autorizado, com progresso calculado pelas tarefas visíveis e acessos às
conversas e documentos da própria área. Área ausente mostra estado vazio.
Não são ampliadas permissões nem feitas consultas a Studios diferentes.
Rotas de perfil ou outros módulos não herdam uma área por coincidência de ID.

Arquivos: `apps/web/src/Breadcrumbs.tsx`, `WorkspacePage.tsx`, integração em
`main.tsx`. Os links mantêm as rotas de hash existentes.

## Equipe

Grade e lista mostram no máximo 20 membros ativos por página. A pessoa 21
começa a página 2; a 41 começa a página 3. Busca por nome/@/cargo profissional
e filtro de cargo de acesso são aplicados antes de dividir os resultados.
Mudar busca ou cargo retorna à primeira página. Trocar grade/lista mantém
a página. Ao reduzir a equipe, uma página que deixou de existir é ajustada
para a última disponível; a troca de Studio reinicia a paginação.

O rodapé informa o intervalo e o total, com anúncio acessível das mudanças.
Acima de 20 resultados, mostra Anterior, Próxima e números de página, com
extremos desabilitados e página atual identificada. Em listas grandes,
limita a janela de números e oferece primeira/última. Até 20 resultados,
mostra só o intervalo. Sem resultados, mostra 0 membros e o estado vazio.

Arquivos: `People.tsx`, `TeamPagination.tsx`, `teamPaging.ts`, `pages.css`.
A paginação é local sobre o snapshot já entregue pela API; não reduz o
volume de membros transferidos. Uma futura paginação no backend precisa
de contrato e consultas próprios. Não foram criados membros na equipe real.

## Verificação

Testes de limites: 0, 1, 19, 20, 21, 40 e 41 membros; ausência de duplicação
ou perda; página inválida e ajuste após filtro/redução. Testes do caminho
cobrem projeto, área, conversas e ausência de pais inventados.

QA visual isolada na porta 4190 com 41 membros fictícios: 20/20/1 nas três
páginas, troca para lista, busca e filtro a partir da página 3. Projeto →
área exibiu apenas o projeto correspondente. A fixture de manutenção está
em `work/team-navigation-qa.ts`; grava em diretório temporário próprio,
sem ler a base `.data` da equipe.


## UX de navegação — revisão0.30,27/10/2026

A navegação principal concentra Início, Minhas tarefas, Inbox, Calendário, Spaces e
Equipe. Conversas e Reuniões continuam visíveis; Documentos, Relatórios e os módulos
de gestão autorizados ficam no grupo Ferramentas, que abre ao entrar nessas rotas.
Nada é removido do produto ou liberado a outro cargo.

Na lista lateral de Spaces, clicar no nome abre a área. A seta independente
expande/recolhe seus projetos, com aria-expanded e aria-controls. A área atual
expande por padrão, respeitando escolha manual de recolhimento. Ver todos os
Spaces leva à lista com busca. Chat da área e Documentos abrem as abas do Space.

Abas usam #workspace/ID/overview, /chat, /tasks, /docs, /files e /meetings. Endereço,
recarregamento e histórico mantêm a aba; valor desconhecido usa visão geral. O
breadcrumb mostra Início, área e aba, com links e indicação do destino atual.
Rotas antigas de conversas/documentos da área continuam aceitas.

Criar, na barra superior, oferece Nova tarefa, Reunir agora, Agendar encontro e
Novo documento quando existe projeto ativo gerenciável. No contexto de área ou
projeto, a seleção inicial segue esse contexto. O formulário existente pode
permitir escolher outro projeto autorizado. Novo Space é exclusivo do Admin.
Usuário sem permissão de gestão não recebe esse menu. A apresentação não substitui
a autorização do backend, que continua validando a operação.

O seletor identifica o projeto, foca a primeira ação e fecha com Escape ou clique
externo; Escape devolve foco ao botão. O usuário pode navegar normalmente por Tab.
Cada ação reutiliza os formulários existentes, sem criar dados até confirmar.

Em telas até900px, a navegação inferior oferece Início, Tarefas, Spaces, Inbox e
Perfil. Inbox mantém contagem pessoal. A barra reserva espaço, incluindo safe-area,
e fica oculta nas páginas de chat e reunião para não sobrepor compositores ou
controles de mídia; o menu superior continua disponível nesses contextos.

Implementação: AppNavigation.tsx, navigation.ts/css e integração em main.tsx,
WorkspacePage.tsx e Breadcrumbs.tsx. Sem nova dependência, schema ou serviço.
Testes cobrem cargo, área/projeto, projeto arquivado, abas e breadcrumbs. QA usa
fixture local fictício para entrada direta no Space, menu contextual, teclado,
reload/voltar e mobile. As fontes desktop/web mudaram; instalador e sessão online
separada não foram substituídos. Controles JUR-05 e JUR-09.


Resultado desta rodada:151 testes Node e18 documentais aprovados; builds web,
desktop e API concluídos. QA confirmou Space pelo nome, aba preservada no reload
e no botão Voltar, Escape com retorno de foco e criação de tarefa fictícia com
projeto inicial correto. Em320/390px não houve overflow horizontal da página.
Aviso de sucesso ficou a88px da base, acima da barra inferior, sem sobreposição.
Capturas locais: navigation-ux-desktop.png e navigation-ux-mobile.png em work/beta.
