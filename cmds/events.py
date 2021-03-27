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

def setup(bot):
    bot.add_cog(Event(bot))