# Revisão da estrutura — 23/10/2026

Conclusão: a organização atual atende a um MVP local. Não é necessário reorganizar todo o projeto nem adotar microsserviços ou um gerenciador de monorepo agora. A principal lacuna para o produto de equipe é o backend compartilhado: cada instalação desktop ainda possui sua própria API/base.

## O que está coerente

| Parte | Responsabilidade real |
|---|---|
| apps/api/src | HTTP, autenticação local, autorização por organização/projeto, domínio e persistência |
| apps/web/src | Interface compartilhada de trabalho e diretório landing exclusivo do site |
| apps/desktop | Janela Electron, bridge limitada, ciclo de vida do servidor local e integração com Windows |
| packages/contracts | Tipos de domínio e respostas; não substituem validação em runtime |
| scripts | Build, pacote, instalador e verificação técnica |
| tests | Regressões de regras, isolamento, persistência, rotas e desktop |
| docs | Guias técnicos; capítulos do produto ficam em outputs/documentacao-software |
| dist / dist-desktop / dist-api | Artefatos gerados, distintos das fontes |
| release / .data / .npm-cache | Distribuição, dados privados e cache; fora do contexto de build e versionamento |

Há um único pacote npm na raiz do MVP, com lockfile único. A separação por apps é organizacional; não foram configurados pacotes npm independentes por app. Isso é suficiente para a escala atual.

Site e desktop possuem builds separados. O app desktop não importa a landing e não copia downloads, usa uma janela e atende todos os cargos. Rotas de API e política de acesso ficam no backend. Nada nesta revisão concede criação pública de Studios.

## Mudanças necessárias, em prioridade

1. **Antes de usar em equipe entre computadores: backend e dados centrais.** apps/desktop/main.cjs:47 cria createApp no perfil local; apps/api/src/store.ts mantém uma fila apenas por instância. Uma conta/convite de um computador não existe em outro. Isso é uma limitação assumida do piloto, mas não cumpre colaboração remota. Próximo incremento deve conectar os clientes a uma API comum, com identidade, banco e arquivos compartilhados, TLS e autorização central, mantendo o Electron como cliente. Uma URL em .env não resolve isso: as chamadas são relativas à origem e o override atual é só para loopback em desenvolvimento. Não apontar duas APIs para o mesmo JSON.
2. **Antes da oferta comercial: separar operador da plataforma de Admin de equipe por autenticação central.** O menu nativo atual controla a própria instalação usando acesso do usuário Windows, não uma credencial de operador remoto. É adequado apenas à fronteira local documentada. Não basta esconder esse menu para impedir criação de Studios em um serviço comercial.
3. **Antes de ampliar ERP/HRM: dividir arquivos por domínio, gradualmente.** app.ts agrega todos os endpoints em um Controller; actions.ts mistura despacho de tarefas, mensagens, cargos e comandos; Dialogs.tsx agrega formulários de vários módulos. Extrair auth/contas, tarefas, conversas, arquivos e CRM em módulos/serviços do mesmo monólito, preservando policy.ts e a transação comum. No React, agrupar funcionalidades por domínio quando forem alteradas. Não criar camadas genéricas ou extrair todos os componentes numa mudança única.
4. **Antes da distribuição externa:** validar instalador/upgrade/desinstalação em Windows limpo, acessibilidade, assinatura e atualização/rollback. Os smokes existentes exercitam o payload e processos reais, mas não comprovam os passos do instalador no Windows.

Não alterei dados, identidade, banco, serviços externos, permissões ou arquitetura de autenticação nesta revisão. A arquitetura central já proposta no capítulo 04 continua como evolução, não como funcionalidade pronta.

## Problemas corrigidos nesta revisão

| Evidência | Correção |
|---|---|
| .gitignore e .dockerignore não excluíam dist-desktop, release ou .npm-cache; variantes .env também faltavam | Exclusões adicionadas, mantendo .env.example como template distribuível e excluindo .npmrc |
| Dockerfile usava build completo, incluindo renderer desktop desnecessário ao servidor | Comandos build:web, build:desktop e build:api explícitos; build geral continua validando tudo, container usa web/API |
| API busca instaladores em /app/release/downloads, mas a imagem final/Compose não forneciam os arquivos | Bind somente leitura de ./release/downloads para esse caminho; volume forma-data preservado |
| .env.example sugeria reutilizar o servidor da landing no desktop | Orientação corrigida para permitir somente servidor de depuração do build desktop |
| ZIP documental referenciava guias do MVP ausentes do arquivo | Allowlist dos guias adicionada ao gerador, excluindo código, perfis, instaladores e segredos; regressão reproduziu o erro e verifica o pacote extraído |

Não apaguei os candidatos antigos de release. Eles ocupam espaço e merecem política de retenção com backup; removê-los não era necessário para corrigir o build. Mover o código de outputs/software-mvp para outro lugar também não traz benefício imediato e quebraria referências e scripts relativos.

## Operação Docker

No host Windows, gere o instalador com npm run desktop:installer antes de servi-lo pelo container. O arquivo fica em release/downloads e entra apenas como volume de leitura; não é incorporado na imagem. Sem o artefato, o download retorna 404. Não montar a pasta inteira release ou .data em /app nem apagar o volume forma-data para atualizar a imagem.

Docker não está instalado/disponível neste ambiente. Verifiquei o YAML e os caminhos/montagens, mas não executei docker build, compose up ou um teste HTTP dentro do container. Não houve instalação de ferramenta ou modificação de volumes.

Configuração baseada no [contexto e .dockerignore oficiais](https://docs.docker.com/build/concepts/context/) e em [bind mounts do Docker](https://docs.docker.com/engine/storage/bind-mounts/), consultados em 23/10/2026. Context7 indisponível.

## Verificações e alcance

Revisão de estrutura e fluxos em código, configuração, regras e documentação; não é auditoria completa de segurança ou certificação de produção.

- 63 testes da aplicação aprovados nesta revisão.
- Build geral aprovado com tipagem, site, desktop sem landing e bundles da API.
- YAML do Compose analisado; volume de dados existente preservado e instaladores em bind somente leitura.
- Regressão documental cobre inclusão de guias referenciados e exclusão de dados/segredos/código.
- Nenhum runtime do produto mudou: não foi necessário gerar um novo instalador só pelas correções de build/documentação.

18 testes documentais aprovados. O ZIP real v0.12 foi extraído em pasta temporária e passou no --check sem depender dos guias da árvore original. Banco remoto, e-mail, mídia multipessoa, pagamentos e módulos futuros não foram habilitados.
