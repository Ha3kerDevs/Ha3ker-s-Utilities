import discord
import os
import asyncio
import datetime
from asyncio import sleep
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv('.env')

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')
client.launch_time = datetime.datetime.utcnow()

cogs = [
  "cogs.misc",
  "cogs.moderation",
  "cogs.event",
  "cogs.help",
  "cogs.info",
  "cogs.manager",
  "cogs.owner",
  "cogs.temporary",
  "cogs.fun"
]
#_____________Update Status_______________#
async def status():
  while True:
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.users)} members"))
    await sleep(120)
    await client.change_presence(activity=discord.Game(name="Roblox: 4K UHD"))
    await sleep(120)
    await client.change_presence(activity=discord.Streaming(name="Nonsense", url="https://www.youtube.com/watch?v=NfSGm9DDQ3o"))
    await sleep(120)
    await client.change_presence(activity=discord.Game(name="2020 2"))
    await sleep(120)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="music"))
    await sleep(120)


client.loop.create_task(status())
#______________________________________#
@client.event
async def on_ready():
  channel = client.get_channel(808280097844756480)
  embed = discord.Embed(title="Bot Activity:",
  description="Activated.", color=0x3BE067)

  embed.set_footer(text=f"epic")

  await channel.send("<@!341837496763678731>", embed=embed)
  print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  for cog in cogs:
    try:
      client.load_extension(cog)
      print(f"{cog} loaded.")
    except Exception as e:
      print(e)


client.run(os.getenv("DISC0RD_T0KEN"))