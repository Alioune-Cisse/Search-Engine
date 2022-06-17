import sqlite3
from sqlite3 import Error
import pandas as pd


# Connexion à notre BDD
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# Récupération d'une table avec Pandas
def getdb(conn):
    
    df = pd.read_sql("SELECT * FROM GetData", conn)
    return df


# Fonction main()
def recupdf():
    database = r"C:/Users/lenovo/Desktop/TP1WebScraping/SenewebProject/extract_Seneweb_Data.db"

    conn = create_connection(database)
    with conn:
        return getdb(conn)
    
    conn.close()
