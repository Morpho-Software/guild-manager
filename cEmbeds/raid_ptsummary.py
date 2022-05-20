import discord
from Utility.helper import split_list

class raid_ptsummary():
    """
    Function:
    To show leaders the players in the raids.
    
    Displayed:
    In private messages from the op_term_lead.py reactions.
    
    Output:
    
    """
    def __init__(self, raid, characters, message):
        
        #most recent day
        day = raid['raid_days'][len(raid['raid_days'])-1]
        
        self.embed = discord.Embed(
                title = raid['raid_name'],
                description=f"**Raid ID: {raid['raid_id']} | Raid Host: <@{raid['raid_scheduler'][0]}> \n**Day: {day['day']}** | **{day['datetime'].month}/{day['datetime'].day}/{day['datetime'].year}** | **{day['datetime'].strftime('%I:%M%p')}**\n Bosses:({raid['raid_bosses_killed']}/{raid['raid_boss_count']})** \n",
                color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        #This splits the characters into two columns        
        col1, col2 = split_list(characters)
        col1_value = ''
        col2_value = ''
        
        for character in col1:
            col1_value += f"**{character['character_name']}**\n{character['class_specialization']}\n{raid['raid_name']} Points: {character['raid_points'][raid['raid_name']]['points']}\n\n"
        
        for character in col2:
            col2_value += f"**{character['character_name']}**\n{character['class_specialization']}\n{raid['raid_name']} Points: {character['raid_points'][raid['raid_name']]['points']}\n\n"
        
        self.embed.add_field(
            name=f'\u200b',
            value=col2_value
        )
        self.embed.add_field(
            name=f'\u200b',
            value=col1_value
        )

        # self.embed.add_field(
        #     name=f"**{character}**",
        #     value=f"`{class id}, {specs}` \n{raid.raid_name} {points}"
        # )