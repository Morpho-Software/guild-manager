import discord

from Utility.helper import open_discord_emotes, open_raid_data

class help():
    """
    Function:
    To show players their raid point summaries for each character.
    
    Displayed:
    In private messages from the help.py reactions.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "[Soft Beeping]",
            description=f"Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
        
        self.embed.add_field(
            name=f"```fix \nRaid Point Summary for {userid} \n```",
            value=f"*If you want to set you character names please type their names in the order listed.*"
        )
        
        #Logged Character names will be that until changed. This repeats for each character. \n{raid.raid_name} {points} repeats for each raid under value.
        
        self.embed.add_field(
            name=f"**Character 1**",
            value=f"`{class id}, {specs}` \n{raid.raid_name} {points}"
        )