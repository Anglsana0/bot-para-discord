import discord
import random




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
    if message.content.startswith('!hola'):
        await message.channel.send("¡Hola!")
    elif message.content.startswith('!Adios'):
        await message.channel.send("\\Nos vemos")
    elif message.content.startswith('!numero al alzar'):
       
        NUM = random.randint(0,10000)
        await message.channel.send(f"Número al azar: {NUM}")
    else:
        await message.channel.send(message.content)

client.run("#aqui va su token")
