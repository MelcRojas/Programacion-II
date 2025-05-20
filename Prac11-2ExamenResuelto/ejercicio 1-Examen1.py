class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        
    def get_precio(self):
        return self.precio

class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

class Obra:
    def __init__(self, titulo, material, artistas, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artistas = artistas
        self.anuncio = anuncio
    
    def agregar_anuncio(self, anuncio):
        self.anuncio = anuncio
        
    def get_artista_con_mas_experiencia(self):
        return max(self.artistas, key=lambda a: a.años_experiencia)
    
    def get_precio(self):
        if self.anuncio:
            return self.anuncio.get_precio()
        return 0

class Pintura(Obra):  
    def __init__(self, titulo, material, artistas, genero, anuncio=None):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero
        
    def __str__(self):
        return f"Pintura: {self.titulo}, Material: {self.material}, Artistas: {[artista.nombre for artista in self.artistas]},Género: {self.genero},Anuncio: {self.anuncio.numero if self.anuncio else 'Sin anuncio'}"

#a) Crear dos objetos Pintura
artista1 = Artista("pepe", "12345678", 8)
artista2 = Artista("pepa", "45678910", 10)
artista3 = Artista("papo", "78910111", 5)

anuncio1 = Anuncio(101, 2000)

pintura1 = Pintura("Amanecer", "Óleo", [artista1, artista2], "Paisaje", anuncio1)
pintura2 = Pintura("Noche", "Acrílico", [artista3], "Abstracto")
print(pintura1)
print(pintura2)

#b) Mostrar artista con más experiencia
pinturas = [pintura1, pintura2]
max_exp = max(pinturas, key=lambda p: p.get_artista_con_mas_experiencia().años_experiencia)
mayor_exp = max_exp.get_artista_con_mas_experiencia()
print("Artista con más experiencia:", mayor_exp.nombre)

#c) Agregar anuncio a pintura 2 y mostrar total
anuncio2 = Anuncio(102, 1500)
pintura2.agregar_anuncio(anuncio2)
monto_total = pintura1.get_precio() + pintura2.get_precio()
print("Monto total de venta:", monto_total)
