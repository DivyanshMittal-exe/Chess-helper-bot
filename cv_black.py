import discord
# from discord import messages
from PIL import ImageGrab
import io
import webbrowser
from details import *

image = ImageGrab.grabclipboard()

class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await self.get_channel(channel_number).send(file=discord.File(fp=image_binary, filename='image.png'))
            await self.get_channel(channel_number).send("cv.scan black")
    
    async def on_message(self,message):
        if message.author.bot:
            try:
                embed_content_in_dict = message.embeds[0].to_dict()
                s = embed_content_in_dict['fields'][-1]['value']
                url = s[s.find('(')+1:s.find(')')]
                webbrowser.open(url, new=2)
            except:
                pass
        
            exit()

client = MyClient(intents=discord.Intents.default())
client.run(TOKEN,bot=False)


