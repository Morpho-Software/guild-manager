
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
        self.class_emoji = ''
        self.spec_emoji = ''
        self.character_name = None
        self.character_race = None
        self.raid_points = {}
        self.registered = []
        self.attended = []
        self.canceled = []
        self.noshows = []
        self.reserves = []
        self.guild_canceled = []
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
            "class_emoji":self.class_emoji,
            "spec_emoji":self.spec_emoji,
            "specialization": self.specialization,
            "character_name": self.character_name,
            "character_race": self.character_race,
            "raid_points": self.raid_points,
            "registered": self.registered,
            "attended": self.attended,
            "canceled": self.canceled,
            "noshows": self.noshows,
            "reserves": self.reserves,
            "guild_canceled": self.guild_canceled,
            "equipment": self.equipment
        }
        
    def set_class_spec(self,reactions) -> None:
        dismoji = open_discord_emotes()
        validDone = False
        class_name = ''
        spec_num = ''
        spec_emoji = ''
        class_emoji = ''
        for reaction in reactions:
            if str(reaction) in dismoji['emotes']['class_emoji_ids']:
                class_name = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
                class_emoji = str(reaction)
            if str(reaction) in dismoji['emotes']['spec_emoji_ids']:
                spec_num = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
                spec_emoji = str(reaction)
            if str(reaction) in dismoji['emotes']['done_emoji']:
                validDone = True
        
        if spec_num in dismoji['emotes']['class_spec'][class_name] and validDone:
            self.class_name = class_name
            self.class_emoji = class_emoji
            self.spec_emoji = spec_emoji
            self.specialization = f"{dismoji['emotes']['class_spec'][class_name][spec_num]}"
            self.class_specialization = f"{dismoji['emotes']['class_spec'][class_name][spec_num]} {class_name}"
    
    def populate_raid_points(self) -> None:
        for raid in self.rd:
            if raid not in ['instance_name','World Bosses']:
                if self.rd[raid]['game'] == 'tbc' and 'tier' in self.rd[raid]:
                    self.raid_points[raid] = {"raid_name":raid,"points":0,"raid_tier":self.rd[raid]['tier']}
                elif self.rd[raid]['game'] == 'classic' and 'classic' not in self.raid_points:
                    self.raid_points['classic'] = {"raid_name":'Classic',"points":0}