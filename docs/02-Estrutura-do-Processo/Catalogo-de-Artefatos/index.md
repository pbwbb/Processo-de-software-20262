---
---

# Catálogo de Artefatos

Dezoito artefatos compõem o processo. O A18 foi incluído no Grau B pela decisão DB06. A obrigatoriedade de cada um varia por categoria, conforme a [Matriz de Customização](../Matriz-de-Customizacao.md). Os modelos estão em [Templates](./Templates.md).

| ID | Artefato | Propósito | Fase | Autor | Revisor | Onde fica |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Documento de visão | Registrar problema, escopo macro, stakeholders e critérios de sucesso | Concepção | Gerente de projeto, ou Product Owner em módulo de produto | CTO, no gate G1 | Wiki |
| A02 | Termo de abertura e contrato de escopo | Formalizar objetivo, escopo, premissas e restrições do projeto contratado | Concepção | Gerente de projeto | CTO e cliente | Wiki e repositório contratual |
| A03 | Backlog com critérios de aceite | Registrar o que será construído e como será verificado | Todas | Product Owner | Analista de qualidade | Azure Boards |
| A04 | Especificação de requisitos | Detalhar regras de negócio, fluxos e restrições do núcleo | Elaboração | Analista de qualidade | Arquiteto | Wiki |
| A05 | Matriz de rastreabilidade | Ligar origem da demanda, requisito, implementação e teste | Todas | Analista de qualidade | Engenheiro de processo | Wiki e links do Boards |
| A06 | Documento de arquitetura e registros de decisão | Registrar a arquitetura e a razão de cada decisão relevante | Elaboração | Arquiteto | CTO | Wiki e repositório |
| A07 | Avaliação de risco de segurança e privacidade | Identificar dado tratado, risco e controles necessários | Elaboração | Security champion | Encarregado de dados | Wiki |
| A08 | Relatório de ameaças e contramedidas | Registrar a modelagem de ameaças e as contramedidas adotadas | Elaboração | Security champion | Núcleo de segurança | Wiki |
| A09 | Plano de testes | Definir estratégia, níveis, ambientes e critérios de saída do teste | Elaboração | Analista de qualidade | Product Owner | Azure Test Plans |
| A10 | Evidência de teste automatizado | Comprovar que o incremento foi verificado | Construção | Desenvolvedor | Analista de qualidade | Azure Pipelines |
| A11 | Teste de intrusão antes do go-live | Verificar a aplicação por avaliação externa ou interna independente | Transição | Núcleo de segurança | CTO | Wiki com acesso restrito |
| A12 | Plano de release e de rollback | Definir conteúdo, janela, sequência e caminho de reversão | Construção | Engenheiro de confiabilidade | Product Owner | Wiki e Pipelines |
| A13 | Plano de implantação e migração de dados | Detalhar passos, dados migrados, validação e plano de contingência | Transição | Engenheiro de confiabilidade | Gerente de projeto | Wiki |
| A14 | Termo de aceite do cliente | Registrar o aceite formal da entrega | Transição | Gerente de projeto | Cliente | Repositório contratual |
| A15 | Registro de riscos | Listar risco, probabilidade, impacto e resposta | Todas | Gerente de projeto ou Product Owner | Engenheiro de processo | Wiki |
| A16 | Procedimento de controle de mudanças | Registrar solicitação, análise de impacto e decisão | Todas as fases dos contratos | Gerente de projeto | Cliente | Wiki e Boards |
| A17 | Retrospectiva e lições aprendidas | Registrar o que manter, o que mudar e a ação acordada | Construção e encerramento | Equipe | Engenheiro de processo | Wiki |
| A18 | Registro de experimento | Registrar hipótese, critério de sucesso, resultado e aprendizado de um experimento | Ciclo exploratório | Desenvolvedor | Arquiteto | Wiki |

## Regras comuns a todos os artefatos

1. Todo artefato vive na Wiki ou em uma ferramenta do Azure DevOps, nunca em pasta compartilhada. Essa regra responde a P07, porque a evidência precisa estar localizável no momento da auditoria
2. Todo artefato tem autor identificado e data da última revisão
3. Todo artefato que registre decisão de processo aponta o problema numerado que a motivou
4. Artefatos com dado pessoal sensível ficam em páginas de acesso restrito, com permissão concedida por grupo e revisada semestralmente
5. Um artefato desatualizado em mais de dois releases é sinalizado pelo engenheiro de processo na revisão trimestral

## Artefatos por fase

| Fase | Artefatos produzidos |
| --- | --- |
| Entrada | A03 |
| Concepção | A01, A02, A15 |
| Elaboração | A04, A05, A06, A07, A08, A09 |
| Construção | A10, A12, A17 |
| Transição | A11, A13, A14 |
| Operação | A15 atualizado, A17 |
| Transversal | A05, A15, A16 |
| Ciclo exploratório | A18 |
