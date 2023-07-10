import csv
from collections import Counter
import re
import os
os.system("clear")
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

# Mostramos el ranking top ten de palabras más repetidas
print("\tRANKING TOP 10 PALABRAS")
print("##########################################")
for i, (palabra, count) in enumerate(top_ten, start=1):
    print(f"{i}. Palabra: {palabra}, Repeticiones: {count}")

# Obtener las 10 palabras más repetidas como nombres para un nuevo archivo de texto
nombres_archivo = [palabra for palabra, _ in top_ten]

# Crear el archivo de texto con los nombres de las palabras más repetidas
for nombre in nombres_archivo:
    with open(f"{nombre}.txt", "w") as file:
        file.write("Contenido del archivo")  # Aquí puedes agregar el contenido que desees
    # Establecer los permisos chmod 400 al archivo
    os.chmod(f"{nombre}.txt", 0o400)

print ("#########################################")
print("\tARCHIVOS")
print("##########################################")
os.system("ls -l")
print("#########################################")
#PEDRO QUINTANA 
# SEBASTIAN CANCINO
# EXAMEN
