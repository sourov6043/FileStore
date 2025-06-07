import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler

def get_int_env(key, default=0):
    try:
        return int(os.environ.get(key, default))
    except (TypeError, ValueError):
        raise Exception(f"{key} must be set and must be an integer.")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = get_int_env("APP_ID")
API_HASH = os.environ.get("API_HASH", "")
CHANNEL_ID = get_int_env("CHANNEL_ID")
OWNER = os.environ.get("OWNER", "sewxiy")
OWNER_ID = get_int_env("OWNER_ID")
PORT = os.environ.get("PORT", "")
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "showrovislam535")
FSUB_LINK_EXPIRY = get_int_env("FSUB_LINK_EXPIRY", 10)
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/Anime_Cheat_Group")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 8)
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ...</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ our channels...</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>")
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False").lower() == 'true'

LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
