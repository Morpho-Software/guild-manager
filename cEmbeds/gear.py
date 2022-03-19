import discord

from Utility.helper import open_discord_emotes, open_raid_data

class gear():
    """
    Function:
    Raiders will recieve this when successfully signing up for a raid. It includes gear suggestions.
    
    Displayed:
    Private Message.
    
    Output:
    
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "[Long Beeps]",
            description=f"`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.` \n\nIn The Sun-Hoof Coalition, you have successfully signed-up for '{raid.raid_id}' with {character name} as a {class and spec}! \n\n***If you have an item, or better please respond with it's name.** Gear suggestions are found on {bis site link}.*",
            color=discord.Color.gold()
        )
        
        self.embed.add_field(
            name="```fix \nGear Suggestions \n```",
            value=f"{item name}"
        )

        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        # Include all gear slot suggestions this same way.
        # Item names come from BIS site. 
        # Items with no suggestion says, "*none*". 
        # Gear will not be suggested if they have items from a higher tier logged from this message corresponding to a higher raid tier sign up.

        self.embed.add_field(
            name="`Head Suggestion`",
            value=f"{item name}"
        )