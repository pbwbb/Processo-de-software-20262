# Atividades

O Grau A definiu as atividades como linhas da [Matriz RACI](../../02-Estrutura-do-Processo/Matriz-RACI.md) e caixas dos [fluxos modelados](../../02-Estrutura-do-Processo/Modelagem-das-Atividades.md). Esta seção as transforma em instruções de trabalho. Cada atividade tem um identificador estável, no formato AT01 a AT28, que é usado nos checklists, nos templates e nos work items do Boards.

## Estrutura de uma atividade

Toda atividade é especificada com os mesmos campos, para que quem a executa encontre a informação sempre no mesmo lugar.

| Campo | O que informa |
| --- | --- |
| Propósito | Por que a atividade existe, em uma frase |
| Categorias | Em quais categorias é obrigatória (O), recomendada (R) ou dispensada, conforme a [Matriz de Customização](../../02-Estrutura-do-Processo/Matriz-de-Customizacao.md) |
| Gatilho | O evento que inicia a atividade |
| Entradas | Artefatos e informações consumidos |
| Saídas | Artefatos produzidos ou atualizados, com o ID do [catálogo](../../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md) |
| Papéis | R executa, A responde, C é consultado, I é informado |
| Ferramentas | Onde o trabalho é feito e registrado |
| Instrumento de apoio | Template ou checklist que guia a execução |
| Critério de conclusão | Condição verificável que encerra a atividade |
| Problemas atendidos | Problemas do diagnóstico que justificam a atividade |

Os passos vêm numerados logo abaixo da tabela, na ordem em que devem ser executados.

## Catálogo de atividades

| ID | Atividade | Fase | Responde (A) | Categorias obrigatórias |
| --- | --- | --- | --- | --- |
| AT01 | [Registrar e classificar a demanda](./Entrada-da-Demanda.md#at01-registrar-e-classificar-a-demanda) | Entrada | EP | Todas |
| AT02 | [Levantar necessidade e stakeholders](./Concepcao.md#at02-levantar-necessidade-e-stakeholders) | Concepção | GP | B, C |
| AT03 | [Definir escopo macro](./Concepcao.md#at03-definir-escopo-macro) | Concepção | GP | B, C |
| AT04 | [Estimar ordem de grandeza](./Concepcao.md#at04-estimar-ordem-de-grandeza) | Concepção | GP | B, C |
| AT05 | [Conduzir o gate G1](./Concepcao.md#at05-conduzir-o-gate-g1) | Concepção | CTO | B, C |
| AT06 | [Detalhar requisitos](./Elaboracao.md#at06-detalhar-requisitos) | Elaboração | PO | B, C |
| AT07 | [Definir arquitetura e registrar decisões](./Elaboracao.md#at07-definir-arquitetura-e-registrar-decisões) | Elaboração | ARQ | B, C |
| AT08 | [Avaliar risco de segurança e privacidade](./Elaboracao.md#at08-avaliar-risco-de-segurança-e-privacidade) | Elaboração | DPO | B, C |
| AT09 | [Elaborar plano de testes](./Elaboracao.md#at09-elaborar-plano-de-testes) | Elaboração | QA | B, C |
| AT10 | [Elaborar plano de release](./Elaboracao.md#at10-elaborar-plano-de-release) | Elaboração | PO | A, B, C, D |
| AT11 | [Conduzir o gate G2](./Elaboracao.md#at11-conduzir-o-gate-g2) | Elaboração | CTO | B, C |
| AT12 | [Planejar a iteração](./Construcao.md#at12-planejar-a-iteração) | Construção | PO | A, B, C |
| AT13 | [Implementar](./Construcao.md#at13-implementar) | Construção | DEV | A, B, C, D |
| AT14 | [Revisar código do par](./Construcao.md#at14-revisar-código-do-par) | Construção | DEV | A, B, C, D |
| AT15 | [Automatizar e executar testes](./Construcao.md#at15-automatizar-e-executar-testes) | Construção | QA | A, B, C, D |
| AT16 | [Verificar segurança do incremento](./Construcao.md#at16-verificar-segurança-do-incremento) | Construção | SEC | A, B, C, D |
| AT17 | [Revisar a iteração e retrospectivar](./Construcao.md#at17-revisar-a-iteração-e-retrospectivar) | Construção | PO | A, B, C |
| AT18 | [Conduzir o gate G3](./Construcao.md#at18-conduzir-o-gate-g3) | Construção | SRE | A, B, C, D |
| AT19 | [Homologar com o cliente](./Transicao.md#at19-homologar-com-o-cliente) | Transição | GP | B, C |
| AT20 | [Migrar dados e implantar](./Transicao.md#at20-migrar-dados-e-implantar) | Transição | SRE | A, B, C, D |
| AT21 | [Conduzir o gate G4](./Transicao.md#at21-conduzir-o-gate-g4) | Transição | GP | B, C |
| AT22 | [Atender chamado de sustentação](./Operacao.md#at22-atender-chamado-de-sustentação) | Operação | SRE | D |
| AT23 | [Analisar causa raiz de incidente crítico](./Operacao.md#at23-analisar-causa-raiz-de-incidente-crítico) | Operação | SRE | Todas as produtivas |
| AT24 | [Avaliar solicitação de mudança](./Transversais.md#at24-avaliar-solicitação-de-mudança) | Transversal | GP | B, C |
| AT25 | [Aprovar desvio de elemento obrigatório](./Transversais.md#at25-aprovar-desvio-de-elemento-obrigatório) | Transversal | CTO | Quando houver desvio |
| AT26 | [Coletar e revisar indicadores](./Transversais.md#at26-coletar-e-revisar-indicadores) | Transversal | EP | Organizacional |
| AT27 | [Revisar e evoluir o processo](./Transversais.md#at27-revisar-e-evoluir-o-processo) | Transversal | EP | Organizacional |
| AT28 | [Conduzir experimento](./Transversais.md#at28-conduzir-experimento) | Ciclo exploratório | ARQ | E |

As atividades AT10, AT17 e AT28 não existiam como linha da Matriz RACI no Grau A, embora aparecessem nas fases e nos fluxos. A inclusão está registrada na decisão DB04 em [Evolução e Roadmap](../Evolucao-e-Roadmap.md).

## Siglas dos papéis

PO Product Owner, GP gerente de projeto, EP engenheiro de processo, ARQ arquiteto de software, DEV desenvolvedor, QA analista de qualidade, SEC security champion, SRE engenheiro de confiabilidade, SUP analista de suporte, DPO encarregado de dados. A especificação completa de cada um está em [Papéis](../Papeis.md).
