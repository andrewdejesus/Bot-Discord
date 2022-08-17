from discord.ext import commands
from lol import *

class Talks(commands.Cog):
    """Conversar com o usuário"""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="oi", help="envia uma saudação")
    async def send_oi(self, ctx):
        name = ctx.author.name

        response = "Olá, " +name 
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Talks(bot))