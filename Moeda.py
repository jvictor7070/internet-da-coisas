import requests # Importamos a biblioteca que você acabou de instalar
import questionary
#import customtkinter a
#from tkinter import ttk
import os
os.system("cls")

class Moeda:
    def __init__(self,escolha_moeda,valor_moeda_estrangeira):
        self.escolha_moeda = escolha_moeda
        self.valor_moeda_estrangeira = valor_moeda_estrangeira

    def conversao_moeda(self,preco):
        self.preco=preco
        self.resultado = self.valor_moeda_estrangeira * preco
        print(f"R${self.valor_moeda_estrangeira} em reais, equivale a: R${self.resultado:.2f} reais")


moeda_escolhida = questionary.select(
    "Escolha a moeda que deseja converter em valor_moeda_estrangeira: ",
    choices = ["AED Dirham dos Emirados Árabes Unidos(AED)", "$ Dólar Americano(USD)", "$ Dólar Australiano(AUD)", "$ Dólar Canadense(CAD)", "$ Dólar Neozelandês(NZD)", 
               "€ Euro(EUR)", "CHF Franco Suíço(CHF)", "¥ Iene Japonês(JPY)", "£ Libra Esterlina(GBP)", "₺ Lira Turca(TRY)", 
               "₪ Novo Shekel Israelense(ILS)", "$ Peso Argentino(ARS)", "$ Peso Chileno(CLP)", "$ Peso Colombiano(COP)", "$ Peso Mexicano(MXN)", 
               "$ Peso Uruguaio(UYU)", "R Rand Sul-Africano(ZAR)", "SR Riyal Saudita(SAR)", "₹ Rúpia Indiana(INR)", "¥ Yuan Chinês(CNY)"
]
).ask()
if not moeda_escolhida:
    print("Conversão encerrada")
sigla = moeda_escolhida[-4:-1]

# 1. Definimos a URL da API para Dólar (USD) para valor_moeda_estrangeira (BRL)
url = f"https://economia.awesomeapi.com.br/last/{sigla}-BRL"

# 2. O robô acessa o site
resposta = requests.get(url)

# 3. Transformamos a resposta em um Dicionário Python (JSON)
dados = resposta.json()

# 4. Extraímos apenas o preço atual ("bid") navegando pelo dicionário
chave = f"{sigla}BRL"
preco1 = float(dados[chave]["bid"])
valor_valor_moeda_estrangeira = float(input("Valor a ser convertido: "))
moeda_convertida = Moeda(moeda_escolhida,valor_valor_moeda_estrangeira)
moeda_convertida.conversao_moeda(preco1)