# 02 · Requisitos e regras de negócio

Os requisitos de expansão RF-30 a RF-41 e regras RN-26 a RN-32 estão definidos no [capítulo 13](13-gestao-integrada-e-expansao.md). RF-30/31 têm um primeiro recorte local entregue, conforme a seção 9; demais módulos são planejamento posterior. As permissões específicas de RH e financeiro não decorrem automaticamente da inspeção administrativa de chats descrita abaixo.

## 1. Organização e autorização

**RN-01:** usuário pode pertencer a várias organizações no modelo, mas o primeiro piloto usa uma. Cada recurso pertence exatamente a uma organização. Trocar a organização ativa limpa resultados, caches e assinaturas anteriores.

**RN-02:** a hierarquia é organização → workspace → projeto → tarefa. Workspace agrupa uma área ou frente; projeto representa uma iniciativa. Um projeto pode envolver pessoas de várias áreas, desde que tenham acesso ao workspace e associação ao projeto.

**RN-03:** para Usuário e Coordenador, acesso ao workspace não concede automaticamente acesso a todos os projetos. Acesso ao projeto exige associação ativa a organização, workspace e projeto. Coordenador atua apenas em escopos que lhe foram atribuídos. Remover acesso do workspace suspende os acessos descendentes. Exceção explícita: Admin ativo pode acessar e administrar todas as áreas, projetos e chats da sua própria organização, sem associação artificial a cada recurso; a exceção nunca atravessa organizações.

**RN-04:** os cargos são **Admin**, **Coordenador** e **Usuário**, com códigos propostos `admin`, `coordinator` e `user`. Não há quarto cargo Owner/Manager. Permissões são cumulativas: Admin inclui Coordenador e Usuário; Coordenador inclui Usuário. O cargo pertence à associação na organização; acesso às áreas/projetos delimita o alcance do Coordenador e do Usuário. Negar por padrão toda ação não concedida.

| Ação | Admin | Coordenador | Usuário |
|---|---|---|---|
| Adicionar usuário por convite | Sim, no servidor | Sim, como Usuário e só para seus escopos | Não |
| Delegar/alterar cargos | Sim | Não, inclusive em convites | Não |
| Editar dados administrativos, suspender e excluir usuário do servidor | Sim | Não | Não |
| Configurar servidor, criar áreas e atribuir coordenadores | Sim | Não | Não |
| Visualizar todas as áreas, projetos e chats do servidor | Sim, inclusive chats diretos; acesso administrativo auditado | Apenas escopos atribuídos e chats dos quais participa | Apenas escopos atribuídos e chats dos quais participa |
| Criar projeto/gerenciar associações dentro de área existente | Sim | Sim, na área atribuída; sem ampliar o próprio acesso | Não |
| Criar/editar/delegar tarefas | Sim, no servidor | Sim, no projeto atribuído | Não |
| Marcar tarefa Em andamento ou Concluída | Sim | Sim, no projeto atribuído | Sim, se responsável ativo pela tarefa |
| Visualizar progresso e relatórios | Todo o servidor | Seus escopos | Próprias tarefas e resumos dos projetos acessíveis |
| Criar chats e pastas | Sim | Sim, nos escopos atribuídos | Não |
| Editar configuração de chat: nome, descrição e participantes | Todos os chats do servidor, respeitando coerência do escopo | Chats que coordena; participantes já autorizados | Não |
| Apagar mensagens de terceiros | Sim, em qualquer chat do servidor | Nos canais do escopo que coordena; sem moderar diretos alheios | Não |
| Enviar mensagens/comentários e editar/remover os próprios | Sim, onde participa | Sim, onde participa | Sim, onde participa |
| Agendar/iniciar/gerenciar reuniões de trabalho | Sim | Sim, no projeto atribuído | Não; pode responder convite e entrar |
| Entrar em meet | Sim, com ingresso autorizado na sala | Sim, com ingresso autorizado na sala | Sim, em projeto atribuído e sala autorizada |
| Enviar arquivos, vídeos, áudio e imagens | Sim, em destino autorizado | Sim, em destino autorizado | Sim, em destino autorizado |
| Visualizar perfil profissional de colega do servidor | Sim | Sim | Sim |
| Configurar próprio perfil, login e preferências | Sim, apenas a própria credencial | Sim, apenas a própria credencial | Sim, apenas a própria credencial |
| Enviar help e consultar solicitações próprias | Sim | Sim | Sim |
| Usar comandos `/` | Catálogo completo, dentro do servidor | Comandos pessoais e de coordenação no escopo | Comandos pessoais e ações permitidas sobre suas tarefas |
| Mencionar pessoa por `@handle` | Participantes autorizados no contexto | Participantes autorizados no contexto | Participantes autorizados no contexto |
| Menção coletiva por cargo/escopo | Todos os grupos autorizados | Usuários/Coordenadores do escopo, sem convocar Admins como grupo | Não; pode mencionar pessoa individual visível |
| Ler e organizar Inbox | Só a própria | Só a própria | Só a própria |

