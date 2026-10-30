# Setup e evidências

**Execução:** 22/10/2026 · **Estado:** setup documental executado; descoberta nativa do Context7 e hook RTK permanecem sem observação funcional no aplicativo.

## Fontes e baseline

Toolkit: revisão `790a895304e0c08b70a5b215c9d334f1c86b816c`, obtida em checkout externo ao projeto. Plano e desenho aprovados pelo usuário. Escopo: base documental; sem aplicação, banco, CI ou Git.

Baseline preservada em work/toolkit-setup: 34 arquivos copiados e comparados por SHA-256; manifesto legal original corresponde a 13 snapshots. Antes das alterações, revisão independente constatou 36 links válidos e 31 entradas válidas no ZIP v0.3.

Runtime observado: Python 3.12.10, Node 24.14.0, npm 11.9.0, Git 2.53.0.windows.2, RTK 0.48.0 e CLI Codex 0.162.1. CLI não determina versão do app. Nenhuma credencial foi lida ou gravada para este setup; autenticação/modelo principal e permissões foram preservados.

## Contexto e documentação

Os nove destinos estão no [mapa](document-map.json); fontes de produto permanecem nos capítulos. AGENTS é índice local, LEIS encaminha o recorte legal, README contém comandos. Memória global do usuário não foi alterada. Progresso temporário não faz parte do conhecimento permanente nem da distribuição.

Detalhes do uso estão em [onboarding](onboarding.md), critérios em [quality](quality.md) e decisões por ferramenta na [matriz](02-matriz-de-cobertura.md). As 23 entradas receberam decisão; nenhuma skill adicional foi instalada porque as disponíveis cobrem as tarefas atuais. Não há promessa de validação de ferramentas sem plataforma-alvo.

## Evidências de ferramentas

| Camada | Resultado observado |
|---|---|
| RTK instalado | Binário existente 0.48.0 reutilizado; sem atualização global |
| RTK local | dry-run e init executados; RTK.md lido e regra conciliada para não prefixar duas vezes nem invalidar PowerShell |
| RTK execução | `rtk git status` e `rtk proxy git status` saíram 0 no checkout externo limpo |
| Hook RTK | Referência preexistente preservada; reescrita de comandos pelo cliente não observada. Não afirmar ganho medido |
| Context7 arquivo | `.codex/config.toml` local contém uma seção pública; sintaxe validada com tomllib. Excluído do ZIP, com exemplo de recuperação no onboarding |
| Context7 serviço | initialize, tools/list, resolve-library-id e query-docs responderam por MCP HTTP público. ID retornado `/python/cpython`; resposta de 6.309 caracteres sobre pathlib, com fonte cpython. Sem token ou dado privado |
| Context7 cliente | Ferramentas não descobertas na sessão atual. Consulta direta ao serviço não comprova carregamento no app |
| Outros clientes/skills | CLAUDE é ponte documental; Claude não foi instalado/testado. Vercel/Supabase/artifacts já disponíveis, sem duplicação ou alteração de conta |

**Intervenção pendente:** reabrir uma sessão confiável neste projeto e confirmar descoberta de resolve-library-id/query-docs; repetir a consulta por esses tools nativos. Nenhuma mudança de confiança ou permissão foi feita por automação. Para RTK, observar uma chamada suportada na próxima sessão e evitar prefixo duplicado quando o hook estiver comprovadamente ativo.

## Verificação e distribuição

- Suíte final: **17 testes**, incluindo dependência obrigatória ausente, ZIP com metadados estáveis entre plataformas, caminho relocado, check sem escrita, requisitos/capítulos, links, hashes e escape de manifesto.
- Wrapper original preservado como entrada portátil; CLI de fontes e geração usa biblioteca padrão. `--check` funciona de outro diretório.
- ZIP v0.4 extraído em caminho com espaços/acentos: check, suíte incluída e CRC válidos; inventário antes/depois do check idêntico. Geração repetida com os mesmos inputs produz os mesmos bytes. Hash final da distribuição é registrado no checkpoint local, fora do ZIP para evitar autorreferência.
- Os 13 snapshots legais, seu inventário e manifesto permanecem iguais à baseline. Não foi executado o registrador para alterar hashes; não houve nova decisão jurídica nesta manutenção.
- ZIP v0.3 preservado. A distribuição v0.4 contém fontes, instruções, mapa, gerador e testes; exclui configuração do cliente, backups, caches, trials e relatórios privados.

## Avaliação e revisão

[Avaliação nativa](avaliacao-harness.md): dois casos independentes reproduziram 5/7 e passaram a 7/7; caso read-only preservou fixture. Baseline de manutenção rejeitada antes do runtime por raiz absoluta; candidato isolado passou. Pausa/retomada e reinício real não executados.

Revisor independente examinou código, instruções, pacote e baseline somente por leitura. Dois achados importantes foram reproduzidos por testes vermelhos: omissão silenciosa de arquivos necessários e metadado ZIP dependente do SO. Ambos corrigidos; os 17 testes ficaram verdes. Nenhum achado crítico ou outro importante confirmado ficou aberto.

O revisor considerou, sem confirmar fuga efetiva, symlinks de destinos; contenção de caminhos nos inputs e substituição do link final permaneceram verificadas por leitura, sem alegação de auditoria exaustiva. Atomicidade conjunta dos derivados e ausência do próprio ZIP em pacote extraído foram aceitas como limites já documentados. Mudanças de produto, implementação de banco/UI e revisão jurídica atualizada ficaram fora desta tarefa aprovada.

Reaplicação em cópia descartável: duas execuções de `rtk init --codex` preservaram nota personalizada; a segunda reconheceu a referência existente. Nenhuma skill/hook foi reinstalada. Configuração Context7 tem uma única seção. Não se generaliza esse teste para autenticação ou reinício do cliente.

## Fonte oficial de configuração

A configuração MCP de projeto depende de confiança no cliente, conforme [configuração oficial do Codex](https://learn.chatgpt.com/docs/config-file/config-basic) e [MCP](https://learn.chatgpt.com/docs/extend/mcp). O endpoint é documentado pelo [Context7 para Codex](https://context7.com/docs/clients/codex). Nenhuma alteração de confiança, configuração global ou permissões foi inferida desses exemplos.
