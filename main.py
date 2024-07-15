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

Desde sua extração nas profundezas do Mar do Norte, o petróleo Brent não é apenas uma commodity, mas um indicador vital para a economia mundial. Como referência internacional para os preços do petróleo bruto, o Brent estabelece padrões nas transações globais, influenciando desde o custo do transporte até o preço dos alimentos.
A trajetória dos preços do petróleo Brent é turbulenta, refletindo a interseção complexa de fatores econômicos e geopolíticos. Ao longo das décadas, eventos como a Guerra do Golfo e os ataques terroristas de 2001 causaram flutuações abruptas, enquanto crises financeiras globais e conflitos regionais como a Primavera Árabe moldaram tendências duradouras.
Organizações como a Energy Information Administration (EIA) dos EUA desempenham um papel crucial ao fornecer dados precisos que orientam decisões econômicas e políticas em todo o mundo. A influência da OPEP na produção também é determinante, impactando diretamente os preços globais do Brent.

O Instituto de Pesquisa Econômica Aplicada (IPEA) do Brasil contribui com análises fundamentais para entendermos o impacto desses eventos na economia nacional. Suas pesquisas fornecem insights valiosos sobre como flutuações nos preços do petróleo afetam variados setores, desde o mercado de trabalho até políticas ambientais.

À medida que nos adaptamos às mudanças globais, tecnologias como o TensorFlow e o Keras tornam possível prever essas flutuações com maior precisão. Ferramentas como o Prophet permitem modelar cenários futuros com base em dados históricos, ajudando a mitigar os impactos econômicos adversos.
Em resumo, a evolução do preço do petróleo Brent não é apenas um registro econômico, mas um reflexo dinâmico das interações complexas entre política, economia e tecnologia em escala global. Entender seu curso é fundamental para antecipar desafios e oportunidades em um mundo cada vez mais interconectado e interdependente.

A História do Preço do Petróleo 

Ao longo das décadas, diversos eventos significativos, como guerras e revoluções, moldaram o contexto geopolítico global e influenciaram profundamente os preços do petróleo, uma commodity vital para a economia mundial. 

Abaixo estão 15 desses eventos cruciais, apresentados cronologicamente: 
            
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