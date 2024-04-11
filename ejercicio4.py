#Leer 10 números enteros e imprimir el promedio, el mayor y menor ingresado.
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

menor = 0
mayor = 0
suma = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    suma += num
    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num

promedio = suma / 10

print(f"El promedio es {promedio}, el mayor numero es {mayor}, el menor numero es {menor}")