from Models.raider import newraider as new_raider
from Models.character import newcharacter as new_character
from cEmbeds.raid_characters import raid_characters as new_character_embed
from Utility.helper import get_message_reactions_by_member_id, check_for_valid_reactions



async def process_new_raider(mongo,payload,reactor_reactions,raid):
    #This code runs if no account have ever been created with the raider
    newraider = new_raider(payload)
    newcharacter = new_character(payload, reactor_reactions)
    mongo.insert_new_raider(newraider.to_dictionary())
    mongo.insert_new_character(newcharacter.to_dictionary())
    mongo.add_character_to_raider(payload.user_id,newcharacter.character_id)
    dm = await payload.member.create_dm()
    embed=new_character_embed(raid,newcharacter,payload)
    message = await dm.send(embed=embed.embed)
    await message.add_reaction('🤖')
    
async def process_raid_signup(payload,mongo,bot):
    channel = bot.get_channel(payload.channel_id)
    raid_msg = await channel.fetch_message(payload.message_id)
    raid = mongo.find_raid_by_posting_message_id(raid_msg.id)
        
    if payload.emoji.name == 'Done':
        reactor_reactions = await get_message_reactions_by_member_id(raid_msg,payload.member.id)
        if len(reactor_reactions) == 3 and check_for_valid_reactions(reactor_reactions):
            #Check if reactor is in the database
            if mongo.find_raider_by_discord_member_id(payload.member.id):
                #raider exist
                print('I exist')
            else:
                await process_new_raider(mongo, payload, reactor_reactions, raid)
                print('Added a raider and a character.')
        else:
            #The user has failed to correctly fill out the reactions on a raid
            dm = await payload.member.create_dm()
            message = await dm.send(f"[Beeping and Whirring]\nGreetings! This is SQ-Bot 300X, programmed for your optimized battling experience by the Great Lord Gildu Soulbeam, now also an engineer.\nIn The Sun-Hoof Coalition, you have attempted to sign up for `{raid['raid_id']}`, but it is **incomplete**.\n\n*Please make sure you select: your **class** icon, your **class number** icon representing your specialization (found in #faq), and the **done** icon.\nIf you wish to cancel your sign-up, please select the cancel icon.*")
            await message.add_reaction('🤖')