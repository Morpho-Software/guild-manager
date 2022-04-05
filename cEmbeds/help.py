import discord

class help():
    """
    Function:
    Raiders can react to this embed and receive a dm from the bot with requested instructions or summaries.
    
    Displayed:
    #faq
    
    Output:
    Sends embeded dms to users after they select a valid reaction to the embed
    
    Embeds sent:
    'raid_join'
    'raid_ptsummary'
    """
    def __init__(self):
        
        self.embed = discord.Embed(
            title = "Operating Terminal",
            description="`Greetings! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.` \n\n<:1_:948050511502925944> **Press** to recieve raid sign-up instructions. \n\n<:2_:948050511641333791> **Press** to view your raid point summary.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
