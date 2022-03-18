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
        
        self.embed.add_field(
            name="**Scheduling a Raid**",
            value=f"`sh/ schedule Raid \"Name\" Date(00/00/0000) Time(0:00PM/AM) \"Notes\"` \n*Example: sh/ schedule \"Karazhan\" 01/01/2022 5:00PM \"We will meet beforehand.\"*"
        )
        
        self.embed.add_field(
            name="**Editing a Raid**",
            value=f"`sh/ edit RaidID Date(00/00/0000) Time(0:00PM/AM) \"Notes\"` \n*Example: sh/ edit Karazhan#1 01/01/2022 5:00PM \"We will not meet beforehand.\"*"
        )