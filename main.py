import discord, setting, random, time, wavelink, requests, json
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(bot)
# @bot.event
# async def on_ready():
#     print('1414124')
#     for guild in client.guilds:
#         print(f"Tên Server: {guild.name}, ID: {guild.id}")
#         await tree.sync(guild=discord.Object(id=guild.id))
#         print('ok')


imge = []
@bot.command()
async def img_random(ctx):
    if not imge:
        try:
            res = requests.get("https://api.nekosapi.com/v3/images/random").json()['items']
            await ctx.send(res[0]['image_url'])
            for i in range(1, len(res)):
                imge.append(res[i]['image_url'])
        except:
            await ctx.send('Lỗi API')
    else:
        await ctx.send(imge[0])
        imge.pop(0)    


@bot.command()
async def hentai(ctx):
    # await ctx.message.delete()
    try:
        res = requests.get("https://nekos.pro/api/random").json()
        await ctx.send(res['url'])
    except:
        await ctx.send('Lỗi API')
 
@bot.command()
async def neko(ctx):
    try:
        res = requests.get("https://nekos.pro/api/neko").json()
        await ctx.send(res['url'])
    except:
        await ctx.send('Lỗi API')  

@bot.command(name='guild_id')
async def guild_id(ctx):
    # Lấy Guild ID từ ngữ cảnh của lệnh
    guild_id = ctx.guild.id
    await ctx.send(f"Guild ID: {guild_id}, {ctx.guild.name}")
    await bot.guild
# @bot.slas
# async def gif(ctx, params):
#     res = requests.get(f'https://api.otakugifs.xyz/gif?reaction={params}').json()['url']
#     discord.MessageType.reply('ok')
#     await ctx.send(res)








# @bot.command()
# async def waifu(ctx):
#     res = requests.get(f'https://waifu.it/api/v4/waifu', 
#     headers={
#         "Authorization": {setting.WAIFU_TOKEN}
#     },
# ).json()
#     print(res)

@bot.command()
async def fuck_hai(ctx, e : int):
    content = ['Sv Hải gay yêu Hiếu', 
                'Đcmm Hải ăn cứt', 
                'đcmmmmm', 
                'Hải bú cu Trường',
                'Hải ăn l', 
                'Hải ăn cứt',
                'hải bú cu',
                'Hải sóc lọ',
                'Hải xem séc',
                'Hải 3cm',
                'lol'
                'sv hải'
                ]
    for _ in range(e):
        await ctx.send(random.choice(content))
        time.sleep(0.3)

bot.run(setting.DISCORD_API)