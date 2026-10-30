# 12 · Legislação e aplicabilidade

**Extensão de escopo em 23/10/2026:** CRM, RH/ATS, horas, custos e operações planejados no [capítulo 13](13-gestao-integrada-e-expansao.md) ampliam os tratamentos a inventariar em JUR-01 a JUR-10. São controles de engenharia propostos, sem nova conclusão jurídica. A base normativa deste capítulo não prova cobertura de ponto, folha, recrutamento, contabilidade, tributação ou pagamentos. Revisar normas oficiais específicas e contexto antes da implementação/uso real correspondente. Nesta extensão não se atualizaram cópias legais nem se declarou conformidade.

**Versão 0.3 · Incorporado por solicitação do usuário · 21/10/2026**

Escopo confirmado: referências relevantes ao software de trabalho da equipe. Esta seção introduz controles de produto e critérios de verificação; não afirma implementação nem conformidade concluída. Fontes e cópias estão no [inventário legal](../referencia-legal/README.md).

## 1. Referências e enquadramento

| Norma | Dispositivos examinados para este produto | Aplicação a verificar |
|---|---|---|
| LGPD, Lei 13.709/2018 | Arts. 1, 3–9, 11, 14–16, 18–20, 33, 37, 39, 41, 46, 48–50 | Tratamento de dados pela equipe; exceções dependem de quem trata e para qual finalidade |
| Marco Civil, Lei 12.965/2014 | Arts. 3, 7, 8, 10, 11, 13–16, 19, 21 e 22 | Comunicações e registros; não equiparar aplicação a provedor de conexão |
| Software, Lei 9.609/1998 | Texto oficial, especialmente arts. 2–6 e 9; arts. 7–8 em eventual comercialização | Titularidade, autorização de uso e distribuição do código |
| Direitos autorais, Lei 9.610/1998 | Arts. 7, 8, 22, 24, 27–29, 37, 46, 49, 50, 102, 107 e 108 | Materiais enviados, assets, conteúdos e licenças |
| Inclusão, Lei 13.146/2015 | Arts. 3, 4, 55 e 63 | Desenho universal; alcance específico a sites e disponibilização deve ser analisado |

O uso por amigos não estabelece sozinho a exceção de fins exclusivamente particulares e não econômicos do art. 4º, I, da LGPD. A plataforma foi descrita como ferramenta de trabalho, portanto adotará controles de privacidade desde a concepção, enquanto se documenta o enquadramento concreto. Esta é uma decisão de engenharia do projeto, sem concluir fatos ainda desconhecidos sobre a organização. [LGPD oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm).

## 2. Controles obrigatórios para a continuidade

Os controles abaixo são instruções de projeto decorrentes da solicitação do usuário. A seleção dos mecanismos técnicos é proposta de engenharia, não transcrição de obrigação literal de cada lei.

| Controle | Definição no produto | Evidência antes do piloto |
|---|---|---|
| JUR-01 Inventário de dados | Registrar categoria, finalidade, responsável, fundamento a avaliar, destinatários, região e prazo por tratamento | Inventário preenchido para conta, chat, arquivos, RH, presença, métricas, suporte e mídia |
| JUR-02 Transparência | Disponibilizar aviso claro e canal de privacidade; diferenciar necessários e opcionais | Aviso revisado e canal operante, sem consentimento genérico |
| JUR-03 Direitos | Receber, verificar legitimidade, responder e executar pedidos aplicáveis | Simulação de acesso/correção e eliminação com proteção de terceiros |
| JUR-04 Ciclo de vida | Retenção por finalidade e eventual obrigação; eliminar/anonimizar quando cabível, inclusive objetos e derivados | Procedimento exercitado e exceções registradas |
| JUR-05 Acesso e segurança | Autorizar domínio, storage, socket e sala; preservar sigilo do conteúdo | Testes negativos descritos no capítulo 08 |
| JUR-06 Fornecedores | Identificar operadores/suboperadores, regiões, acesso de suporte e mecanismos de transferência quando necessários | Registro do fluxo real e revisão dos termos dos serviços escolhidos |
| JUR-07 Incidentes | Ter responsável, avaliação de risco, escalonamento e comunicação no enquadramento aplicável | Simulado com linha do tempo e registro de decisão |
| JUR-08 Direitos sobre materiais | Conferir licença de dependências, fontes, ícones, fotos, vídeos e contribuições | Inventário de origem/licenças e avisos exigidos na distribuição |
| JUR-09 Acessibilidade | Implementar teclado, foco, contraste e suporte a tecnologias assistivas | Teste do percurso principal com leitor de tela e teclado no Electron |
| JUR-10 Revisão normativa | Revalidar texto oficial quando mudar finalidade, público, gravação, IA ou distribuição | Registro da fonte, versão consultada, análise e controles afetados |

