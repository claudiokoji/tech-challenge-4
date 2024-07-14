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


# Carregar dados históricos (substitua pelo seu próprio conjunto de dados)
@st.cache
def load_data():
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
    data = pd.read_csv(url, parse_dates=['Date'])
    data.set_index('Date', inplace=True)
    return data

# Carregar dados
data = load_data()

# Título da aplicação
st.title('Análise Exploratória do Petróleo Brent')

# Mostrar os dados
st.subheader('Dados Históricos')
st.write(data.head())

# Gráfico de preços ao longo do tempo
st.subheader('Preço do Petróleo Brent ao Longo do Tempo')
st.line_chart(data['Price'])

# Histograma da distribuição dos preços
st.subheader('Distribuição dos Preços')
fig, ax = plt.subplots()
ax.hist(data['Price'], bins=50, color='blue', edgecolor='black')
st.pyplot(fig)

# Análise de médias móveis
st.subheader('Médias Móveis')
data['Média Móvel de 30 Dias'] = data['Price'].rolling(window=30).mean()
data['Média Móvel de 90 Dias'] = data['Price'].rolling(window=90).mean()
st.line_chart(data[['Price', 'Média Móvel de 30 Dias', 'Média Móvel de 90 Dias']])

# Análise de volatilidade
st.subheader('Volatilidade')
data['Retorno Diário'] = data['Price'].pct_change()
data['Volatilidade de 30 Dias'] = data['Retorno Diário'].rolling(window=30).std()
st.line_chart(data['Volatilidade de 30 Dias'])

# Conclusão
st.subheader('Conclusão')
st.write("""
Esta análise exploratória mostra como o preço do petróleo Brent variou ao longo do tempo, sua distribuição, 
médias móveis e volatilidade. Essas visualizações ajudam a entender os padrões históricos e podem ser úteis para 
previsões futuras e tomadas de decisão informadas.
""")




    
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


