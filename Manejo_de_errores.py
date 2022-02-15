
### Manejo de Errores ###

def divisores(num):
    try:
        if str(num)[0] == "-":
            raise ValueError("Solo se pueden numeros positivos")
        divisores = []

        num = int(num)
        i = 1
        for i in range(i, num + 1):
            if num % i == 0:
                divisores.append(i)
        return divisores
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
       num = input("Ingrese un número")
       print(divisores(num))
    except TypeError:
       print("Solo se pueden ingresar numeros")


if __name__ == "__main__":
    run()