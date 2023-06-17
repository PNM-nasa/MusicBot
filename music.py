import discord
from discord.ext import commands
from youtubesearchpython import *
import yt_dlp

async def join(ctx : commands.Context):
    if ctx.author.voice == None:
        await ctx.respond("Làm Ơn Hãy Tham Gia 1 Kênh Âm Nhạc")
    if ctx.voice_client == None:
        vc = await ctx.author.voice.channel.connect()
        await ctx.respond("Bot Đã Tham Gia!")
    else:
        await ctx.voice_client.move_to(ctx.author.voice.channel) 
        await ctx.respond("Bot Đã Tham Gia!")

async def leave(ctx : commands.Context):
    if ctx.voice_client == None:
        await ctx.respond("Bot Không Ở Kênh Âm Nhạc Nào Cả!")
    else:
        await ctx.voice_client.disconnect()
        await ctx.respond("Bot Đã Thoát Kênh Âm Nhạc!")

async def play(ctx : commands.Context, url : str):
    if ctx.voice_client == None:
        await ctx.author.voice.channel.connect()
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {
            'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options':'-vn'
            }
    YDL_OPTIONS = {
            'format':'bestaudio'
            }

    await ctx.respond(f"Đang Chơi:{url}")
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        print(info)
        url2 = info['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)

async def pause(ctx : commands.Context):
    ctx.voice_client.pause()
    await ctx.respond("Đã Tạm Đừng ⏸️")

async def resume(ctx : commands.Context):
    ctx.voice_client.resume()
    await ctx.respond("Đã Tiếp Tục ▶️")



