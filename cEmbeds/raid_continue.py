import discord

class raid_continue():
    
    def __init__(self):
        
        
        self.embed = discord.Embed(
            title = "[Alert Beep]",
            description=f"Thank you for participating today! We did not manage to defeat the forces of evil today so a follow up has been scheduled for tomorrow! \n\n**Your spot in the raid will be held for 12 hours.** \nPlease click one of the below reactions to confirm your spot or leave the raid.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )