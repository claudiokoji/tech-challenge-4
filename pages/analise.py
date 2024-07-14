import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from util.layout import output_layout, format_number
import os
import numpy as np


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






# Função para carregar os dados
@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        st.write("Colunas disponíveis no arquivo CSV:")
        st.write(data.columns)

        # Ajuste o nome das colunas aqui conforme necessário
        data.rename(columns={'DATA': 'Date', 'VALOR': 'Price'}, inplace=True)

        # Verificar se a coluna 'Date' está presente após a renomeação
        if 'Date' not in data.columns:
            st.error("A coluna 'Date' não está presente no DataFrame após a renomeação.")
            st.write("Colunas disponíveis após renomeação:")
            st.write(data.columns)
            return None

        data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
        data.set_index('Date', inplace=True)
        return data
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Nome do arquivo
file_path = '/mount/src/tech-challenge-4/brent_preco.csv'

# Imprimir o caminho absoluto do arquivo e o diretório atual para depuração
st.write(f"Caminho absoluto do arquivo: {os.path.abspath(file_path)}")
st.write(f"Diretório atual: {os.getcwd()}")

# Carregar dados
data = load_data(file_path)

if data is not None:
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
    st.hist_chart(data['Price'])

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
else:
    st.error("Não foi possível carregar os dados corretamente. Verifique o arquivo e tente novamente.")



    
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


