import sqlite3
import os

OUTPUT_DIR = "genealogia_chile_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DB_PATH = os.path.join(OUTPUT_DIR, "genealogia_familias.db")

def crear_base_datos():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS persona (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        familia TEXT NOT NULL,
        siglo TEXT,
        rol TEXT,
        padre_id INTEGER,
        FOREIGN KEY(padre_id) REFERENCES persona(id)
    )
    ''')

    conn.commit()
    conn.close()
    print(f"[SQL] Base de datos creada en {DB_PATH}")

def insertar_personas():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Ejemplo básico, agrega más según necesites
    personas = [
        (1, "José Miguel Valdés", "Valdés", "XIX", "Político y empresario", None),
        (2, "Ramón Valdés", "Valdés", "XX", "Político", 1),
        (3, "María Valdés", "Valdés", "XX", "Empresaria", 1),
        (4, "Juan Hernández", "Hernández", "XVIII", "Primer chileno de la familia", None),
        (5, "Pedro Hernández", "Hernández", "XIX", "Militar", 4),
        (6, "Luis Hernández", "Hernández", "XX", "Político", 5)
        # Puedes añadir más...
    ]

    c.execute("DELETE FROM persona")

    for p in personas:
        c.execute('''
            INSERT INTO persona (id, nombre, familia, siglo, rol, padre_id) VALUES (?, ?, ?, ?, ?, ?)
        ''', p)

    conn.commit()
    conn.close()
    print("[SQL] Datos insertados correctamente")

def main():
    crear_base_datos()
    insertar_personas()

if __name__ == "__main__":
    main()
