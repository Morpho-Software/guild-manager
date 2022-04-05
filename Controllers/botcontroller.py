import discord
import json,datetime
from Models.raider import newraider as new_raider
from Models.character import newcharacter as new_character
from Models.raid import newraid
from cEmbeds.raid_newcharacter import raid_characters as new_character_embed
from cEmbeds.raid import raid as raid_embed
from cEmbeds.signup_confirmation import signup_confirmation as signup_confirmation_embed
from cEmbeds.raid_ptsummary import raid_ptsummary as raid_ptsummary_embed
from cEmbeds.raid_continue import raid_continue as raid_continue_embed
from dateutil.parser import parse
from dateutil.tz import gettz

from Utility.helper import add_raid_emojis, get_message_reactions_by_member_id, check_for_valid_reactions, open_discord_emotes,open_raid_tier_data

async def leadership_chat(bot, msg) -> None:
    channel_id = '930981831308894288'
    #channel_id = '955234475661480006'
    channel = await bot.fetch_channel(channel_id)
    await channel.send(msg)

def get_class_spec(reactions) -> str:
    dismoji = open_discord_emotes()
    validDone = False
    className =''
    specNum =''
    for reaction in reactions:
        if str(reaction) in dismoji['emotes']['class_emoji_ids']:
            className = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
        if str(reaction) in dismoji['emotes']['spec_emoji_ids']:
            specNum = dismoji['emotes']['class_spec_emoji_ids'][str(reaction)]
        if str(reaction) in dismoji['emotes']['done_emoji']:
            validDone = True
        
    if specNum in dismoji['emotes']['class_spec'][className] and validDone:
        return f"{dismoji['emotes']['class_spec'][className][specNum]} {className}"

async def process_new_character(mongo,payload,reactor_reactions,raid) -> None:
    newcharacter = new_character(payload, reactor_reactions)
    mongo.insert_new_character(newcharacter.to_dictionary())
    mongo.add_character_to_raider(payload.user_id,newcharacter.character_id)
    mongo.temporary_signup_character(newcharacter.character_id,raid['raid_id'])
    dm = await payload.member.create_dm()
    embed=new_character_embed(raid,newcharacter,payload)
    message = await dm.send(embed=embed.embed)

async def process_new_raider(mongo,payload,reactor_reactions,raid) -> None:
    #This code runs if no account have ever been created with the raider
    newraider = new_raider(payload)
    mongo.insert_new_raider(newraider.to_dictionary())

async def process_add_sunhoof_role_selection(payload,mongo,bot) -> None:
    message_id = payload.message_id
    if message_id == 946989019236040714:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        
        if payload.emoji.name == 'Guest':
            role = discord.utils.get(guild.roles, name='Guest')
        elif payload.emoji.name in ['SunwellSociety','ThunderhoofTribe']:
            role = discord.utils.get(guild.roles, name='Sun-Hoofer')
            
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")
    else:
        pass

async def get_guild_member_id_by_guild_id_user_id(user_id, guild_id,bot) -> discord.Member:
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    member = discord.utils.find(lambda m : m.id == int(user_id), guild.members)
    return member

async def process_remove_sunhoof_role_selection(payload,mongo,bot) -> None:
    message_id = payload.message_id
    if message_id == 946989019236040714:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        
        if payload.emoji.name == 'Guest':
            role = discord.utils.get(guild.roles, name='Guest')
        elif payload.emoji.name in ['SunwellSociety','ThunderhoofTribe']:
            role = discord.utils.get(guild.roles, name='Sun-Hoofer')
            
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")
            
async def send_raid_continue_confirmation(raid,character,bot,mongo) -> None:
    #Send raid continue message to raiders in a raid that has an extenstion
    embed = raid_continue_embed()
    member = await get_guild_member_id_by_guild_id_user_id(character['discord_member_id'],933472737874313258,bot)
    dm = await member.create_dm()
    message = await dm.send(embed=embed.embed)
    mongo.link_raid_continues(raid,character,message)
    
    await message.add_reaction("<:Done:955361992883961896>")
    await message.add_reaction("<:Cancel:955362577267949598>")

async def send_raid_signup_confirmation(raid,character,payload) -> None:
    #Send signup confirmation
    embed = signup_confirmation_embed(raid,character,character['character_name'])
    dm = await payload.member.create_dm()
    message = await dm.send(embed=embed.embed)
    await message.add_reaction('🤖')
    
