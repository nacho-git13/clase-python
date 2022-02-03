import random

def palabra_random():
    palabras = []
    with open("./ahorcado/palabras.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append(enumerate(line))
    num = random.randrange(1, len(palabras))
    palabra_random = palabras[num][1]
    indice = palabras[num][0]
    palabra_indice = [indice, palabra_random]
    return palabra_indice
    
def inicio():
    espacios = []
    palabra = list(palabra_random()[1])
    indice = palabra_random()[0]
    for letra in palabra:
        if letra == "\n":
            break
        espacios.append("-")
    espacios = "".join(espacios)
    letra = input("El Juego del Ahorcado \n" + espacios + "\nIngrese una letra: ")
    juego(letra, list(espacios), palabra)

def juego(letra, espacios, palabra):
    try:
        if len(letra) > 1:
            raise ValueError("No se puede ingresar mas de una letra")

        i = -1
        print(espacios)
        desbloqueo = espacios
        for elemento in palabra:
            if letra == elemento:
                desbloqueo[i] = letra
            else:
                desbloqueo[i] = "-"
            print(i)
            i = i+1
        while desbloqueo != palabra:
            print(espacios)
            letrica = input("El Juego del Ahorcado \n" + "".join(desbloqueo) + "\nIngrese una letra: ")
            juego(letrica, desbloqueo, palabra)
        else:
            print("Felicidades Ganaste!")
    except ValueError as ve:
        print(ve)

def run():
    inicio()

if __name__ == "__main__":
    run()