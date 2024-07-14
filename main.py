import streamlit as st
from util.constantes import TITULO_PRINCIPAL
from util.layout import output_layout
from st_pages import show_pages, Page

import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(
    ":blue[Análise histórica do petróleo Brent: analisando o seu passado e prevendo o seu futuro]",
    divider="blue",
)
st.markdown(
    """
    A análise histórica do petróleo Brent revela uma forte influência de fatores geopolíticos, econômicos e tecnológicos em seus preços. Para prever o futuro, é essencial considerar uma combinação desses fatores, juntamente com mudanças nas políticas de energia e avanços tecnológicos. Embora seja impossível prever com precisão exata, a compreensão desses elementos pode ajudar a fazer previsões mais informadas
    """
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
     ????????.
"""
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    •	Análise Técnica: Uso de padrões históricos de preços e indicadores técnicos para prever movimentos futuros.
    •	Modelagem Econômica: Modelos econométricos que consideram variáveis macroeconômicas e setoriais.
    •  	Simulações e Cenários: Criação de cenários baseados em diferentes suposições sobre variáveis-chave.
Perspectivas para o Futuro
    •	Curto Prazo: Pode haver volatilidade devido a incertezas geopolíticas e flutuações na demanda pós-pandemia.
    •	Médio a Longo Prazo: A transição energética global para fontes renováveis pode resultar em uma demanda estruturalmente menor por petróleo, pressionando os preços para baixo, embora a volatilidade permaneça devido a fatores geopolíticos e econômicos.

"""
)
