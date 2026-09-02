import os
os.system("cls")

try:
    numero = int(input("Informe um número: "))
    for i in range(1,11):
        resultado = numero * i

        print(f"{numero}X{i}={resultado}")
except ValueError:
    print("Digite somente números inteiros")

