import streamlit as st
from util.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from util.layout import output_layout, format_number
import pandas as pd
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import matplotlib.pyplot as plt

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


def prever_brent():
    # Definir o caminho do arquivo CSV
    file_path = 'dados/base_brent_ipea.csv'

    # Carregar e preparar os dados
    data_csv = pd.read_csv(file_path, delimiter=';')
    data_csv.columns = ['Data', 'Preço', 'Unnamed']
    data = data_csv[['Data', 'Preço']]
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
    st.write(df_performance[['horizon', 'mape', 'rmse', 'mae']].head())

    # Plotar métricas de desempenho
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(df_performance['horizon'], df_performance['mape'], label='MAPE')
    ax1.plot(df_performance['horizon'], df_performance['rmse'], label='RMSE')
    ax1.plot(df_performance['horizon'], df_performance['mae'], label='MAE')
    ax1.set_xlabel('Horizonte')
    ax1.set_ylabel('Erro')
    ax1.legend()
    plt.title('Métricas de Desempenho da Validação Cruzada')
    st.pyplot(fig1)

    # Plotar os dados reais e as previsões para o período completo
    future = model.make_future_dataframe(periods=60)
    forecast = model.predict(future)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(df_prophet['ds'], df_prophet['y'], label='Dados Reais', color='blue')
    ax2.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='purple', linestyle='--')
    ax2.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='green', alpha=0.2)
    ax2.set_title('Previsão Completa com Dados Reais')
    ax2.set_xlabel('Data')
    ax2.set_ylabel('Preço')
    ax2.legend()
    st.pyplot(fig2)

    # Imprimir o valor e data da previsão
    st.write(f"Data da previsão: {forecast['ds'].iloc[-1]}")
    st.write(f"Valor previsto: {forecast['yhat'].iloc[-1]}")

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")
    
with st.container():
    st.subheader(":blue[Previsão de Preços do Petróleo Brent Utilizando Prophet]", divider="blue")

    st.markdown(
        """
        Este notebook utiliza o modelo Prophet para prever os preços futuros do petróleo Brent, pois é um modelo que lida muito bem com sazonalidades. Serão realizados os seguintes passos:
        1. Carregar e preparar os dados
        2. Treinar o modelo Prophet
        3. Realizar validação cruzada
        4. Avaliar o desempenho do modelo
        5. Plotar as previsões e os dados reais
    """
    )
    
    prever_brent()
