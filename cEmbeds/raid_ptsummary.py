import discord

class raid_ptsummary():
    """
    Function:
    To show leaders the players in the raids.
    
    Displayed:
    In private messages from the op_term_lead.py reactions.
    
    Output:
    
    """
    def __init__(self, raid, characters, message):
        
        self.embed = discord.Embed(
                title = raid.raid_name,
                description=f"**Raid ID: {raid.raid_id} | Raid Host: <@{raid.scheduler[0]}> \n**{raid.datetime.month}/{raid.datetime.day}/{raid.datetime.year}** | **{raid.datetime.strftime('%I:%M%p')}**\n Bosses:({raid.bosses_killed}/{raid.raid_boss_count})** \n",
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