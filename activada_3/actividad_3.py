#1 Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self):

        return f"Vehículo con velocidad máxima de {self.velocidad_maxima} km/h y kilometraje de {self.kilometraje} km"

mi_vehiculo = Vehiculo(200, 50000)
print(mi_vehiculo)     

#2 Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
#3 A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

    def mostrar(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx ** 2 + dy ** 2) ** 0.5

punto1 = Punto(1, 2)
punto2 = Punto(4, 6)

punto1.mostrar()

punto1.mover(2, 3)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"La distancia entre los puntos es {distancia:.2f}")

#4 Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los 
# puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su 
# perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return ancho == alto
    
punto1 = Punto(1, 1)
punto2 = Punto(5, 5)

rectangulo = Rectangulo(punto1, punto2)
print(f"El perímetro del rectángulo es {rectangulo.calcular_perimetro():.2f}")
print(f"El área del rectángulo es {rectangulo.calcular_area():.2f}")
print(f"El rectángulo es un cuadrado: {rectangulo.es_cuadrado()}")