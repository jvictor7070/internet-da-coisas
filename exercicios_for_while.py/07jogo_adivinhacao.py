import os
os.system("cls")

import random

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Chute um número de 1 a 20: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número sorteado é MAIOR!")
    elif palpite > numero_secreto:
        print("O número sorteado é MENOR!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
        break