**Detalhes de engenharia propostos para tornar o pedido executável:**

- Coordenador adiciona novas pessoas sem conceder cargos superiores; associa apenas a áreas/projetos que coordena. Admin é o único que promove/rebaixa cargos. O último Admin ativo não pode ser excluído, suspenso nem rebaixado; criar o servidor designa seu primeiro Admin.
- Admin não lê senhas, tokens ou credenciais de outros usuários. Edição administrativa cobre cadastro profissional e associações do servidor; redefinição de senha usa recuperação pelo próprio titular. Excluir usuário remove acesso à organização, sem apagar conta global de outras organizações nem autoria em cascata; eliminação/anonimização segue RF-23/RN-19.
- “Editar chat” significa configurar o chat, sem reescrever uma mensagem de outra pessoa como se fosse o autor. Alterar participantes de um direto cria nova conversa, preservando a audiência histórica; chats de projeto/área não concedem acesso fora do escopo.
- Admin pode inspecionar diretos sem tornar-se participante nem enviar mensagens se passando por alguém. O aviso de uso explica esse acesso antes da entrada; a interface não promete sigilo exclusivo entre participantes. A leitura administrativa tem trilha mínima, sem copiar conteúdo para logs. Essa escolha de produto não certifica adequação jurídica ao uso real.
- “Configurações gerais do próprio login” abrange senha pelo provedor, sessão, timezone, notificações e preferências pessoais. Não inclui cargo, configuração global do servidor ou acesso a dados de colegas.

## 2. Catálogo funcional e aceite

