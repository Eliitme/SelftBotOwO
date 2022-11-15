import discord
from discord.ext import commands
from colorama import Fore
import asyncio
from webserver import keep_alive
import time
import re


import random

from decouple import config

dict = {
    '⁰': '0',
    '¹': '1',
    '²': '2',
    '³': '3',
    '⁴': '4',
    '⁵': '5',
    '⁶': '6',
    '⁷': '7',
    '⁸': '8',
    '⁹': '9'
}

prefix = "q"

keep_alive()
token = config("TOKEN")
prefix_owo = 'owo'

# ---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)


def at():
    return f'{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}'


@bot.command(pass_context=True)
async def s(ctx):
    clientId = ctx.message.channel.id
    await ctx.message.delete()
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send(f"{prefix_owo}h")
            print(f"{at()}: {Fore.GREEN}succefully owoh")
        # async with ctx.typing():
        #     await asyncio.sleep(1)
        #     await ctx.send(f"{prefix_owo}b")
        #     print(f"{at()}: {Fore.GREEN}succefully owob")

        recentMsg = await ctx.bot.get_channel(clientId).history(limit=5
                                                                ).flatten()
        for msg in recentMsg:
            if msg.author.id == 408785106942164992 and 'spent' in msg.content.lower(
            ):
                useGem = random.choice([1])
                print(f"{Fore.MAGENTA} {useGem}")
                if useGem == 1:
                    async with ctx.typing():
                        await asyncio.sleep(random.choice([1, 2, 3]))
                        await ctx.send(f"{prefix_owo}inv")
                    checkInv = await ctx.bot.get_channel(clientId).history(
                        limit=5).flatten()
                    msgContent = ''
                    for msgonce in checkInv:
                        if 'inventory' in msgonce.content.lower():
                            msgContent = msgonce.content.lower()
                    if msgContent:
                        await gem(ctx, msgContent)

            if msg.author.id == 408785106942164992 and 'captcha' in msg.content.lower(
            ):
                async with ctx.typing():
                    await asyncio.sleep(1)
                    dmcs = False
                    print(f"{at()}: {Fore.RED}stop capcha")

        await asyncio.sleep(random.choice([17, 20]))


async def gem(ctx, msg):
    arrQuantity = []
    invWithQuantity = {}

    inv = re.findall(r'`(.*?)`', msg)
    quantity = re.findall(r'>(.*?)\s', msg)

    # remove 0 before number from inv
    for i in range(len(inv)):
        inv[i] = inv[i].replace('0', '')

    # remove 0 before number from quantity
    for i in range(len(quantity)):
        quantity[i] = quantity[i].replace('0', '')

    for item in quantity:
        arrQuantity.append(item.strip().translate(str.maketrans(dict)))

    for x in range(len(arrQuantity)):
        invWithQuantity[str(inv[x])] = int(arrQuantity[x])

    gem1 = ''
    gem2 = ''
    gem3 = ''

    def getValue(key):
        value = invWithQuantity.get((key))
        if value:
            return value
        else:
            return 0

    for i in range(6):
        if getValue(str(int(i) + 51)) > 0 and getValue(
                str(int(i) + 65)) > 0 and getValue(str(int(i) + 72)) > 0:
            gem1 = str(int(i) + 51)
            gem2 = str(int(i) + 65)
            gem3 = str(int(i) + 72)

            if gem1 and gem2 and gem3:
                break

    async with ctx.typing():
        await asyncio.sleep(random.choice([7, 8, 9]))
        await ctx.send(f"{prefix_owo}use {gem1} {gem2} {gem3}")
        print(f"{at()}: {Fore.YELLOW}use gem {gem1} {gem2} {gem3}")
        await asyncio.sleep(1)


@bot.command()
async def z(ctx):
    await ctx.message.delete()
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def spam(ctx):
    content = ctx.message.content
    status = content.split(' ')[1]
    await ctx.message.delete()
    global spamOwO
    if (status == 'on'):
        spamOwO = True
        print(f"{at()}: {Fore.GREEN}spam on")
    elif (status == 'off'):
        spamOwO = False
        print(f"{at()}: {Fore.RED}spam off")

    while spamOwO:
        await asyncio.sleep(random.choice([21, 32, 43]))
        await ctx.send(f"{prefix_owo}")


@bot.command(pass_context=True)
async def count(ctx):
    await ctx.message.delete()

    channelId = 899852247607943178

    channel = bot.get_channel(channelId)

    global dcount
    dcount = True

    while dcount:
        async with channel.typing():
            await asyncio.sleep(2)
            message = await channel.history(limit=1).flatten()

            last_msg = message[0]

            if (last_msg.author != bot.user and last_msg.author.bot != True
                    and len(last_msg.reactions) != 0):
                print(
                    f"{at()}: {Fore.GREEN} {last_msg.author.name}: {last_msg.content}"
                )
                last_num = await convertNum(last_msg.content.split()[0])

                if (last_num != ''):
                    await channel.send(last_num + 1)
                    print(f"{at()}: {Fore.RED}count: {last_num + 1}")
                    await asyncio.sleep(2)
        await asyncio.sleep(4)


async def convertNum(str):
    num = ''
    try:
        num = int(str)
    except:
        num = ''

    return num


@bot.command()
async def stop_count(ctx):
    await ctx.message.delete()
    global dcount
    dcount = False


@bot.event
async def on_ready():
    activity = discord.Game(name="", type=4)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f''.join("READY"))


bot.run(token, bot=False)
