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
            title = "[Alert Beep]",
            description=f"`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.`",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url=SOULBEAM_IMG
        )

        self.embed.add_field(
            name="\u200b",
            value=f"```fix\nMaintenance Needed!\n``` My functioning is s-stalling. You-you can help with my repairs in two ways: \n\n{link to buy me a coffee} \n\n{link to boost server}"
        )

        #this needs a timer, sent out biweekly and deleted automatically once reposted