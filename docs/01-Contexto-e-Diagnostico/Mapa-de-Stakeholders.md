---
sidebar_position: 4
---

# Mapa de Stakeholders

## Mapa de poder e interesse

| Quadrante | Estratégia | Stakeholders |
| --- | --- | --- |
| Poder alto e interesse alto | Gerenciar de perto | CTO, operadoras contratantes, CEO e Diretor Comercial |
| Poder alto e interesse baixo | Manter satisfeito | ANS e ANPD |
| Poder médio e interesse alto | Manter informado e envolvido | PMO, Product Owners, desenvolvedores e QA, SRE e segurança |
| Poder baixo e interesse médio | Monitorar | Suporte N1 e N2, clínicas e profissionais de saúde |

## Detalhamento

| Stakeholder | Tipo | Interesse principal | Poder | Expectativa em relação ao processo |
| --- | --- | --- | --- | --- |
| CEO e Diretor Comercial | Interno | Previsibilidade de prazo e preservação de margem | Alto | Que o processo reduza o atraso sem aumentar o custo de estrutura |
| CTO | Interno | Capacidade de entrega e redução de retrabalho | Alto | Que o processo seja adotável pelos squads atuais |
| Gerentes de projeto do PMO | Interno | Controle de escopo e aceite formal | Alto | Que exista um procedimento de mudança oponível ao cliente |
| Product Owners | Interno | Fluxo que não trave a evolução do produto | Médio | Que o SaaS não herde a formalidade dos contratos |
| Squad leads e desenvolvedores | Interno | Clareza de requisito e critério de pronto | Médio | Que a demanda chegue entendida e priorizada |
| Analistas de qualidade | Interno | Distribuição do teste ao longo da iteração | Médio | Que o teste deixe de se concentrar na última semana |
| Infraestrutura, SRE e Segurança | Interno | Implantação segura, reversível e rastreável | Médio | Que a implantação deixe de depender de janela manual |
| Suporte N1 e N2 | Interno | Redução do volume de chamados por defeito | Baixo | Que a triagem tenha critério e o retorno tenha prazo |
| Operadoras contratantes | Externo | Cumprimento contratual e evidência de conformidade | Alto | Que a Vértice apresente evidências sem esforço extraordinário |
| Clínicas e profissionais de saúde | Externo | Disponibilidade e usabilidade do SaaS | Médio | Que atualizações não interrompam o atendimento |
| ANS e ANPD | Externo regulador | Conformidade com TISS, LGPD e normas setoriais | Alto | Que o tratamento de dado sensível seja documentado |
| Auditorias contratadas pelos clientes | Externo | Evidências de controle e de ciclo de vida | Médio | Que a evidência exista no momento da auditoria |

## Conflitos de interesse relevantes

Três tensões aparecem no levantamento e precisam ser resolvidas por decisão de processo, não por negociação caso a caso.

1. O Comercial quer compromisso de prazo cedo, e o CTO quer escopo entendido antes do compromisso. O gate G1 existe para arbitrar esse ponto
2. O Suporte quer atendimento imediato, e os Product Owners querem capacidade previsível para o roadmap. O fluxo separado de sustentação com limite de capacidade existe para isso
3. As operadoras querem evidência formal, e os squads querem documentação mínima. A matriz de customização existe para que a formalidade recaia apenas sobre as categorias que a exigem
