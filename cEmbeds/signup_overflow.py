import discord

from Utility.helper import open_discord_emotes, open_raid_data

class signup_overflow():
    """
    Function:
    To let players know a duplicate raid has been created for the 10+ or 25+ who tried to sign up for that raid when it was full.
    
    Displayed:
    In a private message.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Repeated Boops]",
            description=f"Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.\n\nIn The Sun-Hoof Coalition, a '{raid.raid_name}' has been created if you are still interested.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )