import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from util.layout import output_layout, format_number

st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

    st.markdown(
        """
        Texto sobre Analises dos exploratoria.
    """
    )
    
with st.container():
    st.subheader(":blue[Análise Descritiva]", divider="blue")

    st.markdown(
        """
        Texto sobre analise.
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
    
with st.container():
    st.subheader(":blue[Grafico 3]", divider="blue")

    st.markdown(
        """
        Texto sobre grafico 3
    """
    )


