# Relatório de preparação da beta — 26/10/2026

## Atual: sala real no piloto local

LiveKit local oficial Windows verificado e integrado ao npm run dev. Reunir agora
abre a sala com participantes reais, controles de câmera/microfone, saída e tela
quando suportada. Teste com2 usuários recebeu áudio/vídeo sintéticos nos dois
sentidos, sem captura de dispositivos humanos. Guia: [sala real](meeting-room.md).

136 testes Node e builds passaram; revisão encerrou2P2 de capacidade e revogação.
Portas de sinalização/mídia restritas ao loopback. Nenhum firewall aberto, serviço
pago ou publicação. Servidor Windows sem monitor de CPU: piloto, não produção.
Chamadas públicas/duas máquinas e reuniões do domínio Supabase ainda faltam.
Não confundir mídia local funcional com beta online comercial completa. Histórico
abaixo registra o estado anterior, quando só existia a prévia.

## Reunião sem agendamento — ambiente local

Botão Reunir agora em Reuniões, Calendário e chat de projeto. Admin/Coordenador
escolhe título, projeto e pessoas; sem data/horário. meeting.instant usa relógio
do servidor, inclui o criador, notifica convidados e abre a prévia. Retry não
duplica; rebaixamento, projeto arquivado e convidado externo são recusados.
Instantâneas não aparecem na grade da agenda nem em próximos compromissos da Home.
A lista Reuniões permite reabrir; janela de acesso rápido de2 horas é metadado,
não duração confirmada da chamada. Não permite editar instantânea como agendamento.

Este incremento usa o backend JSON local existente; não acrescenta reuniões ao
domínio #central do Supabase. O instalador0.2.1 não foi substituído. Vídeo remoto
continua indisponível, sem participantes simulados e sem captura automática.
Interface avisa explicitamente que criar registro/prévia não inicia chamada.

131 testes Node e build completo passaram. QA em127.0.0.3 com dados fictícios
confirmou formulário sem datas, convite, abertura imediata e exclusão da grade
do Calendário. Nenhum acesso a câmera/microfone foi solicitado pelo agente.
Conta QA deslogada, aba fechada e servidor QA encerrado; base real preservada.

## Incremento atual: exportação administrativa

Admin ativo pode usar Exportar dados dentro do Studio online. NDJSON inclui
trabalho e histórico com índice de arquivos; não inclui bytes, Auth ou finanças.
Paginação, revalidação por página/final, limite20MiB/120s/2.000 páginas e nenhuma
resposta parcial. Cobertura vencida mantém leitura autorizada. Guia e evidências:
[exportação do Studio](studio-export.md). Não substitui backup/restauração.

129 testes Node e build completo passaram; SQL real com rollback e revisão
independente sem P1/P2 nesse escopo. Browser fictício confirmou interrupção,
reabertura e download; arquivo baixado verificou manifesto/complete e campos
privados ausentes. Migração17 aplicada no Forma; nenhum usuário/Studio/contrato
de teste permaneceu. Código novo ainda não integra o instalador0.2.1.

## Histórico: preparação comercial

Essencial ajustado para R$79/mês por Studio; Pro aprovado a R$149/mês.
Propostas empresariais são privadas, com preço e limites versionados por operador.
Landing e #central apresentam os dois planos. Backend de assinaturas Mercado Pago,
webhook verificado, conciliação, provisionamento idempotente e cotas foram
implementados no código e no Supabase Forma. Detalhes: [assinaturas](billing.md).

125 testes Node e builds passaram na implementação. SQL real com rollback cobriu
isolamento financeiro, pagamento repetido/tardio, preço versionado e cotas de
trabalho/Storage. A revisão encerrou os seis achados P1/P2 identificados. QA de
interface usou provedor fictício; não houve cobrança real. Advisors de26/10:
nenhum WARN/ERROR,12 INFO esperados em tabelas privadas com negação por padrão.

Vendas continuam bloqueadas no código, banco e ambiente. Faltam credenciais e
testes Mercado Pago, HTTPS/webhook público, mídia real, nova release desktop,
recuperação, backup/restauração, exportação integral com anexos, retenção/limpeza e
operação comercial/fiscal. Reservas de contratos externos cancelados não são
liberadas automaticamente. O instalador0.2.1 não foi substituído. Não houve deploy.

## Histórico: trabalho online de25/10

## Incremento atual: trabalho online

Além de conta/perfil/convites, #central agora tem Studio online com áreas,
projetos, tarefas em quadro/lista/calendário, conversas por contexto, documentos
versionados, arquivos privados e equipe20/página. Schema normalizado com RLS,
RPC invoker e sessão HttpOnly no projeto Forma. O JSON local permanece separado.
Detalhes, contratos e aceites: [trabalho online](central-work.md).

SQL real com rollback cobriu isolamento, cargos, versões, documentos, paginação,
prova de inspeção, Storage imutável, revogação e cancelamento. Advisors: nenhuma
ocorrência WARN/ERROR; INFO de RLS sem policy em upload_verifiers é intencional
(tabela privada sem grants ao usuário). UI autenticada foi exercitada com
provedor fictício, incluindo código literal, conflito e equipe20+3. Teste com
conta real e bytes no Storage remoto permanece pendente.

