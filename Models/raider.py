import datetime, sys, os
from tokenize import String
sys.path.append('..')
from Utility.helper import open_raid_data
import uuid
class newraider():
    
    def __init__(self, payload):
        
        self.rd = open_raid_data()
        
        self.discord_member_id = str(payload.user_id)
        self.characters = []
        
    def to_dictionary(self) -> dict:
        return {
            "discord_member_id":self.discord_member_id,
            "characters":self.characters
        }
