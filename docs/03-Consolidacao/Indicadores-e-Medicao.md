---
sidebar_position: 4
---

# Indicadores e Medição

Sete indicadores, todos com fonte em ferramenta já em uso. A escolha foi deliberadamente curta, porque a Vértice não mede nada hoje e um conjunto extenso não seria coletado.

| ID | Indicador | Fórmula | Fonte | Linha de base | Meta em 12 meses | Frequência |
| --- | --- | --- | --- | --- | --- | --- |
| I01 | Lead time de entrega | Mediana de dias entre a criação e o fechamento do work item | Azure Boards | Não medido | Estabelecer e reduzir 20% após o primeiro trimestre de coleta | Mensal |
| I02 | Aderência ao prazo contratual | Projetos categoria B entregues no prazo dividido pelo total encerrado | Azure Boards e registro contratual | 30%, sendo 6 de 20 em 2025 | 70% | Trimestral |
| I03 | Densidade de defeitos em produção | Chamados de defeito por release, por produto | Ferramenta de chamados | Não medido | Reduzir 30% em relação à linha de base do primeiro trimestre | Mensal |
| I04 | Retrabalho por requisito mal especificado | Chamados classificados como comportamento não especificado dividido pelo total | Ferramenta de chamados | 38% | Abaixo de 15% | Mensal |
| I05 | Capacidade consumida por demanda não planejada | Horas da categoria D dividido pela capacidade total do squad | Azure Boards | 35% | Até 20% | Por iteração |
| I06 | Tempo entre achado de segurança e correção | Mediana de dias entre o registro do achado e o deploy da correção | Azure Boards e relatório de segurança | 60 dias | Até 15 dias para severidade crítica | Trimestral |
| I07 | Taxa de implantação revertida | Releases com rollback dividido pelo total de releases | Azure Pipelines | Três rollbacks em 2025 | Abaixo de 1% | Trimestral |

## Ligação com o diagnóstico

| Indicador | Problema que verifica |
| --- | --- |
| I01 | P01 e P08 |
| I02 | P03 e P11 |
| I03 | P04 |
| I04 | P02 |
| I05 | P08 |
| I06 | P06 |
| I07 | P05 |

## Regras de coleta

1. Toda coleta vem de consulta no Azure DevOps ou na ferramenta de chamados, sem planilha intermediária, porque dado digitado à mão deixa de ser coletado no segundo trimestre
2. O engenheiro de processo publica o painel até o quinto dia útil de cada mês
3. Indicador sem linha de base não recebe meta numérica até completar um trimestre de coleta
4. Um indicador que não mudou o comportamento de ninguém em dois trimestres é candidato à remoção na revisão trimestral

A quarta regra existe porque medir sem consequência consome esforço e não resolve P10.

## Painel

O painel é montado no Azure DevOps Dashboards, com um widget por indicador e um gráfico de tendência de doze meses. O acesso é aberto a toda a tecnologia, e a leitura é feita na revisão trimestral do processo.
