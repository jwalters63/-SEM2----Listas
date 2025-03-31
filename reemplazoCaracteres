import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

cadenas = []
contador = 0

print("Ingrese hasta 5 cadenas para reemplazar un carácter por otro.  (o presione Enter para salir...)")
while contador < 5:
    cadena = input(f"[{5 - contador} restantes]: ")
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
    print("\nIngrese el carácter a reemplazar:")
    caracter_antiguo = input("> ")
    if len(caracter_antiguo) == 1:
        break
    else:
        print("Ingrese solo un carácter.")

while True:
    print("Ingrese el nuevo carácter:")
    caracter_nuevo = input("> ")
    if len(caracter_nuevo) == 1:
        break
    else:
        print("Ingrese solo un carácter.")

for i in range(len(cadenas)):
    cadenas[i] = cadenas[i].replace(caracter_antiguo, caracter_nuevo)

print("\nResultado:")
for i, c in enumerate(cadenas):
    print(f"Cadena {i+1}: {c}")

input("\nPresione Enter para salir...")
limpiar_terminal()
