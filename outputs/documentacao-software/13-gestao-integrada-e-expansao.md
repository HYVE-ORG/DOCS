# 13 · Gestão integrada e expansão do Forma

**Data: 23/10/2026 · v0.8: primeiro incremento CRM/comercial entregue; demais módulos planejados.**

O usuário solicitou avaliar ERP, CRM, HRM, ATS, projetos, horas, vendas, finanças e operações e aprovou a direção apresentada. A divisão, prioridade e regras abaixo organizam a evolução; o estado implementado está na seção 9. Esta extensão não amplia silenciosamente o aceite do primeiro piloto. Nenhuma tela, API ou integração futura deve aparecer como disponível na landing ou no aplicativo.

## 1. Direção e alternativas

O Forma continua sendo um espaço especializado de trabalho. A expansão deve permitir acompanhar o trabalho desde a demanda de um cliente até a entrega e seu custo, reutilizando Studio, áreas, equipe, projetos, agenda, documentos, Inbox e autorização.

Alternativas consideradas: construir um ERP completo imediatamente amplia demais o piloto e mistura regras fiscais, trabalhistas e industriais ainda desconhecidas; manter apenas tarefas perde o vínculo entre demanda, esforço e resultado solicitado agora. A recomendação é gestão integrada modular: colaboração como base; clientes, horas e custos primeiro; pessoas, recrutamento e operações em etapas próprias. Esta recomendação é uma escolha de planejamento, sujeita a revisão com o uso real.

Um módulo pode estar desabilitado por Studio. Não criar microserviços, nova dependência ou tabela vazia apenas para reservar lugar. Funcionalidades são entregues como percursos completos, com persistência, autorização, estados de erro e documentação de uso.

## 2. Cobertura do pedido e prioridade

| Família / recursos pedidos | Decisão para o Forma | Etapa proposta |
|---|---|---|
| PM: projetos, tarefas, agenda, etiquetas, relatórios | Evoluir o núcleo existente; dependências, recorrência, modelos e aprovações | Base e E1 |
| CRM: clientes, contatos, leads, fornecedores | Cadastro único por Studio, histórico de relacionamento e vínculo com projetos | E1 |
| Vendas: pipeline, propostas, estimativas | Oportunidades por etapa, propostas versionadas e conversão em projeto | E1 |
| Horas, atividades e timesheets | Timer explícito, lançamento manual, revisão e aprovação | E1 |
| Custos, receitas e despesas | Orçamento e resultado gerencial de projetos, contas a pagar/receber | E1 |
| Dashboard | Indicadores autorizados de entregas, horas, pipeline e finanças; filtros e denominadores | E1, conforme dados reais |
| HRM: colaboradores, contratos, taxas, onboarding | Cadastro restrito separado do perfil social, vínculo e checklist de entrada/saída | E2 |
| Ausências, feriados e aprovações | Solicitação, calendário de disponibilidade e revisão; sem cálculo legal automático de direitos | E2 |
| ATS: vagas, candidatos e entrevistas | Pipeline de candidatura e agenda com notas restritas | E2 |
| Objetivos, KPI, OKR e desempenho | Metas com responsável, período, origem e revisão humana | E2 |
| ERP e financeiro ampliado | Compras, orçamento, fornecedores e integração com sistemas especialistas | E3 |
| Invoices, estimates, accounting e pagamentos | Propostas/cobranças gerenciais primeiro; emissão fiscal, escrituração e processamento por integração posterior | E3, com análise específica |
| Inventário e equipamentos compartilhados | Patrimônio, empréstimos, reservas e devoluções | E3 |
| Estoque e supply chain | Movimentos de estoque, compras, recebimento e fornecedores, se houver operação física | E4, condicional |
| Produção | Ordens, materiais, capacidade e rastreabilidade somente com caso de uso industrial validado | E4, condicional |
| Múltiplas organizações, áreas e times | Preservar conta global e participações isoladas; time operacional não concede acesso automaticamente | Transversal |
| Help center e base de conhecimento | Evoluir ajuda e Docs; artigos internos com busca e permissões | E1 |
| APIs headless | Contratos versionados e credenciais de integração com escopos, independentes da interface | Transversal, após domínio estável |
| Integrações: Upwork, Hubstaff e outras | Adaptadores avaliados por necessidade, permissões, contrato do fornecedor e custo | Posterior; nenhuma conexão instalada |
| Histórico e templates de e-mail | Templates versionados e vínculo ao contato; envio só após configuração e autorização explícitas | E2/E3 |
| Importação/exportação | CSV com prévia, validação, relatório de falhas e exportação autorizada | E1 |
| Cargos e permissões | Manter Admin/Coordenador/Usuário; acrescentar permissões específicas por módulo | Transversal |
| Multimoeda | Código de moeda por registro, valores exatos e conversão explícita | E3; nunca somar moedas distintas diretamente |
| Multilíngue | pt-BR inicial; catálogo de mensagens e formatos locais antes de novos idiomas | Transversal; sem tradução completa nesta etapa |
| Temas escuro/claro/corporativo/material | Manter Claro/Escuro/Híbrido existentes; identidade corporativa com contraste validado; Material é opção a avaliar | Transversal |
| Páginas públicas de organização/colaborador | Publicação opcional, prévia e campos explicitamente selecionados | Posterior; perfis atuais continuam internos |

