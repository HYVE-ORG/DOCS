# Plataforma de trabalho colaborativo

Preparação comercial: Essencial R$79/mês e Pro R$149/mês por Studio, com propostas
empresariais privadas. Implementação e bloqueios de lançamento estão no
[guia de assinaturas](outputs/software-mvp/docs/billing.md). Cobranças reais desativadas.

Revisão atual de estrutura e prioridades: [relatório técnico](outputs/software-mvp/docs/structure-review.md). O ZIP documental inclui os guias referenciados, mas não o código completo da aplicação, bases, caches ou instaladores.

Desktop Windows: instalador com download direto na landing e alternativa portátil implementados. Leia [operação e limites](outputs/documentacao-software/14-aplicativo-desktop.md) e o [guia técnico](outputs/software-mvp/docs/desktop.md). O perfil é separado do localhost e não há sincronização entre dispositivos nesta etapa.

Evolução de produto: [gestão integrada do Forma](outputs/documentacao-software/13-gestao-integrada-e-expansao.md),
com CRM, horas, custos, HRM, ATS e operações por etapas. O primeiro incremento
de Clientes/Comercial já está no MVP; seu guia está em `outputs/software-mvp/docs/crm.md`.
Horas, custos e demais módulos continuam planejados.

Este projeto contém a documentação do produto e um MVP local Forma em `outputs/software-mvp`, com React, NestJS, Electron e armazenamento JSON. A prévia online usa Supabase para contas e trabalho por Studio com RLS e Storage privado; testes reais de usuário, mídia remota e publicação ainda estão pendentes. Veja o [guia online](outputs/software-mvp/docs/central-work.md). Os comandos abaixo mantêm o pacote documental; no MVP use `npm run dev`, `npm test` e `npm run build`.

Comece pelo [índice do produto](outputs/documentacao-software/README.md). Consulte o [onboarding](outputs/toolkit-setup/onboarding.md) para preparar o ambiente documental, [qualidade](outputs/toolkit-setup/quality.md) para os checks e [setup](outputs/toolkit-setup/setup.md) para evidências e limites das integrações.

## Comandos

Python 3.11 ou superior; nenhuma dependência Python externa.

```powershell
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B work/finalizar_documentacao.py --check
python -B work/finalizar_documentacao.py
```

`--check` não escreve arquivos. Sem a flag, o script valida as fontes e gera o consolidado e o ZIP da versão editorial. Artefatos presentes desatualizados fazem a checagem falhar; a geração permite atualizá-los a partir de fontes válidas. Um ZIP extraído não precisa conter uma cópia de si próprio para ser validado.

Da pasta original ou de um pacote extraído, os comandos usam a raiz do script, sem caminho fixo desta máquina. Esses comandos se referem ao ambiente documental; a aplicação local tem comandos próprios em `outputs/software-mvp/package.json`.

As referências legais ficam em [LEIS.md](LEIS.md). Fontes e capítulos são editáveis; consolidado e ZIP são derivados. Backups locais e configurações do cliente não acompanham o pacote.
