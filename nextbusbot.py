from discord.ext import commands


# Create the bot.
bot = commands.Bot(command_prefix='bus ', description='Get Bus Notifications from NextBus!')

# Load the nextbus cog.
extensions = ['cogs.nextbus']

for extension in extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# Start the bot.
bot.run('TOKEN')
