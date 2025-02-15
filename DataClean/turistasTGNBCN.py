import sys
import os
import pandas as pd

data_path = './data/turistasTGNBCN.csv'
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas


def detect_delimiter(file_path):
    """Detecta el delimitador del archivo leyendo la primera línea."""
    with open(file_path, "r", encoding="utf-8") as f:
        first_line = f.readline()
    if ";" in first_line:
        return ";"
    elif "," in first_line:
        return ","
    else:
        return None


def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR! File not found: {file_path}")
        sys.exit(1)

    # Detectar el delimitador automáticamente
    delimiter = detect_delimiter(file_path)
    if delimiter is None:
        print("ERROR: No se pudo detectar un delimitador válido.")
        sys.exit(1)

    # Cargar el archivo CSV
    try:
        df = pd.read_csv(file_path, sep=delimiter, decimal=",", encoding="utf-8", on_bad_lines="skip")
        print("Archivo cargado correctamente.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)

    print("Columnas detectadas:", df.columns)

    return df


def process_data(df):
    # Eliminar columnas irrelevantes si existen
    columns_to_drop = ['destinoTotalNacional', 'concepto', 'destinoComarca']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore')

    # Extraer año y mes si la columna "Periodo" existe
    if 'Periodo' in df.columns:
        df["año"] = df["Periodo"].astype(str).str[:4]
        df["mes"] = df["Periodo"].astype(str).str[5:]
    else:
        print("WARNING: No se encontró la columna 'Periodo' para extraer año y mes.")

    # Filtrar por 'CCAA y provincia de destino.2'
    provincias_validas = ["Tarragona", "Barcelona"]

    if 'CCAA y provincia de destino.2' in df.columns:
        df = df[df['CCAA y provincia de destino.2'].isin(provincias_validas)]
    else:
        print("WARNING: No se encontró la columna 'CCAA y provincia de destino.2' para filtrar.")

    return df


df = read_file(data_path)
df = process_data(df)

print(df.head())

# Guardar el archivo limpio y filtrado
output_path = "dataClean/turTGNBCN.csv"
df.to_csv(output_path, sep=';', index=False)
print(f"Archivo limpio y filtrado guardado en {output_path}")