| ID | Requisito | Critério de aceite mínimo |
|---|---|---|
| RF-01 | Convite e entrada | Admin e Coordenador convidam por e-mail com uso único e validade proposta de 7 dias; Coordenador só concede Usuário nos seus escopos; apenas destinatário autenticado aceita |
| RF-02 | Sessão e recuperação | Login, logout, renovação e recuperação funcionam; erro não revela cadastro; suspensão bloqueia novas operações |
| RF-03 | Perfil e conta pessoal | Nome e @, foto e capa/background, bio, localização informada e cargo profissional; editar os próprios dados, timezone, sessões e preferências; ver colegas no mesmo servidor, sem credenciais; perfil não altera privilégios |
| RF-04 | Workspaces | Criar, editar, associar membros e arquivar; pessoa sem acesso não vê nomes privados na sidebar ou busca |
| RF-05 | Projetos | Admin/Coordenador cria no workspace autorizado e define membros; coordenação deriva do cargo/escopo, sem cargo Manager separado; projeto arquivado permite leitura e bloqueia mutações de trabalho |
| RF-06 | Tarefas e delegação | Admin/Coordenador cria e edita título, descrição, responsáveis, prioridade, prazo, etiquetas e checklist no escopo; Usuário responsável atualiza status/checklist, sem reatribuir ou criar tarefa |
| RF-07 | Kanban | Arrastar ou mover por teclado; alteração aparece nos demais clientes; conflito não sobrescreve silenciosamente |
| RF-08 | My Tasks | Lista tarefas atribuídas ao usuário em projetos acessíveis; filtra prazo, status e projeto; remoção de acesso elimina o item |
| RF-09 | Comentários | Autor cria, edita e remove seu comentário; marcação exige destinatário com acesso; exclusão mantém marcador no histórico |
| RF-10 | Chat e moderação | Admin/Coordenador cria chats no escopo; participantes ativos enviam mensagens; Admin acessa/configura todos do próprio servidor e Coordenador só os seus; exclusão moderada mostra marcador e auditoria |
| RF-11 | Arquivos | Upload autorizado, progresso, erro, cancelamento e download privado; arquivo de outro projeto não pode ser reutilizado sem autorização |
| RF-12 | Vídeos | Upload respeita tamanho permitido; player para formatos compatíveis; formato não suportado oferece download com aviso |
| RF-13 | Reuniões | Participantes autorizados entram com microfone/câmera, escolhem dispositivos, compartilham tela e saem; bloqueio do SO tem orientação de recuperação |
| RF-14 | Calendar | Admin/Coordenador agenda eventos de trabalho/reuniões no escopo; Usuário responde e participa; todos podem manter lembretes pessoais sem criar reuniões para terceiros; tarefas com prazo não viram eventos duplicados |
| RF-15 | Docs | Criar documento por projeto, salvar revisão e controlar versão; duas edições concorrentes não perdem conteúdo silenciosamente |
| RF-16 | Reports | Progresso, tarefas por status, atrasos e conclusões por período; mostrar filtros, denominadores e horário de atualização |
| RF-17 | Contribuições | Summary no perfil com mapa diário, quantidade de tarefas concluídas e foguinho; mesma fonte de créditos e filtro de acesso; reabertura/conclusão repetida não inflam contagem |
| RF-18 | Inbox de notificações | Central pessoal para atribuições, menções, convites e lembretes; abas Todas/Não lidas, filtro por tipo, paginação, marcar lida/não lida e todas como lidas; badge consistente entre clientes e sem vazar conteúdo inacessível |
| RF-19 | Team | Exibir membros, áreas e papéis visíveis; presença é indicativa, não prova de produtividade |
| RF-20 | Ajuda e suporte | Consultar guia e abrir solicitação com protocolo; apenas solicitante e atendentes designados acessam detalhes |
| RF-21 | Busca | Buscar tarefas, documentos e arquivos acessíveis por texto; resultados paginados e escopo claro |
| RF-22 | Auditoria | Registrar alterações de acesso, arquivamento e eventos críticos; usuário comum não altera registros |
| RF-23 | Direitos e privacidade | Canal comunicado recebe pedidos de titulares, inclusive sem conta ativa; responsável verifica identidade, responde e executa medidas cabíveis com registro restrito; pode operar manualmente no piloto |
| RF-24 | Pastas | Admin/Coordenador cria, renomeia, move e arquiva pastas de materiais do escopo; Usuário navega e envia arquivos; pasta não amplia permissões nem permite mover anexos entre escopos |
| RF-25 | Áudio e imagens | Participante envia imagem ou grava/anexa áudio com prévia, cancelamento, progresso e retry; gravação de áudio exige ação e microfone explícitos; reprodução não inicia sozinha; sem transcrição automática |
| RF-26 | Administração do servidor | Somente Admin edita nome, imagem e descrição da organização, delega cargos e edita/suspende/exclui associações de usuários; impedir escalada e operação contra último Admin; auditar mudanças |
| RF-27 | Comandos de chat | Digitar / abre catálogo permitido por cargo/escopo; parâmetros tipados, ação de domínio autorizada e erros preservam entrada; invocação direta de comando proibido também é negada |
| RF-28 | Menções por hierarquia | @ sugere pessoas autorizadas e grupos permitidos; destinatários sem acesso não são incluídos; enviar mensagem revalida cargo/escopo; menção notifica sem conceder acesso |
| RF-29 | Foguinho de incentivo | Sequência atual e melhor sequência de dias com conclusão elegível, conforme RN-23; texto explica cálculo, timezone e escopo; sem pontos extras por reabrir, ranking ou monitoramento oculto |

## 3. Tarefas e estados

**RN-05:** fluxo inicial: `todo` → `in_progress` → `in_review` → `done`. Admin/Coordenador pode mover/reabrir tarefas no escopo; Usuário responsável pode iniciar e marcar a própria tarefa concluída, além de submetê-la à revisão opcional. Não altera tarefa de outro responsável nem reabre conclusão sem coordenação. Revisão pode ser pulada; não há aprovador diferente obrigatório. Toda transição registra autor e estado anterior; checklists pendentes exigem confirmação explícita antes da conclusão.

