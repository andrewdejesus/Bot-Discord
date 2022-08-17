from concurrent.futures import thread
from discord.ext import commands
from invocadores import pegar_tier_solo
from lol import *
from invocadores import *




class Smarts(commands.Cog):
    """Comandos inteligentes"""
    def __init__(self, bot):
      self.bot = bot


    @commands.command(name="skins", help="Lista skins")
    async def skins_expression(self, ctx, champ):
      name = "".join(champ)
      responses = buscar_champs(name)
      
      if responses:
        for i in ROUPAS:
          
          await ctx.send(str(i))
        
        await ctx.send(">>>>> {} tem um total de: {} Skins".format(champ, len(ROUPAS)))
        await ctx.send(">>>>> Fim das Skins do(a): {}".format(champ))
        ROUPAS.clear()
      else:
        await ctx.send("Esse campeão não existe ou houve erro de digitação. Tente novamente!")


    @commands.command(name="flex", help="Informações do invocador na Flex")
    async def flex_expression(self, ctx, champ):
      name = "".join(champ)

      ranks = pegar_tier_solo(name)
      if ranks:
        await ctx.send("{} {}\n{} PDL\nwins: {}\nlosses: {}".format(ranks[0]['tier'], ranks[0]['rank'], ranks[0]['leaguePoints'], ranks[0]['wins'], ranks[0]['losses']))
      else:
        await ctx.send("Invocador não encontrado")
      

    @commands.command(name="solo", help="Informações do invocador na Solo/Duo")
    async def solo_expression(self, ctx, champ):
      name = "".join(champ)

      ranks = pegar_tier_flex(name)
      if ranks:
        await ctx.send("{} {}\n{} PDL\nwins: {}\nlosses: {}".format(ranks[1]['tier'], ranks[1]['rank'], ranks[1]['leaguePoints'], ranks[1]['wins'], ranks[1]['losses']))
      else:
        await ctx.send("Invocador não encontrado")
      
      
      
def setup(bot):
    bot.add_cog(Smarts(bot))