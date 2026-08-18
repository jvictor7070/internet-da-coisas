import os
os.system("cls")

n1 = int(input("Informe o n1: "))
n2 = int(input("Informe o n2: "))
operacao = input("Escolha a operação desejada(+, -, *, /)")

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
        
print(f"{n1}{operacao}{n2}={resultado}")
       
        
        