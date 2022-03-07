#This brings in the code needed to operate a discord bot.
import discord

#This is our bot's registration token.
TOKEN = 'OTMzODY1NDk3Njg5MTk4NjAz.YenwBQ.MqRxTpu0P_vUcNQcBg_mKHvvvwM'

#This is showing where in the code the bot's blueprint is.
bot = discord.Client()

#
@bot.event
async def on_ready():
    pass