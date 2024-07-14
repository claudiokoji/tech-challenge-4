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
O objetivo desta análise é entender os fatores históricos que influenciam os preços do petróleo Brent e utilizar esse conhecimento para fazer previsões sobre suas futuras variações de preço. Isso pode ser útil para investidores, economistas, formuladores de políticas e outros stakeholders que desejam:

1.  Tomar Decisões Informadas: Compreender os padrões e os fatores que influenciam o preço do petróleo Brent pode ajudar a tomar decisões de investimento mais bem fundamentadas. \n

2.  Mitigar Riscos: Empresas e governos podem usar previsões de preços para mitigar riscos associados à volatilidade dos preços do petróleo, como flutuações nos custos de produção e transporte. \n

3.  Planejamento e Estratégia: Planejar estratégias de longo prazo que considerem possíveis cenários futuros, como a transição para fontes de energia renovável ou mudanças nas políticas internacionais de energia. \n

4.  Aprimorar Políticas Energéticas: Governos e órgãos reguladores podem usar essas análises para desenvolver políticas energéticas mais eficazes e adaptativas, que levem em conta as tendências globais e as futuras necessidades energéticas. \n

5.  Gerar Insights Econômicos: Entender a relação entre os preços do petróleo e a economia global pode fornecer insights valiosos sobre o crescimento econômico, inflação, e outros indicadores macroeconômicos. \n

Portanto, o objetivo é fornecer uma base sólida de conhecimento histórico e uma abordagem metodológica para prever futuros movimentos de preços, auxiliando na tomada de decisões estratégicas em diversos contextos. \n
     
"""
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
Análise Técnica: Uso de padrões históricos de preços e indicadores técnicos para prever movimentos futuros.\n
    Modelagem Econômica: Modelos econométricos que consideram variáveis macroeconômicas e setoriais.\n
    Simulações e Cenários: Criação de cenários baseados em diferentes suposições sobre variáveis-chave.\n
Perspectivas para o Futuro \n
    Curto Prazo: Pode haver volatilidade devido a incertezas geopolíticas e flutuações na demanda pós-pandemia. \n
    Médio a Longo Prazo: A transição energética global para fontes renováveis pode resultar em uma demanda estruturalmente menor por petróleo, pressionando os preços para baixo, embora a volatilidade permaneça devido a fatores geopolíticos e econômicos. \n

"""
)