## 3. Tratamentos do produto

| Fluxo | Dados esperados | Decisão prática para implementação |
|---|---|---|
| Convite e conta | E-mail, nome, identificadores e sessão | Apenas destinatário aceita; não pedir CPF/endereço para colaboração comum |
| Tasks e contribuições | Responsáveis, comentários, datas e entregas | Explicar métrica; sem ranking automático de produtividade |
| Chat e arquivos | Texto, conteúdo de anexos e metadados | Acesso por escopo; suporte não lê conversas por padrão |
| Reunião | Voz, imagem, identificação técnica e participação | Usuário escolhe dispositivos; gravação/transcrição continuam fora do piloto |
| RH | Pode conter dados pessoais e eventualmente sensíveis | Área restrita não basta: definir finalidade/categorias antes de coletar documentos sensíveis |
| Suporte e segurança | Relato, logs mínimos e requestId | Evitar reprodução desnecessária de conteúdo privado |

O fundamento de cada tratamento será registrado conforme o contexto, distinguindo dados comuns e sensíveis. Habilitar microfone no Windows não equivale a consentir com gravação, publicidade ou treinamento de modelos. A hipótese de trabalho com menores demanda revisão específica antes do uso correspondente; não se deve assumir que todos os amigos são adultos.

## 4. Direitos dos titulares desde o piloto

O acesso aos próprios dados não fica adiado com o recurso futuro de exportação completa da organização. No piloto, um procedimento manual restrito pode atender pedidos sem criar uma central automatizada de privacidade. O responsável deve:

1. Receber o pedido por canal comunicado ao titular, inclusive quando a conta estiver suspensa.
2. Verificar identidade por meio proporcional, sem exigir documentos adicionais automaticamente.
3. Classificar o pedido, localizar dados em Auth, domínio, Storage, mídia, suporte e fornecedores pertinentes.
4. Separar dados do requerente de dados privados de colegas; validar resultado antes de entregar.
5. Executar ou responder fundamentadamente, registrando eventuais retenções e limites aplicáveis.
6. Usar entrega segura, com registro da resposta e descarte de arquivos temporários.

O art. 19 da LGPD diferencia resposta simplificada imediata e declaração completa em até 15 dias para confirmação/acesso. Esse prazo não deve ser copiado como prazo universal para qualquer pedido; verificar regras aplicáveis ao caso. [Fonte oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm).

## 5. Retenção e histórico

Os prazos de 24h para reservas, 30 dias para conteúdo excluído e 90 dias para logs, existentes na proposta, são escolhas operacionais iniciais. Não são prazos legais gerais. Sua adoção depende de finalidade, necessidade e eventuais obrigações de conservação. Histórico de tarefas, revisões, créditos de conclusão, outbox e backups precisam entrar na análise; chamar uma tabela de append-only não autoriza preservação permanente de dados identificáveis.

