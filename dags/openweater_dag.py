import sys

sys.path.append('/app/')

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from scripts.get_api_data import get_weather_data
from scripts.add_new_data import add_new_raw_data_to_clean_data
from scripts.train_models import compute_model_score
from scripts.train_models import train_best_model


my_dag = DAG(
    dag_id='openweather_dag',
    description='openweather_dag',
    tags=['openweather', 'airflow_examen'],
    schedule_interval='* * * * *',
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(0),
    },
    catchup=False
)


get_data_from_api = PythonOperator(
    task_id='get_data_from_api',
    python_callable=get_weather_data,
    dag=my_dag
)

update_fresh_data = PythonOperator(
    task_id='update_fresh_data',
    python_callable=add_new_raw_data_to_clean_data,
    op_kwargs= {
        'filename': 'data', 
        'n_files': 20
    },
    dag=my_dag
)

update_fulldata = PythonOperator(
    task_id='update_fulldata',
    python_callable=add_new_raw_data_to_clean_data,
    op_kwargs= {
        'filename': 'fulldata', 
        'n_files': None
    },
    dag=my_dag
)

get_linear_regression_score = PythonOperator(
    task_id='get_linear_regression_score',
    python_callable=compute_model_score,
    op_kwargs= {
        'model_name': 'LinearRegression',
    },
    dag=my_dag
)


get_decision_tree_score = PythonOperator(
    task_id='get_decision_tree_score',
    python_callable=compute_model_score,
    op_kwargs= {
        'model_name': 'DecisionTree',
    },
    dag=my_dag
)

get_random_forest_score = PythonOperator(
    task_id='get_random_forest_score',
    python_callable=compute_model_score,
    op_kwargs= {
        'model_name': 'RandomForest',
    },
    dag=my_dag
)

train_best_model = PythonOperator(
    task_id='train_best_model',
    python_callable=train_best_model,
    dag=my_dag
)

get_data_from_api >> [update_fresh_data, update_fulldata]

update_fulldata >> [get_linear_regression_score, get_decision_tree_score, get_random_forest_score]

[get_linear_regression_score, get_decision_tree_score, get_random_forest_score] >> train_best_model