async def send_pulled_from_reserves_dm(raid, character,bot) -> None:
    embed = signup_confirmation_embed(raid,character,character['character_name'])
    member = await get_guild_member_id_by_guild_id_user_id(character['discord_member_id'],933472737874313258,bot)
    dm = await member.create_dm()
    message = await dm.send(embed=embed.embed)
    await message.add_reaction('🤖')

async def send_raid_signup_confirm_from_dm(raid, character, member) -> None:
    #Send signup confirmation used when adding from DM
    embed = signup_confirmation_embed(raid,character,member.display_name)
    dm = await member.create_dm()
    message = await dm.send(embed=embed.embed)

async def update_raid_signup_message(raid, raid_msg) -> None:
    #Update Raid Signup Message After someone is signed up
    embed = raid_embed(raid, False)
    await raid_msg.edit(embed=embed.embed)

async def update_raid_signup_message_mirrors(raid,bot) -> None:
    #Update Raid Mirrors
    for mirror in raid['raid_mirrors']:
        channel = await bot.fetch_channel(mirror['channel_id'])
        mirror_msg = await channel.fetch_message(mirror['message_id'])
        embed = raid_embed(raid, False, True)
        await mirror_msg.edit(embed=embed.embed)

def remove_character_from_raid(character,raid):
    character_role = ''
    for role in raid['raid_raiders']:
        for index,reg_character in enumerate(raid['raid_raiders'][role]['registered']):
            print(index,reg_character)
            if reg_character['character_id'] == character['character_id']:
                del raid['raid_raiders'][role]['registered'][index]
                character_role = role
                break
                
    return raid, character_role

def check_if_character_is_in_raid(character,raid):
    for signup_status in ['registered','reserves']:
        for role in raid['raid_raiders']:
            for reg_character in raid['raid_raiders'][role][signup_status]:
                if reg_character['character_id'] == character['character_id']:
                    return True
    return False
            
async def get_raid_signup_msg(channel_id,message_id,bot):
    channel = bot.get_channel(int(channel_id))
    raid_msg = await channel.fetch_message(int(message_id))
    return raid_msg
    
async def process_raid_signup(payload,mongo,bot) -> None:
    channel = bot.get_channel(payload.channel_id)
    raid_msg = await channel.fetch_message(payload.message_id)
    raid = mongo.find_raid_by_posting_message_id(raid_msg.id)
        
    if payload.emoji.name == 'Done':
        reactor_reactions = await get_message_reactions_by_member_id(raid_msg,payload.member.id)
        if len(reactor_reactions) == 3 and check_for_valid_reactions(reactor_reactions):
            #Check if reactor is in the database
            if mongo.find_raider_by_discord_member_id(payload.member.id):
                #raider exist
                #Check if character is in the database
                if mongo.find_character_by_raider_and_class_spec(payload.member.id,get_class_spec(reactor_reactions)):
                    character = mongo.find_character_by_raider_and_class_spec(payload.member.id,get_class_spec(reactor_reactions))
                    
                    if not check_if_character_is_in_raid(character, raid) or True:
                        #Now we can register this raider and character in the raid they reacted to.
                        mongo.add_character_to_raid_signup(character, raid, payload.member)
                        
                        #Add raid point to character and update in DB
                        character['raid_points'][raid['raid_name']]['points'] = character['raid_points'][raid['raid_name']]['points'] + 1
                        mongo.replace_character(character)
                        
                        await send_raid_signup_confirmation(raid, character, payload)
                        
                        await update_raid_signup_message(raid, raid_msg)
                        
                        await update_raid_signup_message_mirrors(raid, bot)
                    else:
                        print(f"{character['character_name']} is already in the raid!")
                    
                else:
                    await process_new_character(mongo,payload,reactor_reactions,raid)
            else:
                #raider does not exist so no characters exist either
                await process_new_raider(mongo, payload, reactor_reactions, raid)
                await process_new_character(mongo, payload, reactor_reactions, raid)
        else:
            #The user has failed to correctly fill out the reactions on a raid
            dm = await payload.member.create_dm()
            message = await dm.send(f"[Beeping and Whirring]\nGreetings! This is SQ-Bot 300X, programmed for your optimized battling experience by the Great Lord Gildu Soulbeam, now also an engineer.\nIn The Sun-Hoof Coalition, you have attempted to sign up for `{raid['raid_id']}`, but it is **incomplete**.\n\n*Please make sure you select: your **class** icon, your **class number** icon representing your specialization (found in #faq), and the **done** icon.\nIf you wish to cancel your sign-up, please select the cancel icon.*")
            await message.add_reaction('🤖')
    elif payload.emoji.name == 'Cancel':
        characters = mongo.find_characters_by_discord_member_id(payload.member.id)
        for character in characters:
            for signup_type in ['registered','reserves']:
                if raid['raid_id'] in character[signup_type]:
                    #Break connection in character and remove their raid point
                    character[signup_type].remove(raid['raid_id'])
                    character['canceled'].append(raid['raid_id'])
                    character['raid_points'][raid['raid_name']]['points'] = character['raid_points'][raid['raid_name']]['points'] - 1
                    mongo.replace_character(character)
                    #Break the connection in the raid
                    raid,character_role = remove_character_from_raid(character,raid)
                    
                    #Checks to see if anyone is in the reserves for the role that just cancled and then moves the first in queue to join the raid
                    #Then deletes the character from the reserves
                    if len(raid['raid_raiders'][character_role]['reserves']) != 0:
                        raid['raid_raiders'][character_role]['registered'].append(raid['raid_raiders'][character_role]['reserves'][0])
                        
                        #Handles pulling the characters off the reserves
                        reserve_character = mongo.find_character_by_character_id(raid['raid_raiders'][character_role]['reserves'][0]['character_id'])
                        reserve_character['reserves'].remove(raid['raid_id'])
                        reserve_character['registered'].append(raid['raid_id'])
                        
                        await send_pulled_from_reserves_dm(raid,reserve_character,bot)
                        
                        mongo.replace_character(reserve_character)
                        
                        del raid['raid_raiders'][character_role]['reserves'][0]
                    
                    
                    mongo.replace_raid(raid['raid_id'],raid)
                    
                    await update_raid_signup_message(raid,raid_msg)
                    await update_raid_signup_message_mirrors(raid, bot)

