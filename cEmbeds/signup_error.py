import discord

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
            title = "`[Beeping and Whirring]`",
            description=f"You have attempted to sign up for {raid.raid_id}, but it is **incomplete**. \nMake sure to select: one *class* icon, one *specialization number* icon (found in #faq), and the *done* icon.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
