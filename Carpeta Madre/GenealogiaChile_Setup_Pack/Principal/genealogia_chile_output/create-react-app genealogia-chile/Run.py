from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit, QMessageBox
)
import sys
from pymongo import Client

def insertar_datos_iniciales(db):
    familias = [
        {"apellido": "Romero", "descripcion": "Familia con influencia desde el siglo XVIII."},
        {"apellido": "Valdés", "descripcion": "Familia histórica del Maule y Ñuble."},
        {"apellido": "Hernández", "descripcion": "Primeros colonos con presencia en Chile."}
    ]
    res = db.familias.insert_many(familias)

    personas = [
        {"nombre": "Juan Romero", "familia_id": res.inserted_ids[0], "bio": "Primer Romero registrado en Chile."},
        {"nombre": "José Miguel Valdés", "familia_id": res.inserted_ids[1], "bio": "Político destacado del siglo XIX."},
        {"nombre": "Francisco Hernández", "familia_id": res.inserted_ids[2], "bio": "Primer Hernández asentado en Chile."}
    ]
    db.personas.insert_many(personas)

class GenealogiaApp(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Genealogía Familias Chile")
        self.resize(600, 400)
        self.db = db

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label_search = QLabel("Buscar familias:")
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Escribe para filtrar apellidos...")
        self.search_bar.textChanged.connect(self.filtrar_familias)

        layout.addWidget(self.label_search)
        layout.addWidget(self.search_bar)

        self.list_fam = QListWidget()
        self.list_fam.itemClicked.connect(self.mostrar_familia_info)
        layout.addWidget(QLabel("Familias:"))
        layout.addWidget(self.list_fam)

        self.list_personas = QListWidget()
        self.list_personas.itemClicked.connect(self.mostrar_persona_info)
        layout.addWidget(QLabel("Personas en familia:"))
        layout.addWidget(self.list_personas)

        self.cargar_familias()

    def cargar_familias(self):
        self.list_fam.clear()
        familias = self.db.familias.find()
        self.familias = list(familias)
        for fam in self.familias:
            self.list_fam.addItem(f"{fam['apellido']} (ID: {fam['_id']})")

    def filtrar_familias(self):
        texto = self.search_bar.text().lower()
        self.list_fam.clear()
        for fam in self.familias:
            if texto in fam['apellido'].lower():
                self.list_fam.addItem(f"{fam['apellido']} (ID: {fam['_id']})")
        self.list_personas.clear()

    def mostrar_familia_info(self, item):
        try:
            id_str = item.text().split("ID: ")[1].rstrip(')')
        except:
            return
        fam = next((f for f in self.familias if str(f['_id']) == id_str), None)
        if fam:
            QMessageBox.information(self, f"Familia {fam['apellido']}",
                                    f"Apellido: {fam['apellido']}\nDescripción: {fam.get('descripcion','No info')}")
            self.list_personas.clear()
            personas = self.db.personas.find({"familia_id": fam['_id']})
            self.personas_fam = list(personas)
            for p in self.personas_fam:
                self.list_personas.addItem(f"{p['nombre']} (ID: {p['_id']})")

    def mostrar_persona_info(self, item):
        try:
            id_str = item.text().split("ID: ")[1].rstrip(')')
        except:
            return
        per = next((p for p in self.personas_fam if str(p['_id']) == id_str), None)
        if per:
            QMessageBox.information(self, f"Persona: {per['nombre']}",
                                    f"Nombre: {per['nombre']}\nBiografía: {per.get('bio','No info')}")

if __name__ == "__main__":
    client = Client("mongodb://localhost:27017")
    db = client["genealogia_db"]
    crear_iso()
    pimongo_db()
    # Solo insertar datos iniciales si la colección está vacía
    if db.familias.count_documents({}) == 0:
        insertar_datos_iniciales(db)

    app = QApplication(sys.argv)
    window = GenealogiaApp(db)
    window.show()
    sys.exit(app.exec())
