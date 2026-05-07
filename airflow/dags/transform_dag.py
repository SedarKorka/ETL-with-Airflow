from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

# Fonction de transformation
def transform_data():
    # Date d'aujourd'hui
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Lire le fichier extrait
    df = pd.read_csv(
        '/workspaces/ETL-with-Airflow/lab/orchestrated/airflow-extract-data.csv',
        comment='#',
        header=None,
        names=['Domain']
    )
    
    print(f"Données lues: {len(df)} domaines")
    
    # Ajouter la date
    df['date'] = today
    
    # Sauvegarder
    df.to_csv(
        '/workspaces/ETL-with-Airflow/lab/orchestrated/airflow-transform-data.csv',
        index=False
    )
    
    print(f"Transformation terminée ✅ - {len(df)} domaines sauvegardés")

with DAG(
    dag_id='transform_dag',
    description='DAG Transform - Top Level Domains',
    schedule_interval='@daily',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
    )