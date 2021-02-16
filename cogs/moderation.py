import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command(aliases=['k']) #kick member
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx,member : discord.Member,*,reason= "No reason provided"):
	    try:
		    await ctx.send(member.name + " has been kicked from the Skyland. Reason: "+reason)
		    await member.send("You have been kicked out from the Skyland. Reason: "+reason)
	    except:
		    await ctx.send("The member has their dms closed.")

	    await member.kick(reason=reason)
	    await ctx.message.delete()
    
    @kick.error
    async def clear_error(self, ctx, error):
	    if isinstance(error, commands.MissingRequiredArgument):
		    await ctx.send("Please specify a user to kick.")
		    await ctx.message.delete()
    

    @commands.command(aliases=['b']) #ban member
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx,member : discord.Member,*,reason= "No reason provided"):
	    try:
		    await ctx.send(member.name + " has been banned from the Skyland. Reason: "+reason)
		    await member.send("You have been banned from the Skyland. Reason: "+reason)
	    except:
		    await ctx.send("The member has their dms closed.")

	    await member.ban(reason=reason)
	    await ctx.message.delete()

    @ban.error
    async def clear_error(self, ctx, error):
	    if isinstance(error, commands.MissingRequiredArgument):
		    await ctx.send("Please specify a user to ban.")
		    await ctx.message.delete()





def setup(client):
    client.add_cog(Moderation(client))