#Cada cliente que va al banco Galicia, indica su número de documento y aguarda a ser atendido. Cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido (DNI) y quién fue el último.
#Emiliano Fernandez
#Aplicaciones informaticas
#emilianofernandezesp@gmail.com

cant = 0
dni = 0

while(dni != -1):
    dni= int(input("ingrese su numero de documento: "))
    cant += 1
    if cant == 1:
        primerDNI= dni
    if dni != -1:
        ultimoDNI = dni
print(f"El primer dni fue {primerDNI} y el ultimo fue {ultimoDNI}")