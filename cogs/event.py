import random
import discord
from asyncio import sleep
from discord.ext import commands
from cogs.utils import config

class Event(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  #@commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(title="Slow Down!", description="This command is in cooldown, try again in **%.2f** seconds." % error.retry_after, color=0xEC2828)
      await ctx.send(embed=embed, delete_after=3)
      await ctx.message.delete()
      return
    elif isinstance(error, commands.NotOwner):
      embed = discord.Embed(title="Access Denied!", description="❌ This command is only available for server owner.", color=0xEC2828)
      await ctx.send(embed=embed, delete_after=5)
      await ctx.message.delete()
      return
    elif isinstance(error, discord.HTTPException):
      embed = discord.Embed(title="Error!", description="A HTTP Exception has occurred.")
      await ctx.send(embed=embed)
      await ctx.message.delete()
      return
    elif isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title="Access Denied!", description="❌ You don't have permission to run this command.")
      await ctx.send(embed=embed, delete_after=5)
      await ctx.message.delete()
      return

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = member.guild.get_channel(793679695409053718)
    welcome = [
      f"a **{member.name}**",
      f"b **{member.name}**",
      f"c **{member.name}**",
      f"d **{member.name}**"
    ]
    embed = discord.Embed(description=random.choice(welcome), color=0x9CDFFF)
    embed.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"Member #{member.guild.member_count}", icon_url=member.guild.icon_url)
    
    await channel.send(embed=embed)


def setup(client):
  client.add_cog(Event(client))