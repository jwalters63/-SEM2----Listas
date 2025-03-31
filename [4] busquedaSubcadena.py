import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Escriba una cadena de texto para buscar una subcadena:")
print("[!] Nota del programador: Es mejor escribir una cadena larga para tener más subcadenas para buscar")
cadena = input("> ")

while True:
    print("\nEscriba la subcadena a buscar (o presione Enter para salir):")
    subcadena = input("> ")

    if subcadena == "":
        while True:
            print("¿Está seguro de que desea salir? (s/n)")
            confirmar = input("> ").lower()
            if confirmar == "s":
                print("Fin del programa, presione Enter para salir...")
                input()
                limpiar_terminal()
                exit()
            elif confirmar == "n":
                break
            else:
                print("Respuesta no válida. Por favor escriba 's' o 'n'.")
        continue

    if subcadena in cadena:
        print(f"La subcadena '{subcadena}' se encuentra en la cadena.")
    else:
        print(f"La subcadena '{subcadena}' no se encuentra en la cadena.")