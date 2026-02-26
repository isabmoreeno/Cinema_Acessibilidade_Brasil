# 🎬 Acessibilidade Econômica ao Cinema no Brasil

Projeto de Análise e Ciência de Dados que investiga a acessibilidade econômica ao cinema no Brasil, utilizando dados públicos do IBGE para avaliar a relação entre renda per capita e o custo médio de ingressos de cinema.

---

## 📌 Contexto

O cinema é uma das principais formas de acesso à cultura e ao entretenimento. No entanto, o aumento do custo de vida, aliado às desigualdades socioeconômicas regionais, pode limitar significativamente o acesso da população a esse tipo de lazer.

Diante desse cenário, este projeto busca responder à seguinte pergunta:

> **O cinema é financeiramente acessível para a população brasileira?**

---

## 🎯 Objetivo

Analisar a acessibilidade econômica ao cinema nos municípios e estados do Brasil, com base na renda per capita, criando um indicador capaz de mensurar o impacto do preço do ingresso sobre o orçamento da população.

---

## 🧠 Metodologia

O projeto seguiu as seguintes etapas:

1. **Coleta de Dados**
   - Renda nominal mensal domiciliar per capita por município e estado.
   - Fonte: IBGE – PNAD Contínua (2024).

2. **Tratamento dos Dados**
   - Limpeza, padronização e organização dos dados.
   - Estruturação em planilhas Excel e posterior importação no Python.

3. **Análise Exploratória**
   - Estatísticas descritivas.
   - Rankings nacionais.
   - Visualizações gráficas.

4. **Criação de Indicador**
   - Desenvolvimento do **Índice de Acessibilidade Econômica ao Cinema (IAEC)**.

5. **Visualização e Interpretação**
   - Geração de gráficos e análises interpretativas dos resultados.

---

## 📊 Índice de Acessibilidade Econômica ao Cinema (IAEC)

Foi criado um indicador próprio para medir o impacto do custo do ingresso sobre a renda mensal:

\[
IAEC = \frac{\text{Preço do ingresso}}{\text{Renda per capita}} \times 100
\]

- Preço médio do ingresso considerado: **R$ 35,00**
- O IAEC representa o **percentual da renda mensal gasto em uma única ida ao cinema**.

### Classificação adotada:

| IAEC (%) | Classificação |
|------------|----------------|
| Até 1% | Muito acessível |
| 1% – 2% | Acessível |
| 2% – 3% | Moderadamente caro |
| 3% – 4% | Caro |
| Acima de 4% | Muito caro |

---

## 📈 Principais Análises

- Ranking dos estados com maior e menor acessibilidade ao cinema.
- Ranking dos municípios mais impactados economicamente.
- Distribuição nacional do índice de acessibilidade.
- Classificação dos municípios em faixas de acesso cultural.

---

## 🔍 Principais Descobertas

- Existe uma **grande desigualdade regional** no acesso econômico ao cinema.
- Em diversos municípios brasileiros, **mais de 3% da renda mensal é comprometida com apenas um ingresso**, caracterizando o cinema como um lazer de difícil acesso.
- Regiões com menor renda per capita apresentam **índices significativamente mais altos**, indicando maior exclusão cultural.
- O acesso ao cinema no Brasil ainda é **fortemente condicionado à renda**, reforçando desigualdades sociais.

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Microsoft Excel

---

## 🚀 Possíveis Extensões

- Inclusão de preços reais de ingressos por cidade.
- Análise comparativa entre cinema e plataformas de streaming.
- Criação de dashboards interativos.
- Modelos preditivos para estimar frequência ao cinema.

---

## 👩‍💻 Autora

Isabela Moreno  
Estudante de Análise e Desenvolvimento de Sistemas  
Interesse em Ciência de Dados  
