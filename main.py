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
    ??????
    """
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(

     Origens e Importância
•	Descoberta e Nomenclatura: O petróleo Brent é extraído do Mar do Norte e recebeu o nome do campo petrolífero Brent, operado pela Shell.
•	Referência Global: Ele é amplamente utilizado como referência para a precificação de outros tipos de petróleo, especialmente na Europa, África e Oriente Médio.

Fatores Históricos que Influenciaram o Preço

•	Geopolítica: Conflitos no Oriente Médio, sanções econômicas e políticas da OPEP têm impacto significativo nos preços do Brent.
    o	    Crise do Golfo (1990-1991)
    o	    Guerra do Iraque (2003)
    o	    Sanções contra o Irã (década de 2010)

•	Economia Global: A demanda por petróleo está intimamente ligada ao crescimento econômico global.
    o	    Recessão de 2008: Resultou em uma queda acentuada nos preços do Brent.

•	Tecnologia e Oferta: Avanços em tecnologias de extração e novas descobertas de reservas afetam a oferta.
    o	    Revolução do Shale nos EUA: Aumentou a oferta global e pressionou os preços para baixo.

•	Eventos Climáticos e Desastres Naturais: Furacões, derramamentos de óleo e outros desastres podem interromper a produção e distribuição.
•	Políticas Energéticas e Ambientais: Mudanças na regulamentação ambiental e políticas de energia renovável também têm impacto.

Tendências e Padrões
•	Volatilidade: O preço do Brent é conhecido por sua alta volatilidade.
•	Ciclos de Alta e Baixa: A história mostra ciclos recorrentes de alta e baixa, muitas vezes ligados a fatores econômicos e geopolíticos.

Previsão Futura do Petróleo Brent

Fatores Considerados
•	Geopolítica e Conflitos: Continuação das tensões no Oriente Médio e relações internacionais podem impactar a oferta.
•	Políticas de Energia e Transição Verde: O aumento do investimento em energias renováveis e políticas de descarbonização podem reduzir a demanda por petróleo.
•	Inovações Tecnológicas: Avanços na eficiência energética e tecnologias de extração podem alterar a oferta e demanda.
•	Economia Global: O crescimento ou recessão econômica global afetará a demanda por petróleo.

Metodologias de Previsão
•	Análise Técnica: Uso de padrões históricos de preços e indicadores técnicos para prever movimentos futuros.
•	Modelagem Econômica: Modelos econométricos que consideram variáveis macroeconômicas e setoriais.
•	Simulações e Cenários: Criação de cenários baseados em diferentes suposições sobre variáveis-chave.

Perspectivas para o Futuro
•	Curto Prazo: Pode haver volatilidade devido a incertezas geopolíticas e flutuações na demanda pós-pandemia.
•	Médio a Longo Prazo: A transição energética global para fontes renováveis pode resultar em uma demanda estruturalmente menor por petróleo, pressionando os preços para baixo, embora a volatilidade permaneça devido a fatores geopolíticos e econômicos.

Conclusão
A análise histórica do petróleo Brent revela uma forte influência de fatores geopolíticos, econômicos e tecnológicos em seus preços. Para prever o futuro, é essencial considerar uma combinação desses fatores, juntamente com mudanças nas políticas de energia e avanços tecnológicos. Embora seja impossível prever com precisão exata, a compreensão desses elementos pode ajudar a fazer previsões mais informadas.


)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    ?????????;
"""
)
