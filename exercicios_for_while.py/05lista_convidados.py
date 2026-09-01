import os
os.system("cls")

nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    
    if nome.lower() == 'fim':
        break
        
    nomes.append(nome)

nomes.sort()

print("\nNomes em ordem alfabética:", nomes)
print("Quantidade total de nomes:", len(nomes))