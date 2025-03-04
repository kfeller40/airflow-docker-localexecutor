from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from my_python_functions import print_date, sleep, echo_hello

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
    'example_python_dag',
    default_args=default_args,
    description='A simple tutorial DAG using PythonOperator',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 10, 1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='print_date',
        python_callable=print_date,
    )

    task2 = PythonOperator(
        task_id='sleep',
        python_callable=sleep,
    )

    task3 = PythonOperator(
        task_id='echo_hello',
        python_callable=echo_hello,
    )

    task1 >> task2 >> task3