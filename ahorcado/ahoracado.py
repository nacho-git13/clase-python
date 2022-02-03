import random
import os

def palabra_random():
    with open("./ahorcado/palabras.txt", "r", encoding="utf-8") as f:
            espacios = list(enumerate(f))
    num = random.randrange(1, len(espacios))
    palabra_indice = [espacios[num][0], espacios[num][1].strip("\n")]
    return palabra_indice

def juego():
    try:
        espacios = []
        adivinar = list(palabra_random()[1])
        for letra in adivinar:
            espacios.append("_ ")
        mostrando = "".join(espacios)
        while adivinar != espacios:
            letra = input("Bienvenido al Juego del Ahorcado\n" + mostrando + "\nIngresa una letra: ")
            if letra in adivinar:
                for key, value in enumerate(adivinar):
                    if value == letra:
                        espacios[key] = letra
                        mostrando = "".join(espacios).strip(" ")
            os.system("cls")
        espacios = "".join(espacios)
        print(f'Felicidades! Ganaste. La palabra era {espacios}')

        denuevo = int(input("Quieres jugar de nuevo? \n1. Si\n2. No\n: "))
        if denuevo == 1:
            run()
        else:
            print("Hasta la Próxima")
    except ValueError:
        print("Solo se pueden letras")


def run():  
    juego()

if __name__ == "__main__":
    run()

