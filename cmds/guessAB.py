import random
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import os
import json

dict={} # put user(temp)
num = {}

class GuessAB(Cog_Extension):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.start = False
        #self.time = 0
        self.win = False
        #print(self.start)
        #print(self.time)

    @commands.command()
    async def ABstart(self,ctx):
        '''beta version'''
        dict[str(ctx.author)] = 10
        #self.time = 10
        self.start = True
        self.win = False
        self.L = [i for i in range(10)]
        num[str(ctx.author)] = random.sample(self.L, 4)
        #print(self.start)
        #print(self.time)
        #print(self.L)
        print(str(ctx.author),num[str(ctx.author)])
        await ctx.send(F'{ctx.author} GUESS AB START')
        #3 8
        #
        def check(msg: discord.Message):
            n = str(msg.content)
            return msg.author == ctx.author and msg.channel == ctx.channel and (len(n)==4 and n[0]!=n[1]!=n[2]!=n[3]) or n == 'q'
        while dict[str(ctx.author)] > 0:
            #print(F'ur time {self.time}')
            await ctx.send(F'{ctx.author} You have {dict[str(ctx.author)]} chances left')
            msg = await self.bot.wait_for('message', check=check)

            #print(msg.content)
            n = str(msg.content)
            if n == 'q':
                self.start = False
                #self.time = 0
                dict[str(ctx.author)] = 0
                break
            if len(n) != 4:
                print(F"{ctx.author} input length error!")
                await ctx.send(F'{ctx.author} input length error! {len(n)}')
            else:
                A, B = 0, 0
                for i in range(4):
                    for j in range(4):
                        # print(n[i],num[j])
                        if int(n[i]) == int(num[str(ctx.author)][j]) and i == j:
                            A += 1
                        elif int(n[i]) == int(num[str(ctx.author)][j]) and i != j:
                            B += 1
                if A == 4:
                    #print('success')
                    self.start = False
                    self.win = True
                    dict[str(ctx.author)] = 0
                    #self.time = 0
                    await ctx.send(F'{ctx.author},U Guessed~')
                    break
                else:
                    #print(F'{ctx.author},ur input {n} : {A} A {B} B')
                    await ctx.send(F'{ctx.author},ur input {n} : {A} A {B} B')
                dict[str(ctx.author)] -= 1
        if self.win:
            self.win = False
            await ctx.send(F':shit:{ctx.author} win 500 bubble milk tea :) :shit: (But my function is not finished yet)')
        else:
            await ctx.send(F'{ctx.author} the number is {num[str(ctx.author)]}\n:-1: Game Over，get out :-1:')
            self.start = False
            #self.time = 0
            dict[str(ctx.author)] = 0
        #print(self.start)
        #print(dict[str(ctx.author)] )
        print(str(ctx.author),'success')

def setup(bot):
    bot.add_cog(GuessAB(bot))