import discord
from discord.ext import commands
from model import model_load

intents = discord.Intents.default()
intents.message_content = True

harvis = commands.Bot(command_prefix="!", intents=intents)

@harvis.event
async def on_ready():
    print(f'Logged in as {harvis.user}')

@harvis.command()
async def hola(ctx):
    await ctx.send("¡Hola!")

@harvis.command()
async def ayuda(ctx):
    await ctx.send("en que puedo ayudarte?")

@harvis.command()
async def check(ctx):
    await ctx.send("Envia una imagen para analizar")

    def imagen(m):
        return m.author==ctx.author and len(m.attachments) > 0

    try:
        mensaje = await harvis.wait_for('message', check=imagen, timeout=60)
        image = mensaje.attachments[0]
        ruta_imagen = f"img/{image.filename}"
        
        # Se agregó 'await' y se corrigió la ruta
        await image.save(ruta_imagen)
        
        resultado = model_load(
            image_path=ruta_imagen, 
            model_path="keras_model.h5", 
            labels_path="labels.txt"
        )
        await ctx.send(resultado)
        
    except TimeoutError:
        await ctx.send("Se agotó el tiempo de espera. Vuelve a intentar con `!check`.")

harvis.run("YOU_TOKEN")