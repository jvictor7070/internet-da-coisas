import os
os.system("cls")

lista_produtos = []

for i in range(5):
    produtos = input(f"Informe o {i+1}º produto: ")
    lista_produtos.append(produtos)

print(f"\nLista de produtos: {lista_produtos}")