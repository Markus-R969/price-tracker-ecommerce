import logging
import sqlite3
import pandas as pd
from config import LOG_LEVEL, DB_PATH
from db import init_db, save_product
from scraper import run_scraper

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def export_to_csv():
    """Exporta los datos de la BD a un CSV compatible con Excel."""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT url, name, price, currency, scraped_at FROM products", conn)
        csv_path = "precios_competidores.csv"
        # utf-8-sig garantiza que Excel abra acentos, ñ y símbolos correctamente
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        conn.close()
        logger.info(f"📄 Exportado a CSV: {csv_path} ({len(df)} registros)")
    except Exception as e:
        logger.error(f"❌ Error al exportar a CSV: {e}")
        import traceback
        traceback.print_exc()

def main():
    logger.info("🚀 Price Tracker v1.0 - Iniciando")
    init_db()
    products = run_scraper()
    
    saved_count = 0
    for prod in products:
        save_product(prod)
        saved_count += 1
    
    logger.info(f"✅ Finalizado. {saved_count} registros procesados.")
    
    # ✅ Llamada a la función de exportación
    export_to_csv()

if __name__ == "__main__":
    main()