import datetime, sys, os
from tokenize import String
sys.path.append('..')
from Utility.helper import open_raid_data, open_raids
from Utility.mongo import Mongodb

class raid():
    
    def __init__(self, split_incoming_message, inc_msg):
        
        print(os.getcwd())
        rd = open_raid_data()
        #raids = open_raids()
        
        
        self.raid_name = self.validate_raid_name(rd,split_incoming_message[2])
        mdb = Mongodb('raids')
        self.raid_id = f'{rd[self.raid_name]["name"]}#{(mdb.get_raid_count())+1}'
        
        print(os.getcwd())
        
        split_year = split_incoming_message[3].split('/')
            
        year = int(split_year[2])
        month = int(split_year[1])
        day = int(split_year[0])
            
        self.datetime = datetime.datetime(
            year=year,
            month=month,
            day=day
        )
        
        self.message_id = None
            
        self.note = split_incoming_message[5]
        self.reocurring = split_incoming_message[6],
        self.confirmed = False,
        self.scheduler = str(inc_msg.author),
        self.raiders = {
            "tank":{
                "amount":[],
                "registered":[]
            },
            "dps":{
                "amount":[],
                "registered":[]
            },
            "healers":{
                "amount":[],
                "registered":[]
            }
        }
        self.set_raid_composition(rd)
        
    def set_raid_composition(self, rd) -> None:
        for raid in rd:
            if raid == self.raid_name:
                self.raiders['tank']['amount'] = rd[raid]['composition']['tank']['amount']
                self.raiders['dps']['amount'] = rd[raid]['composition']['dps']['amount']
                self.raiders['healers']['amount'] = rd[raid]['composition']['dps']['amount']
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
            "raid_disc_confirm_message":str(self.confirm_message_id)
        }
        return raid_dict