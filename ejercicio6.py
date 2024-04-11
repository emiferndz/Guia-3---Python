#Crear un programa que permita ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos números en total se ingresaron.
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

suma = 0
cantidad = 0

while (suma < 100 ):
    numero = int(input("Ingrese numeros pares para sumarlos, hasta que lleguen a 100: "))
    cantidad += 1
    if numero % 2 == 0:
        suma += numero
    else:
        print("ingrese un numero que sea par")
print ("La cantidad de numeros que se ingresaron fueron: ",cantidad)