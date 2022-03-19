import json,discord,random

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
    
def open_bot_status():
    return open_json_file(r'/home/chris/Documents/pyapps/guild-manager/data/static/bot_status.json')
    

    
def make_emoji_str(string):
    emoji_string = ''
    for char in string:
        if char == " ":
            emoji_string += '    '
        else:
            emoji_string += f':{char.upper()}_:'
    return emoji_string

async def add_raid_emojis(message):
    
    emojis = [
        '<:1_:948050511502925944>','<:2_:948050511641333791>',
        '<:3_:948050511628734525>','<:4_:948050511578411128>',
        '<:Priest:948050245537890314>','<:Druid:948050245659557978>',
        '<:Hunter:948050245340774442>','<:Shaman:948050245554688010>',
        '<:Warrior:948050245491752961>','<:Mage:948050245391118337>',
        '<:Rogue:948050245193986059>','<:Paladin:948050245500141578>',
        '<:Warlock:948050245672108093>','<:Done:948280499049201744>',
        '<:Cancel:948777741094895687>'
    ]
    for emoji in emojis:
        await message.add_reaction(emoji)
        
async def get_message_reactions_by_member_id(msg,member_id):
        """
        This function returns a dictionary with values of which reactions a 
        """
        reactions = []
        for reaction in msg.reactions:
            async for user in reaction.users():
                if user.id == member_id:
                    reactions.append(reaction.emoji.id)
        return reactions
    
def check_for_valid_reactions(reactions):
    dismoji = open_discord_emotes()
    validDone = False
    className =''
    specNum = ''
    for reaction in reactions:
        if str(reaction) in dismoji['emotes']['class_emoji_ids']:
            className = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
        if str(reaction) in dismoji['emotes']['spec_emoji_ids']:
            specNum = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
        if str(reaction) in dismoji['emotes']['done_emoji']:
            validDone = True
    
    if specNum in dismoji['emotes']['class_spec'][className] and validDone:
        return f"{dismoji['emotes']['class_spec'][className][specNum]} {className}"
    return False
    
    # if validClass and validSpec and validDone:
    #     return True
    
async def set_bot_status(bot, status_activity, name):
    if status_activity == 'playing':
        await bot.change_presence(activity=discord.Game(name=name))
    elif status_activity == 'listening':
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
    elif status_activity == 'watching':
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))

async def pick_random_bot_status(bot):
    status = open_bot_status()
    rannum = random.randint(0,len(status))
    await set_bot_status(bot,status[rannum]['activity_status'],status[rannum]['activity_text'])
    

