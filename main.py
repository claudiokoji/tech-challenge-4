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

Tecnologias como TensorFlow e Keras melhoram a previsão dessas flutuações, enquanto ferramentas como Prophet ajudam a modelar cenários futuros com base em dados históricos, mitigando impactos econômicos adversos. Assim, a evolução do preço do petróleo Brent é um reflexo dinâmico das interações entre política, economia e tecnologia globalmente. Compreender seu comportamento é essencial para antecipar desafios e oportunidades em um mundo interconectado e interdependente.

História do Preço do Petróleo

Ao longo das décadas, guerras e revoluções moldaram o cenário geopolítico global, influenciando profundamente os preços do petróleo, uma commodity vital para a economia mundial. Aqui estão 15 desses eventos cruciais, apresentados cronologicamente:
            
1.  Guerra do Golfo (1990-1991): A invasão do Kuwait pelo Iraque levou a um aumento nos preços devido às preocupações com o fornecimento.
2.  Crise Financeira Asiática (1997-1998): A crise econômica na Ásia resultou em uma queda na demanda por petróleo, diminuindo os preços.
3.  Ataques de 11 de setembro (2001): Os ataques terroristas nos EUA aumentaram a instabilidade geopolítica e afetaram temporariamente os preços.
4.  Invasão do Iraque (2003): A invasão do Iraque elevou os preços devido às preocupações com a produção no Oriente Médio.
5.  Furacão Katrina (2005): Danos à infraestrutura de produção nos EUA aumentaram os preços.
6.  Crise Financeira Global (2008): A crise financeira levou a uma queda drástica na demanda por petróleo.
7.  Primavera Árabe (2010-2011): Revoltas no Oriente Médio e Norte da África criaram incertezas sobre o fornecimento.
8.  Guerra Civil na Líbia (2011): O conflito na Líbia interrompeu a produção, elevando os preços.
9.  Acordo Nuclear com o Irã (2015): O acordo levou à expectativa de aumento da oferta, pressionando os preços para baixo.
10. Queda dos Preços do Petróleo (2014-2016): Aumento da produção de xisto nos EUA e excesso de oferta.
11. Ataque às Instalações da Aramco (2019): Ataques com drones na Arábia Saudita interromperam a produção.
12. Pandemia de COVID-19 (2020): A pandemia reduziu drasticamente a demanda por petróleo.
13. Acordo de Corte de Produção da OPEP+ (2020): Acordo para cortar a produção e estabilizar os preços.
14. Invasão da Ucrânia pela Rússia (2022): A invasão criou incertezas sobre o fornecimento de petróleo e gás da Rússia.
15. Acordos de Redução de Emissões e Transição Energética (2021-presente): Políticas para reduzir as emissões de carbono impactam a demanda de longo prazo.
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
- Análise Técnica: Utilização de padrões históricos de preços e indicadores técnicos para prever movimentos futuros.

- Modelagem Econômica: Aplicação de modelos econométricos que levam em conta variáveis macroeconômicas e setoriais.

- Simulações e Cenários: Criação de cenários com base em diferentes suposições sobre variáveis-chave.

Perspectivas para o Futuro

- Curto Prazo: Pode haver volatilidade devido a incertezas geopolíticas e flutuações na demanda pós-pandemia.

- Médio a Longo Prazo: A transição global para fontes de energia renovável pode levar a uma demanda estruturalmente menor por petróleo, pressionando os preços para baixo, embora a volatilidade deva continuar devido a fatores geopolíticos e econômicos. \n

"""
)