---
sidebar_position: 1
---

# Termo de Abertura

## Objetivo

Propor um Processo Organizacional de Desenvolvimento de Software para a Vértice Sistemas, partindo do diagnóstico do contexto da empresa e definindo ciclo de vida, fases, atividades, papéis, responsabilidades, artefatos, ferramentas, categorias de projeto e mecanismos de customização.

## Escopo incluído

- Diagnóstico do contexto organizacional, incluindo portfólio, estrutura de equipes, stakeholders e práticas atuais
- Identificação e numeração dos problemas e das oportunidades de melhoria
- Definição do processo proposto e das suas fases, atividades, papéis e artefatos
- Definição das categorias de projeto e da matriz de customização
- Justificativa de cada decisão de processo em função do contexto
- Plano de implantação, indicadores e plano de melhoria contínua

## Escopo excluído

- Implementação real do processo na organização
- Desenvolvimento de software, automação de pipeline ou configuração de ferramentas em ambiente produtivo
- Avaliação oficial de maturidade segundo MPS.BR ou CMMI
- Estimativa de custo de adoção em valores monetários

## Organização objeto

Vértice Sistemas Ltda., empresa fictícia construída para o trabalho. A caracterização completa está em [Caracterização da Organização](../01-Contexto-e-Diagnostico/Caracterizacao-da-Organizacao.md).

A escolha por uma organização fictícia foi deliberada. O portfólio precisava reunir produto SaaS de cadência alta, projeto contratado de escopo fechado, módulo sob exigência regulatória e sustentação de alto volume, porque sem essa variedade a exigência de categorias de projeto e mecanismos de customização ficaria artificial.

## Equipe e papéis

Ver [Papéis da Equipe](./Papeis-da-Equipe.md).

## Cadência de trabalho

| Cerimônia | Frequência | Saída registrada |
| --- | --- | --- |
| Planejamento da Sprint | Início de cada Sprint | Itens movidos para a iteração no Boards |
| Sincronização da equipe | Duas vezes por semana | Atualização de estado dos work items |
| Revisão da Sprint | Fim de cada Sprint | Entregáveis publicados na Wiki e marcados como Done |
| Retrospectiva | Fim de cada Sprint | Página em [Retrospectivas](./Retrospectivas.md) |

## Definição de pronto dos artefatos

Um artefato só é considerado pronto quando atende às cinco condições abaixo.

1. Está publicado como página da Wiki, no caminho previsto na estrutura
2. Tem autor identificado e data da última revisão no rodapé
3. Foi revisado por ao menos um integrante que não o escreveu
4. Está vinculado ao work item que o originou, pelo campo de descrição
5. Quando contém decisão de processo, aponta explicitamente o problema que a motivou

## Critérios de aceite do trabalho

- Todo problema registrado na Sprint 1 tem necessidade, objetivo e decisão de processo correspondentes
- Toda decisão de processo tem justificativa ligada a uma característica da organização
- As cinco categorias de projeto têm critério objetivo de enquadramento
- A matriz de customização não contém célula sem marcação
- A documentação está organizada em uma única árvore navegável

## Riscos do trabalho

| Risco | Probabilidade | Impacto | Resposta |
| --- | --- | --- | --- |
| Divergência entre o enunciado detalhado das Sprints e o plano adotado | Média | Alto | Validar o plano com o professor na primeira semana e ajustar a Wiki |
| Organização fictícia detalhada demais para o prazo | Média | Médio | Congelar a caracterização ao fim da Sprint 1 e tratar alterações como mudança |
| Incoerência entre entregas de Sprints diferentes | Alta | Alto | Revisão de coerência como item obrigatório da Sprint 3 |
| Concentração do trabalho em poucos integrantes | Média | Médio | Atribuir responsável por página no Boards e revisar na sincronização |
