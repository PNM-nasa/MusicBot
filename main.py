import discord, json
from discord.ext import commands

f = open('./config.json')
data = json.load(f)

token = data['token']
prefix = data['prefix']

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Yeah, {}".format(bot.user))

@bot.slash_command(description="Kiểm Tra Bot Có Sống Hay Không")
async def ping(ctx : commands.Context):
    await ctx.respond("Pong, Bot Is Online")

cogs_list = [
        'event',
        'Music',
        'search'
        ]

for cogs in cogs_list:
    bot.load_extension(f"cogs.{cogs}")

bot.run(token)
