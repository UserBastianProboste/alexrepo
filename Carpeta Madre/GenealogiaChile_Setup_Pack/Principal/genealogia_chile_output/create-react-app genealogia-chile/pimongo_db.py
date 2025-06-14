
from pymongo import MongoClient

class GenealogiaDB:
    def __init__(self, db_name="genealogia"):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db.familias

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

if __name__ == "__main__":
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
