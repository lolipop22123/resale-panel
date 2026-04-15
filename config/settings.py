import os
from dotenv import load_dotenv

# load_dotenv()

# Common settings
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_telegram_bot_token_here")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/database.sqlite")
WEB_PORT = int(os.getenv("WEB_PORT", 8000))
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
