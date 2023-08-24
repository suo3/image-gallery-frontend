import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv(dotenv_path="./.env.local")

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "admin")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "pass")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)


mongo_client = MongoClient(
    host=MONGO_URL,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    port=MONGO_PORT
)


def insert_test_document():
    db = mongo_client.test
    test_collection = db.test_collection
    res = test_collection.insert_one({"name": "Sam", "instructor": "Sam Fox"})
    print(res)
