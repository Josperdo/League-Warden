import discord
import os
from dotenv import load_dotenv
import requests
import json
import random

# May need better way to store + access bot token long term
load_dotenv()

# reference discord.py library for function names
client = discord.Client()

# Initial buildout of functions and commands for example to expand upon/ alter later

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]


# Runs bot
client.run(os.getenv("DISCORD_TOKEN"))
