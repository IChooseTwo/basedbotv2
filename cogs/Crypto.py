import discord
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import requests, os
from bs4 import BeautifulSoup

class Crypto(commands.Cog):
    def __init__(self, client):
        self.client = client
    #Commands
    @commands.command(aliases = ['cprices', 'cryptop'])
    async def cryptoprice(self, ctx, coin=None):
        coin = coin.lower()
        price = cg.get_price(ids=f'{coin}', vs_currencies='usd')
        coin_price = price[f'{coin}']['usd']
        lite = discord.Embed(
            title = 'Crypto Worth',
            description = f'{coin} currently worth in, USD ${coin_price}'
        )
        await ctx.send(embed=lite)

def setup(client):
    client.add_cog(Crypto(client))
