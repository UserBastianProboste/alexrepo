from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['familias_chile']
coleccion = db['genealogia']

genealogia = {
    "nombre": "José Miguel Valdés",
    "familia": "Valdés",
    "siglo": "XIX",
    "rol": "Político y empresario",
    "imagen_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Coat_of_Arms_of_Chile.svg/120px-Coat_of_Arms_of_Chile.svg.png",
    "descendientes": [
        {
            "nombre": "Ramón Valdés",
            "familia": "Valdés",
            "siglo": "XX",
            "rol": "Político",
            "descendientes": []
        },
        {
            "nombre": "María Valdés",
            "familia": "Valdés",
            "siglo": "XX",
            "rol": "Empresaria",
            "descendientes": []
        }
    ]
}

def insertar_genealogia():
    result = coleccion.insert_one(genealogia)
    print(f"Documento insertado con ID: {result.inserted_id}")

def consultar_genealogia():
    for doc in coleccion.find():
        print_genealogia(doc)

def print_genealogia(persona, nivel=0):
    indent = "  " * nivel
    print(f"{indent}{persona['nombre']} ({persona['familia']}) - Siglo: {persona['siglo']} - Rol: {persona['rol']}")
    for hijo in persona.get("descendientes", []):
        print_genealogia(hijo, nivel + 1)

if __name__ == "__main__":
    # insertar_genealogia()  # Ejecuta solo una vez para no duplicar
    consultar_genealogia()
