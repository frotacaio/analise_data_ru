from sklearn.metrics import r2_score
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

from datetime import datetime
from plotly import figure_factory as ff

from analise_data_ru.view.data import create_predict_data, load_ru_data, get_split_data
from analise_data_ru.models import get_best_models


def predict(model_almoco, model_janta, X):
    y_predict_almoco = model_almoco.predict(X)
    y_predict_janta = model_janta.predict(X)
    return y_predict_almoco, y_predict_janta

def custom_prediction():
    st.title('Predição de novos dados')
    st.sidebar.title('Predição de novos dados')

    st.markdown(
        'Aqui você pode fazer a predição de uma nova serie temporal.'
    )

    initial_date = st.sidebar.date_input('Digite a data de inicio')
    final_date = st.sidebar.date_input('Digite a data final')

    initial_datetime = datetime(year=initial_date.year, month=initial_date.month, day=initial_date.day)
    final_datetime = datetime(year=final_date.year, month=final_date.month, day=final_date.day)

    periods = (final_datetime - initial_datetime).days + 1    
    datelist = pd.date_range(initial_datetime, periods=periods)

    df = pd.DataFrame({
        'Data': datelist,
        'ano': [date.year for date in datelist],
        'mes': [date.month for date in datelist],
        'mes': [date.month for date in datelist],
        'dia_semana': [date.weekday() for date in datelist],
        'dia': [date.day for date in datelist],
    })
    
    best_model_almoco, best_model_janta = get_best_models()
    y_predict_almoco, y_predict_janta = predict(best_model_almoco, best_model_janta, df.drop(columns=['Data']))

    predicted_df_almoco, predicted_df_janta = create_predict_data(df, y_predict_almoco, y_predict_janta)

    fig1 = px.line(
        predicted_df_almoco,
        x='Data',
        y='Qt_almoco_pred',
    )
    
    fig1.update_traces(line_color='red')
    fig1.layout.update({'title': 'Predição: Almoço'})
    fig1.layout.yaxis.update({'title': 'Pratos servidos'})
    fig1.layout.xaxis.update({'title': 'Período'})



    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(
        predicted_df_janta,
        x='Data',
        y='Qt_jantar_pred',
    )
    fig2.update_traces(line_color='red')
    fig2.layout.update({'title': 'Predição: Jantar'})
    fig2.layout.yaxis.update({'title': 'Pratos servidos'})
    fig2.layout.xaxis.update({'title': 'Período'})

    st.plotly_chart(fig2, use_container_width=True)


custom_prediction()