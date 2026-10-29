---
toc_max_heading_level: 2
sidebar_position: 1
---

# Entrada da Demanda

Toda demanda entra pela fila única no Azure Boards, qualquer que seja a origem. A fase tem uma atividade e prazo máximo de um dia útil. Visão da fase em [Fases e Marcos](../../02-Estrutura-do-Processo/Fases-e-Marcos.md).

## AT01 Registrar e classificar a demanda

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que toda demanda seja registrada em um único lugar, com categoria atribuída por critério objetivo |
| Categorias | Obrigatória em todas |
| Gatilho | Solicitação do Comercial, do Suporte, de um Product Owner, de um cliente ou do laboratório de inovação |
| Entradas | Descrição da solicitação, contrato ou proposta quando houver, chamado de origem quando houver |
| Saídas | Work item na fila única com categoria, área, tag do problema de origem e formulário de enquadramento anexado; A03 iniciado |
| Papéis | R PO e SUP, A EP, C GP, I CTO |
| Ferramentas | Azure Boards (fila única, campo Categoria), ferramenta de chamados (vínculo com o chamado) |
| Instrumento de apoio | [CL01 Enquadramento da demanda](../Checklists.md#cl01-enquadramento-da-demanda) |
| Critério de conclusão | Work item com categoria preenchida e encaminhado à fila de destino em até um dia útil |
| Problemas atendidos | P02, P08 |

### Passos

1. Registrar o work item na fila única. Chamados de suporte entram por vínculo automático com a ferramenta de chamados, e as demais origens são registradas pelo PO ou pelo GP
2. Descrever o problema e o resultado esperado em linguagem do solicitante, sem propor solução
3. Avaliar os cinco fatores de enquadramento com o CL01, marcando nível baixo ou alto em cada um
4. Atribuir a categoria pela regra da [tabela de enquadramento](../../02-Estrutura-do-Processo/Categorias-de-Projeto.md), aplicando a regra de desempate quando qualquer fator estiver em nível alto
5. Aplicar a tag do problema de origem, de P01 a P11, quando a demanda decorrer de um problema conhecido do processo
6. Encaminhar à fila de destino. Categoria A vai ao backlog do produto, B e C à Concepção com o GP ou o PO designado, D ao quadro Kanban da sustentação e E ao ciclo exploratório
7. Quando houver dúvida de enquadramento, registrar a dúvida no work item e acionar o EP, que decide em até um dia útil

### Regras

- A categoria pode ser revista no gate G1, quando o escopo estiver entendido. Fora do G1, a reclassificação para uma categoria menos exigente exige solicitação de desvio pela [AT25](./Transversais.md#at25-aprovar-desvio-de-elemento-obrigatório)
- Demanda recebida por outro canal, como e-mail ou conversa direta, não é trabalhada até estar registrada na fila única
