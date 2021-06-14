import discord
from discord.ext import commands

class Help_Command(commands.HelpCommand):
    COLOUR = discord.Colour.orange()
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Bot Commands",description="You can use `r!help [command]` for more info on a command",colour=self.COLOUR)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, cmds in mapping.items():
            if cog is None:
                continue
            name = cog.qualified_name
            filtered = await self.filter_commands(cmds, sort=True)
            if filtered:
                value = "\u2002\n".join(f"`{c.name}`" for c in cmds)
                if cog and cog.description:
                    value = "{0}\n{1}".format(cog.description, value)

                embed.add_field(name=name, value=value)


        await self.get_destination().send(embed=embed)
    
    
    async def send_command_help(self, command):
        embed = discord.Embed(title=command.qualified_name, colour=self.COLOUR)
        embed.add_field(name="Usage:", value=self.get_command_signature(command))
        if command.help:
            embed.description = command.help

        await self.get_destination().send(embed=embed)

def setup(bot:commands.Bot):
    bot.help_command = Help_Command()