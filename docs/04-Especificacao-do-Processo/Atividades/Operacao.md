---
toc_max_heading_level: 2
sidebar_position: 6
---

# Operação e Evolução

Mantém o software em operação e realimenta o backlog com o que a operação revela. A sustentação (categoria D) roda em fluxo contínuo Kanban, com limite de seis itens em progresso por squad e reserva de 20% da capacidade.

## AT22 Atender chamado de sustentação

| Campo | Conteúdo |
| --- | --- |
| Propósito | Resolver correções e ajustes de até 40 horas sem desorganizar o trabalho planejado |
| Categorias | D obrigatória |
| Gatilho | Chamado não resolvido no N1 e classificado na categoria D pela AT01 |
| Entradas | Chamado com descrição, severidade e SLA |
| Saídas | Correção em produção pelo fluxo AT13 a AT16 e AT18 a AT20; chamado encerrado com registro da causa |
| Papéis | R DEV e SUP, A SRE, C QA, I PO |
| Ferramentas | Ferramenta de chamados, quadro Kanban da categoria D no Azure Boards |
| Instrumento de apoio | [CL03 Definição de pronto](../Checklists.md#cl03-definição-de-pronto) |
| Critério de conclusão | Correção em produção, cliente informado e chamado encerrado dentro do SLA |
| Problemas atendidos | P08 |

### Passos

1. O SUP faz a triagem N1 e encerra com registro o que pode ser resolvido sem desenvolvimento
2. O SUP classifica a severidade e o SLA, e o item entra no quadro da categoria D
3. O squad puxa o item quando houver vaga no limite de seis itens. Com o limite atingido, o item aguarda na fila priorizada por severidade
4. Se a severidade exigir furar o limite, o PO decide explicitamente e o desvio fica registrado no item
5. O DEV corrige pelo fluxo normal de construção, sem dispensar revisão de código, teste automatizado e gate G3
6. Se o esforço passar de 40 horas, o item volta à AT01 para reclassificação
7. O SUP informa o cliente e encerra o chamado

## AT23 Analisar causa raiz de incidente crítico

| Campo | Conteúdo |
| --- | --- |
| Propósito | Impedir que o mesmo incidente crítico se repita |
| Categorias | Obrigatória para todo incidente de severidade crítica, em qualquer categoria produtiva |
| Gatilho | Incidente de severidade crítica resolvido |
| Entradas | Linha do tempo do incidente, logs e métricas, chamados relacionados |
| Saídas | Análise de causa raiz publicada; ações corretivas no backlog; proposta de evolução quando aplicável |
| Papéis | R DEV, A SRE, C EP, ARQ, QA, SEC e SUP, I PO e CTO |
| Ferramentas | Azure Wiki, Grafana e Azure Monitor, Azure Boards |
| Instrumento de apoio | Seção de análise de causa raiz no registro de incidente |
| Critério de conclusão | Causa raiz identificada, ações com responsável e prazo, publicada em até cinco dias úteis |
| Problemas atendidos | P05, P09 |

### Passos

1. Reconstruir a linha do tempo do incidente, da detecção à resolução
2. Aplicar a técnica dos cinco porquês até chegar a uma causa sobre a qual a equipe tenha ação
3. Separar a causa técnica da causa de processo. A causa de processo é encaminhada ao EP
4. Registrar ações corretivas como itens no backlog, com a tag P05
5. Publicar a análise sem atribuição de culpa individual
