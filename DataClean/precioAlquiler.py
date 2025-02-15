import sys
import os
import pandas as pd

data_path = './data/preu_lloguer.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    dtype_mapping = { #mappeig tipus de dades
        "ambitTerritorial": "string",
        "codiTerritorial": "string",
        "nomTerritori": "string",
        "any": "Int64",
        "periode": "string",
        "habitatges": "Int64",
        "renda": "float",
        "tramPreus": "string"
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=",", decimal=".",
                     names=['ambitTerritorial', 'codiTerritorial', 'nomTerritori', 'any',
                            'periode', 'habitatges', 'renda', 'tramPreus'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)

    return df

def process_date(df):
    # eliminar columnes irrellevants
    df = df.drop(columns=['codiTerritorial'])

    # si hi ha valors nulls eliminar la fila
    df = df.dropna(subset=["habitatges", "renda"])
    df["nomTerritori"] = df["nomTerritori"].str.split(",", n=1, expand=True)[0]

    return df

df = read_file(data_path)
df = process_date(df)

print(df.head())
df.to_csv("dataClean/preuLloguer.csv", sep=';', index=False)