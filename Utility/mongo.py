import pymongo
from pymongo import MongoClient

class Mongodb():
    
    def __init__(self,COLLECTION_NAME,DB_NAME='guild_manager',MONGODB_HOST='localhost',MONGODB_PORT=27017):
        self.COLLECTION_NAME = COLLECTION_NAME
        self.DB_NAME = DB_NAME
        self.MONGODB_HOST = MONGODB_HOST
        self.MONGODB_PORT = MONGODB_PORT
        
        self.client = MongoClient(MONGODB_HOST,MONGODB_PORT)
        
        self.db = self.client[self.DB_NAME]
        self.collection = self.db[self.COLLECTION_NAME]
        
    # def insert_one_into_collection(self, item):
    #     self.collection.insert_one(item)
        
        
    #########
    # Raids #
    #########
    
    def update_raid(self, raid_id, raid):
        query = {"raidId":raid_id}
        self.collection.update(query,raid)
    
    def insert_new_raid(self, raid):
        self.set_collection('raids')
        self.collection.insert_one(raid)
    
    def find_raid_by_raid_id(self, raid_id):
        self.set_collection('raids')
        self.collection.find_one({"raidId":raid_id})
        
    def get_raid_count(self):
        self.set_collection('raids')
        count = list(self.collection.find({}))
        return len(count)
        
    ################
    #   Setters    #
    ################
    
    def set_collection(self, COLLECTION_NAME):
        self.COLLECTION_NAME = COLLECTION_NAME
        self.collection = self.db[self.COLLECTION_NAME]