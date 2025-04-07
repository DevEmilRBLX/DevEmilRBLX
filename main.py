import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}")

@client.event
async def on_message(message):
    if message.content == "!ping":
        await message.channel.send("Pong!")

# Hol dir den Token aus der Umgebungsvariable
TOKEN = os.getenv("BOT_TOKEN")
client.run(TOKEN)
