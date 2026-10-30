# Landing page do Forma

## Destino de cadastro — 30/10/2026

O link `#register` abre o novo card central de cadastro, com Google Sans Flex,
Phosphor, campos claros e fundo gráfico original em CSS. O formulário de
login mantém sua apresentação atual. Nome, e-mail e senha continuam usando
o endpoint local `/register`, com a mesma sessão e redirecionamento à Home.
Não há migração de contas nem alteração da autenticação online de `#central`.

A senha pode ser exibida ou ocultada; mantém o limite de 10 a 128 caracteres.
O botão bloqueia envios repetidos durante a requisição e os erros permanecem
em um alerta acessível. O cadastro informa que a conta começa sem Studio e
recebe convites pela Inbox. A navegação acompanha mudanças do hash.

Conferência visual com o componente real e as folhas de estilo do aplicativo,
em página temporária isolada para preservar a sessão existente: desktop,
390px sem transbordamento horizontal, alternância da senha e retorno ao login.
Nenhuma conta foi criada nesse teste visual. A página temporária foi removida.

## Contagem regressiva de lançamento — 30/10/2026

Seção após o hero, com quatro blocos de dias, horas, minutos e segundos,
no canvas azul claro do produto. Data informada pelo usuário: 25/01/2027.
Como não foi informado um horário, foi adotado 00h no horário de Brasília:
`2027-01-25T00:00:00-03:00`, equivalente a 03h UTC. Essa suposição também
aparece na seção. A data canônica fica em `launch-date.ts`.

`LaunchSection.tsx` calcula o intervalo a partir do relógio do dispositivo
a cada segundo e ao retornar à aba; remove timer e listener ao desmontar.
Não depende de servidor ou coleta de dados. O timer não anuncia cada segundo
ao leitor de tela. Usa números tabulares, grade responsiva e link para a
demonstração existente. Ao chegar à data, permanece em zero e mostra
“Chegou o dia do lançamento.”, sem ativar cobranças nem afirmar disponibilidade
de recursos. Não há reinício artificial da contagem por visita.

Testes cobrem fuso, separação das unidades, último segundo e data alcançada.

## Adaptações da referência Human — 30/10/2026

Referência pública observada: https://black.humanacademy.ai/ em 30/10/2026.
Foram consultados o hero, a organização dos benefícios em mosaico, o seletor
de formações e a chamada flutuante. A adaptação ao Forma é original e usa
apenas React, CSS, Phosphor e o GSAP já instalado; não copia assets, marcas,
fotos, professores, depoimentos, textos de campanha, captura de e-mail,
contagem regressiva ou condições promocionais do site de referência.

- Mosaico no lugar do manifesto: seis superfícies conectam tarefas, chat,
  prévia de código, agenda, Studio e acesso; cada link tem destino existente.
- Seção `Workflows.tsx`: três botões Organizar, Conversar e Conectar trocam
  explicação, benefícios e uma ilustração textual. A seleção usa `aria-pressed`
  e um painel associado, com foco nativo por teclado. O fundo azul profundo
  dá contraste entre seções, mantendo a identidade clara no restante da página.
- Chamada flutuante: surge após o início da seção Produto e se oculta antes
  do CTA final. É controlada por ScrollTrigger e fica fora do conteúdo
  transformado pelo ScrollSmoother. No celular exibe apenas marca e cadastro.
  Não coleta dados nem inicia assinatura: leva ao cadastro já existente.

### Caminhos de entrada e índice do rodapé

Uma segunda seleção da referência usa a separação por público do trecho
`#para-voce` para organizar o fechamento em três cards: criar conta pessoal,
entrar em conta existente e conhecer os planos para trazer a equipe. Cada
card é um link nativo, com foco por teclado, e leva a uma rota já disponível.
No celular os cards ficam em uma coluna. Não há novas regras de acesso,
formulários, cobranças ou provisionamento de Studio nessa seção.

O rodapé apresenta um índice numerado com seis destinos: Produto, Recursos,
Como funciona, Planos, Dúvidas e Aplicativo Windows. A navegação de conta e
download permanece separada. Os números são decorativos para leitores de tela.

