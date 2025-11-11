class Socio:
    def __init__(self, codigo, nombre, email, codLibro = None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.codLibro = codLibro
    
    def __str__(self):
        return f"{self.codigo}█{self.nombre}█{self.email}█{self.codLibro}"