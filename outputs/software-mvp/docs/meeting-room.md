# Sala real de áudio e vídeo — piloto local

26/10/2026. O Forma agora conecta participantes reais em uma sala LiveKit,
com grade, identificação, áudio remoto, câmera, microfone, saída e compartilhamento
de tela quando o navegador permite. Reunir agora entra diretamente na sala com
dispositivos desligados. Reuniões agendadas têm Entrar na sala. A prévia continua
disponível, mas não é mais o único fluxo quando a mídia está configurada.

## Usar nesta máquina

Abra http://127.0.0.1:5173/#meetings ou http://127.0.0.1:4100/#meetings.
Admin/Coordenador cria Reunir agora e seleciona pessoas com acesso ao projeto.
Convidados podem entrar pelo registro/Inbox. Use Microfone e Câmera para ativar
dispositivos; Compartilhar tela pede seleção explícita da janela/tela. Sair da
reunião ou fechar a sala desmonta a conexão e encerra as capturas locais.
Até8 participantes por sala; o piloto limita32 salas ativas no servidor.

O servidor local foi baixado da release oficial LiveKit1.13.11 Windows amd64 e
verificado por SHA256 do arquivo ZIP:
5D071EA43339F0140D24A66F0B2FF8A7BF6C4D0DCEB19B30ABCA835670213667.
Binário em .tools/livekit, ignorado pelo Git e ausente do pacote documental.
Código upstream sob Apache2.0; preservar licenças na distribuição futura.

Para reproduzir o piloto: executar scripts/install-media-local.ps1 no Windows,
configurar .env.media.local com LIVEKIT_URL=ws://127.0.0.1:7880,
LIVEKIT_API_KEY=devkey e LIVEKIT_API_SECRET=secret (credenciais públicas de
desenvolvimento, exclusivamente loopback). npm run dev carrega esse arquivo
ignorado e inicia API, Vite e LiveKit. Não copiar essas credenciais para servidor
público. .env principal e segredos Supabase/Mercado Pago não foram expostos.

scripts/livekit-local.yaml restringe sinalização TCP7880 e mídia UDP7882 ao
loopback; transporte TCP alternativo desativado. enable_loopback_candidate e filtro
127.0.0.0/8 são necessários para o WebRTC local. Não foi aberto firewall nem
habilitado acesso externo. No Windows o servidor informa que o monitor de CPU
não é suportado; a gestão de capacidade por CPU fica indisponível. O piloto
continua sujeito aos limites explícitos da aplicação e não é servidor de produção.

## Autorização

POST /api/meetings/:id/join exige sessão local atual, origem autorizada, corpo
{} e acesso ativo ao projeto. É necessário convite ou permissão de gestor.
Reuniões encerradas ou com início além de15min no futuro não admitem entrada.
Instantâneas usam a janela de2h existente. Um hash de organização/evento identifica
a sala, sem nomes/e-mails. Identidade é opaca; nome de exibição é enviado ao
servidor de mídia. Tokens de120s só permitem entrar/publicar/assinar na própria
sala; não concedem administração. API key/secret ficam exclusivamente no backend.

O backend revalida leases e remove acessos revogados periodicamente; o cliente
também confere presença a cada3s e desconecta se perder autorização ou a API.
Remoções paralelas usam timeout de3s, com nova tentativa se necessário. Não há
garantia de revogação em exatamente3s: agendamento, rede e inspeção de presença
a30s acrescentam atraso. Capacidade usa salas realmente ativas, sem consumir vaga
por participação histórica. Cache de admissões: limite8192, retenção15min após
última presença observada, cobrindo tokens renovados de10min do LiveKit.

Na hospedagem própria, remover participante não invalida seu JWT imediatamente.
O servidor conserva a revalidação para desconectar reconexões indevidas; novas
emissões são recusadas. Leases são em memória e não sobrevivem ao reinício da
API. Reinício coordenado do piloto encerra também o SFU. Para produção remota,
validar revogação com o provedor, persistência/recuperação de admissões e operação
distribuída. Não tratar este piloto como isolamento já auditado em produção.

