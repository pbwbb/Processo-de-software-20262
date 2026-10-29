---
sidebar_position: 7
---

# Evolução e Roadmap

Registro das decisões tomadas no Grau B, das dificuldades encontradas, do que ainda está pendente e do plano até a Release 1.0.

## Versões do processo

| Versão | Sprint | Conteúdo | Situação |
| --- | --- | --- | --- |
| 0.1 | Sprint 1 | Diagnóstico organizacional | Concluída |
| 0.2 | Sprint 2 | Estrutura do processo | Concluída |
| 0.3 | Sprint 3 | Proposta consolidada, fim do Grau A | Concluída |
| 0.4 | Sprint 4 | Atividades, papéis, templates e checklists especificados, portal em Docusaurus | Atual, apresentada no T3 |
| 0.5 | Sprint 5 | Gerência de configuração, garantia da qualidade, métricas, governança e melhoria contínua | Planejada |
| 1.0 | Sprint 6 | Processo validado, revisado e publicado | Planejada |

## Decisões do Grau B

| ID | Decisão | Motivo | Impacto |
| --- | --- | --- | --- |
| DB01 | Nos gates G1 e G2, o CTO passa a ser o único A. O GP passa a R no G1 e o ARQ passa a R no G2 | A RACI do Grau A tinha dois A nesses gates, contrariando a regra de um único A por atividade que a própria matriz declarava | Matriz RACI corrigida; AT05 e AT11 |
| DB02 | Na avaliação de risco de segurança e privacidade, o SEC executa (R) e o DPO responde (A) | O Catálogo de Artefatos dava o A07 como autoria do SEC com revisão do DPO, e a RACI dizia o contrário. Prevaleceu o catálogo, coerente com a autoridade do DPO de aprovar o tratamento | Matriz RACI corrigida; AT08 |
| DB03 | Funções citadas sem papel são atribuídas a papéis existentes. A análise de negócio fica com o GP em projeto contratado e com o PO em módulo de produto. A implantação em cliente fica com o SRE, apoiado por DEV do squad responsável | A Vértice não tem analista de negócio nem equipe de implantação formal, e criar papéis novos contrariaria a escolha do Grau A de não ampliar a estrutura | AT02 a AT04, AT20; Papéis |
| DB04 | Três atividades novas na RACI: AT10 Elaborar plano de release, AT17 Revisar a iteração e retrospectivar, AT28 Conduzir experimento | Apareciam nas fases e nos fluxos do Grau A sem responsável definido | Matriz RACI e catálogo de atividades |
| DB05 | Squad lead é uma função exercida por um DEV sênior, e não um papel do processo | O Grau A dava a ele a facilitação das cerimônias em Práticas Adotadas, mas não o definia. Mantém a decisão de não criar Scrum Master | Papéis; Construção |
| DB06 | Novo artefato A18 Registro de experimento, único obrigatório da categoria E. A retrospectiva A17 passa a recomendada na E | A categoria E citava "registro da hipótese" e "registro do aprendizado", que não existiam no catálogo | Catálogo, Matriz de Customização, Templates |
| DB07 | Formato único de especificação de atividade, com 10 campos e passos, e IDs estáveis AT, CL e A | Quem executa encontra a informação sempre no mesmo lugar, e os IDs permitem referência cruzada entre páginas, checklists e work items do Boards | Todas as atividades |
| DB08 | O processo passa a ser mantido como código, no portal Docusaurus versionado em Git, com mudanças por pull request e verificação automática de consistência no pipeline | Aplica ao próprio processo as práticas de versionamento, revisão e integração contínua que ele exige dos squads, as mesmas estudadas no seminário de Detection-as-Code do T1 | Portal, AT27, publicação |
| DB09 | Os checklists derivam literalmente dos critérios escritos no Grau A, sem critério novo de gate | Mantém a consistência com a proposta aprovada. Critério novo só entra por revisão do processo | Checklists |

## Dificuldades encontradas

