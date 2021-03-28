import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(jdata['welcome_ch'])
        await channel.send(F'{member} join!')
        print(F'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(jdata['leave_ch'])
        await channel.send(F'{member} join!')
        print(F'{member} leave!')

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(F'{error}遺失參數')
        elif isinstance(error,commands.CommandNotFound):
            await ctx.send(F'{error}查無指令')
        elif isinstance(error,commands.CommandInvokeError):
            await ctx.send(F'{error}參數錯誤')
        else:
            await ctx.send(F'{error}發生錯誤')


def setup(bot):
    bot.add_cog(Event(bot))