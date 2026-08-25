import os
os.system("cls")

temperatura = []

for i in range(5):
    s_temperatura = float(input(f"Informe a {i+1}ª temperatura: "))
    temperatura.append(s_temperatura)
    
media = sum(temperatura) / len(temperatura)
maior = max(temperatura)
menor = min(temperatura)
print(f"Maior (temperatura): {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média temperatura: {media}°C")