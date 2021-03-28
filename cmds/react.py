import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import queue

dinner = ['炒飯','炒麵','屎','牛肉麵','牛排麵','雞排麵','水餃','咖哩飯','火鍋','鴨肉飯','羊肉燴飯','鍋燒意麵','羊肉米粉',
          '麥當勞','KFC','蚵仔煎','鹹酥雞','鹹水雞','烤肉','滷味','便當']
drink = ['奶茶','紅茶','綠茶','烏龍茶','青茶','豆漿','米漿','珍珠奶茶','咖啡','布丁奶茶','冬瓜茶','梅子綠茶','水','藍水','紅水','超級藥水']

json_path = 'C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\BBMT.json'
json_path1 = 'C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\BBMT.json'

dict2 = {}
dict = {}

dice_big_data = queue.Queue(maxsize=20)

def add_json_data(json_path,name,newbubtea):
    with open(json_path, 'r', encoding='utf8') as f:
        params = json.load(f)
        params[name] = newbubtea

        dict = params

    f.close()
    return dict

def write_json_data(dict):
    with open(json_path1, 'w',encoding='utf8') as r:
        json.dump(dict, r,ensure_ascii=False)

    r.close()

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
jfile.close()

class React(Cog_Extension):
    @commands.command()
    async def 本本抽獎(self,ctx):
        rand = random.randint(10000,30000)
        H_comic = random.choice(jdata['H_comics'])
        await ctx.send(F'抽到 {rand}')

    @commands.command()
    async def haachama(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\haachama.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 製粽(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\th1.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 肉便器(self,ctx):
        pic = discord.File(random.choice(jdata["pct"]))
        await ctx.send(file=pic)

    @commands.command()
    async def TSJ(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\TSJ.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 要吃什麼(self,ctx):
        rand = random.randint(0, len(dinner)-1)
        await ctx.send(F'**{ctx.author}** 根據大數據運算， 你今天可以吃 {dinner[rand]}')

    @commands.command()
    async def 要玩什麼(self,ctx):
        #rand = random.randint(0, len(dinner)-1)
        await ctx.send(F'**{ctx.author}** 玩 {random.choice(jdata["game"])}')

    @commands.command()
    async def 要喝什麼(self,ctx):
        rand = random.randint(0, len(drink)-1)
        #rand = int(7)
        if rand == 7:
            with open('BBMT.json', 'r', encoding='utf8') as bbmts:
                bbmt_data = json.load(bbmts)
            bbmts.close()
            name = str(ctx.author)
            the_revised_dict = add_json_data(json_path, name, int(bbmt_data[name])+10)
            write_json_data(the_revised_dict)

        await ctx.send(F'**{ctx.author}** 去喝  {drink[rand]}')


def setup(bot):
    bot.add_cog(React(bot))