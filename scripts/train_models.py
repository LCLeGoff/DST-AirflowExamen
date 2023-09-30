import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from joblib import dump


def get_model_from_name(model_name):
    model = None
    if model_name == 'LinearRegression':
        model = LinearRegression()
    elif model_name == 'DecisionTree':
        model = DecisionTreeRegressor()
    elif model_name == 'RandomForest':
        model = RandomForestRegressor()
    return model


def compute_model_score(model_name):

    X, y = prepare_data('./clean_data/fulldata.csv')

    model = get_model_from_name(model_name)

    cross_validation = cross_val_score(
        model,
        X,
        y,
        cv=3,
        scoring='neg_mean_squared_error')

    model_score = cross_validation.mean()

    return model_score


def train_and_save_model(model_name, X, y, path_to_model='./clean_data/best_model.pickle'):

    model = get_model_from_name(model_name)

    # training the model
    model.fit(X, y)
    # saving model
    print(str(model), 'saved at ', path_to_model)
    dump(model, path_to_model)


def prepare_data(path_to_data='./clean_data/fulldata.csv'):
    # reading data
    df = pd.read_csv(path_to_data)
    # ordering data according to city and date
    df = df.sort_values(['city', 'date'], ascending=True)

    dfs = []

    for c in df['city'].unique():
        df_temp = df[df['city'] == c]

        # creating target
        df_temp.loc[:, 'target'] = df_temp['temperature'].shift(1)

        # creating features
        for i in range(1, 10):
            df_temp.loc[:, 'temp_m-{}'.format(i)
                        ] = df_temp['temperature'].shift(-i)

        # deleting null values
        df_temp = df_temp.dropna()

        dfs.append(df_temp)

    # concatenating datasets
    df_final = pd.concat(
        dfs,
        axis=0,
        ignore_index=False
    )

    # deleting date variable
    df_final = df_final.drop(['date'], axis=1)

    # creating dummies for city variable
    df_final = pd.get_dummies(df_final)

    features = df_final.drop(['target'], axis=1)
    target = df_final['target']

    return features, target


def train_best_model(score_lr, score_dt, score_rf):

    X, y = prepare_data('./clean_data/fulldata.csv')
    score_df = [
        ['LinearRegression', score_lr],
        ['DecisionTree', score_dt],
        ['RandomForest', score_rf],
    ]
    score_df = pd.DataFrame(score_df, columns=['model_name', 'score']).sort_values('score')
    best_model_name = score_df.iloc[-1].loc['model_name']

    train_and_save_model(best_model_name, X, y)
