#  Price Tracker | Rastreador de Precios E-Commerce

Automatización en Python para monitorear precios de productos en tiendas online, guardar histórico y generar reportes comparativos listos para Excel/CSV.

---

## 📦 ¿Qué hace?
✅ Consulta precios actuales vía URL o catálogo  
✅ Guarda histórico con fecha/hora en base de datos local  
✅ Exporta a Excel/CSV con formato limpio y filtros  
✅ Programable: ejecuta manual o vía \un_scheduler.ps1\  
✅ 100% local: sin suscripciones, sin APIs de terceros  

---

## 🚀 Instalación y Uso
1. Clona o descarga el repositorio
2. Instala dependencias:
   \\\ash
   pip install -r requirements.txt
   \\\
3. Configura el producto:
   - Copia \.env.example\ → \.env\
   - Edita \PRODUCT_URL\ y \CHECK_INTERVAL\
4. Ejecuta:
   \\\ash
   python src/main.py
   \\\

---

##  Salida
Se genera automáticamente:
- \precios_competidores.csv\ → Histórico listo para Excel/Google Sheets
- \prices.db\ → Base de datos SQLite para consultas avanzadas
- \logs/\ → Registro de ejecución para depuración

---

## 💼 Casos de Uso
-  Seguimiento de precios para compras estratégicas
-  Análisis de competencia para vendedores e-commerce
-  Automatización de sourcing para tiendas online
-  Alertas de caída de precio (configurable)

---

## ⚙️ Personalización (para clientes)
| Módulo | Descripción |
|--------|-------------|
| 🌍 Multi-tienda | Amazon, eBay, PcComponentes, AliExpress, etc. |
| ⏰ Programación | Task Scheduler / cron para ejecución diaria |
|  Alertas | Email/Telegram cuando el precio baje X% |
| 📈 Dashboard | Integración con Power BI / Google Data Studio |

---

## 📩 Soporte y Desarrollo a Medida
¿Necesitas rastrear múltiples productos, tiendas específicas o alertas automáticas?  
📧 [mark.markuslab@gmail.com](mailto:mark.markuslab@gmail.com) | 💼 Portfolio: [GitHub](https://github.com/Markus-R969)

*Hecho con Python, BeautifulSoup y SQLite. Código limpio, documentado y listo para producción.*
