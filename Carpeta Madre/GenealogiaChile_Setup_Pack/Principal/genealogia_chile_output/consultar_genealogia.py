from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['familias_chile']
coleccion = db['genealogia']

def print_genealogia(persona, nivel=0):
    indent = "  " * nivel
    print(f"{indent}{persona['nombre']} ({persona['familia']}) - Siglo: {persona['siglo']} - Rol: {persona['rol']}")
    for hijo in persona.get("descendientes", []):
        print_genealogia(hijo, nivel + 1)

def consultar_genealogia():
    for doc in coleccion.find():
        print_genealogia(doc)

if __name__ == "__main__":
    consultar_genealogia()
