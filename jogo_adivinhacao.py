import os
import random

os.system("cls")

numero_sorteado = random.randint(1,20)

while True:
    try:
        numero = int(input("Chute um número de 1 a 20: "))

        if numero > numero_sorteado:
           print("O número secreto é menor. Tente de novo!\n")
        elif numero < numero_sorteado:
          print("O número secreto é maior. Tente de novo!\n")
        else:
            print("Parabéns, você acertou!")
            break
    except ValueError:
        print("Digite somente números inteiros")
