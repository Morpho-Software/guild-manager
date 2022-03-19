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
    #       self.collection.insert_one(item)
        
        
    #########
    # Raids #
    #########
    
    def update_raid(self, raid_id, raid):
        query = {"raidId":raid_id}
        self.collection.update_one(query,raid)
        
    def set_raid_posting_msg(self, raid_id, raid_posting_msg):
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        update = {
            "$set": {
                "raid_posting_msg":str(raid_posting_msg.id)
            }
        }
        self.collection.update_one(query,update)
        
    def add_character_to_raid_signup(self, character, raid_id):
        
        
    def confirm_raid(self,raid_id):
        self.set_collection('raids')
        query={"raid_id":raid_id}
        update = {
            "$set": {
                "raid_confirmed":True
            }
        }
        self.collection.update_one(query,update)
        
    
    def insert_new_raid(self, raid):
        self.set_collection('raids')
        self.collection.insert_one(raid)
    
    def find_raid_by_raid_id(self, raid_id):
        self.set_collection('raids')
        return self.collection.find_one({"raid_id":raid_id})
        
    def find_raid_by_confirmation_message_id(self, confirm_msg_id):
        self.set_collection('raids')
        return self.collection.find_one({"raid_disc_confirm_message":str(confirm_msg_id)})
    
    def find_raid_by_posting_message_id(self, posting_msg_id):
        self.set_collection('raids')
        return self.collection.find_one({"raid_posting_msg":str(posting_msg_id)})
        
        
    def get_raid_count(self):
        self.set_collection('raids')
        count = list(self.collection.find({}))
        return len(count)
    
    ###########
    # Raiders #
    ###########
    
    def insert_new_raider(self, raider):
        self.set_collection('raiders')
        self.collection.insert_one(raider)
        
    def find_raider_by_discord_member_id(self, discord_member_id):
        self.set_collection('raiders')
        return self.collection.find_one({"discord_member_id":str(discord_member_id)})
    
    def get_raider_count(self):
        self.set_collection('raiders')
        count = list(self.collection.find({}))
        return len(count)
    
    def add_character_to_raider(self, discord_member_id, character_id):
        raider = self.find_raider_by_discord_member_id(discord_member_id)
        raider['characters'].append(character_id)
        self.set_collection('raiders')
        query = {"discord_member_id":str(discord_member_id)}
        update = {
            "$set":{
                "characters":raider['characters']
            }
        }
        self.collection.update_one(query,update)
        
    ###################
    #   Characters    #
    ###################
    
    def find_character_by_raider_and_class_spec(self, discord_member_id, class_specialization):
        self.set_collection('characters')
        return self.collection.find_one({"discord_member_id":str(discord_member_id),"class_specialization":class_specialization})
    
    def insert_new_character(self, character):
        self.set_collection('characters')
        self.collection.insert_one(character)
        
    def find_character_by_character_id(self, character_id):
        self.set_collection('characters')
        return self.collection.find_one({"character_id":str(character_id)})
    
    def get_character_count(self):
        self.set_collection('characters')
        count = list(self.collection.find({}))
        return len(count)
        
        
    ################
    #   Setters    #
    ################
    
    def set_collection(self, COLLECTION_NAME):
        self.COLLECTION_NAME = COLLECTION_NAME
        self.collection = self.db[self.COLLECTION_NAME]