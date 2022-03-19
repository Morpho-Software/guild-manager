import discord

from Utility.helper import open_discord_emotes, open_raid_data

class signup_error():
    """
    Function:
    To notify a player of a failed sign-up.
    
    Displayed:
    Sent in private messages when a sign-up is failed.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Beeping and Whirring]",
            description=f"`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.` \n\nIn The Sun-Hoof Coalition, you have attempted to sign up for '{raid.raid_id}', but it is **incomplete**. \n*Make sure to select: **class** icon, **specialization number** icon (found in #faq), and **done** icon.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
