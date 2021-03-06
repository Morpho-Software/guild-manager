import discord

class raid_reminder():
    """
    Function:
    To notify when a raid is coming up.
    
    Displayed:
    In #raid-notices.
    Sent in private messages to those who signed up for raids.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "`[Mechanical Ticking]`",
            description=f"{raid.raid_id} on {raid.datetime} is today, but there is currently not enough signed up! \n\n*All participants have been notified.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )