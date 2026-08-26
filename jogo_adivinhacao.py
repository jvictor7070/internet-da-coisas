import os
import time
import random

os.system("cls")

numero_sorteado = random.randint(1,100)
tentativas = 0

while True:
    try:
        numero = int(input("Chute um número de 1 a 100: "))
        tentativas += 1

        if numero > numero_sorteado:
           print("O número secreto é menor. Tente de novo!\n")
           time.sleep(1)
           os.system("cls")
        elif numero < numero_sorteado:
          print("O número secreto é maior. Tente de novo!\n")
          time.sleep(1)
          os.system("cls")
        else:
            print("Parabéns, você acertou!")
            print(f"Você acertou em {tentativas} tentativas")
            break
    except ValueError:
        print("Digite somente números inteiros")
