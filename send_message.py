from os import getenv
import discord
import asyncio


client = discord.Client()
DISCORD_CHANNEL_ID = int(getenv('DISCORD_CHANNEL_ID'))
DISCORD_USER_ID = int(getenv('DISCORD_USER_ID'))
DISCORD_AUTH_TOKEN = getenv('DISCORD_AUTH_TOKEN')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(f't!rep <@{DISCORD_USER_ID}>')
    await client.close()

client.run(DISCORD_AUTH_TOKEN, bot=False)
