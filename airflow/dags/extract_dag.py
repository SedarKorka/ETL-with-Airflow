from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='extract_dag',
    description='DAG Extract - Top Level Domains',
    schedule_interval='@daily',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='mkdir -p /workspaces/ETL-with-Airflow/lab/orchestrated && wget -c "https://data.iana.org/TLD/tlds-alpha-by-domain.txt" -O /workspaces/ETL-with-Airflow/lab/orchestrated/airflow-extract-data.csv',
    )