Quando houver eliminação/anonimização cabível, a trilha pode preservar um evento técnico mínimo sem conteúdo ou identificadores pessoais desnecessários. A arquitetura precisa prever essa transformação e a indisponibilidade dos objetos. A política deve indicar efeitos em métricas e backups e impedir reintrodução por restauração de cópia antiga.

A guarda de seis meses do art. 15 do Marco Civil está vinculada ao enquadramento descrito no dispositivo; não será aplicada automaticamente a todo piloto interno nem ao conteúdo das mensagens. O dever de guarda de registros de conexão de um provedor de acesso também não é uma regra genérica para este aplicativo. Determinações de preservação exigem avaliação específica e impedem descarte incompatível com o dever aplicável. [Marco Civil oficial](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm).

## 6. Incidentes, fornecedores e transferências

O runbook deve registrar quando o controlador tomou conhecimento do incidente, categorias/volume afetados, risco, medidas adotadas e decisão de comunicação. A orientação oficial consultada aponta três dias úteis para comunicação de incidentes abrangidos pelo regulamento, ressalvados prazos específicos. Antes da operação, verificar o regulamento e eventuais regras diferenciadas aplicáveis ao agente; não assumir que toda equipe recebe automaticamente prazo em dobro. Comunicação externa só será realizada pelo responsável autorizado. [Orientação da ANPD](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis).

Usar uma região brasileira para PostgreSQL não prova que todo o fluxo fica no Brasil. Mapear Auth, backups, storage, logs, mídia, e-mail e acesso de suporte. Se houver transferência internacional, examinar mecanismo válido e regulamentação aplicável antes de enviar dados reais. Não cadastrar “consentimento” como justificativa automática em todos os fornecedores.

## 7. Código, conteúdo e acessibilidade