E1 a E4 são incrementos após a estabilização do piloto, sem datas prometidas. Estoque e produção permanecem documentados como possibilidades, não compromissos de implementação para uma equipe digital.

## 3. Requisitos funcionais adicionais

Os RF abaixo são de evolução. Não significam recursos implementados nem mudam a prioridade P0 dos RF anteriores.

| ID | Requisito | Critério de aceite mínimo proposto |
|---|---|---|
| RF-30 | CRM e partes relacionadas | Criar cliente/lead/fornecedor e contatos; buscar e vincular a projetos; detectar duplicidade sem mesclar automaticamente; negar leitura entre Studios |
| RF-31 | Pipeline e propostas | Mover oportunidade com histórico; proposta tem versões e totais; aceite converte uma única vez em projeto, inclusive após retry |
| RF-32 | Horas e timesheets | Iniciar/pausar/encerrar timer ou lançar intervalo; exibir timezone e duração; detectar sobreposição; submeter e revisar período sem perder histórico |
| RF-33 | Orçamento e financeiro gerencial | Registrar custos, receitas, despesas, vencimento e liquidação; distinguir previsto/realizado e pago/pendente; agregado confere com lançamentos conhecidos |
| RF-34 | Pessoas e onboarding | Manter vínculo restrito, admissão/desligamento e checklists; encerrar participação sem apagar autoria; perfil público interno não expõe salário ou documentos |
| RF-35 | Ausências e disponibilidade | Solicitar e aprovar/recusar ausência com histórico, evitar autoaprovação e indicar conflito de agenda sem expor motivo privado |
| RF-36 | ATS | Manter vaga e candidatura com etapas; agendar entrevista; restringir currículo/notas aos autorizados; converter contratado sem duplicar identidade ou convidar automaticamente |
| RF-37 | Metas e avaliação | Meta tem período, unidade, direção, valor-base, alvo, responsável e fonte; resultado pode ser explicado e corrigido; avaliação humana não deriva de cliques ou foguinho |
| RF-38 | Equipamentos e operações | Reservar/emprestar/devolver equipamento sem dupla reserva; eventual estoque usa movimentos auditáveis e inventário conciliável, sem editar saldo diretamente |
| RF-39 | Integração e portabilidade | API/importação/exportação respeitam Studio, escopo e limites; importação tem prévia, chave de deduplicação e resultado por linha; segredo não aparece no cliente ou log |
| RF-40 | Localização e publicação | Formatar idioma/data/moeda sem mudar valor persistido; página pública mostra apenas campos publicados, aceita revogação e não expõe dados por IDs previsíveis |
| RF-41 | Conhecimento e comunicação comercial | Artigos e templates têm versão e visibilidade; e-mail registra destinatário e resultado quando houver provedor; não marcar enviado sem confirmação real |

### Regras complementares

**RN-26:** cada registro de CRM, RH, candidatura, tempo, financeiro e operação pertence a um Studio. Relações cruzadas entre Studios são rejeitadas. Conta pessoal não é empregado, contato comercial nem candidato por definição; cada vínculo tem finalidade e acesso próprios.

**RN-27:** horas de projeto são registros explícitos de esforço. Um timer ativo por conta no produto; mudança de Studio exige encerrar ou resolver o timer anterior sem revelar seu conteúdo. Intervalos sobrepostos são rejeitados na submissão. Duração é calculada por instantes UTC, não pela subtração de horários exibidos. Timesheet segue rascunho → submetido → aprovado ou devolvido; correção de aprovado exige reabertura justificada e histórico. Timer, apontamento de projeto e sistema de ponto trabalhista são produtos distintos.