Não há gravação, transcrição ou upload de áudio/vídeo pelo Forma. A mídia passa
pelo SFU com transporte WebRTC cifrado; não foi implementada criptografia ponta
a ponta contra o servidor. Não prometer E2EE. Tela/dispositivos só são publicados
depois de ação explícita do participante.

## Evidências

Dois usuários fictícios em origens isoladas entraram na mesma sala real e cada
interface mostrou2 participantes. Harness separado publicou vídeo de canvas e
áudio sintetizado: ambos os lados receberam2 faixas remotas e decodificaram1
vídeo remoto. Isso testa transporte de mídia real sem câmera/microfone humanos.
Captura por hardware, compartilhamento no Electron e rede entre máquinas ainda
precisam de teste com o usuário; não foram presumidos a partir desse harness.

136 testes Node passaram, incluindo autorização/origem/DTO, token, sala8,
revogação e capacidade baseada em salas ativas. Tipagem e builds passaram. A suíte
agora usa concorrência2 porque execução paralela com build excedeu a memória
disponível; a repetição limitada passou. Revisão independente encerrou2 achadosP2
de capacidade histórica e remoção sequencial, sem novo P1/P2 nesse escopo.

O SDK de conferência carrega sob demanda. Seu chunk é maior que500kB; o aviso de
build é conhecido e não impediu a compilação. QA usou base descartável, sem seed
na base de uso ou no Supabase. Contas fictícias deslogadas e servidores QA parados.

## O que continua faltando

Este endereço funciona nesta máquina; não é convite utilizável em outro computador.
Não há projeto LiveKit Cloud provisionado, domínio público WSS/TURN ou configuração
de cliente desktop remoto. A integração de reuniões no domínio Supabase #central
também permanece pendente: o piloto usa as contas/eventos do ambiente JSON local.
O instalador0.2.1 não foi substituído. Limites comerciais de minutos não foram
ativados, não houve serviço pago, publicação ou liberação de cobranças.

Para mídia gerenciada, configurar LIVEKIT_URL WSS e chaves próprias somente no
servidor; WS remoto e segredo fraco remoto são recusados. CSP permite a origem
configurada, sem wildcard de serviços externos. Antes de vender, testar identidade
central, capacidade/medição, revogação, falhas e custos no ambiente real escolhido.

