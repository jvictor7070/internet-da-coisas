import os
os.system("cls")

lista_notas = []

try:
    for i in range(3):
        notas = float(input(f"Informe a {i+1}º nota: "))
        lista_notas.append(notas)
        soma = sum(lista_notas)
        media = soma / 3

    if media >= 7:
        print(f"Sua média é: {media:.2f}, Aprovado")
    elif media >=5:
        print(f"Sua média é: {media:.2f},Recuperação")
    else:
        print(f"Sua média é: {media:.2f},Reprovado")
except ValueError:
    print("Erro: digite somente números!")
    
