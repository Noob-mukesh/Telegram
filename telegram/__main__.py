
import os
import logging
import pyrogram
from os import environ, getenv
from pyrogram import Client
import config 
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", 0))

noob = "🎉 sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ʙᴏᴛ !!"
noobx = "ᴀʀᴇ ʙʜᴀɪ ᴀʙ ʙᴏᴛ ʙɴ ɢʏᴀ ʜᴀɪ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴋʀʟᴇ @mukeshbotzone"


if __name__ == "__main__" :
    print(noob)
    print(noobx)
    app = pyrogram.Client(
        "telegram",        
        config.API_ID,
        config.API_HASH,
        bot_token=BOT_TOKEN,
        plugins = dict(root="telegram/plugins")
 
        )
                          
app.run()
