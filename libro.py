class Libro:
    def __init__(self, codigo, titulo, autor, ano, categoria, fecPrestamo = None, codSocio = None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.fecPrestamo = fecPrestamo
        self.codSocio = codSocio
        
    def __str__(self):
        return f"{self.codigo}█{self.titulo}█{self.autor}█{self.ano}█{self.categoria}█{self.fecPrestamo}█{self.codSocio}"