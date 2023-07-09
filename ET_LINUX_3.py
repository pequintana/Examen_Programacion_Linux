import os
import time
import requests
import csv

os.system("clear") #Limpiar Pantalla
# Realizamos una solicitud HTTP, si el código de respuesta es 200 es porque la solicitud se realizó con éxito
lectura = requests.get("https://dummyjson.com/quotes")
if lectura.status_code == 200:
    data = lectura.json()
    cita = data['quotes']
    valores = [[quote['author'].ljust(20), quote['quote']] for quote in cita]

    # Abrimos el archivo endpoint.csv y guardamos los datos en el archivo CSV
    with open("endpoint.csv", mode='w', newline='\n') as file:
        escritor = csv.writer(file, delimiter='\t')
        escritor.writerow(["\tAUTOR\t", "\tCITA\t"])
        escritor.writerows(valores)

    print("___________________________________")
    print("¡¡¡¡Archivo CSV guardado exitosamente!!!\n")
    time.sleep(2)
else:
    print("___________________________________")
    print("¡¡¡Error al realizar la solicitud al endpoint!!! :(\n")
    time.sleep(2)

# Leemos los datos de endpoint.csv
def leer_datos_csv():
    with open("endpoint.csv", mode='r') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        next(lector)
        for row in lector:
            author = row[0]
            quote = row[1]
            print("Autor:", author)
            print("Cita:", quote)
            print()
            time.sleep(1)
        

# Creamos un menú para permitir al usuario visualizar el archivo .CSV o salir
while True:

    print("___________________________________")
    print("\tMENU")
    print("###################################")
    print("1. Mostrar datos de endpoint.csv")
    print("2. Salir")
    print("###################################")
    opcion = input("Ingrese una opción: ")
    print("___________________________________")
    time.sleep(1)

    if opcion == "1":
        leer_datos_csv()
    elif opcion == "2":
        print("Adiós. :)")
        time.sleep(1)
        break
    else:
        print("Opción inválida.\n")
        time.sleep(2)
        input("Presione Enter para continuar...")
#SEBASTIAN CANCINO  
#PEDRO QUINTANA
#EXAMEN 
