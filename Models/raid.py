import datetime, sys, os
from tokenize import String
sys.path.append('..')
from Utility.helper import open_raid_data, open_raids
from Controllers.mongocontroller import Mongodb

class newraid():
    
    def __init__(self, split_incoming_message, inc_msg):
        
        print(os.getcwd())
        rd = open_raid_data()
        #raids = open_raids()
        
        self.raid_name = self.validate_raid_name(rd,split_incoming_message[2])
        self.game = rd[self.raid_name]['game']
        mdb = Mongodb('raids')
        self.raid_id = f'{rd[self.raid_name]["name"]}#{(mdb.get_raid_count())+1}'
        
        split_year = split_incoming_message[3].split('/')
            
        year = int(split_year[2])
        month = int(split_year[1])
        day = int(split_year[0])
            
        self.datetime = datetime.datetime(
            year=year,
            month=month,
            day=day
        )
        
        self.raid_post_channel = None
        
        self.message_id = None
        self.mirrors = []
            
        self.note = split_incoming_message[5]
        self.reocurring = split_incoming_message[6],
        self.confirmed = False,
        self.scheduler = str(inc_msg.author.id),
        self.raiders = {
            "tank":{
                "amount":[],
                "registered":[],
                "reserves":[]
            },
            "damage":{
                "amount":[],
                "registered":[],
                "reserves":[]
            },
            "healer":{
                "amount":[],
                "registered":[],
                "reserves":[]
            }
        }
        self.set_raid_composition(rd)
        
    def set_raid_composition(self, rd) -> None:
        for raid in rd:
            if raid == self.raid_name:
                self.raiders['tank']['amount'] = rd[raid]['composition']['tank']['amount']
                self.raiders['damage']['amount'] = rd[raid]['composition']['damage']['amount']
                self.raiders['healer']['amount'] = rd[raid]['composition']['damage']['amount']
                break
        
    def validate_raid_name(self, rd, raid_name) -> String:
        isValidRaid = False
        for raid in rd:
            if raid_name in rd[raid]['alt_names']:
                raid_name = raid
                isValidRaid = True
                
        if raid_name not in rd and not isValidRaid:
            raise Exception(f"Raid '{self.raid_name}' not found")
        return raid_name
    
    def set_confirm_message_id(self, message_id):
        self.confirm_message_id = message_id
    
    def to_dict(self):
        raid_dict = {
            "raid_name":str(self.raid_name),
            "raid_id":str(self.raid_id),
            "raid_time":str(self.datetime),
            "raid_note":self.note,
            "raid_reoccuring":self.reocurring,
            "raid_confirmed":self.confirmed,
            "raid_scheduler":self.scheduler,
            "raid_raiders":self.raiders,
            "raid_disc_confirm_message":str(self.confirm_message_id),
            "raid_game":self.game,
            "raid_mirrors":self.mirrors
        }
        return raid_dict