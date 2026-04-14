import discord
import os
import re

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_NAMES = {"news", "meme-review"}
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

    if message.author.name == "xavi.campos":
        await message.add_reaction("❤️")

    if message.author.name == "chucho4":
        for emoji in ["🇸", "🇪", "🇽"]:
            await message.add_reaction(emoji)

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
        elif any(word in content_lower for word in ["sardina", "jarry"]):
            await message.reply(file=discord.File("cirno-touhou.gif"))
        elif any(word in content_lower for word in ["feudal", "age", "aoe2"]):
            await message.reply(file=discord.File("wololo.mp3"))
        elif any(word in content_lower for word in ["somin", "yandrak"]):
            await message.reply(file=discord.File("tole-cat.gif"))


client.run(TOKEN)
