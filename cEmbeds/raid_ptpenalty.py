import discord

from Utility.helper import open_discord_emotes, open_raid_data

class raid_ptpenalty():
    """
    Function:
    To notify when a raider loses a raid point.
    
    Displayed:
    Sent in private messages to those who were marked absent.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Alert Siren]",
            description=f" You were marked **absent** for'{raid.raid_id}' on {raid.datetime}. \n\nYou have lost one point from {highest raid tier}. \n\n*Please make sure to notify a raid leader 3 hours before of your cancelation.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )