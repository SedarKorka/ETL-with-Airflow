import pandas as pd
from datetime import datetime

# Lire le fichier extrait
df = pd.read_csv('/workspaces/ETL-with-Airflow/lab/manual/manual-extract-data.csv',
                 comment='#',
                 header=None,
                 names=['Domain'])

# Vérifier les données
print("Données brutes:")
print(df.head(10))
print(f"Total domaines: {len(df)}")

# Ajouter la date d'aujourd'hui
df['date'] = datetime.now().strftime('%Y-%m-%d')

# Sauvegarder
df.to_csv('/workspaces/ETL-with-Airflow/lab/manual/manually-transform-data.csv', 
          index=False)

print("\nTransformation terminée ✅")
print(f"Fichier sauvegardé avec {len(df)} domaines")