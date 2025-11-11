class Tabla:
    # constructor de la utilidad tabla
    def __init__(self, cabeceras, datos):
        self.cabeceras = cabeceras
        self.datos = datos
        self.tabla = self.crearTabla()

    # Calcula el ancho de cada columna según cabecera y datos
    def findAnchoColumnas(self):
        anchos = []
        for i, cabecera in enumerate(self.cabeceras):
            max_len = len(str(cabecera))
            for fila in self.datos:
                if len(str(fila[i])) > max_len:
                    max_len = len(str(fila[i]))
            anchos.append(max_len + 4)  # +4 de margen visual
        return anchos

    # genera la tabla segun los anchos de columna de los datos y cabecera proporcionados
    def crearTabla(self):
        anchos = self.findAnchoColumnas()
        total = sum(anchos) + len(anchos) + 1
        result = "▄" * total + "\n"

        # Cabecera
        result += "█"
        for i, cabecera in enumerate(self.cabeceras):
            result += f"{str(cabecera).center(anchos[i])}█"
        result += "\n" + "█" + "═" * (total - 2) + "█\n"

        # Filas
        for fila in self.datos:
            result += "█"
            for i, dato in enumerate(fila):
                result += f"{str(dato).center(anchos[i])}█"
            result += "\n"

        result += "▀" * total
        return result

    # funcion de renderizacion
    def render(self):
        print(self.tabla)