**RN-28:** orçamento e resultado usam quantias decimais exatas, moeda e regra de arredondamento definida por moeda. Taxa de custo e preço têm vigência; lançamentos preservam a taxa utilizada. Despesas aprovadas e horas aprovadas entram no realizado; estimativas permanecem previstas. Correções financeiras usam ajuste/estorno, preservando origem. Horas não faturáveis não viram cobrança. Taxa e custo individual não são campos do perfil público.

**RN-29:** tarefas concluídas, horas, presença e metas são métricas distintas. Histórico de atividade significa eventos explícitos do produto. Não adicionar captura de tela, teclas, sites visitados, GPS, webcam em segundo plano ou pontuação automática de produtividade. Indicadores não decidem contratação, remuneração ou sanção automaticamente. Monitoramento invasivo não integra esta proposta.

**RN-30:** autor não aprova a própria timesheet, ausência, despesa ou proposta que exija revisão. Admin configura aprovadores autorizados; caso não haja outro aprovador, o item permanece pendente ou é registrado como não revisado, sem aprovação fictícia. Delegação tem escopo e validade; substituto não ganha acesso geral ao RH/financeiro.

**RN-31:** cobrança do cliente de um Studio é separada da assinatura do próprio Forma. Nenhum plano, cobrança real, emissão fiscal ou integração bancária está habilitado. Pagamento confirmado no futuro depende do provedor, idempotência, conciliação e tratamento de estorno; clique do usuário não confirma pagamento. Multi-Studio não habilita criação pública: permanece a regra atual de administração da plataforma, com planos como evolução.

**RN-32:** módulos restritos exigem permissão específica, além de cargo e escopo. Coordenador de projeto não recebe automaticamente salários, currículos, custos individuais ou contas financeiras. Usuário vê seus apontamentos/solicitações; avaliadores veem apenas os recursos delegados. Admin gerencia concessões, sem converter inspeção de chats em acesso universal às categorias novas. Exportações, busca, dashboards e notificações aplicam a mesma política e trilha de auditoria.

## 4. Percurso integrado e navegação

Fluxo de referência: contato → oportunidade → proposta versionada → aceite → projeto → tarefas/horas/despesas → entrega → cobrança gerencial → liquidação registrada → análise. Cada etapa referencia a anterior por ID; mover etapa do pipeline não reconhece receita automaticamente. Conversão idempotente reutiliza o projeto criado e não duplica tarefas, anexos ou clientes.

Novas seções de Studio propostas: Clientes, Comercial, Horas, Pessoas e Financeiro. Operações só aparece se o módulo for adotado. A navegação pessoal mantém Minhas tarefas, Inbox, Calendário e Perfil. Em projeto, abas Clientes, Horas, Orçamento e Resultados aparecem apenas quando habilitadas e autorizadas. Não mostrar menus vazios como se fossem funções prontas.

Em Pessoas, lista de colaboradores continua com 20 membros por página. Cadastro administrativo de RH, vaga e candidatura são telas separadas dos cards de perfil. A agenda indica indisponibilidade sem tornar público o motivo de afastamento. Filtros de período, moeda, Studio e estado acompanham cada indicador.

## 5. Arquitetura e dados propostos

Manter TypeScript/React/Electron e NestJS; preferir módulos do mesmo backend e reutilizar validação, auditoria, anexos privados, Inbox e controle de versão. JSON continua sendo a persistência real do MVP. A arquitetura PostgreSQL/Supabase segue proposta; apontamentos concorrentes, aprovação e financeiro ampliado exigem decisão de persistência e migração testada antes de implementação. Não simular transações distribuídas no cliente.

| Domínio | Entidades futuras principais | Integridade essencial |
|---|---|---|
| CRM | business_parties, contacts, contact_links | Tipos cliente/lead/fornecedor coexistem no mesmo cadastro; unicidade e merge por Studio |
| Comercial | pipelines, stages, opportunities, proposals, proposal_lines, conversions | Versão da proposta, moeda e conversão única por origem |
| Tempo | timers, time_entries, timesheets, approvals | Proprietário, UTC, fim maior que início, não sobreposição, versão e aprovação |
| Pessoas | employee_records, engagements, onboarding_items, leave_requests, holiday_calendars | Participação separada do vínculo; escopo restrito e vigência |
| Recrutamento | job_openings, candidates, applications, interviews | Candidato pode existir sem conta; uma pessoa pode ter candidaturas distintas |
| Financeiro | project_budgets, rate_versions, financial_entries, settlements | Valores exatos, moeda, origem, ajuste e vínculo ao projeto/parte |
| Metas | objectives, key_results, metric_observations, reviews | Período, unidade, fonte, fórmula e autoria |
| Operações | assets, reservations, loans; depois stock_items, stock_movements, purchase_orders | Conflito de reserva, devolução, movimento e unidade de medida |
| Plataforma | module_settings, permission_grants, integration_connections, import_jobs | Negação por padrão, credenciais protegidas e jobs vinculados ao Studio |

