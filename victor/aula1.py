import os
os.system("cls")

uni1 = float(input("Informe a sua nota do 1ª unidade: "))
uni2= float(input("Informe a sua nota do 2ª unidade: "))
uni3 = float(input("Informe a sua nota do 3ª unidade: "))

soma_notas = uni1 + uni2 + uni3
media = soma_notas / 3

if media >= 5:
    print(f"Media:{media:.1f}, Aluno Aprovado")
else:
    print(f"Media:{media:.1f}, Aluno reprovado!")