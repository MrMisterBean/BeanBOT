import discord 
from discord.ext import commands


class Main(commands.Cog):

    def __init__(self, client):
        self.client = client

    # sends message with github link
    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def git(self, ctx):
        await ctx.send('https://github.com/MrMisterBean/BeanBOT')

    # returns bot latency (ping) in milliseconds 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Main(client))