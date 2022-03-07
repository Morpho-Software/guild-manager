import datetime, sys
from tkinter import E
from tokenize import String
sys.path.append('..')
from Utility.helper import open_raid_data, open_raids

class raid():
    
    def __init__(self, split_incoming_message, inc_msg):
        
        rd = open_raid_data()
        raids = open_raids()
        
        
        self.raid_name = self.validate_raid_name(rd,split_incoming_message[2])
        self.id = f'{rd[self.raid_name]["name"]}#{len(raids)+1}'
        
        
        
        split_year = split_incoming_message[3].split('/')
            
        year = int(split_year[2])
        month = int(split_year[1])
        day = int(split_year[0])
            
        self.datetime = datetime.datetime(
            year=year,
            month=month,
            day=day
        )
            
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