import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands


client = discord.Client()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents=intents)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()


if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            bot.load_extension(f"cogs.{extension}")


@bot.event
async def on_ready():
    print("Bot is ready!")


bot.run(token)
