import discord
import os
import re

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_NAMES = {"gassy", "meme-review"}
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

    if message.channel.name in CHANNEL_NAMES:
        content_lower = message.content.lower()
        if "the fog is coming" in content_lower:
            await message.channel.send("the fog is coming", tts=True)
        elif "fog" in content_lower:
            await message.reply(FOG_EMOJI * 10)
        elif "xavi" in content_lower:
            await message.reply(file=discord.File("reari-dog-barking.gif"))
        elif "moreno" in content_lower:
            await message.reply(file=discord.File("daleMoreno.mp3"))
        elif re.search(r'\b(war|warhammer|hammer)\b', content_lower):
            await message.reply(file=discord.File("starking.webp"))
        elif "11" in message.content:
            await message.reply("chupalo entonces")
        elif "me gusta" in content_lower:
            await message.reply("el pico")


client.run(TOKEN)
