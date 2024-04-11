#Crear un programa en el que el usuario introduzca una frase y el programa calcule el número de vocales de dicha frase.
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

frase = input("Ingrese una frase para calcular el numero de vocales: ")
vocales = 0

for i in frase:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocales+=1
print("La cantidad de vocales de su frase es: ",vocales)