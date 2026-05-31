import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from urllib.parse import urljoin
import logging
from config import BASE_URL, MAX_PAGES

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((requests.RequestException, ConnectionError))
)
def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    response.encoding = 'utf-8'  # Evita problemas con caracteres como £, €, Â
    return response.text

def parse_page(html: str, base_url: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    products = []
    
    for article in soup.select("article.product_pod"):
        name = article.h3.a.get("title", "").strip()
        price_text = article.select_one("p.price_color").get_text(strip=True)
        
        # Limpieza robusta del precio
        price_clean = ''.join(c for c in price_text if c.isdigit() or c in '.-,')
        price_clean = price_clean.replace(',', '.')
        price = float(price_clean)
        
        relative_url = article.h3.a.get("href", "")
        full_url = urljoin(f"{base_url}/catalogue/", relative_url)
        
        products.append({
            "url": full_url,
            "name": name,
            "price": price,
            "currency": "GBP",
            "scraped_at": __import__("datetime").datetime.now().isoformat()
        })
    return products

def run_scraper() -> list[dict]:
    all_products = []
    for page in range(1, MAX_PAGES + 1):
        url = f"{BASE_URL}/catalogue/page-{page}.html"
        logger.info(f"🌐 Página {page}: {url}")
        html = fetch_page(url)
        products = parse_page(html, BASE_URL)
        all_products.extend(products)
        logger.info(f"📦 +{len(products)} productos")
    return all_products