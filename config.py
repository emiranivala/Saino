# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25276967"))
API_HASH = getenv("API_HASH", "daf793293a5a244e5c426a129656e0a1")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "922270982").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002262642477")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002437305944"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000000"))

#AutoDeleteTime
SECONDS = int(getenv("SECONDS", "5270400000")) #5_minutes