| Dificuldade | Como foi tratada |
| --- | --- |
| Inconsistências do Grau A só apareceram ao detalhar quem faz o quê | Cada uma virou decisão registrada (DB01 a DB06). Detalhar passou a ser tratado como teste de consistência da proposta |
| Risco de transformar o processo em burocracia para categorias simples | Toda atividade declara em quais categorias é obrigatória, e o roteiro por categoria mostra o caminho mínimo de cada uma |
| Manter a consistência entre muitas páginas à mão | Script de verificação automática que roda antes de cada publicação |
| Migrar a documentação da Wiki do Azure DevOps para o Docusaurus | Script de conversão que preservou diagramas, links e ordem das páginas |
| Escopo pensado para equipes de até quatro pessoas, executado por duas | Priorização dos elementos de maior peso na avaliação, com o restante planejado para as Sprints 5 e 6 |

## Pendências

| Pendência | Sprint | Situação |
| --- | --- | --- |
| Política de gerência de configuração: estratégia de branches, versionamento de produtos, linha de base, gestão de releases e versionamento do próprio processo | 5 | Iniciada na AT13 e na AT14 |
| Garantia da qualidade do processo: auditoria de aderência, revisão de artefatos por pares e tratamento de não conformidades | 5 | Não iniciada |
| Plano de medição: consulta de cada indicador no Azure Boards, procedimento de coleta e painel | 5 | Indicadores definidos no Grau A |
| Governança: fórum de decisão, ciclo de mudança do processo e registro de desvios | 5 | Iniciada na AT25 e na AT27 |
| Melhoria contínua: ligação entre retrospectivas, análises de causa raiz e revisão trimestral em um ciclo único | 5 | Iniciada na AT27 |
| Diagramas por fase com os IDs das atividades | 5 | Não iniciada |
| Validação do processo | 6 | Plano abaixo |
| Busca no portal e versão 1.0 congelada | 6 | Não iniciada |

## Plano das Sprints 5 e 6

| Sprint | Objetivo | Entregáveis |
| --- | --- | --- |
| 5 | Estabelecer os mecanismos de controle e evolução do processo | Gerência de configuração; garantia da qualidade; plano de medição; governança e melhoria contínua; diagramas por fase |
| 6 | Validar, revisar e publicar a Release 1.0 | Relatório de validação; ajustes decorrentes; versão 1.0 congelada no portal; apresentação final |

## Plano de validação

A validação acontece na Sprint 6 e combina quatro técnicas. Cada achado vira item no Boards e, quando aceito, mudança no processo antes da Release 1.0.

| ID | Técnica | Como será feita | Critério de sucesso |
| --- | --- | --- | --- |
| V1 | Simulação por cenário | Percorrer o portal com um caso de cada categoria, usando os exemplos de [Categorias de Projeto](../02-Estrutura-do-Processo/Categorias-de-Projeto.md): agenda com confirmação (A), integração com operadora (B), faturamento TISS (C), correção de coparticipação (D) e classificação de glosas (E). Em cada um, executar as atividades da trilha e preencher os templates | Todas as trilhas percorridas sem atividade órfã, artefato sem template ou decisão sem responsável |
| V2 | Verificação de consistência automática | Script `verificar-consistencia.py`, já em uso no pipeline, ampliado na Sprint 5 para cobrir a Matriz RACI e a Matriz de Customização | Zero inconsistências na publicação da 1.0 |
| V3 | Revisão por pares | Outra equipe da turma revisa o portal com um checklist de clareza, completude e navegabilidade | Achados classificados e tratados ou justificados |
| V4 | Questionário de aplicabilidade | Colegas com experiência profissional avaliam se conseguiriam usar o processo, em escala de 1 a 5 por seção | Média de 4 ou mais em todas as seções |

## Critérios para a Release 1.0

- Todas as pendências da Sprint 5 concluídas
- Validação V1 a V4 executada, com relatório publicado no portal
- Achados da validação tratados ou registrados como evolução futura com justificativa
- Verificação de consistência sem erros
- Versão 1.0 congelada com o versionamento do Docusaurus, mantendo a versão em evolução separada
- Registro de mudanças da 0.4 para a 1.0 publicado nesta página
