import discord

class signup_confirmation():
    """
    Function:
    To notify leaders of which players have which points.
    
    Displayed:
    Sent in private messages on day of raid.
    
    Output:
    
    """
    def __init__(self, raid, character,payload):
        
        self.embed = discord.Embed(
            title = "[Confirmation Ding]",
            description=f"`Greetings {payload.member.nick}! This is SQ-Bot 300X, programmed for your optimized battling experience by The Great Lord Gildu Soulbeam, now also an engineer.` \n\n`{raid id}` Is starting and here are the player's points. **Each point is 1 roll on a needed main spec item.**",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster - Bot 300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )

        #repeats for every character
        self.embed.add_field(
            name="\u200b",
            value=f"```fix\nPlayer Points\n```"
        )    

        self.embed.add_field(
            name=f"**{character name}**",
            value=f"{points}"
        )