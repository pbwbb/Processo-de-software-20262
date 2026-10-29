---
sidebar_position: 5
---

# Templates

Modelos de todos os artefatos do catálogo, prontos para copiar. O botão de cópia aparece ao passar o mouse sobre cada bloco. Todos os modelos também podem ser baixados de uma vez no pacote [modelos-pvd.zip](/modelos/modelos-pvd.zip).

## O que mudou em relação ao Grau A

| Mudança | Motivo |
| --- | --- |
| De 10 para 18 modelos, cobrindo todo o catálogo | O Grau A tinha modelo só para parte dos artefatos obrigatórios. A02, A04, A13 e A14 são obrigatórios nas categorias B e C e A08 e A11 na categoria C, e estavam sem modelo |
| Cabeçalho comum em todos os modelos | Cumpre as regras 2 e 3 do [Catálogo de Artefatos](../02-Estrutura-do-Processo/Catalogo-de-Artefatos/index.md), que exigem autor, data de revisão e problema de origem |
| Instrução de preenchimento em cada modelo | O modelo indica quem preenche, em que atividade e o que é obrigatório |
| A18 Registro de experimento | A categoria E citava dois artefatos que não existiam no catálogo. Decisão DB06 |

## Cabeçalho comum

Todo artefato publicado na Wiki começa com este bloco.

```markdown
| Campo | Valor |
| --- | --- |
| Artefato | <ID e nome, por exemplo A01 Documento de visão> |
| Projeto ou produto | <nome> |
| Work item | <ID do Épico ou da Feature no Boards> |
| Categoria | <A, B, C, D ou E> |
| Autor | <nome e papel> |
| Revisor | <nome e papel> |
| Versão | <número> |
| Última revisão | <data> |
| Problema de origem | <P01 a P11, quando aplicável> |
```

## Índice

