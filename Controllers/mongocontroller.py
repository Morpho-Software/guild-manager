import pymongo, sys
from pymongo import MongoClient
sys.path.append('..')
from Utility.helper import open_wow_class_information
from cEmbeds.raid import raid as raid_embed

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
    
    def update_raid(self, raid_id, raid) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        self.collection.update_one(query,raid)
        
    def edit_raid(self,raid_id,replacement) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        self.collection.find_one_and_replace(query,replacement)
        
    def replace_raid(self,raid_id,raid) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        self.collection.replace_one(query,raid)
        
    def set_raid_datetime(self, raid_id, raid) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        update = {
            "$set": {
                "raid_datetime":str(raid['raid_datetime'])
            }
        }
        self.collection.replace_one(query,update)
        
    def set_raid_note(self, raid_id, raid) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        update = {
            "$set": {
                "raid_note":str(raid['raid_note'])
            }
        }
        self.collection.update_one(query,update)
        
    def set_raid_posting_msg(self, raid_id, raid_posting_msg) -> None:
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        update = {
            "$set": {
                "raid_posting_msg":str(raid_posting_msg.id)
            }
        }
        self.collection.update_one(query,update)
        
    def set_raid_posting_channel(self, raid_id, raid_posting_msg):
        self.set_collection('raids')
        query = {"raid_id":raid_id}
        update = {
            "$set":{
                "raid_posting_channel":str(raid_posting_msg.channel.id)
            }
        }
        self.collection.update_one(query,update)
        
        
    async def add_mirror_raid_post(self, raid, mirrors,bot) -> None:
        self.set_collection('raids')
        for mirror in mirrors:
            raid['raid_mirrors'].append(mirror)
            channel = await bot.fetch_channel(mirror['channel_id'])
            embed = raid_embed(raid, False)
            mirror_message = await channel.send(embed=embed.embed)
            raid['raid_mirrors'][len(raid['raid_mirrors'])-1]['message_id'] = mirror_message.id
        
        query = {"raid_id":raid['raid_id']}
        update = {
            "$set":{
                "raid_mirrors":raid['raid_mirrors']
            }
        }
        self.collection.update_one(query, update)
        
    def find_characters_by_discord_member_id(self,member_id):
        self.set_collection('characters')
        query = {"discord_member_id":str(member_id)}
        characters = self.collection.find(query)
        return characters
        
        
    def add_character_to_raid_signup(self, character, raid, member) -> None:
        #Add character Id to the raid first
        class_info = open_wow_class_information()
        role = class_info[character['class_name'].lower()]['specs'][character['specialization'].lower()]['roles']
        
        ticket = 'reserves'
        if len(raid['raid_raiders'][role]['registered'])<raid['raid_raiders'][role]['amount'][0]:
            ticket = 'registered'
        
        raid['raid_raiders'][role][ticket].append(
            {
                'character_id':character['character_id'],
                'character_name':character['character_name'],
                'discord_member_id':character['discord_member_id'],
                'discord_member_display_name':f'@{member.display_name}#{member.discriminator}'
            }
        )
        
        self.set_collection('raids')
        query = {"raid_id":raid['raid_id']}
        update = {
            "$set":{
                "raid_raiders":raid['raid_raiders']
            }
        }
        self.collection.update_one(query, update)
        
        #Add the raid Id to the character's signups
        self.set_collection('characters')
        query = {"character_id":character['character_id']}
        
        character[ticket].append(raid['raid_id'])
        
        update = {
            "$set":{
                ticket:character[ticket]
            }
        }
        self.collection.update_one(query, update)
    
    def find_character_empty_name_by_discord_member_id(self, discord_member_id):
        self.set_collection('characters')
        query = {
            "discord_member_id":str(discord_member_id),
            "character_name": None
        }
        return self.collection.find_one(query)
        
        
    def confirm_raid(self,raid_id) -> None:
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
    
    def get_all_registered_characters(self, raiders_list):
        characters = []
        self.set_collection('characters')
        for raider in raiders_list:
            characters.append({
                "character":self.find_character_by_character_id(raider['raider']['character_id']),
                "role":raider['role']
                })
        return characters
    
    def replace_character(self, character):
        self.set_collection('characters')
        query = {
            "character_id":character["character_id"]
        }
        self.collection.replace_one(query,character)
    
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
        
    def set_character_name(self,character_id,character_name):
        self.set_collection('characters')
        query = {"character_id":character_id}
        update = {
            "$set":{
                "character_name":character_name
            }
        }
        self.collection.update_one(query,update)
        return self.collection.find_one(query)
    
    def get_characters_registered_for_raid_by_raid_id(self,raid_id) -> list:
        raid = self.find_raid_by_raid_id(raid_id)
        registered_characters = []
        for character in raid['raid_raiders']['tank']['registered']:
            registered_characters.append(self.find_character_by_character_id(character['character_id']))
        for character in raid['raid_raiders']['damage']['registered']:
            registered_characters.append(self.find_character_by_character_id(character['character_id']))
        for character in raid['raid_raiders']['healer']['registered']:
            registered_characters.append(self.find_character_by_character_id(character['character_id']))
        return registered_characters
        
    #####################
    # Temporary Signups #
    #####################
        
    def find_raid_by_character_id_from_temp(self, character_id):
        self.set_collection('temp_signup')
        query = {"character_id":character_id}
        temp =  self.collection.find_one(query)
        raid = self.find_raid_by_raid_id(temp['raid_id'])
        return raid
    
    def temporary_signup_character(self,character_id,raid_id):
        self.set_collection('temp_signup')
        self.collection.insert_one({
            "character_id":character_id,
            "raid_id":raid_id
        })
        
    #####################
    #   Raid Continues  #
    #####################
    
    def link_raid_continues(self, raid, character, message):
        self.set_collection('raid_continues')
        self.collection.insert_one({
            "confirmation_status":"no_response",
            "character_id":character['character_id'],
            "raid_id":raid['raid_id'],
            "message_id":message.id,
            "discord_member_id":character['discord_member_id']
        })
        
    def find_raid_continue_by_message_id(self, message_id):
        """
        Returns a raid_continue if it's found
        """
        self.set_collection('raid_continues')
        query = {"message_id":message_id}
        return self.collection.find_one(query)


    ################
    #   Setters    #
    ################
    
    def set_collection(self, COLLECTION_NAME):
        self.COLLECTION_NAME = COLLECTION_NAME
        self.collection = self.db[self.COLLECTION_NAME]