---
toc_max_heading_level: 2
sidebar_position: 3
---

# Elaboração

Obrigatória nas categorias B e C. O objetivo é detalhar o essencial, fixar a arquitetura e produzir um plano confiável. Duração típica de duas a seis semanas. A fase termina no gate G2.

## AT06 Detalhar requisitos

| Campo | Conteúdo |
| --- | --- |
| Propósito | Transformar o escopo macro em requisitos verificáveis do núcleo da solução |
| Categorias | B e C obrigatória, A recomendada para Features com regra de negócio nova |
| Gatilho | G1 aprovado |
| Entradas | A01, A02, Features no Boards |
| Saídas | A04 Especificação de requisitos; itens de backlog A03 com critérios de aceite; A05 Matriz de rastreabilidade iniciada |
| Papéis | R QA, A PO, C GP, ARQ, DEV, SEC e DPO, I CTO |
| Ferramentas | Azure Wiki (A04 e A05), Azure Boards (itens com critério de aceite) |
| Instrumento de apoio | [Template A04](../Templates.md#a04-especificação-de-requisitos), [Template A03](../Templates.md#a03-item-de-backlog), [Template A05](../Templates.md#a05-matriz-de-rastreabilidade) |
| Critério de conclusão | Requisitos do núcleo com regra de negócio e critério de aceite, cada um ligado a uma Feature na matriz de rastreabilidade |
| Problemas atendidos | P02, P04 |

### Passos

1. Identificar o núcleo, que são as Features de maior risco ou maior valor. Requisitos fora do núcleo são detalhados durante a Construção
2. Conduzir sessões de refinamento com PO e cliente, registrando regras de negócio, fluxos principais, fluxos de erro e restrições
3. Escrever os critérios de aceite no formato Dado, Quando, Então, incluindo ao menos um caso de erro por item
4. Consultar o SEC e o DPO sobre requisitos de segurança e de dado pessoal
5. Registrar cada requisito no A05 com sua origem e o work item correspondente
6. Validar o A04 com o PO e, na categoria B, com o cliente

## AT07 Definir arquitetura e registrar decisões

| Campo | Conteúdo |
| --- | --- |
| Propósito | Estabelecer a arquitetura candidata e registrar a razão de cada decisão relevante |
| Categorias | B e C obrigatória, A recomendada quando a Feature altera integração ou modelo de dados |
| Gatilho | Requisitos do núcleo identificados na AT06 |
| Entradas | A04 em elaboração, arquitetura atual do produto, A15 |
| Saídas | A06 Documento de arquitetura e registros de decisão (ADR); prova de conceito dos pontos de maior risco |
| Papéis | R DEV, A ARQ, C PO, GP, SEC, SRE e CTO |
| Ferramentas | Azure Wiki (documento), Azure Repos (ADRs junto do código em `docs/adr`) |
| Instrumento de apoio | [Template A06](../Templates.md#a06-registro-de-decisão-de-arquitetura) |
| Critério de conclusão | Visão da arquitetura publicada e uma ADR aceita para cada decisão que afete integração, dado ou segurança |
| Problemas atendidos | P09 |

### Passos

1. Descrever a arquitetura em uma visão de contexto e uma de componentes, apenas no nível necessário para o núcleo
2. Listar as decisões em aberto e priorizar as que têm maior risco técnico
3. Construir prova de conceito para cada risco técnico alto, com prazo máximo de cinco dias por prova
4. Registrar cada decisão como ADR, com alternativas consideradas e consequências aceitas
5. Revisar o documento com SRE, para requisitos de implantação e monitoramento, e com SEC, para superfície exposta

## AT08 Avaliar risco de segurança e privacidade

| Campo | Conteúdo |
| --- | --- |
| Propósito | Identificar o dado tratado, os riscos e os controles antes de o código existir |
| Categorias | B e C obrigatória, A e D recomendada |
| Gatilho | Arquitetura candidata disponível |
| Entradas | A04, A06, inventário de dados do produto |
| Saídas | A07 Avaliação de risco de segurança e privacidade; A08 Relatório de ameaças na categoria C; requisitos de segurança incorporados ao backlog |
| Papéis | R SEC, A DPO, C PO, GP, ARQ e SRE, I CTO |
| Ferramentas | Azure Wiki (página de acesso restrito), Miro ou quadro equivalente (sessão de modelagem de ameaças), Azure Boards |
| Instrumento de apoio | [Template A07](../Templates.md#a07-avaliação-de-risco-de-segurança-e-privacidade), [Template A08](../Templates.md#a08-relatório-de-ameaças-e-contramedidas), [CL09 Verificação de segurança por categoria](../Checklists.md#cl09-verificação-de-segurança-por-categoria) |
| Critério de conclusão | Todo dado pessoal classificado com base legal e todo risco alto com controle definido e responsável |
| Problemas atendidos | P06, P07 |

### Passos

1. Inventariar os dados tratados e classificar cada um, com base legal e prazo de retenção
2. Mapear a superfície exposta, com interfaces, integrações e perfis de acesso
3. Na categoria C, conduzir sessão de modelagem de ameaças pelo método STRIDE com ARQ e DEV, registrando o resultado no A08
4. Selecionar os requisitos ASVS do nível exigido pela categoria e incluí-los no backlog como itens com critério de aceite
5. Submeter o A07 ao DPO, que emite parecer sobre o tratamento de dados

O Grau A atribuía o R ao DPO e o A ao security champion, o contrário do que dizia o Catálogo de Artefatos, onde o SEC é autor do A07 e o DPO é revisor. A matriz foi alinhada ao catálogo pela decisão DB02.

## AT09 Elaborar plano de testes

| Campo | Conteúdo |
| --- | --- |
| Propósito | Definir como o incremento será verificado, para que o teste aconteça durante a iteração e não no fim |
| Categorias | B e C obrigatória, A recomendada |
| Gatilho | Requisitos do núcleo com critério de aceite |
| Entradas | A04, A03, A07 |
| Saídas | A09 Plano de testes; suítes de teste criadas no Test Plans |
| Papéis | R e A QA, C PO, GP, DEV e SEC, I CTO |
| Ferramentas | Azure Test Plans |
| Instrumento de apoio | [Template A09](../Templates.md#a09-plano-de-testes) |
| Critério de conclusão | Estratégia, níveis de teste, ambientes, massa de dados e critérios de saída definidos e aprovados pelo PO |
| Problemas atendidos | P04 |

### Passos

1. Definir os níveis de teste e a proporção esperada de automação por nível
2. Definir a massa de dados e como o dado pessoal será anonimizado nos ambientes de teste
3. Incluir os testes de segurança derivados do A07
4. Definir critérios de saída mensuráveis, como cobertura do caminho principal e ausência de defeito crítico
5. Criar as suítes no Test Plans e vincular cada uma à Feature correspondente

## AT10 Elaborar plano de release

| Campo | Conteúdo |
| --- | --- |
| Propósito | Planejar o conteúdo, a janela e o caminho de reversão de cada release |
| Categorias | A, B, C e D obrigatória |
| Gatilho | Nas categorias B e C, durante a Elaboração para os marcos e a cada release para o detalhe. Nas categorias A e D, a cada release |
| Entradas | Backlog priorizado, A06, A09 |
| Saídas | A12 Plano de release e de rollback |
| Papéis | R SRE, A PO, C GP, ARQ e QA, I SUP |
| Ferramentas | Azure Wiki, Azure Pipelines (ambientes e aprovações) |
| Instrumento de apoio | [Template A12](../Templates.md#a12-plano-de-release-e-de-rollback) |
| Critério de conclusão | Conteúdo, janela, sequência e plano de rollback definidos, com gatilho de reversão explícito |
| Problemas atendidos | P03, P05 |

### Passos

1. Na Elaboração das categorias B e C, definir os marcos de release e a estimativa refinada, que alimentam o G2
2. Para cada release, listar os itens com seus work items
3. Definir janela e comunicação com o Suporte e, na categoria B, com o cliente
4. Escrever a sequência de implantação e as verificações pós-implantação
5. Escrever o plano de rollback com gatilho de acionamento, passos e tempo máximo de reversão, e testá-lo em homologação

## AT11 Conduzir o gate G2

| Campo | Conteúdo |
| --- | --- |
| Propósito | Confirmar que a arquitetura e o plano são sólidos o bastante para iniciar a Construção |
| Categorias | B e C obrigatória |
| Gatilho | AT06 a AT10 concluídas |
| Entradas | A04, A05, A06, A07, A08 na categoria C, A09, A12, A15 atualizado |
| Saídas | Decisão de G2 registrada no Épico; linha de base do escopo |
| Papéis | R ARQ, A CTO, C PO, GP, EP e SEC |
| Ferramentas | Azure Boards, Azure Wiki |
| Instrumento de apoio | [CL05 Checklist do gate G2](../Checklists.md#cl05-gate-g2-baseline-de-arquitetura) |
| Critério de conclusão | Todos os itens do CL05 marcados e decisão do CTO registrada |
| Problemas atendidos | P03, P09 |

### Passos

1. O ARQ verifica o CL05 e agenda a reunião de gate
2. O ARQ apresenta arquitetura, decisões e riscos técnicos, e o GP apresenta o plano de release com a estimativa refinada
3. O SEC confirma que a avaliação de risco foi concluída e que os riscos altos têm controle
4. O CTO decide e o ARQ registra a decisão no Épico
5. O GP congela a versão aprovada do escopo como linha de base. A partir daí, toda mudança passa pela [AT24](./Transversais.md#at24-avaliar-solicitação-de-mudança)
