from typing import Optional
import numpy as np
import pandas as pd
import streamlit as st

from analise_data_ru import ROOT_PATH


DATE_COLUMN = 'date/time'
DATA_URL = (
    'https://s3-us-west-2.amazonaws.com/'
    'streamlit-demo-data/uber-raw-data-sep14.csv.gz'
)

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


def load_ru_data(nrows: Optional[int] = None, raw: bool = False) -> pd.DataFrame:
    data = (
        pd.read_csv(ROOT_PATH / 'data' / 'processed' / 'final_base.csv', nrows=nrows)
        if raw is False else pd.read_csv(ROOT_PATH / 'data' / 'raw' / 'data_ru.csv', nrows=nrows)
    )
    return data


def get_split_data() -> tuple[pd.DataFrame]:
    train_df = pd.read_csv(ROOT_PATH / 'data' / 'processed' / 'train_data.csv')
    test_df = pd.read_csv(ROOT_PATH / 'data' / 'processed' / 'test_data.csv')
    return train_df, test_df


def create_predict_data(data, y_almoco_pred, y_janta_pred, compare: bool = False):
    if compare:
        predicted_df_almoco = pd.DataFrame(
            {
                'Data': data['Data'],
                'Qt_almoco': data['Qt_almoco'],
                'Qt_almoco_pred': np.ceil(y_almoco_pred),        
            }
        )
        predicted_df_janta = pd.DataFrame(
            {
                'Data': data['Data'],
                'Qt_jantar': data['Qt_jantar'],
                'Qt_jantar_pred': np.ceil(y_janta_pred),        
            }
        )
    else:
        predicted_df_almoco = pd.DataFrame(
            {
                'Data': data['Data'],
                'Qt_almoco_pred': np.ceil(y_almoco_pred),        
            }
        )
        predicted_df_janta = pd.DataFrame(
            {
                'Data': data['Data'],
                'Qt_jantar_pred': np.ceil(y_janta_pred),        
            }
        )
    return predicted_df_almoco, predicted_df_janta
