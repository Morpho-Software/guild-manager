import discord

class operating_terminal():
    """
    Function:
    Raiders can react to this embed and receive a dm from the bot with requested instructions or summaries.
    
    Displayed:
    #faq
    
    Output:
    Sends embeded dms to users after they select a valid reaction to the embed; needs the 1 and 2 emojis automatically on it
    
    Embeds sent:
    'raid_join'
    'raid_ptsummary'
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description="```fix \nOperating Terminal\n``` \n`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by Lord Gildu Soulbeam.` \n\n<:1_:967637986105761792> **Press** to recieve raid sign-up instructions. \n\n<:2_:955975423605473340> **Press** to view your raid point summaries.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
