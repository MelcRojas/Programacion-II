class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
    
    def __str__(self):
        return f"Anuncio: {self.numero}, Precio: {self.precio}"    
        
    def get_precio(self):
        return self.precio
    
    def incrementar_precio(self, incremento):
        self.precio += incremento

class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

class Obra:
    def __init__(self, titulo, material, artistas, anuncio):
        self.titulo = titulo
        self.material = material
        self.artistas = artistas
        self.anuncio = anuncio

    def get_precio(self):
        if self.anuncio:
            return self.anuncio.get_precio()
        return 0
    
    def get_titulo(self):
        return self.titulo
        
    def incrementar_precio_por_artista(self, nombre_artista, incremento):
        for artista in self.artistas:
            if artista.nombre == nombre_artista and self.anuncio:
                self.anuncio.incrementar_precio(incremento)
                print(f"Nuevo precio de {self.titulo}: {self.anuncio.precio} con incremento de {incremento} por {nombre_artista}")
    
    def get_total_experiencia(self):
        return sum(artista.años_experiencia for artista in self.artistas)
    
    def get_cantidad_artistas(self):
        return len(self.artistas)

class Pintura(Obra):
    def __init__(self, titulo, material, artistas, genero, anuncio):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero
        
    def __str__(self):
        return f"Pintura: {self.titulo}, Material: {self.material}, Artistas: {[artista.nombre for artista in self.artistas]}, Género: {self.genero}, Anuncio: {self.anuncio if self.anuncio else 'Sin anuncio'}"

# a) Crear dos pinturas con anuncios de venta
a1 = Artista("Pedro", "11111111", 7)
a2 = Artista("María", "22222222", 9)
a3 = Artista("X", "33333333", 12)

an1 = Anuncio(201, 2500)
an2 = Anuncio(202, 3000)

p1 = Pintura("Pintura1", "Madera", [a1, a2], "Retrato", an1)
p2 = Pintura("Pintura2", "Lienzo", [a3], "Moderno", an2)
print(p1)
print(p2)

# b) Calcular promedio de años de experiencia de artistas de ambas pinturas
total_exp = p1.get_total_experiencia() + p2.get_total_experiencia()
cantidad = p1.get_cantidad_artistas() + p2.get_cantidad_artistas()
print("Promedio años experiencia:", total_exp / cantidad)

# c) Incrementar el precio en X a la pintura del artista con nombre X 

incremento = 500
pinturas = [p1, p2]
artista = "X"
for p in pinturas:
    p.incrementar_precio_por_artista(artista, incremento)
    

