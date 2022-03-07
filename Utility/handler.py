import requests, json
import xml.etree.ElementTree as ET
import xmltodict


class Handler:
    
    def __init__(self):
        with open('C:/Users/hellw/Desktop/PythonPrograms/DiscordRaidManager/Data/wow_classes.json') as json_file:
            self.wow_classes = json.load(json_file)
        json_file.close()
        
    def simple_handler(self,url,expected_return_type='json'):
        #request = requests.get()
        #request.status_code
        #return request.content
        if expected_return_type == 'json':
            return json.loads(requests.get(url).content)
        return requests.get(url).content
        
        
    def get_spec_bis_list(self,spec):
        return (self.simple_handler(f'https://wowtbc.gg/page-data/bis-list/{spec}/page-data.json'))['result']
        
    def get_all_bis_list(self):
        bis_list = []
        for wow_class in self.wow_classes:
            for spec in self.wow_classes[wow_class]['specs']:
                bis_list.append(self.get_spec_bis_list(f'{self.wow_classes[wow_class]["specs"][spec]["name"]}-{self.wow_classes[wow_class]["name"]}'))
        return bis_list
        
    #10004
    def get_item_from_wowhead_raw_xml(self, item_id):
        return (self.simple_handler(f'https://www.wowhead.com/item={item_id}&xml','xml'))
    
    def get_item_from_wowhead(self, item_id):
        raw_xml = self.get_item_from_wowhead_raw_xml(item_id)
        return xmltodict.parse(raw_xml)['wowhead']['item']
        #print(test['wowhead']['item']['name'])
        #print(test['wowhead']['item']['link'])
        
        
