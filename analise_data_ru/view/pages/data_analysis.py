import streamlit as st

from analise_data_ru.view.data import load_ru_data
from plotly import figure_factory as ff
import plotly.express as px


def data_analysis():
    st.title('Análise de Dados Exploratória')
    st.sidebar.title('Análise de dados exploratória')
    st.markdown(
        'A tabela abaixo mostra algumas informações como por exemplo a média dos valores de cada'
        ' coluna,a quantidade, valores mínimos e máximos e os quartis'
    )

    processed_data = load_ru_data()
    st.dataframe(processed_data[['Qt_almoco', 'Qt_jantar']].describe().transpose())

    st.markdown(
        'Observando a tabela acima podemos concluir que:'
    )
    st.markdown(
        '* A média de almoço é maior que a de janta, ou seja, os estudantes vão mais para almoçar do que jantar.'
    )

    almoco_array = processed_data['Qt_almoco'].to_numpy()
    janta_array = processed_data['Qt_jantar'].to_numpy()

    left_col, right_col = st.columns(2)

    with left_col:
        fig1 = ff.create_distplot(
            [almoco_array],
            ['Almoço'],
            bin_size=[24],
        )
        fig1.layout.update({'title': 'Distribuição de dados do almoço'})

        st.plotly_chart(fig1, use_container_width=True)

    with right_col:
        fig2 = ff.create_distplot(
            [janta_array],
            ['Jantar'],
            bin_size=[24],
            colors=['orange']
        )
        fig2.layout.update({'title': 'Distribuição de dados do jantar'})

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown(
        'O que se conclui pelo histogrma é que os dados não seguem a distribuição normal.'
    )



data_analysis()