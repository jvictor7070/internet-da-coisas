import os
os.system("cls")

try:
    saldo = float(input("Digite seu saldo: "))
    saque = float(input("Digite o valor do saque: "))

    if saque <= 0:
        print("Valor do saque deve ser maior que zero!")
    elif saque <= saldo:
        saldo_restante = saldo - saque
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: {saldo_restante:.0f}")
    else:
        print("Saldo insuficiente!")

except ValueError:
    print("Erro: digite apenas valores numéricos!")