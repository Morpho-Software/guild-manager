import discord

class raid_characters():
    """
    Function:
    Create characters
    
    Displayed:
    When a raider signs up for the first time with a specific class-spec combo.
    """
    def __init__(self, raid, character, payload):
        
        self.embed = discord.Embed(
            title = "[Mechanical Whirring]",
            description=f"`Greetings {payload.member.nick}!` \n\nIn The Sun-Hoof Coalition, you have attempted to sign up for `{raid['raid_id']}`, but I do not recognize this {character.class_specialization}. \n\nIf you respecialized, or this a new character, **just type their name** so I can log their points correctly (include special ascii characters). \n\n*If this is a mistake, please go update your sign-up.*",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )