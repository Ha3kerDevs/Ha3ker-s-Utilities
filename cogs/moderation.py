from datetime import datetime
import discord
from discord.ext import commands
from cogs.utils import config

class Moderation(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  #____________Kick____________#
  @commands.command(
    name='kick',
    description='testing',
    usage='<member> [reason]',
    aliases=['k']
  )
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx,member : discord.Member,*,reason="No reason provided"):
    channel = member.guild.get_channel(798728528094036000)
    try:
      embed1 = discord.Embed(description=f"✅ **{member.name}** has been kicked from the skyland. | Reason: **{reason}**", color=0x3BE067)
      await ctx.send(embed=embed1, delete_after=8)
      await member.send("You have been kicked from TheHa3ker's Skyland. Reason: "+reason)
    except:
      embed2 = discord.Embed(description="The member has their dms closed.", color=0x9CDFFF)
      await ctx.send(embed=embed2, delete_after=6)
    
    embed3 = discord.Embed(title="Member Kicked",color=0xFFC300, timestamp = datetime.utcnow())
    embed3.add_field(name="Target", value=f"{member.mention} (`{member.id}`)", inline=False)
    embed3.add_field(name="Moderator", value=f"{ctx.message.author.mention} (`{ctx.message.author.id}`)", inline=False)
    embed3.add_field(name="Reason", value=reason, inline=False)
    embed3.set_footer(text=f"{config.tm} {config.Version}")
    await channel.send(embed=embed3)

    await member.kick(reason=reason)
    await ctx.message.delete()

  @kick.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(description="❌ Please specify a user to kick.", color=0xEC2828)
      await ctx.send(embed=embed, delete_after=5)
      await ctx.message.delete()

  
  #____________Ban____________#
  @commands.command(
    name='ban',
    description='testing',
    usage='<member> [reason]',
    aliases=['b']
  )
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx,member : discord.Member,*,reason="No reason provided"):
    channel = member.guild.get_channel(798728528094036000)
    try:
      embed1 = discord.Embed(description=f"✅ **{member.name}** has been banned from the skyland. | Reason: **{reason}**", color=0x3BE067)
      await ctx.send(embed=embed1, delete_after=8)
      await member.send("You have been banned from TheHa3ker's Skyland. | Reason: " +reason)
    except:
      embed2 = discord.Embed(description="The member has thier dms closed.", color=0xEC2828)
      await ctx.send(embed=embed2, delete_after=5)
    
    embed3 = discord.Embed(title="Member Banned", color=0xE91C1C, timestamp = datetime.utcnow())
    embed3.add_field(name="Target", value=f"{member.mention} (`{member.id}`)", inline=False)
    embed3.add_field(name="Moderator", value=f"{ctx.message.author.mention} (`{ctx.message.author.id}`)", inline=False)
    embed3.add_field(name="Reason", value=reason, inline=False)
    embed3.set_footer(text=f"{config.tm} {config.Version}")
    await channel.send(embed=embed3)

    await member.ban(reason=reason)
    await ctx.message.delete()
    
  @ban.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(description="❌ Please specify a user to ban.", color=0xEC2828)
      await ctx.send(embed=embed, delete_after=5)
      await ctx.message.delete()
  
  #____________Mute____________#
  
    

def setup(client):
    client.add_cog(Moderation(client))