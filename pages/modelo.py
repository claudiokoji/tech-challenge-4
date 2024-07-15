import streamlit as st
from util.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from util.layout import output_layout, format_number

import pandas as pd
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import matplotlib.pyplot as plt

# Set up the Streamlit page
st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)

output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")

    st.markdown(
        """
        Esta página apresenta a previsão dos preços do Brent com base em dados históricos.
        """
    )

# Define the file path for the CSV file
file_path = '/dados/base_brent_ipea.csv'

# Load and prepare the data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, delimiter=';')
    data['Data'] = pd.to_datetime(data['Data'], dayfirst=True)
    data['Preço'] = data['Preço'].str.replace(',', '.').astype(float)
    data = data.dropna()
    data = data[data['Data'] >= '2020-01-01']
    return data

data = load_data(file_path)

# Prepare the data for Prophet
df_prophet = data[['Data', 'Preço']].rename(columns={'Data': 'ds', 'Preço': 'y'})

# Define and train the Prophet model
def train_model(df_prophet):
    model = Prophet(
        daily_seasonality=True,
        yearly_seasonality=True,
        weekly_seasonality=True,
        changepoint_prior_scale=0.02,
        seasonality_prior_scale=5.0
    )
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    model.add_seasonality(name='quarterly', period=91.25, fourier_order=8)
    model.fit(df_prophet)
    return model

model = train_model(df_prophet)

# Perform cross-validation
df_cv = cross_validation(model, initial='1095 days', period='180 days', horizon='365 days')
df_performance = performance_metrics(df_cv)

# Display performance metrics
with st.container():
    st.subheader(":blue[Métricas de Desempenho da Validação Cruzada]", divider="blue")

    st.dataframe(df_performance[['horizon', 'mape', 'rmse', 'mae']].head())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_performance['horizon'], df_performance['mape'], label='MAPE')
    ax.plot(df_performance['horizon'], df_performance['rmse'], label='RMSE')
    ax.plot(df_performance['horizon'], df_performance['mae'], label='MAE')
    ax.set_xlabel('Horizonte')
    ax.set_ylabel('Erro')
    ax.legend()
    ax.set_title('Métricas de Desempenho da Validação Cruzada')
    st.pyplot(fig)

# Make future predictions
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Plot the real data and predictions
with st.container():
    st.subheader(":blue[Previsão Completa com Dados Reais]", divider="blue")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_prophet['ds'], df_prophet['y'], label='Dados Reais', color='blue')
    ax.plot(forecast['ds'], forecast['yhat'], label='Previsão', color='purple', linestyle='--')
    ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='green', alpha=0.2)
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.legend()
    ax.set_title('Previsão Completa com Dados Reais')
    st.pyplot(fig)

    st.markdown(
        """
        Esta seção mostra a previsão dos preços do Brent para os próximos 365 dias com base nos dados históricos.
        """
    )
