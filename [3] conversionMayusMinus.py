import os
cadenas = []
contador = 0

def limpiar_terminal():
    os.system('cls')

while contador < 5:
    print(f"Escriba hasta 5 cadenas de texto para pasar a Mayúscula (par) o Minúscula (impar) [{5 - contador} restantes // Cadena vacía para terminar]:")
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

print("\nResultados:")
for i in range(len(cadenas)):
    longitud = len(cadenas[i])
    if longitud % 2 == 0:
        transformada = cadenas[i].upper()
    else:
        transformada = cadenas[i].lower()
    print(f"Cadena {i+1}: '{cadenas[i]}' → longitud: {longitud} → resultado: {transformada}")

print("\nFin del programa, presione Enter para salir...")
input()
limpiar_terminal()