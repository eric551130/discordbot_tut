import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency * 1000)}(ms)')

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    '''@commands.command()
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def music(self,ctx,*,msg):
        await ctx.send(F'!p {msg}')'''

def setup(bot):
    bot.add_cog(Main(bot))