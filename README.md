# biblioPythonPlaiaundi

Gestión básica de una biblioteca en consola, desarrollada en Python.  
Permite cargar libros y socios, mostrar listas, prestar/devolver libros, buscar, y generar tablas legibles en terminal.

---

## 🧱 Características

- Interfaz de texto (menú de consola) con opciones numeradas.  
- Representación tabular de datos (libros, socios, préstamos) usando caracteres ASCII/Unicode para mejorar la legibilidad.  
- Módulos separados:
  - `libro.py` → clase para gestionar libros.  
  - `socio.py` → clase para gestionar socios.  
  - `menu.py` → clase para mostrar y gestionar el menú de opciones.  
  - `tabla.py` → clase para formatear y mostrar tablas en la consola.  
  - `main.py` → punto de entrada del programa con la lógica principal.  
- Uso de variables globales (`cache`) para almacenar temporalmente listas de libros y socios.  
- Soporte para buscar libros y mostrar sólo los disponibles para préstamo (WIP).  
- Diseño pensado para un entorno de FP Superior (DAM) que permite ampliación futura (persistencia, interfaz gráfica, etc.).

---

## 🚀 Requisitos

- Python 3.10 o superior (por el uso de `match-case`).  
- Sistema operativo: Windows, macOS o Linux (aunque en Windows puede requerir cambiar codificación de consola a UTF-8 para mostrar caracteres especiales correctamente).

---

## 🧑‍💻 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/pfalonsoplaiaundi/biblioPythonPlaiaundi.git

2. Ejecuta desde el main.py:
   ```bash
   python ".\<tu ruta>\python main.py"
