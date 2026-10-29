---
sidebar_position: 4
---

# Matriz RACI

Legenda. **R** executa, **A** responde pelo resultado, **C** é consultado, **I** é informado. Cada atividade tem exatamente um A. Quando a linha não tem R, quem responde também executa.

:::note Revisão do Grau B
A matriz foi corrigida na versão 0.4: um único A nos gates G1 e G2 (decisão DB01), executor e responsável da avaliação de risco alinhados ao catálogo (DB02) e três atividades incluídas (DB04). Cada atividade está especificada em [Atividades](../04-Especificacao-do-Processo/Atividades/index.md), e a justificativa das correções em [Evolução e Roadmap](../04-Especificacao-do-Processo/Evolucao-e-Roadmap.md).
:::

## Papéis do processo

| Papel | Propósito | Alocação na Vértice |
| --- | --- | --- |
| Product Owner (PO) | Prioriza o backlog e aceita o incremento | Quatro pessoas, uma por produto e frente |
| Gerente de projeto (GP) | Responde por escopo, prazo e controle de mudanças | Dois no PMO, atuando nos contratos |
| Engenheiro de processo (EP) | Mantém o processo, instrui desvios e conduz a medição | Papel novo, uma pessoa dedicada |
| Arquiteto de software (ARQ) | Define a arquitetura e registra as decisões | Formalização dos dois seniores que já atuam assim |
| Desenvolvedor (DEV) | Implementa, revisa código do par e automatiza teste | 40 pessoas nos squads |
| Analista de qualidade (QA) | Define critérios de aceite e o plano de testes | Cinco pessoas, realocadas para dentro dos squads |
| Security champion (SEC) | Conduz modelagem de ameaças e verificação de segurança | Um por squad, apoiado pelo núcleo de segurança |
| Engenheiro de confiabilidade (SRE) | Opera pipeline, implantação e monitoramento | Quatro pessoas |
| Analista de suporte (SUP) | Triagem, classificação e registro do chamado | Nove pessoas |
| Encarregado de dados (DPO) | Avalia impacto à privacidade e aprova o tratamento | Papel acumulado pelo núcleo de segurança |
| CTO | Aprova gates estruturais e desvios do processo | Um |

## Matriz por atividade

| Atividade | PO | GP | EP | ARQ | DEV | QA | SEC | SRE | SUP | DPO | CTO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Registrar e classificar a demanda | R | C | A | | | | | | R | | I |
| Levantar necessidade e stakeholders | C | A | | C | | | | | C | | I |
| Definir escopo macro | C | A | | C | | | C | | | | I |
| Estimar ordem de grandeza | C | A | | C | R | C | | | | | I |
| Aprovar G1 | C | R | C | C | | | | | | | A |
| Detalhar requisitos | A | C | | C | C | R | C | | | C | I |
| Definir arquitetura e registrar decisões | C | C | | A | R | | C | C | | | C |
| Avaliar risco de segurança e privacidade | C | C | | C | | | R | C | | A | I |
| Elaborar plano de testes | C | C | | | C | A | C | | | | I |
| Elaborar plano de release | A | C | | C | | C | | R | I | | |
| Aprovar G2 | C | C | C | R | | | C | | | | A |
| Planejar a iteração | A | C | | C | R | R | | | | | I |
| Implementar | C | | | C | A | | | | | | |
| Revisar código do par | | | | C | A | | C | | | | |
| Automatizar e executar testes | C | | | | R | A | | | | | |
| Verificar segurança do incremento | | | | C | R | C | A | | | C | I |
| Revisar a iteração e retrospectivar | A | | I | | R | R | | C | | | |
| Aprovar G3 | C | C | | C | | C | C | A | I | | I |
| Homologar com o cliente | C | A | | | C | R | | | I | | I |
| Migrar dados e implantar | I | C | | C | C | | C | A | I | C | I |
| Aprovar G4 | C | A | | | | | | C | I | | I |
| Atender chamado de sustentação | I | | | | R | C | | A | R | | |
| Analisar causa raiz de incidente crítico | I | | C | C | R | C | C | A | C | | I |
| Avaliar solicitação de mudança | C | A | C | C | C | | | | | | I |
| Aprovar desvio de artefato obrigatório | C | C | R | C | | | C | | | C | A |
| Conduzir experimento da categoria E | C | | | A | R | | | | | | I |
| Coletar e revisar indicadores | C | C | A | C | I | I | I | C | I | | C |
| Revisar e evoluir o processo | C | C | A | C | C | C | C | C | C | C | C |

## Mudanças de responsabilidade em relação ao estado atual

| Mudança | Razão |
| --- | --- |
| Criação do papel de engenheiro de processo | Não existe hoje quem responda pelo processo, o que é a raiz de P01 e P10 |
| Formalização do papel de arquiteto | Duas pessoas já exercem a função sem registro, o que alimenta P09 |
| Realocação do QA para dentro dos squads | O QA centralizado é o gargalo da última semana de iteração, descrito em P04 |
| Criação do security champion por squad | O núcleo de dois não consegue acompanhar seis squads, o que empurra segurança para o fim do ciclo em P06 |
| Atribuição do aceite de G3 ao SRE | Hoje ninguém aprova formalmente a ida à produção, o que explica os rollbacks de P05 |
