import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='!!!', intents = discord.Intents.all())

@Bot.event
async def on_ready():
    guild = Bot.get_guild()
    bans = [entry async for entry in guild.bans(limit=2000)]
    for user in bans:
        await guild.unban(user.user)
        print(f'USER UNBANED\t{user.user.name}')


Bot.run("TOKEN")
