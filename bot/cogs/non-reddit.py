import discord
from discord.ext import commands
from typing import Union
from discord import User, Member


class Other(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @commands.command(help="Check the bot's latency")
    async def ping(self,ctx):
        embed=discord.Embed(title="Pong",description=f"Ping: {round(self.bot.latency * 1000,1)}")
        await ctx.send(embed=embed)
    
    @commands.command(help="Kick a member from the server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:Union[Member,User],*, reason):
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked")
    @commands.command(help="Ban a member from the server.")
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:Union[Member,User],*, reason):
        await member.ban(reason=reason)
        await ctx.send(f"{member} was banned")

def setup(bot):
    bot.add_cog(Other(bot))