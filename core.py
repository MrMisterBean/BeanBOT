import discord 
import os
from discord.ext import commands



#creates variable client to avoind having to type this crap 1,000 times
client = commands.Bot(command_prefix = '.')
# function to load an extension (cog)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
# function to unload an extension (cog)
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
# load each .py file in the cogs folder 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

# print when it is ready to go
@client.event
async def on_ready():
    print("Bot is ready!")

# returns bot latency (ping) in milliseconds 
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

client.run('ODExNzU3NjYwNzM5MjA3MjQw.YC22PA.4yR5yZomznCg91zr-IN-JwQ_WRk')