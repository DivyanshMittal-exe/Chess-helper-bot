import discord
from discord import message
from PIL import ImageGrab
import io
import webbrowser

from details import *
# Defines token and channel number

client = discord.Client()

image = ImageGrab.grabclipboard()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await client.get_channel(channel_number).send(file=discord.File(fp=image_binary, filename='image.png'))
        await client.get_channel(channel_number).send("cv.scan white")

@client.event  
async def on_message(message):
    if message.author.bot:
        try:
            embed_content_in_dict = message.embeds[0].to_dict()
            s = embed_content_in_dict['fields'][-1]['value']
            url = s[s.find('(')+1:s.find(')')]
            webbrowser.open(url, new=2)
        except:
            pass
        
        exit()
        
client.run(TOKEN,bot = False)



