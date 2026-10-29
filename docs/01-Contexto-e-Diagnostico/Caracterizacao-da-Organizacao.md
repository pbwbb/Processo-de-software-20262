---
sidebar_position: 1
---

# Caracterização da Organização

## Identificação

| Atributo | Valor |
| --- | --- |
| Razão social | Vértice Sistemas Ltda. |
| Fundação | 2009 |
| Sede | Parque tecnológico Tecnosinos, São Leopoldo, Rio Grande do Sul |
| Filial | Escritório comercial em São Paulo |
| Colaboradores | 142, dos quais 86 em tecnologia |
| Receita anual | Aproximadamente R$ 48 milhões |
| Mercado | Saúde suplementar e serviços privados de saúde |

A organização descrita nesta Wiki é fictícia. Os dados foram construídos para o trabalho acadêmico e não representam nenhuma empresa real.

## Modelo de negócio

A receita vem de três fontes. A assinatura mensal do SaaS Vértice Care responde por cerca de 55% do faturamento, os contratos de licença e manutenção do Vértice Autoriza por 30% e os projetos de implantação e customização pelos 15% restantes. Essa composição explica a tensão central do contexto, porque a maior parte da receita exige cadência alta enquanto a maior parte do risco contratual está concentrada na menor delas.

## Clientes

| Perfil | Quantidade | Produto consumido |
| --- | --- | --- |
| Clínicas e consultórios | 310 assinantes | Vértice Care |
| Hospitais privados de pequeno porte | 18 | Vértice Care com módulos adicionais |
| Operadoras de planos de saúde | 12 | Vértice Autoriza em instalação dedicada |

## Tecnologia

| Camada | Tecnologia em uso |
| --- | --- |
| Back-end | Java com Spring Boot nos módulos novos, .NET Framework no legado de faturamento |
| Front-end | React nos produtos atuais, páginas em JSF em módulos antigos do Autoriza |
| Dados | PostgreSQL no Care, SQL Server no Autoriza |
| Infraestrutura | Azure, com máquinas virtuais no Autoriza e containers no Care |
| Ferramentas | Azure DevOps para repositório e board, planilhas para requisitos, ferramenta própria de chamados |

O Azure DevOps já é pago e está subutilizado, servindo hoje apenas como repositório Git e, em dois squads, como quadro informal de tarefas.

## Exigências externas

A atuação em saúde suplementar impõe três conjuntos de obrigações que qualquer processo precisa acomodar.

1. Padrão TISS da ANS, que define o formato de troca de informação entre prestadores e operadoras e muda por versão publicada
2. LGPD, que trata dado de saúde como dado pessoal sensível e exige registro de tratamento, controle de acesso e resposta a incidente
3. Cláusulas contratuais das operadoras, que pedem evidência de ciclo de vida, de teste e de controle de acesso em auditorias periódicas

## Por que esta organização serve ao trabalho

O portfólio reúne quatro naturezas de trabalho que exigem graus de formalidade diferentes, o que torna a definição de categorias de projeto uma necessidade real do contexto. Detalhamento em [Tipos de Software e Projetos](./Tipos-de-Software-e-Projetos.md).
