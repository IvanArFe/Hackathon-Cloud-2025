import sys
import os
import pandas as pd

data_path = './data/plazasTurismoTotales.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    dtype_mapping = { #mappeig tipus de dades
        "totalNacional": "string",
        "comunitatsAut": "string",
        "provincia": "string",
        "municipi": "string",
        "tipus": "string",
        "periode": "string",
        "total": "string"
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=";", decimal=",",
                     names=['totalNacional', 'comunitatsAut', 'provincia', 'municipi',
                            'tipus', 'periode', 'total'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)

    return df

def process_data(df):
    # eliminar columnes irrellevants
    df = df.drop(columns=['totalNacional'])

    df = df[df["provincia"].str.contains("tarragona", case=False, na=False)]
    df["municipi"] = df["municipi"].str.replace(r", L'$", "", regex=True)

    #extraer año y mes
    df["año"] = df["periode"].str[:4]  # año
    df["mes"] = df["periode"].str[5:]  # mes

    return df
df = read_file(data_path)
df = process_data(df)

print(df.head())
df.to_csv("dataClean/habTuristic.csv", sep=';', index=False)