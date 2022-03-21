import discord

class raid_cancel():
    """
    Function:
    To notify when a raid is canceled.
    
    Displayed:
    Edited message on canceled raid in azeroth-raids and outland-raids.
    Sent in private messages to those who signed up for raids.
    
    Output:
    Deletes the message after 12 hours.
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Mechanical Ticking]",
            description=f"`{raid.raid_id}` on {raid.datetime} has been **canceled**. \n\n*This message will self destruct in 12 hours. All participants have been notified.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
