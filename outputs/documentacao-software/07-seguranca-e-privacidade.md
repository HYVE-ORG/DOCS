# 07 · Segurança e privacidade

A expansão do [capítulo 13](13-gestao-integrada-e-expansao.md) aplica RN-26 a RN-32: dados administrativos de RH, currículos, taxas individuais e financeiro exigem permissão específica, sem herdar acesso de uma coordenação de projeto ou da inspeção de chats. Dashboard, busca, API, anexos, exportação e Inbox seguem o mesmo limite. Horas são apontamentos explícitos; captura de tela/teclas e vigilância contínua não integram a proposta. CRM local já filtra Studio/área/cargo, revalida retry e preserva condições comerciais fora da descrição pública interna do projeto. Controles de RH/financeiro ainda precisam ser implementados nos respectivos módulos.

Esta seção deve ser aplicada em conjunto com [Legislação e aplicabilidade](12-legislacao-e-aplicabilidade.md), incorporada por solicitação do usuário. Os controles legais pertinentes passam a integrar a continuidade do projeto.

## 1. Objetivo e fronteiras

Proteger credenciais, conversas, arquivos e projetos privados da equipe. Ameaças prioritárias: acesso horizontal por troca de IDs, conteúdo malicioso em mensagens/arquivos, vazamento de sessão no desktop, socket sem autorização, associação revogada ainda ativa e erro de contexto no pool do banco.

Serviços externos recebem apenas dados necessários. Não há promessa de criptografia ponta a ponta. HTTPS/WSS e os mecanismos de armazenamento do provedor precisam ser configurados e verificados; isso não equivale a E2EE.

## 2. Identidade e autorização

- Autenticação pelo Supabase Auth; nenhuma senha armazenada no domínio ou em logs.
- Verificar token criptograficamente no backend; validar emissor, audience esperada e validade. Metadata editável não concede papel.
- Confirmar associação ativa a cada operação e em emissão de download/token de reunião.
- Reautenticação para alteração de cargos, exclusão/suspensão de usuários e outras operações administrativas críticas; proteger o último Admin ativo.
- Revogação deve produzir invalidação de cache, fechamento de sockets e remoção da chamada; alvo proposto de propagação em até 10 segundos, sujeito a teste.
- Sessão vencida impede mutações; refresh não deve gerar várias renovações concorrentes.
- Aplicar rate limit em login, convites, busca, criação e envio; configurar recuperação de conta com respostas não enumeráveis.

Autenticação válida não significa permissão para uma organização. Testes de acesso incluem API, banco, storage, socket e serviço de mídia.

Papéis de acesso são Admin/Coordenador/Usuário, conforme RN-04. Coordenador não concede cargos nem amplia seu escopo ao adicionar pessoas. Usuário não cria/delega tarefas; somente responsável ativo altera estado/checklist da própria tarefa. Admin tem alcance total nas áreas/chats do próprio servidor, sem privilégios sobre outras organizações ou credenciais alheias. Alterar cargo exige validação no servidor e propagação a caches, subscriptions e downloads futuros; um token antigo não conserva o cargo anterior.

## 3. Desktop Electron

Renderer sem Node integration, com `contextIsolation` e sandbox habilitados. Preload expõe operações estreitas e tipadas; main valida origem/remetente, schema e permissão de cada chamada IPC. Nenhum IPC permite executar shell, ler caminho arbitrário ou abrir URL sem validação.

Conteúdo do aplicativo é local; links externos aprovados abrem no navegador do sistema. Bloquear navegação e novas janelas inesperadas. CSP restrita; não desativar `webSecurity`. Não renderizar HTML arbitrário de mensagens ou documentos. Downloads não executam automaticamente.

Refresh token deve ficar em armazenamento protegido pelo SO, acessado pelo main, com bridge mínima de sessão. Access token de curta duração pode ficar em memória do renderer quando necessário à API. Evitar `localStorage` para credenciais persistentes. A implementação do fluxo Supabase/Electron e proteção em Windows deve ser comprovada em spike antes de consolidar a distribuição.

Captura de tela é ação explícita. O usuário escolhe tela/janela e vê indicação enquanto compartilha. Solicitar apenas permissões necessárias. Pacote distribuído deve ser assinado; atualização automática exige assinatura e verificação. Sem orçamento de certificado definido, não prometer instalador assinado já disponível.

