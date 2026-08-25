import os
os.system('cls')

lista_numeros = []

while True:
    numero = int(input("Informe um número: "))
    
    if numero!=0:
        lista_numeros.append(numero)
    else:
        break
    
soma = sum(lista_numeros)
print(f"Lista de números: {lista_numeros}")
print(f"Soma dos números: {soma}")