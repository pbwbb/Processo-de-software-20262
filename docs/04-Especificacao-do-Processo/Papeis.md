---
sidebar_position: 4
---

# Papéis

O Grau A definiu onze papéis e a [Matriz RACI](../02-Estrutura-do-Processo/Matriz-RACI.md). Esta página especifica cada papel no nível que uma pessoa precisa para assumi-lo: o que faz, o que pode decidir, que competências exige e onde atua no processo.

Um papel não é um cargo. Uma pessoa pode acumular papéis, como o núcleo de segurança, que acumula o de encarregado de dados, e um papel pode ser exercido por várias pessoas, como os 40 desenvolvedores.

## Resumo

| Papel | Responde (A) por | Autoridade principal | Ocupação na Vértice |
| --- | --- | --- | --- |
| [Product Owner](#product-owner-po) | AT06, AT10, AT12, AT17 | Prioridade do backlog e aceite do incremento | 4 pessoas |
| [Gerente de projeto](#gerente-de-projeto-gp) | AT02 a AT04, AT19, AT21, AT24 | Mudança de escopo dentro da tolerância contratual | 2 pessoas no PMO |
| [Engenheiro de processo](#engenheiro-de-processo-ep) | AT01, AT26, AT27 | Regras de classificação e pauta da revisão do processo | 1 pessoa, papel novo |
| [Arquiteto de software](#arquiteto-de-software-arq) | AT07, AT28 | Decisões de arquitetura | 2 seniores, papel formalizado |
| [Desenvolvedor](#desenvolvedor-dev) | AT13, AT14 | Aprovação de pull request | 40 pessoas |
| [Analista de qualidade](#analista-de-qualidade-qa) | AT09, AT15 | Bloqueio de item que não passa no teste | 5 pessoas, nos squads |
| [Security champion](#security-champion-sec) | AT16 | Bloqueio por achado crítico | 1 por squad |
| [Engenheiro de confiabilidade](#engenheiro-de-confiabilidade-sre) | AT18, AT20, AT22, AT23 | Aprovação do G3 e acionamento de rollback | 4 pessoas |
| [Analista de suporte](#analista-de-suporte-sup) | Nenhuma | Severidade do chamado | 9 pessoas |
| [Encarregado de dados](#encarregado-de-dados-dpo) | AT08 | Parecer sobre tratamento de dado pessoal | Núcleo de segurança |
| [CTO](#cto) | AT05, AT11, AT25 | Gates G1 e G2 e desvios do processo | 1 pessoa |

## Product Owner (PO)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Maximizar o valor entregue por um produto, decidindo o que é construído e em que ordem |
| Responsabilidades | Manter o backlog priorizado e preparado; escrever ou validar critérios de aceite; aceitar ou devolver itens na revisão da iteração; negociar a reserva de 20% para a sustentação; conduzir a Concepção de módulos críticos de produto (categoria C sem contrato) |
| Autoridade | Decide a prioridade do backlog; aceita o incremento; decide furar o limite de trabalho em progresso da categoria D |
| Não decide | Mudança de escopo contratado, que é do GP; arquitetura, que é do ARQ |
| Competências | Conhecimento do domínio de saúde suplementar, escrita de critério de aceite, priorização por valor e risco |
| Artefatos de autoria | A03 Backlog com critérios de aceite; A15 Registro de riscos nas categorias A e C de produto |
| Interage com | GP, QA, ARQ, SUP e clientes |

## Gerente de projeto (GP)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que projetos contratados entreguem o escopo acordado, no prazo e no custo |
| Responsabilidades | Conduzir a Concepção dos projetos contratados; manter a linha de base do escopo; avaliar solicitações de mudança; conduzir homologação e aceite com o cliente; registrar lições aprendidas |
| Autoridade | Aprova mudança dentro da tolerância contratual; recomenda a decisão do G1 |
| Não decide | Aprovação de gate estrutural, que é do CTO; prioridade de produto, que é do PO |
| Competências | Gestão de escopo e risco, negociação com cliente, leitura de contrato |
| Artefatos de autoria | A01 Documento de visão; A02 Termo de abertura; A14 Termo de aceite; A15 Registro de riscos na categoria B; A16 Solicitação de mudança |
| Interage com | Cliente, Comercial, CTO, ARQ e PO |

O GP exerce também a função de análise de negócio na Concepção, que o Grau A atribuía a um "analista de negócio" inexistente na estrutura da Vértice. Ver decisão DB03.

## Engenheiro de processo (EP)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Ser o dono do processo, mantendo-o útil, medido e atualizado |
| Responsabilidades | Manter o portal e os templates; definir as regras de classificação; instruir pedidos de desvio; coletar os indicadores e publicar o painel; conduzir a revisão trimestral; treinar as equipes |
| Autoridade | Decide dúvidas de classificação de demanda; define a pauta da revisão do processo; sinaliza artefato desatualizado |
| Não decide | Aprovação de desvio, que é do CTO |
| Competências | Engenharia de software e processos, MPS.BR, Azure DevOps, facilitação, análise de dados |
| Artefatos de autoria | Portal do processo; painel de indicadores; registro de desvios |
| Interage com | Todos os papéis |

## Arquiteto de software (ARQ)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que as decisões técnicas relevantes sejam boas, conhecidas e registradas |
| Responsabilidades | Definir a arquitetura na Elaboração; registrar decisões como ADR; revisar mudanças que alteram integração, dado ou autenticação; conduzir o G2; responder pelos experimentos da categoria E |
| Autoridade | Aprova ou veta decisão de arquitetura; recomenda a decisão do G2 |
| Não decide | Prioridade do backlog; aprovação final do G2, que é do CTO |
| Competências | Java e .NET, integração com sistemas de operadoras, padrões TISS, segurança de aplicações |
| Artefatos de autoria | A06 Documento de arquitetura e registros de decisão |
| Interage com | DEV, SEC, SRE, PO e GP |

## Desenvolvedor (DEV)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Construir incrementos funcionais, testados e integrados |
| Responsabilidades | Implementar itens; escrever testes automatizados junto do código; revisar o código do par; corrigir achados de segurança; estimar ordem de grandeza na Concepção; executar experimentos |
| Autoridade | Aprova ou devolve pull request de um par |
| Não decide | Aceite do item, que é do PO |
| Competências | Stack do produto, teste automatizado, revisão de código, práticas básicas de codificação segura |
| Artefatos de autoria | Código; A10 Evidência de teste automatizado |
| Interage com | QA, ARQ, SEC e PO |

Um desenvolvedor sênior de cada squad exerce a função de squad lead, que facilita as cerimônias da iteração. A função não é um papel separado, decisão DB05.

## Analista de qualidade (QA)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que a verificação aconteça durante a iteração e que o critério de aceite seja verificável |
| Responsabilidades | Detalhar requisitos; elaborar o plano de testes; executar testes de aceitação e exploratórios; manter a matriz de rastreabilidade; conduzir a homologação com o cliente |
| Autoridade | Bloqueia a passagem de item que não atende à definição de pronto |
| Não decide | Aceite do item, que é do PO |
| Competências | Análise de requisitos, técnicas de teste, automação de teste, Azure Test Plans |
| Artefatos de autoria | A04 Especificação de requisitos; A05 Matriz de rastreabilidade; A09 Plano de testes |
| Interage com | PO, DEV e cliente |

## Security champion (SEC)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Trazer a segurança para dentro do squad, em vez de deixá-la para o fim do ciclo |
| Responsabilidades | Conduzir a avaliação de risco e a modelagem de ameaças; selecionar requisitos ASVS; revisar mudanças sensíveis; tratar achados da análise estática |
| Autoridade | Bloqueia release com achado crítico sem tratamento |
| Não decide | Aceite de risco residual alto, que é do CTO |
| Competências | OWASP Top 10, ASVS, STRIDE, ferramentas de análise estática e de dependências. Formação inicial de 16 horas dada pelo núcleo de segurança |
| Artefatos de autoria | A07 Avaliação de risco; A08 Relatório de ameaças |
| Interage com | Núcleo de segurança, ARQ, DEV e DPO |

## Engenheiro de confiabilidade (SRE)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que a ida à produção seja repetível, reversível e monitorada |
| Responsabilidades | Elaborar o plano de release; manter os pipelines; aprovar o G3; executar implantações e migrações; monitorar a estabilização; responder pela sustentação e pela análise de causa raiz |
| Autoridade | Aprova ou reprova o G3; aciona rollback sem consulta prévia quando o gatilho é atingido |
| Não decide | Conteúdo do release, que é do PO |
| Competências | Azure, containers, Azure Pipelines, observabilidade, gestão de incidentes |
| Artefatos de autoria | A12 Plano de release e de rollback; A13 Plano de implantação e migração |
| Interage com | DEV, SUP, GP e operadoras |

## Analista de suporte (SUP)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Ser a porta de entrada dos chamados e o elo entre cliente e squad |
| Responsabilidades | Triagem N1; classificação de severidade e SLA; registro na fila única; comunicação com o cliente; recepção da documentação de operação no G4 |
| Autoridade | Define a severidade do chamado |
| Não decide | Prioridade entre chamados e trabalho planejado, que segue a reserva acordada com o PO |
| Competências | Conhecimento funcional dos produtos, atendimento, registro estruturado |
| Artefatos de autoria | Registro do chamado |
| Interage com | Clientes, DEV, SRE e PO |

O Suporte responde ao Diretor Comercial, fora da estrutura de tecnologia, lacuna registrada na [Análise de Aderência](../03-Consolidacao/Analise-de-Aderencia.md).

## Encarregado de dados (DPO)

| Campo | Conteúdo |
| --- | --- |
| Propósito | Garantir que o tratamento de dado pessoal tenha base legal e controle adequado |
| Responsabilidades | Emitir parecer sobre a avaliação de risco; ser consultado em migração de dados e requisitos de privacidade |
| Autoridade | Aprova ou condiciona o tratamento de dado pessoal |
| Não decide | Controles técnicos, que são do SEC e do ARQ |
| Competências | LGPD, normas da ANS sobre dado de saúde |
| Artefatos de autoria | Parecer no A07 |
| Interage com | SEC, ARQ e GP |

## CTO

| Campo | Conteúdo |
| --- | --- |
| Propósito | Responder pela tecnologia e pela integridade do processo |
| Responsabilidades | Decidir os gates G1 e G2; aprovar ou recusar desvios; participar da revisão trimestral; aceitar riscos residuais altos |
| Autoridade | Decisão final de G1, G2 e desvios |
| Competências | Visão de negócio e de tecnologia |
| Interage com | EP, ARQ, GP e diretoria |

## Funções que não são papéis do processo

| Função | Como é tratada |
| --- | --- |
| Squad lead | Desenvolvedor sênior que facilita as cerimônias. Decisão DB05 |
| Analista de negócio | Função exercida pelo GP em projeto contratado e pelo PO em módulo de produto. Decisão DB03 |
| Equipe de implantação | SRE com apoio de desenvolvedores do squad responsável. Decisão DB03 |
| Núcleo de segurança | Apoia os security champions, conduz o teste de intrusão (A11) e acumula o papel de DPO |
| Cliente | Parte externa. Valida o escopo, homologa e assina o aceite |