**RN-06:** tarefa tem um ou mais responsáveis ou permanece sem responsável em A fazer. Para iniciar trabalho deve haver ao menos um responsável. Prioridades: baixa, média, alta, urgente. Bloqueio é atributo separado, com motivo; não é uma coluna adicional.

**RN-07:** datas de prazo são datas civis (`due_date`), consideradas vencidas após o fim daquele dia no timezone do projeto. Eventos usam instante e timezone IANA. Alterar timezone não reescreve instantes históricos.

**RN-08:** arquivamento tira itens das consultas padrão e métricas operacionais; não apaga o histórico. Exclusão definitiva geral de projetos e materiais fica posterior ao piloto; exclusão de associação de usuário pelo Admin faz parte do piloto conforme RF-26. Isso não adia eliminações ou anonimizações cabíveis em pedidos de privacidade, atendidos pelo procedimento restrito do RF-23. Arquivo e documento não ficam públicos por terem sido anexados.

**RN-09:** progresso do projeto = tarefas não arquivadas em `done` / todas as tarefas não arquivadas, multiplicado por 100. Zero tarefas exibe “Sem tarefas”, sem divisão por zero. Percentual do checklist aparece como checklist, não como avanço subjetivo da tarefa. Não somar percentuais de tarefas para obter progresso do projeto.

## 4. Contribuições inspiradas no GitHub

**RN-10:** transição real para `done` cria evento imutável com autor da ação, instante e cópia dos responsáveis daquele momento. A primeira conclusão válida de cada tarefa concede uma contribuição a cada responsável registrado; o autor do movimento não recebe crédito extra. Sem responsável, entra apenas no total do projeto.

Uma tarefa concluída, reaberta e concluída novamente continua contando uma vez, na data da primeira conclusão. Reatribuir depois não transfere crédito histórico. O indicador mede entregas históricas, enquanto progresso mede estado atual; reabertura diminui progresso e não apaga a entrega histórica. A interface explica essa diferença.

**RN-11:** agrupar contribuições pelo timezone de perfil selecionado; padrão inicial `America/Sao_Paulo`. Um dia vai de 00h00 até antes de 00h00 do dia seguinte nesse timezone. Alterar o timezone pode redistribuir os dias, mas não a quantidade total. Datas do observador seguem o timezone explicitado no relatório, nunca uma mistura por pessoa.

**RN-12:** filtros de autorização são aplicados antes da agregação. Quem perdeu acesso não consulta o projeto nem seus números; histórico de ex-membro fica disponível aos membros autorizados do projeto. No perfil, mapa/total/foguinho só agregam projetos atualmente acessíveis tanto ao titular quanto ao observador, conforme RN-23. Não há ranking público ou acesso a RH por inferência de métricas.

**AC de exemplo:** tarefa com Ana e Bruno concluída na segunda soma 1 para cada um e 1 no projeto. Reaberta terça e concluída quarta continua com 1 no projeto na segunda. Maria executar a segunda conclusão não altera crédito. Avanço do projeto volta a cair enquanto estiver reaberta.

## 5. Comunicação e agenda

**RN-13:** mensagem direta pertence a uma organização; não cruza organizações. Participantes ativos e Admins ativos da própria organização podem ler conteúdo, com identificação do acesso administrativo conforme RN-04. Coordenador sem participação não lê diretos. Remoção organizacional bloqueia leitura, envio, sockets e reuniões; perder cargo Admin revoga também a inspeção de conversas das quais não participa.

**RN-14:** canais de área/projeto são acessíveis aos membros ativos do escopo e ao Admin da organização. Autor pode editar/remover sua mensagem; Admin pode apagar qualquer mensagem do servidor e Coordenador pode moderar canais que coordena. Ninguém reescreve texto alheio. Edição tem indicação; remoção mantém marcador com indicação de moderação, auditoria mínima e expurgo conforme retenção aprovada. Feed e busca não recuperam o conteúdo removido.