| ID | Modelo | Atividade | Obrigatório em |
| --- | --- | --- | --- |
| A01 | [Documento de visão](#a01-documento-de-visão) | AT02, AT03, AT04 | B, C |
| A02 | [Termo de abertura e contrato de escopo](#a02-termo-de-abertura-e-contrato-de-escopo) | AT03 | B, C |
| A03 | [Item de backlog](#a03-item-de-backlog) | AT01, AT06 | A, B, C, D |
| A04 | [Especificação de requisitos](#a04-especificação-de-requisitos) | AT06 | B, C |
| A05 | [Matriz de rastreabilidade](#a05-matriz-de-rastreabilidade) | AT06, AT15 | B, C |
| A06 | [Registro de decisão de arquitetura](#a06-registro-de-decisão-de-arquitetura) | AT07 | B, C |
| A07 | [Avaliação de risco de segurança e privacidade](#a07-avaliação-de-risco-de-segurança-e-privacidade) | AT08 | B, C |
| A08 | [Relatório de ameaças e contramedidas](#a08-relatório-de-ameaças-e-contramedidas) | AT08 | C |
| A09 | [Plano de testes](#a09-plano-de-testes) | AT09 | B, C |
| A10 | [Evidência de teste automatizado](#a10-evidência-de-teste-automatizado) | AT15 | A, B, C, D |
| A11 | [Relatório de teste de intrusão](#a11-relatório-de-teste-de-intrusão) | AT19 | C |
| A12 | [Plano de release e de rollback](#a12-plano-de-release-e-de-rollback) | AT10 | A, B, C, D |
| A13 | [Plano de implantação e migração de dados](#a13-plano-de-implantação-e-migração-de-dados) | AT20 | B, C |
| A14 | [Termo de aceite do cliente](#a14-termo-de-aceite-do-cliente) | AT21 | B, C |
| A15 | [Registro de riscos](#a15-registro-de-riscos) | AT04 e todas as fases | B, C |
| A16 | [Solicitação de mudança](#a16-solicitação-de-mudança) | AT24 | B, C |
| A17 | [Retrospectiva](#a17-retrospectiva) | AT17, AT21 | A, B, C |
| A18 | [Registro de experimento](#a18-registro-de-experimento) | AT28 | E |

## A01 Documento de visão

Preenchido pelo GP, ou pelo PO em módulo de produto, ao longo das atividades AT02 a AT04. Todas as seções são obrigatórias para o gate G1.

```markdown
# Visão, <nome da iniciativa>

<cabeçalho comum>

## Problema
Qual dor do cliente ou da operação motiva esta iniciativa, com a evidência que a sustenta.

## Oportunidade
O que a Vértice ganha ao resolver.

## Stakeholders
| Stakeholder | Interesse | Influência |
| --- | --- | --- |

## Escopo macro
### Incluído
- <capacidade, em uma frase>
### Excluído
- <o que deliberadamente fica de fora>

## Critérios de sucesso
| Métrica | Valor alvo | Prazo de verificação |
| --- | --- | --- |

## Riscos iniciais
Ver A15 Registro de riscos do projeto.

## Estimativa de ordem de grandeza
| Feature | Mínimo (pessoas-mês) | Máximo (pessoas-mês) |
| --- | --- | --- |
| Total | | |

Premissas usadas:
- <premissa>

## Categoria proposta
| Fator | Nível | Justificativa |
| --- | --- | --- |
| Sensibilidade do dado | | |
| Obrigação contratual | | |
| Exigência regulatória | | |
| Esforço estimado | | |
| Reversibilidade | | |

Categoria resultante: <A, B, C, D ou E>
```

## A02 Termo de abertura e contrato de escopo

Preenchido pelo GP na AT03, somente em projeto contratado. Serve de base para a proposta comercial, que só é emitida com o G1 aprovado.

```markdown
# Termo de abertura, <nome do projeto>

<cabeçalho comum>

## Cliente
Razão social, contato responsável e quem assina pelo cliente.

## Objetivo
O resultado de negócio esperado, em uma ou duas frases.

## Escopo contratado
| ID | Entrega | Critério de aceite resumido |
| --- | --- | --- |

## Fora do escopo
- <item explicitamente excluído>

## Premissas
- <condição que o cliente deve garantir, como acesso a ambiente ou dados>

## Restrições
- <prazo legal, janela de implantação, tecnologia imposta>

## Tolerância para mudança
Variação de escopo aprovada pelo GP sem aditivo, em horas ou percentual do contrato. Acima disso, vale o procedimento A16 com aditivo.

## Marcos
| Marco | Data prevista | Gate associado |
| --- | --- | --- |

## Aprovação
| Papel | Nome | Data |
| --- | --- | --- |
| Gerente de projeto | | |
| CTO | | |
| Cliente | | |
```

## A03 Item de backlog

Escrito pelo PO e refinado com o QA. Um item só entra na iteração se passar pelo [CL02 Definição de preparado](./Checklists.md#cl02-definição-de-preparado).

```markdown
**Como** <papel do usuário>
**quero** <capacidade>
**para que** <benefício>.

### Critérios de aceite
- Dado <contexto>, quando <ação>, então <resultado verificável>
- Dado <contexto>, quando <ação de erro>, então <tratamento esperado>

### Problema de origem
P<NN>

### Categoria
<A, B, C, D ou E>

### Dependências externas
- <sistema, equipe ou cliente de quem o item depende>
```

## A04 Especificação de requisitos

Escrita pelo QA na AT06 e validada pelo PO e, na categoria B, pelo cliente. Cobre apenas o núcleo da solução. O restante é detalhado item a item durante a Construção.

```markdown
# Especificação de requisitos, <nome da iniciativa>

<cabeçalho comum>

## Contexto
Resumo do problema e referência ao A01.

## Atores
| Ator | Descrição | Perfil de acesso |
| --- | --- | --- |

## Requisitos funcionais do núcleo
### RF<NN> <nome>
- **Feature:** <ID no Boards>
- **Descrição:** <o que o sistema deve fazer>
- **Regras de negócio:** <RN<NN>, uma por linha>
- **Fluxo principal:** <passos numerados>
- **Fluxos de erro:** <passos numerados>
- **Critérios de aceite:** <Dado, quando, então>

## Regras de negócio
| ID | Regra | Fonte (contrato, norma ANS, TISS, LGPD) |
| --- | --- | --- |

## Requisitos não funcionais
| ID | Categoria | Requisito | Como será verificado |
| --- | --- | --- | --- |
| RNF01 | Desempenho | | |
| RNF02 | Segurança | <requisito ASVS selecionado na AT08> | |
| RNF03 | Privacidade | | |

## Integrações
| Sistema | Direção | Formato | Responsável do outro lado |
| --- | --- | --- | --- |

## Questões em aberto
| Questão | Responsável | Prazo |
| --- | --- | --- |
```

## A05 Matriz de rastreabilidade

Mantida pelo QA desde a AT06. Cada linha liga a origem da demanda ao teste que a verifica. O vínculo de commit e pull request é feito automaticamente pelo Boards quando a mensagem cita o work item.

```markdown
| Requisito | Origem | Work item | Commit ou PR | Caso de teste | Status |
| --- | --- | --- | --- | --- | --- |
| RF01 | P02 / Feature 1234 | 1301 | PR 88 | TC 455 | Verificado |
```

## A06 Registro de decisão de arquitetura

Escrito pelo DEV e aprovado pelo ARQ na AT07. Um arquivo por decisão, guardado no repositório em `docs/adr`.

```markdown
# ADR <NNN>, <título da decisão>

**Status** proposta, aceita ou substituída por ADR <NNN>
**Data**
**Decisores**

## Contexto
Situação técnica e restrições que forçaram a decisão.

## Decisão
O que foi decidido, em uma frase.

## Alternativas consideradas
| Alternativa | Vantagem | Por que foi descartada |
| --- | --- | --- |

## Consequências
O que passa a ser verdade, incluindo o custo aceito.
```

## A07 Avaliação de risco de segurança e privacidade

Conduzida pelo SEC e aprovada pelo DPO na AT08. Publicada em página de acesso restrito.

```markdown
# Avaliação de risco, <nome da iniciativa>

<cabeçalho comum>

## Dados tratados
| Dado | Classificação | Base legal | Retenção |
| --- | --- | --- | --- |

## Superfície exposta
Interfaces, integrações e perfis de acesso.

## Riscos identificados
| Risco | Probabilidade | Impacto | Controle adotado | Responsável |
| --- | --- | --- | --- | --- |

## Requisitos de segurança aplicáveis
Nível ASVS exigido pela categoria: <1 ou 2>
| Requisito ASVS | Item de backlog |
| --- | --- |

## Parecer do encarregado de dados
Aprovado, aprovado com condições ou reprovado, com justificativa, nome e data.
```

## A08 Relatório de ameaças e contramedidas

Produzido pelo SEC na sessão de modelagem de ameaças da AT08. Obrigatório na categoria C.

```markdown
# Modelagem de ameaças, <nome da iniciativa>

<cabeçalho comum>

## Escopo da modelagem
Componentes e fluxos de dados analisados, com referência ao diagrama do A06.

## Participantes
| Nome | Papel |
| --- | --- |

## Ameaças identificadas (STRIDE)
| ID | Componente | Categoria STRIDE | Ameaça | Probabilidade | Impacto | Contramedida | Item de backlog |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | | Spoofing | | | | | |

## Riscos aceitos
| ID | Justificativa | Aceito por (CTO) | Data |
| --- | --- | --- | --- |

## Revisão
Data prevista para revisar a modelagem, que deve ser refeita quando a arquitetura mudar.
```

## A09 Plano de testes

Escrito pelo QA na AT09 e aprovado pelo PO. As suítes correspondentes ficam no Azure Test Plans.

```markdown
# Plano de testes, <nome da iniciativa>

<cabeçalho comum>

## Estratégia
| Nível | O que verifica | Proporção automatizada | Quem executa |
| --- | --- | --- | --- |
| Unitário | | | DEV |
| Integração | | | DEV |
| Aceitação | | | QA |
| Exploratório | | Manual | QA |
| Segurança | <requisitos do A07> | | DEV e SEC |

## Escopo
O que será testado e o que foi deliberadamente deixado de fora.

## Ambientes e massa de dados
Como a massa é gerada e como o dado pessoal é anonimizado.

## Critérios de saída
| Critério | Valor exigido |
| --- | --- |
| Caminho principal coberto por teste automatizado | 100% dos itens |
| Defeito crítico em aberto | Nenhum |

## Riscos de teste
| Risco | Resposta |
| --- | --- |
```

## A10 Evidência de teste automatizado

Gerada pelo pipeline na AT15. O registro abaixo é anexado ao release quando a evidência precisa sair do Azure DevOps, como em auditoria de cliente.

```markdown
# Evidência de teste, release <versão>

<cabeçalho comum>

## Execução
| Campo | Valor |
| --- | --- |
| Pipeline e execução | <nome e número do run> |
| Commit | <hash> |
| Data | |
| Ambiente | Homologação |

## Resultado
| Suíte | Casos executados | Aprovados | Falhos | Cobertura de linhas |
| --- | --- | --- | --- | --- |
| Unitários | | | | |
| Integração | | | | |
| Aceitação | | | | |

## Análise estática e de dependências
| Ferramenta | Achados críticos | Achados altos | Portão de qualidade |
| --- | --- | --- | --- |
| SonarQube | | | Aprovado ou reprovado |
| Trivy | | | |

## Falhas e tratamento
| Caso | Defeito registrado | Decisão |
| --- | --- | --- |
```

## A11 Relatório de teste de intrusão

Produzido pelo núcleo de segurança, ou por avaliador externo, durante a AT19. Obrigatório na categoria C antes da implantação em produção. Acesso restrito.

```markdown
# Teste de intrusão, <aplicação e versão>

<cabeçalho comum>

## Escopo e regras de engajamento
Alvos, ambiente, janela, técnicas permitidas e excluídas.

## Metodologia
Referência usada, como OWASP Web Security Testing Guide, e nível ASVS verificado.

## Resumo executivo
| Severidade | Quantidade | Corrigidos antes do go-live |
| --- | --- | --- |
| Crítica | | |
| Alta | | |
| Média | | |
| Baixa | | |

## Achados
### V<NN> <título>
- **Severidade:** <crítica, alta, média ou baixa, com CVSS>
- **Componente afetado:**
- **Descrição e evidência:**
- **Recomendação:**
- **Item de backlog:**
- **Status:** aberto, corrigido ou risco aceito

## Conclusão
Liberado ou não liberado para produção, com nome e data.
```

## A12 Plano de release e de rollback

Escrito pelo SRE na AT10 e aprovado pelo PO. Verificado no gate G3.

```markdown
# Release <versão>

<cabeçalho comum>

## Conteúdo
| Item | Work item | Categoria |
| --- | --- | --- |

## Janela e comunicação
Data, duração estimada e quem é avisado, com antecedência.

## Sequência de implantação
1.

## Verificações pós-implantação
| Verificação | Resultado esperado | Responsável |
| --- | --- | --- |

## Plano de rollback
- **Gatilho de acionamento:** <condição objetiva, como taxa de erro acima de X% por Y minutos>
- **Passos:**
- **Tempo máximo de reversão:**
- **Testado em homologação em:** <data>
```

## A13 Plano de implantação e migração de dados

Escrito pelo SRE na preparação da AT20, com apoio do DEV do squad responsável. Obrigatório nas categorias B e C.

```markdown
# Plano de implantação, <projeto> no cliente <nome>

<cabeçalho comum>

## Ambiente de destino
Infraestrutura do cliente, versões, acessos necessários e contato técnico da operadora.

## Pré-requisitos
| Pré-requisito | Responsável | Status |
| --- | --- | --- |

## Migração de dados
| Origem | Destino | Volume | Transformação | Validação |
| --- | --- | --- | --- | --- |

Ensaio em homologação realizado em <data>, com duração de <tempo>.

## Roteiro de implantação
| Passo | Ação | Responsável | Duração | Verificação |
| --- | --- | --- | --- | --- |

## Contingência
Gatilho para abortar, passos de reversão e como os dados voltam ao estado anterior.

## Treinamento
| Público | Conteúdo | Data | Material |
| --- | --- | --- | --- |

## Estabilização
Indicadores monitorados durante cinco dias úteis e valores esperados.
```

## A14 Termo de aceite do cliente

Emitido pelo GP no gate G4 e assinado pelo cliente. Arquivado no repositório contratual.

```markdown
# Termo de aceite, <projeto>

<cabeçalho comum>

## Identificação
Contrato, cliente, período de execução.

## Entregas aceitas
| ID | Entrega | Referência da homologação |
| --- | --- | --- |

## Pendências aceitas
| Pendência | Prazo de resolução | Impacto no aceite |
| --- | --- | --- |

## Declaração
O cliente declara que as entregas acima atendem ao escopo contratado e ao registro de homologação, encerrando a fase de implantação. Correções posteriores seguem o contrato de sustentação.

## Assinaturas
| Parte | Nome | Cargo | Data |
| --- | --- | --- | --- |
| Vértice Sistemas | | Gerente de projeto | |
| Cliente | | | |
```

## A15 Registro de riscos

Iniciado na AT04 e atualizado em todas as fases pelo GP ou PO.

```markdown
| ID | Risco | Probabilidade | Impacto | Severidade | Resposta | Responsável | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | | Baixa, média ou alta | Baixo, médio ou alto | Probabilidade x impacto | Evitar, mitigar, transferir ou aceitar | | Aberto |
```

## A16 Solicitação de mudança

Preenchida pelo solicitante e decidida na AT24. Nenhuma mudança é trabalhada sem este registro.

```markdown
# Solicitação de mudança <NNN>

**Solicitante**
**Data**
**Projeto**

## Mudança pedida
## Motivo
## Análise de impacto
| Dimensão | Impacto |
| --- | --- |
| Escopo | |
| Prazo | |
| Custo | |
| Risco | |

## Decisão
Aprovada, recusada ou aprovada com aditivo. Quem decidiu e quando.

## Linha de base atualizada
Referência à versão do escopo após a mudança.
```

## A17 Retrospectiva

Registrada na AT17, ao fim de cada iteração, e na AT21, como lições aprendidas do projeto.

```markdown
# Retrospectiva, iteração <NN>

| O que funcionou | O que atrapalhou | Decisões | Ação de melhoria |
| --- | --- | --- | --- |

**Ação com responsável e prazo**
**Verificação da ação da iteração anterior** concluída, em andamento ou abandonada, e por quê
**Encaminhado ao engenheiro de processo** <sim ou não, e o quê>
```

## A18 Registro de experimento

Único artefato obrigatório da categoria E, preenchido em duas etapas na AT28: hipótese no início e aprendizado no fim.

```markdown
# Experimento, <título>

<cabeçalho comum>

## Hipótese
Acreditamos que <mudança técnica> resultará em <efeito>.

## Critério de sucesso
Métrica, valor que confirma a hipótese e como será medido.

## Prazo
Início, fim (máximo de quatro semanas).

## Execução
O que foi feito, repositório e ambiente usados.

## Resultado
Valor medido em comparação com o critério.

## Decisão
Seguir, com o ID da nova demanda na fila única, ou abandonar.

## Aprendizado
O que a equipe sabe agora que não sabia antes.
```
