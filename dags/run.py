from scripts.add_new_data import add_new_raw_data_to_clean_data
from scripts.get_api_data import get_weather_data
from scripts.train_models import prepare_data, compute_model_score, train_best_model


get_weather_data()

add_new_raw_data_to_clean_data('data', 20)
add_new_raw_data_to_clean_data('fulldata', None)


X, y = prepare_data('./clean_data/fulldata.csv')
score_lr = compute_model_score('LinearRegression', X, y)
score_dt = compute_model_score('DecisionTree', X, y)
score_rf = compute_model_score('RandomForest', X, y)
train_best_model(X, y, score_lr, score_dt, score_rf)
