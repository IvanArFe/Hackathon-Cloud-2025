import sys
import os
import pandas as pd

data_path = './data/relacionEconomica.csv'
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    # Cargar archivo con delimitador ";"
    df = pd.read_csv(file_path, sep=";", decimal=",", encoding="utf-8", header=0)

    # Eliminar columnas vacías detectadas por la presencia de ";"
    df = df.dropna(axis=1, how='all')  # Elimina columnas donde todos los valores son NaN

    return df

def process_data(df):
    # Eliminar filas con valores nulos en cualquier columna
    df = df.dropna()

    return df

df = read_file(data_path)
df = process_data(df)

print(df.head())

df.to_csv("dataClean/relEco.csv", sep=';', index=False)
print(f"Archivo limpio guardado en dataClean/relEco.csv")
