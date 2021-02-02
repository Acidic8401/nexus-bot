import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
load_dotenv()
token=os.getenv("BOT_TOKEN")
intents=discord.Intents.default()
intents.bans=True
intents.members=True

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, intents=intents)

@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
        
    prefixes[str(guild.id)] = '~'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.guild_only()
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix has been changed to: `{prefix}`')


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.unload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
@client.command()
async def rload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.unload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
        client.load_extension(f'cogs.{extension}')
        print(f'{extension} has been reloaded')

for filename in os.listdir(r'C:\Users\Bailey\Documents\Programs\Nexus\nexus-bot\cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)