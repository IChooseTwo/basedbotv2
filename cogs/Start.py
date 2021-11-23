import discord
from discord.ext import commands

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client
    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on')

def setup(client):
    client.add_cog(Start(client))