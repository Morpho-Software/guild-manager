import discord

from Utility.helper import open_discord_emotes, open_raid_data

class gearvault_reminder():
    """
    Function:
    To remind people to donate consumables to the guild vault.
    
    Displayed:
    #raid-notices.
    
    Output:
    
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "[Squeaking Gears]",
            description=f"```fix\nReminder!\n``` Raids need consumables and gold for repairs. Please donate what you can to `guild vaults`. \n\n*For The Horde!*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        #this needs a timer, sent out weekly and deleted automatically once reposted