---
sidebar_position: 5
---

# Riscos da Adoção

Severidade calculada como probabilidade por impacto, em escala de baixo, médio e alto.

| ID | Risco | Probabilidade | Impacto | Severidade | Resposta | Responsável |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | Equipes percebem o processo como burocracia e voltam à prática informal | Alta | Alto | Alta | Piloto com critério de avanço que exige não piorar o lead time, e matriz que dispensa o que não agrega por categoria | Engenheiro de processo |
| R02 | Comercial continua emitindo proposta com prazo antes do gate G1 | Alta | Alto | Alta | Regra registrada no termo de abertura dos projetos e aprovação de G1 compartilhada entre gerente de projeto e CTO | CTO |
| R03 | Reserva de 20% para sustentação é consumida e ninguém decide o estouro | Média | Alto | Média | Estouro do limite exige decisão explícita e registrada do Product Owner, visível no quadro | Product Owner |
| R04 | Papel de engenheiro de processo não é preenchido em dedicação integral | Média | Alto | Média | Condição de início da onda 0, sem a qual a implantação não começa | CTO |
| R05 | Realocação do QA para dentro dos squads gera perda de padrão de teste | Média | Médio | Média | Plano de testes padronizado pelo catálogo de artefatos e revisão cruzada entre analistas | Analista de qualidade |
| R06 | Security champions sem tempo alocado tornam a prática simbólica | Alta | Médio | Média | Alocação formal de 10% da capacidade do champion, acordada com o squad lead | CTO |
| R07 | Doze instalações dedicadas do Autoriza impedem o pipeline automatizado | Alta | Médio | Média | Implantação assistida mantida e automação negociada cliente a cliente na onda 3 | Engenheiro de confiabilidade |
| R08 | Suporte, que responde ao Comercial, ignora a fila única | Média | Alto | Média | Acordo formal de nível de serviço interno entre tecnologia e comercial, revisado na revisão trimestral | CTO e Diretor Comercial |
| R09 | Indicadores coletados e não usados em decisão | Média | Médio | Média | Regra de remoção de indicador sem consequência após dois trimestres | Engenheiro de processo |
| R10 | Desvios aprovados em volume que esvazia a matriz de customização | Média | Alto | Média | Revisão trimestral obrigatória dos desvios acumulados e ajuste da matriz quando o padrão se repete | Engenheiro de processo |
| R11 | Treinamento insuficiente faz os squads interpretarem o processo de formas diferentes | Média | Médio | Média | Oito horas de treinamento por grupo com exercício sobre casos reais da empresa, e Wiki como fonte única | Engenheiro de processo |

## Riscos herdados das lacunas

Dois riscos vêm de situações que o processo não resolve, identificadas em [Análise de Aderência](./Analise-de-Aderencia.md).

| Risco | Origem | Tratamento adotado |
| --- | --- | --- |
| R08 | Suporte fora da estrutura de tecnologia | Acordo interno de nível de serviço, com recomendação de revisão da estrutura organizacional |
| R07 | Instalações dedicadas do Autoriza | Automação progressiva por cliente, sem exigir janela única |

## Monitoramento

Os riscos são revisados na revisão trimestral do processo. Um risco cuja resposta não foi executada por dois trimestres é escalado ao CTO com proposta de alteração do plano de implantação.
