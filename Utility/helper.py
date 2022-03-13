import json

def write_dict_to_json(dictionary,file):
    j = json.dumps(dictionary, indent=4)
    f = open(file, 'w')
    f.write(j)
    f.close()
    
def open_json_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
    json_file.close()
    return data

def open_discord_emotes():
    return open_json_file(r'/home/chris/Documents/pyapps/guild-manager/data/static/discord_emotes.json')
    
def open_raid_data():
    return open_json_file(r'/home/chris/Documents/pyapps/guild-manager/data/static/raid_data.json')
    
def open_raids():
    return open_json_file(r'/home/chris/Documents/pyapps/guild-manager/data/db/raids.json')

def write_raids(raids):
    write_dict_to_json(raids,r'/home/chris/Documents/pyapps/guild-manager/data/db/raids.json')
    

    
def make_emoji_str(string):
    emoji_string = ''
    for char in string:
        if char == " ":
            emoji_string += '    '
        else:
            emoji_string += f':{char.upper()}_:'
    return emoji_string