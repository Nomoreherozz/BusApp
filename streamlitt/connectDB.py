import os

from dotenv                                             import load_dotenv
from pymongo.mongo_client                               import MongoClient


load_dotenv()

USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@m24.2v2vgpk.mongodb.net/?retryWrites=true&w=majority"

def connection():
    """ Create a new client and connect to the server """ 
    try:
        client = MongoClient(URI)
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client
    except Exception as e:
        print(e)

client = connection()

for x in client.find():
    print(x)