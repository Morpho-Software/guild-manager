import discord

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
            title = "`[Repeated Boops]`",
            description=f"A duplicate {raid.raid_name} has been created if you are still interested! \n\n*Be sure to remove yourself from stand-ins if you sign-up.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )