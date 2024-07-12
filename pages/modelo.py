import streamlit as st
from util.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from util.layout import output_layout, format_number

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")

    st.markdown(
        """
        teste de pagina para modelo
    """
    )
    
with st.container():
    st.subheader(":blue[Grafico 1]", divider="blue")

    st.markdown(
        """
        Texto sobre grafico 1
    """
    )
    
with st.container():
    st.subheader(":blue[Grafico 2]", divider="blue")

    st.markdown(
        """
        Texto sobre grafico 2
    """
    )
