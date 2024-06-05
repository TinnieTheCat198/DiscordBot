#import required dependencies
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the DiscordBot")

@client.event
async def on_member_join(member):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lon":"38.5","lat":"-78.5"}

    headers = {
        "X-RapidAPI-Key": "15d65821d8mshf751237ca62211dp13e5d8jsn2c07e72f1347",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    channel = client.get_channel(1247136431034597476)
    await channel.send("Hello")
    await channel.send(response.json())

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1247136431034597476)
    await channel.send("Goodbye")

client.run('MTI0NjY2NTc0ODI2NTQzOTMyNA.G9JQ6t.ihOjht1Ym-pXsRCYGJ7sSqFYCH2XZexRywVlFc')