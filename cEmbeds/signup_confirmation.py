import discord

class signup_confirmation():
    """
    Function:
    To notify a player of a failed sign-up.
    
    Displayed:
    Sent in private messages when a sign-up is failed.
    
    Output:
    
    """
    def __init__(self, raid, character,user_name):
        
        self.embed = discord.Embed(
            title = "[Confirmation Ding]",
            description=f"`Greetings {user_name}!` \n\nIn The Sun-Hoof Coalition, you have successfully signed up for `{raid['raid_id']}` on {raid['raid_datetime'].month}/{raid['raid_datetime'].day}/{raid['raid_datetime'].year} at {raid['raid_datetime'].strftime('%I:%M%p')} as the {character['class_specialization']}, {character['character_name']}! \n**You have {character['raid_points'][raid['raid_name']]['points']} Raid Points to use, each as an extra needed MS roll in this raid!** \n\n*Please cancel up to 3 hours before to not recieve a point penalty. If you meant to sign up as a different character of the same class and spec, type their name.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )