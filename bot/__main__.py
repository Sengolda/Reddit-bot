from bot.bot import RedditBot

if __name__ == "__main__":
    from config.config import bot_config
    bot = RedditBot()
    bot.run(bot_config.token)