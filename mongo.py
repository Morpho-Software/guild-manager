import pymongo
from pymongo import MongoClient

class mongodb():
    
    def __init__(self,COLLECTION_NAME,DB_NAME='guild_manager',MONGODB_HOST='localhost',MONGODB_PORT=27017):
        self.COLLECTION_NAME = COLLECTION_NAME
        self.DB_NAME = DB_NAME
        self.MONGODB_HOST = MONGODB_HOST
        self.MONGODB_PORT = MONGODB_PORT
        
        self.client = MongoClient(MONGODB_HOST,MONGODB_PORT)
        
        self.db = self.client[self.DB_NAME]
        self.collection = self.collection[self.COLLECTION_NAME]
        
    def insert_one_into_collection(self, item):
        self.collection.insert_one(item)
        
        
        