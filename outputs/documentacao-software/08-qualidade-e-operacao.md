# 08 · Qualidade, ambientes e operação

Os aceites específicos da expansão estão no [capítulo 13](13-gestao-integrada-e-expansao.md): isolamento entre Studios, aprovação sem autoaprovação, tempo concorrente, quantias/moedas, estorno, importação recuperável e dados restritos de RH/ATS. O primeiro incremento CRM/comercial tem testes de domínio/HTTP/persistência e QA visual ali registrados. Horas, financeiro, importação e RH/ATS ainda não possuem módulos implementados ou testes funcionais executados. A validação documental não equivale a QA funcional dessas capacidades.

## 1. Metas não funcionais propostas

| ID | Meta | Como validar |
|---|---|---|
| RNF-01 | 30 membros, 15 simultâneos e 10.000 tarefas no piloto | Cenário de carga com dataset fictício; ajustar após inventário real |
| RNF-02 | p95 da API abaixo de 500 ms para leituras comuns e 800 ms para mutações | Medir no servidor sob carga do piloto; exclui mídia, transferência e provedor indisponível |
| RNF-03 | Atualização de tarefa/mensagem visível em outro cliente em até 2 s no p95 | Medição ponta a ponta em rede controlada, incluindo persistência |
| RNF-04 | Sala com até 8 pessoas, tela e áudio estáveis em cenário aprovado | Testar Electron real e redes distintas; medir perda, reconexão e qualidade |
| RNF-05 | Disponibilidade mensal alvo de 99,5% da API | Monitorar por sondas; é objetivo interno, sem SLA comercial |
| RNF-06 | Recuperação alvo RPO de 24h e RTO de 8h | Simular restauração de banco, objetos e configuração; confirmar recursos do plano contratado |
| RNF-07 | Acesso por teclado e zoom 200% nos fluxos principais | Teste manual e verificações automatizadas aplicáveis |
| RNF-08 | Revogação online em até 10 s | Suspender usuário durante API, socket e chamada; observar limites de URLs já emitidas |

Não existe garantia de capacidade ou desempenho enquanto os testes não forem executados. Volume de vídeos e minutos de reunião precisam de orçamento próprio.

## 2. Ambientes

| Ambiente | Uso | Dados e serviços |
|---|---|---|
| Desenvolvimento | Trabalho individual | Supabase local via CLI/Docker ou projeto dev; dados fictícios |
| Staging | Integração, QA e instalação de teste | Projeto Supabase e mídia separados; mesma arquitetura de produção |
| Produção piloto | Uso da equipe | Credenciais, buckets e banco próprios; acesso restrito |

Não copiar banco de produção para desenvolvimento. Variáveis têm schema validado no boot. Exemplo documental de categorias: `API_BASE_URL`, `SUPABASE_URL`, chave pública permitida ao cliente, issuer/JWKS esperado, credencial SQL restrita da API, segredo de webhook e credenciais de mídia apenas no servidor. Nomes finais serão definidos no template real; este documento não é um `.env` funcional.

Docker Compose proposto para API, worker e dependências auxiliares necessárias. Supabase local tem stack própria coordenada pela CLI. Usar healthchecks, rede privada e volumes nomeados. Electron é executado/empacotado fora de containers. Configuração gerenciada de produção pode usar Supabase remoto e API em host de containers; host e região ainda serão decididos.

## 3. Estratégia de testes

| Camada | Risco que deve provar |
|---|---|
| Unidade de domínio | Último Admin ativo, três cargos, escopo, status, prazos, contagem de conclusões e snapshot de responsáveis |
| Integração PostgreSQL | Transação, FK entre tenants, RLS, contexto do pool, duplicação de evento e concorrência |
| Integração Storage | Reserva, confirmação, conteúdo real, URL expirada e anexo de outro escopo |
| Contrato API | DTO, paginação, erro, versão e idempotência; spec OpenAPI coerente |
| Socket | Assinatura indevida, suspensão, reconexão e evento duplicado/fora de ordem |
| E2E | Convite → acesso → projeto → tarefa → conversa → reunião → conclusão → relatório |
| Electron instalado | Login persistente protegido, IPC, links, dispositivos, tela e atualização |
| Visual/acessibilidade | Referência, viewports, teclado, foco, contraste e zoom |

## 4. Casos de regressão indispensáveis

### Aceite dos cargos e das novas mídias

Executar futura suíte com Admin A, Coordenador Design, Coordenador RH, Usuário atribuído, Usuário não atribuído e Admin de outra organização. São critérios para implementação, não testes já executados neste pacote documental.

