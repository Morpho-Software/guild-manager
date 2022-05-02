import discord

class signup_confirmation():
    """
    Function:
    To notify leaders of which players have which points.
    
    Displayed:
    Sent in private messages on day of raid.
    
    Output:
    sh/ raid info command

    """
    def __init__(self, raid, character,payload):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description=f"```fix\nPlayer Points\n```",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        #repeats for every character
        self.embed.add_field(
            name="\u200b",
            value=f"Your raid, {raid['raid_id']}, is starting and here are the fighter's points. Reminder: Each point is equal to 1 roll on any **needed main spec item**."
        )    

        self.embed.add_field(
            name=f"**{character name}**",
            value=f"{points}"
        )
