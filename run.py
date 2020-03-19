import os
import discord
import asyncio

client = discord.Client()
DISCORD_CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']
DISCORD_USER_ID = os.environ['DISCORD_USER_ID']
DISCORD_AUTH_TOKEN = os.environ['DISCORD_AUTH_TOKEN']


async def rep():
    await client.wait_until_ready()
    channel = discord.Object(id=DISCORD_CHANNEL_ID)
    while not client.is_closed:
        await client.send_message(channel, f't!rep <@{DISCORD_USER_ID}>')
        await asyncio.sleep(86460)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(rep())
client.run(DISCORD_AUTH_TOKEN, bot=False)
