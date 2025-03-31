import os

cadenas = []
longitudes = []
contador = 0

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while contador < 5:
    print(f"Escriba hasta 5 cadenas de texto para determinar su longitud [{5 - contador} restantes // Cadena vacía para terminar]:")
    cadena = input("> ")
    
    if cadena == "":
        while True:
            print("¿Está seguro de que desea terminar? (s/n)")
            respuesta = input("> ").lower()
            if respuesta == "s":
                print("Operación cancelada")
                print("Fin del programa, presione Enter para salir...")
                input()
                limpiar_terminal()
                exit()
            elif respuesta == "n":
                break
            else:
                print("Respuesta no válida, por favor escriba 's' o 'n'.")
        continue

    cadenas.append(cadena)
    contador += 1

for c in cadenas:
    longitudes.append(len(c))

print("\nResultados:")
for i in range(len(cadenas)):
    print(f"Cadena {i+1}: '{cadenas[i]}' → longitud: {longitudes[i]} caracteres")

print("\nFin del programa, presione Enter para salir...")
input()
limpiar_terminal()