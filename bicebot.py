import discord
import roller
import os

PREFIX = os.environ.get("BICEBOT_PREFIX") or "!"

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    content = message.content
    if message.author == client.user:
        return

    if len(content) < 1 or content[0] != PREFIX:
        return

    roll = roller.parsecommand(message.content, PREFIX)
    if roll:
        await message.reply(roll)

client.run(os.environ.get("BICEBOT_TOKEN"))
