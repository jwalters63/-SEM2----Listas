import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cadenas = []
contador = 0

print(f"Ingrese hasta 5 cadenas (las vacías serán eliminadas). [{5 - contador} restantes] (o presione Enter para salir...)")
print("[!] Nota del programador: Si desea salir, presione Enter sin ingresar nada. Si quiere ingresar una cadena vacía, escriba un espacio y presione Enter.")
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

cadenas_filtradas = [c for c in cadenas if c.strip() != ""]

print("\nLista sin cadenas vacías:")
for i, c in enumerate(cadenas_filtradas):
    print(f"Cadena {i+1}: {c}")

input("\nPresione Enter para salir...")
limpiar_terminal()
