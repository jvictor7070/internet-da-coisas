import os
os.system("cls")

temperatura = 29

if temperatura < 15:
    print(f"Temperatura = {temperatura}° graus")
    print("O clima está frio")
elif temperatura <= 25:
    print(f"Temperatura = {temperatura}° graus")
    print("O clima Está agradavel")
else:
    print(f"Temperatura = {temperatura}° graus")
    print("O clima Está quente")
