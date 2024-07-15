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
    st.markdown("""
        Texto sobre Análises Exploratórias.
    """)

# Função para carregar os dados sem parse_dates para inspeção
@st.cache_data
def inspect_data(file_path):
    try:
        data = pd.read_csv(file_path, sep=";")
        return data
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Verificação do caminho do arquivo
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'dados/base_brent_ipea.csv')

# Imprimir o caminho absoluto do arquivo e o diretório atual para depuração
st.write(f"Caminho absoluto do arquivo: {os.path.abspath(file_path)}")
st.write(f"Diretório atual: {current_directory}")

# Inspecionar dados
inspected_data = inspect_data(file_path)

if inspected_data is not None:
    st.subheader('Inspeção Inicial dos Dados')
    st.write(inspected_data.head())

    # Verificar as colunas do dataframe inspecionado
    st.write("Colunas disponíveis no arquivo CSV:")
    st.write(inspected_data.columns)

    # Função para carregar e normalizar os dados
    @st.cache_data
    def load_and_normalize_data(file_path):
        try:
            data = pd.read_csv(file_path, sep=";")
            st.write("Colunas lidas do arquivo CSV:")
            st.write(data.columns)  # Print column names for debugging

            # Ajuste o nome das colunas aqui conforme necessário
            if 'Data' not in data.columns or 'Preço' not in data.columns:
                st.error("As colunas esperadas 'Data' e 'Preço' não foram encontradas no arquivo CSV.")
                return None

            data.rename(columns={'Data': 'Date', 'Preço': 'Price'}, inplace=True)
            data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
            data['Price'] = data['Price'].replace(',', '.', regex=True).astype(float)
            data.set_index('Date', inplace=True)
            data['Price'].fillna(data['Price'].mean(), inplace=True)  # Preenchendo valores ausentes com a média
            return data
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")
            return None

    # Carregar e normalizar dados
    data = load_and_normalize_data(file_path)

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
        fig, ax = plt.subplots()
        data['Price'].plot(kind='hist', ax=ax)
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
    else:
        st.error("Não foi possível carregar os dados corretamente após a inspeção.")
else:
    st.error("Não foi possível inspecionar os dados.")