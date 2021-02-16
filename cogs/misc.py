import discord
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency
        trueLatency = latency * 1000
        await ctx.send(f'Takes {round(trueLatency)} milliseconds to respond.'
                    )
    

def setup(client):
    client.add_cog(Misc(client))