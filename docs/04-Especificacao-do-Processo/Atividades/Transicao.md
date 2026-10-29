---
toc_max_heading_level: 2
sidebar_position: 5
---

# Transição

Leva o incremento ao ambiente do cliente com reversibilidade e aceite formal. Nas categorias B e C dura de uma a quatro semanas. Nas categorias A e D se resume à AT20, executada em horas.

A implantação em cliente é executada pelo SRE com apoio de desenvolvedores do squad responsável, em geral do Squad Integrações. O Grau A chamava esse grupo de "equipe de implantação", que não é um papel do processo. Ver decisão DB03.

## AT19 Homologar com o cliente

| Campo | Conteúdo |
| --- | --- |
| Propósito | Obter do cliente a confirmação de que a entrega atende ao que foi contratado, antes da produção |
| Categorias | B e C obrigatória |
| Gatilho | G3 aprovado |
| Entradas | Release em ambiente de homologação do cliente, A04, A09, roteiro de homologação |
| Saídas | Registro de homologação aprovado pelo cliente; na categoria C, A11 Relatório de teste de intrusão |
| Papéis | R QA, A GP, C PO e DEV, I SUP e CTO |
| Ferramentas | Azure Test Plans (roteiro e resultado), Azure Wiki |
| Instrumento de apoio | [Template A09](../Templates.md#a09-plano-de-testes) (critérios de saída), [Template A11](../Templates.md#a11-relatório-de-teste-de-intrusão) |
| Critério de conclusão | Registro de homologação assinado pelo representante do cliente, sem defeito crítico em aberto |
| Problemas atendidos | P03, P07 |

### Passos

1. O QA prepara o roteiro de homologação a partir dos critérios de aceite das Features do release
2. O GP agenda a homologação com o cliente e confirma quem assina pelo cliente
3. O cliente executa o roteiro com acompanhamento do QA
4. Na categoria C, o núcleo de segurança conduz o teste de intrusão no ambiente de homologação e publica o A11. A implantação em produção só ocorre sem achado crítico em aberto
5. Defeitos apontados são classificados por severidade, e os críticos voltam à construção
6. O GP registra a aprovação do cliente

## AT20 Migrar dados e implantar

| Campo | Conteúdo |
| --- | --- |
| Propósito | Colocar a release em produção de forma reversível e monitorada |
| Categorias | A, B, C e D obrigatória. Migração de dados e plano A13 obrigatórios em B e C |
| Gatilho | G3 aprovado, e homologação aprovada nas categorias B e C |
| Entradas | A12, A04, artefato do build aprovado, contato técnico da operadora nas instalações dedicadas |
| Saídas | A13 Plano de implantação e migração de dados nas categorias B e C; release em produção; verificações pós-implantação registradas; material de treinamento entregue nas categorias B e C |
| Papéis | R e A SRE, C GP, ARQ, DEV, SEC e DPO, I PO, SUP e CTO |
| Ferramentas | Azure Pipelines (estágio de produção), Grafana e Azure Monitor |
| Instrumento de apoio | [Template A13](../Templates.md#a13-plano-de-implantação-e-migração-de-dados), [Template A12](../Templates.md#a12-plano-de-release-e-de-rollback) |
| Critério de conclusão | Verificações pós-implantação aprovadas e monitoramento ativo durante o período de estabilização |
| Problemas atendidos | P05 |

### Passos

1. Nas categorias B e C, preparar o A13 com o DEV do squad responsável antes de agendar a janela
2. Comunicar a janela ao Suporte e, nas categorias B e C, ao cliente, com a antecedência definida no A12
3. Nas categorias B e C, executar o ensaio da migração em homologação com dados anonimizados e medir o tempo
4. Executar a implantação pelo pipeline, seguindo a sequência do A12. Nas instalações dedicadas do Autoriza, a implantação é assistida e o SRE executa o roteiro do A13 junto da operadora
5. Executar as verificações pós-implantação e registrar o resultado
6. Se um gatilho de rollback for atingido, executar o rollback imediatamente, sem aguardar decisão adicional
7. Nas categorias B e C, treinar os usuários-chave do cliente
8. Monitorar indicadores de estabilização por cinco dias úteis nas categorias B e C, e por 24 horas nas categorias A e D

## AT21 Conduzir o gate G4

| Campo | Conteúdo |
| --- | --- |
| Propósito | Encerrar formalmente a entrega com aceite do cliente e transferência para a operação |
| Categorias | B e C obrigatória |
| Gatilho | Cinco dias úteis de estabilização concluídos |
| Entradas | Registro de homologação, indicadores de estabilização, documentação de operação |
| Saídas | A14 Termo de aceite assinado; documentação de operação entregue ao Suporte; lições aprendidas registradas no A17 |
| Papéis | R e A GP, C PO e SRE, I SUP e CTO. O cliente assina o aceite |
| Ferramentas | Repositório contratual, Azure Wiki, Azure Boards |
| Instrumento de apoio | [CL07 Checklist do gate G4](../Checklists.md#cl07-gate-g4-aceite), [Template A14](../Templates.md#a14-termo-de-aceite-do-cliente) |
| Critério de conclusão | A14 assinado e arquivado, e Épico fechado no Boards |
| Problemas atendidos | P03, P07, P09 |

### Passos

1. O GP verifica o CL07
2. O SRE confirma que os indicadores de estabilização ficaram dentro do esperado
3. O GP envia o A14 ao cliente e arquiva a versão assinada
4. O SRE entrega a documentação de operação ao Suporte em sessão de repasse
5. O GP conduz a sessão de lições aprendidas e registra no A17
6. O GP fecha o Épico e libera o faturamento final
