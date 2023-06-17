import discord
from discord.ext import commands
import music

class Utils(discord.ui.View):
    def __init__(self, ctx : commands.Contex):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="Pause", style=discord.ButtonStyle.red, emoji='⏸️')
    async def pase(self, button : discord.ui.Button, interaction : discord.Interaction):
        await music.pause(self.ctx)
    @discord.ui.button(label="Resume", style=discord.ButtonStyle.red, emoji='▶️')
    async def resl(self, button : discord.ui.Button, interaction : discord.Interaction):
        await music.resume(self.ctx)
    @discord.ui.button(label="Stop", style=discord.ButtonStyle.red, emoji='🚶')
    async def resm(self, button : discord.ui.Button, interaction : discord.Interaction):
        self.ctx.voice_client.stop()
        await interaction.response.send_message("Đã Đừng Nhạc")
    @discord.ui.button(label="Leave", style=discord.ButtonStyle.red, emoji='❌')
    async def resbsm(self, button : discord.ui.Button, interaction : discord.Interaction):
        await music.leave(self.ctx)

