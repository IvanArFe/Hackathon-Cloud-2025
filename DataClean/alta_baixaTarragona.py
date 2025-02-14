import sys
import os
import pandas as pd

alta_path = './data/altaTarragona.csv'
baixa_path = './data/baixaTarragona.csv'
pd.set_option('display.max_columns', None) #mostar totes les columnes

def read_file(file_path, tipo):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    dtype_mapping = { #mappeig tipus de dades
        "any": "Int64",
        "mes": "Int64",
        "motiu": "string",
        "quantitat": "Int64",
        "codiEns": "Int64",
        "nomEns": "string"
    }
    # carregar fitxer amb ; i especificar les columnes
    df = pd.read_csv(file_path, sep=",", decimal=".",
                     names=['any', 'mes', 'motiu', 'quantitat',
                            'codiEns', 'nomEns'],
                     dtype=dtype_mapping, encoding="utf-8",
                     header=0)
    df["tipo"] = tipo

    return df

def process_date(df):
    # eliminar columnes irrellevants
    df = df.drop(columns=['codiEns', 'nomEns'])

    # si hi ha valors nulls eliminar la fila
    df = df.dropna(subset=["motiu"])

    return df

df = read_file(alta_path, "alta")
df = read_file(baixa_path, "baixa")
df = process_date(df)

print(df.head())