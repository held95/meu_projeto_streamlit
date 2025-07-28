# 📊 Dashboard das 200 Cidades Mais Produtivas do Brasil

Este projeto é um dashboard interativo desenvolvido com **Streamlit** e **Plotly**, que permite a visualização e análise das 200 cidades mais produtivas do Brasil com base em indicadores como temperatura média, renda per capita, índice educacional e índice de saúde.

## 🚀 Funcionalidades

- Filtros interativos por cidade, temperatura, renda e educação.
- Indicadores (KPIs) como número de cidades selecionadas, média de renda e índice de saúde.
- Gráficos interativos de distribuição de temperatura e relação entre renda e saúde.
- Tabela com os dados filtrados.

## 📁 Estrutura do Projeto

```
📦seu-projeto/
├── app.py                       # Código principal com Streamlit
├── cidades_producao_brasil.csv # Base de dados com os indicadores
├── requirements.txt            # Lista de bibliotecas necessárias
└── README.md                   # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

## ▶️ Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale os pacotes:

```bash
pip install -r requirements.txt
```

3. Execute o app:

```bash
streamlit run app.py
```

> ⚠️ Certifique-se de que o arquivo `cidades_producao_brasil.csv` esteja na mesma pasta que o `app.py`.

## 🌐 Deploy com Streamlit Cloud

1. Suba os arquivos para um repositório no GitHub.
2. Acesse [streamlit.io/cloud](https://streamlit.io/cloud).
3. Conecte sua conta do GitHub e selecione o repositório.
4. Informe que o arquivo principal é `app.py`.
5. Clique em **Deploy**.

## 📷 Exemplos do App

- Gráfico de distribuição de temperatura
- Dispersão entre Renda Per Capita e Índice de Saúde
- Tabela dinâmica com os dados filtrados

---

Desenvolvido com ❤️ por Hélder Corrêa