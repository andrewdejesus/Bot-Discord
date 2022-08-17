from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Gerencia o bot"""
    def __init__(self, bot):
     self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"Estou pronto! Estou conectado como {self.bot.user}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
     if isinstance(error,CommandNotFound):
        await ctx.send ("O comando não existe. Digite !help")
     elif isinstance(error,MissingRequiredArgument):
        await ctx.send ("Por favor, enviar todos os argumentos. Digite !help")
     else:
        raise error
    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.bot.user:
         return

      if "vai tomar no cu" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "vai se foder" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "vai se fuder" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "vsf" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "vtnc" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "porra" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

      if "tnc" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()
      if "viado" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()
      if "viadinho" in message.content:
         await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais membros!")
         await message.delete()

        
       

def setup(bot):
  bot.add_cog(Manager(bot))