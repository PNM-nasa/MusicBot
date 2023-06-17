import discord
from discord.ext import commands
from music import play
from youtubesearchpython import VideosSearch

class Choose(discord.ui.View):
    def __init__(self, ctx, title , url):
        super().__init__()
        self.ctx = ctx
        self.title = title
        self.url = url

    @discord.ui.button(label="1", style=discord.ButtonStyle.green, emoji="🎶")
    async def choose1(self, button : discord.ui.Button, interaction : discord.Interaction):
        await play(self.ctx, self.url[0])
        self.stop()
    @discord.ui.button(label="2", style=discord.ButtonStyle.green, emoji="🎶")
    async def choose2(self, button : discord.ui.Button, interaction : discord.Interaction):
        await play(self.ctx, self.url[1])
        self.stop()
    @discord.ui.button(label="3", style=discord.ButtonStyle.green, emoji="🎶")
    async def choose3(self, button : discord.ui.Button, interaction : discord.Interaction):
        await play(self.ctx, self.url[2])
        self.stop()
    @discord.ui.button(label="4", style=discord.ButtonStyle.green, emoji="🎶")
    async def choose4(self, button : discord.ui.Button, interaction : discord.Interaction):
        await play(self.ctx, self.url[3])
        self.stop()

async def delete(message):
    await message.delete()

class search(commands.Cog):
    def __init__(self , bot : commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Tìm Nhạc Trên YouTube Qua Từ Khoá")
    async def search(self, ctx : commands.Context, query : str):
        info = VideosSearch(query, limit = 4)
        Title = []
        Url = []
        a = info.result()
        for i in range(4):
            title = a['result'][i-1]['title']
            url = a['result'][i-1]['link']
            Title.append(title)
            Url.append(url)

        embed = discord.Embed(title="Search", color=discord.Color.random())
        embed.add_field(name="1.", value=Title[0], inline=False)
        embed.add_field(name="2.", value=Title[1], inline=False)
        embed.add_field(name="3.", value=Title[2], inline=False)
        embed.add_field(name="4.", value=Title[3], inline=False)
        embed.set_footer(text=f"Request By {ctx.author.display_name}", icon_url=ctx.author.avatar)
        view = Choose(ctx , Title, Url)
        message = await ctx.respond(embed = embed, view = view)
    
def setup(bot):
    bot.add_cog(search(bot))
