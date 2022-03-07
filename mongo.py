from typing import Collection
import pymongo
from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'guild_manager'
COLLECTION_NAME = 'raids'



client = MongoClient(MONGODB_HOST,MONGODB_PORT)

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

collection.insert_one({"name":"sarah","looks":"beautiful"})

print("complete")