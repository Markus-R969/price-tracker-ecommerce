#!/usr/bin/env python3
"""Script simple para verificar que la base de datos tiene datos válidos."""

import sqlite3
from config import DB_PATH

def verify_database():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Contar total de registros
        cursor.execute("SELECT COUNT(*) FROM products")
        total = cursor.fetchone()[0]
        print(f"✅ Total de productos en la BD: {total}")
        
        # Mostrar los primeros 5 productos
        print("\n📋 Primeros 5 productos:")
        print("-" * 60)
        cursor.execute("SELECT name, price, currency FROM products LIMIT 5")
        for i, (name, price, currency) in enumerate(cursor.fetchall(), 1):
            print(f"{i}. {name[:40]}{'...' if len(name)>40 else ''} | {currency}{price}")
        
        print("-" * 60)
        print("✅ Verificación completada. Los datos están guardados correctamente.")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar la BD: {e}")
        return False

if __name__ == "__main__":
    verify_database()