Verificação desta seleção: cards em desktop e viewport de 390 × 844px,
foco visível ao navegar pelo teclado e largura do documento de 375px no
celular, sem transbordamento horizontal da página.

Os limites da beta, os dois planos, o download e as rotas existentes permanecem.
Os grafismos continuam estáticos; a nova seção tem apenas transição de conteúdo
ao clicar. Conferência em navegador: seleção de Conversar no desktop e Conectar
no viewport de 390px, com chamada flutuante visível e largura do documento de
375px. A comparação não é uma cópia integral nem auditoria de acessibilidade.

## Redesign de 29/10/2026 — identidade atual do sistema

A versão atual acompanha o design do aplicativo: Google Sans Flex, canvas
`#f6f8fb`, superfícies brancas, bordas `#e2e8f1`, azul `#3477e9` e Phosphor Icons.
A composição roxo/coral e seus quadrados foram substituídos por uma apresentação
do produto. Não há novos assets externos, bibliotecas ou publicação.

### Composição

- Navbar branca com links públicos, login, download e menu móvel.
- Hero em duas colunas: “Seu time. Seu contexto. Tudo em Forma.” e um painel
  ilustrativo de boas-vindas com tarefas e encontro, identificado como prévia.
- Áreas de trabalho com ícones Phosphor, seguidas por um manifesto compacto.
- Prévia interativa clara: rail de ícones, navbar compacta, Quadro/Conversa/
  Calendário com navegação por teclado. Dados são fictícios e rotulados;
  nenhum nome, mensagem ou métrica de usuário real é carregado pela landing.
- Quatro cards de recursos: tarefas, conversas/código, encontros e Studios.
- Fluxo conta → convite → trabalho; download Windows; dois planos; FAQ;
  chamada final e rodapé. Os destinos públicos existentes são preservados.

### Escala e adaptação

Conteúdo com largura máxima de 1180px. Texto de 13–17px, títulos de seção
de 30–46px e hero de 44–76px conforme o viewport. Cards com raios de 12–20px,
botões com altura de 40–48px, espaçamentos coerentes com o aplicativo.
Hero, recursos, funcionamento, download e FAQ empilham em telas menores.
O quadro ilustrativo e a semana do calendário têm rolagem horizontal interna
no celular, preservando a largura do restante da página.

### Funcionalidades e limites preservados

Cadastro/login continuam nas rotas do app. Instalador direto
`/downloads/installers/Forma-Setup-0.2.1-x64.exe`, guia, limites de sincronização
e diferenças do piloto são mantidos. Essencial R$79/mês e Pro R$149/mês por
Studio continuam vindo de `PublicPlanCards`; proposta empresarial permanece
separada. Este redesign não ativa checkout, cobranças ou provisionamento.

GSAP mantém entrada, revelação por scroll, progresso e transformações suaves
na prévia e nas ilustrações. ScrollSmoother continua em 1.1 no desktop e
rolagem nativa no toque. O painel decorativo do hero é estático. Os elementos
de FAQ/instalação usam details/summary e o demo conserva o comportamento de
teclado. Os controles JUR-08 e JUR-09 continuam pertinentes; os checks de
build e rotas não constituem auditoria completa de acessibilidade visual.

Arquivos principais: `LandingPage.tsx`, `ProductDemo.tsx`, `landing.css` e
`useLandingMotion.ts`, em `apps/web/src/landing`. A folha de estilos foi
reescrita como uma composição única, em vez de acumular outra camada sobre
a antiga. O build desktop continua excluindo a landing.

### Verificação concluída em 30/10/2026

Typecheck e builds web/desktop/API passaram. Os três testes de rotas públicas,
exclusão da landing no desktop e oferta de planos passaram, assim como os
18 testes documentais. Documentação regenerada e `--check` aprovado.
No navegador local foram conferidos hero e prévia em desktop, abertura do
menu em largura de 390px, navegação por âncora e troca para Conversa e
Calendário. A largura do documento no teste móvel foi de 375px para um
viewport de 390px, sem transbordamento horizontal geral. Duas colisões
visuais foram corrigidas nessa conferência: classe genérica do checkbox
ilustrativo e espaçamento de textos com quebra de linha ocultada no celular.
Não houve publicação ou ativação comercial.

