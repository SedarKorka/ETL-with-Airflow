from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

# Fonction Transform
def transform_data():
    today = datetime.now().strftime('%Y-%m-%d')
    
    df = pd.read_csv(
        '/workspaces/ETL-with-Airflow/lab/end-to-end/basic-etl-extract-data.csv',
        comment='#',
        header=None,
        names=['Domain']
    )
    
    df['date'] = today
    
    df.to_csv(
        '/workspaces/ETL-with-Airflow/lab/end-to-end/basic-etl-transform-data.csv',
        index=False
    )
    print(f"Transform terminé ✅ - {len(df)} domaines")

with DAG(
    dag_id='basic_etl_dag',
    description='DAG ETL Complet',
    schedule_interval='@daily',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # EXTRACT
    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='mkdir -p /workspaces/ETL-with-Airflow/lab/end-to-end && wget -c "https://data.iana.org/TLD/tlds-alpha-by-domain.txt" -O /workspaces/ETL-with-Airflow/lab/end-to-end/basic-etl-extract-data.csv',
    )

    # TRANSFORM
    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
    )

    # LOAD
    load_task = BashOperator(
        task_id='load_task',
        bash_command='sqlite3 /workspaces/ETL-with-Airflow/lab/end-to-end/basic-etl-load-db.db -cmd ".mode csv" ".import /workspaces/ETL-with-Airflow/lab/end-to-end/basic-etl-transform-data.csv top_level_domains"',
    )

    # DÉPENDANCES ETL
    extract_task >> transform_task >> load_task