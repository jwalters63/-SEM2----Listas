import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cadenas = []
contador = 0

print(f"Ingrese hasta 5 cadenas para dividir. [{5 - contador} restantes] (o presione Enter para salir...)")
while contador < 5:
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

print("Ingrese el delimitador (ej: ',' o ' '):")
delimitador = input("> ")

print("\nResultado:")
for i, c in enumerate(cadenas):
    partes = c.split(delimitador)
    print(f"Cadena {i+1}: {partes}")

input("\nPresione Enter para salir...")
limpiar_terminal()
