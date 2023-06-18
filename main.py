import discord, json
from discord.ext import commands

f = open('./config.json')
data = json.load(f)

token = data['token']
prefix = data['prefix']

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Yeah", bot.user)

bot.run(token)
