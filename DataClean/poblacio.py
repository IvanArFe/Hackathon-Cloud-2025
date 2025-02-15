import sys
import os
import pandas as pd

data_path = './data/poblacioTGN.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    dtype_mapping = { #mappeig tipus de dades
        "municipi": "string",
        "sexe": "string",
        "periode": "int",
        "total": "string"
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=";", decimal=",",
                     names=['municipi', 'sexe', 'periode', 'total'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)

    return df

def process_date(df):
    # si hi ha valors nulls eliminar la fila
    df = df.dropna().copy()

    #separar codi postal i poblacio
    df[["codi_postal", "poblacio"]] = df["municipi"].str.split(" ", n=1, expand=True)

    #eliminar article de la poblacio
    df["poblacio"] = df["poblacio"].str.split(",", n=1, expand=True)[0]
    return df

df = read_file(data_path)
df = process_date(df)

print(df.head())
df.to_csv("dataClean/poblacio.csv", sep=';', index=False)