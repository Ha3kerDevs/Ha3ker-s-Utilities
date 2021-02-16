from cogs.utils import config
from discord.ext import commands


def is_mod():
  def predicate(ctx):
    if ctx.author.id not in config.devs \
     and ctx.author.id not in config.owners \
     and ctx.author.id not in config.mod_roles:
      raise
    else:
      return True
  return commands.check(predicate)

def is_trainee():
  def predicate(ctx):
    if ctx.author.id not in config.devs \
     and ctx.author.id not in config.owners \
     and ctx.author.id not in config.trainee_mod_role:
      raise
    else:
      return True
  return commands.check(predicate)

def in_right_channel():
  async def predicate(ctx):
    if ctx.channel.id not in config.channel_ids \
     and ctx.author.id not in config.owners \
     and ctx.author.id not in config.dev:
      raise
    else:
      return True
  return commands.check(predicate)