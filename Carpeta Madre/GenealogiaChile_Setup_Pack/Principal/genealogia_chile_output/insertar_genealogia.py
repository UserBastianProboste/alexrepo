from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['familias_chile']
coleccion = db['genealogia']

genealogia = {
    "nombre": "José Miguel Valdés",
    "familia": "Valdés",
    "siglo": "XIX",
    "rol": "Político y empresario",
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
    coleccion.delete_many({})
    result = coleccion.insert_one(genealogia)
    print(f"Documento insertado con ID: {result.inserted_id}")

if __name__ == "__main__":
    insertar_genealogia()
