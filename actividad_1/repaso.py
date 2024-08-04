"1. Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla"
nombre=input("ingrese su nombre:")
edad=int(input("ingrese su edad:"))
print("su nombre es",nombre, "y su edad es",edad)

"2. Escribir una función que calcule el área de un círculo dado su radio."
pi=3.14159265359
radio=eval(input("ingrese el radio: "))
area=pi*(radio**2)
print("el area del circulo es:",area)

from random import randint
numeros=[randint(1,10) for i in range(0,10)]
print(numeros)