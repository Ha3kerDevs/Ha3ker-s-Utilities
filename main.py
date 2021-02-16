import discord
import os
import asyncio
from asyncio import sleep
from discord.ext import commands

client = commands.Bot(command_prefix=".")

async def status():
	while True:
		await client.wait_until_ready()
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Ha3ker's Skyland"))
		await sleep(30)
		await client.change_presence(activity=discord.Game(name="with you"))
		await sleep(30)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='the chat'))
		await sleep(30)
		await client.change_presence(activity=discord.Game(name="with the boiss"))
		await sleep(30)
		await client.change_presence(activity=discord.Game(name="in development."))
		await sleep(30)

client.loop.create_task(status())


@client.event
async def on_ready():
    print("bot is ready")
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
                print(f"loaded {filename}")
            except Exception as e:
                print(f"failed to load {filename}")
                print(f"[ERROR] {e}")
        

client.run("Nzk0MTgxNjczMTc2MjY4ODIw.X-3FUg.OGMMOlN5lHjvXcobg-wr85wfUKU")