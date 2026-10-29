---
sidebar_position: 6
---

# Checklists

Instrumentos de apoio usados nas decisões do processo. Cada checklist transforma um critério escrito no Grau A em itens que podem ser marcados um a um. No Azure DevOps, os checklists de gate são incluídos como lista de verificação no Épico, e o DoR e o DoD como regra do quadro.

| ID | Checklist | Usado em | Quem verifica |
| --- | --- | --- | --- |
| CL01 | [Enquadramento da demanda](#cl01-enquadramento-da-demanda) | AT01 | PO ou SUP, com o EP em caso de dúvida |
| CL02 | [Definição de preparado](#cl02-definição-de-preparado) | AT12 | Squad, no planejamento |
| CL03 | [Definição de pronto](#cl03-definição-de-pronto) | AT13 a AT15, AT22 | QA |
| CL04 | [Gate G1, aprovação de concepção](#cl04-gate-g1-aprovação-de-concepção) | AT05 | GP |
| CL05 | [Gate G2, baseline de arquitetura](#cl05-gate-g2-baseline-de-arquitetura) | AT11 | ARQ |
| CL06 | [Gate G3, prontidão para release](#cl06-gate-g3-prontidão-para-release) | AT18 | SRE |
| CL07 | [Gate G4, aceite](#cl07-gate-g4-aceite) | AT21 | GP |
| CL08 | [Revisão de código](#cl08-revisão-de-código) | AT14 | DEV revisor |
| CL09 | [Verificação de segurança por categoria](#cl09-verificação-de-segurança-por-categoria) | AT08, AT16 | SEC |
| CL10 | [Solicitação de desvio](#cl10-solicitação-de-desvio) | AT25 | EP |

## CL01 Enquadramento da demanda

Marque o nível de cada fator. Qualquer fator em nível alto puxa a demanda para a categoria mais exigente compatível.

| Fator | Pergunta | Baixo | Alto |
| --- | --- | --- | --- |
| Sensibilidade do dado | Trata dado de saúde, financeiro ou pessoal sensível? | Não | Sim |
| Obrigação contratual | Escopo, prazo ou preço estão acordados em contrato? | Não | Sim |
| Exigência regulatória | ANS, TISS, LGPD ou norma de prontuário se aplicam? | Não | Sim |
| Esforço estimado | Qual o esforço provável? | Até 40 horas | Acima de 6 pessoas-mês |
| Reversibilidade | Exige migração de dados ou causa indisponibilidade? | Não, rollback simples | Sim |

**Decisão**

- [ ] Hipótese técnica sem compromisso de entrega → **E**
- [ ] Esforço até 40 horas, sem fator alto além do esforço → **D**
- [ ] Obrigação contratual alta → **B**, ou **C** se dado ou regulação também forem altos
- [ ] Dado sensível ou exigência regulatória alta, sem contrato → **C**
- [ ] Nenhum fator alto, evolução de produto → **A**

Categoria atribuída: ____ Responsável: ____ Data: ____

## CL02 Definição de preparado

Um item entra na iteração somente com todos os itens marcados.

- [ ] Tem descrição do problema e do resultado esperado
- [ ] Tem critérios de aceite escritos e verificáveis, incluindo ao menos um caso de erro
- [ ] Tem categoria atribuída e tag do problema de origem
- [ ] Tem dependências externas identificadas e resolvidas ou com data
- [ ] Cabe em uma iteração, ou foi dividido até caber

## CL03 Definição de pronto

Um item sai da iteração somente com todos os itens marcados.

- [ ] Atende a todos os critérios de aceite
- [ ] Tem teste automatizado cobrindo o caminho principal e os casos de erro previstos
- [ ] Passou por revisão de código de ao menos um par (CL08)
- [ ] Passou na análise estática e na análise de dependências vulneráveis, sem achado crítico
- [ ] Está vinculado ao requisito de origem na matriz de rastreabilidade
- [ ] Está implantado no ambiente de homologação

## CL04 Gate G1, aprovação de concepção

**Critérios de entrada**, verificados pelo GP antes de agendar o gate

- [ ] Documento de visão (A01) publicado com todas as seções preenchidas
- [ ] Estimativa de ordem de grandeza registrada em faixa, com premissas
- [ ] Riscos iniciais registrados no A15
- [ ] Na categoria B, termo de abertura (A02) redigido

**Critérios de saída**, verificados na reunião

- [ ] Escopo macro aceito pelo cliente ou pelo PO
- [ ] Riscos de severidade alta com resposta definida
- [ ] Categoria confirmada pelo EP após o entendimento do escopo
- [ ] Decisão registrada pelo CTO no Épico, com data e participantes

## CL05 Gate G2, baseline de arquitetura

**Critérios de entrada**

- [ ] Especificação de requisitos do núcleo (A04) publicada e validada
- [ ] Documento de arquitetura com ADRs das decisões relevantes (A06)
- [ ] Avaliação de risco de segurança concluída com parecer do DPO (A07)
- [ ] Na categoria C, relatório de ameaças (A08) concluído
- [ ] Plano de testes (A09) aprovado pelo PO

**Critérios de saída**

- [ ] Arquitetura aprovada pelo CTO, com recomendação do ARQ
- [ ] Riscos técnicos de maior severidade mitigados ou aceitos formalmente
- [ ] Plano de release com marcos e estimativa refinada (A12)
- [ ] Matriz de rastreabilidade com requisitos do núcleo ligados ao escopo (A05)
- [ ] Linha de base do escopo congelada pelo GP

## CL06 Gate G3, prontidão para release

**Critérios de entrada**

- [ ] Todos os itens do release atendem à definição de pronto (CL03)
- [ ] Plano de rollback escrito e testado em homologação (A12)
- [ ] Verificação de segurança do nível da categoria concluída (CL09)
- [ ] Evidência de teste publicada (A10)

**Critérios de saída**

- [ ] Plano de release aprovado pelo PO
- [ ] Nenhum defeito de severidade crítica em aberto
- [ ] Janela e comunicação acordadas com Suporte e, quando aplicável, com o cliente
- [ ] Aprovação registrada pelo SRE no estágio de produção do pipeline

## CL07 Gate G4, aceite

**Critérios de entrada**

- [ ] Implantação concluída e monitorada por cinco dias úteis
- [ ] Registro de homologação aprovado pelo cliente
- [ ] Indicadores de estabilização dentro do esperado
- [ ] Na categoria C, teste de intrusão (A11) sem achado crítico em aberto

**Critérios de saída**

- [ ] Termo de aceite (A14) assinado pelo cliente
- [ ] Documentação de operação entregue ao Suporte em sessão de repasse
- [ ] Lições aprendidas registradas (A17)
- [ ] Épico fechado no Boards

## CL08 Revisão de código

- [ ] A mudança atende ao critério de aceite do item vinculado
- [ ] O código é legível sem explicação do autor
- [ ] Há teste automatizado para o caminho principal e para os erros previstos, e o teste falharia sem a mudança
- [ ] Entradas externas são validadas e saídas são codificadas
- [ ] Nenhum segredo, senha ou dado pessoal real aparece no código, nos testes ou nos logs
- [ ] Consultas ao banco usam parâmetros, sem concatenação de texto
- [ ] Erros são tratados sem expor detalhes internos ao usuário
- [ ] Mudança em integração, modelo de dados ou autenticação tem também o ARQ ou o SEC como revisor
- [ ] Decisão de arquitetura nova está registrada em ADR

## CL09 Verificação de segurança por categoria

| Verificação | A | B | C | D |
| --- | --- | --- | --- | --- |
| Nível ASVS mínimo | 1 | 2 | 2 | 1 |
| Análise estática e de dependências no pipeline | Sim | Sim | Sim | Sim |
| Avaliação de risco de segurança e privacidade (A07) | Recomendada | Sim | Sim | Recomendada |
| Modelagem de ameaças (A08) | Não | Recomendada | Sim | Não |
| Verificação manual dos requisitos ASVS selecionados | Não | Por release | Por iteração | Não |
| Teste de intrusão antes do go-live (A11) | Não | Recomendado | Sim | Não |
| Parecer do encarregado de dados | Quando houver dado pessoal | Sim | Sim | Quando houver dado pessoal |

**Para cada release**

- [ ] Pipeline sem achado crítico da análise estática e de dependências
- [ ] Achados altos corrigidos ou aceitos com justificativa do SEC
- [ ] Requisitos ASVS do nível da categoria verificados conforme a tabela
- [ ] A07 atualizado se um achado revelou risco não previsto

## CL10 Solicitação de desvio

- [ ] Elemento obrigatório a dispensar, com referência à Matriz de Customização
- [ ] Projeto, categoria e work item
- [ ] Motivo do desvio
- [ ] Risco assumido e como será mitigado
- [ ] Precedentes de desvio do mesmo elemento na mesma categoria, levantados pelo EP
- [ ] Instrução do EP registrada em até dois dias úteis
- [ ] Decisão do CTO registrada em até três dias úteis
