import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="PALOP Data Hub",
    page_icon="🌍",
    layout="wide"
)

# Título
st.title("🌍 PALOP Data Hub")

st.subheader(
    "Dados para compreender e analisar os países africanos "
    "de língua portuguesa."
)

st.markdown("---")

# Carregar dados
dados = pd.read_csv("data/populacao.csv")
# Carregar histórico de população
historico = pd.read_csv("data/populacao_historica.csv")

# Países
st.header("Países")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("🇦🇴 Angola", "AGO")
col2.metric("🇨🇻 Cabo Verde", "CPV")
col3.metric("🇬🇼 Guiné-Bissau", "GNB")
col4.metric("🇲🇿 Moçambique", "MOZ")
col5.metric("🇸🇹 São Tomé e Príncipe", "STP")

st.markdown("---")

# Indicadores
st.header("Principais indicadores")

col1, col2, col3 = st.columns(3)

# População total
populacao_total = dados["populacao"].sum()

col1.metric(
    "👥 População dos PALOP",
    f"{populacao_total / 1_000_000:.1f} milhões"
)

col2.metric("💰 PIB per capita", "Em breve")

col3.metric("🌐 Acesso à internet", "Em breve")

col1, col2, col3 = st.columns(3)

col1.metric("🏥 Expectativa de vida", "Em breve")
col2.metric("⚡ Acesso à eletricidade", "Em breve")
col3.metric("🎓 Educação", "Em breve")

st.markdown("---")

# Tabela
st.header("População por país")

tabela = dados[["pais", "ano", "populacao"]].copy()

tabela["populacao"] = tabela["populacao"].map(
    lambda x: f"{x:,.0f}".replace(",", ".")
)

st.dataframe(
    tabela,
    use_container_width=True,
    hide_index=True
)
# Gráfico de população
st.header("📊 População dos PALOP")

grafico = dados.sort_values(
    "populacao",
    ascending=False
)

st.bar_chart(
    grafico,
    x="pais",
    y="populacao"
)
# Evolução histórica da população
st.header("📈 Evolução da população")

serie_historica = historico.pivot(
    index="ano",
    columns="pais",
    values="populacao"
)

st.line_chart(serie_historica)
st.markdown("---")

st.info(
    "🚧 PALOP Data Hub está em desenvolvimento. "
    "Novos indicadores serão adicionados progressivamente."
)

st.caption("PALOP Data Hub • Projeto de Ciência de Dados")
