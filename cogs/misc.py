from datetime import datetime
from discord.ext import commands
from cogs.utils import config
import discord, datetime, time


start_time = time.time()

class Miscellaneous(commands.Cog):
  
  def __init__(self, client):
    self.client = client


  @commands.command(
    name='ping',
    description='testing',
    usage='',
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def ping(self, ctx):
    start = time.time()
    message = await ctx.send("<a:loading:808959142299172864> Checking latency...")
    embed = discord.Embed(title='Pong!', color=0x3BE067, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"{config.tm} {config.Version}")
    embed.add_field(
      name="Typing latency:",
      value=f"```{round((time.time() - start) * 1000)}ms```",
      inline=True
    )
    embed.add_field(
      name='Websocket Latency:',
      value=f'```{round(self.client.latency * 1000)}ms```'
    )
    await message.edit(content=None, embed=embed)

  @commands.command(hidden=True)
  @commands.is_owner()
  async def say(self, ctx,*, msg):
    await ctx.reply(msg)
  
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def membercount(self, ctx):
    em = discord.Embed(title="Member count:", description=f"{ctx.guild.member_count}",timestamp=datetime.datetime. utcnow(), color=ctx.author.color)
    em.set_footer(text=f"{config.tm} {config.Version}")
    await ctx.send(embed=em)
  
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def uptime(self, ctx):
    delta_uptime = datetime.datetime.utcnow() - self.client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

  



def setup(client):
    client.add_cog(Miscellaneous(client)) 