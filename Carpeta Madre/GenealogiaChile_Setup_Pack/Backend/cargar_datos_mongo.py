from pymongo import MongoClient

# Conexión (ajusta la URL si usas MongoDB Atlas o servidor remoto)
client = MongoClient('mongodb://localhost:27017/')
db = client['familias_chile']
coleccion = db['personajes']

# Datos ejemplo (pueden ser más complejos, con árboles, referencias, etc)
personajes = [
    {
        "familia": "Romero",
        "nombre": "José Romero Silva",
        "siglo": "XVIII",
        "rol": "Terrateniente, fundador de haciendas",
        "imagen_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Coat_of_Arms_of_Spain.svg/120px-Coat_of_Arms_of_Spain.svg.png"
    },
    {
        "familia": "Hernández",
        "nombre": "Manuel Hernández Fuentes",
        "siglo": "XVIII",
        "rol": "Agricultor destacado en Ñuble",
        "imagen_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Coat_of_Arms_of_Chile.svg/120px-Coat_of_Arms_of_Chile.svg.png"
    }
]

def insertar_personajes():
    result = coleccion.insert_many(personajes)
    print(f"Documentos insertados con IDs: {result.inserted_ids}")

def consultar_personajes():
    for doc in coleccion.find().sort("siglo"):
        print(f"{doc['nombre']} ({doc['familia']}) - Siglo: {doc['siglo']} - Rol: {doc['rol']}")
        print(f"Imagen: {doc['imagen_url']}\n")

if __name__ == "__main__":
    # Descomenta la línea para insertar los datos solo una vez
    # insertar_personajes()
    consultar_personajes()
