import pickle
from analise_data_ru import ROOT_PATH


def get_best_models():
    with open(ROOT_PATH / 'models' / 'best_model_almoco_padrao.plk', 'rb') as best_model_almoco:
        best_model_almoco = pickle.load(best_model_almoco)

    with open(ROOT_PATH / 'models' / 'best_model_janta_padrao.plk', 'rb') as best_model_janta:
        best_model_janta = pickle.load(best_model_janta)

    return best_model_almoco, best_model_janta