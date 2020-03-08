import discord
import asyncio

client = discord.Client()


async def rep():
    await client.wait_until_ready()
    channel = discord.Object(id='***REMOVED***')
    while not client.is_closed:
        await client.send_message(channel, 't!rep <@***REMOVED***>')
        await asyncio.sleep(86460)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(rep())
client.run("***REMOVED***", bot=False)
