import subprocess

def check_ubuntu_updates():
    # Ejecutar el comando 'apt update' para actualizar los repositorios
    subprocess.run(['sudo', 'apt', 'update'])

    # Ejecutar el comando 'apt list --upgradable' para obtener las actualizaciones disponibles
    resultado = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
    salida = resultado.stdout.strip()

    if salida:
        print("¡Existen actualizaciones disponibles!")
        # Generar el prompt para que el usuario decida si instalar o no las actualizaciones
        choice = input("¿Desea instalar las actualizaciones? (y/n): ")
        if choice.lower() == 'y':
            # Ejecutar el comando 'sudo apt upgrade' para instalar las actualizaciones
            subprocess.run(['sudo', 'apt', 'upgrade'])
            print("Las actualizaciones se han instalado correctamente.")
        else:
            print("No se han instalado las actualizaciones.")
    else:
        print("No hay actualizaciones disponibles.")

# Llamar a la función para verificar las actualizaciones en Ubuntu
check_ubuntu_updates()


#SEBASTIAN CANCINO
#PEDRO QUINTANA
#ET LINUX 3
