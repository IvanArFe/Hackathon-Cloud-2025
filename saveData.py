import os
import sys
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path='psswd.env')

# Get the MONGO_URI from the environment
MONGO_URI = os.getenv("MONGO_URI")

print(f'DATABASE_URL: {MONGO_URI}')

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # add an element to the collection
    db = client['hackato-urv']
    collection = db['local']
    data = {"name": "John", "age": 30}
    collection.insert_one(data)
    print("Data inserted successfully")
except Exception as e:
    print(e)