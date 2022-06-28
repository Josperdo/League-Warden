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
            
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

messages = [
    "Bro, seriously... Stop playing league. You literally don't even ENJOY the game.",
    "Why are you playing League when there's more productive uses of your time?",
]

@client.event
async def on_ready():
    print("Ready!")
    print(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} Heathens"))
    members = 0
    
    for guild in client.guilds:
        for member in guild.members:
            members += 1

    with open("members.txt", "w") as f:
        f.write(str(members))


@client.event
async def on_member_update(before, after):
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(status)))


    if after.activity != None:
        print(after.name)
        if len(after.activities) > 1:
            print(after.activities[1].name)
            if str(after.activities[1].name).lower() == "league of legends":
                print("banning")
                try:
                    with open("hall-of-shame.txt", "a+") as f:
                        f.write(after.name)

                    await after.send(random.choice(messages))
                    await after.ban(reason='Playing League of legends')
                except discord.errors.Forbidden:
                    print("Not valid permissions")
                    after.send("")

                print(after.activities[1])
            
# Runs bot + maintains uptime
upTime()
client.run(os.getenv("Token"))