import discord
from cogs.utils import config
from discord.ext import commands
  
class Help(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.command(hidden=True, name="help", description="Shows a list of commands.",)
  async def help(self, ctx, *cmd):
    prefix = self.client.command_prefix
    if not cmd:
      embed = discord.Embed(title="Help Center", description=f"Use `{prefix}help <command>` for help.", color=0x84c2fd)
      embed.set_footer(text=f"{config.tm} {config.Version}")
      for cog in sorted(self.client.cogs):
        value = " ".join(
          f"`{prefix}{str(command)}`" for command in filter(
          lambda x: not x.hidden, sorted(
            self.client.get_cog(cog).get_commands(),
            key=lambda y: y.name
          ) 
          )
        )
        if value:
          embed.add_field(name=f"{cog} Commands", value=value, inline=False)
    else:
      if self.client.get_command(cmd[0].replace(prefix, "")):
        command = self.client.get_command(cmd[0].replace(prefix, ""))
        name = command.name
        usage = command.usage
        aliases = sorted(command.aliases)
        embed = discord.Embed(title=f"Command: {prefix}{name}", description=f"{command.description}", color=0x303337)
        embed.set_footer(text=f"{config.tm} {config.Version} • Arg Usage: <> = Required; [] = Optional")
        if usage:
          embed.add_field(name="Usage", value=f"{prefix}{name} {usage}")
        if aliases:
          embed.add_field(name="Aliases", value=", ".join(f"{prefix}{alias}" for alias in aliases))
      else:
        embed = discord.Embed(
          title="Error!",
          description="Unknown Command",
          color=0xe74c3c
        )
    await ctx.send(embed=embed)
  

def setup(client):
  client.add_cog(Help(client))