Essas entidades não são migrações executadas. Escolher apenas as necessárias ao incremento em implementação. Não duplicar contas, projetos ou arquivos para atender um novo módulo. Exclusão e retenção precisam tratar todas as referências e derivados.

### Contratos de API propostos

Prefixo futuro `/api/v1/studios/:studioId`. Recursos candidatos: `contacts`, `opportunities`, `proposals`, `time-entries`, `timesheets`, `employees`, `leave-requests`, `applications`, `budgets`, `financial-entries` e `assets`. São contratos de intenção; não são endpoints disponíveis no MVP.

Listas usam paginação e filtros autorizados; mutações validam versão, escopo e estado. Conversão e operações repetíveis usam chave idempotente. Erros distinguem validação, conflito e falta de permissão sem revelar registros externos. Credenciais de integração são revogáveis e vinculadas a escopos; não reutilizar senha pessoal. Webhooks futuros exigem autenticação, deduplicação, limites de retry e reconciliação.

Eventos candidatos: `opportunity.won`, `proposal.accepted`, `timesheet.submitted`, `timesheet.approved`, `leave.decided` e `expense.approved`. Publicar após persistência, por mecanismo durável quando implementado. Inbox recebe só os destinatários autorizados; não copiar salário, currículo ou motivo de ausência para prévias.

## 6. Indicadores e controles

| Indicador | Definição proposta | Cuidado de interpretação |
|---|---|---|
| Entregas | Tarefas distintas concluídas conforme o filtro | Não equivale a horas ou valor gerado |
| Esforço | Soma de intervalos elegíveis sem sobreposição | Informar se rascunho, submetido ou aprovado |
| Pipeline | Valor das oportunidades abertas por etapa/moeda | Projeção comercial não é receita realizada |
| Resultado gerencial | Receitas reconhecidas pela política definida menos custos elegíveis no período/moeda | Distinguir resultado de caixa e de margem orçada |
| Caixa | Liquidações de entrada menos saída no período | Não somar vencimentos ainda pendentes como pagamentos |
| OKR | Evolução segundo unidade, direção e fórmula da meta | Fonte e revisão humana visíveis; sem nota universal de pessoa |

Uma eventual taxa de conversão exige fonte e data, preservando valor original e convertido. Dashboard mostra data de atualização, filtros, estados vazios e denominadores. Não inserir bônus, salário, avaliação ou receita fictícia para preencher cards.

Aplicar JUR-01 a JUR-10: inventariar tratamentos adicionais, finalidade, destinatários, retenção, exportação e direitos. Esta é uma proposta de engenharia, sem parecer jurídico. Antes de coletar dados reais de empregados/candidatos, controlar jornada, emitir documentos fiscais ou processar pagamentos, revisar as normas oficiais específicas e o contexto da organização; o acervo atual não cobre integralmente essas operações. Não alterar snapshots legais para dar aparência de cobertura. Benefícios, folha, cálculo de férias, banco de horas, impostos e escrituração ficam fora da primeira entrega desses módulos.

## 7. Backlog executável por incremento

| Épico | Entrega verificável | Dependência |
|---|---|---|
| EP-15 Clientes e comercial | Cliente → oportunidade → proposta aceita → projeto vinculado | Identidade, Studio, projetos, autorização e auditoria |
| EP-16 Horas e revisão | Apontamento → timesheet → revisão → relatório correto | Tarefas, timezone, concorrência e aprovadores |
| EP-17 Custos e orçamento | Orçamento → despesas/horas aprovadas → resultado por moeda | EP-16, taxas vigentes e lançamentos exatos |
| EP-18 Pessoas e disponibilidade | Onboarding, vínculo e ausência com revisão restrita | Permissões de RH e inventário de dados |
| EP-19 Recrutamento | Vaga → candidatura → entrevista → registro de contratação | Agenda, privacidade e acesso de avaliador |
| EP-20 Metas e conhecimento | Meta rastreável, revisão e artigo interno versionado | Indicadores confiáveis e Docs |
| EP-21 Portabilidade e integração | CSV revisável e API autorizada com revogação | Domínio estável e política de exportação |
| EP-22 Operações condicionais | Equipamento → reserva → empréstimo → devolução | Necessidade validada; estoque/produção avaliados depois |

