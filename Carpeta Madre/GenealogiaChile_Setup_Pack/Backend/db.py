from pymongo import MongoClient
from typing import List, Optional
from backend.models import Persona, Familia
import bson

class GenealogiaDB:
    def __init__(self, uri="mongodb://localhost:27017", dbname="genealogia"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.personas = self.db.personas
        self.familias = self.db.familias

    # CRUD Personas
    def agregar_persona(self, persona: Persona) -> str:
        data = persona.__dict__.copy()
        if 'id' in data:
            del data['id']
        result = self.personas.insert_one(data)
        return str(result.inserted_id)

    def obtener_persona(self, persona_id: str) -> Optional[Persona]:
        data = self.personas.find_one({"_id": bson.ObjectId(persona_id)})
        if data:
            return Persona(
                id=str(data["_id"]),
                nombre=data.get("nombre", ""),
                apellido_paterno=data.get("apellido_paterno", ""),
                apellido_materno=data.get("apellido_materno", ""),
                fecha_nacimiento=data.get("fecha_nacimiento"),
                lugar_nacimiento=data.get("lugar_nacimiento"),
                notas=data.get("notas"),
            )
        return None

    def listar_personas(self) -> List[Persona]:
        lista = []
        for data in self.personas.find():
            lista.append(Persona(
                id=str(data["_id"]),
                nombre=data.get("nombre", ""),
                apellido_paterno=data.get("apellido_paterno", ""),
                apellido_materno=data.get("apellido_materno", ""),
                fecha_nacimiento=data.get("fecha_nacimiento"),
                lugar_nacimiento=data.get("lugar_nacimiento"),
                notas=data.get("notas"),
            ))
        return lista

    # CRUD Familias
    def agregar_familia(self, familia: Familia) -> str:
        data = familia.__dict__.copy()
        if 'id' in data:
            del data['id']
        result = self.familias.insert_one(data)
        return str(result.inserted_id)

    def obtener_familia(self, familia_id: str) -> Optional[Familia]:
        data = self.familias.find_one({"_id": bson.ObjectId(familia_id)})
        if data:
            return Familia(
                id=str(data["_id"]),
                apellido=data.get("apellido", ""),
                origen=data.get("origen"),
                historia=data.get("historia"),
                miembros=data.get("miembros", []),
            )
        return None

    def listar_familias(self) -> List[Familia]:
        lista = []
        for data in self.familias.find():
            lista.append(Familia(
                id=str(data["_id"]),
                apellido=data.get("apellido", ""),
                origen=data.get("origen"),
                historia=data.get("historia"),
                miembros=data.get("miembros", []),
            ))
        return lista