Fontes oficiais consultadas: [servidor local](https://docs.livekit.io/transport/self-hosting/local/),
[tokens e revogação](https://docs.livekit.io/frontends/reference/tokens-grants/),
[configuração da release](https://github.com/livekit/livekit/blob/v1.13.11/config-sample.yaml).
Context7 indisponível; consulta às fontes oficiais. Aplicam-se os controles de
privacidade/transparência de reuniões existentes; nenhuma certificação jurídica.


### Interface refinada — 26/10/2026

Controles agrupados e responsivos, conexão real no cabeçalho e lista expansível dos
participantes LiveKit. Dispositivos continuam desligados na entrada. Não adiciona
IA, gravação, transcrição, novos dados de presença ou provedor remoto. Fluxo de acesso
e encerramento permanece o mesmo. Detalhes visuais no capítulo03 da documentação.


## Estrutura de Meet — 26/10/2026

A sala agora abre em um dialog amplo, com cabeçalho próprio, palco principal,
miniaturas selecionáveis, barra de mídia e conteúdo do projeto. Em Foco, a seleção
automática prioriza tela compartilhada e depois falante ativo; uma miniatura fixa
sua câmera/tela. Tocar outra vez desfaz a fixação. Automático restaura o acompanhamento.
Grade apresenta todas as faixas disponíveis. As setas percorrem as miniaturas.

O painel lateral alterna Resumo/Participantes e pode ser fechado/reaberto. Resumo
mostra nome/descrição do projeto, área, fuso, tarefas pendentes e arquivos reais;
não é geração por IA. Participantes vem das conexões LiveKit, sem confundir pessoas
convidadas com pessoas conectadas. Não há gravação ou transcrição nesta etapa.

As abas inferiores são Chat, Arquivos, Tarefas e Notas. O chat é o chat persistente
do projeto, identificado na interface: pode ser lido por outras pessoas autorizadas
fora da reunião. Envio usa a mesma mutação, autorização e chave de retry do domínio.
Não é uma conversa privada dos participantes da chamada. Arquivos mostra conteúdos
autorizados por projeto/conversa, permite download e usa o upload existente do projeto.
Tarefas apresenta status e detalhes expansíveis. Notas lê os documentos do projeto;
não são notas privadas nem uma ata/transcrição automática da reunião.

No celular, palco e miniaturas precedem os cartões de contexto e conteúdo. A barra
de microfone, câmera, tela (quando suportada), sair, automático e pessoas fica fixa
na base. O dialog mantém seu fechamento e o foco/teclado nativos. Dispositivos
continuam desligados na entrada. Aviso de dispositivo não esconde os controles;
erro fatal desmonta a conexão e mantém o fechamento/retry acessível.

Implementação: MeetingRoom.tsx, meeting-room.css, meeting-view.ts e classe opcional
no Modal existente. Sem novo serviço, dependência, schema ou permissão. As assinaturas
utilizadas foram conferidas na versão instalada dos componentes LiveKit. Context7
não foi consultado nesta rodada, pois suas ferramentas não estavam disponíveis.

Verificação: teste da seleção de foco antes/depois da implementação;138 testes Node
passaram. Build web/desktop/API e typecheck passaram. Fixture isolado conectou duas
contas fictícias; vídeo remoto sintético decodificado no palco e nas miniaturas,
grade e destaque manual funcionaram. Chat persistiu mensagem de QA; tarefas, notas
e lista real de participantes foram verificadas. O harness sintético agora publica
com source Camera/Microphone explícitos, como os dispositivos reais. A tentativa de
upload pela automação do seletor de arquivos não foi concluída antes da expiração
da reunião; não é evidência de upload pela nova interface. Backend de arquivos
continua coberto pela suíte existente. Sem teste de hardware real ou chamada remota.

Controles aplicados: JUR-05 (escopo em mídia/chat/arquivos), JUR-08 (estrutura original,
sem copiar fotografias das referências), JUR-09 (foco, teclado, responsividade). Os
limites de distribuição e do piloto local descritos acima continuam válidos.


Validação final de interface: em390px e320px o dialog não apresentou overflow
horizontal e os seis controles ficaram visíveis na base. End na aba Chat levou a
Notas, com foco preservado. Nomes dos participantes têm contraste branco no palco.
A revisão confirmou as correções de falha de dispositivo e retorno ao automático,
sem P1/P2 remanescente nesses pontos.18 testes documentais também passaram.


## Sala como página — revisão0.27

A chamada agora ocupa uma página do aplicativo em #meeting/ID, com barra lateral e
navegação do Forma. Não usa dialog, backdrop ou bloqueio de foco. Lista de reuniões,
Reunir agora e botão Entrar na sala da prévia levam à mesma rota. Os formulários de
agendamento e prévia de dispositivos continuam separados da sala conectada.

Sair retorna a #meetings; navegar para outra página desmonta o componente LiveKit
e desconecta a chamada. Reabrir a rota conecta novamente, começando com câmera e
microfone desligados. URL direta exige sessão e acesso vigente no servidor; ID
indisponível mostra estado de erro e opção de voltar. Presença e revogação seguem
os controles anteriores. Não há chamada persistente em segundo plano nesta entrega.

Chat, arquivos, tarefas, notas, foco/grade, participantes e painel de contexto foram
preservados. Em celular, o menu do app continua acessível no topo e os controles da
chamada ficam na base. A versão local web e fontes desktop foram atualizadas; o
instalador anterior e o fluxo online separado não foram substituídos.

QA isolado: sala conectada, zero dialogs, uma região main, saída para Reuniões,
página mobile390px e rejeição de rota inexistente. Build web/desktop/API e147 testes
Node aprovados. Aplicam-se JUR-05 e JUR-09; sem novos dados ou serviços.
