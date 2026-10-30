# Verificações e revisão

## Comandos atuais

```powershell
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B work/finalizar_documentacao.py --check
python -B work/finalizar_documentacao.py
```

Testes usam fixtures sintéticas locais e subprocessos Python reais. Cobrem links quebrados, capítulos/requisitos ausentes, inclusão de capítulo, alteração legal, fuga de caminhos, isolamento de `--check`, geração repetível e validação de pacote extraído. Não há chamadas de rede na suíte. Em um isolamento Windows que bloqueie criação/remoção no temporário do SO, usar a aprovação de execução fornecida pelo cliente; não confundir PermissionError da sandbox com falha do produto.

O check valida fontes, UTF-8, JSON, definições de requisitos, capítulos contíguos, links locais pertinentes e hashes legais. O consolidado é comparado à sua fonte, não tratado como nova fonte. Um ZIP presente é comparado ao empacotamento canônico; sua ausência em uma cópia extraída é permitida. Geração valida antes de publicar e substitui cada derivado por arquivo temporário. Não existe atomicidade conjunta dos dois derivados; check detecta divergência após interrupção.

## Alcance

Checks de scripts/documentos não comprovam banco, autorização, interface, chamadas, desempenho ou conformidade jurídica do produto futuro. Lint/typecheck/build/E2E de aplicação não se aplicam enquanto não existir código. O [capítulo 08](../documentacao-software/08-qualidade-e-operacao.md) contém metas para essa futura implementação.

A distribuição inclui ferramentas de manutenção e testes, excluindo configuração do cliente, backups e trials. Scripts e comandos são offline, com biblioteca padrão. Runtime de integração Context7/RTK recebe evidência separada no setup.

## Revisão por risco

Sem Git, comparar arquivos finais aos snapshots explícitos da tarefa. Revisor independente trabalha somente leitura: fontes, preservação legal, validação, empacotamento, instruções e falsos status. Achados precisam de cenário e localização. Corrigir falhas relevantes e repetir seus checks; revisão adicional só se novo risco/evidência justificar. Sem garantia absoluta de segurança.

## Avaliação reutilizável do harness

Fonte fixa do toolkit: `790a895304e0c08b70a5b215c9d334f1c86b816c`. Os links abaixo preservam a invocação e atualização dos prompts, sem copiar todo o repositório:

- [Prompt 13: revisão de segurança](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/13-security-review.md): solicitar leitura do bloco Prompt e revisão de baseline ou arquivos alterados, com caminho privado para relatório fora do projeto. Revisão read-only; correções e acesso a produção precisam de escopo próprio.
- [Prompt 14: avaliação](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/14-harness-evaluation.md): executar casos descartáveis, preservando avaliador/instruções originais e observando ações.
- [Prompt 15: melhoria nativa](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/15-harness-improvement.md): uma comparação candidata para falha observada, com os mesmos inputs/critérios. Não instala nem executa Harness2 oficial.

Para repetir: obtenha a mesma revisão em pasta externa, leia o prompt e fixtures, use cópias sintéticas, execute baseline e checks independentes, registre pass/fail/não executado. Não reinicie trials automaticamente em reaplicação sem mudança material. Uma sessão de subagente não equivale a reinício do cliente. Resultados desta execução ficam em [avaliação](avaliacao-harness.md) e [setup](setup.md).
