import os
cadenas = []
contador = 0

def limpiar_terminal():
    os.system('cls')

while contador < 5:
    print(f"Escriba hasta 5 cadenas de texto para concatenar [{5 - contador} restantes // Cadena vacía para terminar]:")
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

resultado = " ".join(cadenas)
print(f"La cadena concatenada es: {resultado}")
print("Fin del programa, presione Enter tecla para salir...")
input()
limpiar_terminal()