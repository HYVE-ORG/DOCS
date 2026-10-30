# Preparação do backend para a beta — incremento 1

24/10/2026. Implementado: contrato de persistência injetável. O produto continua
em modo local; banco central e chamadas remotas ainda não estão disponíveis.

## Mudança

apps/api/src/state-store.ts define StateStore.read e StateStore.transact.
createApp(directory, port, options) aceita options.store opcional. Sem essa opção,
constrói o mesmo Store JSON no diretório informado. Adapter fornecido precisa
implementar ambos os métodos; configuração parcial falha antes de abrir a API.
Falhas posteriores de leitura/escrita retornam erro, sem recorrer a outra base.

O diretório de uploads deriva do argumento directory da API. A persistência do
estado não precisa expor caminhos de disco. Upload/download continuam aplicando
as mesmas permissões no servidor. Isto não cria Storage remoto: arquivos ainda
ficam no disco local da API.

Não há variável de ambiente que ative um banco remoto neste incremento. A opção
é uma composição interna do backend, não um parâmetro aceito por endpoint.
Não usar um adapter em memória com dados reais: ele existe apenas nos testes.

## Contrato e limites para o próximo adapter

read espera transações anteriores e entrega um estado que o chamador pode usar
sem alterar a versão persistida. transact recebe draft isolado, permite callback
assíncrono e resolve somente após commit. Rejeição não persiste o draft e não
inutiliza a próxima transação. O Store JSON preserva fila, backup e migração.

Callbacks atuais podem ter efeitos em arquivos. Um futuro adapter SQL não pode
repeti-los automaticamente durante retry de serialização. A interface não aprova
salvar todo o produto em um blob PostgreSQL nem define a migração central.

Testes com duas APIs compartilham um adapter em memória dentro do mesmo processo.
Isso comprova a fronteira e a manutenção das autorizações; não comprova transações
entre processos, Socket.IO distribuído, Storage compartilhado ou uso remoto.
Nunca apontar duas APIs para o mesmo state.json como solução para a beta.

## Verificação

Novos testes: state-store.test.ts e app-store.test.ts. Cobrem transação assíncrona,
rejeição/recuperação, duas APIs, conta sem Studio, configuração inválida, erro HTTP
sem fallback, uploads privados com store sem directory e reabertura do JSON.

69 testes anteriores +6 novos: 75 passaram. A falha de tipagem pela interface
ausente e quatro falhas de integração foram observadas antes da implementação;
depois os seis testes específicos passaram. Build completo e tipagem passaram,
incluindo web, desktop sem landing e bundles da API. Testes usam diretórios
temporários, sem seed da base real.

Comandos na raiz do MVP:

```powershell
node --import tsx --test tests/state-store.test.ts tests/app-store.test.ts
npm test
npm run build
```

Base real preservada, SHA256 anterior e posterior idênticos:
EFA01673C632C05D57B23287DF329F33AE74D944A0268C5F5B091AFA842D790F.
Não houve nova dependência, serviço remoto, migração ou publicação. O instalador
0.2.0 já distribuído não foi substituído por uma release com o mesmo nome.

## Próximos incrementos

Identidade, PostgreSQL e arquivos centrais; conexão segura do desktop; LiveKit
Cloud com tokens por sala e revogação; interface de chamadas; testes entre redes
e operação/distribuição da beta. A primeira beta exige áudio/vídeo interno real,
conforme escopo aprovado. Este incremento sozinho não habilita esse aceite.

Controles aplicáveis: JUR-04/05/08/10 do capítulo12. Não muda finalidade de dados,
fornecedor ou retenção; conserva controle de acesso e mantém snapshots legais.
Não representa auditoria de segurança ou declaração de conformidade.
