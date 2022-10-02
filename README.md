# Chess helper bot
This self-discord bot uses another discord bot, ["Chess-Vision-AI"](https://chessvision.ai/) to make it easier to read some chess books. All it does is grab the image in your clipboard, and call the Chess-Vision-AI bot, and open the position on lichess, so you can easily analyse it.

The auto hotkey files make it easier to run the script. Simply pressing <kbd>Right Cntrl</kbd> + <kbd>W</kbd> opens up lichess with white to move and <kbd>Right Cntrl</kbd> + <kbd>B</kbd> opens up lichess with black to move.

## Setup
Install the discord.py module[^1]. In a details.py file, just add the "Token" and "channel_number". To get the token, follow this [guide](https://discordhelp.net/discord-token). The channel_number is the Channel ID that the bot will use to communicate with Chess-Vision-AI bot. So just create a new random server, add chess vision ai bot to it, and set channel_number to any of the servers channel-id.

To use the autohotkey, change the path of python, to that of your machines

[^1]: Install any version of type 2.x