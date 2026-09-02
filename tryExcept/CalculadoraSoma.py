import os
os.system("cls")

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    
    resultado = n1 + n2
    print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: digite apenas números!")