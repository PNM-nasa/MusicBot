import discord
from discord.ext import commands
from music import join, leave, play, pause, resume
from youtubesearchpython import Video, VideosSearch



class Music(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Bot Tham Gia Kênh Âm Thanh")
    async def join(self, ctx : commands.Context):
        await join(ctx)
    @commands.slash_command(description="Bot Thoát Kênh Âm Nhạc")
    async def leave(self, ctx : commands.Context):
        await leave(ctx)
    @commands.slash_command(description="Chơi 1 Bản Nhạc Từ Link Youtube")
    async def play(self, ctx : commands.Context, url : str):
        await play(ctx , url)
    @commands.slash_command(description='Tạm Dừng Bài Hát')
    async def pause(self, ctx : commands.Context):
        await pause(ctx)
    @commands.slash_command(description='Tiếp Tục Bài Hát')
    async def resume(self, ctx : commands.Context):
        await resume(ctx)
    @commands.slash_command(description='Hiển Thị Thông Tin Bot')
    async def info(self, ctx : commands.Context):
        await ctx.respond("Chưa Cập Nhật, Mà T Đc Đẻ Ra Từ KhanhLam(Virual)")
    @commands.slash_command(description='Dừng Nhạc Đang Chơi')
    async def stop(self, ctx : commands.Context):
        await ctx.voice_client.stop()

def setup(bot : commands.Bot):
    bot.add_cog(Music(bot))
