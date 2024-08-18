import os

API_ID    = os.environ.get("API_ID", "24519365")
API_HASH  = os.environ.get("API_HASH", "48508ad3b574199df57d2a16ae46a4fe")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7176989009:AAFjF3HX84ZK5ZEoU3sh_potj3j91YrEJLY") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
