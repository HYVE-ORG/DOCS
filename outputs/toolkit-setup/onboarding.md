# Uso local e manutenção

Esta base contém especificação e ferramentas de documentação. Não existe aplicação para iniciar. A stack React/Electron/NestJS/Supabase continua sendo proposta de produto, descrita no [índice](../documentacao-software/README.md).

## Preparar

Abra a raiz do projeto ou extraia o ZIP completo em uma pasta nova. Use Python 3.11 ou superior; não há dependências externas. Leia o README da raiz e LEIS.md. No Codex, AGENTS.md é a entrada local; no Claude, CLAUDE.md importa as mesmas instruções. Não é necessário instalar ambos os clientes.

## Verificar e gerar

```powershell
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B work/finalizar_documentacao.py --check
python -B work/finalizar_documentacao.py
```

Passe o caminho completo do script para executá-lo a partir de outra pasta; a raiz padrão vem do script. `--root` permite verificar uma cópia explicitamente escolhida. `--check` valida fontes e compara artefatos presentes sem escrever; um ZIP extraído não precisa incluir seu próprio arquivo ZIP. Sem a flag, fontes válidas geram consolidado e ZIP com metadados estáveis.

Um arquivo legal alterado faz a checagem falhar. Não execute o registrador do manifesto para esconder divergência: restaure a cópia conhecida ou realize atualização autorizada com nova procedência. Snapshot íntegro não comprova vigência jurídica.

## Editar

Edite capítulos separados. A data editorial e a lista de capítulos/requisitos obrigatórios estão no manifesto documental; a versão está no índice do produto. Novos capítulos contíguos são descobertos sem mudar contagens no código. Novos requisitos e remoção intencional de capítulos exigem atualização explícita do manifesto e revisão de escopo.

Depois de editar fontes, execute testes, gere e cheque. Uma mudança em instruções, ferramentas ou setup também altera o pacote; regenere-o. A versão 0.3 foi preservada; a manutenção do toolkit passa a integrar a distribuição 0.4.

## Ferramentas do cliente

RTK usa a instalação existente. Não duplique o prefixo quando houver hook observado. Context7 tem configuração local separada, excluída do pacote: caso necessária numa cópia nova, crie `.codex/config.toml` com a configuração pública abaixo e confirme confiança do projeto no cliente.

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
```

Reabra a sessão quando o cliente exigir e confirme se resolve-library-id/query-docs aparecem. Não grave tokens no projeto. A configuração só é considerada funcional após consulta real; consulte o [relatório de setup](setup.md) para o estado observado nesta entrega. A CLI e o app podem ter descoberta diferente.

## Recuperação

Antes de mudanças relevantes, guarde cópia dos arquivos que serão alterados. Esta execução manteve backups em work/toolkit-setup/backups, fora do ZIP. Restaure somente os arquivos afetados e regenere derivados. Não há histórico Git neste projeto, nem recuperação automática de arquivos não incluídos em seus backups.
