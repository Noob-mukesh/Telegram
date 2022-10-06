
import os
import logging
import pyrogram
from os import environ, getenv
from pyrogram import Client
import config 
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
#lol
from config import (
    BOT_NAME,
    LOGGER,
    OWNER_ID,
    OWNER_USERNAME,
    SUPPORT_CHAT,
    URL,
    dispatcher,
    pbot,
    updater,
)


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
        plugins = dict(root="telegram/modules")
 
        )
                          
app.run()
