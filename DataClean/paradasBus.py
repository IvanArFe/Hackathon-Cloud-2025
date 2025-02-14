import sys
import os
import pandas as pd

data_path = './data/paradasBus.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)
    "CODI", "NOM", "ADRECA", "LATITUD", "LONGITUD", "CODI_ENS", "NOM_ENS"
    dtype_mapping = { #mappeig tipus de dades
        "codi": "float",
        "nom": "string",
        "adreca": "string",
        "latitud": "float",
        "longitud": "float",
        "codiEns": "Int64",
        "nomEns": "string"
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=",", decimal=".",
                     names=['codi', 'nom', 'adreca', 'latitud',
                            'longitud', 'codiEns', 'nomEns'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)

    return df

def process_date(df):
    # eliminar columnes irrellevants
    df = df.drop(columns=['codiEns', 'nomEns'])

    return df

df = read_file(data_path)
df = process_date(df)

print(df.head())
df.to_csv("dataClean/paradesBus.csv", sep=';', index=False)