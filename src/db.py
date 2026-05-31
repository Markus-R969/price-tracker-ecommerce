import sqlite3
import logging
from config import DB_PATH

logger = logging.getLogger(__name__)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                url TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                currency TEXT DEFAULT 'GBP',
                scraped_at TEXT NOT NULL
            )
        """)
    logger.info("✅ Base de datos inicializada")

def save_product(product: dict):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO products (url, name, price, currency, scraped_at)
            VALUES (:url, :name, :price, :currency, :scraped_at)
            ON CONFLICT(url) DO UPDATE SET
                price = excluded.price,
                scraped_at = excluded.scraped_at
        """, product)
    logger.debug(f"💾 Guardado: {product['name']}")