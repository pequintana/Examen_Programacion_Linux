import csv
from collections import Counter
import re
import os
import requests

os.system("clear")
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
palabras_excluidas = [
    'the', 'a', 'an', 'and', 'or', 'but', 'for', 'with', 'in', 'on', 'at', 'to', 'from', 't', 've'
]  # Palabras que excluiremos ya que son conectores o artículos

contador = Counter()  # Contador de palabras

with open("endpoint.csv", mode='r') as file:
    lector = csv.reader(file, delimiter='\t')
    next(lector)

    for row in lector:
        cita = row[1]
        palabras = re.findall(r"\b(?:\w+(?:'\w+)?|\w+)\b", cita)  # Extraemos palabras completas con apóstrofes

        # Incrementamos el contador de palabras
        for palabra in palabras:
            if palabra.lower() not in palabras_excluidas:
                contador[palabra.lower()] += 1

# Obtenemos las diez palabras más repetidas
top_ten = contador.most_common(10)

# Crear el nombre del archivo con todas las palabras del top separadas por guiones bajos
nombre_archivo = "_".join(palabra for palabra, _ in top_ten)

# Agregar la extensión ".txt" al nombre del archivo
nombre_archivo += ".txt"

# Crear el archivo de texto con el nombre formado por todas las palabras del top
with open(nombre_archivo, "w") as file:
    file.write("Contenido del archivo")  # Aquí puedes agregar el contenido que desees

# Establecer los permisos 400 al archivo
os.chmod(nombre_archivo, 0o400)

print("\tRANKING TOP 10 PALABRAS")
print("##########################################")
for i, (palabra, count) in enumerate(top_ten, start=1):
    print(f"{i}. Palabra: {palabra}, Repeticiones: {count}")

print("##########################################")
print("Archivo creado exitosamente \tPermisos: 400.")
print("##########################################")
print("\tARCHIVOS")
os.system("ls -l")
#SEBASTIAN CANCINO
#PEDRO QUINTANA
#EXAMEN
