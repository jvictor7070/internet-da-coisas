import os
os.system("cls")

lista_numeros = []
for i in range(6):
    numero = int(input(f"Informe o {i+1}º número:"))
    lista_numeros.append(numero)

soma = sum(lista_numeros)
maximo = max(lista_numeros)
minimo = min(lista_numeros)
ordem = sorted(lista_numeros)

print(f"Soma dos números: {soma}")
print(f"Maior dos números: {maximo}")
print(f"Menor dos números: {minimo}")
print(f"Números em ordem Crescente: {ordem}")