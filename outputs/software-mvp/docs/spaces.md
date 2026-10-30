# Spaces: criação e edição

Implementação local web e fontes desktop, 26/10/2026. Space é uma área dentro do
Studio; não cria empresa nem altera assinatura. As referências visuais do usuário
orientam composição e navegação, preservando marca Forma e capas próprias em CSS.

## Uso

1. Entre como Admin e abra Spaces na barra lateral ou o botão + ao lado de Spaces.
2. Informe nome (até80 caracteres), descrição (até500), ícone, cor e capa predefinida.
3. Selecione membros já existentes no Studio; o criador entra automaticamente.
4. Confira a prévia e o fuso, depois crie. No celular, avance pelas três etapas.
5. Na visão geral ou lista, abra Configurar Space para editar. Salvar alterações
   persiste a identidade e os membros; Cancelar volta à área.

Geral reúne identidade, endereço privado e fuso. Membros tem busca por nome, @ ou
e-mail disponível ao Admin. Canais lista conversas da área e dos projetos ativos,
abrindo os controles existentes; novo canal exige um projeto da área. Permissões
explica os cargos herdados, administrados no Studio. O resumo mostra apenas dados
reais no escopo autorizado, incluindo arquivos, projetos e documentos.

## Regras

- Somente Admin cria e edita Spaces do próprio Studio; outras contas acessam áreas
  autorizadas. Não há adesão pública. Pessoas externas precisam do convite do Studio.
- Limite desta beta:50 membros por Space, incluindo criador. Suspensos não recebem
  nova área; vínculo antigo pode ser preservado.
- Adicionar pessoa à área libera seu contexto de conversa, sem liberar projetos
  existentes. Remover pessoa retira também os projetos da área; outras áreas ficam.
- Vínculo direto permanece quando um Admin edita posteriormente acesso por projeto.
- Operações exigem sessão, origem válida, cargo atual e confirmação recente de senha.
  Se solicitado, preencha a senha no formulário e salve novamente.
- Alteração concorrente de identidade ou membros retorna conflito e pede recarregar.
  O rascunho fica na tela. Retry idempotente revalida autorização e não duplica área.

## Dados e limites

workspace.create/update validam campos estritos; update usa version e, ao editar
membros, expectedMemberIds da abertura do formulário. Workspace possui metadados
opcionais description, icon, cover, timezone, memberIds, createdAt, createdBy e
version, compatíveis com bases antigas. A criação gera conversa Geral da própria
área. Alteração da identidade e dos acessos participa da mesma transação e auditoria.

Capas são composições predefinidas; não há upload de imagem nesta entrega. Idioma e
início da semana exibidos seguem o comportamento existente, sem controles fictícios.
O fuso do Space contextualiza suas datas; a agenda pessoal mantém o fuso do perfil.
Excluir/arquivar área, automações e integrações não foram adicionados neste recorte.
Esta interface pertence à sessão local JSON; #central/Supabase usa fluxo separado.
O instalador0.2.1 disponível anteriormente não contém automaticamente esta mudança.

## Verificação

Testes de domínio cobrem criação, legado, serialização, negação por cargo/Studio,
campos inválidos, remoção com revogação, vínculos diretos, retry e conflito após
mudança de acesso. Testes gerais, typecheck e builds web/desktop/API verificam
regressões. QA de formulário usa contas fictícias em fixture local isolado.


Resultado em26/10/2026:147 testes Node e18 testes documentais aprovados; builds
web, desktop e API concluídos. No navegador, criação desktop/celular, edição de
identidade/membros, canal restrito da área e persistência após recarregar foram
verificados em fixture fictício. Em320px não houve transbordamento horizontal do
formulário. O pacote documental0.26 passou também após extração do ZIP.


## Painel do Space — revisão0.28,27/10/2026

A visão geral #workspace/ID reúne cabeçalho com identidade, capa decorativa original,
resumo do trabalho e abas Visão geral, Chat, Tarefas, Docs, Arquivos e Reuniões.
O painel lateral apresenta descrição, membros com link para perfil, documentos
recentes e atalhos com contagens. No celular, o painel lateral passa para baixo e
as abas/canais permitem rolagem horizontal.

Os indicadores usam tarefas não arquivadas de projetos ativos autorizados: abertas,
concluídas e percentual. Reuniões são encontros ainda não encerrados desses projetos;
documentos contam o mesmo escopo. O resumo de conversas mostra as cinco mensagens
recentes não apagadas dos canais da área/projetos ativos, excluindo conversas diretas.
Anexos conservam visualização e download privados existentes. Não há IA, presença
online ou tempo de foco simulados.

Chat reutiliza canais e envio existentes; criar/editar canal continua no Space e
limita projetos ao contexto da área e ao cargo. Tarefas reutiliza cartões existentes,
status com versão e detalhe. Docs reutiliza busca/edição existentes. Arquivos agrega
anexos dos projetos e conversas autorizados; envio continua pelo chat/projeto.
Reuniões abre a página própria da sala ou a prévia quando mídia não está configurada;
Reunir agora exige projeto gerenciável. Configurar Space continua exclusivo do Admin.

Ao trocar de área, a aba volta à visão geral e os filtros locais são reiniciados.
A lista de projetos com busca/progresso permanece na visão geral. Indicadores não
concedem novos acessos; todos os dados vêm do snapshot validado do Studio.

Verificação em fixture fictício: tarefas/documentos/reuniões da área, criação de
canal preservando rota e troca para Marketing sem mensagens/projetos da outra área.
Desktop e celular390px conferidos no navegador. Builds web/desktop/API e testes de
regressão validados. A interface pertence à sessão local; instalador e #central não
foram substituídos. Controles aplicados: JUR-05/08/09.
