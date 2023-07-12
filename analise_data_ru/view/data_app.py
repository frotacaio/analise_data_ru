import streamlit as st
import pandas as pd

from analise_data_ru.view.data import load_ru_data
from analise_data_ru import ROOT_PATH


def main() -> None:
    st.title('DataApp RU')
    st.sidebar.title('DataApp RU')

    st.markdown('## Processo OSEMN')

    st.markdown('### Obtain(Obter)')
    st.markdown(
        'Nesta etapa, os cientistas de dados identificam as fontes de dados relevantes para o projeto.'
        ' Isso pode envolver a coleta de dados brutos de várias fontes, como bancos de dados, APIs,'
        ' arquivos CSV, textos da web, entre outros. É importante considerar as questões de privacidade'
        ' e ética ao obter os dados necessários para o projeto.'
    )
    
    st.markdown('### Scrub(Preparar)')
    st.markdown(
        'Após a obtenção dos dados, eles precisam ser preparados para análise. Isso inclui a limpeza dos dados,'
        ' removendo valores ausentes, tratando outliers e lidando com quaisquer problemas de qualidade dos dados.'
        ' Além disso, pode envolver a seleção das variáveis relevantes para o projeto e a transformação dos dados'
        ' em um formato adequado para a análise.'
    )
    
    st.markdown('### Explore(Explorar)')
    st.markdown(
        'Nesta etapa, os cientistas de dados exploram os dados por meio de análises estatísticas e visualizações.'
        ' Eles procuram padrões, tendências e insights preliminares nos dados. Isso pode envolver a aplicação de'
        ' técnicas de visualização de dados, como gráficos, histogramas e diagramas de dispersão, bem como a execução'
        ' de análises estatísticas descritivas para resumir os dados.'
    )
    
    st.markdown('### Model(Modelagem)')
    st.markdown(
        'Uma vez que os dados tenham sido explorados, é possível construir modelos estatísticos ou algoritmos de aprendizado'
        ' de máquina para fazer previsões ou tomar decisões. Essa etapa envolve a seleção e construção de modelos apropriados'
        ' para o problema em questão, bem como a avaliação e otimização desses modelos.'
    )

    st.markdown('### iNterpret(Interpretação)')
    st.markdown(
        'Este passo se mostra relevante para dar significado ao que o modelo apresentou como saída, o que aquela predição'
        ' representa e como ela pode ser aplicada. Esse tipo de inferência pode ser apresentada de forma gráfica, permitindo'
        ' um melhor entendimento por parte do público-alvo da solução.'
    )

    

    if st.sidebar.checkbox('Mostrar dados não preprocessados'):
        raw_data = load_ru_data(200, raw=True)
        st.subheader('Dados não processados')
        st.dataframe(raw_data)

    processed_data = load_ru_data(200)
    st.subheader('Banco de dados do RU (Dados após preprocessamento)')
    st.dataframe(processed_data.style)
    

if __name__ == '__main__':
    main()