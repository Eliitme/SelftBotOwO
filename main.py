import discord
from discord.ext import commands
from colorama import Fore
import asyncio
from webserver import keep_alive
import json
import re


import random

from decouple import config

dict = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
        '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}

prefix = "q"

keep_alive()
token = config("TOKEN")
channelId = config("CHANNEL_ID")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)


@bot.command(pass_context=True)
async def abc(ctx):
    await ctx.message.delete()
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send('vh')
            print(f"{Fore.GREEN}succefully owoh")
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send('vb')
            print(f"{Fore.GREEN}succefully owob")

        recentMsg = await ctx.bot.get_channel(
            ctx.message.channel.id).history(limit=5).flatten()
        for msg in recentMsg:
            if msg.author.id == 408785106942164992 and 'spent' in msg.content:
                await gem(ctx)
            if msg.author.id == 408785106942164992 and 'capcha' in msg.content.lower():
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send('qstop')
                    print(f"{Fore.RED}stop capcha")

        await asyncio.sleep(random.choice([17, 20]))


async def gem(ctx):
    inv = 0
    quantity = 0
    async with ctx.typing():
        await asyncio.sleep(random.choice([1, 2, 3]))
        await ctx.send('vinv')
    checkInv = await ctx.bot.get_channel(ctx.message.channel.id).history(limit=10).flatten()
    arrQuantity = []

    invWithQuantity = {}

    for msg in checkInv:
        if 'inventory' in msg.content.lower():
            inv = re.findall(r'`(.*?)`', msg.content)
            quantity = re.findall(r'>(.*?)\s', msg.content)

    for item in quantity:
        arrQuantity.append(item.strip().translate(str.maketrans(dict)))

    for x in range(len(arrQuantity)):
        invWithQuantity[str(inv[x])] = int(arrQuantity[x])

    gem1 = ''
    gem2 = ''
    gem3 = ''

    def getValue(key):
        value = invWithQuantity.get(key)
        if value:
            return value
        else:
            return 0

    for i in range(6):
        if getValue(str(int(i) + 51)) > 0 and getValue(str(int(i) + 65)) > 0 and getValue(str(int(i) + 72)) > 0:
            gem1 = str(int(i) + 51)
            gem2 = str(int(i) + 65)
            gem3 = str(int(i) + 72)

    for gem in [gem1, gem2, gem3]:
        async with ctx.typing():
            await asyncio.sleep(random.choice([7, 8, 9]))
            await ctx.send('vuse ' + gem)
            print(f"{Fore.YELLOW}use gem " + gem)
            await asyncio.sleep(1)


@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    global dmcs
    dmcs = False


@bot.event
async def on_ready():
    activity = discord.Game(name="", type=4)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f''.join("READY"))

bot.run(token, bot=False)
