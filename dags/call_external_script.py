from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'call_external_script',
    default_args=default_args,
    description='A simple DAG to call an external script',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

call_script = BashOperator(
    task_id='call_script',
    bash_command='python /external_scripts/current_time.py',
    dag=dag,
)

call_script