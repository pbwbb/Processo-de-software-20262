---
sidebar_position: 6
---

# Registro de Problemas e Oportunidades

Cada problema recebe um identificador estável, usado como tag nos work items do Boards e citado por toda decisão de processo da Sprint 2.

## Problemas

| ID | Problema | Evidência | Fonte | Stakeholder mais afetado |
| --- | --- | --- | --- | --- |
| P01 | Ausência de processo definido | Seis squads e quatro formas distintas de registrar requisito | Observação | CTO |
| P02 | Requisitos sem rastreabilidade | 38% dos chamados do último trimestre classificados como comportamento não especificado | Extração da ferramenta de chamados | Suporte e clientes |
| P03 | Estimativa e prazo não confiáveis | 14 dos 20 projetos de implantação de 2025 estouraram o prazo, com atraso médio de 41 dias | Extração do Azure DevOps e contratos | Comercial e PMO |
| P04 | Qualidade concentrada no fim da iteração | QA recebe 70% do volume na última semana da sprint | Extração do Azure DevOps | QA e desenvolvedores |
| P05 | Implantação manual e arriscada | Três rollbacks em 2025, com janela média de seis horas | Registro de operações | SRE e clínicas |
| P06 | Segurança tratada no fim do ciclo | Pentest anual gerou 23 achados, sendo 7 críticos, corrigidos em média 60 dias depois | Relatório do pentest | Segurança e operadoras |
| P07 | Conformidade reativa | Auditoria de cliente em 2025 exigiu evidências de controle de acesso e a empresa levou 3 semanas para reuni-las | Análise documental | Operadoras e CTO |
| P08 | Sustentação interrompe o desenvolvimento | 35% da capacidade dos squads consumida por demandas não planejadas | Extração do Azure DevOps | Product Owners |
| P09 | Conhecimento concentrado | Duas pessoas detêm o conhecimento do módulo de faturamento TISS | Entrevistas | CTO |
| P10 | Ausência de métricas de processo | Nenhum indicador de lead time, densidade de defeitos ou retrabalho é coletado | Observação | CTO e diretoria |
| P11 | Mudança de escopo sem controle | Alterações aceitas verbalmente em projetos de preço fechado | Entrevistas e análise contratual | PMO e Comercial |

## Agrupamento por causa raiz

| Causa raiz | Problemas | Leitura |
| --- | --- | --- |
| Falta de definição comum | P01, P10 | Sem processo descrito, não há o que padronizar nem o que medir |
| Entrada de demanda desgovernada | P02, P03, P08, P11 | Três portas de entrada sem triagem produzem retrabalho, atraso e escopo não controlado |
| Verificação empurrada para o fim | P04, P05, P06 | Teste, implantação e segurança acontecem depois que o custo da correção já subiu |
| Conhecimento e evidência não registrados | P07, P09 | O que não é documentado durante o ciclo precisa ser reconstruído sob pressão |

## Oportunidades

| ID | Oportunidade | Por que facilita a adoção |
| --- | --- | --- |
| O01 | Azure DevOps já contratado e subutilizado | Elimina custo e tempo de aquisição de ferramenta |
| O02 | Núcleo interno de segurança com duas pessoas | Viabiliza atividades de segurança distribuídas sem contratação externa |
| O03 | Quatro squads já operam em cadência quinzenal | Reduz a mudança cultural necessária na fase de construção |
| O04 | Contratos com operadoras já exigem evidência formal | Transforma a institucionalização do processo em argumento comercial |
| O05 | Volume de chamados já é registrado em ferramenta própria | Fornece linha de base imediata para os indicadores de processo |
