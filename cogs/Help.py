import discord
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Help(self, ctx):
        help = discord.Embed(
        title = 'Help Menu',
        description = 'Use > to use a command'
    )
        help.add_field(name = "🪙 **Crypto** 🪙", value = "`cprices, cryptop, cryptoprices`", inline=False)
        help.add_field(name = "❓ **Random** ❓", value = "`ping`", inline=False)
        await ctx.send(embed=help)

def setup(client):
    client.add_cog(Help(client))
