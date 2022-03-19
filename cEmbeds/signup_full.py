import discord

from Utility.helper import open_discord_emotes, open_raid_data

class help():
    """
    Function:
    To let players know the raid they tried to sign-up for is full.
    
    Displayed:
    In a private message.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Loud Beep]",
            description=f"Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.\n\nIn The Sun-Hoof Coalition, you have attempted to sign up for '{raid.raid_id}', but it is **full**. \n\n*If there are 10+ or 25+ more players interested in this raid, another will be automatically created to sign up for.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
