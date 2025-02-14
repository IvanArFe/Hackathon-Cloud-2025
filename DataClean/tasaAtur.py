import sys
import os
import pandas as pd

data_path = './data/tasaAtur.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    dtype_mapping = { #mappeig tipus de dades
        "sexo": "string",
        "provincias": "string",
        "tasas": "string",
        "periodo": "string",
        "tasaAtur": "float",
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=";", decimal=",",
                     names=['sexo', 'provincias', 'tasas', 'periodo',
                            'tasaAtur'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)

    return df

def process_date(df):

    # si hi ha valors nulls eliminar la fila
    df = df.dropna()

    return df

df = read_file(data_path)
df = process_date(df)

print(df.head())
df.to_csv("dataClean/tasaAtur.csv", sep=';', index=False)