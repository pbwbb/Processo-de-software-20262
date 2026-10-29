---
sidebar_position: 6
---

# Mapa de Ferramentas

O Azure DevOps já é pago e subutilizado, o que o torna a base natural do processo. Nenhuma ferramenta nova paga é proposta nas duas primeiras ondas.

## Ferramentas por fase

| Fase | Ferramenta | Uso |
| --- | --- | --- |
| Entrada | Azure Boards | Fila única, classificação em categoria, tag do problema de origem |
| Entrada | Ferramenta de chamados | Registro do chamado e triagem N1, integrada ao Boards por item vinculado |
| Concepção | Azure Wiki | Documento de visão, registro de riscos |
| Concepção | Azure Boards | Épicos e Features com estimativa de ordem de grandeza |
| Elaboração | Azure Wiki | Especificação de requisitos, arquitetura, registros de decisão, avaliação de risco |
| Elaboração | Azure Test Plans | Plano de testes e suítes por release |
| Elaboração | Miro ou quadro equivalente | Modelagem de ameaças em sessão conjunta |
| Construção | Azure Repos | Branch por item, pull request com revisão obrigatória |
| Construção | Azure Pipelines | Integração contínua, build, teste automatizado, análise estática |
| Construção | SonarQube | Análise estática e portão de qualidade no pipeline |
| Construção | Trivy ou OWASP Dependency-Check | Análise de dependências vulneráveis no pipeline |
| Transição | Azure Pipelines | Implantação por ambiente, com aprovação manual no gate G3 |
| Transição | Azure Wiki | Plano de implantação, registro de homologação, termo de aceite |
| Operação | Grafana e Azure Monitor | Disponibilidade, desempenho e alerta |
| Operação | Ferramenta de chamados | Incidentes, SLA e análise de causa raiz |
| Transversal | Azure Dashboards | Painel dos sete indicadores |
| Transversal | Azure Wiki | Processo, templates, decisões e evidência de conformidade |

## Configuração do Azure DevOps

| Elemento | Configuração proposta |
| --- | --- |
| Processo de template | Agile |
| Hierarquia de work items | Epic, Feature, User Story e Task |
| Caminhos de área | Um por produto e um por squad |
| Iterações | Quinzenais, nomeadas por ano e número |
| Campo obrigatório | Categoria de projeto, com os valores A, B, C, D e E |
| Tags obrigatórias | Problema de origem no formato P01 a P11, e categoria |
| Vínculos | Related entre item que produz um artefato e item que o consome |
| Regras | Transição para Resolved bloqueada sem critério de aceite preenchido |
| Quadro da categoria D | Quadro próprio com limite de seis itens em progresso por squad |
| Permissões | Páginas com dado sensível restritas por grupo, revisadas a cada semestre |

## Ferramenta candidata para a onda 3

| Ferramenta | Função | Por que fica para depois |
| --- | --- | --- |
| Ferramenta de modelagem BPMN | Modelagem formal dos fluxos do processo | Os diagramas em Mermaid na Wiki atendem a adoção inicial sem custo de licença |
| Gestão de catálogo de serviços | Formalização ITIL completa | O ganho só aparece depois que a fila única estiver consolidada |
