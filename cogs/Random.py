import discord
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

class Random(commands.Cog):
    def __init__(self, client):
        self.client = client
    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Random(client))
