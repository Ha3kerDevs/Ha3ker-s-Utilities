import discord
import sys
import traceback
import subprocess
from discord.ext import commands
from cogs.utils import config, checks

class Owner(commands.Cog, command_attrs=dict(hidden=True)):
  
  def __init__(self, client):
    self.client = client

  async def restart_bot(self):
    await self.client.logout()
    subprocess.call([sys.executable, "main.py"])  

  async def stop_bot(self):
    await self.client.logout()

  @commands.command(hidden=True, aliases=['re'])
  @commands.is_owner()
  async def restart(self, ctx):
    channel = self.client.get_channel(808280097844756480)
    embed = discord.Embed(title="Bot Activity:",
    description="Restarting...", color=0xF9F827)

    embed.set_footer(text=f"{config.tm} {config.Version}")

    await channel.send(embed=embed)
    await ctx.message.delete()
    print("Restarting...")
    await self.restart_bot()

  @commands.command(hidden=True)
  @commands.is_owner()
  async def stop(self, ctx):
    channel = self.client.get_channel(808280097844756480)
    embed = discord.Embed(title="Bot Activity:",
    description="Stopped. (Manually)",color=0xEC2828)

    embed.set_footer(text=f"{config.tm} {config.Version}")

    await channel.send(embed=embed)
    await ctx.message.delete()
    print("Stopped")
    await self.stop_bot()
  
  @commands.command(hidden=True)
  @commands.is_owner()
  async def recog(self, ctx, extension):
    await ctx.message.delete()
    self.client.unload_extension(f"cogs.{extension}")
    self.client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Extension **cog.{extension}** reloaded", delete_after=5)
  
  @checks.in_right_channel()
  @commands.command(hidden=True)
  async def annlock(self, ctx):
    await ctx.send(
      "<a:loading:808959142299172864> Testing locked. your lock role will be taken out when it's ready. <a:loading:808959142299172864>"
    )
  
  @commands.command(hidden=True)
  @commands.is_owner()
  async def dm(self, ctx, target: discord.User, *, message: str):
    await target.send(message)
  

def setup(client):
  client.add_cog(Owner(client))