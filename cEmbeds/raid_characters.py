import discord

from Utility.helper import open_discord_emotes, open_raid_data

class raid_characters():
    """
    Function:
    Create characters
    
    Displayed:
    When a raider signs up for the first time with a specific class-spec combo.
    """
    def __init__(self, raid, character, payload):
        
        self.embed = discord.Embed(
            title = "[Mechanical Whirring]",
            description=f"`Greetings {payload.member.nick}! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.` \n\nIn The Sun-Hoof Coalition, you have attempted to sign up for '{raid['raid_id']}', but I do not recognize this {character.class_specialization}. \n\nIf you respecialized, or this this a new character, **just type their name** so I can log their points correctly (include special ascii characters).",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )