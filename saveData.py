import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv


def save_csv_to_mongo(csv_filename):
    load_dotenv(dotenv_path='psswd.env')
    MONGO_URI = os.getenv("MONGO_URI")

    if not MONGO_URI:
        print("Error: MONGO_URI not found in environment variables.")
        return

    client = MongoClient(MONGO_URI)
    try:
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")

        # Buscar el archivo CSV en el sistema
        if not os.path.exists(csv_filename):
            print(f"Error: File '{csv_filename}' not found.")
            return

        # Leer el archivo CSV con separador ';'
        df = pd.read_csv(csv_filename, delimiter=';')
        data = df.to_dict(orient='records')

        # Obtener el nombre del archivo sin la extensión
        collection_name = os.path.splitext(os.path.basename(csv_filename))[0]

        # Insertar datos en MongoDB
        db = client['hackato-urv']
        collection = db[collection_name]
        collection.insert_many(data)
        print(f"Data from '{csv_filename}' inserted successfully into collection '{collection_name}' in MongoDB.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    csv_files = [f for f in os.listdir() if f.endswith(".csv")]
    for file in csv_files:
        save_csv_to_mongo(file)
