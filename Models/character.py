
import uuid, sys
sys.path.append('..')
from Utility.helper import open_discord_emotes, open_raid_data, open_raids, write_dict_to_json

class newcharacter():
    
    def __init__(self, payload, raider_reactions):
        self.rd = open_raid_data()
        
        self.discord_member_id = str(payload.user_id)
        self.character_id = str(uuid.uuid4())
        self.confirmed = False
        self.class_name = ''
        self.class_specialization = ''
        self.specialization = ''
        self.character_name = None
        self.character_race = None
        self.raid_points = {}
        self.registered = []
        self.attended = []
        self.canceled = []
        self.noshows = []
        self.reserves = []
        self.equipment = {
            "head":{
                "name":"head",
                "item": ""
            },
            "shoulders":{
                "name":"shoulders",
                "item": ""
            },
            "chest":{
                "name":"chest",
                "item":""
            },
            "back":{
                "name":"back",
                "item":""
            },
            "neck":{
                "name":"neck",
                "item":""
            },
            "shirt":{
                "name":"shirt",
                "item":""
            },
            "tabard":{
                "name":"tabard",
                "item":""
            },
            "wrist":{
                "name":"wrist",
                "item":""
            },
            "hands":{
                "name":"hands",
                "item":""
            },
            "waist":{
                "name":"waist",
                "item":""
            },
            "legs":{
                "name":"legs",
                "item":""
            },
            "feet":{
                "name":"feet",
                "item":""
            },
            "finger":{
                "name":"ring",
                "left_hand":"",
                "right_hand":""
            },
            "trinket":{
                "name":"trinket",
                "left_ear":"",
                "right_ear":""
            },
            "relic":{
                "name":"relic",
                "item":""
            },
            "main-hand":{
                "name":"main-hand",
                "item":""
            },
            "off-hand":{
                "name":"off-hand",
                "item":""
            },
            "wand":{
                "name":"wand",
                "item":""
            },
            "ammo":{
                "name":"ammo",
                "item":""
            }
        }
        self.set_class_spec(raider_reactions)
        self.populate_raid_points()
        
    def to_dictionary(self) -> dict:
        return {
            "discord_member_id": self.discord_member_id,
            "character_id": self.character_id,
            "confirmed": self.confirmed,
            "class_name": self.class_name,
            "class_specialization": self.class_specialization,
            "specialization": self.specialization,
            "character_name": self.character_name,
            "character_race": self.character_race,
            "raid_points": self.raid_points,
            "registered": self.registered,
            "attended": self.attended,
            "canceled": self.canceled,
            "noshows": self.noshows,
            "reserves": self.reserves,
            "equipment": self.equipment
        }
        
    def set_class_spec(self,reactions) -> str:
        dismoji = open_discord_emotes()
        validDone = False
        className =''
        specNum =''
        for reaction in reactions:
            if str(reaction) in dismoji['emotes']['class_emoji_ids']:
                className = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
            if str(reaction) in dismoji['emotes']['spec_emoji_ids']:
                specNum = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
            if str(reaction) in dismoji['emotes']['done_emoji']:
                validDone = True
        
        if specNum in dismoji['emotes']['class_spec'][className] and validDone:
            self.class_name = className
            self.specialization = f"{dismoji['emotes']['class_spec'][className][specNum]}"
            self.class_specialization = f"{dismoji['emotes']['class_spec'][className][specNum]} {className}"
        return
    
    def populate_raid_points(self) -> None:
        for raid in self.rd:
            if raid not in ['instance_name','World Bosses'] and 'tier' in self.rd[raid]:
                self.raid_points[raid] = {"raid_name":raid,"points":0,"raid_tier":self.rd[raid]['tier']}