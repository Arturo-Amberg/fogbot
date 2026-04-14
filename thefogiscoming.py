import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_NAME = "news"
FOG_EMOJI = "🌫️"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == CHANNEL_NAME:
        if "fog" in message.content.lower():
            await message.reply(FOG_EMOJI * 10)
        elif "moreno" in message.content.lower():
            await message.reply(file=discord.File("daleMoreno.mp3"))
        elif "warhammer" in message.content.lower():
            await message.reply(file=discord.File("starking.webp"))
        elif "11" in message.content:
            await message.reply("chupalo entonces")
        elif "me gusta" in message.content.lower():
            await message.reply("el pico")


client.run(TOKEN)
