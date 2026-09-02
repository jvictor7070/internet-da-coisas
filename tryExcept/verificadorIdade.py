import os
os.system("cls")

try:
    idade = int(input("Digite sua idade: "))
    
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

except ValueError:
    print("Erro: digite uma idade válida!")