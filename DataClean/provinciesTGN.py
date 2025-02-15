import pandas as pd

# Cargar los datos
preu_lloguer_path = './dataClean/preuLloguer.csv'
habTuristic_path = './dataClean/habTuristic.csv'

df_preu_lloguer = pd.read_csv(preu_lloguer_path, sep=";", decimal=".", encoding="utf-8")
df_hab_turistic = pd.read_csv(habTuristic_path, sep=";", decimal=".", encoding="utf-8")

# Preprocesar las columnas si es necesario
df_preu_lloguer["nomTerritori"] = df_preu_lloguer["nomTerritori"].str.strip()
df_hab_turistic["poblacio"] = df_hab_turistic["poblacio"].str.strip()

# Hacer el merge en base a las columnas correspondientes
df_merged = pd.merge(df_preu_lloguer, df_hab_turistic, left_on="nomTerritori", right_on="poblacio", how="inner")

# Guardar el resultado
df_merged.to_csv("dataClean/preuLloguer_NomesTGN.csv", sep=';', index=False)

print(df_merged.head())