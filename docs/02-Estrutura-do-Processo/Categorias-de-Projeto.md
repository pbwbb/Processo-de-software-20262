---
sidebar_position: 6
---

# Categorias de Projeto

A categoria é atribuída na entrada da demanda e registrada como campo obrigatório do work item. Ela decide quantas fases a demanda percorre e quais artefatos são exigidos.

## As cinco categorias

| Categoria | O que abrange | Exemplo no portfólio | Fases percorridas |
| --- | --- | --- | --- |
| A, Evolução de produto SaaS | Novas funcionalidades e melhorias do Vértice Care | Agenda com confirmação automática por mensagem | Construção, Transição e Operação |
| B, Projeto contratado | Implantação, integração e customização para um cliente nomeado | Integração do Autoriza com o sistema de uma operadora | Todas, da Concepção à Operação |
| C, Módulo crítico ou regulatório | Módulo que trate dado de saúde, decisão financeira ou exigência da ANS | Nova versão do faturamento TISS | Todas, com atividades reforçadas |
| D, Sustentação | Correção, ajuste de parametrização e evolução até 40 horas | Correção de cálculo de coparticipação | Operação, em fluxo contínuo |
| E, Inovação | Prova de conceito e experimento técnico | Classificação automática de glosas por aprendizado de máquina | Ciclo exploratório próprio |

## Critérios objetivos de enquadramento

Cinco fatores são avaliados na entrada. Qualquer fator em nível alto puxa a demanda para a categoria mais exigente entre as compatíveis.

| Fator | Nível baixo | Nível alto |
| --- | --- | --- |
| Sensibilidade do dado | Dado operacional ou cadastral | Dado de saúde, dado financeiro ou dado pessoal sensível |
| Obrigação contratual | Escopo definido internamente | Escopo, prazo ou preço acordados em contrato |
| Exigência regulatória | Nenhuma norma aplicável | ANS, TISS, LGPD ou norma de prontuário aplicável |
| Esforço estimado | Até 40 horas | Acima de 6 pessoas-mês |
| Reversibilidade | Mudança revertida por rollback simples | Migração de dados ou indisponibilidade de serviço |

### Regra de desempate

Uma demanda que seria categoria A, mas trata dado de saúde ou responde a exigência da ANS, passa a ser categoria C. Uma demanda que seria categoria D, mas exige mais de 40 horas, sobe para A, B ou C conforme os demais fatores. Essa regra impede que a classificação seja usada para fugir da formalidade exigida.

## Política de cada categoria

### Categoria A

Cadência quinzenal, planejamento por iteração, sem gates G1 e G2. O gate G3 continua obrigatório, porque o risco de uma implantação ruim atinge 310 clientes de uma vez.

### Categoria B

Percorre todas as fases. O gate G1 precede qualquer proposta comercial com prazo, e o controle de mudanças é obrigatório desde a assinatura. É a categoria com maior volume de artefatos, justificada pelo risco contratual registrado em P03 e P11.

### Categoria C

Mesmo fluxo da categoria B, acrescido de modelagem de ameaças, teste de intrusão antes do go-live, nível ASVS 2 como mínimo e parecer do encarregado de dados. A diferença vem do tipo de dado tratado e da exposição regulatória, descrita em P06 e P07.

### Categoria D

Fluxo contínuo em Kanban, sem fases de concepção e elaboração. Três regras a governam.

1. Limite de seis itens em progresso por squad
2. Reserva de 20% da capacidade do squad, acordada com o Product Owner no início de cada iteração
3. Prioridade por severidade e SLA, com estouro de limite exigindo decisão explícita do Product Owner

A reserva de capacidade responde diretamente a P08, porque hoje os 35% consumidos pela sustentação não são negociados nem visíveis.

### Categoria E

Ciclo exploratório com prazo máximo de quatro semanas e critério de sucesso definido antes do início. Um único artefato obrigatório, o A18 Registro de experimento, que reúne a hipótese no início e o aprendizado no fim. Um experimento aprovado não vira produto por continuidade, e sim entra na fila única para ser classificado como A, B ou C.

## Distribuição esperada

| Categoria | Volume anual estimado | Participação na capacidade |
| --- | --- | --- |
| A | 26 releases quinzenais | 35% |
| B | 20 projetos | 25% |
| C | 6 a 8 módulos | 15% |
| D | 4800 chamados | 20% |
| E | 3 a 4 iniciativas | 5% |
