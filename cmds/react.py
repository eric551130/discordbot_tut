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

def get_json_data(json_path,name,newbubtea):
    # 获取json里面数据

    with open(json_path, 'r',encoding='utf8') as f:
        params = json.load(f)
        params[name] = newbubtea

        dict = params

    f.close()

    return dict

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
        await ctx.send(F'{ctx.author} 根據大數據運算， 你今天可以吃 {dinner[rand]}')

    @commands.command()
    async def 介紹(self,ctx):
        await ctx.send('一開始先 **[珍珠奶茶** 初始100杯\n用 **[賭骰子 數量 bet** 來賭，可以大，小，單，雙\n沒了可以 **[拜託啦給我喝珍奶** ，會給你50杯')

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

    @commands.command()
    async def 珍珠奶茶(self,ctx):
        with open('BBMT.json', 'r', encoding='utf8') as bbmts:
            bbmt_data = json.load(bbmts)
        bbmts.close()

        if bbmt_data.__contains__(str(ctx.author)) == False:
            the_revised_dict = get_json_data(json_path, str(ctx.author), int(100))
            write_json_data(the_revised_dict)

        with open('BBMT.json', 'r', encoding='utf8') as bbmts:
            bbmt_data = json.load(bbmts)
        bbmts.close()

        name = str(ctx.author)
        await ctx.send(F'**{ctx.author}** :u5272: 你的珍奶有 {bbmt_data[name]} 杯')

    @commands.command()
    async def 拜託啦給我喝珍奶(self,ctx):
        with open('BBMT.json', 'r', encoding='utf8') as bbmts:
            bbmt_data = json.load(bbmts)
        bbmts.close()

        if(bbmt_data[str(ctx.author)] == 0):
            the_revised_dict = get_json_data(json_path, str(ctx.author), int(50))
            write_json_data(the_revised_dict)
            await ctx.send(F'好啦，再給你 50 杯')
        else:
            await ctx.send(F'滾')

    @commands.command()
    async def 賭骰子(self,ctx,number,bet):
        with open('BBMT.json', 'r', encoding='utf8') as bbmts:
            bbmt_data = json.load(bbmts)
        bbmts.close()

        if bbmt_data.__contains__(str(ctx.author)) == False:
            await ctx.send(F'**{ctx.author}** 你還沒買珍奶，滾')
        else:
            number = int(number)
            if int(number) > int(bbmt_data[str(ctx.author)]):
                await ctx.send(F'**{ctx.author}** 你珍奶沒了，滾')
            elif int(number) < 0:
                new_bubtea = -999999
                the_revised_dict = get_json_data(json_path, str(ctx.author), int(new_bubtea))
                write_json_data(the_revised_dict)
                await ctx.send(F'**{ctx.author}** 還敢輸負的R，你的珍奶變為 {new_bubtea}')
            else:
                if number == 0:
                    number = int(bbmt_data[str(ctx.author)])
                rand = random.randint(1, 6)
                bubtea = int(bbmt_data[str(ctx.author)])-number
                pic = discord.File(jdata['dice'][rand-1])
                await ctx.send(file = pic)

                if(dice_big_data.full() == True):
                    dice_big_data.get()
                    dice_big_data.put(rand)
                else:
                    dice_big_data.put(rand)

                if bet == str(rand):
                    new_bubtea = int(bubtea + (number * 6))
                    await ctx.send(F'恭喜!! **{ctx.author}** ，你的珍奶變為 {new_bubtea}')
                elif bet == '單' and rand%2 == 1:
                    new_bubtea = int(bubtea + (number * 2))
                    await ctx.send(F'恭喜!! **{ctx.author}** ，你的珍奶變為 {new_bubtea}')
                elif bet == '雙' and rand%2 == 0:
                    new_bubtea = int(bubtea + (number * 2))
                    await ctx.send(F'恭喜!! **{ctx.author}** ，你的珍奶變為 {new_bubtea}')
                elif bet == '小' and rand <= 3:
                    new_bubtea = int(bubtea + (number * 2))
                    await ctx.send(F'恭喜!! **{ctx.author}** ，你的珍奶變為 {new_bubtea}')
                elif bet == '大' and rand >= 4:
                    new_bubtea = int(bubtea + (number * 2))
                    await ctx.send(F'恭喜!! **{ctx.author}** ，你的珍奶變為 {new_bubtea}')
                else:
                    new_bubtea = int(bubtea)
                    await ctx.send(F'輸家 **{ctx.author}** ，滾 ，你的珍奶變為 {new_bubtea}')
                AStr = ""
                for q in dice_big_data.queue:
                    AStr += str(q) + "  "

                await ctx.send(AStr)

                the_revised_dict = get_json_data(json_path, str(ctx.author), int(new_bubtea))
                write_json_data(the_revised_dict)

    @commands.command()
    async def 排行榜(self,ctx):
        with open('BBMT.json', 'r', encoding='utf8') as bbmts:
            bbmt_data = json.load(bbmts)
            dict2 = bbmt_data
        bbmts.close()

        dict2 = sorted(dict2.items(), key=lambda x:x[1], reverse = True)
        lst_key = []
        lst_value = []
        for key, value in dict2:
            lst_key.append(key)
            lst_value.append(value)
        #print(lst_key)
        str = ""
        await ctx.send(F'排行榜')
        for i in range (len(lst_key)):
            #await ctx.send(F'第{i+1}名 : **{lst_key[i]}**， 有 **{lst_value[i]}** 杯')
            str += (F'第{i+1}名 : **{lst_key[i]}**， 有 **{lst_value[i]}** 杯\n')
        #print(str)
        await ctx.send(str)




def setup(bot):
    bot.add_cog(React(bot))