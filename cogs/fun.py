import random
from datetime import datetime
import discord
from discord.ext import commands


class Fun(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command(
    name="8ball", 
    description="BRUHHHHHHHHH",
    usage="<question>",
    aliases=['8']
  )
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def _8ball(self, ctx, arg1):
    answers = [
      "It is certain.",
      "It is decidedly so.",
      "Without a doubt.",
      "Yes – definitely.",
      "You may rely on it.",
      "As I see it, yes.",
      "Most likely.",
      "Outlook good.",
      "Yes.",
      "Signs point to yes.",
      "Reply hazy, try again.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don’t count on it.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Very doubtful."
    ]
    embed = discord.Embed(title="🎱 8Ball", description=random.choice(answers), color=0x9CDFFF)
    await ctx.channel.send(embed=embed)
  



def setup(client):
  client.add_cog(Fun(client))