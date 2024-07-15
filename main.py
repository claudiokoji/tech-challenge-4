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
Evolução do Preço do Petróleo: Uma Jornada pela Economia Global


O petróleo Brent, extraído do Mar do Norte, é mais que uma commodity; é um indicador econômico global crucial. Como referência internacional para os preços do petróleo bruto, ele influencia custos de transporte e alimentos. Seus preços são voláteis, refletindo a complexidade dos fatores econômicos e geopolíticos. Eventos como a Guerra do Golfo e os ataques de 2001 causaram grandes flutuações, enquanto crises financeiras e conflitos regionais como a Primavera Árabe moldaram tendências duradouras. A Energy Information Administration (EIA) dos EUA fornece dados essenciais que orientam decisões econômicas e políticas globalmente, e a OPEP impacta diretamente os preços do Brent com sua produção.

No Brasil, o Instituto de Pesquisa Econômica Aplicada (IPEA) analisa o impacto desses eventos na economia nacional, oferecendo insights sobre como as flutuações nos preços do petróleo afetam diversos setores, desde o mercado de trabalho até políticas ambientais.

Ferramentas como Prophet ajudam a modelar cenários futuros com base em dados históricos, mitigando impactos econômicos adversos. Assim, a evolução do preço do petróleo Brent é um reflexo dinâmico das interações entre política, economia e tecnologia globalmente. Compreender seu comportamento é essencial para antecipar desafios e oportunidades em um mundo interconectado e interdependente.
    """
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
O objetivo desta análise é compreender os fatores históricos que influenciam os preços do petróleo Brent e utilizar esse conhecimento para prever suas futuras variações. Isso é útil para investidores, economistas, formuladores de políticas e outros interessados que buscam:

- Tomar Decisões Informadas: Conhecer os padrões e fatores que afetam o preço do Brent ajuda a fundamentar melhor as decisões de investimento.

- Mitigar Riscos: Empresas e governos podem usar previsões de preços para reduzir os riscos associados à volatilidade do petróleo, como flutuações nos custos de produção e transporte.

- Planejamento e Estratégia: Desenvolver estratégias de longo prazo que considerem possíveis cenários futuros, incluindo a transição para energias renováveis ou mudanças nas políticas energéticas internacionais.

- Aprimorar Políticas Energéticas: Governos e reguladores podem utilizar essas análises para criar políticas energéticas mais eficazes e adaptáveis, que considerem as tendências globais e as necessidades energéticas futuras.

- Gerar Insights Econômicos: Compreender a relação entre os preços do petróleo e a economia global pode oferecer insights valiosos sobre o crescimento econômico, inflação e outros indicadores macroeconômicos.

Assim, o objetivo é fornecer uma base sólida de conhecimento histórico e uma abordagem metodológica para prever futuros movimentos de preços, auxiliando na tomada de decisões estratégicas em diversos contextos.

"""
)


st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
- Análise Histórica: Examinamos os dados passados do preço do petróleo Brent para identificar tendências e eventos significativos que influenciaram suas flutuações.

- Análise Exploratória: Realizamos uma análise detalhada dos dados atuais e históricos do Brent, incluindo a distribuição dos preços, cálculos de médias móveis e avaliação da volatilidade. Criamos visualizações gráficas para revelar insights ocultos nos dados, permitindo uma compreensão mais profunda dos padrões subjacentes e ajudando a identificar possíveis anomalias ou tendências emergentes.

- Simulação: Desenvolvemos uma simulação baseada em um modelo preditivo utilizando a biblioteca Prophet.
"""
)