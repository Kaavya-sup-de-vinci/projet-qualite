from sqlalchemy import create_engine
import urllib.parse
import pandas as pd
 
# Paramètres de connexion PostgreSQL
user = 'postgres'
password = 'Bjkbjkbjk56'
host = 'localhost'
port = '5432'
database = 'postgres'
 

 
# Créer l'URL de connexion
connection_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
 
# Charger le fichier CSV
csv_file_path = 'C:/Users/boral/OneDrive/Documents/Projet entrepôt données/dim_insee.csv'
 
try:
    # Création de l'objet SQLAlchemy engine
    engine = create_engine(connection_url)
   
    # Tester la connexion
    with engine.connect() as connection:
        print("Connexion réussie à la base de données !")
   
    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(csv_file_path, sep=';', encoding='utf-8')  
 

   
    # Importer le DataFrame dans PostgreSQL
    table_name = 'dim_insee'  # Nom de la table cible
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
 
    print(f"Table {table_name} importée avec succès dans la base de données.")
 
except Exception as e:
    print("Erreur :", e)