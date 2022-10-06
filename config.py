import os 
from os import getenv

API_ID = int(getenv("API_ID", "7507532"))
API_HASH = getenv("API_HASH", "c4f37d9aea37ef639f1f2da178acec3d")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "5207640479"))
OWNER_USERNAME = getenv("OWNER_USERNAME","itz_mst_Boi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","the_support_chat")  # Your own group for support, do not add the @
LOGGER = getenv("LOGGER","-1001770762410")
EVENT_LOGS = (-100177076241)  
LOAD = []
NO_LOAD = ["rss", "cleaner", "connection", "math"]
WEBHOOK = False
INFOPIC = True
URL = None
BOT_NAME = getenv("BOT_NAME", "MUKESH")
