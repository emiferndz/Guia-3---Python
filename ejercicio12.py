#Crear un programa en el que el usuario introduzca un número entero y el programa genere una frase con las palabras correspondientes a cada cifra. Por ejemplo, 547 devolvería “cinco cuatro siete”.
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

numero = (input("Ingrese un numero entero para generarle una frase: "))
frase = ""

for i in numero:
    if i == "0":
        frase += "cero "
    elif i == "1":
        frase += "uno "
    elif i == "2":
        frase += "dos "
    elif i == "3":
        frase += "tres "
    elif i == "4":
        frase += "cuatro "
    elif i == "5":
        frase += "cinco "
    elif i == "6":
        frase += "seis "
    elif i == "7":
        frase += "siete "
    elif i == "8":
        frase += "ocho "
    elif i == "9":
        frase += "nueve "
print("Su numero en frase es: ",frase)