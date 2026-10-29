---
sidebar_position: 2
---

# Rastreabilidade Grau A e B

O Grau B não redefine o processo. Ele detalha o que foi decidido no Grau A. Esta página mostra, nos dois sentidos, como cada elemento da proposta consolidada virou especificação, e onde a especificação precisou corrigir a proposta.

## Da proposta à especificação

| Elemento do Grau A | Onde foi definido | Como foi especificado no Grau B | Situação |
| --- | --- | --- | --- |
| Cinco fases e fase de entrada | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | Uma página de atividades por fase | Especificado |
| Quatro gates com critérios | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | Atividades AT05, AT11, AT18 e AT21 e checklists CL04 a CL07 | Especificado |
| Seis fluxos modelados | [Modelagem das Atividades](../02-Estrutura-do-Processo/Modelagem-das-Atividades.md) | Cada caixa dos fluxos virou atividade com ID, conforme a tabela abaixo | Especificado |
| 25 atividades da RACI | [Matriz RACI](../02-Estrutura-do-Processo/Matriz-RACI.md) | 28 atividades com 10 campos e passos | Especificado, com 3 atividades novas (DB04) |
| Onze papéis | [Matriz RACI](../02-Estrutura-do-Processo/Matriz-RACI.md) | [Papéis](./Papeis.md) com responsabilidade, autoridade e competências | Especificado, com correções (DB01, DB02, DB03, DB05) |
| Dezessete artefatos | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) | Campo Saídas de cada atividade | Especificado, com 1 artefato novo (DB06) |
| Dez templates | [Templates do Grau A](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/Templates.md) | [Templates](./Templates.md), 18 modelos com cabeçalho comum | Especificado |
| Cinco categorias e fatores de enquadramento | [Categorias de Projeto](../02-Estrutura-do-Processo/Categorias-de-Projeto.md) | AT01, CL01 e [Como usar o processo](./Guia-de-Uso.md) | Especificado |
| Matriz de customização | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) | Campo Categorias de cada atividade e CL09 | Especificado |
| Procedimento de desvio | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) | AT25 e CL10 | Especificado |
| Definição de preparado e de pronto | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | CL02 e CL03 | Especificado |
| Controle de mudanças | [Modelagem das Atividades](../02-Estrutura-do-Processo/Modelagem-das-Atividades.md) | AT24 e template A16 | Especificado |
| Mapa de ferramentas | [Mapa de Ferramentas](../03-Consolidacao/Mapa-de-Ferramentas.md) | Campo Ferramentas de cada atividade | Especificado |
| Sete indicadores | [Indicadores e Medição](../03-Consolidacao/Indicadores-e-Medicao.md) | AT26 | Parcial, consultas e plano de medição na Sprint 5 |
| Melhoria contínua e revisão trimestral | [Plano de Implantação](../03-Consolidacao/Plano-de-Implantacao.md) | AT27 | Parcial, governança e versionamento do processo na Sprint 5 |
| Disciplina de gestão de configuração | [Ciclo de Vida e Justificativa](../02-Estrutura-do-Processo/Ciclo-de-Vida-e-Justificativa.md) | Convenção de branch na AT13 e política de branch na AT14 | Parcial, política completa na Sprint 5 |
| Disciplina de garantia de qualidade | [Ciclo de Vida e Justificativa](../02-Estrutura-do-Processo/Ciclo-de-Vida-e-Justificativa.md) | AT09, AT14, AT15 e CL03 | Parcial, auditoria de aderência ao processo na Sprint 5 |

## Dos fluxos às atividades

| Fluxo do Grau A | Atividades |
| --- | --- |
| Entrada e classificação da demanda | AT01 |
| Fases planejadas, categorias B e C | AT02 a AT11, AT19 a AT21 |
| Iteração de construção | AT12 a AT18 |
| Sustentação, categoria D | AT22, AT23, com AT13 a AT16 na correção |
| Controle de mudanças | AT24 |
| Ciclo exploratório, categoria E | AT28 |

## Dos problemas às atividades

Cada atividade declara os problemas que atende. A tabela é a leitura inversa, e confirma que os onze problemas do diagnóstico têm atividade concreta que os trata, e não apenas decisão escrita.

| Problema | Atividades que o tratam |
| --- | --- |
| P01 Ausência de processo definido | AT12, AT17, AT25, AT27, AT28 |
| P02 Requisitos sem rastreabilidade | AT01, AT02, AT06, AT13 |
| P03 Estimativa e prazo não confiáveis | AT02, AT03, AT04, AT05, AT10, AT11, AT19, AT21 |
| P04 Qualidade concentrada no fim | AT06, AT09, AT13, AT14, AT15 |
| P05 Implantação manual e arriscada | AT10, AT18, AT20, AT23 |
| P06 Segurança no fim do ciclo | AT08, AT16 |
| P07 Conformidade reativa | AT08, AT15, AT19, AT21 |
| P08 Sustentação interrompe o desenvolvimento | AT01, AT12, AT22 |
| P09 Conhecimento concentrado | AT07, AT11, AT14, AT21, AT23 |
| P10 Ausência de métricas | AT17, AT26, AT27 |
| P11 Mudança de escopo sem controle | AT03, AT05, AT24 |

## Correções feitas na proposta

Detalhar a proposta funcionou como teste de consistência. Seis pontos do Grau A não se sustentavam quando se tentava escrever quem faz o quê, e foram corrigidos. As justificativas estão no registro de decisões em [Evolução e Roadmap](./Evolucao-e-Roadmap.md).

| Inconsistência encontrada | Decisão |
| --- | --- |
| G1 e G2 tinham dois papéis com A, contrariando a regra da própria RACI | DB01 |
| A07 tinha autor SEC no catálogo e executor DPO na RACI | DB02 |
| "Analista de negócio" e "equipe de implantação" executavam atividades sem existir como papel | DB03 |
| Plano de release, revisão da iteração e experimento existiam nas fases, mas sem linha na RACI | DB04 |
| O squad lead facilitava cerimônias sem estar definido | DB05 |
| A categoria E citava dois artefatos que não existiam no catálogo | DB06 |
