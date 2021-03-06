import discord

class operating_terminal_leader():
    """
    Function:
    This is a direction manual to display leader commands regarding raid creation,editing
    
    Displayed:
    Displayed Always in Bot Operating Channel 'MESSAGENUMBER' Pinned, It's a static message.
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description="```fix \nLeadership Operating Terminal\n``` \n`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by Lord Gildu Soulbeam.` \n\nPlease only type these commands in #bot-operating. These commands can only be done by Leaders.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
        
        self.embed.add_field(
            name="**Scheduling a Raid**",
            value=f"`sh/ schedule Raid \"Name\" Date(00/00/0000) Time(0:00PM/AM) \"Notes\"` \nExample: sh/ schedule \"Karazhan\" 01/01/2022 5:00PM \"We will meet beforehand.\""
        )
        
        # self.embed.add_field(
        #     name="**Editing a Raid**",
        #     value=f"`sh/ edit RaidID Date(00/00/0000) Time(0:00PM/AM) \"Notes\"` \nExample: sh/ edit Karazhan#1 01/01/2022 5:00PM \"We will not meet beforehand.\""
        # )
        
        self.embed.add_field(
            name="**Marking Absences**",
            value=f"`sh/ absent RaidID [name1,name2,name3]` \nExample: sh/ absent Karazhan#1 [Gildu,Laelo,Bramin] \n*You must mark absences after each raid for players to recieve points.*"
        )

        # self.embed.add_field(
        #     name="**Raid Info**",
        #     value=f"`sh/ info RaidID` \nExample: sh/ info Karazhan#1"
        # )