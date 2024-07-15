import streamlit as st
from util.constantes import TITULO_HISTORIA, TITULO_PRINCIPAL
from util.layout import output_layout
import pandas as pd
import plotly.graph_objects as go

def plot_grafico_evolucao_preco_petroleo():
    file_path = 'dados/base_brent_ipea.csv'

    try:
        df_oil = pd.read_csv(file_path, delimiter=';')
        df_oil.columns = ['Date', 'Preço', 'Unnamed']
        df = df_oil[['Date', 'Preço']]
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
        df['Preço'] = df['Preço'].str.replace(',', '.').astype(float)
        df.dropna(inplace=True)
        df.rename(columns={'Date': 'ds', 'Preço': 'y'}, inplace=True)

        pontos_de_interesse = [
            {'data': '1990-08-02', 'label': '1. Guerra do Golfo (1990-1991)'},
            {'data': '1997-06-03', 'label': '2. Crise Financeira Asiática (1997-1998)'},
            {'data': '2001-09-11', 'label': '3. Atentados terroristas nos EUA (2001)'},
            {'data': '2003-03-20', 'label': '4. Invasão do Iraque (2003)'},
            {'data': '2005-08-29', 'label': '5. Furacão Katrina (2005)'},
            {'data': '2008-08-01', 'label': '6. Crise financeira global (2008)'},
            {'data': '2010-12-20', 'label': '7. Primavera Árabe (2010-2012)'},
            {'data': '2011-02-17', 'label': '8. Guerra Civil na Líbia (2011)'},
            {'data': '2014-11-28', 'label': '9. Queda dos Preços do Petróleo (2014-2016)'},
            {'data': '2015-01-02', 'label': '10. Acordo Nuclear com o Irã (2015)'},
            {'data': '2019-09-16', 'label': '11. Ataque às Instalações da Aramco (2019)'},
            {'data': '2020-01-30', 'label': '12. Pandemia de COVID-19 (2020)'},
            {'data': '2020-04-09', 'label': '13. Acordo de Corte de Produção da OPEP+ (2020)'},
            {'data': '2021-01-05', 'label': '14. Acordos de Redução de Emissões e Transição Energética (2021-presente)'},
            {'data': '2022-02-24', 'label': '15. Invasão da Ucrânia pela Rússia (2022)'},
        ]

        def add_ponto_interesse(fig, data, label, text_index):
            ponto = df[df['ds'] == data]
            if ponto.empty:
                st.warning(f"Data não encontrada: {label}")
                return
            valor_interesse = ponto['y'].values[0]

            fig.add_trace(
                go.Scatter(
                    x=[data],
                    y=[valor_interesse],
                    mode="markers",
                    marker=dict(color="red", size=10, line=dict(color="white", width=1)),
                    name=label
                )
            )

            fig.add_annotation(
                x=data,
                y=valor_interesse,
                text=text_index,
                showarrow=False,
                font=dict(color="white", size=10),
                bgcolor="red",
                borderwidth=1,
                bordercolor="white",
            )

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=df['ds'], y=df['y'], mode="lines", name="Preço do barril de petróleo")
        )

        for index, ponto in enumerate(pontos_de_interesse, start=1):
            add_ponto_interesse(fig, ponto['data'], ponto['label'], str(index))

        fig.add_annotation(
            x=0.5,
            y=-0.15,
            xref="paper",
            yref="paper",
            text="",
            showarrow=False,
            font=dict(color="black", size=10),
            bgcolor="black",
            borderwidth=1,
            bordercolor="black",
        )

        fig.update_layout(
            title="Evolução do preço do barril de petróleo Brent ao longo das décadas (1987 até hoje)",
            xaxis_title="Data",
            yaxis_title="Preço em US$",
            height=640,
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar os dados: {str(e)}")

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange:[{TITULO_HISTORIA}]")

    st.markdown(
        """
    O preço do petróleo Brent é influenciado por diversos fatores geopolíticos e econômicos. Aqui estão 15 eventos globais significativos que impactaram os preços:
    1. **Guerra do Golfo (1990-1991)**: A invasão do Kuwait pelo Iraque levou a um aumento nos preços devido às preocupações com o fornecimento.
    2. **Crise Financeira Asiática (1997-1998)**: A crise econômica na Ásia resultou em uma queda na demanda por petróleo, diminuindo os preços.
    3. **Ataques de 11 de setembro (2001)**: Os ataques terroristas nos EUA aumentaram a instabilidade geopolítica e afetaram temporariamente os preços.
    4. **Invasão do Iraque (2003)**: A invasão do Iraque elevou os preços devido às preocupações com a produção no Oriente Médio.
    5. **Furacão Katrina (2005)**: Danos à infraestrutura de produção nos EUA aumentaram os preços.
    6. **Crise Financeira Global (2008)**: A crise financeira levou a uma queda drástica na demanda por petróleo.
    7. **Primavera Árabe (2010-2011)**: Revoltas no Oriente Médio e Norte da África criaram incertezas sobre o fornecimento.
    8. **Guerra Civil na Líbia (2011)**: O conflito na Líbia interrompeu a produção, elevando os preços.
    9. **Acordo Nuclear com o Irã (2015)**: O acordo levou à expectativa de aumento da oferta, pressionando os preços para baixo.
    10. **Queda dos Preços do Petróleo (2014-2016)**: Aumento da produção de xisto nos EUA e excesso de oferta.
    11. **Ataque às Instalações da Aramco (2019)**: Ataques com drones na Arábia Saudita interromperam a produção.
    12. **Pandemia de COVID-19 (2020)**: A pandemia reduziu drasticamente a demanda por petróleo.
    13. **Acordo de Corte de Produção da OPEP+ (2020)**: Acordo para cortar a produção e estabilizar os preços.
    14. **Invasão da Ucrânia pela Rússia (2022)**: A invasão criou incertezas sobre o fornecimento de petróleo e gás da Rússia.
    15. **Acordos de Redução de Emissões e Transição Energética (2021-presente)**: Políticas para reduzir as emissões de carbono impactam a demanda de longo prazo.
    """
    )

with st.container():
    st.subheader(":blue:[Gráfico de evolução do preço]")

    plot_grafico_evolucao_preco_petroleo()
