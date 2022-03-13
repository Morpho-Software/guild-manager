import discord, pprint, os, shlex, sys
from dotenv import load_dotenv
sys.path.append('..')
from Models.raid import raid
from cEmbeds.raid import raid as raid_embed
from Utility.helper import open_raids, write_raids
import json
from Utility.mongo import Mongodb

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
                        
                        newRaid = raid(inc_message_split, message)
                            
                        #raids = open_raids()  
                        #raids.append(newRaid.__dict__)
                        
                        
                        
                        embed = raid_embed(newRaid)
                        
                        #write_raids(raids)
                        
                        print(mongo.get_raid_count())
                        
                        sent_message = await message.channel.send(embed=embed.embed)
                        
                        newRaid.set_confirm_message_id(sent_message.id)
                        
                        mongo.insert_new_raid(newRaid.to_dict())
                        
                        
                    except Exception as e:
                        #print(f"unrecognized command given: {user_message}")
                        #await message.channel.send(f"unrecognized command given: {inc_message_split}")
                        await message.channel.send(f'Tell Lord Gildu I am upset about: {e}')
                        return
                    
                elif command == commands[1]: #help
                    emoji_string = 'help'
                    embed = discord.Embed(
                        title=emoji_string,
                        description="__Commands__",
                        color=discord.Color.gold()
                    )
                    embed.set_author(
                        name="Soulbeams",
                        icon_url="https://cdn.discordapp.com/attachments/933481167565488128/947780767310827550/WoWScrnShot_090521_044754.jpg"
                    )
                    
                    embed.add_field(
                        name="**sh/ schedule**",
                        value=f">>> To schedule raids and to make them reoccurring.\n\nType: sh/ schedule Raid Name Date(00/00/0000) Time(0:00PM/AM) \"Notes\" Yes/No(Reoccurring)\n\n```sh/ schedule Karazhan 01/01/2022 5:00PM \"We will meet beforehand.\" Yes```\n\n",
                        inline=False
                    )
                    embed.add_field(
                        name="**sh/ edit**",
                        value=f">>> To edit existing raids.\n\nType: sh/ edit Raid ID Raid Name Date(00/00/0000) Time(0:00PM/AM) \"Notes\" Yes/No(Reoccurring)\n\n",
                        inline=False
                    )
                    embed.add_field(
                        name="**sh/ absent**",
                        value=f">>> To mark players that were absent for raids that had signed up.\n\nType: sh/ absent Raid ID @name @name @name\n\n```sh/ absent Karazhan-2 @Gildu @Laelo```\n\n",
                        inline=False
                    )
                    #await message.channel.send(f'> {emoji_string}\n> The follow commands can be used: \n> **sh/** schedule\n> **sh/** help')
                    await message.channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    print(message_id)
    pprint.pprint(payload)
    
    #Bot Closet
    if payload.channel_id == 933481167565488128:
        print('here')
        
        if mongo.find
            
        
        
    
    if message_id == 948051241525719051:
        print("I saw it")
        guild_id = payload.guild_id
        #guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        #message = discord.utils.find(948051241525719051)
        #message.channel.send("I saw it")
        channel = client.get_channel(payload.channel_id)
        message = channel.fetch_message()
        await message.add_reaction(':SunHoof:')
        

        if payload.emoji.name == 'SunHoof':
            print("Sun Hoofer")
            dm = await payload.member.create_dm()
            await dm.send("HE_LLO - I AM WAS CREATED BY LORD GILDU. I DO SPEAK THALASSIAN PERFECTLY")

@client.event
async def on_raw_reaction_remove(payload):
    pass

client.run(os.environ['TOKEN'])