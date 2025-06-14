from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Persona:
    id: Optional[str] = None  # MongoDB ObjectId como string
    nombre: str = ""
    apellido_paterno: str = ""
    apellido_materno: str = ""
    fecha_nacimiento: Optional[str] = None  # formato 'YYYY-MM-DD'
    lugar_nacimiento: Optional[str] = None
    notas: Optional[str] = None

@dataclass
class Familia:
    id: Optional[str] = None
    apellido: str = ""
    origen: Optional[str] = None  # Ej: España, Chile, etc
    historia: Optional[str] = None
    miembros: List[str] = field(default_factory=list)  # IDs de Personas
