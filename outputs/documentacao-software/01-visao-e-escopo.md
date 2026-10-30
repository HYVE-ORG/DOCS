# 01 · Visão de produto e escopo

## 1. Problema

A equipe precisa de um ambiente para executar trabalho especializado. Reuniões, conversas, tarefas, arquivos e agenda pertencem ao mesmo processo, mas costumam ficar espalhados. A consequência é perder decisões, procurar materiais em vários lugares e ter dificuldade para entender responsabilidades e progresso.

O software deve responder rapidamente: o que preciso fazer, em que projeto, com quem, até quando, onde estão os materiais e qual foi a evolução das entregas?

## 2. Público e necessidades

O primeiro público é a equipe do criador, incluindo seus amigos. A quantidade de membros ainda será levantada. O MVP já permite cadastro pessoal público sem Studio; a entrada em uma equipe exige convite. Não há venda ou cobrança ativa; somente a administração da plataforma cria Studios nesta etapa.

| Perfil | Necessidade principal | Exemplo |
|---|---|---|
| Usuário | Executar o trabalho e colaborar | Entra em meet, recebe tarefa, atualiza status, envia mensagens/mídia e pede ajuda |
| Coordenador | Distribuir e acompanhar entregas | Adiciona usuários, cria/delega tarefas, acompanha progresso e organiza chats, pastas e reuniões de sua área |
| Admin | Administrar o servidor da equipe | Acessa todas as áreas e chats, gerencia cargos e usuários e configura o servidor |

São os três cargos solicitados pelo usuário. Admin acumula as capacidades de Coordenador e Usuário; Coordenador acumula as de Usuário. “Servidor” significa a organização da equipe dentro do produto, não acesso ao sistema operacional ou ao host de infraestrutura. Alcance e controles estão no documento 02.

## 3. Proposta de valor

Reunir a execução do trabalho em um contexto compartilhado. Uma reunião pode estar ligada a um projeto; sua ata pode gerar tarefas; tarefas podem ter arquivos e comentários; conclusões alimentam indicadores e o histórico de contribuições. O diferencial proposto está nessa continuidade, não no volume de funções isoladas.

## 4. Objetivos e indicadores

Após quatro semanas de piloto, avaliar:

| Objetivo | Indicador proposto | Como medir |
|---|---|---|
| Tornar o sistema parte da rotina | Ao menos 70% dos convidados ativos por semana | Usuários com tarefa, comentário, mensagem ou reunião; apenas login não conta |
| Melhorar clareza | Ao menos 90% das tarefas em andamento têm responsável | Consulta semanal, com denominador e período visíveis |
| Preservar contexto | Ao menos 80% das entregas amostradas têm informação suficiente no projeto | Revisão manual de tarefas, decisões e materiais |
| Reduzir atrito | Usuário encontra uma tarefa e inicia uma reunião sem ajuda | Sessão observada com membros reais |

São hipóteses de sucesso do piloto, não compromissos comprovados. Medidas de atividade não devem ser convertidas em ranking automático de desempenho individual.

## 5. Escopo do primeiro lançamento

1. Convites, autenticação, perfis, cargos Admin/Coordenador/Usuário e gestão de membros.
2. Organização, workspaces por área e projetos com acesso explícito.
3. Home, My Tasks, Calendar, Team, Docs, Reports, Inbox e perfil profissional ampliado.
4. Kanban com A fazer, Em andamento, Em revisão e Concluída; visualização em lista e calendário de tarefas.
5. Tarefas com responsáveis, prazo, prioridade, descrição, checklist, comentários e anexos.
6. Chat por workspace e projeto, mensagens diretas, comandos `/`, menções `@`, moderação por cargo e Inbox de notificações.
7. Pastas lógicas, upload privado de arquivos, vídeos, imagens e mensagens de áudio; reprodução dos formatos suportados pelo cliente.
8. Reuniões internas com áudio, vídeo e compartilhamento de tela.
9. Agenda própria, documentos simples, relatórios básicos e perfil com summary inspirado no GitHub: mapa, total de tarefas concluídas e foguinho de sequência de entregas. Bio, nome/@, foto/capa, localização informada e cargo profissional completam o perfil.
10. Ajuda, solicitação de suporte, configurações pessoais e administração do próprio servidor pelo Admin.

Todos esses módulos fazem parte do produto solicitado. A entrega será incremental, mas o piloto completo só será considerado pronto quando o conjunto obrigatório estiver integrado.

## 6. Fora do primeiro lançamento

Cobrança, assinatura, marketplace, portal público, convidados externos, aplicativo móvel nativo, macOS/Linux certificados, sincronização Google/Outlook, integração GitHub, edição colaborativa simultânea de documentos, gravação/transcrição de reuniões, IA, automações de workflow, ponto eletrônico, folha de pagamento e trabalho offline com sincronização.

RH é inicialmente um workspace restrito aos membros atribuídos e aos Admins do servidor, conforme a matriz. Não pressupõe um sistema de folha, prontuário de funcionários ou recrutamento. Design e desenvolvimento também não pressupõem editor gráfico ou IDE internos.

## 7. Hipóteses de produto

A expansão de 23/10/2026 está no [capítulo 13](13-gestao-integrada-e-expansao.md): primeiro incremento CRM/comercial já entregue no MVP; horas e custos a seguir; HRM/ATS, metas e operações em etapas posteriores. Isso atualiza a direção futura de RH descrita acima, sem incluir recrutamento no primeiro piloto. Estoque e produção dependem de necessidade validada. Dados de RH/financeiro terão permissões específicas. O capítulo 13 distingue o recorte entregue das demais capacidades planejadas.

- O MVP utiliza a marca Forma; “Mova” pertence à imagem de referência e não foi escolhido como nome.
- Windows é o primeiro alvo de distribuição; Electron foi solicitado, mas sistemas operacionais não foram especificados.
- A equipe aceita operar conectada; falhas de rede devem ser visíveis e recuperáveis.
- “Meet” significa videoconferência dentro do produto. Não foi solicitada integração com Google Meet.
- “Summary igual ao GitHub” significa resumo e mapa diário de conclusões; não implica acessar contas ou repositórios GitHub.
- A expressão “feitas” e “concluídas” foi normalizada: concluída é uma única categoria terminal; revisão é uma etapa opcional proposta.

## 8. Exemplo de uso completo

O administrador convida uma designer para Marketing. Ela entra no projeto Campanha, lê o briefing em Docs, aceita uma tarefa e conversa no canal. A equipe agenda uma revisão, compartilha a tela e registra a decisão em uma ata. A designer envia o material, move a tarefa para revisão e o responsável aprova a conclusão. A entrega aparece no relatório e no mapa diário de contribuições, respeitando os acessos do observador.

## 9. Limites desta documentação

Esta versão define uma base transversal para o produto e sua engenharia. Layouts finais, migrações executáveis, OpenAPI validada, política jurídica, orçamento contratado e procedimentos de produção comprovados serão produzidos ou confirmados durante as respectivas fases. Decisões abertas não devem ser apresentadas como já aprovadas.
