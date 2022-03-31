
import discord, os, shlex, sys
from dotenv import load_dotenv
sys.path.append('..')
from Utility.helper import pick_random_bot_status
from Utility.bot_constants import *
from Controllers.mongocontroller import Mongodb
import Controllers.botcontroller as botcontroller

load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(
    intents=intents
)

mongo = Mongodb('raids')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(933472737874313258)
    channel = guild.get_channel(933473237428486154)
    await channel.send(f"You made it!")
    await member.send(f"Glad you're here!")

@bot.event
async def on_message(message):
    #If the bot is the author of the message, return nothing to avoid an infinite loop
    if message.author == bot.user:
        return
    inc_username = str(message.author).split('#')[0]
    user_message = str(message.content)
    
    #Takes place in a discord channel
    if message.channel.type.name != 'private':
        await pick_random_bot_status(bot)
        channel = str(message.channel.name)
        print(f'{inc_username}: {user_message} ({channel})')
        if message.channel.name == 'bot-closet':
            if message.content.startswith(COMMAND_KEYWORD):
                
                inc_message_split = shlex.split(user_message)
                
                #This is a list of approved commands
                commands = [
                    "schedule",
                    "help", #remove obselete
                    "absent",
                    "info",
                    "edit"
                ]
                
                #This is the command the user passed
                command = inc_message_split[1]
                
                if command in commands:
                    if command == commands[0]: #Schedule
                        try:
                            
                            if len(inc_message_split) > 8:
                                raise Exception("Malformed Command -- Too many Arguments")
                            
                            await botcontroller.process_schedule_raid(message,mongo,inc_message_split)
                            
                        except Exception as e:
                            await message.channel.send(f'Tell Lord Gildu I am upset about: {e}')
                            return
                    elif command == commands[2]: #absent
                        try:
                            
                            if len(inc_message_split) > 4:
                                raise Exception("[BOOOOOOP]")
                            
                            await botcontroller.mark_raid_attendance(bot,mongo,inc_message_split)
                        except Exception as e:
                            await message.channel.send(f'[ALERT][ALERT]Self-Destruct Sequence Engaged... 3...')
                            await message.channel.send(f'2....')
                            await message.channel.send(f'1....')
                            await message.channel.send('https://tenor.com/view/robot-freak-out-head-explode-mind-blown-gif-12345244')
                            return
                    elif command == commands[3]: #info
                        try:
                            if len(inc_message_split) > 3:
                                raise Exception("[ZAP]")
                            await botcontroller.send_raid_info_dm(bot,mongo,inc_message_split,message)
                        except Exception as e:
                            await message.channel.send(f'[ALERT]...Self-Destruct Sequence Engaged...[ALERT]')
                            await message.channel.send(f'3....')
                            await message.channel.send(f'2....')
                            await message.channel.send(f'1....')
                            await message.channel.send('https://tenor.com/view/robot-freak-out-head-explode-mind-blown-gif-12345244')
                            await message.channel.send(f'{e}')
                            return
                    # elif command == commands[4]: #edit
                    #     try:
                    #         if len(inc_message_split) > 8:
                    #             raise Exception["[BAAAAZINGA]"]
                        
                    #         await botcontroller.edit_raid(bot,mongo,inc_message_split,message)
                    #     except Exception as e:
                    #         await message.channel.send(f'[ALERT]...Self-Destruct Sequence Engaged...[ALERT]')
                    #         await message.channel.send(f'3....')
                    #         await message.channel.send(f'2....')
                    #         await message.channel.send(f'1....')
                    #         await message.channel.send('https://tenor.com/view/robot-freak-out-head-explode-mind-blown-gif-12345244')
                    #         await message.channel.send(f'{e}')
                            
    #Message coming from DM
    else:
        #handle naming characters
        sunhoof_member = await botcontroller.get_guild_member_id_by_guild_id_user_id(message.author.id,933472737874313258,bot)
        character = mongo.find_character_empty_name_by_discord_member_id(sunhoof_member.id)
        if character:
            raid = mongo.find_raid_by_character_id_from_temp(character['character_id'])
            channel = await bot.fetch_channel(raid['raid_posting_channel'])
            raid_msg = await channel.fetch_message(raid['raid_posting_msg'])
            character = mongo.set_character_name(character['character_id'],str(message.content))
            
            mongo.add_character_to_raid_signup(character,raid,sunhoof_member)
            #Add raid point to character and update in DB
            character['raid_points'][raid['raid_name']]['points'] = character['raid_points'][raid['raid_name']]['points'] + 1
            mongo.replace_character(character)
            
            await botcontroller.send_raid_signup_confirm_from_dm(raid, character,sunhoof_member)
            await botcontroller.update_raid_signup_message(raid,raid_msg)
            await botcontroller.update_raid_signup_message_mirrors(raid,bot)
        else:
            dm = await sunhoof_member.create_dm()
            message = await dm.send("https://tenor.com/view/puppet-awkward-looking-what-side-eye-gif-15476992")
            
            
            

@bot.event
async def on_raw_reaction_add(payload):
    
    #This stops the bot from running operations when it reacts to messages
    if payload.user_id == 933865497689198603:
        return
    
    #This code handles people joining the discord
    if payload.channel_id == 933473675062161509:
        await botcontroller.process_add_sunhoof_role_selection(payload,mongo,bot)
    #This code handles people reacting to items in the raid closet
    if payload.channel_id == 933481167565488128:
        await botcontroller.process_bot_closet_reactions(payload,mongo,bot)
        
    #This code handles people reacting to the raid channels specifically
    elif payload.channel_id in [933527657373663252,933472914840387644]:
        #This code is executed when someone reacts to one of the raid signups
        await botcontroller.process_raid_signup(payload,mongo,bot)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 933473675062161509:
        await botcontroller.process_remove_sunhoof_role_selection(payload,mongo,bot)
    

bot.run(os.environ['TOKEN'])