---
sidebar_position: 7
---

# Matriz de Customização

Este é o mecanismo central de adaptação do processo. A marcação indica **O** obrigatório, **R** recomendado e **D** dispensado.

## Artefatos por categoria

| ID | Artefato | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Documento de visão | R | O | O | D | R |
| A02 | Termo de abertura e contrato de escopo | D | O | O | D | D |
| A03 | Backlog com critérios de aceite | O | O | O | O | R |
| A04 | Especificação de requisitos | D | O | O | D | D |
| A05 | Matriz de rastreabilidade | R | O | O | D | D |
| A06 | Documento de arquitetura e registros de decisão | R | O | O | D | R |
| A07 | Avaliação de risco de segurança e privacidade | R | O | O | R | D |
| A08 | Relatório de ameaças e contramedidas | D | R | O | D | D |
| A09 | Plano de testes | R | O | O | D | D |
| A10 | Evidência de teste automatizado | O | O | O | O | D |
| A11 | Teste de intrusão antes do go-live | D | R | O | D | D |
| A12 | Plano de release e de rollback | O | O | O | O | D |
| A13 | Plano de implantação e migração de dados | D | O | O | D | D |
| A14 | Termo de aceite do cliente | D | O | O | D | D |
| A15 | Registro de riscos | R | O | O | D | R |
| A16 | Procedimento de controle de mudanças | D | O | O | D | D |
| A17 | Retrospectiva e lições aprendidas | O | O | O | R | R |
| A18 | Registro de experimento | D | D | D | D | O |

## Atividades e cerimônias por categoria

| Elemento | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| Fase de Concepção | D | O | O | D | D |
| Fase de Elaboração | D | O | O | D | D |
| Gate G1 | D | O | O | D | D |
| Gate G2 | D | O | O | D | D |
| Gate G3 | O | O | O | O | D |
| Gate G4 | D | O | O | D | D |
| Planejamento de iteração | O | O | O | D | D |
| Revisão de código por par | O | O | O | O | R |
| Modelagem de ameaças | D | R | O | D | D |
| Nível ASVS mínimo | 1 | 2 | 2 | 1 | Nenhum |
| Retrospectiva | O | O | O | Mensal | R |
| Limite de trabalho em progresso | D | D | D | O | D |

## Procedimento de desvio

Dispensar um elemento marcado como obrigatório exige registro formal. Sem esse controle, a customização degenera na informalidade que o processo existe para corrigir.

| Passo | Quem | Prazo |
| --- | --- | --- |
| Registrar a solicitação de desvio, com elemento, motivo e risco assumido | Solicitante | No momento do pedido |
| Instruir o pedido, avaliando impacto no processo e precedentes | Engenheiro de processo | Dois dias úteis |
| Aprovar ou recusar | CTO | Três dias úteis |
| Registrar a decisão na página do projeto e no work item | Engenheiro de processo | No momento da decisão |
| Revisar os desvios acumulados e propor ajuste do processo | Engenheiro de processo | Revisão trimestral |

Um elemento dispensado por desvio três vezes seguidas na mesma categoria é levado à revisão trimestral como candidato a mudança permanente da matriz. Esse laço é o que impede a matriz de envelhecer.

## Rastreabilidade das decisões de customização

| Decisão | Problemas atendidos | Justificativa |
| --- | --- | --- |
| Concepção e Elaboração obrigatórias apenas em B e C | P03, P11 | O atraso nasce do compromisso assumido antes do escopo entendido, situação que só ocorre em contrato |
| Gate G3 obrigatório em A, B, C e D | P05 | Qualquer ida à produção afeta cliente, e os três rollbacks de 2025 ocorreram sem critério objetivo |
| Modelagem de ameaças obrigatória só em C | P06 | Concentra o esforço do núcleo de segurança onde o dado é sensível, em vez de diluí-lo |
| Backlog com critérios de aceite obrigatório em todas as categorias produtivas | P02, P04 | Chamados por comportamento não especificado e gargalo de QA têm a mesma origem |
| Limite de trabalho em progresso só na categoria D | P08 | O problema é a demanda não planejada, que por definição só existe na sustentação |
| Categoria E com um único artefato obrigatório, o A18 | P01 | Sem essa saída, a padronização seria rejeitada pelo laboratório de inovação |
