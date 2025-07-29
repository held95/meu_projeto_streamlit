# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# 🔐 Ativação do ngrok (caso esteja rodando no ambiente local + Colab)
try:
    from pyngrok import ngrok, conf
    conf.get_default().auth_token = "SEU_TOKEN_NGROK_AQUI"
    public_url = ngrok.connect(8501)
    print(f"Acesse seu app aqui: {public_url}")
except Exception as e:
    print("⚠️ Ngrok não ativado. Execute apenas se estiver em ambiente compatível.")
    print(e)

# =========================== Configurações do Streamlit ===========================

st.set_page_config(page_title="Dashboard Cidades Produtivas", layout="wide")
st.title("📊 Dashboard das 200 Cidades Mais Produtivas do Brasil")

# =========================== Função de carga de dados =============================

@st.cache_data
def carregar_dados():
    return pd.read_csv("cidades_producao_brasil.csv")  # Garanta que o CSV esteja na raiz do projeto

df = carregar_dados()

# ============================== Barra lateral de filtros ==============================

with st.sidebar:
    st.header("Filtros")
    cidades_selecionadas = st.multiselect(
        "Escolha as cidades:",
        options=df["Cidade"].unique(),
        default=df["Cidade"].unique()[:10]
    )
    temp_min, temp_max = st.slider(
        "Temperatura Média (°C)",
        float(df["Temperatura Média (°C)"].min()),
        float(df["Temperatura Média (°C)"].max()),
        (20.0, 30.0)
    )
    renda_min, renda_max = st.slider(
        "Renda Per Capita (R$)",
        float(df["Renda Per Capita (R$)"].min()),
        float(df["Renda Per Capita (R$)"].max()),
        (1000.0, 4000.0)
    )
    educ_min = st.slider("Índice Educacional mínimo", 0.3, 1.0, 0.5)

# ============================== Aplicação dos filtros ==============================

df_filtrado = df[
    (df["Cidade"].isin(cidades_selecionadas)) &
    (df["Temperatura Média (°C)"].between(temp_min, temp_max)) &
    (df["Renda Per Capita (R$)"].between(renda_min, renda_max)) &
    (df["Índice Educacional"] >= educ_min)
]

# ============================== Métricas / KPIs ==============================

col1, col2, col3 = st.columns(3)
col1.metric("Cidades Selecionadas", len(df_filtrado))
col2.metric("Média Renda Per Capita", f"R$ {df_filtrado['Renda Per Capita (R$)'].mean():,.2f}")
col3.metric("Média Índice Saúde", f"{df_filtrado['Índice de Saúde'].mean():.2f}")

st.markdown("---")

# ============================== Gráficos ==============================

col4, col5 = st.columns(2)

with col4:
    fig1 = px.histogram(df_filtrado, x="Temperatura Média (°C)", nbins=20, title="Distribuição de Temperaturas")
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.scatter(
        df_filtrado,
        x="Renda Per Capita (R$)",
        y="Índice de Saúde",
        size="Número de Habitantes",
        color="Cidade",
        title="Renda vs Saúde"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ============================== Tabela ==============================

st.markdown("### 📋 Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)
