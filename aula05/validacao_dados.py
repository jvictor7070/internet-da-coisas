import os
os.system("cls")

while True:
    senha = input("Digite sua senha de 4 dígitos numéricos: ")
    
    if len(senha) == 4 and senha.isdigit():
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha Inválida")