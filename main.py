from libro import Libro
from socio import Socio
from menu import Menu
from tabla import Tabla
import datetime
import time

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

# --------------- WIP ------------------

def prestamosActuales():
    printTitulo("Prestamos actuales")
    global cache
    libros = cache[0]
    socios = cache[1]
    datos = []
    for libro, socio in zip(libros, socios):
        if libro.fecPrestamo is not None:
            datos.append([
                libro.fecPrestamo,
                libro.titulo,
                socio.nombre
            ])
    tabla = Tabla(["Fecha prestamo","Libro","Socio"], datos)
    tabla.render()
    printFin()

def nuevoSocio():
    menu = Menu("Nuevo Socio WIP")
    menu.render()

def cargarDatos():
    libros = [
            Libro(1, "El Quijote", "Cervantes", "1800", "Novela"),
            Libro(2, "1984", "George Orwell", "1800", "Novela"),
            Libro(3, "It", "Stephen King", "1800", "Novela", "2025-10-10"),
        ]
    socios = [
            Socio(1, "Pepe", "pepe@test.com"),
            Socio(2, "Paco", "paco@test.com"),
            Socio(3, "Pili", "pili@test.com", 3)
        ]
    return libros, socios

# --------------- END WIP ------------------

def Main(bWork = False):
    # 1.Cargar ficheros de libros y socios
    if not(bWork) :
        global cache
        cache = cargarDatos()
        print(f"Cache cargada : {cache}")
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
    # Readme.txt
    # Gestion del tiempo
    return
Main()