**RN-15:** eventos pessoais são privados; eventos de projeto seguem o acesso do projeto. Mover ou reagendar não confirma presença automaticamente. Respostas: pendente, aceito e recusado. Recorrência e integrações externas ficam para depois.

**RN-16:** Admin/Coordenador agenda ou inicia encontros internos no escopo; Usuário entra com acesso válido ao projeto e autorização de sala. Link encaminhado não concede entrada. A inspeção de chat pelo Admin não o conecta automaticamente a meet nem captura dispositivos. Encerrar/remover participante exige Admin ou Coordenador anfitrião/autorizado. Gravação de reuniões fica desabilitada no piloto; mensagem de áudio RF-25 é fluxo independente.

## 6. Notificações, suporte e limites

**RN-17:** notificações são geradas por evento persistido, deduplicadas por destinatário/evento/tipo. Mencionar a si próprio não gera notificação. Lembretes vencidos não são reenviados indefinidamente após indisponibilidade.

**RN-18:** atendentes são membros designados por Admin para suporte; designação é capacidade adicional, não quarto cargo e não abre projetos/chats por si só. Solicitações incluem apenas informações fornecidas pelo solicitante, sem captura automática de tela/conversas. Todos os cargos podem enviar help e acompanhar protocolo próprio; detalhes ficam com solicitante/atendentes, mesmo quando há administração de chats.

**RN-19:** retenção e preservação do histórico dependem da finalidade e de eventual obrigação aplicável. Prazos propostos de limpeza não são prazos legais gerais. Pedidos de titulares podem exigir eliminação/anonimização também de eventos, revisões e créditos; preservar somente o que tiver justificativa documentada, com acesso restrito e proteção de terceiros.

**RN-20:** decisões jurídicas usam a fonte oficial pertinente e seu enquadramento, não apenas a cópia do GitHub. Seguir os controles JUR-01 a JUR-10 do capítulo 12 nas funcionalidades afetadas. Licença de um acervo ou dependência não define a licença do produto nem transfere direitos de arquivos enviados.

Limites iniciais propostos: título de tarefa até 200 caracteres, mensagem até 10.000 caracteres, arquivo até 250 MB, vídeo até 1 GB, 10 anexos por envio e até 8 participantes por reunião. A política efetiva depende de suporte do provedor, teste de rede e orçamento. Rejeitar acima do limite tanto no cliente quanto no servidor, antes de reservar upload quando possível.

## 7. Comandos `/` e menções `@`

**RN-21:** comando é atalho de interface para uma ação existente, nunca execução de shell, SQL, scripts ou código livre. O servidor fornece catálogo conforme cargo atual, organização, escopo e parâmetros; negar comando não autorizado mesmo que digitado manualmente. Alterar cargo durante a digitação exige nova checagem ao executar. Texto de arquivos, mensagens recebidas e previews nunca executa comando automaticamente. Comando desconhecido preserva rascunho e mostra ajuda.

Catálogo inicial **proposto**, com nomes finais ajustáveis:

| Comando | Cargos e condição | Resultado |
|---|---|---|
| `/ajuda`, `/perfil`, `/minhas-tarefas` | Todos, próprio contexto | Ajuda, próprio perfil ou tarefas em resposta privada ao solicitante |
| `/andamento tarefa`, `/concluir tarefa` | Usuário responsável; Coordenador do escopo; Admin | Mesmas transições e créditos de RN-05/10, sem regra paralela |
| `/help assunto` | Todos | Abre solicitação própria; relato e protocolo não são publicados no chat |
| `/tarefa criar`, `/atribuir tarefa @pessoa` | Admin/Coordenador autorizado | Prévia/formulário com validação de projeto, responsável e prazo |
| `/chat criar`, `/pasta criar`, `/reuniao agendar` | Admin/Coordenador autorizado | Abre o mesmo fluxo permitido pela interface |
| `/apagar-mensagem id` | Autor ou moderador autorizado de RN-14 | Confirmação da exclusão, marcador e auditoria conforme o caso |
| `/cargo @pessoa cargo`, `/usuario editar`, `/usuario remover`, `/servidor editar` | Apenas Admin, na própria organização | Fluxo administrativo com confirmação/reautenticação quando exigidas |

