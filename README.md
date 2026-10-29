# Portal do Processo Vértice de Desenvolvimento

Portal em [Docusaurus](https://docusaurus.io/) com o processo organizacional de desenvolvimento de software da Vértice Sistemas (disciplina Processo de Software, UNISINOS, 2026/2).

## Rodar localmente

Requer Node.js 20 ou superior.

```bash
npm install
npm start          # servidor de desenvolvimento em http://localhost:3000
npm run build      # gera o site estático em build/ (falha se houver link quebrado)
npm run serve      # serve o build localmente
```

## Estrutura

```
docs/
  index.md                       página inicial (rota /)
  00-Gestao-do-Trabalho/         termo de abertura, sprints, papéis, glossário, retrospectivas
  01-Contexto-e-Diagnostico/     diagnóstico organizacional (Sprint 1)
  02-Estrutura-do-Processo/      ciclo de vida, fases, atividades, RACI, artefatos, customização (Sprint 2)
  03-Consolidacao/               proposta consolidada, aderência, implantação, indicadores (Sprint 3)
  04-Especificacao-do-Processo/  Grau B: guia de uso, atividades, papéis, templates, checklists, roadmap
scripts/                         verificação de consistência, geração de modelos, migração da Wiki
azure-devops/                    backlog do Grau B para importar no Boards
```

- O menu lateral é gerado a partir das pastas. A ordem vem de `sidebar_position` no topo de cada página e de `_category_.json` em cada pasta.
- O prefixo numérico (`02-`) ordena as pastas e não aparece na URL: `docs/02-Estrutura-do-Processo/Matriz-RACI.md` vira `/Estrutura-do-Processo/Matriz-RACI`.
- Os diagramas usam blocos ` ```mermaid `.
- Os arquivos `.md` são lidos como Markdown puro, sem JSX, então `<placeholder>` nos templates não quebra o build. Use `.mdx` só se precisar de componentes React.
- Links entre páginas usam o caminho relativo do arquivo (`./Fases-e-Marcos.md`). O build falha se algum link estiver quebrado.

## Manutenção do processo

O portal é a fonte oficial do processo desde o Grau B. Edite as páginas em `docs/` e publique por pull request.

| Script | O que faz | Quando roda |
| --- | --- | --- |
| `scripts/verificar-consistencia.py` | Confere atividades (campos, um único A, passos), artefatos (template e atividade produtora), problemas cobertos e checklists citados | No pipeline, antes do build, e com `npm run verificar` |
| `scripts/gerar-modelos.py` | Gera `static/modelos/modelos-pvd.zip` a partir da página de Templates | Automaticamente antes de `npm run build` |
| `scripts/migrar-wiki.py` | Converteu a Wiki do Azure DevOps nas seções 00 a 03 | Uso único. Não rode de novo, porque sobrescreveria as correções do Grau B |

O arquivo `azure-devops/backlog-grau-b.csv` traz o backlog das Sprints 4 a 6 para importar no Azure Boards (Boards → Work Items → Import Work Items). Ajuste o `Iteration Path` para os nomes das iterações do projeto antes de importar.

## Publicar no GitHub Pages

O workflow `.github/workflows/deploy.yml` compila e publica o site a cada push na branch `main`. A URL e o caminho base vêm do próprio repositório, então não é preciso editar `docusaurus.config.js`.

1. Crie o repositório no GitHub e faça o push deste projeto para a branch `main`
2. Em **Settings → Pages → Build and deployment → Source**, escolha **GitHub Actions**
3. Acompanhe a execução na aba **Actions**. O site fica em `https://<usuario>.github.io/<repositorio>/`

Para congelar a Release 1.0 do processo, use o versionamento de docs do Docusaurus: `npm run docusaurus docs:version 1.0`.