Referência: [recomendações oficiais do Electron](https://www.electronjs.org/docs/latest/tutorial/security).

## 4. Dados e Storage

Separar credenciais de runtime e migração. Nenhum segredo privilegiado em código cliente. Policy de banco considera tenant, associações e tipo da operação; testar ausência de contexto e reutilização de conexão. `app_api` não pode ser dono das tabelas nem BYPASSRLS. Schema privado reduz exposição pela Data API, sem substituir menor privilégio.

Buckets privados; chave opaca, nunca nome fornecido pelo usuário como caminho executável. Nome exibido passa por escape. Validar MIME, extensão, bytes reais, tamanho, destino e cota. Impedir path traversal e anexos cruzados. SVG/HTML e formatos ativos não recebem preview executável. Binários só são disponibilizados após a estratégia de inspeção definida para o piloto.

Não carregar URLs arbitrárias no servidor para “prévia” sem política contra SSRF. No primeiro lançamento, previews se limitam a objetos internos validados; link externo é apenas link. Proteção contra malware reduz risco, sem garantir que todo arquivo seja seguro.

Referência: [grants e RLS no Supabase](https://supabase.com/docs/guides/database/postgres/row-level-security).

## 5. Conteúdo privado e RH

RH usa workspace e projetos com associação explícita para Coordenador/Usuário. Admin pode visualizar todas as áreas da sua organização, inclusive RH, conforme pedido do usuário; não há um quarto cargo ou bypass entre organizações. A UI explica esse alcance e a inspeção administrativa gera trilha mínima. Não incluir documentos de RH em busca, notificações ou relatórios de pessoas sem acesso. Coleção de dados sensíveis exige análise específica de finalidade e necessidade; cargo técnico não substitui essa análise.

Nesta versão, Admin pode ler e administrar todos os chats de trabalho da própria organização, inclusive diretos. Isso substitui a proposta anterior de acesso exclusivo dos participantes. Coordenador lê diretos apenas quando participa e modera terceiros apenas nos canais que coordena. Admin em modo de inspeção não envia mensagem, não muda recibos nem simula participação; conteúdo alheio não é editado como se fosse do autor. Toda exclusão moderada registra ator/alvo/motivo, preserva marcador e respeita retenção, sem manter cópia integral nos logs.

Antes do primeiro uso e ao abrir um direto, informar claramente a possibilidade de inspeção administrativa; “direto” descreve destinatários, sem promessa de sigilo exclusivo. Documentar finalidade, responsáveis, campos e controles desse acesso antes do piloto, como JUR-01/02/05/10; o requisito funcional não equivale a validação jurídica concluída. Solicitações de suporte continuam restritas a solicitante/atendente: ter Admin ou inspecionar chats não libera todos os tickets. Diagnóstico permite revisão e remove tokens/URLs assinadas antes do envio.

## 6. Privacidade por padrão

Minimizar cadastro a nome, e-mail de identidade e avatar opcional. Presença, contribuições e relatórios têm finalidade de coordenação, sem coleta de teclas, capturas silenciosas ou monitoramento oculto. Telemetria de conteúdo fica desligada; logs usam IDs e códigos de erro.

Perfil de colega mostra apenas dados profissionais compartilháveis no mesmo servidor, com cargo de acesso separado de função profissional. E-mail de identidade, telefone e dados de RH não se tornam públicos por constarem das imagens. Admin edita cadastro/associações administrativas, sem visualizar senha, redefinir credencial em nome do titular ou alterar configurações pessoais globais de outra conta. Excluir usuário do servidor primeiro revoga o acesso local; não destrói automaticamente identidade de outros servidores nem autoria.

Áudio em mensagem exige captura iniciada pelo usuário, indicador ativo, prévia e cancelamento; nunca gravação de fundo ou de reunião. Imagem/áudio/vídeo passam pelos mesmos controles de tipo, inspeção, limite e destino. Pastas não mudam a classificação do material; feed de atividade não serve de canal alternativo para conteúdo removido ou sem autorização.

Antes do piloto, definir responsável pelo tratamento, contato de privacidade, finalidade, fundamento a avaliar por tratamento, retenção, subprocessadores, localização dos dados e procedimento de acesso/correção/exclusão. O atendimento a direitos cabíveis deve funcionar desde o piloto, ainda que por operação manual restrita; não depende da futura exportação administrativa completa. A revisão jurídica aplicável depende do uso real e não está concluída por esta documentação. Não afirmar conformidade legal automática por usar Supabase.

### Comandos, menções e perfil ampliado

Comandos `/` usam allowlist e ações do domínio, sem eval, shell, SQL ou interpretação de conteúdo recebido. Resolver cargo/escopo no servidor para catálogo e execução, sem confiar no item oculto no menu. Passagem manual de commandId/actorId/role não concede acesso. Confirmação/reautenticação e idempotência são as mesmas do fluxo normal. `/help` responde privadamente; não publica protocolo ou relato no canal. Menções `@` resolvem IDs ativos e grupos autorizados; limitar busca e fanout para não enumerar pessoas nem gerar spam. Menção não concede acesso.

Inbox pertence apenas ao destinatário, inclusive em servidor administrado pelo observador. Recursos revogados e mensagens removidas deixam de fornecer prévias e totais; revalidar lista, abertura, badge e entrega em tempo real. Um log ou notificação não vira cópia permanente do conteúdo. Sugestões de menção e métricas do perfil obedecem à mesma contenção entre organizações/escopos.

Bio, localização, cargo profissional, foto e capa são dados de apresentação deliberadamente publicados aos colegas do mesmo servidor. Campos opcionais não são enriquecidos automaticamente; não coletar coordenadas/endereço ou inferir localização do IP. Exibir formulário com público de cada campo e permitir limpar opcionais. Foto/capa só de uploads internos inspecionados; não importar imagem de URL arbitrária nem renderizar HTML em bio. Handle e cargo profissional são independentes de role, e alteração não muda destinatários históricos de menções.

Mapa/total/foguinho são derivados dos créditos autorizados, sem permitir descobrir projeto privado por soma global, cache de outro visitante ou dia selecionado. Foguinho não coleta horas, presença contínua, pausas ou teclas; não cria ranking/avaliação individual. Direitos/eliminação pertinentes alcançam perfil, menções, Inbox, caches e derivados, conforme o procedimento já descrito. Não apresentar o incentivo como medida de valor profissional.

## 7. Retenção e exclusão

Proposta inicial: edição/exclusão de mensagem mantém marcador; conteúdo removido é expurgado após 30 dias; arquivo sem vínculo/reserva vencida é coletado em até 24h; projetos arquivados preservam histórico justificado. Logs de segurança: proposta de 90 dias com acesso administrativo limitado. Esses números não são prazos legais gerais: datas e limites devem ser confrontados com finalidade e obrigações de guarda aplicáveis, aprovados antes de produção e refletidos no aviso de privacidade.

Exclusão de conta não pode apagar silenciosamente autoria e comprometer projetos. Fluxo administrativo separa revogação de acesso, anonimização quando aplicável e retenções justificadas. Backups possuem janela própria; documentar quando conteúdo deixa também as cópias de recuperação.

## 8. Resposta a incidente

1. Registrar incidente, horário e responsável sem reproduzir segredo em ticket.
2. Conter: revogar sessão/chave, interromper rota ou desabilitar integração afetada.
3. Preservar logs mínimos e identificar organizações/recursos atingidos.
4. Corrigir causa e provar isolamento/regressão em ambiente separado.
5. Avaliar e realizar comunicações cabíveis à ANPD e aos titulares pelo responsável autorizado, conforme prazo e enquadramento regulamentares registrados no capítulo 12; manter linha do tempo e decisão documentadas.
6. Registrar causa, impacto, recuperação e ação preventiva.

Nenhum atendente deve solicitar senha, refresh token, chave de serviço ou acesso remoto irrestrito para resolver um ticket.

## Evidência desktop — v0.9

A prévia portátil implementa isolamento do renderer, navegação restrita e IPC por frame/origem, conforme [capítulo 14](14-aplicativo-desktop.md). Usa sessões do backend local; não implementa o fluxo Supabase de refresh token descrito como proposta acima. Não tem assinatura, updater ou criptografia própria em repouso. Administração local depende do acesso do operador ao usuário Windows/base; não é um papel remoto autenticado. Não promover esta prévia a distribuição pública de produção sem resolver essas condições.

## Segurança comercial —26/10/2026

Identidade financeira não concede acesso ao trabalho de outra empresa. Operador
da plataforma é allowlist própria, diferente de Admin do Studio. Segredos MP e
atestação ficam exclusivamente no servidor, fora de VITE_*, bundles e ZIP.
SQL real verificou isolamento, assinatura/replay, limites e coluna purged_at
não forjável. Falta operar retenção/limpeza de nonces e auditoria; não adotar
conservação indefinida por omissão. Evidências e limitações no
[guia comercial](../software-mvp/docs/billing.md).
