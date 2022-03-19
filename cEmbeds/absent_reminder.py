import discord

from Utility.helper import open_discord_emotes, open_raid_data

class gearvault_reminder():
    """
    Function:
    To remind raid creator to mark absences.
    
    Displayed:
    Private messages.
    
    Output:
    
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "[Loud Beep]",
            description=f"`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.`",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        self.embed.add_field(
            name="```fix \nReminder! \n```",
            value=f"You were the creator of {raid.raid_id}. **Please mark absences or no one will get their points!** \n\n*If there were no absences, you still must log that and leave the name list blank."
        )

        #this needs a timer, sent out weekly and deleted automatically once reposted