| Cenário | Resultado esperado |
|---|---|
| Coordenador convida pessoa para projeto atribuído | Convite como Usuário, sem liberar outra área |
| Coordenador força role admin/coordinator no convite ou PATCH do próprio perfil | Negado; nenhum cargo elevado, mesmo por API direta |
| Usuário tenta criar/delegar tarefa, chat, pasta ou reunião de trabalho | Negado; botões ausentes e backend recusa |
| Usuário responsável atualiza status e checklist | Permitido em sua tarefa conforme RN-05; tarefa alheia, reatribuição e reabertura negadas |
| Coordenador cria/delega tarefa, chat, pasta e reunião | Permitido só no escopo; troca de IDs não libera RH/outro projeto |
| Admin edita servidor/cargo/cadastro ou exclui associação | Permitido com reautenticação para ações críticas e auditoria; sem senha/token ou exclusão da identidade de outros servidores |
| Duas operações removem/rebaixam/suspendem Admins simultaneamente | Ao menos um Admin ativo permanece; operação perdedora falha |
| Admin é rebaixado durante inspeção de direto/RH | Consultas e subscriptions administrativas revogadas no alvo RNF-08; sem alegar recolher cópias baixadas |
| Admin inspeciona direto sem participar | Modo administrativo, aviso e trilha sem conteúdo; sem recibo, participação ou envio em nome alheio |
| Coordenador apaga mensagem de terceiro | Só canal coordenado; direto alheio negado; marcador/motivo, sem edição de autoria |
| Perfil, login e help | Todos veem perfil profissional permitido e editam própria conta; cargo alheio e tickets de terceiros negados |
| Imagem/áudio/vídeo: cancelamento, tipo inválido, retry e revogação | Sem publicação parcial/duplicada; captura explícita, prévia, reprodução acessível e inspeção de arquivo |
| Pasta movida para outro projeto ou ciclo entre pastas | Negado; nenhum novo acesso; arquivar pasta preserva anexo histórico |
| Feed, busca, relatórios e notificações | Mesma matriz RN-04; sem texto removido ou evento inacessível |

### Regressões transversais

1. Usuário A troca todos os IDs de projeto/tarefa/arquivo por IDs de workspace privado B; nenhum conteúdo ou agregado é retornado.
2. Admin ativo acessa áreas, projetos e todos os chats apenas do próprio servidor, inclusive RH/diretos sem associação; leitura administrativa gera trilha e não o torna participante. Admin de outra organização não acessa nada.
3. Suspensão durante uso encerra socket e chamada, impede nova credencial e bloqueia API.
4. Duas conclusões concorrentes produzem um primeiro evento válido e um único crédito por responsável.
5. Reabrir e concluir novamente não muda o dia nem soma contribuição; progresso acompanha estado atual.
6. Conclusão perto da meia-noite e mudança de timezone respeitam a regra de agrupamento.
7. Retry de mensagem após timeout não duplica; mesma chave com texto diferente retorna conflito.
8. Duas edições de documento preservam o rascunho do segundo usuário e retornam conflito.
9. Falha após gravar tarefa mas antes de publicar evento é recuperada pela outbox.
10. Upload cancelado não aparece como arquivo disponível; destino não autorizado não recebe intenção assinada.
11. Conexão SQL reutilizada não herda identidade; contexto ausente falha fechado.
12. Provedor de vídeo indisponível mantém tarefas, arquivos e chat operacionais.
13. Pedido de dados do usuário suspenso pode ser recebido e autenticado; resposta não revela conversas/dados privados de terceiros.
14. Eliminação/anonimização cabível alcança revisões, objetos e derivados; restauração de backup não reintroduz dados sem aplicar o registro de expurgo.

## 5. Pipeline de entrega proposto

Pull request → instalação por lockfile → lint/typecheck → testes relevantes → build API/desktop → migração em ambiente descartável → integração/E2E → revisão de alterações → staging → smoke test com pacote instalado → publicação aprovada pelo responsável.

Não exigir percentual arbitrário de cobertura como substituto dos casos críticos. Release registra versão, migrações, compatibilidade de clientes e instrução de rollback. Recursos incompletos permanecem ocultos, sem botões que simulam funcionamento.

## 6. Observabilidade

Logs estruturados com `requestId`, organização quando apropriado, rota, duração e código de erro. Excluir corpos de mensagens, documentos, tokens, URLs assinadas e senhas. Eventos administrativos têm trilha própria. Métricas: latência/erros API, conexões de socket, atraso da outbox, tentativas falhas de job, bytes de Storage e falhas de mídia.

Alertas iniciais: erro 5xx sustentado, falha de readiness, outbox atrasada, upload rejeitado em excesso, falha de backup e limite de orçamento próximo. Responsável e canal de alerta precisam ser designados antes do piloto; criar esta documentação não configura alertas.

## 7. Backups e recuperação

Confirmar cobertura e retenção do plano Supabase antes de contratar. Backup de PostgreSQL não deve ser tomado como backup de objetos. Documentar cópia de Storage, restauração de credenciais/configurações sem vazar segredos e ordem de retorno dos serviços.

Runbook de recuperação: declarar incidente → interromper escritas se necessário → escolher ponto de restauração → restaurar em ambiente isolado → verificar associações, contagem e objetos de amostra → reconciliar outbox/webhooks sem reenvio em massa → promover ambiente recuperado → validar clientes → comunicar impacto e perda estimada. Registrar tempo real e comparar com RTO/RPO propostos.

