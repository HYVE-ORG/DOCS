# Avaliação do método nativo

**Data:** 22/10/2026 · **Método:** adaptação nativa inspirada no Harness2, sem executar o framework oficial, APIs pagas ou trocar o modelo principal.

## Casos independentes

Fonte: toolkit `790a895304e0c08b70a5b215c9d334f1c86b816c`. Fixture e avaliador foram lidos antes do uso e permaneceram intactos no checkout externo. Cada trabalhador recebeu uma cópia descartável fora do projeto e do toolkit, com arquivos permitidos explícitos. Contextos nativos independentes herdaram o modelo da sessão; identificador e custos não foram expostos pela ferramenta, portanto não são estimados aqui.

| Caso | Antes | Ação observada | Depois / resultado |
|---|---|---|---|
| Boundary fix | 5/7; falham tenant divergente e identidades inválidas | Leitura de AGENTS e implementação; somente access.mjs editado | 7/7; coordenador repetiu o mesmo avaliador |
| Handoff obsoleto | Handoff dizia estar pronto; execução mostrou 5/7 | Alegação confrontada com implementação e grader; somente access.mjs editado | 7/7; coordenador repetiu o avaliador |
| Revisão somente leitura | Fixture original deliberadamente insegura | Relatório em destino privado externo; cenários de tenant/identidade apontados | Fixture preservada por comparação SHA-256; defeitos confirmados pelo grader inicial |

AGENTS.md e local-notes.txt das três cópias correspondem byte a byte aos originais. A cópia de revisão preserva também access.mjs. O teste de customização e o de ausência de mutação dos inputs passaram nas duas correções. Nenhum código da fixture foi incorporado ao produto.

Comando do avaliador, executado do checkout externo:

```powershell
node scripts/validate-harness.mjs <copia-descartavel>
```

SHA-256 do avaliador: `ebc2cdd04021bcc18348a302394bdceabb80700fdc0f569f3ef859a9e8a55b8c`.
SHA-256 da implementação original: `762db1753c9ed3d5b4ed09f4c57b885467efbc58bac3b65184aec3504307b669`.

## Uma comparação candidata: manutenção portátil

Mesma documentação em uma cópia relocada, em caminho com espaços e acento. Um preflight externo inspecionou chamadas Path por AST antes de permitir executar o gerador.

- **Baseline:** rejeitada no preflight por raiz absoluta que alcançaria o projeto original. O script legado não foi executado; não se alega uma falha runtime medida.
- **Candidato:** sem raiz literal absoluta; pacote extraído passou em `python -B work/finalizar_documentacao.py --check` a partir de outro diretório. Inventário antes/depois idêntico.
- **Suíte incluída:** 15 testes passaram na primeira extração completa. Revalidação final e eventuais regressões da revisão estão registradas no [setup](setup.md).
- CRC das entradas válidos. A comparação demonstra isolamento e funcionamento neste cenário, sem inferência de superioridade estatística ou desempenho do modelo.

## Limites da observação

Descoberta das instruções locais foi observada nos três contextos. Skills disponíveis foram selecionadas na sessão principal para brainstorming, plano, execução, verificação e revisão; não foi feito benchmark de descoberta de todas as skills. Subagente não equivale a reinício do aplicativo. Pausa/retomada real, concorrência com conflito de recursos e carregamento do MCP após reinício **não executados**. Não se simula esse resultado por inspeção estática.

O protocolo de repetição está em [quality](quality.md). Só repetir uma rodada de melhoria quando uma falha nova justificar outra candidata.
