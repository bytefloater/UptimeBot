import console
import os
from web_interface import startServer
from discord.ext import commands


bot = commands.Bot(
	command_prefix="!",    # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = os.environ.get('discordAuthorID')  # Change to your discord id!!!


@bot.event 
async def on_ready():  # When the bot is ready
    console.log("Logged in as {}".format(bot.user))

extensions = [
	'cogs.cog_uptimerobot',
    'cogs.cog_errors'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

startServer()  # Starts a webserver.
token = os.environ.get("discordBotToken") 
bot.run(token)  # Starts the bot