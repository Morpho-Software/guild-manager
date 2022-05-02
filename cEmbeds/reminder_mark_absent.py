import discord

class reminder_mark_absent():
    """
    Function:
    To remind raid creator to mark absences.
    
    Displayed:
    Private messages.
    
    Output:
    
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description=f"```fix\nReminder!\n``` \nYou were the creator of {raid.raid_id}. **Please mark absences or no one will get their points!** \n\n*If there were no absences, you still must log that and leave the name list blank.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        #this needs a timer, sent out weekly and deleted automatically once reposted