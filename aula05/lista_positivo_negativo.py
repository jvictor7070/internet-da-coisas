import os

os.system("cls")

lista_numero = []
positivos = []
negativos = []

for i in range(10):
    numero = int(input(f"informe o {i+1}º número: "))
    lista_numero.append(numero)

for numero in lista_numero:
    if numero >= 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print(f"Quantidade de negativos: {len(negativos)}")
print(f"Quantidade de positivos: {len(positivos)}")
print(f"Números negativos: {negativos}")
print(f"Soma dos positivos: {sum(positivos)}")