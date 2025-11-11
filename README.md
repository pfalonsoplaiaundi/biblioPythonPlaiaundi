# biblioPythonPlaiaundi

## 📚 Descripción  
Este proyecto es una aplicación en **Python** para gestionar una pequeña biblioteca: libros, socios y préstamos. Permite registrar libros, asignarlos a socios cuando se prestan, devoluciones, y mantener los datos sincronizados (libro ↔ socio).  

El objetivo es:  
- Tener un sistema sencillo que controle qué libro está prestado a qué socio.  
- Que tanto el archivo de libros como el de socios estén **sincronizados**: si un libro tiene fecha de préstamo y un código de socio, dicho socio debe tener asignado ese libro, y viceversa.  
- Servir como base o ejemplo para implementar posteriores mejoras (interfaz gráfica, base de datos, etc.).

## 🛠️ Estructura del proyecto  
| Archivo         | Función                                                                 |
|-----------------|------------------------------------------------------------------------|
| `main.py`       | Punto de entrada del programa; controla el flujo principal             |
| `menu.py`       | Módulo que implementa el menú de opciones (alta, baja, préstamo…)     |
| `libro.py`      | Definición de la clase `Libro` y métodos relacionados                   |
| `socio.py`      | Definición de la clase `Socio` y métodos relacionados                   |
| `tabla.py`      | Funciones para mostrar los datos en formato tabla, o manejar listas     |
| `README.md`     | Documento de presentación y guía de uso                                |

## 🚀 Instalación y uso  
1. Clona este repositorio:  
   ```bash
   git clone https://github.com/pfalonsoplaiaundi/biblioPythonPlaiaundi.git
   ```  
2. Entra en la carpeta del proyecto:  
   ```bash
   cd biblioPythonPlaiaundi
   ```  
3. Asegúrate de tener instalado Python 3.6 o superior.  
4. Ejecuta el programa:  
   ```bash
   python main.py
   ```  
5. Usa el menú para:  
   - Registrar nuevos libros o nuevos socios  
   - Prestar un libro: asignar libro → socio  
   - Devolver un libro: cancelar la asignación  
   - Ver listados de libros y socios  

## ✅ Reglas de negocio principales  
- Un libro prestado debe tener: `fecPrestamo` definido **y** `codSocio` que apunte a un socio.  
- Dicho socio debe tener su `codLibro` con el código del libro.  
- Si un libro no está prestado (`fecPrestamo = null`), entonces `codSocio = null`.  
- Si un socio no tiene libro asignado, entonces `codLibro = null`.  
- Las operaciones de préstamo y devolución deben mantener estas relaciones correctamente.

## ✨ Mejores prácticas y posibles mejoras  
- Validación de entradas del usuario en el menú  
- Persistencia de datos (archivo JSON / base de datos SQLite) para no perder información al cerrar la aplicación  
- Interfaz gráfica (por ejemplo con Tkinter o PyQt)  
- Función de búsqueda por título, autor o categoría  
- Gestión de vencimientos de préstamo (alertas o listados de libros en espera)  
- Internacionalización (soporte para varios idiomas)  

## 📄 Licencia  
Este proyecto se distribuye bajo la licencia **MIT** (o la que tú prefieras).  
*(Agrega aquí el fichero LICENSE si lo vas a incluir.)*

---

¡Gracias por usar y contribuir a este proyecto! 🙌  