import discord 
import os
from discord.ext import commands


#creates variable client to avoid having to type this crap 1,000 times
client = commands.Bot(command_prefix = '.')

def owner_check(ctx):
    return ctx.author.id == 280529649547608066
# function to load an extension (cog)
@client.command()
@commands.check(owner_check)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
# function to unload an extension (cog)
@client.command()
@commands.check(owner_check)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
# load each .py file in the cogs folder 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

# print when it is ready to go
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('LETS GOOO') )
    print("Bot is ready!")




client.run('ODExNzU3NjYwNzM5MjA3MjQw.YC22PA.4yR5yZomznCg91zr-IN-JwQ_WRk')