## 8. Rollback

Manter imagem anterior da API e instalador anterior. Migrações destrutivas não têm rollback automático por downgrade de binário; usar mudança compatível e plano de restauração/correção. Durante transição, suportar ao menos a versão anterior do cliente para evitar obrigar atualização simultânea. Não publicar atualização se rollback de sessão, contratos ou migração estiver indefinido.

## 9. Custos e limites

Sem orçamento aprovado, não estimar preço fechado. Planilha futura deve considerar: assentos, banco/compute, Storage acumulado, egress de arquivos/vídeo, minutos-participante de reunião, SMTP, API host, backups, observabilidade e certificado de assinatura. Exemplo de volume de mídia: 8 participantes × 60 minutos = 480 minutos-participante, sujeito à unidade comercial real do provedor. Aplicar cota e alerta antes de liberar uploads grandes.

## 10. Condição de pronto

### Aceite adicional da v0.6 · a executar na implementação

| Cenário | Resultado esperado |
|---|---|
| Menu / para cada cargo e mudança de cargo antes de executar | Catálogo correto; requisição manual proibida negada; rascunho preservado |
| Comando destrutivo cancelado e retry de criação após timeout | Cancelar não muda dados; retry não cria segunda tarefa/help/reunião |
| / em arquivo recebido, bio, trecho colado ou meio de texto | Nenhuma execução automática; só invocação explícita do compositor/catálogo |
| Usuário menciona Coordenador/Admin individual participante | Permitido no mesmo contexto, sem menção coletiva de cargo |
| Usuário força @todos/@admins; Coordenador força @admins/área alheia | Negado no servidor, sem fanout parcial ou revelação de nomes |
| Menções individual+grupo para a mesma pessoa; edição/remoção/reinclusão | Um alerta por mensagem/pessoa; novos recebem uma vez, removidos perdem item/prévia; sem renotificar todos |
| Coordenador usa @todos em canal com Admins | Só Usuários/Coordenadores elegíveis são expandidos; Admin não recebe alerta coletivo; menção individual permanece permitida |
| Menções em comentário: envio, edição, remoção e tentativa de origem de outro tenant | Mesma matriz do projeto; origem por comentário, dedupe própria e revogação; FK/CHECK rejeitam origem cruzada/dupla |
| Troca de handle e reutilização por outra pessoa | Menção antiga continua no ID original; não notifica o novo dono do texto |
| Perfil por servidor, cargos e campos opcionais | Bio/@/localização/capa/foto/cargo profissional não vazam entre equipes; editar Senior Software Engineer não altera role |
| Total de conclusões e mapa | Dataset com dois responsáveis, reabertura e reatribuição produz mesmo crédito de RN-10, sem duplicação |
| Foguinho e timezone | RN-23 validada em meia-noite, horário de verão, dias sem entrega, fins de semana e troca de timezone; vários créditos no dia contam um dia |
| Exemplo do foguinho | Segunda+terça=2; quarta sem entrega preserva 2; quinta sem quarta elegível=0 antes de nova conclusão, que inicia 1 |
| Perfil visto pelo titular e colega sem acesso ao RH | Nenhum total, dia, tooltip ou lista revela projeto fora da interseção autorizada; cache não reaproveita visão de outro observador |
| Inbox própria e tentativa de ler Inbox alheia por Admin | Própria disponível; alheia negada; acesso administrativo ao chat não muda essa regra |
| Marcar todas e chegada concorrente de novo item | Só itens até o cursor válido ficam lidos; o novo item mantém badge e estado entre clientes |
| Mensagem apagada ou acesso revogado com Inbox já aberta | Item/prévia e contador reconciliados; link antigo genérico; sem cópia no push/log |
| Teclado/leitor de tela e movimento reduzido | / e @ navegáveis, foco previsível, mapa com alternativa textual e foguinho com sequência por extenso |

Esses critérios não são executados pela suíte Python da documentação: ela verifica integridade de fontes/pacote, sem aplicativo, backend ou dados reais.

Requisito tem implementação real, critério de aceite comprovado, acesso negativo testado, estado de erro e documentação atualizada. Piloto completo exige instalação utilizável, serviços persistentes, backup restaurado em teste, responsável por suporte e orçamento/limites definidos. Também exige evidências pertinentes aos controles JUR-01 a JUR-10 do capítulo 12, incluindo atendimento a direitos, inventário de dados, retenção justificada e licenças de distribuição. Build ou interface estática, isoladamente, não comprovam esses requisitos.

## Evidência desktop — v0.9

Primeiro pacote Windows portátil e scripts de smoke entregues, com API e perfis temporários reais, 59 testes da aplicação e build aprovados. O [capítulo 14](14-aplicativo-desktop.md) discrimina aceites e limites; resultados específicos estão no guia desktop do MVP. Smoke técnico não comprova teste visual nativo, acessibilidade completa, dispositivos físicos ou funcionamento em máquina limpa. O pipeline de produção descrito acima continua proposto.
