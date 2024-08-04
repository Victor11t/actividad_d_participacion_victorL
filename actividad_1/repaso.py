print("hola mundo.")

#1. Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla"
nombre=input("ingrese su nombre:")
edad=int(input("ingrese su edad:"))
print("su nombre es",nombre, "y su edad es",edad)

#2. Escribir una función que calcule el área de un círculo dado su radio."
pi=3.14159265359
radio=eval(input("ingrese el radio: "))
area=pi*(radio**2)
print("el area del circulo es:",area)

#3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla."
from random import randint
numeros=[randint(1,10) for i in range(0,10)]
print(numeros)

#4. Escribir un programa que determine si un número dado es par o impar.
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#5. Crear una función que convierta grados Fahrenheit a grados Celsius.
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")

#6. Crear un programa que calcule la suma de los números en una lista dada.
numeros = [1, 24, 53, 44, 53,26]
suma = sum(numeros)
print("La suma de los números en la lista es:",suma)

#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
numeros = [34, 78, 12, 89, 23, 56, 7]
mayor = max(numeros)
menor = min(numeros)
print("El número más grande en la lista es:",mayor)
print(f"El número más pequeño en la lista es: {menor}")

#8. Crear una función que invierta el orden de los elementos en una lista dada.
mi_lista = [1, 2, 3, 4, 5]
mi_lista = mi_lista[::-1]
print("Lista invertida:", mi_lista)

#9. Crear un programa que genere una matriz de números y la imprima en pantalla.
matriz = []
contador = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador)
        contador = contador + 1
    matriz.append(fila)
for fila in matriz:
    print(fila)

#10. Escribir una función que calcule el factorial de un número dado.
numero = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")

#11. Crear un programa que genere una lista de números pares entre 1 y 100.
pares = []

for numero in range(1, 101):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#12. Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for.
for numero in range(1, 11):
    print(numero)

#13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y
#división.
num1=float(input("ingrese primer un numero"))
num2=float(input("ingrese segundo un numero"))
sum= num1+num2
res=num1-num2
mul= num1*num2
div=num1/num2

print(f"la suma de sus numeros es {sum},la multiplicacion de sus numeros es{mul},la resta de sus numeros es{res},la division de sus numeros es{div}")


#14. Escribir una función que calcule la media aritmética de una lista de números.
umeros = [11, 22, 33, 40, 50]
prom=sum(numeros)/len(numeros)
print(prom)


#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
text = input("Ingresa una cadena de texto: ")
text_limpio = text.replace(" ", "").lower()
if text_limpio == text_limpio[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

