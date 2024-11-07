# Este programa hace que dos numeros enteros se "multipliquen" sin usar el signo de multiplicacion


def multi_v1():
    print("***************Programa Para Multiplicar Números Enteros****************\n")
    while True:
        try:
            numero_1 = int(input("Ingresa el primer número: "))
            break
        except ValueError:
            print("\nPor favor, ingrese un número entero.\n")

    while True:
        try:
            numero_2 = int(input("\nIngresa el segundo número: "))
            break
        except ValueError:
            print("\nPor favor, ingrese un número entero.")

    resultado = 0

    for _ in range(numero_2):
        resultado += numero_1

    print(f"La Multiplicacion de {numero_1} por {numero_2} es igual a {resultado}")


multi_v1()
