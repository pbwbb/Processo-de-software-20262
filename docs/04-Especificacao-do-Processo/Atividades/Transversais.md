---
toc_max_heading_level: 2
sidebar_position: 7
---

# Atividades Transversais e Ciclo Exploratório

Atividades que não pertencem a uma fase. As três primeiras sustentam o controle de mudança e a governança do processo. A última é o ciclo próprio da categoria E.

## AT24 Avaliar solicitação de mudança

| Campo | Conteúdo |
| --- | --- |
| Propósito | Impedir que o escopo de projeto contratado mude sem análise de impacto e registro |
| Categorias | B e C obrigatória a partir do G2 |
| Gatilho | Pedido de alteração de escopo, prazo ou custo, vindo do cliente ou da equipe |
| Entradas | Linha de base do escopo, A16 preenchido pelo solicitante |
| Saídas | A16 com decisão; linha de base, backlog e A05 atualizados quando aprovado |
| Papéis | R e A GP, C PO, EP, ARQ e DEV, I CTO |
| Ferramentas | Azure Wiki (A16), Azure Boards (item de mudança vinculado ao Épico) |
| Instrumento de apoio | [Template A16](../Templates.md#a16-solicitação-de-mudança) |
| Critério de conclusão | Decisão registrada, com aditivo contratual quando o impacto passar da tolerância |
| Problemas atendidos | P11 |

### Passos

1. Registrar a solicitação no A16 antes de qualquer trabalho na mudança. Pedido verbal não é atendido
2. O ARQ e o DEV analisam o impacto em escopo, prazo, custo e risco
3. Se o impacto estiver dentro da tolerância contratual, o GP aprova
4. Se passar da tolerância, o GP submete ao cliente, e a aprovação exige aditivo contratual
5. Aprovada a mudança, o GP atualiza a linha de base, o backlog e a matriz de rastreabilidade
6. Recusada a mudança, o GP registra a recusa e mantém a linha de base

## AT25 Aprovar desvio de elemento obrigatório

| Campo | Conteúdo |
| --- | --- |
| Propósito | Permitir adaptação controlada sem que a customização vire informalidade |
| Categorias | Sempre que um elemento obrigatório da Matriz de Customização for dispensado |
| Gatilho | Solicitação de desvio registrada |
| Entradas | Elemento a dispensar, motivo, risco assumido, precedentes |
| Saídas | Decisão registrada no work item e na página do projeto; entrada no registro de desvios |
| Papéis | R EP, A CTO, C PO, GP, ARQ, SEC e DPO |
| Ferramentas | Azure Boards (item do tipo desvio vinculado ao projeto) |
| Instrumento de apoio | [CL10 Solicitação de desvio](../Checklists.md#cl10-solicitação-de-desvio) |
| Critério de conclusão | Decisão do CTO registrada em até cinco dias úteis da solicitação |
| Problemas atendidos | P01 |

### Passos

1. O solicitante preenche o CL10 com elemento, motivo e risco assumido
2. O EP instrui o pedido em até dois dias úteis, avaliando impacto e precedentes
3. O CTO aprova ou recusa em até três dias úteis
4. O EP registra a decisão no work item e na página do projeto
5. Na revisão trimestral, o EP apresenta os desvios acumulados. Elemento dispensado três vezes seguidas na mesma categoria vira candidato a mudança da matriz

## AT26 Coletar e revisar indicadores

| Campo | Conteúdo |
| --- | --- |
| Propósito | Dar base quantitativa à gestão e à melhoria do processo |
| Categorias | Organizacional |
| Gatilho | Mensal para o painel, trimestral para a revisão |
| Entradas | Consultas do Azure Boards, Pipelines e ferramenta de chamados |
| Saídas | Painel dos indicadores I01 a I07 atualizado até o quinto dia útil do mês |
| Papéis | R e A EP, C PO, GP, ARQ, SRE e CTO, I DEV, QA, SEC e SUP |
| Ferramentas | Azure DevOps Dashboards, consultas salvas do Boards |
| Instrumento de apoio | Definição dos indicadores em [Indicadores e Medição](../../03-Consolidacao/Indicadores-e-Medicao.md) |
| Critério de conclusão | Painel publicado com os sete indicadores e a tendência de doze meses |
| Problemas atendidos | P10 |

### Passos

1. Executar as consultas salvas de cada indicador, sem planilha intermediária
2. Atualizar o painel e comparar com a linha de base e a meta
3. Sinalizar indicador fora da faixa esperada por dois meses seguidos
4. Publicar o painel e avisar os squad leads e o PMO

O detalhamento das consultas de cada indicador e do plano de medição completo está previsto para a Sprint 5.

## AT27 Revisar e evoluir o processo

| Campo | Conteúdo |
| --- | --- |
| Propósito | Manter o processo vivo, ajustado por dados e não por opinião |
| Categorias | Organizacional |
| Gatilho | Trimestral, ou extraordinário por incidente crítico, achado de auditoria ou mudança regulatória |
| Entradas | Painel de indicadores, registro de desvios, ações de retrospectiva encaminhadas, análises de causa raiz |
| Saídas | Nova versão do processo publicada no portal, com registro do que mudou e por quê |
| Papéis | R e A EP, C todos os demais papéis |
| Ferramentas | Portal do processo, Azure Repos (repositório do portal) |
| Instrumento de apoio | Registro de mudanças do processo |
| Critério de conclusão | Decisões da revisão publicadas como nova versão do portal |
| Problemas atendidos | P01, P10 |

### Passos

1. O EP consolida as entradas e propõe a pauta com uma semana de antecedência
2. A reunião com CTO, squad leads e PMO decide cada proposta de mudança
3. Cada mudança aprovada é feita como pull request no repositório do portal, revisado por outro papel afetado
4. O EP publica a nova versão e registra o que mudou e por quê
5. O EP comunica a mudança aos squads

O procedimento de versionamento do processo e o fluxo de mudança no portal serão detalhados na Sprint 5, junto da gerência de configuração.

## AT28 Conduzir experimento

| Campo | Conteúdo |
| --- | --- |
| Propósito | Testar uma hipótese técnica rapidamente, sem a formalidade das categorias produtivas |
| Categorias | E obrigatória |
| Gatilho | Hipótese registrada e classificada na categoria E |
| Entradas | Hipótese, critério de sucesso |
| Saídas | A18 Registro de experimento com o resultado; proposta de produto na fila única, quando aprovado |
| Papéis | R DEV, A ARQ, C PO, I CTO |
| Ferramentas | Azure Boards, Azure Repos (repositório separado do código de produção) |
| Instrumento de apoio | [Template A18](../Templates.md#a18-registro-de-experimento) |
| Critério de conclusão | Decisão de seguir ou abandonar registrada em até quatro semanas |
| Problemas atendidos | P01 |

### Passos

1. Registrar a hipótese e o critério de sucesso no A18 antes de começar
2. Definir o prazo, que não pode passar de quatro semanas
3. Executar o experimento em repositório separado. Código de experimento não vai para produção
4. Ao fim do prazo, comparar o resultado com o critério e decidir
5. Se aprovado, registrar uma nova demanda na fila única, que passa pela AT01 e é classificada como A, B ou C
6. Se reprovado, registrar o aprendizado e encerrar
