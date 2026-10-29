---
sidebar_position: 2
---

# Fases e Marcos

## Fase 0, Entrada da demanda

| Campo | Conteúdo |
| --- | --- |
| Propósito | Receber, classificar e encaminhar toda demanda por uma fila única |
| Entrada | Solicitação do Comercial, do Suporte, do Product Owner ou de um cliente |
| Atividades | Registrar o work item, aplicar os cinco fatores de enquadramento, atribuir a categoria, definir a fila de destino |
| Saída | Work item com categoria atribuída e área definida |
| Responsável | Engenheiro de processo para as regras, Product Owner ou analista de suporte para a execução |
| Prazo máximo | Um dia útil |

A fila única é a resposta direta a P02 e P08. Hoje a demanda entra por três portas que não se comunicam, e nenhuma classificação é feita.

## Fase 1, Concepção

| Campo | Conteúdo |
| --- | --- |
| Propósito | Entender o problema, delimitar o escopo macro e avaliar viabilidade antes de qualquer compromisso |
| Entrada | Work item classificado nas categorias B ou C |
| Atividades | Levantar necessidade do cliente, identificar stakeholders, definir escopo macro, levantar riscos iniciais, estimar ordem de grandeza, avaliar viabilidade técnica e comercial |
| Artefatos produzidos | Documento de visão, registro de riscos inicial, estimativa de ordem de grandeza |
| Papéis | Gerente de projeto executa e responde, ou o Product Owner em módulo de produto; arquiteto e segurança são consultados |
| Duração típica | Uma a três semanas |

### Gate G1, Aprovação de concepção

| Critério de entrada | Critério de saída |
| --- | --- |
| Documento de visão publicado | Escopo macro aceito pelo cliente ou pelo Product Owner |
| Estimativa de ordem de grandeza registrada | Riscos de alta severidade com resposta definida |
| Riscos iniciais identificados | Categoria confirmada após o entendimento do escopo |
| | Aprovação registrada pelo gerente de projeto e pelo CTO |

Sem G1 aprovado, nenhuma proposta comercial com prazo pode ser emitida. Essa regra é a resposta a P03.

## Fase 2, Elaboração

| Campo | Conteúdo |
| --- | --- |
| Propósito | Detalhar o essencial, fixar a arquitetura e produzir um plano confiável |
| Entrada | G1 aprovado |
| Atividades | Detalhar requisitos do núcleo, definir arquitetura candidata, construir prova de conceito dos pontos de maior risco, elaborar plano de release, avaliar risco de segurança e privacidade, definir plano de testes |
| Artefatos produzidos | Especificação de requisitos, documento de arquitetura e registros de decisão, plano de release, avaliação de risco de segurança e privacidade, plano de testes, matriz de rastreabilidade inicial |
| Papéis | Arquiteto executa, Product Owner ou gerente de projeto responde, security champion e encarregado de dados são consultados |
| Duração típica | Duas a seis semanas |

### Gate G2, Baseline de arquitetura

| Critério de entrada | Critério de saída |
| --- | --- |
| Especificação de requisitos do núcleo publicada | Arquitetura aprovada pelo arquiteto e pelo CTO |
| Documento de arquitetura com decisões registradas | Riscos técnicos de maior severidade mitigados ou aceitos formalmente |
| Avaliação de risco de segurança concluída | Plano de release com marcos e estimativa refinada |
| | Matriz de rastreabilidade com os requisitos do núcleo ligados ao escopo |

## Fase 3, Construção

| Campo | Conteúdo |
| --- | --- |
| Propósito | Produzir incrementos funcionais, testados e integrados |
| Entrada | G2 aprovado nas categorias B e C, ou item preparado no backlog na categoria A |
| Atividades | Planejar a iteração, refinar requisitos, implementar, revisar código por par, automatizar teste, integrar continuamente, verificar segurança, revisar e retrospectivar a iteração |
| Artefatos produzidos | Incremento, evidência de teste automatizado, resultado da revisão de código, registro de retrospectiva |
| Papéis | Desenvolvedores e analista de qualidade executam, Product Owner responde, arquiteto é consultado |
| Cadência | Iterações de duas semanas |

