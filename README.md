# 🍫 Plataforma Analítica "Especial Páscoa 2026.1" - Unifacs

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://unifacspascoa.streamlit.app/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZqJoYa7cHY7HV8fBD7OcQ0jaRsNLDbSd)

## 📌 Visão Geral da Solução
O Dashboard **"Especial Páscoa"** é um Produto Mínimo Viável (MVP) focado na análise preditiva de dados logísticos, macroeconômicos e de suprimentos da indústria de chocolates. 

Construída em Python, a plataforma converte bases de dados brutas em inteligência visual, permitindo monitorar o passado, diagnosticar o presente e prever o futuro dos custos de produção. A aplicação destaca-se por sua interface responsiva, tratamento resiliente de dados temporais e integração ponta a ponta com algoritmos de **Machine Learning**.

---

## 🎯 O Problema de Negócio
A indústria de chocolates enfrenta uma "tempestade perfeita" que ameaça as margens de lucro e a qualidade dos produtos nas prateleiras:
1. **Incerteza Global (Cacau):** O mercado de commodities sofre com guerras, instabilidade no Oriente Médio e choques climáticos (El Niño na África), fazendo o preço do cacau explodir.
2. **O "Custo Brasil":** A flutuação da Taxa Selic encarece o financiamento de estoques, enquanto a alta do Dólar multiplica o risco de importação.
3. **O Paradoxo do Consumo:** Apesar dos altos preços, datas sazonais como a Páscoa possuem demanda inelástica (*"O consumidor reclama, mas compra"*). 

A indústria precisava de um **Sistema de Suporte à Decisão (DSS)** que identificasse matematicamente quando o custo se torna insustentável, forçando a alteração das fórmulas dos produtos (fenômeno da **Skimpflation**).

---

## ⚙️ Arquitetura e Módulos do Sistema

A aplicação foi estruturada em um pipeline de dados completo, dividido nas seguintes frentes:

### 1. Extração e Engenharia de Dados (ETL)
- **APIs Externas:** Consumo automatizado de dados do Yahoo Finance (Cacau, Leite, Açúcar, Soja, Milho, Trigo, Petróleo) e do Banco Central do Brasil - SGS (Dólar, Selic, IPCA de Alimentos).
- **Time Windowing (Lags Temporais):** Criação de variáveis defasadas (6M e 12M atrás) para capturar a *inércia de mercado* — o tempo que um choque no valor do petróleo ou do dólar leva para refletir no frete e chegar às gôndolas.

### 2. Análise Macroeconômica (Dual-Axis)
- Cruzamento de dados de eixo duplo espelhado que prova a correlação entre a Política Monetária (Selic), o Risco Cambial (Dólar) e o controle da Inflação.

### 3. O Gatilho da "Skimpflation" (Alerta Prescritivo)
- Utilização de **Feature Scaling** (`MinMaxScaler`) para colocar insumos de preços discrepantes (Cacau em dólares vs. Leite em reais) na mesma escala (0 a 1).
- Motor de **Thresholding** que acende uma "Zona de Risco" no dashboard sempre que a pressão de custos atinge o quartil de 75% da série histórica, avisando o momento exato em que a margem quebra.

### 4. Machine Learning & Previsão Varejista 2027
- **Treinamento:** Modelo `Random Forest Regressor` treinado para prever a inflação futura com base no histórico consolidado.
- **Transparência Algorítmica:** O modelo possui um $R^2$ de cerca de 87%, assumindo de forma ética e intelectualmente honesta que a variância restante é o ruído imprevisível do mercado.
- **Veredito Automatizado:** A IA projeta o cenário e dita a regra de negócio (Antecipar estoques, Aguardar janela de compra ou Focar em fluxo de caixa).
- **Simulador:** Aplicação da inflação predita sobre um banco de dados de produtos reais (coletados via Web Scraping), projetando preços para a Páscoa de 2027.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Front-end & Deploy:** Streamlit Community Cloud
* **Engenharia de Dados:** Pandas, NumPy, Requests, yFinance
* **Machine Learning:** Scikit-Learn (Random Forest, MinMaxScaler)
* **Visualização:** Matplotlib, Seaborn

---

## 🚀 Como Executar o Projeto Localmente

1. Clone o repositório:
```bash
git clone [https://github.com/ViniciusPaula140/Analise-de-chocolate.git](https://github.com/ViniciusPaula140/Analise-de-chocolate.git)
cd Analise-de-chocolate
