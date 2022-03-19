import discord

from Utility.helper import open_discord_emotes, open_raid_data

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
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        self.embed.add_field(
            name="```fix \nMaintainence Needed \n```",
            value=f"My functioning is stalling. You can help with my repairs in two ways: \n\n{link to buy me a coffee} \n\n{link to boost server}"
        )

        #this needs a timer, sent out biweekly and deleted automatically once reposted