import discord

class raid_continue():
    
    def __init__(self,raid):
        
        
        self.embed = discord.Embed(
            title = raid['raid_name'],
            description=f"",
            color=discord.Color.gold()
        )
        
        self.embed.add_field(
            name="",
            value=""
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )