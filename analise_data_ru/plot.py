from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd


def get_almoco_and_janta_plot(data: pd.DataFrame, predicted_data: pd.DataFrame = None) -> None:
    domain = data['Data'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    df_almoco = data['Qt_almoco']
    df_janta = data['Qt_jantar']
    refeicoes_array = [df_almoco, df_janta]

    if predicted_data is not None:
        df_almoco_pred = predicted_data['Qt_almoco']
        df_janta_pred = predicted_data['Qt_jantar']
        refeicoes_pred_array = [df_almoco_pred, df_janta_pred]
        


    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12,8))

    labels = ['Valores reais']
    plots = []
    for index, r in enumerate(refeicoes_array):
        ax[index].spines[["top", "right"]].set_visible(False)
        
        plot_real = ax[index].plot(domain, r, label='Valores reais')
        plots.append(plot_real)

        ax[index].set_xticklabels(ax[index].get_xticklabels(), rotation=45)
        ax[index].set_ylabel('Quantidade')
        if predicted_data is not None:
            plot_predict = ax[index].plot(domain, refeicoes_pred_array[index], label='Predição')
            plots.append(plot_predict)
            labels.append('Predição')

    ax[0].set_title('Quantidade de pratos no Almoço')
    ax[1].set_title('Quantidade de pratos no Jantar')
    fig.legend(plots, labels=labels, loc='upper right',)

    plt.tight_layout()