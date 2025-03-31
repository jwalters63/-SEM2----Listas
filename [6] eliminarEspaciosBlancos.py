import os

def limpiar_terminal():
    os.system('cls')

cadenas = []
contador = 0

print("Ingrese hasta 5 cadenas para eliminar espacios al inicio y final.")
while contador < 5:
    cadena = input(f"[{5 - contador} restantes] (o presione Enter para salir...): ")
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

for i in range(len(cadenas)):
    cadenas[i] = cadenas[i].strip()

print("\nResultado:")
for i, c in enumerate(cadenas):
    print(f"Cadena {i+1}: '{c}'")

input("\nPresione Enter para salir...")
limpiar_terminal()
