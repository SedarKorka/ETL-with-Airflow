from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='two_task_dag',
    description='DAG avec 2 tâches',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    t0 = BashOperator(
        task_id='t0',
        bash_command='echo "First Airflow Task"',
    )

    t1 = BashOperator(
        task_id='t1',
        bash_command='sleep 5 && echo "Second Airflow Task"',
    )

    t0 >> t1