## Histórico — redesign de 26/10/2026, referência Labrina

Referência visual consultada no navegador: https://labrina.framer.website/ em
26/10/2026. Foram observados a abertura centralizada, espaço em branco, títulos
amplos, geometria roxo/coral, botões arredondados e ritmo editorial das seções.
A implementação é original em React/CSS/GSAP. Não foram copiados código,
fotografias, fontes, depoimentos, logos de clientes ou resultados da referência.
Os controles pertinentes são JUR-08 (origem de materiais) e JUR-09 (acessibilidade).

### Estrutura daquela versão

1. Cabeçalho: marca Forma, produto, recursos, como funciona, planos, dúvidas,
   login e acesso ao download; menu expansível em telas pequenas.
2. Abertura: “Menos abas abertas. Mais ideias ganhando forma.”, grafismos
   estáticos, CTA para conhecer e atalho para a seção do instalador.
3. Áreas e manifesto: contexto do problema e públicos de design, marketing,
   desenvolvimento e pessoas; sem logotipos de clientes ou números de resultado.
4. Produto: demonstração existente com abas Quadro, Conversa e Calendário,
   identificada como ilustrativa e com dados fictícios.
5. Recursos: tarefas, chat/arquivos/código, reuniões no piloto local e Studios.
6. Como funciona: conta pessoal sem Studio → convite na Inbox → projetos.
7. Desktop: download direto real de Forma-Setup-0.2.1-x64.exe, guia expansível,
   requisitos e limites da versão instalada.
8. Planos: reutilização de PublicPlanCards; Essencial R$79 e Pro R$149/mês por
   Studio; proposta empresarial privada. Sem checkout ou cobrança ativados.
9. FAQ: conta, Studio, contratação, instalação, mídia e prévia de código.
10. Encerramento e rodapé: cadastro, login, download e navegação do produto.

### Movimento e implementação

Arquivos: apps/web/src/landing/LandingPage.tsx, landing.css,
useLandingMotion.ts. ProductDemo.tsx e PlanCards.tsx são reutilizados.
A landing permanece fora do build desktop. Não há novas dependências.

Os quadrados roxo/coral são estáticos, sem animação de entrada ou movimento
contínuo, conforme ajuste solicitado em 26/10/2026. GSAP anima a entrada de
títulos e conteúdo, revela seções no scroll, transforma as ilustrações no desktop e atualiza a
barra de progresso. ScrollSmoother usa smooth 1.1 no desktop; toque mantém
rolagem nativa. As animações continuam ativas conforme decisão anterior do
usuário. ResizeObserver atualiza alturas ao abrir FAQ/instalação; o contexto
GSAP, observer e smoother são limpos ao desmontar. Nenhuma chamada depende
de eventos privados ou dados reais do usuário.