Resultados pessoais e erros são privados por padrão. Ações publicadas usam eventos normais do domínio, sem enviar recibos/dados administrativos como mensagem. Ações destrutivas exigem confirmação; cancelamento não produz efeito. Retry usa a mesma chave idempotente, sem duplicar tarefa, convite, help ou reunião. Inspeção de chat sem participação continua sem compositor: usar a administração apropriada, sem contornar esse limite por comando.

**RN-22:** distinguir **menção individual** e **menção coletiva**. A hierarquia limita a convocação coletiva, sem impedir um Usuário de pedir ajuda a um Coordenador/Admin individual que já participa do contexto.

| Alvo proposto | Admin | Coordenador | Usuário |
|---|---|---|---|
| `@handle` de pessoa | Sim | Sim | Sim |
| `@usuarios` / `@coordenadores` | Sim | Sim, no escopo coordenado | Não |
| `@admins` | Sim | Não | Não |
| `@todos` no canal | Sim, todos os participantes elegíveis | Sim, apenas Usuários/Coordenadores do escopo; exclui Admins | Não |

Todos os casos exigem permissão de envio e destinatários ativos que já possam ler aquele canal/conversa. Para Coordenador, a expansão de qualquer grupo, inclusive `@todos`, exclui Admins; a prévia mostra o alcance e a contagem, sem usar esse grupo para contornar `@admins`. Mencionar Admin individual participante continua permitido. No direto, destinatários se restringem aos participantes; inspeção administrativa não é participação para receber menções. Menção nunca convida, concede cargo ou abre um projeto. Sugestões não revelam nomes/handles inacessíveis. Grupos expandem para IDs no envio, deduplicam a pessoa mencionada várias vezes e respeitam preferências/rate limit; não há menção global entre servidores. Comentários de tarefa usam as mesmas regras, com acesso ao projeto e origem própria para destinatários/notificações.

## 8. Perfil, summary e incentivo

**RN-23:** summary pessoal usa `completion_credits` e primeiras conclusões de RN-10/11/12. “Tarefas concluídas” conta tarefas distintas com crédito daquela pessoa no intervalo/escopo exibido; não mede quantas vezes ela clicou em concluir nem corresponde à quantidade de tarefas hoje em done. Reabrir não dá novo crédito. Tarefa com dois responsáveis pode contar uma vez para cada perfil, nunca duas vezes no mesmo perfil.

Regra inicial **proposta** para o foguinho: um dia civil com ao menos um crédito elegível mantém a sequência; várias tarefas no dia não somam dias extras. Dias consecutivos incluem fins de semana. Sequência atual é a cadeia que termina hoje ou ontem; sem atividade em nenhum desses dias, vale zero. Melhor sequência é a maior cadeia do histórico elegível. Exemplo: segunda e terça com entregas → 2; quarta sem entrega mantém 2 até o fim do dia; quinta sem nova entrega → 0. Na quinta com entrega, começa 1, pois quarta interrompeu a cadeia.

Calendário e foguinho usam o timezone declarado do perfil da pessoa observada, padrão RN-11; mostrar timezone e data de atualização, sem misturar com timezone do visitante. Trocar timezone ou perder acesso pode recalcular dias/sequência; não gera crédito novo e a interface explica mudanças. A contagem respeita interseção entre projetos acessíveis ao titular e ao observador; nem o número isolado denuncia RH/projeto restrito. O total e mapa seguem o filtro de período; o foguinho indica explicitamente que usa histórico elegível completo, não só o período filtrado. Sem dados elegíveis, mostrar 0 e estado vazio, sem dados fictícios.

Foguinho é incentivo visual e textual, não avaliação formal, ranking, recompensa financeira ou requisito de jornada. Não coletar horas de trabalho nem criar lembretes de cobrança por inatividade por causa dessa função. Animação respeita movimento reduzido; texto “sequência de N dias” acompanha o ícone.

**RN-24:** campos do perfil: nome e @ de identificação, foto, capa/background, bio, cidade/região de residência ou trabalho informada pela própria pessoa e cargo profissional, por exemplo “Senior Software Engineer”. Bio, localização, cargo profissional e capa são opcionais; não exigir endereço exato ou GPS. Cargo profissional é texto de apresentação, distinto e visualmente separado de Admin/Coordenador/Usuário. Editá-lo nunca promove permissões.

