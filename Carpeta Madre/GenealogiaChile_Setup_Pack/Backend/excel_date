import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['familias_chile']
coleccion = db['genealogia']

def extraer_a_excel():
    cursor = coleccion.find()
    lista = []

    def recorrer(persona):
        lista.append({
            "Nombre": persona['nombre'],
            "Familia": persona['familia'],
            "Siglo": persona['siglo'],
            "Rol": persona['rol']
        })
        for hijo in persona.get('descendientes', []):
            recorrer(hijo)

    for doc in cursor:
        recorrer(doc)

    df = pd.DataFrame(lista)
    df.to_excel("genealogia_chile.xlsx", index=False)
    print("Datos exportados a genealogia_chile.xlsx")

if __name__ == "__main__":
    extraer_a_excel()
