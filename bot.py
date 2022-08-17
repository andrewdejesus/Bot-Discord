import os
from decouple import config
from discord.ext import commands
from lol import *
bot = commands.Bot("!")

def load_cogs(bot):
   bot.load_extension("manager")

   for file in os.listdir("commands"):
     if file.endswith(".py"):
       cog = file[:-3]
       bot.load_extension(f"commands.{cog}")


load_cogs(bot)

#ultima linha
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)