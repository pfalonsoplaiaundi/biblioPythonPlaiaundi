class Menu:
    def __init__(self, titulo: str, *opciones: str):
        titulo = f" {titulo} "
        ancho = len(titulo) + 2
        for opcion in opciones:
            if len(opcion) > ancho:
                ancho = len(opcion) + 10  # margen visual

        # cabecera
        self.menu = (
            f"{'▄' * ancho}\n"
            f"█{titulo.upper().center(ancho-2, ' ')}█\n"
            f"█{'═' * (ancho-2)}█\n"
        )

        # opciones numeradas
        for i, opcion in enumerate(opciones, start=0):
            self.menu += f"█ {i:<2} - {opcion:<{ancho - 8}}█\n"

        # cierre del marco
        self.menu += f"{'▀' * ancho}"

    def __str__(self):
        return self.menu
            
    def render(self):
        print(self.menu)
        return self.opcion()
     
    # Selector de opcion       
    def opcion(self):
        try:
            opcion = int(input("Elige tu opcion: "))
            return opcion
        except:
            print ("\n[ERROR] -> Elige una opcion valida")
            return self.render()