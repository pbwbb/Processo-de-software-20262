---
sidebar_position: 3
---

# Estrutura das Equipes

## Organograma de tecnologia

```mermaid
graph TD
  CEO[CEO] --> CTO[CTO]
  CEO --> DC[Diretor Comercial]
  CTO --> S1[Squad Care Clinico<br/>7 pessoas]
  CTO --> S2[Squad Care Financeiro<br/>8 pessoas]
  CTO --> S3[Squad Autoriza Core<br/>8 pessoas]
  CTO --> S4[Squad Autoriza Auditoria<br/>6 pessoas]
  CTO --> S5[Squad Integracoes<br/>5 pessoas]
  CTO --> S6[Squad Plataforma<br/>6 pessoas]
  CTO --> QA[QA centralizado<br/>5 pessoas]
  CTO --> INF[Infraestrutura e SRE<br/>4 pessoas]
  CTO --> SEC[Seguranca da Informacao<br/>2 pessoas]
  CTO --> PMO[PMO<br/>2 gerentes de projeto]
  DC --> SUP[Suporte N1 e N2<br/>9 pessoas]
```

## Distribuição das 86 pessoas de tecnologia

| Grupo | Pessoas | Responsabilidade atual |
| --- | --- | --- |
| Squads de produto e integração | 40 | Desenvolvimento do Care, do Autoriza e das customizações |
| QA centralizado | 5 | Teste manual de todos os squads, concentrado no fim da iteração |
| Infraestrutura e SRE | 4 | Ambientes, deploy manual e monitoramento |
| Segurança da Informação | 2 | Política, gestão de acessos e acompanhamento do pentest anual |
| PMO | 2 | Cronograma e relacionamento nos contratos de implantação |
| Suporte N1 e N2 | 9 | Atendimento de chamados e triagem para os squads |
| Product Owners | 4 | Priorização do Care e do Autoriza |
| Arquitetura | 2 | Decisões técnicas sem registro formal |
| Demais funções | 18 | Dados, implantação em cliente e treinamento |

## Observações do diagnóstico

Os seis squads não trabalham do mesmo modo. Quatro seguem um Scrum informal com sprints de duas semanas, enquanto o Squad Integrações e o Squad Plataforma operam por demanda, sem cadência. Essa divergência não é uma escolha documentada, e sim o resultado de equipes formadas em momentos diferentes.

O QA centralizado responde a todos os squads ao mesmo tempo, o que transforma a última semana de cada iteração em gargalo previsível.

O Suporte responde ao Diretor Comercial, e não ao CTO. Isso faz com que a priorização de chamados chegue aos squads por fora da estrutura de tecnologia, sem negociação de capacidade.

A arquitetura não tem papel formal. Dois desenvolvedores seniores atuam de fato como arquitetos, sem que as decisões sejam registradas em lugar algum, o que contribui para a concentração de conhecimento descrita no problema P09.
