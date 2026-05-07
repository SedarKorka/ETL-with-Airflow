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

    # Lire le fichier extrait
    df = pd.read_csv(
        '/workspaces/ETL-with-Airflow/lab/challenge/challenge-extract-data.csv'
    )

    print("Colonnes disponibles:", df.columns.tolist())
    print(df.head())

    # Compter les entreprises par secteur
    sector_counts = df.groupby('GICS Sector').size().reset_index(name='count')

    # Ajouter la date
    sector_counts['date'] = today

    print(f"Secteurs trouvés: {len(sector_counts)}")
    print(sector_counts)

    # Sauvegarder
    sector_counts.to_csv(
        '/workspaces/ETL-with-Airflow/lab/challenge/challenge-transform-data.csv',
        index=False
    )
    print("Transform terminé ✅")

with DAG(
    dag_id='challenge_dag',
    description='Challenge DAG - S&P 500 par secteur',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # EXTRACT
    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='wget -c "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv" -O /workspaces/ETL-with-Airflow/lab/challenge/challenge-extract-data.csv',
    )

    # TRANSFORM
    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
    )

    # LOAD
    load_task = BashOperator(
        task_id='load_task',
        bash_command='sqlite3 /workspaces/ETL-with-Airflow/lab/challenge/challenge-load-db.db -cmd ".mode csv" ".import /workspaces/ETL-with-Airflow/lab/challenge/challenge-transform-data.csv sp500_sectors"',
    )

    # DÉPENDANCES
    extract_task >> transform_task >> load_task