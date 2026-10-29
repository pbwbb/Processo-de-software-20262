---
sidebar_position: 1
---

# Proposta Consolidada

Documento único da Proposta de Processo Organizacional de Desenvolvimento de Software da Vértice Sistemas. Cada seção remete à página onde o assunto está detalhado.

## 1. Resumo da proposta

A Vértice Sistemas opera hoje sem processo definido, com seis squads trabalhando de quatro formas diferentes, demanda entrando por três portas sem triagem e verificação empurrada para o fim do ciclo. O resultado aparece em números, com 14 de 20 projetos de implantação atrasados em 2025, 35% da capacidade consumida por demanda não planejada e achados críticos de segurança corrigidos em média 60 dias depois de identificados.

A proposta é o **Processo Vértice de Desenvolvimento**, um ciclo de vida iterativo e incremental com cinco fases e quatro gates de aprovação, acompanhado de cinco categorias de projeto e de uma matriz de customização que define quais elementos se aplicam a cada categoria. A estrutura macro vem do Processo Unificado, a cadência interna vem do Scrum, o fluxo da sustentação vem do Kanban e as práticas de verificação vêm de DevOps, OWASP e ITIL, com MPS.BR nível F como referência de completude.

## 2. Diagnóstico

Onze problemas numerados, agrupados em quatro causas raiz, sustentam todas as decisões. Detalhe em [Registro de Problemas e Oportunidades](../01-Contexto-e-Diagnostico/Registro-de-Problemas-e-Oportunidades.md).

| Causa raiz | Problemas | Efeito mensurado |
| --- | --- | --- |
| Falta de definição comum | P01, P10 | Nenhum indicador de processo é coletado |
| Entrada de demanda desgovernada | P02, P03, P08, P11 | Atraso médio de 41 dias e 35% da capacidade em demanda não planejada |
| Verificação empurrada para o fim | P04, P05, P06 | 70% do volume de QA na última semana e três rollbacks em 2025 |
| Conhecimento e evidência não registrados | P07, P09 | Três semanas para reunir evidências em auditoria de cliente |

Contexto completo em [Caracterização da Organização](../01-Contexto-e-Diagnostico/Caracterizacao-da-Organizacao.md), [Estrutura das Equipes](../01-Contexto-e-Diagnostico/Estrutura-das-Equipes.md), [Mapa de Stakeholders](../01-Contexto-e-Diagnostico/Mapa-de-Stakeholders.md) e [Práticas Atuais](../01-Contexto-e-Diagnostico/Praticas-Atuais.md).

## 3. Ciclo de vida

Cinco fases, que são Concepção, Elaboração, Construção, Transição e Operação, com os gates G1 a G4 entre elas, e seis disciplinas transversais. A categoria da demanda define o ponto de entrada no fluxo. Detalhe em [Ciclo de Vida e Justificativa](../02-Estrutura-do-Processo/Ciclo-de-Vida-e-Justificativa.md) e [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md).

## 4. Atividades

Seis fluxos modelam o processo, cobrindo entrada e classificação, fases planejadas, iteração de construção, sustentação, controle de mudanças e ciclo exploratório. Detalhe em [Modelagem das Atividades](../02-Estrutura-do-Processo/Modelagem-das-Atividades.md).

## 5. Papéis e responsabilidades

Onze papéis, com cinco mudanças em relação à estrutura atual, sendo a criação do engenheiro de processo, a formalização do arquiteto, a realocação do QA para dentro dos squads, a criação do security champion por squad e a atribuição do aceite de G3 ao engenheiro de confiabilidade. Detalhe em [Matriz RACI](../02-Estrutura-do-Processo/Matriz-RACI.md).

## 6. Artefatos

Dezessete artefatos na proposta consolidada, dezoito após a inclusão do A18 no Grau B, todos armazenados na Wiki ou em ferramentas do Azure DevOps. Detalhe em [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) e modelos em [Templates](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/Templates.md).

## 7. Categorias e customização

Cinco categorias, cinco fatores objetivos de enquadramento e uma matriz que marca cada artefato e cada atividade como obrigatório, recomendado ou dispensado. O desvio de um elemento obrigatório exige instrução do engenheiro de processo e aprovação do CTO. Detalhe em [Categorias de Projeto](../02-Estrutura-do-Processo/Categorias-de-Projeto.md) e [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md).

## 8. Ferramentas

O Azure DevOps sustenta o processo com Boards, Repos, Pipelines, Test Plans e Wiki, complementado por análise estática, análise de dependências e observabilidade. Detalhe em [Mapa de Ferramentas](./Mapa-de-Ferramentas.md).

## 9. Adoção e medição

Implantação em três ondas ao longo de nove meses, com sete indicadores e revisão trimestral do processo. Detalhe em [Plano de Implantação](./Plano-de-Implantacao.md) e [Indicadores e Medição](./Indicadores-e-Medicao.md).

## 10. Verificação da proposta

Os onze problemas têm decisão de processo correspondente, verificada item a item em [Análise de Aderência](./Analise-de-Aderencia.md). Os riscos da adoção estão em [Riscos da Adoção](./Riscos-da-Adocao.md).
