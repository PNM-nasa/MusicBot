import discord
from discord.ext import commands

class event(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        print(f"New Member Join: {member.display_name}")

def setup(bot : commands.Bot):
    bot.add_cog(event(bot))
