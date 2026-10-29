---
toc_max_heading_level: 2
sidebar_position: 2
---

# Concepção

Obrigatória nas categorias B e C. O objetivo é entender o problema e delimitar o escopo antes de qualquer compromisso de prazo. Duração típica de uma a três semanas.

Na Concepção, quem conduz as atividades depende da origem da demanda. Em projeto contratado (categoria B, ou C vinculada a contrato), é o gerente de projeto. Em módulo crítico de produto (categoria C sem contrato), é o Product Owner do produto. A regra está na decisão DB03 em [Evolução e Roadmap](../Evolucao-e-Roadmap.md). Por simplicidade, as tabelas abaixo usam GP para esse condutor.

## AT02 Levantar necessidade e stakeholders

| Campo | Conteúdo |
| --- | --- |
| Propósito | Entender a dor real do cliente ou da operação e quem será afetado pela iniciativa |
| Categorias | B e C obrigatória, A recomendada para iniciativas acima de uma iteração |
| Gatilho | Work item classificado em B ou C e encaminhado à Concepção |
| Entradas | Work item da AT01, contrato ou proposta preliminar, histórico de chamados do cliente |
| Saídas | Seções Problema, Oportunidade e Stakeholders do A01 Documento de visão |
| Papéis | R e A GP, C PO, ARQ e SUP, I CTO |
| Ferramentas | Azure Wiki (página do projeto), ferramenta de chamados (consulta ao histórico) |
| Instrumento de apoio | [Template A01](../Templates.md#a01-documento-de-visão) |
| Critério de conclusão | Problema descrito com evidência e stakeholders listados com interesse e influência |
| Problemas atendidos | P02, P03 |

### Passos

1. Criar a página do projeto na Wiki a partir do template A01
2. Conduzir ao menos uma reunião com o solicitante e uma com o usuário final, quando forem pessoas diferentes
3. Consultar o Suporte sobre chamados recentes do cliente ou do módulo, para identificar dores já conhecidas
4. Registrar o problema com a evidência que o sustenta, como volume de chamados, prazo legal ou perda financeira
5. Listar os stakeholders, com interesse e influência de cada um

## AT03 Definir escopo macro

| Campo | Conteúdo |
| --- | --- |
| Propósito | Delimitar o que está dentro e fora da iniciativa antes de estimar |
| Categorias | B e C obrigatória |
| Gatilho | AT02 concluída |
| Entradas | A01 com problema e stakeholders |
| Saídas | Seções Escopo macro e Critérios de sucesso do A01; A02 Termo de abertura na categoria B; Épico e Features no Boards |
| Papéis | R e A GP, C PO, ARQ e SEC, I CTO |
| Ferramentas | Azure Wiki, Azure Boards (Épico e Features) |
| Instrumento de apoio | [Template A01](../Templates.md#a01-documento-de-visão), [Template A02](../Templates.md#a02-termo-de-abertura-e-contrato-de-escopo) |
| Critério de conclusão | Lista de incluído e excluído validada pelo solicitante e Features criadas no Boards |
| Problemas atendidos | P03, P11 |

### Passos

1. Escrever o escopo como lista de capacidades, cada uma em uma frase, e a lista explícita do que fica de fora
2. Consultar o ARQ sobre dependências técnicas e o SEC sobre o tipo de dado tratado, o que pode confirmar ou alterar a categoria
3. Definir os critérios de sucesso com métrica, valor alvo e prazo de verificação
4. Na categoria B, redigir o A02 com objetivo, escopo, premissas e restrições, que será a base da proposta comercial
5. Criar o Épico e as Features no Boards, com a tag de categoria

## AT04 Estimar ordem de grandeza

| Campo | Conteúdo |
| --- | --- |
| Propósito | Dar uma faixa de esforço confiável o bastante para decidir se a iniciativa segue |
| Categorias | B e C obrigatória |
| Gatilho | AT03 concluída |
| Entradas | Escopo macro, Features no Boards, histórico de projetos semelhantes |
| Saídas | Seção Estimativa de ordem de grandeza do A01; A15 Registro de riscos inicial |
| Papéis | R DEV, A GP, C PO, ARQ e QA, I CTO |
| Ferramentas | Azure Boards (campo de esforço nas Features), Azure Wiki |
| Instrumento de apoio | [Template A15](../Templates.md#a15-registro-de-riscos) |
| Critério de conclusão | Faixa mínima e máxima em pessoas-mês registrada, com premissas e riscos iniciais |
| Problemas atendidos | P03 |

### Passos

1. Estimar cada Feature por analogia com entregas anteriores, em faixa de pessoas-mês e nunca em valor único
2. Registrar as premissas da estimativa, como disponibilidade do cliente, integrações existentes e volume de dados
3. Levantar os riscos iniciais no A15, com probabilidade, impacto e resposta proposta
4. Somar as faixas e aplicar margem proporcional aos riscos de severidade alta
5. Quando a faixa máxima passar o dobro da mínima, registrar o motivo e o que a Elaboração precisa esclarecer

A estimativa em pontos de história foi deliberadamente não adotada, como registrado em [Práticas Adotadas e Origem](../../02-Estrutura-do-Processo/Praticas-Adotadas-e-Origem.md).

## AT05 Conduzir o gate G1

| Campo | Conteúdo |
| --- | --- |
| Propósito | Decidir formalmente se a iniciativa segue para a Elaboração, antes de qualquer proposta com prazo |
| Categorias | B e C obrigatória |
| Gatilho | AT02, AT03 e AT04 concluídas |
| Entradas | A01 completo, A02 na categoria B, A15 inicial |
| Saídas | Decisão de G1 registrada no Épico (aprovado, reprovado com retorno à AT03 ou encerrado); categoria confirmada |
| Papéis | R GP, A CTO, C PO, EP e ARQ |
| Ferramentas | Azure Boards (campo de estado do gate no Épico), Azure Wiki |
| Instrumento de apoio | [CL04 Checklist do gate G1](../Checklists.md#cl04-gate-g1-aprovação-de-concepção) |
| Critério de conclusão | Todos os itens do CL04 marcados e decisão do CTO registrada |
| Problemas atendidos | P03, P11 |

### Passos

1. O GP verifica o CL04 e só agenda a reunião de gate com todos os critérios de entrada atendidos
2. O GP apresenta escopo, estimativa e riscos em até 30 minutos
3. O EP confirma a categoria à luz do escopo entendido
4. O CTO decide e o GP registra a decisão, a data e os participantes no Épico
5. Com o G1 aprovado na categoria B, o Comercial pode emitir proposta com prazo. Sem G1 aprovado, nenhuma proposta com prazo pode ser emitida

A responsabilidade pelo G1 foi corrigida no Grau B. O Grau A atribuía o A ao GP e ao CTO ao mesmo tempo, contrariando a regra de um único A por atividade. Ver decisão DB01.
