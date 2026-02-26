import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# -------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------

st.set_page_config(
    page_title="Acessibilidade ao Cinema no Brasil",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------
# TÍTULO
# -------------------------------

st.title("🎬 Acessibilidade Econômica ao Cinema no Brasil")
st.markdown("""
Dashboard interativo que analisa o impacto da renda per capita no acesso ao cinema,
utilizando dados oficiais do IBGE.
""")

# -------------------------------
# CARREGAMENTO DOS DADOS
# -------------------------------

arquivo = 'Tabela Per Capita-Brasil.xlsx'

df = pd.read_excel(arquivo, sheet_name='Estados')
df.columns = ['estado', 'uf', 'renda_per_capita']

# -------------------------------
# PARÂMETROS
# -------------------------------

PRECO_INGRESSO = st.sidebar.slider(
    'Preço médio do ingresso (R$)',
    min_value=10,
    max_value=60,
    value=30,
    step=1
)

df['iaec_percentual'] = (PRECO_INGRESSO / df['renda_per_capita']) * 100

# -------------------------------
# KPIs
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Preço Ingresso", f"R$ {PRECO_INGRESSO}")
col2.metric("Renda Média Brasil", f"R$ {df['renda_per_capita'].mean():.2f}")
col3.metric("IAEC Médio", f"{df['iaec_percentual'].mean():.2f}%")
col4.metric("Estados", df.shape[0])

# -------------------------------
# MAPA
# -------------------------------

st.subheader("Mapa da Acessibilidade ao Cinema")

url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"

try:
    geojson_estados = requests.get(url, timeout=10).json()
    
    mapa_nomes = {
        'Acre': 'Acre','Alagoas': 'Alagoas','Amapá': 'Amapa','Amazonas': 'Amazonas',
        'Bahia': 'Bahia','Ceará': 'Ceara','Distrito Federal': 'Distrito Federal',
        'Espírito Santo': 'Espirito Santo','Goiás': 'Goias','Maranhão': 'Maranhao',
        'Mato Grosso': 'Mato Grosso','Mato Grosso do Sul': 'Mato Grosso do Sul',
        'Minas Gerais': 'Minas Gerais','Pará': 'Para','Paraíba': 'Paraiba',
        'Paraná': 'Parana','Pernambuco': 'Pernambuco','Piauí': 'Piaui',
        'Rio de Janeiro': 'Rio de Janeiro','Rio Grande do Norte': 'Rio Grande do Norte',
        'Rio Grande do Sul': 'Rio Grande do Sul','Rondônia': 'Rondonia',
        'Roraima': 'Roraima','Santa Catarina': 'Santa Catarina',
        'São Paulo': 'Sao Paulo','Sergipe': 'Sergipe','Tocantins': 'Tocantins'
    }

    df['estado_mapa'] = df['estado'].map(mapa_nomes)

    fig_map = px.choropleth(
        df,
        geojson=geojson_estados,
        locations='estado_mapa',
        featureidkey='properties.name',
        color='iaec_percentual',
        color_continuous_scale='Reds',
        hover_name='estado',
        hover_data={
            'renda_per_capita': True,
            'iaec_percentual': ':.2f'
        },
        title='Percentual da renda mensal necessário para 1 ingresso'
    )

    fig_map.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig_map, use_container_width=True)

except Exception as e:
    st.error("⚠️ Não foi possível carregar o mapa geográfico.")
    st.write(e)

# -------------------------------
# RANKINGS
# -------------------------------

st.subheader("📊 Ranking dos Estados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Mais inacessíveis")
    st.dataframe(
        df.sort_values(by='iaec_percentual', ascending=False)
          .head(10)[['estado','iaec_percentual']]
    )

with col2:
    st.markdown("### Mais acessíveis")
    st.dataframe(
        df.sort_values(by='iaec_percentual')
          .head(10)[['estado','iaec_percentual']]
    )

# -------------------------------
# DISTRIBUIÇÃO
# -------------------------------

st.subheader("📈 Distribuição da Acessibilidade")

fig_hist = px.histogram(
    df,
    x='iaec_percentual',
    nbins=15,
    title='Distribuição do IAEC (%)',
    labels={'iaec_percentual':'% da renda mensal'}
)

st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------------
# RODAPÉ
# -------------------------------

st.markdown("---")
st.markdown("""
**Projeto de Ciência de Dados — Isabela Moreno**  
Fonte dos dados: IBGE (PNAD Contínua 2024)
""")