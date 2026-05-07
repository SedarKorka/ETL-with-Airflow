from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='one_task_dag',
    description='Mon premier DAG',
    schedule_interval='@daily',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    task_one = BashOperator(
        task_id='one_task',
        bash_command='echo Hello LinkedIn Learning > /tmp/createthisfile.txt',
    )