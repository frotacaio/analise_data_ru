import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import cross_validate, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDRegressor, LinearRegression
from sklearn.kernel_ridge import KernelRidge
from sklearn.ensemble import RandomForestRegressor

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from analise_data_ru import ROOT_PATH
from analise_data_ru.plot import get_almoco_and_janta_plot


train_df = pd.read_csv(ROOT_PATH / 'data' / 'processed' / 'train_data.csv')
test_df = pd.read_csv(ROOT_PATH / 'data' / 'processed' / 'test_data.csv')

X_almoco_train = train_df.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
y_almoco_train = train_df['Qt_almoco']

X_almoco_test = test_df.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
y_almoco_test = test_df['Qt_almoco']

X_janta_train = train_df.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
y_janta_train = train_df['Qt_jantar']

X_janta_test = test_df.drop(columns=['Qt_almoco', 'Qt_jantar', 'Data'])
y_janta_test = test_df['Qt_jantar']


krr_params = {
    'alpha': np.logspace(-6, 5, num=50, base=10),
    'kernel': ('rbf', 'sigmoid', 'poly', 'chi2', 'laplacian'),
    'gamma': np.logspace(-7, 1, num=50, base=10),
    'coef0': np.logspace(-2, 2, num=50, base=10),
    'degree': [3, 4],
}

mlp_regr_params = {
    'hidden_layer_sizes': np.random.randint(50, 1000, size=100),
    'activation': ('logistic', 'tanh', 'relu'),
    'solver': ('lbfgs', 'sgd', 'adam'),
    'alpha': np.logspace(-7, -1, num=50, base=10),
    'learning_rate': ('constant', 'invscaling', 'adaptive'),
}

random_forest = {
    'n_estimators': np.random.randint(80, 300, size=100),
    'criterion': ('squared_error', 'absolute_error', 'friedman_mse', 'poisson'),
    'max_features': ('sqrt', 'log2')
    
}

krr_search = RandomizedSearchCV(
    KernelRidge(), param_distributions=krr_params, n_iter=200, n_jobs=-1, verbose=10
)
mlp_search = RandomizedSearchCV(
    MLPRegressor(), param_distributions=mlp_regr_params, n_iter=200, n_jobs=-1, verbose=10
)

rf_search = RandomizedSearchCV(
    RandomForestRegressor(), param_distributions=random_forest, n_iter=200, n_jobs=-1, verbose=10
)

regressors_almoco = {
    'KRR': krr_search,
    'MLP_regr': mlp_search,
    'random_forest': rf_search,
}

regressors_janta = {
    'KRR': krr_search,
    'MLP_regr': mlp_search,
    'random_forest': rf_search,
}

trained_almoco_models = {}
for k, regr_almoco in regressors_almoco.items():
    print(f'Running Random Search for {k}:\n')
    regr_almoco.fit(X_almoco_train, y_almoco_train)
    print(f'Done {k}:\n')
    trained_almoco_models.update({k: regr_almoco.best_estimator_})

    with open(ROOT_PATH / 'models' / f'{k}_almoco.plk', 'wb') as almoco_file:
        pickle.dump(trained_almoco_models[k], almoco_file)

    print(f'saved: {k} in a binary file')

trained_janta_models = {}
for k, regr_janta in regressors_janta.items():
    print(f'Running the training for {k}:\n')
    regr_janta.fit(X_janta_train, y_janta_train)
    print(f'Done {k}:\n')
    trained_janta_models.update({k: regr_janta.best_estimator_})

    with open(ROOT_PATH / 'models' / f'{k}_janta.plk', 'wb') as janta_file:
        pickle.dump(trained_janta_models[k], janta_file)

    print(f'saved: {k} in a binary file')