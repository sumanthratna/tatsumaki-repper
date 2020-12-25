from os import getenv
import discord
import asyncio


client = discord.Client()
DISCORD_CHANNEL_ID = getenv('DISCORD_CHANNEL_ID')
DISCORD_USER_ID = getenv('DISCORD_USER_ID')
DISCORD_AUTH_TOKEN = getenv('DISCORD_AUTH_TOKEN')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = discord.get_channel(DISCORD_CHANNEL_ID)
    await client.send_message(channel, f't!rep <@{DISCORD_USER_ID}>')
    client.close()

client.run(DISCORD_AUTH_TOKEN, bot=False)
