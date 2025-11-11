from libro import Libro
from socio import Socio
from menu import Menu
from tabla import Tabla
import os
import datetime
import time
import json

cache = []

def printTitulo(titulo):
    print(f"\n{f" {titulo} ":-^40}\n")
    
def printFin():
    print()
    print("-"*40)
    time.sleep(0.1)
    print()

def librosDisponibles():
    printTitulo("LibrosDisponibles")
    global cache
    libros = cache[0]
    filas = []
    for libro in libros:
        if libro.fecPrestamo is None:
            filas.append((
                getattr(libro, "codigo", ""),
                getattr(libro, "titulo", ""),
                getattr(libro, "autor", ""),
                getattr(libro, "ano", ""),
                getattr(libro, "categoria", ""),
                getattr(libro, "fecPrestamo", "")
            ))

    tabla = Tabla(
        ["Codigo", "Titulo", "Autor", "Año", "Categoria", "Fecha prestamo"],
        filas
    )
    tabla.render()
    printFin()

def buscarLibro():
    printTitulo("Busqueda de libros")
    global cache
    libros = cache[0]
    busqueda = input("Filtro: ").lower().strip()
    
    resultados = []
    for libro in libros:
        texto = f"{libro}".lower()
        if busqueda in texto:
            resultados.append(libro)
    
    listaLibros = []
    if not resultados:
        print("\n[INFO] No se encontraron coincidencias.")
        return  
    else:
        for libro in resultados:
            listaLibros.append((
                getattr(libro, "codigo", ""),
                getattr(libro, "titulo", ""),
                getattr(libro, "autor", ""),
                getattr(libro, "ano", ""),
                getattr(libro, "categoria", ""),
                getattr(libro, "fecPrestamo", "")
            ))
    
    tabla = Tabla(["Codigo", "Titulo", "Autor", "Año", "Categoria", "Fecha prestamo"], listaLibros)
    tabla.render()
    printFin()
    
def prestarLibro():
    printTitulo("Prestamo de libros")
    global cache
    libros = cache[0]
    socios = cache[1]
    lib, soc = "", ""
    idLibro, idSocio = int(input("ID libro: ")), int(input("ID socio: "))
    
    for libro in libros:
        if libro.codigo == idLibro:
            print(f"Libro seleccionado: {libro.titulo}")
            if libro.fecPrestamo is None:
                lib = libro
            else: 
                print("No disponible")
                return
            break
        
    for socio in socios:
        if socio.codigo == idSocio:
            print(f"Socio seleccionado: {socio.nombre}")
            if socio.codLibro is None:
                soc = socio
            else: 
                print("Ya tiene un prestamo activo")
                return
            break

    correcto = input("¿Es correcto? ").lower().strip() in ("y", "s", "si", "sí", "yes", "true", "1")
            
    if correcto:
       fecha = datetime.datetime.now()
       lib.fecPrestamo = fecha.date()
       soc.codLibro = idLibro
       datos = [
           [
                lib.fecPrestamo,
                lib.titulo,
                soc.nombre
           ],
       ]
       tabla = Tabla(["Fecha prestamo", "Libro", "Socio"], datos)
       tabla.render()
    printFin()


def devolverLibro():
    printTitulo("Devolver libro")
    global cache
    libros = cache[0]
    socios = cache[1]
    lib, soc = "", ""
    idLibro, idSocio = int(input("ID libro: ")), int(input("ID socio: "))
    
    for libro in libros:
        if libro.codigo == idLibro:
            print(f"Libro seleccionado: {libro.titulo}")
            lib = libro
            break
        
    for socio in socios:
        if socio.codigo == idSocio:
            print(f"Socio seleccionado: {socio.nombre}")
            soc = socio
            break

    correcto = input("¿Es correcto? ").lower().strip() in ("y", "s", "si", "sí", "yes", "true", "1")
            
    if correcto:
       lib.fecPrestamo = None
       soc.codLibro = None
       datos = [
           [
                datetime.datetime.now().date(),
                lib.titulo,
                soc.nombre
           ],
       ]
       tabla = Tabla(["Fecha devolucion", "Libro", "Socio"], datos)
       tabla.render()
    printFin()


def prestamosActuales():
    printTitulo("Prestamos actuales")
    global cache
    libros = cache[0]
    libros = sorted(libros, key=lambda x: x.codigo)
    socios = cache[1]
    datos = []
    for socio in socios:
        if socio.codLibro is not None:
            datos.append([
                libros[socio.codLibro-1].fecPrestamo,
                libros[socio.codLibro-1].codigo,
                libros[socio.codLibro-1].titulo,
                socio.codigo,
                socio.nombre
            ])
    tabla = Tabla(["Fecha prestamo","Cod Libro","Titulo","Cod Socio","Socio"], datos)
    tabla.render()
    printFin()

def nuevoSocio():
    printTitulo("Nuevo socio")
    global cache
    socios = cache[1]
    id = 0
    for socio in socios:
        id = socio.codigo if socio.codigo > id else id
    socio = Socio(id+1, input("Nombre: "), input("Email: "))
    socios.append(socio)
    printFin()

def guardarCache():
    global cache
    libros_dict = [libro.__dict__ for libro in cache[0]]
    socios_dict = [socio.__dict__ for socio in cache[1]]
    data = {
        "libros": libros_dict,
        "socios": socios_dict
    }
    with open("datos.json", "w", encoding="utf-8") as a:
        json.dump(data, a, indent=4, ensure_ascii=False)

def cargarDatos():
    if os.path.exists("datos.json"):
        with open("datos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        libros = [Libro(**libro) for libro in data["libros"]]
        libros = sorted(libros, key=lambda x: x.titulo)
        socios = [Socio(**socio) for socio in data["socios"]]
        socios = sorted(socios, key=lambda x: x.nombre)
        return libros, socios
    return libros, socios

def Main(bWork = False):
    # 1.Cargar ficheros de libros y socios si es el arranque
    if not(bWork) :
        global cache
        cache = cargarDatos()
        
    # 2.Menu -> 0.Salir, 1.Lista libros libres, 2. Buscar libro, 3. Prestar libro, 4. Devolver libro, 5. Socios con libros y 6. Añadir socio
    menu = Menu("Menu", 
                "Salir", 
                "Libros disponibles", 
                "Buscar libro", 
                "Prestar libro", 
                "Devolver libro", 
                "Prestamos actuales", 
                "Nuevo socio"
                )
    match (menu.render()):
        case 0:
            guardarCache()
            return
        case 1:
            librosDisponibles()
            Main(True)
        case 2:
            buscarLibro()
            Main(True)
        case 3:
            prestarLibro()
            Main(True)
        case 4:
            devolverLibro()
            Main(True)
        case 5:
            prestamosActuales()
            Main(True)
        case 6:
            nuevoSocio()
            Main(True)
    return
Main()