import discord
from discord.ext import commands
from typing import Tuple
import re


class RedditBot(commands.Bot):
    def __init__(
        self,
        load_extensions=True,
        intents_all=True
    ):
        self.prefix = self.data_mine_prefix
        super().__init__(
            command_prefix=self.prefix,
            intents=discord.Intents.all()
        )
        self.load_ext(
            
                "bot.cogs.reddit"
            
        )
        self.load_ext("bot.cogs.non-reddit")
        self.load_ext("bot.help_command")
    def data_mine_prefix(self,_, message:discord.Message):
        bot_id = self.user.id
        prefix = "r!"
        prefixes = [prefix, f"<@{bot_id}> ", f"<@!{bot_id}>"]
        regex = re.compile(
            "^(" + "|".join(re.escape(p) for p in prefixes) + ").*", flags=re.I
        )
        match = regex.match(message.content)
        if match == None:
            return match.group(1)
        else:
            return prefix
    def load_ext(self,arg):
            try:
                self.load_extension(arg)
            except Exception as e:
                raise e
    async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
        if isinstance(error,commands.CommandInvokeError):
            msg = "commandinvokeerror,please enter correct type on variable."
            await ctx.send(
                embed=discord.Embed(
                    title="Error!",
                    description=msg
                )
            )
            return
        if isinstance(error,commands.CommandNotFound):
            return
        if isinstance(error,commands.MissingRequiredArgument):
            msg = str(error)
            await ctx.send(embed=discord.Embed(title="Error!",description=msg))
            return
        if isinstance(error,commands.MissingPermissions):
            msg = "You don't have the perms to run this command!"
            await ctx.send(embed=discord.Embed(title="Error!",description=msg))
            return
        else:
            raise error
    
    async def on_ready(self):
        print("Ready!")