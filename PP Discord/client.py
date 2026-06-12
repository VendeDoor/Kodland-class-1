import discord
from bot_logic import gen_pass, gen_emoji, flip_coin, gen_number

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$generate_password"):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$random_number'):
        await message.channel.send(gen_number(1000))
    else:
        await message.channel.send(message.content)

client.run("token")