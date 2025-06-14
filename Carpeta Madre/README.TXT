=============================
DOCUMENTACIÓN DEL PROYECTO
=============================

Nombre del Proyecto:
Genealogía e Historia de Familias Relevantes en Chile (Siglos XV-XXI)

Descripción General:
Este proyecto recopila, organiza y presenta información histórica y genealógica de varias familias importantes en Chile y Europa desde el siglo XV hasta la actualidad.  
Incluye generación de documentos Word y Excel con datos relevantes, imágenes, y base de datos SQL para gestión de información.  
Se ofrece una interfaz gráfica en PyQt para navegación y consulta manual.

-----------------------------
1. REQUERIMIENTOS
-----------------------------
- Python 3.8 o superior
- Librerías Python:
  - pandas
  - openpyxl
  - python-docx
  - pymongo
  - requests
  - PyQt5

Para instalar las librerías:
    pip install pandas openpyxl python-docx pymongo requests PyQt5

-----------------------------
2. ESTRUCTURA DE ARCHIVOS
-----------------------------
- main.py            : Código principal con interfaz gráfica PyQt.
- genealogia.py      : Código para generación de datos genealógicos.
- base_datos.py      : Manejo y creación de base de datos SQL y MongoDB.
- reportes.py        : Generación de Word y Excel con información e imágenes.
- README.txt         : Este archivo de documentación.
- output/            : Carpeta donde se guardan los reportes y archivos generados.
- imágenes/          : Carpeta para almacenar imágenes descargadas (opcional).

-----------------------------
3. USO DEL PROGRAMA
-----------------------------
1) Ejecutar el archivo `main.py` para abrir la interfaz gráfica.
2) Usar el menú para seleccionar:
   - Visualizar información genealógica.
   - Consultar datos históricos.
   - Generar reportes en Word o Excel.
3) Los reportes se guardan en la carpeta `output/`.
4) Se pueden descargar imágenes automáticamente para enriquecer los reportes.
5) La base de datos contiene la información estructurada y permite consultas futuras.

-----------------------------
4. BASE DE DATOS
-----------------------------
- Se crea una base de datos SQLite para almacenar información genealógica.
- También se conecta a MongoDB usando PyMongo para consultas avanzadas.
- Tablas principales incluyen:
  - Familias
  - Personas
  - Relaciones
  - Eventos históricos

-----------------------------
5. INTERFAZ GRÁFICA (PyQt5)
-----------------------------
- Menú principal con botones para:
  - Consultar familia
  - Consultar período histórico
  - Generar reportes
- Paneles para mostrar tablas y textos.
- Opciones para filtrar por apellido, siglo, región, etc.

-----------------------------
6. EXTENSIONES FUTURAS
-----------------------------
- Visualización gráfica de árboles genealógicos.
- Funcionalidad para edición y actualización de datos.
- Integración con bases de datos remotas.
- Exportación en otros formatos (PDF con gráficos, HTML).

-----------------------------
7. NOTAS ADICIONALES
-----------------------------
- La información histórica es recopilada de registros, archivos y bases públicas.
- Las imágenes se obtienen desde Internet, se recomienda revisar derechos de uso.
- El proyecto es un prototipo y puede ampliarse o personalizarse.

-----------------------------
8. CONTACTO / SOPORTE
-----------------------------
Para dudas o sugerencias, contactar con el desarrollador en [alex6romerohernadez@gmail.com]

---

Gracias por usar el proyecto.  
¡Esperamos que sea de gran utilidad para tu investigación!

