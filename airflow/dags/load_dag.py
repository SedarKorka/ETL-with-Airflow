from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='load_dag',
    description='DAG Load - Top Level Domains',
    schedule_interval='@daily',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    load_task = BashOperator(
        task_id='load_task',
        bash_command='sqlite3 /workspaces/ETL-with-Airflow/lab/orchestrated/airflow-load-db.db -cmd ".mode csv" ".import /workspaces/ETL-with-Airflow/lab/orchestrated/airflow-transform-data.csv top_level_domains"',
    )