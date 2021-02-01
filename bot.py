import discord
from discord.ext import commands, tasks
import json

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)