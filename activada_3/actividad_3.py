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

#5 Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con
#  parámetros en el constructor. Defina métodos en la clase para calcular el área, el 
# perímetro e indicar si un punto pertenece al círculo o no.

import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def contiene_punto(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio

circulo = Circulo((0, 0), 5)
print(f"Área: {circulo.area():.2f}")
print(f"Perímetro: {circulo.perimetro():.2f}")
print(f"Contiene punto (3, 4): {circulo.contiene_punto((3, 4))}")
print(f"Contiene punto (6, 6): {circulo.contiene_punto((6, 6))}")

#6 Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al 
# momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que
# representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Treboles"
    ESPADAS = "Espadas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):    
        return f"{self.valor} de {self.pinta}"
    
carta1 = Carta("A", Carta.CORAZONES)
print(carta1)  # A de Corazones

carta2 = Carta("K", Carta.ESPADAS)
print(carta2)  # K de Espadas

#7 Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y 
# balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.

class CuentaBancaria:

    def __init__(self, numero_cuenta, propietario, balance = 0.0):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance
    
    def __str__(self):
        return f"Número de cuenta: {self.numero_cuenta}, Propietarios: {', '.join(self.propietarios)}, Balance: {self.balance:.2f}"
 
    def depositar(self, monto):
        self.balance += monto
    
    def retirar(self, monto):
        if monto > self.balance:
            raise ValueError("No hay suficiente saldo en la cuenta")
        self.balance -= monto
    
cuenta = CuentaBancaria("1234567890", ["Juan Pérez", "María García"], 1000.0)
print(cuenta)  
cuenta.depositar(500.0)
print(cuenta)  
cuenta.retirar(200.0)
print(cuenta) 

#8 Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

class CuentaBancaria:
    
    def depositar(self, monto):
         if monto < 0:
            
          self.balance += monto
          print(f"deposito de {monto} reakizado. Nuevo valance: {self.valance}")
         else:
             print("El monto a depositar debe ser mayor a cero.")
             

#9 Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

    def retirar(self, valor):
        if valor > 0:
            if valor <= self.balance:
                self.balance -= valor
                print(f"Retiro de {valor} realizado. Nuevo balance: {self.balance}")
            else:
                print("Fondos insuficientes para el retiro.")
        else:
            print("El valor a retirar debe ser mayor que cero.")

#10 Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un
# porcentaje del 2% sobre el balance de la cuenta

    def aplicar_cuota_manejo(self):
        porcentaje = 0.02
        cuota = self.balance * porcentaje
        self.balance -= cuota
        print(f"Cuota de manejo de {cuota} .El nuevo balance es: {self.balance}")


#11 Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por
# consola los detalles de la cuenta bancari

def mostrar_detalles(self):
        print(f"Su número de cuenta es: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")
