import os
import time
import shutil
import re


# Función para validar el nombre de usuario
def validar_nombre_usuario(nombre):
    if len(nombre) > 10 or not re.match("^[a-zA-Z]*$", nombre):
        print("¡¡¡¡¡¡¡¡¡¡¡CONSIDERE QUE EL NOMBRE DE USUARIO DEBE TENER UN MAX. DE 10 CARACTERES Y TENER SOLO LETRAS!!!!!!!")
        time.sleep(5)
        return False
    return True


# Función para validar el nombre de archivo
def validar_nombre_archivo(nombre):
    nombre_sin_extension = os.path.splitext(nombre)[0]
    if len(nombre_sin_extension) > 10 or not re.match("^[a-zA-Z]*$", nombre_sin_extension) or not nombre.endswith(('.txt', '.pdf', '.docx', '.xlsx')):
        print("¡¡¡¡¡¡¡CONSIDERE QUE EL NOMBRE DE ARCHIVO DEBE TENER UN MAX. DE 10 CARACTERES(sin la extension), TENER SOLO LETRAS Y TERMINAR CON ALGUNA DE ESTAS EXTENSIONES: .txt, .pdf, .docx, .xlsx.")
        time.sleep(5)
        return False
    return True


while True:
    os.system("clear")
    print("###############################")
    print(" MENU ")
    print("###############################")
    print("a.-Administracion de usuarios")
    print("b.-Administracion de archivos")
    print("c.-Salir")
    print("###############################")
    opcion = input("Ingrese opción: ")
    print("###############################")


    if opcion == "c":
        break


    elif opcion == "b":
        while True:
            os.system("clear")
            print("##############################")
            print("MENU ADMIN. ARCHIVOS")
            print("##############################")
            print("a.-Crear archivo")
            print("b.-Eliminar archivo")
            print("c.-Volver")
            print("###############################")
            opcion_archivo = input("Ingrese opción: ")
            print("###############################")


            if opcion_archivo == "c":
                break


            if opcion_archivo == "a":
                nombre_archivo = input("Ingrese el nombre del archivo a crear: ")
                print("###############################")
                if validar_nombre_archivo(nombre_archivo):
                    if not os.path.exists(nombre_archivo):
                        with open(nombre_archivo, "w"):
                            pass
                        print(f"Se ha creado el archivo {nombre_archivo}")
                        print("#########ARCHIVOS######################")
                        os.system("ls -l")
                        time.sleep(5)
                    else:
                        print(f"El archivo {nombre_archivo} ya existe")
                        print("#########ARCHIVOS######################")
                        os.system("ls -l")
                        time.sleep(5)
                continue


            if opcion_archivo == "b":
                nombre_archivo = input("Ingrese el nombre del archivo a eliminar: ")
                print("###############################")
                if validar_nombre_archivo(nombre_archivo):
                    if os.path.exists(nombre_archivo):
                        os.remove(nombre_archivo)
                        print(f"Se ha eliminado el archivo {nombre_archivo}")
                        print("#########ARCHIVOS######################")
                        os.system("ls -l")
                        time.sleep(5)
                    else:
                        print(f"El archivo {nombre_archivo} no existe")
                        print("#########ARCHIVOS######################")
                        os.system("ls -l")
                        time.sleep(5)
                continue


            else:
                print("Opción inválida")
                time.sleep(5)
                continue


    elif opcion == "a":
        while True:
            os.system("clear")
            print("###############################")
            print(" MENU ADMIN. USUARIOS ")
            print("###############################")
            print("a.-Crear usuario")
            print("b.-Eliminar usuario")
            print("c.-Volver")
            print("###############################")
            opcion_u = input("Ingrese opción: ")
            print("###############################")


            if opcion_u == "c":
                break


            if opcion_u == "a":
                usuario = input("Ingrese nombre de usuario que desea crear: ")
                print("###############################")
                if validar_nombre_usuario(usuario):
                    resultado = os.system(f"id -u {usuario} >/dev/null 2>&1")
                    if resultado == 0:
                        print(f"El usuario {usuario} ya existe")
                        print("############USUARIOS###################")
                        os.system("cat /etc/passwd")
                        time.sleep(5)
                    else:
                        resultado = os.system(f"useradd {usuario}")
                        if resultado == 0:
                            print(f"El usuario {usuario} se ha creado")
                            print("############USUARIOS###################")
                            os.system("cat /etc/passwd")
                            time.sleep(5)
                        else:
                            print(f"No se pudo crear el usuario {usuario}")
                            time.sleep(5)
                continue


            if opcion_u == "b":
                usuario = input("Ingrese nombre de usuario que desea eliminar: ")
                print("###############################")
                if validar_nombre_usuario(usuario):
                    resultado = os.system(f"id -u {usuario} >/dev/null 2>&1")
                    if resultado != 0:
                        print(f"El usuario {usuario} no existe")
                        print("#############USUARIOS##################")
                        os.system("cat /etc/passwd")
                        time.sleep(5)
                    else:
                        resultado = os.system(f"userdel {usuario}")
                        if resultado == 0:
                            print(f"El usuario {usuario} se ha eliminado")
                            print("#############USUARIOS##################")
                            os.system("cat /etc/passwd")
                            time.sleep(5)
                        else:
                            print(f"No se pudo eliminar el usuario {usuario}")
                            time.sleep(5)
                continue


            else:
                print("Opción inválida")
                time.sleep(5)
                continue


    else:
        print("Opción inválida")
        time.sleep(5)
        continue
#PEDRO QUINTANA 
# SEBASTIAN CANCINO
# EXAMEN
