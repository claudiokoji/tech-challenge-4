import streamlit as st
from util.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from util.layout import output_layout, format_number

import pandas as pd
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import matplotlib.pyplot as plt



# Definir o caminho do arquivo CSV
file_path = '/content/base_brent_ipea.csv'

# Carregar os dados do arquivo CSV
data = pd.read_csv(file_path, delimiter=';')

# Converter a coluna de datas e ajustar os preços
data['Data'] = pd.to_datetime(data['Data'], dayfirst=True)
data['Preço'] = data['Preço'].str.replace(',', '.').astype(float)

# Remover linhas com valores nulos
data = data.dropna()

# Filtrar os dados para incluir apenas a partir de 2020
data = data[data['Data'] >= '2020-01-01']

# Renomear as colunas para o formato esperado pelo Prophet
df_prophet = data[['Data', 'Preço']].rename(columns={'Data': 'ds', 'Preço': 'y'})

# Instanciar o modelo Prophet com ajustes específicos
model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True,
    weekly_seasonality=True,
    changepoint_prior_scale=0.02,  # Sensibilidade a mudanças na tendência
    seasonality_prior_scale=5.0  # Sensibilidade aos componentes sazonais
)

# Adicionar sazonalidade mensal e trimestral
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
model.add_seasonality(name='quarterly', period=91.25, fourier_order=8)

# Treinar o modelo com os dados preparados
model.fit(df_prophet)

# Realizar a validação cruzada
df_cv = cross_validation(model, initial='1095 days', period='180 days', horizon='365 days')

# Calcular as métricas de desempenho da validação cruzada
df_performance = performance_metrics(df_cv)


# Imprimir as primeiras linhas das métricas de desempenho
print(df_performance[['horizon', 'mape', 'rmse', 'mae']].head())

# Plotar as métricas de desempenho
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(df_performance['horizon'], df_performance['mape'], label='MAPE')
ax.plot(df_performance['horizon'], df_performance['rmse'], label='RMSE')
ax.plot(df_performance['horizon'], df_performance['mae'], label='MAE')
ax.set_xlabel('Horizonte')
ax.set_ylabel('Erro')
ax.legend()
plt.title('Métricas de Desempenho da Validação Cruzada')
plt.show()


# Fazer previsões para o período completo
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Plotar os dados reais e as previsões
plt.figure(figsize=(10, 6))
plt.plot(df_prophet['ds'], df_prophet['y'], label='Dados Reais', color='blue')
plt.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='purple', linestyle='--')
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='green', alpha=0.2)
plt.title('Previsão Completa com Dados Reais')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.show()

def prever_brent():
    # Definir o caminho do arquivo CSV
    file_path = '/content/base_brent_ipea.csv'  # Substitua pelo caminho correto do arquivo no Colab

    # Carregar e preparar os dados
    data = pd.read_csv(file_path, delimiter=';')
    data['Data'] = pd.to_datetime(data['Data'], dayfirst=True)
    data['Preço'] = data['Preço'].str.replace(',', '.').astype(float)
    data = data.dropna()  # Remover linhas com valores nulos
    data = data[data['Data'] >= '2020-01-01']  # Utilizar dados a partir de 2020
    df_prophet = data[['Data', 'Preço']].rename(columns={'Data': 'ds', 'Preço': 'y'})

    # Instanciar e treinar o modelo nos dados completos
    model = Prophet(
        daily_seasonality=True,
        yearly_seasonality=True,
        weekly_seasonality=True,
        changepoint_prior_scale=0.02,  # Ajustar sensibilidade a mudanças
        seasonality_prior_scale=5.0  # Ajustar sazonalidade
    )
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)  # Adicionar sazonalidade mensal
    model.add_seasonality(name='quarterly', period=91.25, fourier_order=8)  # Adicionar sazonalidade trimestral
    model.fit(df_prophet)

    # Validação cruzada
    df_cv = cross_validation(model, initial='1095 days', period='180 days', horizon='365 days')
    df_performance = performance_metrics(df_cv)

    # Imprimir métricas de desempenho
    print(df_performance[['horizon', 'mape', 'rmse', 'mae']].head())

    # Plotar métricas de desempenho
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.plot(df_performance['horizon'], df_performance['mape'], label='MAPE')
    ax.plot(df_performance['horizon'], df_performance['rmse'], label='RMSE')
    ax.plot(df_performance['horizon'], df_performance['mae'], label='MAE')
    ax.set_xlabel('Horizonte')
    ax.set_ylabel('Erro')
    ax.legend()
    plt.title('Métricas de Desempenho da Validação Cruzada')
    plt.show()

    # Plotar os dados reais e as previsões para o período completo
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)
    plt.figure(figsize=(10, 6))
    plt.plot(df_prophet['ds'], df_prophet['y'], label='Dados Reais', color='blue')
    plt.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='purple', linestyle='--')
    plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='green', alpha=0.2)
    plt.title('Previsão Completa com Dados Reais')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.legend()
    plt.show()

# Chamada da função para executar a previsão
prever_brent()









st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")

    st.markdown(
        """
        teste de pagina para modelo
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