### Definição de preparado

Um item entra na iteração quando atende às quatro condições abaixo.

1. Tem descrição do problema e do resultado esperado
2. Tem critérios de aceite escritos e verificáveis
3. Tem categoria atribuída e tag do problema de origem
4. Tem dependências externas identificadas

### Definição de pronto

Um item sai da iteração quando atende às seis condições abaixo. Esta é a resposta direta a P04.

1. Atende a todos os critérios de aceite
2. Tem teste automatizado cobrindo o caminho principal e os casos de erro previstos
3. Passou por revisão de código de ao menos um par
4. Passou na verificação estática e na análise de dependências vulneráveis
5. Está vinculado ao requisito de origem na matriz de rastreabilidade
6. Está implantado no ambiente de homologação

### Gate G3, Prontidão para release

| Critério de entrada | Critério de saída |
| --- | --- |
| Todos os itens do escopo do release atendem à definição de pronto | Plano de release aprovado |
| Plano de rollback escrito e testado | Nenhum defeito de severidade crítica em aberto |
| Verificação de segurança do nível da categoria concluída | Janela e comunicação acordadas com as partes afetadas |
| | Aprovação registrada pelo engenheiro de confiabilidade |

## Fase 4, Transição

| Campo | Conteúdo |
| --- | --- |
| Propósito | Levar o incremento ao ambiente do cliente com reversibilidade e aceite formal |
| Entrada | G3 aprovado |
| Atividades | Homologar com o cliente, migrar dados, treinar usuários, implantar de forma assistida, monitorar o período de estabilização |
| Artefatos produzidos | Plano de implantação e migração, registro de homologação, material de treinamento, termo de aceite |
| Papéis | Engenheiro de confiabilidade executa com apoio de desenvolvedores do squad responsável, gerente de projeto responde, suporte é informado |
| Duração típica | Uma a quatro semanas nas categorias B e C, horas na categoria A |

### Gate G4, Aceite

| Critério de entrada | Critério de saída |
| --- | --- |
| Implantação concluída e monitorada por cinco dias úteis | Termo de aceite assinado nas categorias B e C |
| Registro de homologação aprovado pelo cliente | Documentação de operação entregue ao suporte |
| Indicadores de estabilização dentro do esperado | Lições aprendidas registradas |

## Fase 5, Operação e evolução

| Campo | Conteúdo |
| --- | --- |
| Propósito | Manter o software em operação e realimentar o backlog com o que a operação revela |
| Entrada | G4 aprovado, ou chamado classificado na categoria D |
| Atividades | Atender chamado em fluxo contínuo, gerir incidentes e problemas, monitorar disponibilidade e desempenho, propor evolução a partir do que a operação mostra |
| Artefatos produzidos | Registro de incidente, análise de causa raiz, proposta de evolução |
| Papéis | Analista de suporte e desenvolvedores executam, engenheiro de confiabilidade responde, Product Owner é informado |
| Política | Limite de trabalho em progresso por squad e reserva de 20% da capacidade para a categoria D |

## Resumo dos gates

| Gate | Entre as fases | Quem aprova | O que impede se reprovado |
| --- | --- | --- | --- |
| G1 | Concepção e Elaboração | CTO, com recomendação do gerente de projeto | Emissão de proposta comercial com prazo |
| G2 | Elaboração e Construção | CTO, com recomendação do arquiteto | Início da construção |
| G3 | Construção e Transição | Engenheiro de confiabilidade | Qualquer implantação em produção |
| G4 | Transição e Operação | Gerente de projeto, com assinatura do cliente | Encerramento do projeto e faturamento final |
