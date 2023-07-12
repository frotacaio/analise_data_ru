from sklearn.metrics import r2_score
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

from datetime import datetime
from plotly import figure_factory as ff

from analise_data_ru.view.data import create_predict_data, get_split_data
from analise_data_ru.models import get_best_models


def split_X_y_test(data):
    X_almoco_test = data.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
    y_almoco_test = data['Qt_almoco']

    X_janta_test = data.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
    y_janta_test = data['Qt_jantar']

    return X_almoco_test, y_almoco_test, X_janta_test, y_janta_test


def predict_almoco(model_almoco, test_data_almoco):
    return model_almoco.predict(test_data_almoco)


def predict_janta(model_janta, test_data_janta):
    return model_janta.predict(test_data_janta)


def regression():
    st.title('Aplicações dos modelos de Regressão')
    st.sidebar.title('Aplicações dos modelos de Regressão')
    st.markdown(
        'Abaixo são mostradas as aplicações dos modelos de regressão para a predição dos dados das series temporais apresentadas:'
    )

    st.markdown(
        'Os modelos testados foram os seguintes:'
    )

    left_col, right_col = st.columns(2)

    with left_col:

        st.markdown(
            '* **Kernel Ridge Regression (KRR)**\n'
            '* **MLP Regressor**\n'
        )

    with right_col:
        st.markdown(
            '* **Regressão Linear**\n'
            '* **Random Forest**'
        )

    train_data, test_data = get_split_data()

    st.markdown(
        'Os datasets foram serparados em:\n'
        f'* {train_data.shape[0]} dados de Treino\n'
        f'* {test_data.shape[0]} dados de Teste\n'
    )

    domain_train = train_data['Data'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
    domain_test = test_data['Data'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    left_col, right_col = st.columns(2)

    with left_col:
        fig1 = px.line(
            train_data,
            x=domain_train,
            y='Qt_almoco',
        )
        fig1.layout.update({'title': 'Dataset de treino: Almoço'})
        fig1.layout.yaxis.update({'title': 'Pratos servidos'})
        fig1.layout.xaxis.update({'title': 'Período'})

        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.line(
            train_data,
            x=domain_train,
            y='Qt_jantar',
        )
        fig2.update_traces(line_color='orange')
        fig2.layout.update({'title': 'Dataset de treino: Jantar'})
        fig2.layout.yaxis.update({'title': 'Pratos servidos'})
        fig2.layout.xaxis.update({'title': 'Período'})

        st.plotly_chart(fig2, use_container_width=True)

    with right_col:
        fig3 = px.line(
            test_data,
            x=domain_test,
            y='Qt_almoco',
        )
        fig3.layout.update({'title': 'Dataset de teste: Almoço'})
        fig3.layout.yaxis.update({'title': 'Pratos servidos'})
        fig3.layout.xaxis.update({'title': 'Período'})

        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.line(
            test_data,
            x=domain_test,
            y='Qt_jantar',
        )
        fig4.update_traces(line_color='orange')
        fig4.layout.update({'title': 'Dataset de teste: Jantar'})
        fig4.layout.yaxis.update({'title': 'Pratos servidos'})
        fig4.layout.xaxis.update({'title': 'Período'})

        st.plotly_chart(fig4, use_container_width=True)


    st.markdown(
        'Os melhores modelos encontrados para a predição de dados do almoço e jantar foram o **KRR** e **Random Forest**, respectivamente.'
    )

    best_model_almoco, best_model_janta = get_best_models()
    X_almoco_test, y_almoco_test, X_janta_test, y_janta_test = split_X_y_test(test_data)
    
    y_almoco_pred = predict_almoco(best_model_almoco, X_almoco_test)
    y_janta_pred = predict_janta(best_model_janta, X_janta_test)

    r2_almoco = r2_score(y_almoco_test, y_almoco_pred)
    r2_janta = r2_score(y_janta_test, y_janta_pred)

    st.markdown(
        f'* R2 Score para o **Random Forest** na predição dos dados de almoço: {r2_almoco.round(3)}\n'
        f'* R2 Score para **Random Forest** na predição dos dados de jantar: {r2_janta.round(3)}'
    )

    predicted_df_almoco, predicted_df_janta = create_predict_data(test_data, y_almoco_pred, y_janta_pred, compare=True)

    fig5 = px.line(
        predicted_df_almoco,
        x='Data',
        y=['Qt_almoco', 'Qt_almoco_pred'],
        color_discrete_map={
                 "Qt_almoco": "blue",
                 "Qt_almoco_pred": "red"
             }
    )
    
    fig5.layout.update({'title': 'Predição dos dados de teste: Almoço'})
    fig5.layout.yaxis.update({'title': 'Pratos servidos'})
    fig5.layout.xaxis.update({'title': 'Período'})



    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.line(
        predicted_df_janta,
        x='Data',
        y=['Qt_jantar', 'Qt_jantar_pred'],
        color_discrete_map={
                 "Qt_jantar": "orange",
                 "Qt_jantar_pred": "red"
             }
    )
    fig6.layout.update({'title': 'Predição dos dados de teste: Jantar'})
    fig6.layout.yaxis.update({'title': 'Pratos servidos'})
    fig6.layout.xaxis.update({'title': 'Período'})

    st.plotly_chart(fig6, use_container_width=True)
    
    


regression()