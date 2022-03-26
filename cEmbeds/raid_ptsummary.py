import discord

class raid_ptsummary():
    """
    Function:
    To show players their raid point summaries for each character.
    
    Displayed:
    In private messages from the help.py reactions.
    
    Output:
    
    """
    def __init__(self, raid, characters, message):
        
        self.embed = discord.Embed(
            title = "[Soft Beeping]",
            description=f"`Greetings {message.author}! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.`",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
        
        self.embed.add_field(
            name="\u200b",
            value=f"```fix\nCharacter Raid Points\n```"
        )

         #This repeats for each character. \n{raid.raid_name} {points} repeats for each raid under value.

        self.embed.add_field(
            name=f"**{character}**",
            value=f"`{class id}, {specs}` \n{raid.raid_name} {points}"
        )