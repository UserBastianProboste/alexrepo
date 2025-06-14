# Parte 5: Guía de instalación y uso
Para que el instalador funcione correctamente:

Descarga el instalador offline de Python 3.11.4 (64 bits) aquí:
https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe

Colócalo en esta carpeta y renómbralo exactamente a:
python-3.11.4-amd64.exe

Instrucciones para compilar y usar el instalador:

1. Descarga e instala Inno Setup:
   https://jrsoftware.org/isinfo.php

2. Coloca el instalador offline de Python 3.11.4 64 bits dentro de installer_files.

3. Abre Inno Setup y carga setup_script.iss.

4. Compila el instalador (F9).

5. Ejecuta el instalador generado en cualquier PC Windows.

6. Usa el acceso directo para iniciar el proyecto.

Puedes extender crear_iso.py con toda la lógica de genealogía y generación de datos que quieras.

Si necesitas añadir dependencias Python, agrégalas en la sección [Run] del script ISS.

---

Contacto para soporte y ampliaciones: [Tu email o alias aquí]
