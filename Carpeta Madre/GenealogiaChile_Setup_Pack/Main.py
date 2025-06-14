from pymongo import pimongo

class GenealogiaDB:
        
    def menu_interactivo():
            
        def __init__(self, db_name="genealogia"):
                self.client = Pimongo()
                self.db = self.client[db_name]
                    self.collection = self.db.familias
            while True:
                print("\n====== MENÚ GENEALÓGICO ======")
                print("1. Ver árbol genealógico completo")
                print("2. Buscar personas por familia")
                print("3. Buscar personas por siglo")
                print("4. Buscar por nombre")
                print("5. Exportar árbol a Word")
                print("6. Exportar árbol a PDF")
                print("7. Salir")
                opcion = input("Selecciona una opción (1-7): ")

                if opcion == "1":
                    personas = obtener_personas()
                    personas_dict, raiz = construir_arbol(personas)
                    print("\nÁrbol genealógico:")
                    imprimir_arbol(personas_dict, raiz)

                elif opcion == "2":
                    familia = input("Escribe el apellido de la familia (Ej: Valdés): ")
                    mostrar_por_familia(familia)

                elif opcion == "3":
                    siglo = input("Escribe el siglo (Ej: XIX): ")
                    mostrar_por_siglo(siglo)

                elif opcion == "4":
                    nombre = input("Escribe parte o todo el nombre: ")
                    buscar_por_nombre(nombre)

                elif opcion == "5":
                    generar_word()

                elif opcion == "6":
                    generar_pdf()

                elif opcion == "7":
                    print("Saliendo del programa...")
                    break

                else:
                    print("Opción no válida. Intenta de nuevo.")


        def insertar_familia(self, familia):
                """
                Inserta una familia en la base de datos.
                familia: dict con la estructura {'nombre': str, 'fundador': str, 'descendientes': list}
                """
                return self.collection.insert_one(familia)

        def obtener_familias(self):
                """Devuelve todas las familias almacenadas."""
                return list(self.collection.find())

        def buscar_familia(self, nombre):
                """Busca una familia por nombre."""
                return self.collection.find_one({"nombre": nombre})

         def cerrar(self):
                """Cierra la conexión a la base de datos."""
                self.client.close()

        def imprimir_arbol(personas_dict, nodos, nivel=0):
            for nodo in nodos:
                persona = personas_dict[nodo]
                indent = "    " * nivel
                print(f"{indent}- {persona['nombre']} ({persona['familia']}, {persona['siglo']}) - {persona['rol']}")
                if persona['hijos']:
                    imprimir_arbol(personas_dict, persona['hijos'], nivel + 1)

        def mostrar_por_familia(familia):
            personas = obtener_personas()
            encontrados = [p for p in personas if p[2].lower() == familia.lower()]
            if encontrados:
                print(f"\nMiembros de la familia {familia}:")
                for p in encontrados:
                    print(f"- {p[1]} ({p[3]}, {p[4]})")
            else:
                print(f"No se encontraron personas de la familia {familia}.")

        def mostrar_por_siglo(siglo):
            personas = obtener_personas()
            encontrados = [p for p in personas if p[3] == siglo]
            if encontrados:
                print(f"\nPersonas del siglo {siglo}:")
                for p in encontrados:
                    print(f"- {p[1]} ({p[2]}, {p[4]})")
            else:
                print(f"No se encontraron personas del siglo {siglo}.")

        def buscar_por_nombre(nombre):
            personas = obtener_personas()
            encontrados = [p for p in personas if nombre.lower() in p[1].lower()]
            if encontrados:
                print(f"\nResultados de búsqueda por nombre '{nombre}':")
                for p in encontrados:
                    print(f"- {p[1]} ({p[2]}, {p[3]}, {p[4]})")
            else:
                print(f"No se encontraron personas con el nombre '{nombre}'.")

        # Sustituye la línea final del script por esto:
        if __name__ == "__main__":
            print("Inicializando sistema genealógico...")
            descargar_imagenes()
            crear_base_datos()
            insertar_personas()
            menu_interactivo()

            # Test rápido
            db = GenealogiaDB()

            familia_romero = {
                "nombre": "Romero",
                "fundador": "Diego Romero (siglo XVIII)",
                "descendientes": ["Juan Romero", "Pedro Romero"]
            }

            db.insertar_familia(familia_romero)
            familias = db.obtener_familias()
            for fam in familias:
                print(fam)
            db.cerrar()



            

