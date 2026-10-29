---
sidebar_position: 2
---

# Tipos de Software e Projetos

## Portfólio

| Linha | Natureza | Volume | Característica dominante |
| --- | --- | --- | --- |
| Vértice Care | SaaS multi-tenant de gestão de clínicas, com prontuário, agenda e faturamento TISS | 310 clientes ativos, release quinzenal | Cadência alta, escopo definido internamente, baixo risco contratual |
| Vértice Autoriza | Plataforma de autorização e auditoria de procedimentos para operadoras | 12 operadoras, instalação dedicada | Dado sensível, alto risco regulatório, janela de implantação longa |
| Projetos de implantação e customização | Integração com sistemas do cliente, parametrização e migração de dados | 20 projetos por ano, duração média de 4 meses | Escopo, prazo e preço acordados em contrato |
| Sustentação | Correção de defeitos, ajuste de parametrização e pequenas evoluções | 400 chamados por mês | Fluxo contínuo, prioridade por SLA |
| Laboratório de inovação | Provas de conceito em classificação de glosas e reconhecimento de guias | 3 a 4 iniciativas por ano | Exploratório, resultado descartável |

## Perfil de cada linha

### Vértice Care

Produto de maior receita e maior número de usuários. Uma falha afeta centenas de clínicas ao mesmo tempo, mas a correção também chega a todas de uma vez, porque o ambiente é único. O escopo é decidido internamente pelo Product Owner, sem compromisso contratual de entrega de funcionalidade específica.

### Vértice Autoriza

Trata autorização de procedimentos, o que envolve dado clínico e decisão com efeito financeiro direto sobre a operadora. Roda em instalação dedicada por cliente, então uma correção precisa ser distribuída doze vezes. É a linha com maior exposição regulatória e a única que hoje passa por teste de intrusão antes do go-live.

### Projetos de implantação e customização

Cada projeto nasce de um contrato com escopo, prazo e preço acordados. É onde o atraso tem consequência financeira direta e onde a mudança de escopo não controlada corrói a margem.

### Sustentação

Entra pelo suporte, atravessa a triagem e chega aos squads sem passar por planejamento. Hoje consome 35% da capacidade das equipes de produto, o que torna a previsão de entrega pouco confiável.

### Laboratório de inovação

Experimentos conduzidos por dois ou três desenvolvedores, com duração de poucas semanas. O resultado esperado é uma decisão de seguir ou abandonar, não um software em produção.

## Consequência para o processo

As cinco linhas pedem graus de formalidade distintos. Submeter a sustentação às mesmas fases de um contrato de implantação paralisaria o atendimento, e dispensar o contrato das fases de concepção manteria o atraso crônico. Essa constatação é a origem direta das categorias de projeto definidas na Sprint 2.
