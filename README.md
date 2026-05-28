# 🤖 Price Tracker - Case 1

Scraper de precios para e-commerce estático. Extrae, limpia y almacena datos de productos en SQLite.

## 🚀 Instalación rápida
```bash
python -m venv --without-pip .venv
.venv\Scripts\activate
python get-pip.py  # Solo la primera vez
pip install -r requirements.txt
Copy-Item .env.example .env
python main.py