async def process_bot_closet_reactions(payload,mongo,bot) -> None:
    channel = bot.get_channel(payload.channel_id)
        
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
            channel = bot.get_channel(933527657373663252)
            embed = raid_embed(raid, False)
            raid_public_post = await channel.send(embed=embed.embed)
            mongo.set_raid_posting_msg(raid['raid_id'],raid_public_post)
            mongo.set_raid_posting_channel(raid['raid_id'],raid_public_post)
            
            mirrors = [{
                "discord_name":"Sunwell Society",
                "channel_id":"955234475661480006",
                "message_id":""
            }]
            await mongo.add_mirror_raid_post(raid,mirrors,bot)
            
            await add_raid_emojis(raid_public_post)
                        
                        
        #outland-raids
        elif raid['raid_game'] == 'tbc':
            channel = bot.get_channel(933472914840387644)
            embed = raid_embed(raid, False)
            mention_raiders_msg = await channel.send(f"Hey, <@&933478722907029584>! A New {raid['raid_name']} Has Been Posted!")
            raid_public_post = await channel.send(embed=embed.embed)
            mongo.set_raid_posting_msg(raid['raid_id'],raid_public_post)
            mongo.set_raid_posting_channel(raid['raid_id'],raid_public_post)
            
            mirrors = [{
                "discord_name":"Sunwell Society",
                "channel_id":"955234475661480006",
                "message_id":""
            }]
            await mongo.add_mirror_raid_post(raid,mirrors,bot)
            
            await add_raid_emojis(raid_public_post)


async def find_registered_raiders_in_raid(raid):
    roles = ['healer','damage','tank']
    raiders = []
    
    for role in roles:
        for raider in raid['raid_raiders'][role]['registered']:
            raiders.append({
                "raider":raider,"role":role
                })
    
    return raiders

async def find_highest_attended_raid(character) -> int:
    print(character)
    raid_tier = open_raid_tier_data()
    highest_tier = 0
    if len(character['attended']) != 0:
        for raid in character['attended']:
            if int(raid_tier['tbc']['name'][raid.split("#")[0]]) > highest_tier:
                highest_tier = int(raid_tier['tbc']['name'][raid.split("#")[0]])
        return raid_tier['tbc']['level'][str(highest_tier)]
    return raid_tier['tbc']['level'][str(1)]



