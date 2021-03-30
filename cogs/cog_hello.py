import discord
from discord.ext import commands

class Greetings(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.command(name='create', aliases=['cr'])
  async def test(self, ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Greetings(bot))