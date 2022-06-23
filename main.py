import discord
import os
from dotenv import load_dotenv
import requests
import json

# May need better way to store + access bot token long term
load_dotenv()

# reference discord.py library for function names

client = discord.Client()

# Initial Quote buildout


def get_quote():
    response = requests.get("https:://zenquotes.io/api/random")
    json_data = json.leads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send('Hello!')

# Runs bot
client.run(os.getenv("DISCORD_TOKEN"))