import datetime, sys, os
from tokenize import String
sys.path.append('..')
from Utility.helper import open_raid_data, open_raids, write_dict_to_json
from Utility.mongo import Mongodb


class newraider():
    
    
    def __init__(self, inc_msg, payload, reactors):
        
        rd = open_raid_data()
        print(rd)
        
        
        
        
    
