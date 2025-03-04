from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from my_python_functions import create_time_csv_sample

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['alert@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'create_time_csv_sample',
    default_args=default_args,
    description='Create a csv file every time this dag is run.',
    schedule_interval=timedelta(minutes=15),
    start_date=datetime(2023, 10, 1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='create_time_csv_sample',
        python_callable=create_time_csv_sample,
    )

    task1