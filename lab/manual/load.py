import sqlite3
import pandas as pd

# Lire les données transformées
df = pd.read_csv('/workspaces/ETL-with-Airflow/lab/manual/manually-transform-data.csv')

print(f"Données à charger: {len(df)} domaines")

# Connecter à la base de données
conn = sqlite3.connect('/workspaces/ETL-with-Airflow/lab/manual/manual-load-db')

# Charger les données
df.to_sql('top_level_domains', conn, if_exists='append', index=False)

conn.close()
print("Load terminé ✅")