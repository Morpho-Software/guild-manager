import discord

from Utility.bot_constants import *

class donations():
    """
    Function:
    To remind people to donate.
    
    Displayed:
    #notice-board
    
    Output:
    
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description=f"```fix\nMaintenance Needed!\n``` \nMy functioning is s-s-stalling. You-you can help with my repairs in two ways: \n\n{link to buy me a coffee} \n\n{link to boost server}",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url=SOULBEAM_IMG
        )

        #this needs a timer, sent out biweekly and deleted automatically once reposted