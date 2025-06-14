from pymongo import MongoClient

try:
    # Conexión a MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['Genealogía']

    # Acceder a la colección "familiares"
    coleccion_familiares = db['familiares']

    # Insertar un documento
    nuevo_familiar = {"nombre": "Juan", "apellido": "Perez", "edad": 30}
    resultado = coleccion_familiares.insert_one(nuevo_familiar)
    print(f"Documento insertado con ID: {resultado.inserted_id}")

    # Buscar un documento
    familiar = coleccion_familiares.find_one({"nombre": "Juan"})
    print(f"Documento encontrado: {familiar}")

    # Cerrar la conexión (opcional, se cierra al salir del contexto)
    # client.close()

except Exception as e:
    print(f"Ocurrió un error: {e}")