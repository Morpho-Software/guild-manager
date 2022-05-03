import discord

class character_summary():
    """
    Function:
    To show players their summaries for each character.
    
    Displayed:
    In private messages from the help.py reactions.
    
    Output:
    
    """
    def __init__(self, raid, characters, message):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description=f"```fix\nYour Character Raid Points\n```",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
        
        self.embed.add_field(
            name="\u200b",
            value=f"\u200b",
            inline=False
        )

         #This repeats for each character. \n{raid.raid_name} {points} repeats for each raid under value.

        for character in characters:
            
            self.embed.add_field(
                name=f'**{character["character_name"]}**',
                value=f"{character['class_specialization']}\n{raid['raid_name']} Points: {character['raid_points'][raid['raid_name']]['points']}"
            )

        # self.embed.add_field(
        #     name=f"**{character}**",
        #     value=f"`{class id}, {specs}` \n{raid.raid_name} {points}"
        # )