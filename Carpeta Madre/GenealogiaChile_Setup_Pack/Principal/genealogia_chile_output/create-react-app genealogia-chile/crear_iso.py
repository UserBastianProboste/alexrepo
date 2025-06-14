
# Datos genealógicos simplificados
familias = {
    "Romero": {
        "fundador": "Diego Romero (siglo XVIII)",
        "descendientes": [
            "Juan Romero",
            "Pedro Romero"
        ]
    },
    "Hernández": {
        "fundador": "Miguel Hernández (siglo XVIII)",
        "descendientes": [
            "José Hernández",
            "María Hernández"
        ]
    },
    "Valdés": {
        "fundador": "José Miguel Valdés (siglo XVIII)",
        "descendientes": [
            "Manuel Valdés",
            "Isabel Valdés"
        ]
    },
    "Parra": {
        "fundador": "Carlos Parra (siglo XIX)",
        "descendientes": [
            "Luis Parra"
        ]
    },
    "Molina": {
        "fundador": "Francisco Molina (siglo XVIII)",
        "descendientes": []
    }
}

def mostrar_arbol_genealogico():
    """Imprime en consola la estructura familiar."""
    print("Árbol Genealógico Simplificado\n")
    for familia, datos in familias.items():
        print(f"Familia {familia}:")
        print(f"  Fundador: {datos['fundador']}")
        if datos["descendientes"]:
            print("  Descendientes:")
            for d in datos["descendientes"]:
                print(f"    - {d}")
        else:
            print("  Descendientes: Ninguno registrado")
        print()

def main():
    print("Proyecto Genealógico - Ejemplo básico\n")
    mostrar_arbol_genealogico()

if __name__ == "__main__":
    main()
