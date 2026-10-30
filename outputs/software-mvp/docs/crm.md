# Clientes e comercial — incremento local EP-15

Entregue em 23/10/2026. Rotas `#clients` e `#sales`, acessíveis a Admin do próprio Studio e Coordenador nas áreas atribuídas. Usuário não recebe contatos, oportunidades ou propostas no snapshot; acessar a rota diretamente mostra estado restrito. Permissões são revalidadas no servidor, inclusive ao repetir uma solicitação.

## Como usar

1. Abra **Clientes → Novo contato** e escolha área, tipo (Cliente/Lead/Fornecedor), nome e dados opcionais. E-mail duplicado no Studio exige revisão do cadastro, sem mesclar registros automaticamente. A lista permite busca, filtro por área, edição e paginação de 20 contatos.
2. Use **Nova oportunidade** no contato ou em **Comercial**. Informe título, área, contato, descrição, valor estimado e etapa. Contato e oportunidade pertencem à mesma área; não se movem entre áreas depois de criados.
3. No pipeline, use **Editar etapa** para acompanhar Novas, Qualificadas, Em proposta ou Perdidas. Ganhas é definida pela conversão de uma proposta aceita. A trilha de etapas é persistida no registro.
4. Crie uma **Proposta**, informe escopo/condições e valor. Cada edição guarda a versão anterior; o histórico pode ser aberto no formulário. O formulário conserva sua versão original: edição concorrente gera conflito, sem sobrescrita silenciosa.
5. Para uma versão já salva, selecione **Registrar aceite desta versão salva**. Informe referência à decisão externa do cliente e confirme a declaração. É um registro interno de aceite recebido, sem envio de e-mail, assinatura eletrônica ou comprovação automática da identidade do cliente.
6. **Confirmar e criar projeto** cria projeto e chat na área da oportunidade, inclui o gestor criador no projeto e abre seu quadro. A oportunidade vira Ganha; o projeto inicia sem tarefas. Convide/atribua a equipe pelos fluxos existentes. As condições comerciais permanecem privadas; a descrição inicial do projeto é neutra para receber o briefing operacional.

Proposta aceita fica somente para leitura. Não é possível trocar o contato de uma oportunidade após criar proposta. Oportunidade convertida não pode ser editada; proposta concorrente da mesma oportunidade não cria outro projeto. Retry e solicitações simultâneas devolvem a mesma conversão. O link **Abrir projeto** só aparece quando o observador também tem acesso ao projeto.

## Valores e limites

BRL exclusivamente neste incremento; totais persistidos em centavos inteiros, de zero a R$ 10.000.000,00 por registro. Entrada aceita vírgula ou ponto decimal com até duas casas, sem separador de milhar. O valor estimado da oportunidade é distinto do total negociado na proposta: ambos permanecem identificados na tela.

Pipeline aberto soma estimativas de oportunidades que não são Ganhas/Perdidas. Contagem de convertidas não é receita, caixa ou resultado financeiro. Nenhum pagamento, fatura, documento fiscal, desconto calculado, imposto ou lançamento contábil é gerado. Sem conteúdo fictício pré-inserido na base real.

Esta entrega não inclui exclusão/mesclagem de contatos, múltiplos pipelines configuráveis, linhas de itens, PDF de proposta, vínculo manual de cliente a projeto antigo, importação/exportação ou envio externo. São refinamentos posteriores de RF-30/31/39/41, não botões simulados. Horas, custos, HRM e ATS continuam no roadmap.

## Contratos reais

O MVP mantém `POST /api/actions`, com envelope `{ type, payload, requestId }` e sessão autenticada. Não implementa o prefixo futuro `/api/v1/studios` do plano arquitetural.

| Ação | Payload |
|---|---|
| `crm.contact.save` | `workspaceId, name, email, phone, company, notes, kind`; atualização inclui `id, version` |
| `crm.opportunity.save` | `workspaceId, contactId, title, description, stage, valueCents`; atualização inclui `id, version` |
| `crm.proposal.save` | `opportunityId, title, body, totalCents`; atualização inclui `id, version` |
| `crm.proposal.accept` | `id, version, acceptanceNote`; retorna `id, projectId` |

Validação estrita rejeita campos desconhecidos e quantias fracionárias em centavos. Versões conflitantes retornam 409; acesso não autorizado é negado sem conceder permissão por payload. `GET /api/state` inclui `crm.contacts`, `crm.opportunities`, `crm.proposals` filtrados. Propostas não são publicadas como Docs, mensagens ou descrição de projeto.

## Persistência, operação e recuperação

`State.crm` é uma extensão opcional do schema JSON v2. Base antiga sem essa propriedade continua legível e só a recebe na primeira escrita comercial. Nenhuma migração destrutiva ou reseed é necessário. Serialização preserva as coleções existentes; Store publica o conjunto transacionalmente, incluindo proposta, oportunidade, projeto, associação e chat. Coleções CRM malformadas interrompem a transação, em vez de serem apagadas/recriadas.

Mantêm-se o backup anterior por escrita e o backup v1 descritos no README. Antes de atualizações operacionais, preservar o conjunto completo de dados conforme o procedimento existente. Não editar a base em paralelo com a API. Limite atual: um processo escritor com fila local; PostgreSQL e escala horizontal continuam propostas.

Contatos e notas devem conter apenas dados necessários ao relacionamento. Aplicam-se os controles JUR-01 a JUR-10 existentes: acesso por Studio/área, trilha sem conteúdo privado, inventário, retenção e atendimento a direitos por procedimento já documentado. A entrega não declara fundamento jurídico ou conformidade concluída, nem altera as cópias legais.

## Evidências

Suíte do MVP: 51 testes, incluindo oito novos testes CRM (cinco domínio, dois persistência, um HTTP). Cobrem sessão, mass assignment, isolamento, revogação em retry, e-mail duplicado, revisão/conflito, conversão única concorrente, reinício, proteção de coleção corrompida e não divulgação de condições comerciais a Usuário do projeto. Typecheck/build passaram.

QA visual em fixture isolada na porta 4192: cliente → oportunidade de R$ 12.500,50 → proposta v1 → revisão de R$ 13.000,00 → aceite → projeto e chat. O servidor foi reiniciado preservando a fixture antes do aceite. Busca sem resultados e viewport de 390 px conferidos; página permaneceu em 390 px e pipeline com rolagem interna. Screenshot `outputs/software-mvp/preview-crm.png` contém somente dados fictícios.
