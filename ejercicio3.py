#Mostrar las tablas de multiplicar (entre 1 y 10) del número 3. ¿Qué cambios harías en el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

num = int(input("Ingrese el numero para saber la tabla de multiplicar: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")