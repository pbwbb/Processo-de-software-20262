---
sidebar_position: 7
---

# Matriz de Rastreabilidade

Cadeia completa do diagnóstico até a decisão de processo. A coluna de decisão foi preenchida na Sprint 2 e o fechamento está em [Análise de Aderência](../03-Consolidacao/Analise-de-Aderencia.md).

| Problema | Necessidade | Objetivo do processo | Decisão de processo | Onde está definida |
| --- | --- | --- | --- | --- |
| P01 | Padrão organizacional único com variação controlada | Definir um processo comum e os pontos onde ele pode ser customizado | Processo Vértice de Desenvolvimento com cinco fases e matriz de customização por categoria | [Ciclo de Vida e Justificativa](../02-Estrutura-do-Processo/Ciclo-de-Vida-e-Justificativa.md) |
| P02 | Ligar origem da demanda, requisito, código e teste | Tornar a rastreabilidade um artefato obrigatório | Matriz de rastreabilidade obrigatória nas categorias A, B e C, com vínculo de work item a commit e a caso de teste | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) |
| P03 | Escopo e estimativa antes do compromisso comercial | Criar marco de aprovação anterior à proposta contratual | Fases de Concepção e Elaboração com gates G1 e G2 obrigatórios nas categorias B e C | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) |
| P04 | Teste distribuído ao longo da iteração | Adotar critérios de aceite e automação como parte do pronto | Definição de pronto com critério de aceite por item e teste automatizado obrigatório | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) |
| P05 | Implantação repetível e reversível | Instituir pipeline automatizado e critério de prontidão | Gate G3 de prontidão para release com plano de rollback obrigatório em todas as categorias produtivas | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) |
| P06 | Segurança distribuída nas fases | Incorporar atividades de segurança desde a concepção | Avaliação de risco na Elaboração e modelagem de ameaças obrigatória na categoria C | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) |
| P07 | Evidência produzida durante o ciclo | Gerar artefatos de conformidade como saída natural das atividades | Artefatos de conformidade vinculados a atividades das fases, armazenados na Wiki e no Test Plans | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) |
| P08 | Separar fluxo contínuo de fluxo planejado | Definir fluxo próprio para sustentação | Categoria D em fluxo Kanban, com limite de trabalho em progresso e reserva de 20% da capacidade do squad | [Categorias de Projeto](../02-Estrutura-do-Processo/Categorias-de-Projeto.md) |
| P09 | Documentação mínima e revisão por pares | Tornar revisão e registro de arquitetura obrigatórios nas categorias críticas | Documento de arquitetura e registros de decisão obrigatórios nas categorias B e C, revisão de código obrigatória em todas | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) |
| P10 | Base quantitativa para melhoria | Definir indicadores do processo e ciclo de revisão | Sete indicadores com fonte no Azure DevOps e revisão trimestral conduzida pelo engenheiro de processo | [Indicadores e Medição](../03-Consolidacao/Indicadores-e-Medicao.md) |
| P11 | Controle formal de mudança no contrato | Criar procedimento de solicitação e aprovação de mudança | Procedimento de controle de mudanças obrigatório nas categorias B e C, com aprovação do gerente de projeto e do cliente | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) |

## Como manter esta matriz

Toda nova decisão de processo acrescenta uma linha aqui antes de ser publicada na sua página de destino. Toda User Story do Boards carrega a tag do problema que a origina, o que permite reconstruir a cadeia a partir da ferramenta sem depender desta página.
