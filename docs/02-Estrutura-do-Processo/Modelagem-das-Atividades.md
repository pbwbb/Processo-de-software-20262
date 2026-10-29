---
sidebar_position: 3
---

# Modelagem das Atividades

Os fluxos abaixo estão em notação de diagrama de atividades simplificado, renderizados em Mermaid. Cada caixa corresponde a uma atividade especificada no Grau B, conforme a tabela de [fluxos e atividades](../04-Especificacao-do-Processo/Rastreabilidade.md#dos-fluxos-às-atividades).

## Fluxo de entrada e classificação da demanda

```mermaid
graph TD
  A[Demanda registrada na fila unica] --> B{Qual a origem}
  B -->|Chamado de suporte| C{Esforco acima de 40h}
  B -->|Contrato assinado| D[Categoria B]
  B -->|Backlog de produto| E{Trata dado sensivel ou exigencia regulatoria}
  B -->|Hipotese tecnica| F[Categoria E]
  C -->|Nao| G[Categoria D]
  C -->|Sim| E
  E -->|Sim| H[Categoria C]
  E -->|Nao| I[Categoria A]
  D --> J[Fase 1 Concepcao]
  H --> J
  I --> K[Fase 3 Construcao]
  G --> L[Fase 5 fluxo continuo]
  F --> M[Ciclo exploratorio]
```

## Fluxo das fases planejadas, categorias B e C

```mermaid
graph TD
  A[Concepcao] --> B[Levantar necessidade e stakeholders]
  B --> C[Definir escopo macro]
  C --> D[Levantar riscos e estimar ordem de grandeza]
  D --> E{G1 aprovado}
  E -->|Nao| C
  E -->|Sim| F[Elaboracao]
  F --> G[Detalhar requisitos do nucleo]
  G --> H[Definir arquitetura e registrar decisoes]
  H --> I[Avaliar risco de seguranca e privacidade]
  I --> J[Elaborar plano de release e de testes]
  J --> K{G2 aprovado}
  K -->|Nao| H
  K -->|Sim| L[Construcao iterativa]
  L --> M{G3 aprovado}
  M -->|Nao| L
  M -->|Sim| N[Transicao]
  N --> O{G4 aprovado}
  O -->|Nao| N
  O -->|Sim| P[Operacao e evolucao]
```

## Fluxo da iteração de construção

```mermaid
graph LR
  A[Backlog preparado] --> B[Planejamento da iteracao]
  B --> C[Implementacao]
  C --> D[Revisao de codigo por par]
  D --> E[Teste automatizado e integracao continua]
  E --> F{Definicao de pronto atendida}
  F -->|Nao| C
  F -->|Sim| G[Incremento em homologacao]
  G --> H[Revisao da iteracao]
  H --> I[Retrospectiva]
  I --> B
```

## Fluxo da sustentação, categoria D

```mermaid
graph TD
  A[Chamado aberto no suporte] --> B[Triagem N1]
  B --> C{Resolvido no N1}
  C -->|Sim| D[Encerramento com registro]
  C -->|Nao| E[Classificacao de severidade e SLA]
  E --> F{Limite de trabalho em progresso atingido}
  F -->|Sim| G[Fila de espera priorizada por severidade]
  F -->|Nao| H[Correcao pelo squad responsavel]
  G --> H
  H --> I[Teste e revisao de codigo]
  I --> J[Release de correcao]
  J --> K[Analise de causa raiz se severidade critica]
  K --> L[Proposta de evolucao para o backlog]
```

## Fluxo de controle de mudanças, categorias B e C

```mermaid
graph TD
  A[Solicitacao de mudanca registrada] --> B[Analise de impacto em escopo prazo e custo]
  B --> C{Impacto dentro da tolerancia contratual}
  C -->|Sim| D[Aprovacao do gerente de projeto]
  C -->|Nao| E[Submissao ao cliente]
  E --> F{Cliente aprova}
  F -->|Nao| G[Registro da recusa e manutencao da linha de base]
  F -->|Sim| H[Aditivo contratual]
  D --> I[Atualizacao da linha de base e do backlog]
  H --> I
  I --> J[Atualizacao da matriz de rastreabilidade]
```

Este fluxo é a resposta a P11. Hoje a alteração de escopo é aceita verbalmente, sem análise de impacto e sem registro oponível ao cliente.

## Fluxo do ciclo exploratório, categoria E

```mermaid
graph LR
  A[Hipotese registrada] --> B[Definicao do criterio de sucesso]
  B --> C[Experimento com prazo maximo de 4 semanas]
  C --> D{Criterio atendido}
  D -->|Sim| E[Proposta de produto entra na fila unica]
  D -->|Nao| F[Registro do aprendizado e encerramento]
```
