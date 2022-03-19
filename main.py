
import discord, pprint, os, shlex, sys
from dotenv import load_dotenv
from Models.character import newcharacter
sys.path.append('..')
from Models.raid import newraid
from Models.raider import newraider as new_raider
from Models.character import newcharacter as new_character
from cEmbeds.raid import raid as raid_embed
from cEmbeds.raid_characters import raid_characters as new_character_embed
from Utility.helper import add_raid_emojis, pick_random_bot_status

from Controllers.mongocontroller import Mongodb
import Controllers.botcontroller as botcontroller

load_dotenv()

client = discord.Client()

command_keyword = 'sh/'

mongo = Mongodb('raids')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #If the bot is the author of the message, return nothing to avoid an infinite loop
    if message.author == client.user:
        return
    inc_username = str(message.author).split('#')[0]
    user_message = str(message.content)
    
    #Takes place in a discord
    if message.channel.type.name != 'private':
        await pick_random_bot_status(client)
        channel = str(message.channel.name)
        print(f'{inc_username}: {user_message} ({channel})')
        if message.channel.name == 'bot-closet':
            print(user_message)
            print(message.author)
            
            if message.content.startswith(command_keyword):
                
                inc_message_split = shlex.split(user_message)
                
                #This is a list of approved commands
                commands = [
                    "schedule",
                    "help"
                ]
                
                #This is the command the user passed
                command = inc_message_split[1]
                
                if command in commands:
                    if command == commands[0]: #Schedule
                        try:
                            
                            if len(inc_message_split) > 8:
                                raise Exception("Malformed Command -- Too many Arguments")
                            
                            newRaid = newraid(inc_message_split, message)
                            
                            embed = raid_embed(newRaid)
                            
                            sent_message = await message.channel.send(embed=embed.embed)
                            
                            await sent_message.add_reaction('<:Done:948280499049201744>')
                            await sent_message.add_reaction('<:Cancel:948777741094895687>')
                            
                            newRaid.set_confirm_message_id(sent_message.id)
                            
                            mongo.insert_new_raid(newRaid.to_dict())
                            
                        except Exception as e:
                            await message.channel.send(f'Tell Lord Gildu I am upset about: {e}')
                            return
    #Message coming from DM
    else:
        print("I hear ya")
                    

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    print(message_id)
    pprint.pprint(payload)
    
    #This stops the bot from running operations when it reacts to messages
    if payload.user_id == 933865497689198603:
        return
    
    #bot-closet
    if payload.channel_id == 933481167565488128:
        channel = client.get_channel(payload.channel_id)
        
        if mongo.find_raid_by_confirmation_message_id(payload.message_id):
            raid = mongo.find_raid_by_confirmation_message_id(payload.message_id)
            raid_confirm_msg = await channel.fetch_message(payload.message_id)
            
            if payload.emoji.name == 'Cancel':
                delete = await raid_confirm_msg.delete()
            if payload.emoji.name == 'Done':
                raid['raid_confirmed'][0] == True
                mongo.confirm_raid(raid['raid_id'])
                
                #azeroth-raids
                if raid['raid_game'] == 'classic':
                    channel = client.get_channel(933527657373663252)
                    embed = raid_embed(raid, False)
                    raid_public_post = await channel.send(embed=embed.embed)
                    mongo.set_raid_posting_msg(raid['raid_id'],raid_public_post)
                    await add_raid_emojis(raid_public_post)
                    
                    
                #outland-raids
                elif raid['raid_game'] == 'tbc':
                    channel = client.get_channel(933472914840387644)
                    embed = raid_embed(raid, False)
                    raid_public_post = await channel.send(embed=embed.embed)
                    mongo.set_raid_posting_msg(raid['raid_id'],raid_public_post)
                    await add_raid_emojis(raid_public_post)
                    
    #This code handles people reacting to the raid channels specifically
    elif payload.channel_id in [933527657373663252,933472914840387644]:
        await botcontroller.process_raid_signup(payload,mongo,client)

@client.event
async def on_raw_reaction_remove(payload):
    pass

client.run(os.environ['TOKEN'])