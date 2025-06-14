import sqlite3
import os

OUTPUT_DIR = "genealogia_chile_output"
DB_PATH = os.path.join(OUTPUT_DIR, "genealogia_familias.db")

def obtener_personas():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, nombre, familia, siglo, rol, padre_id FROM persona")
    personas = c.fetchall()
    conn.close()
    return personas

def construir_arbol(personas):
    personas_dict = {p[0]: {'nombre': p[1], 'familia': p[2], 'siglo': p[3], 'rol': p[4], 'padre_id': p[5], 'hijos': []} for p in personas}

    raiz = []
    for pid, data in personas_dict.items():
        padre_id = data['padre_id']
        if padre_id and padre_id in personas_dict:
            personas_dict[padre_id]['hijos'].append(pid)
        else:
            raiz.append(pid)

    return personas_dict, raiz

def mostrar_arbol(personas_dict, nodos, nivel=0):
    for nodo in nodos:
        persona = personas_dict[nodo]
        indent = "  " * nivel
        print(f"{indent}- {persona['nombre']} ({persona['familia']}, {persona['siglo']}) - {persona['rol']}")
        if persona['hijos']:
            mostrar_arbol(personas_dict, persona['hijos'], nivel+1)

def main():
    personas = obtener_personas()
    personas_dict, raiz = construir_arbol(personas)
    print("Árbol genealógico:\n")
    mostrar_arbol(personas_dict, raiz)

if __name__ == "__main__":
    main()

