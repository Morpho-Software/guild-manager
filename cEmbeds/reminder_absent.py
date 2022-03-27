import discord

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
            description=f"`Greetings {payload.member.nick}!`",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        self.embed.add_field(
            name="\u200b",
            value=f"```fix\nReminder!\n```You were the creator of '{raid.raid_id}'. **Please mark absences or no one will get their points!** \n\n*If there were no absences, you still must log that and leave the name list blank.*"
        )

        #this needs a timer, sent out weekly and deleted automatically once reposted