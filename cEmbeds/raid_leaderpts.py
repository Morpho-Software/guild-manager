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
            title = "[Confirmation Ding]",
            description=f"`Greetings {payload.member.nick}!` \n\nYour raid, `{raid id}`, is starting and here are the fighter's points. **Each point is equal to 1 roll on a needed main spec item.**",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
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
