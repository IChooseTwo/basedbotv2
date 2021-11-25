import discord
from discord.ext import commands
import main

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        emojis = ['🪙','❓','😀']

        home = discord.Embed(
            title='Select A Category:',
            description=''
        )
        home.add_field(name='Crypto Commands:', value='🪙')
        home.add_field(name='Random Commands:', value='❓', inline=False)
        home.add_field(name='Admin Commands:', value='😀', inline=False)

        msg = await ctx.send(embed=home)

        for emoji in emojis:
            await msg.add_reaction(emoji)

        @main.client.event
        async def on_reaction_add(reaction, user, msg=msg, emojis=emojis):
            emoji = reaction.emoji
            crypto_embed = discord.Embed(
                title='🪙Crypto Commands🪙',
                description='cryptoprice,cprice,cryptop'
            )
            random_embed = discord.Embed(
                title='❓Random Commands❓',
                description='Ping'
            )
            admin_embed = discord.Embed(
                title='😀Admin Commands😀',
                description='coming soon'
            )

            if user.bot:
                return
            
            if emoji == emojis[0]:
                await msg.edit(embed=crypto_embed)
            elif emoji == emojis[1]:
                await msg.edit(embed=random_embed)
            elif emoji == emojis[2]:
                await msg.edit(embed=admin_embed)


def setup(client):
    client.add_cog(Help(client))