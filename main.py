import discord
import os
import requests
import random

from discord.ext import commands
from dotenv import load_dotenv
from uptime import upTime

# May need better way to store + access bot token long term
load_dotenv()

# reference discord.py library for function names
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            
# Runs bot + maintains uptime
upTime()
client.run(os.getenv("Token"))