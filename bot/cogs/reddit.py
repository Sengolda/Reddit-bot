import discord
from discord.ext import commands
from config.reddit import reddit_config
import asyncpraw
import random

reddit = asyncpraw.Reddit(
    client_id=reddit_config.id,
    client_secret=reddit_config.secret,
    username=reddit_config.user_name,
    user_agent=reddit_config.user_agent
)

class Reddit(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def reddit(self,ctx,*, subreddit,limit=10):
        await ctx.trigger_typing()
        subreddit = await reddit.subreddit(subreddit)
        top = subreddit.top(limit=limit)
        all_subs = []

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed()
        embed.set_image(url=url)

        await ctx.send(embed=embed)
        print(url)

    @commands.command()
    async def aww(self,ctx):
        """
        Get a random cute pic from r/aww
        """
        await ctx.trigger_typing()
        subreddit = await reddit.subreddit("awww")
        top = subreddit.top(limit=10)
        all_subs = []

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed()
        embed.set_image(url=url)

        await ctx.send(embed=embed)
        print(url)

    @commands.command()
    async def cat(self,ctx):
        """
        Get a random cat pic from r/cats
        """
        await ctx.trigger_typing()
        subreddit = await reddit.subreddit("cats")
        top = subreddit.top(limit=10)
        all_subs = []

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed()
        embed.set_image(url=url)

        await ctx.send(embed=embed)
        print(url)

    @commands.command()
    async def dog(self,ctx):
        """
        Get a random cat pic from r/dogpictures
        """
        await ctx.trigger_typing()
        subreddit = await reddit.subreddit("dogpictures")
        top = subreddit.top(limit=10)
        all_subs = []

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed()
        embed.set_image(url=url)

        await ctx.send(embed=embed)
        print(url)

def setup(bot:commands.Bot):
    bot.add_cog(Reddit(bot))