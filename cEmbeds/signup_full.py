import discord

class signup_full():
    """
    Function:
    To let players know the raid they tried to sign-up for is full.
    
    Displayed:
    In a private message.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "`[Loud Beep]`",
            description=f"You have attempted to sign up for {raid.raid_id}, but it is **full**. You will be put on the *stand-in list*.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