async def mark_raid_attendance(bot,mongo,inc_message_split):
    raid_id = inc_message_split[2]
    raid = mongo.find_raid_by_raid_id(raid_id)
    
    #Creates a useable list of raiders because of some weird handling earlier
    absent_raiders = inc_message_split[3].replace("[","").replace("]","").split(",")
    
    registered_raiders = await find_registered_raiders_in_raid(raid)
    registered_characters = mongo.get_all_registered_characters(registered_raiders)
    
    for character in registered_characters:
        if character['character']['character_name'] in absent_raiders:
            highest_raid = await find_highest_attended_raid(character['character'])
            #character loses raidpoints
            character['character']['noshows'].append(raid_id)
            #Remove Point from highest Raid Tier
            character['character']['raid_points'][highest_raid]['points'] = character['character']['raid_points'][highest_raid]['points'] - 1
            #Remove Point for raid tier they signed up for
            character['character']['raid_points'][raid['raid_name']]['points'] = character['character']['raid_points'][raid['raid_name']]['points'] - 1
            
            character['character']['registered'].remove(raid['raid_id'])
            
            #remove the character from registered_characters
            for index, reg_char in enumerate(registered_characters):
                if character['character']['character_id'] == reg_char['character']['character_id']:
                    del registered_characters[index]
            
            #this deletes the character from the raid, dirty work
            for index, char in enumerate(raid['raid_raiders'][character['role']]['registered']):
                if char['character_id'] == character['character']['character_id']:
                    del raid['raid_raiders'][character['role']]['registered'][index]
            
            mongo.replace_character(character['character'])
        else:
            character['character']['attended'].append(raid_id)
            mongo.replace_character(character['character'])
            
    raid['raid_bosses_killed'] = int(inc_message_split[4])
    
    bNextDay = bool(inc_message_split[5])
    
    if bNextDay and raid['raid_bosses_killed'] != raid['raid_boss_count']:
        next_day = {
            "day":(len(raid['raid_days'])+1),
            "bosses_killed":raid['raid_bosses_killed'],
            "datetime":raid['raid_days'][len(raid['raid_days'])-1]['datetime']+datetime.timedelta(days=1)
        }
        raid['raid_days'].append(next_day)
        
        for character in registered_characters:
            await send_raid_continue_confirmation(raid,character['character'],bot,mongo)
    else:
        raid['raid_status'] = 'Complete'
    
    mongo.replace_raid(raid['raid_id'],raid)
    
    await update_raid_signup_message(raid,await get_raid_signup_msg(raid['raid_posting_channel'],raid['raid_posting_msg'],bot))
    
    

async def send_raid_info_dm(bot,mongo,inc_message_split,message):
    raid = mongo.find_raid_by_raid_id(inc_message_split[2])
    characters = mongo.get_characters_registered_for_raid_by_raid_id(inc_message_split[2])
    embed = raid_ptsummary_embed(raid,characters,message)
    dm = await message.author.create_dm()
    sent_message = await dm.send(embed=embed.embed)
    
    
async def process_schedule_raid(message,mongo,inc_message_split):
    newRaid = newraid(inc_message_split, message)
                            
    embed = raid_embed(newRaid)
                            
    sent_message = await message.channel.send(embed=embed.embed)
                            
    await sent_message.add_reaction('<:Done:955361992883961896>')
    await sent_message.add_reaction('<:Cancel:955362577267949598>')
                            
    newRaid.set_confirm_message_id(sent_message.id)
                            
    mongo.insert_new_raid(newRaid.to_dict())
    
async def edit_raid(bot, mongo, inc_message_split,message):
    #Comeback later
    
    #First we find the raid being edited in the db
    raid_id = inc_message_split[2]
    raid = mongo.find_raid_by_raid_id(raid_id)
    
    #Make our modifications
    raid['raid_datetime'] = parse(f'{inc_message_split[3]} {inc_message_split[4]}')
    raid['raid_note'] = inc_message_split[5]
    
    #Update the raid in the db with our updated values
    mongo.replace_raid(raid_id,raid)
    
    #Fetch the message for the raid
    channel = bot.get_channel(raid['raid_posting_channel'])
    signup_message = channel.fetch_message(raid['raid_posting_msg'])
    
    
    #Edit messages dependant on this raid
    # await update_raid_signup_message()
    # await update_raid_signup_message_mirrors()
    
    
    
    