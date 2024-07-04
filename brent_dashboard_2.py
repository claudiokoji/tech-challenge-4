import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Função para plotar momentos chave
def plot_momentos_chaves_preco_petroleo(ponto, id_evento):
    if not ponto.empty:
        plt.scatter(ponto.Date, ponto.Brent_Price, s=200, facecolors='none', edgecolors='red', linewidths=2)
        plt.text(ponto.Date, ponto.Brent_Price + 4, id_evento, ha='center', va='center', fontsize=8, fontweight='bold', color='red', 
                 bbox=dict(facecolor='white', alpha=0.4, edgecolor='red', boxstyle='round', lw=2))

# Função para definir a legenda
def set_legenda():
    legend_handles, _ = plt.gca().get_legend_handles_labels()
    extra_labels = [
        ('Preço do petróleo em US$', '#1F77B4', 'line'),
        ('1. Guerra do Golfo (1990-1991)', 'red', 'dot'),
        ('2. Atentados terroristas nos EUA (2001)', 'red', 'dot'),
        ('3. Guerra do Iraque (2003-2011)', 'red', 'dot'),
        ('4. Crise financeira global (2007-2008)', 'red', 'dot'),
        ('5. Primavera Árabe (2010-2012)', 'red', 'dot'),
        ('6. Guerra Civil na Líbia (2011)', 'red', 'dot'),
        ('7. Conflito na Síria (a partir de 2011)', 'red', 'dot'),
        ('8. OPEP mantém ritmo de produção (2014)', 'red', 'dot'),
        ('9. Grande produção e baixa demanda (2015)', 'red', 'dot'),
        ('10. Pandemia de COVID-19 (2020-2023)', 'red', 'dot'),
        ('11. Recuperação econômica pós-COVID (2021-presente)', 'red', 'dot'),
        ('12. Conflito Rússia-Ucrânia (2022-presente)', 'red', 'dot')
    ]

    for label, cor, tipo in extra_labels:
        if tipo == 'line':
            legend_handles.append(plt.Line2D([0], [0], color=cor, lw=2, label=label))
        elif tipo == 'dot':
            legend_handles.append(plt.Line2D([0], [0], marker='o', color='None', markerfacecolor=cor, markersize=10, label=label))

    plt.legend(title='Legenda', loc='upper left', handles=legend_handles)

# Carregar os dados
file_path = r'base_brent_ipea.csv'
df = pd.read_csv(file_path, delimiter=';')

# Limpar e preparar os dados
df.columns = ['Date', 'Brent_Price', 'Unnamed']
df = df[['Date', 'Brent_Price']]
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df['Brent_Price'] = df['Brent_Price'].str.replace(',', '.').astype(float)
df.dropna(inplace=True)

# Resample the data to get the monthly average prices
df.set_index('Date', inplace=True)
monthly_avg_prices = df['Brent_Price'].resample('M').mean().reset_index()

# Eventos globais significativos
events = [
    ("Guerra do Golfo", "1990-08-02"),
    ("Crise Financeira Asiática", "1997-07-02"),
    ("Ataques de 11 de setembro", "2001-09-11"),
    ("Invasão do Iraque", "2003-03-20"),
    ("Furacão Katrina", "2005-08-29"),
    ("Crise Financeira Global", "2008-09-15"),
    ("Primavera Árabe", "2010-12-18"),
    ("Guerra Civil na Líbia", "2011-02-17"),
    ("Acordo Nuclear com o Irã", "2015-07-14"),
    ("Queda dos Preços do Petróleo", "2014-06-01"),
    ("Ataque às Instalações da Aramco", "2019-09-14"),
    ("Pandemia de COVID-19", "2020-03-11"),
    ("Acordo de Corte de Produção da OPEP+", "2020-04-12"),
    ("Invasão da Ucrânia pela Rússia", "2022-02-24"),
    ("Acordos de Redução de Emissões", "2021-11-13")
]
event_dates = [pd.to_datetime(date) for _, date in events]

# Aplicação Streamlit
st.set_page_config(page_title="Tech Challenge 4 | FIAP", layout="wide")

# Sidebar para navegação
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Selecione a página", ["Tech Challenge 4 | FIAP", "Evolução do preço do petróleo", "Análises exploratórias", "Modelos de previsão"])

if page == "Tech Challenge 4 | FIAP":
    st.title("Tech Challenge 4 | FIAP")
    st.write("Bem-vindo ao Tech Challenge 4 da FIAP. Navegue pelo menu para explorar diferentes seções.")
    
elif page == "Evolução do preço do petróleo":
    st.title("Evolução do preço do petróleo")
    st.write("""
    ### Resumo sobre a evolução do petróleo
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
    11. **Ataque às Instalações da Aramco (2019)**: Ataques com drones na Arábia Saudita interromperam a produção, elevando os preços.
    12. **Pandemia de COVID-19 (2020)**: A pandemia reduziu drasticamente a demanda por petróleo.
    13. **Acordo de Corte de Produção da OPEP+ (2020)**: Acordo para cortar a produção e estabilizar os preços.
    14. **Invasão da Ucrânia pela Rússia (2022)**: A invasão criou incertezas sobre o fornecimento de petróleo e gás da Rússia.
    15. **Acordos de Redução de Emissões e Transição Energética (2021-presente)**: Políticas para reduzir as emissões de carbono impactam a demanda de longo prazo.
    """)
    
    st.write("### Gráfico de Evolução do Preço do Petróleo Brent com Eventos Significativos")
    plt.figure(figsize=(14, 8))
    plt.plot(monthly_avg_prices['Date'], monthly_avg_prices['Brent_Price'], label='Preço Médio Brent por Mês', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Preço Médio (US$)')
    plt.title('Evolução do Preço Médio Mensal do Petróleo Brent com Eventos Globais Significativos')
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # Adicionando os eventos ao gráfico
    event_dict = {
        1: "1990-08-02",
        2: "2001-09-11",
        3: "2003-03-20",
        4: "2007-08-01",
        5: "2010-12-20",
        6: "2011-02-17",  # Complete the date here
        7: "2011-03-15",
        8: "2014-11-28",
        9: "2015-01-02",
        10: "2020-01-30",
        11: "2021-07-01",
        12: "2022-02-24"
    }

    for event_id, date in event_dict.items():
        ponto = monthly_avg_prices[monthly_avg_prices['Date'] == pd.to_datetime(date)]
        plot_momentos_chaves_preco_petroleo(ponto, event_id)

    plt.grid(linestyle='--', color='gray', alpha=0.5)
    set_legenda()
    plt.title('Evolução do preço do barril de petróleo Brent ao longo das décadas (1987 até hoje)')
    plt.show()
