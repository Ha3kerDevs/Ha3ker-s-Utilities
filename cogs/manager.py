import discord
from discord.utils import get
from discord.ext import commands


class Manager(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.is_owner()
  async def addrole(self, ctx, role: discord.Role = None, member: discord.Member = None):
    await member.add_roles(role)
    embed = discord.Embed(title="Successful!", description=f"✅ **{role}** role added to **{member}**.")
    await ctx.send(embed=embed, delete_after=10)

  @commands.command()
  @commands.is_owner()
  async def removerole(self, ctx, role: discord.Role = None, member: discord.Member = None):
    await member.remove_roles(role)
    embed = discord.Embed(title="Successful!", description=f"✅ **{role}** role removed to **{member}**.")
    await ctx.send(embed=embed, delete_after=10)





def setup(client):
    client.add_cog(Manager(client))