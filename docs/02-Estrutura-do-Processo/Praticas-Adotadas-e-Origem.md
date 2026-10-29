---
sidebar_position: 8
---

# Práticas Adotadas e Origem

O processo incorpora práticas de sete origens. Nenhuma foi adotada integralmente, e cada adaptação tem razão ligada ao contexto da Vértice.

| Origem | Prática adotada | Adaptação feita | Justificativa | Problemas atendidos |
| --- | --- | --- | --- | --- |
| Scrum | Iteração de duas semanas, backlog priorizado, planning, review e retrospectiva | Papel de Scrum Master não é criado, e a facilitação fica com o squad lead | Quatro squads já operam assim e a empresa não tem orçamento para um papel dedicado por squad | P01, P04 |
| Scrum | Definição de pronto e definição de preparado | Tornadas obrigatórias e padronizadas pela organização, não por squad | A ausência desses acordos é o que torna as cerimônias atuais decorativas | P02, P04 |
| Processo Unificado | Fases de concepção, elaboração, construção e transição com marcos | Reduzido a quatro gates com critérios objetivos, sem as nove disciplinas originais | O valor buscado é o controle de escopo antes do compromisso, não o aparato completo do método | P03, P11 |
| Processo Unificado | Arquitetura como artefato de primeira classe, validada na elaboração | Substituída a documentação extensa por registros de decisão curtos | Dois seniores já decidem arquitetura sem registro, e o custo de documentação pesada seria rejeitado | P09 |
| Kanban | Fluxo contínuo, quadro visual, limite de trabalho em progresso e política explícita de priorização | Aplicado apenas à categoria D, com reserva fixa de capacidade | O problema é a demanda não planejada, que não existe nas demais categorias | P08 |
| DevOps e entrega contínua | Integração contínua, pipeline automatizado, plano de rollback e critério de prontidão | Implantação assistida mantida nas instalações dedicadas do Autoriza | Doze operadoras em ambiente próprio não comportam entrega totalmente automatizada no curto prazo | P05 |
| OWASP SAMM | Segurança distribuída pelo ciclo, com security champion por equipe | Adotados os domínios de projeto e verificação, deixando governança e operação para um segundo momento | O núcleo de segurança tem duas pessoas, e ampliar o escopo de uma vez tornaria a prática simbólica | P06 |
| OWASP ASVS | Requisitos de segurança verificáveis por nível | Nível 1 como padrão e nível 2 nas categorias B e C | Proporciona esforço ao risco em vez de aplicar o mesmo rigor a tudo | P06 |
| ITIL | Gestão de incidentes, problemas e mudanças na operação | Adotado o vocabulário e o fluxo de incidente, sem a estrutura completa de gerenciamento de serviços | Suporte e operadoras já usam esses termos nos contratos de SLA | P07, P08 |
| MPS.BR nível F | Gerência de requisitos, gerência de configuração, medição e garantia da qualidade como processos institucionais | Usado como referência de completude, sem buscar avaliação oficial | Modelo nacional reconhecido pelas operadoras e adequado ao porte da empresa | P02, P07, P10 |

## Práticas deliberadamente não adotadas

| Prática | Por que foi descartada |
| --- | --- |
| Estimativa em pontos de história com velocidade por squad | A empresa não tem histórico de medição, e a técnica exigiria dois trimestres de coleta antes de produzir previsão útil |
| SAFe ou outro framework de escala | Seis squads com 40 pessoas não justificam a sobrecarga de coordenação do método |
| Documentação completa de requisitos antes da construção | Inviabilizaria a cadência quinzenal do Vértice Care, que responde por 55% da receita |
| Avaliação formal MPS.BR ou CMMI no primeiro ano | O custo e o prazo da avaliação competiriam com a própria adoção do processo |
| Entrega contínua totalmente automatizada em todos os produtos | As doze instalações dedicadas do Autoriza têm janelas negociadas com cada operadora |

## Como a combinação se sustenta

As origens poderiam entrar em conflito, e três regras evitam isso. A primeira é que a estrutura macro vem de uma única fonte, o Processo Unificado, de modo que fases e gates não competem com cerimônias. A segunda é que a cadência interna vem do Scrum e não é interrompida por marcos, já que os gates ficam nas bordas das fases. A terceira é que as práticas de segurança e de serviço entram como atividades dentro das fases existentes, sem criar um fluxo paralelo.

## Contribuição do seminário T1

O seminário da equipe no T1 tratou de Detection-as-Code, a aplicação de práticas de engenharia de software à criação de regras de detecção de ameaças. A análise crítica feita no seminário entrou no processo em dois pontos.

| Prática estudada no T1 | Onde está no processo |
| --- | --- |
| Toda mudança versionada em Git, com histórico e autoria | Branch por item e commit vinculado ao work item, na [AT13](../04-Especificacao-do-Processo/Atividades/Construcao.md#at13-implementar) |
| Revisão por pares via pull request antes de valer | Revisão obrigatória em todas as categorias, na [AT14](../04-Especificacao-do-Processo/Atividades/Construcao.md#at14-revisar-código-do-par) |
| Validação automática a cada mudança | Análise estática e de dependências no pipeline, na [AT16](../04-Especificacao-do-Processo/Atividades/Construcao.md#at16-verificar-segurança-do-incremento) |
| Testes automatizados antes do deploy | Definição de pronto e evidência A10, na [AT15](../04-Especificacao-do-Processo/Atividades/Construcao.md#at15-automatizar-e-executar-testes) |
| Rollback trivial | Plano de rollback testado e gate G3 |
| Documentação viva junto do código | Registros de decisão de arquitetura no repositório, na [AT07](../04-Especificacao-do-Processo/Atividades/Elaboracao.md#at07-definir-arquitetura-e-registrar-decisões) |

O segundo ponto é a forma como o próprio processo é mantido. No Grau B, a documentação passou a viver em um repositório Git, com mudança por pull request e verificação automática de consistência antes de cada publicação, como registrado na decisão DB08. O processo é tratado como código, da mesma forma que o seminário propunha para as regras de detecção.
