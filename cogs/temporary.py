import aiohttp
import random
import os
from owotext import OwO
import json
import nekos
import discord
from discord import Embed, Member
from discord.ext import commands
from cogs.utils import tempor

class temp(commands.Cog, command_attrs=dict(hidden=True)):

  def __init__(self, client):
    self.client = client
    self.reddit = None

  #@commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)
  @commands.is_owner()
  @commands.is_nsfw()
  async def h(self, ctx):
    embed = discord.Embed(title="h", description="why did you do this")  
    embed.set_footer(text="If the image is not loading, try again. | Taken from Reddit.")
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/MaidH█nt█i/new.json?sort=top') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)
  

  @commands.command(aliases=['n'], hidden=True)
  @commands.is_owner()
  @commands.is_nsfw()
  async def nekos(self, ctx, arg=None):
    await ctx.message.delete()
    embed = discord.Embed(title="noonnoonononnoonon", description="nonononoonononon")
    embed.set_footer(text="If the image is not loading, try again.")
    embed.set_image(url=nekos.img(random.choice(tempor.neko)))
    await ctx.send(embed=embed, delete_after = 60)
  
  @commands.command(help='OwO owoifys a text stwing ( ͡° ᴥ ͡°)')
  async def owoify(self, ctx, *, text: str):
    uwu = OwO()
    await ctx.send(uwu.whatsthis(text))



def setup(client):
  client.add_cog(temp(client))