O projeto deverá manter inventário de dependências e assets, seus titulares/licenças e obrigações de distribuição. Contribuições dos amigos exigem definição de titularidade e permissão de uso; participar de um workspace ou enviar um arquivo não transfere automaticamente direitos patrimoniais ao criador do sistema. Avisos de terceiros acompanham o pacote quando exigidos. A licença final do produto permanece a definir. [Lei do Software](https://www.planalto.gov.br/ccivil_03/leis/l9609.htm), [Direitos autorais](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm).

A referência visual orienta composição; logos, fotos, fontes e assets específicos exigem origem própria ou autorização compatível. O canal de suporte poderá receber relatos sobre conteúdo indevido, sem promessa de imunidade ou fórmula genérica de remoção. A leitura isolada do art. 19 do Marco Civil não basta para concluir o regime atual de responsabilidade: jurisprudência e particularidades do serviço devem ser verificadas quando essa decisão for necessária.

A acessibilidade permanecerá no aceite do produto: operar tarefas sem arrastar, foco previsível, nomes acessíveis, zoom e teste com leitor de tela. A meta WCAG proposta é critério técnico de engenharia; não equivale a certificação jurídica. O art. 63 da LBI trata de sítios de internet nos contextos indicados, e não estabelece por si só que todo shell Electron tenha o mesmo enquadramento. [Lei Brasileira de Inclusão](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm).

## 8. Evidências, limitações e revisão

O download preserva um commit do acervo e os bytes das fontes oficiais no [manifesto](../referencia-legal/manifesto.json). Foram lidos dispositivos pertinentes, sem leitura exaustiva do ordenamento.

Duas divergências já foram identificadas: o acervo da Lei do Software só contém retificação; a LGPD oficial apresenta alterações institucionais da ANPD ausentes na cópia Markdown. Nenhuma cópia foi silenciosamente reescrita. Não considerar a expressão “texto vigente” do cabeçalho suficiente para atestar atualidade.

Regulamentos da ANPD, enquadramento de pequeno porte, decisões judiciais, normas trabalhistas específicas de um RH futuro, direitos de imagem e regras de relações de consumo poderão acrescentar exigências. A seleção atual é uma base de consulta, não lista exaustiva de normas aplicáveis.

Esta seção deve ser revisada antes do piloto com dados reais e a cada alteração relevante de finalidade, fornecedores, público ou modelo comercial. Responsável operacional e fundamentos de tratamento ainda precisam ser definidos por quem efetivamente conduzirá o produto; sua indicação não foi presumida nesta documentação.

## 9. Atualização de cargos e comunicação · 22/10/2026

**Pedido de produto:** Admin acessa todas as áreas/chats do próprio servidor; Coordenador gerencia os escopos atribuídos; Usuário colabora. Acesso administrativo a diretos e RH é mudança em relação à proposta anterior e deve constar do inventário/aviso antes de uso real. Não concluir que o cargo, sozinho, legitima qualquer leitura de conteúdo.

**Base consultada:** texto oficial da [LGPD, arts. 6, 9 e 46](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm) e [Marco Civil, arts. 7 e 10](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm), consultados em 22/10/2026, mantêm referências a finalidade, transparência, segurança e proteção das comunicações. A seleção técnica de permissões não resolve o enquadramento jurídico de uma equipe real; fundamento, necessidade e limites precisam da revisão prevista antes do piloto.

**Controles de engenharia:** JUR-01/02/05/10 cobrem aviso explícito de inspeção, mínimo acesso administrativo, organização correta e trilha sem conteúdo; JUR-03/04 cobrem exclusão de associação sem apagar autoria ou bloquear direitos; JUR-08/09 cobrem referência visual, mídia e acesso com teclado. Mensagem de áudio é envio explícito, sem gravação de reunião ou transcrição implícita. Perfil público interno não inclui automaticamente contatos/dados de RH vistos nas imagens. Evidências de aceite estão no capítulo 08. Snapshots legais e manifesto permanecem preservados; não houve atualização silenciosa do acervo nem declaração de conformidade.

## 10. Perfil, incentivo e notificações · atualização v0.6

Aplicar os controles existentes aos novos tratamentos, como escolha de engenharia:

- **JUR-01/02:** inventariar perfil ampliado, destinatários de menções, Inbox e derivados de conclusão; informar que bio/foto/capa/localização/cargo profissional são visíveis no servidor, sem perfil público externo. Localização é opcional e autodeclarada, sem GPS ou endereço preciso obrigatório.
- **JUR-03/04:** procedimentos de correção/exclusão contemplam handle, foto/capa, menções persistidas, Inbox, créditos e caches. Referências por ID não justificam preservar identificadores ou prévias para sempre; retenção deve ser fundamentada no fluxo real.
- **JUR-05:** comandos e menções revalidam cargo/escopo; Inbox é pessoal mesmo para Admin; contagens e foguinho não revelam projeto restrito. Não coletar horas, teclas ou presença contínua para o incentivo.
- **JUR-08/09:** usar assets próprios/licenciados na interface; mapa/foguinho têm alternativa textual e interação por teclado. As duas imagens novas são referência documental, sem certificação ou licença de reutilização de seus elementos.

Os dispositivos oficiais já consultados e os limites dos capítulos anteriores continuam sendo a base de análise; esta extensão não afirma nova obrigação literal, fundamento jurídico definido ou conformidade concluída. Antes de dados reais, revisar finalidade e comunicação do incentivo com os responsáveis pelo produto. O acervo e seu manifesto não foram modificados.

## Registro de engenharia desktop — v0.9

A distribuição portátil descrita no [capítulo 14](14-aplicativo-desktop.md) preserva avisos de licença do runtime e dependências, exclui dados/perfis/.env do pacote e registra hashes de arquivos. Dados ficam no perfil do usuário Windows; backups e atendimento a titulares continuam sob operação responsável. Não se alteraram snapshots legais, prazos ou conclusões de aplicabilidade. O pacote não certifica conformidade e ainda exige revisão de inventário/licenças e acessibilidade antes de liberação para produção.
