import os
os.system("cls")

idade = int(input("Informe sua idade: "))

if idade >0 and idade <=12:
    print(f"Sua idade é {idade}, Criança")
elif idade >= 13 and idade <18:
    print(f"Sua idade é {idade}, Adolescente")
elif idade >= 18 and idade <= 59:
    print(f"Sua idade é {idade}, Adulto")
else:
    print(f"Sua idade é {idade}, idoso")
    