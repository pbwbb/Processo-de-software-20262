---
sidebar_position: 2
---

# Análise de Aderência

Verificação de que cada problema do diagnóstico recebeu tratamento, e de que nenhuma decisão de processo foi tomada sem origem identificada.

## Cobertura dos problemas

| Problema | Decisão que o atende | Onde está | Evidência esperada após a adoção |
| --- | --- | --- | --- |
| P01 Ausência de processo definido | Processo único com cinco fases e matriz de customização | [Ciclo de Vida e Justificativa](../02-Estrutura-do-Processo/Ciclo-de-Vida-e-Justificativa.md) | Todos os squads com o mesmo fluxo no Boards e desvios registrados |
| P02 Requisitos sem rastreabilidade | Matriz de rastreabilidade obrigatória e vínculo de work item a commit e a teste | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) | Queda na proporção de chamados classificados como comportamento não especificado |
| P03 Estimativa e prazo não confiáveis | Gates G1 e G2 anteriores ao compromisso comercial | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | Nenhuma proposta com prazo emitida sem G1 aprovado |
| P04 Qualidade concentrada no fim | Definição de pronto com critério de aceite e teste automatizado, QA dentro do squad | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | Distribuição do volume de teste ao longo da iteração |
| P05 Implantação manual e arriscada | Gate G3 com plano de rollback testado e pipeline automatizado | [Fases e Marcos](../02-Estrutura-do-Processo/Fases-e-Marcos.md) | Nenhuma implantação sem G3 aprovado e tempo de reversão registrado |
| P06 Segurança no fim do ciclo | Avaliação de risco na Elaboração, security champion por squad, ASVS por categoria | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) | Redução do tempo entre achado e correção |
| P07 Conformidade reativa | Artefatos de conformidade produzidos nas atividades e armazenados na Wiki | [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) | Evidência de auditoria reunida em até dois dias úteis |
| P08 Sustentação interrompe o desenvolvimento | Categoria D em Kanban, limite de seis itens e reserva de 20% da capacidade | [Categorias de Projeto](../02-Estrutura-do-Processo/Categorias-de-Projeto.md) | Interrupções não planejadas dentro da reserva acordada |
| P09 Conhecimento concentrado | Documento de arquitetura e registros de decisão obrigatórios, revisão de código em todas as categorias | [Matriz de Customização](../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) | Mais de duas pessoas aptas a atuar em cada módulo crítico |
| P10 Ausência de métricas | Sete indicadores com fonte no Azure DevOps e revisão trimestral | [Indicadores e Medição](./Indicadores-e-Medicao.md) | Painel publicado e revisão trimestral realizada |
| P11 Mudança de escopo sem controle | Procedimento de controle de mudanças obrigatório nas categorias B e C | [Modelagem das Atividades](../02-Estrutura-do-Processo/Modelagem-das-Atividades.md) | Toda alteração de escopo com análise de impacto registrada |

Onze problemas, onze decisões. Nenhum problema ficou sem tratamento.

## Origem das decisões

Verificação na direção inversa, para garantir que o processo não traz elementos sem justificativa no contexto.

| Elemento do processo | Problema de origem | Situação |
| --- | --- | --- |
| Cinco fases e quatro gates | P01, P03, P05 | Justificado |
| Fila única com classificação na entrada | P02, P08 | Justificado |
| Cinco categorias de projeto | P01, P08 | Justificado |
| Matriz de customização e procedimento de desvio | P01 | Justificado |
| Definição de pronto e de preparado | P02, P04 | Justificado |
| Papel de engenheiro de processo | P01, P10 | Justificado |
| Papel de arquiteto formalizado | P09 | Justificado |
| Security champion por squad | P06 | Justificado |
| Reserva de capacidade para sustentação | P08 | Justificado |
| Sete indicadores e revisão trimestral | P10 | Justificado |
| Procedimento de controle de mudanças | P11 | Justificado |
| Registros de decisão de arquitetura | P09 | Justificado |

## Lacunas identificadas

Duas situações não são resolvidas pelo processo e foram convertidas em risco, registrado em [Riscos da Adoção](./Riscos-da-Adocao.md).

| Lacuna | Por que o processo não resolve | Tratamento |
| --- | --- | --- |
| Suporte responde ao Diretor Comercial, fora da estrutura de tecnologia | Trata-se de decisão organizacional, fora do alcance de uma definição de processo | Mitigado pela reserva de capacidade negociada, com recomendação de revisão da estrutura |
| Doze instalações dedicadas do Autoriza impedem entrega totalmente automatizada | Depende de negociação de janela com cada operadora | Implantação assistida mantida, com automação progressiva por cliente |
