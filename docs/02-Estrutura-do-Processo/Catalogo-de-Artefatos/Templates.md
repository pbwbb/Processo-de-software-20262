---
sidebar_position: 1
---

# Templates

Modelos mínimos dos artefatos obrigatórios, como definidos no Grau A.

:::tip Versão atual
A versão em uso, com os 18 artefatos, cabeçalho comum e pacote para download, está em [Templates do Grau B](../../04-Especificacao-do-Processo/Templates.md). Esta página fica como registro da Sprint 2.
:::

## A01 Documento de visão

```markdown
# Visão, <nome da iniciativa>

## Problema
Qual dor do cliente ou da operação motiva esta iniciativa.

## Oportunidade
O que a Vértice ganha ao resolver.

## Stakeholders
| Stakeholder | Interesse | Influência |

## Escopo macro
Incluído e excluído, em frases curtas.

## Critérios de sucesso
Métrica, valor alvo e prazo de verificação.

## Riscos iniciais
| Risco | Probabilidade | Impacto | Resposta |

## Estimativa de ordem de grandeza
Faixa em pessoas-mês e premissas usadas.

## Categoria proposta
Categoria e justificativa pelos cinco fatores de enquadramento.
```

## A03 Item de backlog

```markdown
**Como** <papel do usuário>
**quero** <capacidade>
**para que** <benefício>.

### Critérios de aceite
- Dado <contexto>, quando <ação>, então <resultado verificável>
- Dado <contexto>, quando <ação de erro>, então <tratamento esperado>

### Problema de origem
P<NN>

### Categoria
<A, B, C, D ou E>
```

## A05 Matriz de rastreabilidade

```markdown
| Requisito | Origem | Work item | Commit ou PR | Caso de teste | Status |
```

## A06 Registro de decisão de arquitetura

```markdown
# ADR <NNN>, <título da decisão>

**Status** proposta, aceita ou substituída
**Data**
**Decisores**

## Contexto
Situação técnica e restrições que forçaram a decisão.

## Decisão
O que foi decidido, em uma frase.

## Alternativas consideradas
| Alternativa | Vantagem | Por que foi descartada |

## Consequências
O que passa a ser verdade, incluindo o custo aceito.
```

## A07 Avaliação de risco de segurança e privacidade

```markdown
# Avaliação de risco, <nome da iniciativa>

## Dados tratados
| Dado | Classificação | Base legal | Retenção |

## Superfície exposta
Interfaces, integrações e perfis de acesso.

## Riscos identificados
| Risco | Probabilidade | Impacto | Controle adotado | Responsável |

## Requisitos de segurança aplicáveis
Nível ASVS exigido pela categoria e requisitos selecionados.

## Parecer do encarregado de dados
```

## A09 Plano de testes

```markdown
# Plano de testes, <nome da iniciativa>

## Estratégia
Níveis de teste, proporção de automação e critérios de parada.

## Escopo
O que será testado e o que foi deliberadamente deixado de fora.

## Ambientes e massa de dados
Como a massa é gerada e como o dado pessoal é anonimizado.

## Critérios de saída
| Critério | Valor exigido |

## Riscos de teste
```

## A12 Plano de release e de rollback

```markdown
# Release <versão>

## Conteúdo
| Item | Work item | Categoria |

## Janela e comunicação
Data, duração estimada e quem é avisado.

## Sequência de implantação
1.

## Verificações pós-implantação
| Verificação | Resultado esperado | Responsável |

## Plano de rollback
Gatilho de acionamento, passos e tempo máximo de reversão.
```

## A15 Registro de riscos

```markdown
| ID | Risco | Probabilidade | Impacto | Severidade | Resposta | Responsável | Status |
```

## A16 Solicitação de mudança

```markdown
# Solicitação de mudança <NNN>

**Solicitante**
**Data**
**Projeto**

## Mudança pedida
## Motivo
## Análise de impacto
| Dimensão | Impacto |
| Escopo | |
| Prazo | |
| Custo | |
| Risco | |

## Decisão
Aprovada, recusada ou aprovada com aditivo. Quem decidiu e quando.

## Linha de base atualizada
Referência à versão do escopo após a mudança.
```

## A17 Retrospectiva

```markdown
# Retrospectiva, iteração <NN>

| O que funcionou | O que atrapalhou | Decisões | Ação de melhoria |

**Ação com responsável e prazo**
**Verificação da ação da iteração anterior**
```