Proposta de @: handle único sem distinção de maiúsculas dentro da organização, com 3–30 caracteres ASCII entre letras, números e underscore; reservar nomes de grupos/comandos para evitar ambiguidade. Normalizar e validar no servidor; sugestão de handle vem no onboarding e exige confirmação. Menção persiste userId, não só texto; mudar @ não redireciona menções antigas para outra pessoa. A autoria existente continua referenciada pelo ID e menções já enviadas não são reprocessadas.

Perfil detalhado e summary ficam dentro do servidor, sem página pública externa. Nome/timezone e preferências pertencem à própria conta; foto, bio, handle, localização, capa e cargo profissional são por organização, evitando propagação involuntária entre equipes. Foto/capa são uploads internos validados, não URLs remotas arbitrárias. Mostrar claramente quais campos são visíveis aos colegas. A lista de campos e as imagens orientam esta versão; o trecho incompleto do pedido não foi convertido em regra adicional.

## 9. Inbox pessoal

**RN-25:** Inbox é a central de notificações persistidas do próprio destinatário, separada de chats e help. Mesmo Admin não lê a Inbox de outra pessoa por possuir cargo. Abrir Inbox não marca tudo como lido; abrir um item marca aquele item, e ação explícita permite marcar todos os itens existentes até o cursor retornado. Notificações que chegam depois permanecem não lidas. Estado de leitura sincroniza entre clientes, e badge contabiliza apenas itens não lidos ainda autorizados.

Revalidar acesso ao renderizar, abrir e contar. Se o recurso ficar inacessível, ocultar prévia e retirar do badge/lista; link antigo abre estado genérico. Menção editada pode notificar apenas destinatários realmente novos ainda elegíveis; removidos perdem a prévia e o item associado. Reenvio idempotente e nova inclusão do mesmo destinatário na mesma mensagem não geram alertas repetidos. Não revelar conteúdo de mensagem excluída em Inbox, push ou logs. Preferências controlam alertas opcionais sem desativar avisos de segurança essenciais; política de retenção inclui notificações e deduplicação, conforme RN-19.

## Evolução confirmada do MVP local — 22/10/2026

Estas decisões atualizam o fluxo inicial de entrada: cadastro pessoal é livre e começa sem Studio; somente a administração da plataforma cria Studios. Admin de Studio não equivale a administrador da plataforma. Futuramente um plano poderá liberar criação, sem cobrança nesta etapa. Admin e Coordenador convidam dentro das permissões; o convite aparece exclusivamente na Inbox do destinatário, que aceita ou recusa. Convites duram sete dias e são revalidados no aceite. Suspensão de participação não elimina a conta pessoal nem concede acesso a outro Studio.

Código pode ser anexado ao chat e lido como texto escapado dentro do aplicativo, com destaque, linhas, cópia e download autorizado. Limites locais: 15 MB por upload; prévia de 500 KB e 5.000 linhas. Não executar anexos. Tarefas abrem em painel lateral e mantêm Quadro/Lista/Calendário; animações respeitam redução de movimento. Temas Claro/Escuro/Híbrido são locais ao dispositivo; Híbrido tem navegação escura e conteúdo claro.

Comandos `/meet` e `/meet criar` abrem, respectivamente, reuniões e agendamento com validação de cargo/escopo. M/C controlam os dispositivos da prévia sem interceptar campos de edição. A prévia não implementa chamada remota. Configurações de Studio incluem identidade, membros, cargos, convites e auditoria; alteração de identidade exige versão atual e privilégio Admin.

## Preparação comercial aprovada —26/10/2026

Mensalidade por Studio: Essencial R$79 e Pro R$149. Ofertas empresariais privadas
são versionadas por operador da plataforma; não constituem terceiro plano público.
Cadastro continua sem Studio. Contrato pago e conferido provisiona um Studio e
seu Admin atomicamente, sem conceder acesso pelo retorno do navegador. Convites
independem da contratação. Valores, cotas, carência, cancelamento e evidências
estão no [guia comercial](../software-mvp/docs/billing.md). Vendas desativadas.
