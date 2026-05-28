import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "prices.db")
BASE_URL = os.getenv("TARGET_BASE_URL", "https://books.toscrape.com")
MAX_PAGES = int(os.getenv("MAX_PAGES", "3"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # ← Esta línea es la que falta