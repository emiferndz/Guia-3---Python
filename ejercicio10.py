#Crear un programa en el que el usuario introduzca números enteros hasta adivinar el número aleatorio entre 0 y 100 generado al azar por el ordenador. El programa debe avisar si el número introducido por el usuario es más grande o más pequeño que el número generado aleatoriamente
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

import random

numeroaleatorio = random.randint(0,100)

print("Adivina el numero aleatorio entre 0 y 100")
intentosjugador = 0

while True:
    intentosjugador = int(input("Ingrese un numero: "))
    if intentosjugador > numeroaleatorio:
        print("El numero ingresado es mas pequeño")
    elif intentosjugador < numeroaleatorio:
        print("El numero ingresado es mas grande")
    else:
        print("Adivinaste el numero")
        break
