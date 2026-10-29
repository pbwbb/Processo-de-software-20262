---
toc_max_heading_level: 2
sidebar_position: 4
---

# Construção

Iterações de duas semanas. É a fase em que as categorias A, B e C convergem, e o ponto de entrada da categoria A. A sustentação (categoria D) usa as atividades AT13 a AT16 dentro do fluxo contínuo.

A facilitação das cerimônias fica com o squad lead, que é um desenvolvedor sênior do squad e não um papel separado do processo. Ver decisão DB05.

## AT12 Planejar a iteração

| Campo | Conteúdo |
| --- | --- |
| Propósito | Selecionar os itens que o squad consegue entregar prontos na iteração |
| Categorias | A, B e C obrigatória |
| Gatilho | Início da iteração |
| Entradas | Backlog priorizado, itens preparados, capacidade do squad descontada a reserva de 20% da categoria D |
| Saídas | Iteração planejada no Boards, com meta e itens divididos em tarefas |
| Papéis | R DEV e QA, A PO, C GP e ARQ, I CTO |
| Ferramentas | Azure Boards (iteração e capacidade) |
| Instrumento de apoio | [CL02 Definição de preparado](../Checklists.md#cl02-definição-de-preparado) |
| Critério de conclusão | Meta da iteração escrita e todos os itens selecionados atendendo à definição de preparado |
| Problemas atendidos | P01, P08 |

### Passos

1. Registrar a capacidade do squad no Boards e reservar 20% para a categoria D
2. O PO apresenta a meta e os itens de maior prioridade
3. Selecionar apenas itens que passam no CL02. Item que não passa volta para refinamento
4. Dividir cada item em tarefas, incluindo explicitamente a tarefa de teste automatizado
5. Registrar a meta da iteração e publicar no Boards

## AT13 Implementar

| Campo | Conteúdo |
| --- | --- |
| Propósito | Produzir o código que atende ao critério de aceite, com teste e rastreabilidade |
| Categorias | A, B, C e D obrigatória |
| Gatilho | Tarefa movida para Em andamento |
| Entradas | Item preparado (A03), A06 quando houver, requisitos de segurança aplicáveis |
| Saídas | Código em branch do item, testes automatizados, pull request aberto |
| Papéis | R e A DEV, C PO e ARQ |
| Ferramentas | Azure Repos, Azure Pipelines |
| Instrumento de apoio | [CL03 Definição de pronto](../Checklists.md#cl03-definição-de-pronto) |
| Critério de conclusão | Pull request aberto com pipeline verde e vínculo ao work item |
| Problemas atendidos | P02, P04 |

### Passos

1. Criar branch a partir da principal com o padrão `item/<id>-<descricao-curta>`
2. Implementar o caminho principal e os casos de erro previstos nos critérios de aceite
3. Escrever os testes automatizados junto do código, e não depois
4. Fazer commits com mensagem que cite o ID do work item, o que cria o vínculo automático no Boards
5. Abrir pull request vinculado ao work item e aguardar o pipeline de integração contínua

## AT14 Revisar código do par

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que nenhuma mudança chegue à branch principal sem um segundo olhar |
| Categorias | A, B, C e D obrigatória, E recomendada |
| Gatilho | Pull request aberto com pipeline verde |
| Entradas | Pull request, critérios de aceite do item |
| Saídas | Pull request aprovado ou devolvido com comentários |
| Papéis | R e A DEV revisor, C ARQ e SEC |
| Ferramentas | Azure Repos, com política de branch que exige um aprovador e pipeline verde |
| Instrumento de apoio | [CL08 Revisão de código](../Checklists.md#cl08-revisão-de-código) |
| Critério de conclusão | Pull request aprovado por ao menos um par diferente do autor, sem comentário bloqueante em aberto |
| Problemas atendidos | P04, P09 |

### Passos

1. O autor indica o revisor, preferindo quem conhece menos o módulo, o que distribui o conhecimento
2. O revisor percorre o CL08 e registra os comentários no pull request
3. Mudanças que alteram integração, modelo de dados ou autenticação exigem também o ARQ ou o SEC como revisor
4. O autor responde aos comentários e o revisor aprova
5. O revisor faz o merge, que dispara a implantação automática em homologação

## AT15 Automatizar e executar testes

| Campo | Conteúdo |
| --- | --- |
| Propósito | Verificar o incremento continuamente durante a iteração |
| Categorias | A, B, C e D obrigatória |
| Gatilho | Merge na branch principal e implantação em homologação |
| Entradas | A09, suítes do Test Plans, incremento em homologação |
| Saídas | A10 Evidência de teste automatizado; defeitos registrados no Boards |
| Papéis | R DEV, A QA, C PO |
| Ferramentas | Azure Pipelines (execução e relatório), Azure Test Plans (casos manuais exploratórios) |
| Instrumento de apoio | [Template A10](../Templates.md#a10-evidência-de-teste-automatizado) |
| Critério de conclusão | Testes do item executados em homologação, resultado publicado no pipeline e caso de teste vinculado na matriz A05 |
| Problemas atendidos | P04, P07 |

### Passos

1. O pipeline executa os testes unitários e de integração a cada merge
2. O QA executa os testes de aceitação do item em homologação no mesmo dia do merge
3. O QA conduz teste exploratório nos itens de maior risco
4. Defeitos encontrados viram work items vinculados ao item de origem
5. O resultado é publicado como A10 e o caso de teste é vinculado na matriz de rastreabilidade

## AT16 Verificar segurança do incremento

| Campo | Conteúdo |
| --- | --- |
| Propósito | Encontrar vulnerabilidades durante a construção, quando a correção é barata |
| Categorias | A, B, C e D obrigatória, no nível ASVS da categoria |
| Gatilho | Cada execução do pipeline, e verificação manual a cada iteração na categoria C |
| Entradas | Incremento, A07, A08 na categoria C |
| Saídas | Relatório da análise estática e de dependências no pipeline; achados registrados no Boards |
| Papéis | R DEV, A SEC, C ARQ, QA e DPO, I CTO |
| Ferramentas | SonarQube, Trivy ou OWASP Dependency-Check, Azure Pipelines |
| Instrumento de apoio | [CL09 Verificação de segurança por categoria](../Checklists.md#cl09-verificação-de-segurança-por-categoria) |
| Critério de conclusão | Nenhum achado crítico ou alto em aberto sem tratamento registrado |
| Problemas atendidos | P06 |

### Passos

1. O pipeline executa a análise estática e a análise de dependências, e falha se houver achado crítico
2. O SEC revisa os achados altos e decide entre corrigir na iteração ou aceitar com justificativa
3. Na categoria C, o SEC verifica manualmente os requisitos ASVS selecionados na AT08
4. Achados viram work items com a tag P06 e prazo pela severidade, de até 15 dias para crítico
5. O SEC atualiza o A07 quando um achado revelar risco não previsto

## AT17 Revisar a iteração e retrospectivar

| Campo | Conteúdo |
| --- | --- |
| Propósito | Validar o incremento com o PO e melhorar a forma de trabalho do squad |
| Categorias | A, B e C obrigatória, D mensal |
| Gatilho | Fim da iteração |
| Entradas | Itens prontos em homologação, indicadores da iteração, ações da retrospectiva anterior |
| Saídas | Itens aceitos ou devolvidos; A17 Retrospectiva com ação de melhoria |
| Papéis | R DEV e QA, A PO, C SRE, I EP |
| Ferramentas | Azure Boards, Azure Wiki |
| Instrumento de apoio | [Template A17](../Templates.md#a17-retrospectiva) |
| Critério de conclusão | Itens com aceite registrado e ao menos uma ação de melhoria com responsável e prazo |
| Problemas atendidos | P01, P10 |

### Passos

1. Demonstrar os itens prontos em homologação para o PO e, quando fizer sentido, para o cliente
2. O PO aceita ou devolve cada item, registrando no Boards
3. Na retrospectiva, verificar primeiro se a ação da iteração anterior foi concluída
4. Levantar o que funcionou e o que atrapalhou, com exemplos concretos
5. Escolher uma ação de melhoria, com responsável e prazo, e registrar no A17
6. Ações que dependem de mudança no processo são encaminhadas ao EP para a revisão trimestral

## AT18 Conduzir o gate G3

| Campo | Conteúdo |
| --- | --- |
| Propósito | Impedir que qualquer release vá para produção sem critério objetivo de prontidão |
| Categorias | A, B, C e D obrigatória |
| Gatilho | Release candidata em homologação |
| Entradas | A12, A10, relatório de segurança do pipeline, lista de defeitos em aberto |
| Saídas | Aprovação registrada no estágio de produção do Azure Pipelines |
| Papéis | R e A SRE, C PO, GP, ARQ, QA e SEC, I SUP e CTO |
| Ferramentas | Azure Pipelines (aprovação manual no ambiente de produção) |
| Instrumento de apoio | [CL06 Checklist do gate G3](../Checklists.md#cl06-gate-g3-prontidão-para-release) |
| Critério de conclusão | Todos os itens do CL06 marcados e aprovação registrada no pipeline |
| Problemas atendidos | P05 |

### Passos

1. O SRE verifica o CL06 com o QA e o SEC
2. O SRE confirma que o plano de rollback foi testado em homologação
3. O SRE aprova o estágio de produção no pipeline, o que registra autor e data automaticamente
4. Se reprovado, o motivo é registrado e a release volta à construção
