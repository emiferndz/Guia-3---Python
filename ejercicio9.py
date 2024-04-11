#Una familia va de vacaciones en auto desde Buenos Aires hasta Córdoba. La familia consta de los dos padres y de un hijo y de una niña. Durante el trayecto los niños preguntan incesantes: ¡¿Ya llegamos?! … a lo que los padres responden ¡No! Crear un programa que recree tal situación y que la consulta formulada por los niños se detenga cuando la respuesta sea ¡¡Sí!!
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

respuestapadres = "no"

print("Papá, ¡¿Ya llegamos?!")

while(respuestapadres != "Si"):
    preguntaniños = input("padres: ")
    if preguntaniños == "No":
        print("niños: ¡¿Ya llegamos?!")
    elif preguntaniños == "Si":
        print("programa finalizados")
        break