Preservadas as rotas #landing, /produto, /recursos, /como-funciona, /desktop,
/planos e /perguntas (com prefixo #landing), além de #login, #register,
#home e #central para seus fluxos existentes. CTAs não criam Studios nem
iniciam assinaturas. A apresentação não promete chamadas pela internet ou
sincronização de trabalho no instalador local. A sala real do piloto web
é diferenciada da versão 0.2.1 disponível para download.

### Aceite e verificação

Validar build web/desktop/API, testes de rotas públicas e isolamento desktop,
menu mobile, ausência de overflow, âncoras e links diretos, três abas da prévia,
FAQ expansível, saída/retorno à landing e endereço real do instalador.
O servidor local é a prévia; esta mudança não publica o site nem gera um
novo instalador. As evidências desta rodada ficam no progresso comercial.

## Histórico anterior (não descreve o estado atual)


**Atualização 0.2.0 — 23/10/2026:** landing e download pertencem somente ao site. O CTA aponta a /downloads/installers/Forma-Setup-0.2.0-x64.exe. O desktop usa build Vite próprio (dist-desktop), sem esta página, CSS de marketing, public/downloads ou link Conhecer o Forma. Um único aplicativo atende todos os cargos; preparação operacional do primeiro Studio está no menu nativo do mesmo app, sem launcher/atalho separado. A versão instalada agora possui [atualizador manual/automático](updates.md) com feed local. Histórico anterior abaixo.

Implementação local aprovada em 22/10/2026. Objetivo: apresentar o produto,
explicar a entrada em uma equipe e orientar a execução no navegador e no desktop.
O público inicial continua sendo a equipe do usuário; a página não lança planos pagos.

## Critérios de aceite

- Explicar finalidade, tarefas, chat, documentos, agenda, Studios e permissões.
- Demonstrar o produto com dados fictícios, sem expor informações da instalação.
- Conectar os CTAs ao cadastro, login e aplicativo existentes.
- Explicar como executar Electron; oferecer guia real e declarar ausência de instalador.
- Usar GSAP na entrada e no scroll, sempre ativo conforme pedido de 23/10/2026, com limpeza ao desmontar.
- Adaptar navegação e conteúdo a telas pequenas; manter controles por teclado.
- Documentar conteúdo, rotas, manutenção, dependências e limites de publicação.

## Conteúdo e experiência

| Seção | Conteúdo e interação |
|---|---|
| Cabeçalho | Marca, produto, como funciona, desktop, dúvidas, entrar e começar |
| Apresentação | “Menos ruído. Mais trabalho que flui.”; cadastro e prévia do produto |
| Produto | Dashboard ilustrativo; abas funcionais Quadro, Conversa e Calendário |
| Áreas | Design, marketing, desenvolvimento e pessoas como exemplos de uso |
| Recursos | Tarefas com responsáveis; chat e código; agenda; Studio, perfil e aparência |
| Como funciona | Conta pessoal sem Studio → convite na Inbox → trabalho em equipe |
| Desktop | Navegador, Electron local, download do guia e instruções expansíveis |
| Dúvidas | Finalidade, cadastro, criação de Studio, download, código e mídia de reuniões |
| Encerramento | CTA de cadastro; rodapé com acesso e guia |

Números, pessoas e entregas da prévia são inventados e identificados como tal.
As abas não gravam dados e não fazem chamadas à API. Não há depoimentos,
contadores comerciais, logos de clientes ou promessas de disponibilidade inventadas.

## Rotas e entrada

| Endereço | Resultado |
|---|---|
| `/` ou `#landing` | Landing, mesmo com sessão existente |
| `#landing/produto` | Prévia interativa |
| `#landing/recursos` | Recursos |
| `#landing/como-funciona` | Passos para começar |
| `#landing/desktop` | Execução e guia |
| `#landing/perguntas` | Dúvidas |
| `#landing/unknown` | Início da landing |
| `#login`, `#register` | Fluxo existente; cadastro abre no modo correto sem sessão |
| `#home` e demais rotas privadas | Aplicativo e autorização existentes |

`Entry` escuta `hashchange` e decide entre landing e aplicativo. A landing é
carregada com `React.lazy`/`Suspense`: não depende da inicialização da API.
O login concluído navega para `#home`. Com sessão ativa, os links de acesso
abrem a conta existente. O Electron abre `#home` por padrão, preservando a
entrada direta no trabalho. A landing usa tema claro apenas enquanto montada
e restaura a preferência anterior na saída, sem alterar o armazenamento local.

## Código e responsabilidades

| Arquivo relativo a `apps/web/src` | Responsabilidade |
|---|---|
| `landing/LandingPage.tsx` | Texto, navegação, seções, FAQ e CTAs |
| `landing/ProductDemo.tsx` | Três vistas ilustrativas com estado local |
| `landing/useLandingMotion.ts` | Ciclo de vida das animações GSAP |
| `landing/routes.ts` | Identificação das rotas públicas |
| `landing/landing.css` | Estilos isolados por `.forma-landing` e prefixo `lp-` |
| `main.tsx` | Entrada pública e aplicação autenticada |
| `Auth.tsx` | Modo inicial de cadastro e link para conhecer o produto |

O arquivo público `apps/web/public/downloads/forma-guia-desktop.md` é copiado
pelo Vite para `dist/downloads/forma-guia-desktop.md`. Os links de download
usam a mesma origem. O guia é Markdown legível, não um executável.
Não inclui credenciais, caminho pessoal ou base da equipe.

## Direção visual e adaptação

Fundo marfim, texto verde escuro, destaque laranja da marca e cartões em tons
suaves de verde, areia, azul e lilás. A prévia contrasta com uma janela escura.
Tipografia usa a pilha local; ilustrações são HTML/CSS/SVG e ícones Lucide.
Não há carregamento de fotografias, fontes ou scripts por CDN.

O container limita largura e mantém margens fluidas. Breakpoints em 1050,
760 e 390 px reorganizam grids, escondem a sidebar ilustrativa e oferecem
menu móvel. As funções reais continuam nos CTAs; ilustrações decorativas
não simulam ações inexistentes. A landing não herda a moldura do aplicativo.

## Animações GSAP

Dependência instalada: GSAP 3.15.0, registrada no lockfile. ScrollTrigger vem
do mesmo pacote. O campo `license` do pacote referencia a
[licença padrão do fornecedor](https://gsap.com/standard-license).
Não presumir licença MIT para essa dependência.

| Elemento | Movimento |
|---|---|
| Navegação | Entrada vertical de 18 px, opacidade, 0,65 s |
| Texto da apresentação | Entrada de 30 px, 0,8 s, stagger de 0,1 s |
| Janela ilustrativa | Entrada de 65 px, perspectiva leve, 1 s |
| Notas flutuantes | Escala/opacidade/deslocamento, stagger de 0,12 s |
| Seções | Revelação de 32 px ao alcançar 90% da altura visível, uma vez |
| Órbita decorativa | Rotação e deslocamento vinculados ao scroll em desktop |

A partir do pedido de 23/10/2026, as animações ficam sempre ativas. O seletor,
a leitura de `prefers-reduced-motion` e o uso da preferência salva foram removidos.
A órbita exige também largura mínima de 900 px. O hook retorna
`media.revert()` para desfazer animações/ScrollTriggers na desmontagem e
suportar React StrictMode. Conteúdo não depende de CSS com opacidade zero.
Essa escolha explícita substitui o comportamento anterior de redução automática
somente na landing; nenhuma preferência do sistema operacional é modificada.

Referências técnicas consultadas: [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/)
e [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/).
Context7 não estava disponível na sessão; a consulta foi à fonte oficial.

## Acessibilidade e privacidade

Cabeçalho, navegação, main e footer semânticos; um h1 e seções hierárquicas.
FAQ e instruções usam `details/summary`, operáveis por teclado. Menu tem nome
e estado expandido. Abas têm associação tab/tabpanel, seleção, foco móvel,
setas esquerda/direita e Home/End. Há link para pular ao produto e foco visível.
Semântica e adaptação são controles implementados, não certificação WCAG.

A página não adiciona analytics, cookies comerciais, formulário de leads,
rastreamento ou acesso a dados pessoais da API. O login mantém os controles
existentes. As normas e controles do capítulo 12 continuam sendo referência;
esta alteração não estabelece conformidade jurídica nem autoriza publicação.

## Execução e manutenção

Na pasta `outputs/software-mvp`, com Node.js 22.12+:

```powershell
npm ci
npm run dev
npm test
npm run build
npm run desktop
```

Abra `http://127.0.0.1:5173/`. Para servir o build local com a API,
use `npm start` e a porta configurada. Não configure dados de produção para QA.

Para editar textos, altere `LandingPage.tsx`; para mudar a simulação,
`ProductDemo.tsx`. Preserve a indicação de dados fictícios. Ao adicionar seção,
atualize também `routes.ts`, navegação e teste de rotas. Ao trocar guia ou
distribuir instalador, valide o arquivo real antes de alterar o CTA e mantenha
visíveis requisitos, plataforma e estado da versão. Instalador assinado,
atualização automática, hospedagem pública, domínio, SSR/SEO avançado e
integração de mídia não foram entregues por esta landing.

## Validação

Teste `tests/landing-routes.test.ts` cobre entrada pública, seções, fallback e
preservação dos links privados. Executar a suíte completa e build do MVP.
Conferir no navegador: apresentação, três abas, FAQ, menu móvel, navegação,
guia real, CTAs e retorno ao aplicativo. Registrar evidências finais em
`work/mvp-progress.md`; nenhuma alteração da base é necessária para esses checks.


## Histórico: ampliação de movimento — 23/10/2026

O comportamento atual está descrito em “Animações permanentes e smooth scroll”.
As seções históricas seguintes documentam a evolução anterior.

Navegação de seções usa ScrollToPlugin com duração de 1,05 s e easing
`power3.inOut`. `autoKill` permite interromper a rolagem ao interagir; o tween
é encerrado ao trocar seção ou desmontar a landing, sem restaurar a posição
anterior. Um listener acompanha mudanças na preferência de movimento e é
removido na limpeza. Não há interceptação da
roda do mouse ou de gestos touch. Não combinar com `scroll-behavior: smooth`
no elemento de rolagem, para evitar concorrência entre CSS e GSAP.

Barra laranja no topo acompanha o avanço da página com `scaleX` e scrub 0,2.
Cartões e passos entram em sequência, com deslocamento de 48 px e escala
0,97 → 1. Em desktop de pelo menos 900 px, a prévia ganha perspectiva
(escala 0,94 → 1 e rotação X de 8° → 0), as ilustrações têm parallax de
22 → -14 px e o ornamento final gira conforme o scroll. Cada efeito usa
alvo distinto da animação de entrada para evitar disputa de transform.

Efeitos de profundidade ficam fora das telas pequenas; com movimento reduzido
a barra é ocultada, os tweens não são criados e a navegação é instantânea.
Cards têm sombra suave no hover e setas dos CTAs se deslocam 3 px apenas
quando o dispositivo permite hover e movimento. Os efeitos não alteram
permissões, cadastros ou dados da equipe.

Fonte oficial adicional: [ScrollToPlugin](https://gsap.com/docs/v3/Plugins/ScrollToPlugin/).


## Histórico: controle de animações no localhost

A implementação anterior condicionava todos os efeitos exclusivamente à
preferência do sistema. No navegador observado, `prefers-reduced-motion: reduce`
estava ativo; por isso nenhum tween era criado, mesmo com o bundle atualizado.

O seletor fixo “Animações” oferece Sistema (padrão), Ativadas e Reduzidas.
A opção Ativadas habilita GSAP, navegação suave e CSS de movimento somente
na landing, sem modificar preferências do Windows. A opção Reduzidas encerra
os efeitos e restaura os estilos pelo contexto GSAP. Sistema acompanha
alterações da preferência do navegador. A escolha fica em
`localStorage['forma.landing.motion']`; erro de storage mantém a escolha
na sessão da página. Valor ausente/inválido volta para Sistema.

Para visualizar: recarregue a landing e selecione Animações → Ativadas no
canto inferior direito. A mudança recria os efeitos; a navegação de seções
e a barra de progresso passam a funcionar mesmo com redução no sistema.
Teste de política cobre as seis combinações entre escolha e preferência,
além de valores inválidos.

### Conferência posterior no navegador — 23/10/2026

A aba aberta ainda executava `index-Dv23LB1g.js`, anterior ao seletor, e
reportava movimento reduzido. Após recarregar, carregou `index-CxHFB7E-.js`;
o seletor apareceu e foi alterado para Ativadas pela interface. Confirmados
`data-motion="full"`, estilos GSAP e console da página sem erros/avisos.
Ao navegar para Como funciona, o scroll avançou de 0 a 2474 px e a barra
de progresso mudou de escala 0,0051 para 0,5808. Os três passos terminaram
visíveis com opacidade 1. Essa conferência substitui a pendência anterior
para esse fluxo; não constitui auditoria exaustiva de acessibilidade.

Uma aba já aberta continua executando seu JavaScript antigo até recarregar.
Naquela versão, Sistema/Ativadas/Reduzidas era uma escolha local por origem.
O pedido posterior de animações permanentes removeu esse seletor.

## Animações permanentes e smooth scroll — comportamento atual

Pedido explícito: manter os efeitos sempre ativos. Não há seletor nem leitura
de `forma.landing.motion`; escolhas anteriores em storage não desativam os efeitos.
Os antigos helpers/testes de preferência foram removidos com essa funcionalidade.

`ScrollSmoother` é importado do GSAP 3.15.0 já instalado, sem nova dependência.
A estrutura contém `.lp-smooth-wrapper` e `.lp-smooth-content`; a barra fixa
permanece fora do conteúdo transformado. Configuração: `smooth: 1.1`,
`smoothTouch: false`, `effects: false`, `normalizeScroll: false`. A rolagem
usa a posição nativa e interpola o deslocamento visual no desktop. Em toque,
o conteúdo acompanha diretamente o gesto. Profundidade continua limitada
ao breakpoint desktop, enquanto revelações funcionam nas demais larguras.

As âncoras usam `ScrollSmoother.offset` para calcular a posição lógica do
destino antes de animar o scroll com ScrollToPlugin. `ScrollTrigger.refresh()`
sincroniza o layout na inicialização. Ao desmontar, o contexto é revertido,
o tween de navegação é encerrado e `smoother.kill()` restaura os estilos de
rolagem. FAQ e conteúdo expansível são acompanhados pelo motor de layout.

Fonte: [ScrollSmoother oficial](https://www.gsap.com/docs/v3/Plugins/ScrollSmoother/).
Verificação local: motor ativo e seletor ausente; ao rolar, scrollY mudou de
2474 para 2998 enquanto o conteúdo ainda interpolava de -2474 para -2998 px.
A âncora Desktop terminou com topo a cerca de 0,06 px do viewport.

## Atualização desktop — 23/10/2026

A copy agora apresenta uma prévia portátil Windows fornecida pela administração, com perfil separado e execução por Forma.exe. O CTA ainda baixa o guia Markdown; o ZIP não foi hospedado publicamente e nenhum link fictício de instalador foi criado. O guia inclui Administrar-Studio.cmd, backup com aplicativo fechado e ausência de sincronização, assinatura/updater e instalador. Operação em [desktop.md](desktop.md).

## Download direto do instalador — 23/10/2026

Esta entrega substitui o comportamento anterior de oferecer somente um guia. Cabeçalho Baixar app aponta à seção Desktop. CTA Baixar para Windows e link do rodapé usam /downloads/installers/Forma-Setup-0.1.0-x64.exe com download. O guia Markdown permanece em Como instalar e começar e no rodapé. Textos e FAQ explicam instalação por atalho, sem Node, dados locais e ausência de sincronização.

A rota de binário não é âncora, modal, link externo ou ação autenticada: entrega o EXE diretamente. Binário e SHA-256 vivem em release/downloads; Nest serve attachment e Vite encaminha o mesmo caminho. Não copiar o EXE para apps/web/public nem dist, pois isso o colocaria dentro de sua próxima distribuição desktop.

Gere/atualize o artefato com npm run desktop:installer antes de disponibilizar esta versão da landing. O comando não publica em hospedagem externa. O teste HTTP verifica bytes reais, attachment, Range e 404; localhost entregou 133.501.480 bytes com o hash do arquivo original. O navegador exibiu o CTA e o clique foi exercitado. Limites de instalação e evidências em [desktop.md](desktop.md).

## Planos comerciais —26/10/2026

A seção Planos (#landing/planos) apresenta Essencial R$79/mês e Pro R$149/mês,
limites por Studio e solicitação empresarial privada. O catálogo vem do backend;
na ausência dele há fallback informativo. O aviso de preparação e botões
indisponíveis impedem interpretar a página como checkout já aberto. Não há
promessa de chamadas prontas. Ver [assinaturas](billing.md).
