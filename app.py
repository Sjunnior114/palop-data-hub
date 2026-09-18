import streamlit as st

st.set_page_config(
    page_title="PALOP Data Hub",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 PALOP Data Hub")

st.subheader(
    "Dados para compreender e analisar os países africanos "
    "de língua portuguesa."
)

st.markdown("---")

st.header("Países")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("🇦🇴 Angola", "AGO")
col2.metric("🇨🇻 Cabo Verde", "CPV")
col3.metric("🇬🇼 Guiné-Bissau", "GNB")
col4.metric("🇲🇿 Moçambique", "MOZ")
col5.metric("🇸🇹 São Tomé e Príncipe", "STP")

st.markdown("---")

st.header("Principais indicadores")

col1, col2, col3 = st.columns(3)

col1.metric("👥 População", "Em breve")
col2.metric("💰 PIB per capita", "Em breve")
col3.metric("🌐 Acesso à internet", "Em breve")

col1, col2, col3 = st.columns(3)

col1.metric("🏥 Expectativa de vida", "Em breve")
col2.metric("⚡ Acesso à eletricidade", "Em breve")
col3.metric("🎓 Educação", "Em breve")

st.markdown("---")

st.info(
    "🚧 Projeto em desenvolvimento — os primeiros dados serão "
    "adicionados nas próximas etapas."
)

st.caption("PALOP Data Hub • Projeto de Ciência de Dados")
