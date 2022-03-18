import discord

from Utility.helper import open_discord_emotes, open_raid_data

class help():
    
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "Operating Terminal",
            description="<:1_:948050511502925944> Recieve raid sign-up instructions.\n<:2_:948050511641333791> View your raid point summary.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