Recomendação de execução: estabilizar piloto → EP-15 → EP-16 → EP-17 → Pessoas/ATS conforme demanda → integrações e operações. Cada incremento recebe plano e critérios próprios antes de código. Não há estimativa de prazo nem custo contratado nesta extensão.

## 8. Evidências necessárias antes de anunciar cada módulo

Validar fluxo completo com dados sintéticos e ao menos dois contextos de Studio. Incluir testes negativos de cargo/escopo, concorrência, retry, revogação, exportação e auditoria. Para tempo: timer após recarga/queda, horário de verão, intervalo aberto e aprovação própria. Para financeiro: centavos, arredondamento, duas moedas, taxa histórica, estorno e divergência entre caixa e orçamento. Para ATS/RH: currículo privado, candidato sem conta, suspensão e retirada de acesso.

Antes de entregar, comprovar persistência após reinício, migração/recuperação, navegação por teclado e responsividade. Importação deve provar falha parcial recuperável sem duplicação nem fórmula executável na exportação para planilha. Publicação externa requer prévia, autorização explícita e teste de revogação. Sem evidência, o estado permanece planejado.

## 9. Estado real e decisões abertas

Na v0.7 foi entregue o plano documental. Após aprovação, a v0.8 entrega o primeiro incremento de EP-15 no MVP: rotas `#clients` e `#sales`, cadastro/edição de clientes, leads e fornecedores por área; busca e paginação de 20 contatos; oportunidades com cinco etapas e histórico persistido; propostas com versões anteriores e registro explícito do aceite externo; conversão transacional e única para projeto e chat. Admin atua no próprio Studio; Coordenador somente nas áreas atribuídas; Usuário não recebe CRM. Condições privadas da proposta não são copiadas para o projeto. Após criar proposta, não é permitido trocar o contato da oportunidade.

Recorte real: BRL, centavos inteiros e limite de R$ 10 milhões por registro, um pipeline fixo, proposta em texto e total gerencial. Não há envio externo, assinatura eletrônica, PDF, itens/tributos, cobrança, exclusão/merge, importação/exportação ou associação manual de cliente a projeto antigo. O aceite é registrado por gestor com referência à decisão do cliente; não representa autenticação do cliente ou aprovação interna de despesa. RF-30/31 estão parcialmente implementados neste recorte; capacidades adicionais permanecem no backlog. A versão original da proposta é preservada e alterações concorrentes retornam conflito.

Contratos reais: `POST /api/actions` com `crm.contact.save`, `crm.opportunity.save`, `crm.proposal.save`, `crm.proposal.accept`; `GET /api/state` inclui snapshot CRM filtrado. `State.crm` é extensão opcional aditiva no JSON v2, preservando base antiga; não se executou migração para PostgreSQL. As entidades/operações da seção 5 continuam propostas de arquitetura ampla, não nomes de tabelas ou rotas já implantadas.

Evidências: 51 testes MVP passaram, oito novos para CRM, incluindo HTTP real, persistência/reinício, isolamento, retry revogado, corrupção, versões, conversão concorrente e privacidade do projeto. Build/typecheck passaram; revisão independente somente leitura identificou dois achados, ambos reproduzidos em testes e corrigidos. QA visual isolada confirmou cadastro → oportunidade → proposta revisada → aceite → projeto/chat, busca vazia e layout de 390 px. Nenhum dado de teste foi inserido na base da equipe. O guia detalhado permanece em `outputs/software-mvp/docs/crm.md`, no checkout do aplicativo.

ERP, HRM, ATS, timesheet, custos/financeiro e demais módulos continuam planejados. Reuniões remotas, instalador distribuível, e-mail externo, pagamentos e Supabase mantêm os limites do README do MVP.

Confirmar ao planejar cada incremento: moeda inicial e política de reconhecimento, aprovadores reais, quais dados de RH são necessários, funil comercial, necessidade de estoque físico, provedores de integração e idiomas. Essas escolhas não impedem manter este mapa de evolução, mas não devem ser apresentadas como decisões aprovadas pelo usuário.
