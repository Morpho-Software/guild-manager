import discord

from Utility.helper import open_discord_emotes, open_raid_data

class raid():
    """
    Function:
    
    Displayed:
    
    Output:
    
    """
    
    def __init__(self, raid, bConfirmationVersion=True):
        
        rd = open_raid_data()
        emotes = open_discord_emotes()
        
        if bConfirmationVersion:
        
            self.raid = raid
            
            self.embed = discord.Embed(
                title = raid.raid_name,
                description=f"Raid ID: {raid.raid_id} \n**{raid.datetime}** | **{raid.datetime}** \n\n*{raid.note}*",
                color=discord.Color.gold()
            )
            
            self.embed.set_author(
                name="Soulbeam's Quartermaster - Bot 300X",
                icon_url="https://cdn.discordapp.com/attachments/845526554963476491/954476489879986246/SQ-Bot_300X-removebg-preview.png"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nTanks ({len(raid.raiders['tank']['registered'])}/{raid.raiders['tank']['amount'][0]})\n``` `Stand-ins ({len(raid.raiders['tank']['reserves'])})`\n{self.build_slots('tank')}"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nDamage ({len(raid.raiders['damage']['registered'])}/{raid.raiders['damage']['amount'][0]})\n``` `Stand-ins ({len(raid.raiders['damage']['reserves'])})`\n{self.build_slots('damage')}"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nHealers ({len(raid.raiders['healer']['registered'])}/{raid.raiders['healer']['amount'][0]})\n``` `Stand-ins ({len(raid.raiders['healer']['reserves'])})`\n{self.build_slots('healer')}"
            )
            
            self.embed.set_image(
                url=rd[raid.raid_name]['image']
            )
            
            self.embed.add_field(
                name="\u200b",
                value=f"```fix\nRaid Confirmation\n``` This is a preview of the raid. Please respond with <:Done:948280499049201744> to confirm the raid or <:Cancel:948777741094895687> to delete the raid."
            )
            
        else:
            self.raid = raid
            
            self.embed = discord.Embed(
                title = raid['raid_name'],
                description=f"Raid ID: {raid['raid_id']} \n**{raid['raid_time']}** | **{raid['raid_time']}** \n\n*{raid['raid_note']}*",
                color=discord.Color.gold()
            )
            
            self.embed.set_author(
                name="Soulbeam's Quartermaster - Bot 300X",
                icon_url="https://cdn.discordapp.com/attachments/933481167565488128/947801465903267890/WoWScrnShot_090521_044754_-_Copy.jpg"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nTanks ({len(raid['raid_raiders']['tank']['registered'])}/{raid['raid_raiders']['tank']['amount'][0]})\n``` `Stand-ins ({len(raid['raid_raiders']['tank']['reserves'])})`\n{self.build_slots('tank',False)}"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nDamage ({len(raid['raid_raiders']['damage']['registered'])}/{raid['raid_raiders']['damage']['amount'][0]})\n``` `Stand-ins ({len(raid['raid_raiders']['damage']['reserves'])})`\n{self.build_slots('damage',False)}"
            )
            
            self.embed.add_field(
                name=f"\u200b",
                value=f"```fix\nHealers ({len(raid['raid_raiders']['healer']['registered'])}/{raid['raid_raiders']['healer']['amount'][0]})\n``` `Stand-ins ({len(raid['raid_raiders']['healer']['reserves'])})`\n{self.build_slots('healer',False)}"
            )
            
            self.embed.set_image(
                url=rd[raid['raid_name']]['image']
            )
            
            
        
        # embed.set_thumbnail(
        #   url="https://bnetcmsus-a.akamaihd.net/cms/content_folder_media/18I0YAIMVR0J1407540721349.jpg"
        # )
        
    def build_slots(self,role, bConfirmationVersion=True):
        if bConfirmationVersion:
            if len(self.raid.raiders[role]['registered']) == 0:
                return"1."
            else:
                slots = ""
                for count, raider in enumerate(self.raid.raiders[role]['registered']):
                    slots += f'{count}. {raider}\n'
        else:
            if len(self.raid['raid_raiders'][role]['registered']) == 0:
                return"1."
            else:
                slots= ""
                for count, raider in enumerate(self.raid['raid_raiders'][role]['registered']):
                    slots += f'{count+1}. {raider["discord_member_display_name"]}\n'
                return slots
                
    def get_embed(self):
        return self.embed