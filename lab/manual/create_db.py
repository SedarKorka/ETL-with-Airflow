import sqlite3

# Créer la base de données
conn = sqlite3.connect('manual-load-db')
cursor = conn.cursor()

# Créer la table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS top_level_domains (
        Domain TEXT,
        date TEXT
    )
''')

conn.commit()
conn.close()
print("Base de données créée ✅")