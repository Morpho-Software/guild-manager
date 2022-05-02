import discord

class raid_join():
    """
    Function:
    Directions to sign-up for a raid with all the class icons and specialization icons.
    
    Displayed:
    In #faq channel. Sent in private messages from the help.py reactions.
    
    Output:
    
    """
    def __init__(self, raid):
        
        self.embed = discord.Embed(
            title = "\u200b",
            description=f"```fix\nHow To Join a Raid\n``` \nReact to each raid with your class icon and specialization number icon, for that raid. \nMark <:Done:948280499049201744> when done. Mark <:Cancel:948777741094895687> to cancel your sign up. \n\nIf you sign up to a full raid, you will become a stand in. If someone cancels, you will fill their role automatically and be notified. If there are enough stand-ins, a duplicate raid will be created.",
            color=discord.Color.gold()
        )
        
        self.embed.set_author(
            name="Soulbeam's Quartermaster Robot V.300X",
            icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
        )
        
        self.embed.add_field(
            name="<:Priest:948050245537890314> **Priest**",
            value=f"<:1_:948050511502925944> Shadow \n<:2_:948050511641333791> Holy"
        )
        
        self.embed.add_field(
            name="<:Druid:948050245659557978> **Druid**",
            value=f"<:1_:948050511502925944> Feral bear \n<:2_:948050511641333791> Restoration \n<:3_:948050511628734525> Balance \n<:4_:948050511578411128> Feral Cat"
        )
        
        self.embed.add_field(
            name="<:Hunter:948050245340774442> **Hunter**",
            value=f"<:1_:948050511502925944> Beast Master \n<:2_:948050511641333791> Survivalist \n<:3_:948050511628734525> Marksmanship"
        )
        
        self.embed.add_field(
            name="<:Shaman:948050245554688010> **Shaman**",
            value=f"<:1_:948050511502925944> Enhancement \n<:2_:948050511641333791> Restoration \n<:3_:948050511628734525> Elemental"
        )
        
        self.embed.add_field(
            name="<:Mage:948050245391118337> **Mage**",
            value=f"<:1_:948050511502925944> Fire \n<:2_:948050511641333791> Arcane \n<:3_:948050511628734525> Frost"
        )
        
        self.embed.add_field(
            name="<:Warrior:948050245491752961> **Warrior**",
            value=f"<:1_:948050511502925944> Protection \n<:2_:948050511641333791> Fury \n<:3_:948050511628734525> Arms"
        )
        
        self.embed.add_field(
            name="<:Rogue:948050245193986059> **Rogue**",
            value=f"<:1_:948050511502925944> Combat \n<:2_:948050511641333791> Subtlety \n<:3_:948050511628734525> Assassination"
        )
        
        self.embed.add_field(
            name="<:Paladin:948050245500141578> **Paladin**",
            value=f"<:1_:948050511502925944> Protection \n<:2_:948050511641333791> Holy \n<:3_:948050511628734525> Retribution \n<:4_:948050511578411128> Holy DPS"
        )
        
        self.embed.add_field(
            name="<:Warlock:948050245672108093> **Warlock**",
            value=f"<:1_:948050511502925944> Demonology \n<:2_:948050511641333791> Affliction \n<:3_:948050511628734525> Destruction \n<:4_:948050511578411128> Destruction Fire"
        )