Vexo não foi ativado. O usuário confirmou que ainda vai cadastrar/confirmar
o e-mail informado pelo operador em #central. Não foi criada conta Auth por SQL nem senha
provisória. Após essa confirmação, falta provisionar o primeiro Admin e testar
convites e acesso com usuários reais em duas máquinas.

O usuário confirmou que ainda não tem projeto LiveKit Cloud. Criar/configurar
o projeto gratuito é dependência para ativar e testar mídia gerenciada. Não há
credenciais LiveKit disponíveis nem chamadas reais prontas. Nenhum plano pago.

Validação do código deste incremento:108 testes Node, tipagem e builds
web/desktop/API passaram. A revisão final encerrou os achados de revogação de
objetos retirados, resposta de chat fora de contexto e anexos concluídos durante
envio. Nenhum novo P1/P2 confirmado. Evidências documentais registradas no ledger
de execução após geração/check. Não houve novo instalador ou publicação pública.

Não foi concluída toda a beta. Recuperação, operação/auditoria do primeiro
Studio, limpeza de órfãos, chamadas reais, HTTPS e desktop remoto permanecem
necessários. O instalador0.2.1 continua a release anterior; a mudança existe
no código e no servidor local. Uma nova release deve avançar a versão.

## Evidências da etapa anterior

## Entregas desta etapa

| Pedido | Resultado | Evidência |
|---|---|---|
| Botão atualizar dentro do app | Configurações → Verificar e atualizar; reutiliza prompts nativos existentes | Bridge com canal fixo e main autorizado; instalador0.2.1 |
| Conectar Supabase | Projeto Forma gratuito separado, Auth alcançável | supabase:check real; SELECT1 no PostgreSQL pelo plugin |
| Continuar backend | GET /api/auth/identity e validação remota de bearer implementados | Testes HTTP/negativos, sem concessão de sessão/cargo local |
| Rever pendências | Matriz abaixo | Comparação com desenho beta e limites atuais |

90 testes passaram; build completo/tipagem aprovados. Revisão estática independente
sem problemas importantes no IPC e na integração de identidade. Testes de identidade
usam fixtures; conectividade real não substitui teste de login completo.

Instalador0.2.1: 136.958.419 bytes; SHA256
31e45cb2fa42cd258b126d043a44faa1e97f02e8385642790514a695cf546255.
O feed local mantém a chave pública de atualização existente. Instalação efetiva
e UI nativa em Windows limpo não estão comprovadas pelo build.

10.444 hashes do payload conferidos; smokes Electron session-pbnRbu e
operator-6lW5xq aprovados em perfis fictícios. Atualizador real session-4ZofPC
encontrou e baixou0.2.1, com progresso, sem executar instalador. Primeiro teste
ficou offline porque o servidor estava desligado; servidor foi iniciado e retry
passou. Não houve instalação no perfil Windows real nem QA visual do botão nativo.

Servidor local ficou disponível em http://127.0.0.1:5173. Rota de identidade da
API em execução recusou token propositalmente inválido com401 após consultar o
Supabase real; nenhuma conta/sessão criada. Login válido ainda requer seu fluxo
de frontend central. 18 testes documentais e geração/check passaram.

## Falta para lançar

| Prioridade | Falta | Aceite |
|---|---|---|
| Bloqueador | Aceite real do trabalho central | Código/RLS/UI implementados; confirmar com duas contas/dispositivos reais sem JSON |
| Bloqueador | Auth real completo e recuperação | UI/cookies prontos para conta; configurar entrega/redirecionamento, exercitar confirmação/login e implementar recuperação |
| Bloqueador | Operador central | Escopos implementados; falta operação auditada do primeiro Studio após cadastro confirmado |
| Bloqueador | Operação Storage | Fluxo privado implementado; validar bytes remotos reais, limpeza de órfãos e recuperação |
| Bloqueador | LiveKit gerenciado | Oito participantes, áudio/vídeo/tela, remoção e reconexão em duas redes |
| Bloqueador | Backend HTTPS hospedado e desktop conectado | Mesma base no navegador/app, sem abrir URL arbitrária |
| Bloqueador | Backup/restauração e avisos de privacidade | Restauração testada e fluxo real de fornecedores/retencão documentado |
| Bloqueador | Distribuição remota e QA Windows | Instalar/upgrade/desinstalar em máquina de teste, assinatura Windows decidida |
| Antes de ampliar | Acessibilidade e consumo | Teclado/leitor de tela, dispositivos físicos e cotas gratuitas exercitados |

Cloudflare Free foi confirmado pelo usuário. Worker de validação continua privado,
sem URL pública; não hospeda backend ou mídia. Atualizador ainda aponta a loopback;
computadores externos não recebem releases por esse endereço. Não habilitar produtos
pagos para contornar limites. LiveKit ainda não foi provisionado.

## Preservação e limites

Base local preservada: SHA256
EFA01673C632C05D57B23287DF329F33AE74D944A0268C5F5B091AFA842D790F.
Nenhum seed/migração no perfil real. Menzu não alterado. Projeto Supabase separado
Free/US$0; nenhuma assinatura paga ou publicação pública ativada nesta etapa.
Relatório não é auditoria jurídica ou pentest.

Guias: [Supabase](supabase.md), [atualizações](updates.md), [Cloudflare](cloudflare.md).
