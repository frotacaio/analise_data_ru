from datetime import datetime
import streamlit as st

from analise_data_ru.view.data import load_ru_data
import plotly.express as px


def time_series():
    st.title('Visualizações das Series Temporais')
    st.sidebar.title('Visualizações das Serie Temporais')
    st.markdown(
        'Abaixo são mostrados os graficos das Serie Temporais para o almoço e jantar'
    )

    processed_data = load_ru_data()

    domain = processed_data['Data'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    fig1 = px.line(
        processed_data,
        x=domain,
        y='Qt_almoco',
    )
    fig1.layout.update({'title': 'Quantidade de pratos servidos ao longo do tempo: Almoço'})
    fig1.layout.yaxis.update({'title': 'Pratos servidos'})
    fig1.layout.xaxis.update({'title': 'Período'})

    st.plotly_chart(fig1, use_container_width=True)

    fig1 = px.line(
        processed_data,
        x=domain,
        y='Qt_jantar',
    )
    fig1.update_traces(line_color='orange')
    fig1.layout.update({'title': 'Quantidade de pratos servidos ao longo do tempo: Jantar'})
    fig1.layout.yaxis.update({'title': 'Pratos servidos'})
    fig1.layout.xaxis.update({'title': 'Período'})

    st.plotly_chart(fig1, use_container_width=True)

    st.markdown(
        'Nota-se, a partir dos dois gráficos, que houve um aumento da quantidade de pratos servidos ao longo dos anos.'
    )


time_series()