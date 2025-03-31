import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cadenas = []
contador = 0

print(f"Ingrese hasta 5 cadenas para contar un carácter específico. [{5 - contador} restantes] (o presione Enter para salir...)")
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

while True:
    print("\nIngrese el carácter que desea contar:")
    caracter = input("> ")
    if len(caracter) == 1:
        break
    else:
        print("Ingrese solo un carácter.")

print(f"\nConteo del carácter '{caracter}':")
for i, c in enumerate(cadenas):
    cantidad = c.count(caracter)
    print(f"Cadena {i+1}: '{c}' → {cantidad} vez/veces")

input("\nPresione Enter para salir...")
limpiar_terminal()
