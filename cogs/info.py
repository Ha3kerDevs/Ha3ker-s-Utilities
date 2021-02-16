from datetime import datetime
from typing import Optional
from cogs.utils import config

import platform
import discord, time
import datetime
import psutil
from discord import Embed, Member
from discord.ext import commands

start_time = time.time()

class Information(commands.Cog):
  
  def __init__(self, client):
    self.client = client
    psutil.cpu_percent()
  
  @commands.command(
    name="whois",
    description="Check your or a person's server information.",
    usage='[user]'
  )
  async def whois(self, ctx, target: Optional[Member]):
    target = target or ctx.author

    roles = [role for role in target.roles]
    
    embed = Embed(title="User information",
                  colour=target.colour,
                  timestamp=datetime.datetime.utcnow())
    
    embed.set_thumbnail(url=target.avatar_url)
    embed.set_footer(text=f"ID: {target.id}")

    embed.add_field(name="Name", value=str(target), inline=True)
    
    embed.add_field(name="Guild/Server name", value=target.display_name, inline=True)

    embed.add_field(name=f"Roles [{len(roles[1:])}]", value=" ".join([role.mention for role in roles[1:]]), inline=False)
    
    embed.add_field(name="Status", 
    value=f"Desktop Status: {config.statuses[target.desktop_status]}\n"
          f"Mobile Status: {config.statuses[target.mobile_status]}\n"
          f"Browser Status: {config.statuses[target.web_status]}",
          inline=False
    )

    embed.add_field(name="Registered", value=target.created_at.strftime("%B %d, %Y %I:%M %p UTC"), inline=False)
    
    embed.add_field(name="Joined", value=target.joined_at.strftime("%B %d, %Y %I:%M %p UTC"), inline=False)

    embed.add_field(name="Bot?", value=target.bot, inline=True)
    
    embed.add_field(name="Boosted?", value=bool(target.premium_since), inline=True)
    
    
    await ctx.send(embed=embed)

  @commands.command(pass_context=True)
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def botinfo(self, ctx):
    delta_uptime = datetime.datetime.utcnow() - self.client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    
    embed = discord.Embed(description="_This bot is only designed for Ha3ker's Skyland._",
    colour=0x9CDFFF)
    embed.set_author(name=f"{self.client.user.name}", icon_url=self.client.user.avatar_url)

    embed.add_field(name="Developer", value="TheHa3ker#3080",inline=True)

    embed.add_field(name="Version", value=config.Version,inline=True)

    embed.add_field(name="Usage",
    value=f"```CPU Usage: {cpu}%\nRAM Usage: {ram}%```", inline=False)

    embed.add_field(name="Version",
    value=f"```Python: v{platform.python_version()}\ndiscord.py: v{discord.__version__}```", inline=False)
    
    embed.set_footer(
      text=f"Powered by {config.tm} | Uptime: {days}d, {hours}h, {minutes}m, {seconds}s")
    await ctx.send(embed=embed)
      


    


def setup(client):
    client.add_cog(Information(client))