import customtkinter as ctk
import requests
ctk.set_appearance_mode('Light')

def converter_moeda():
    
    try:
        # FAz com que a caixa de resultado so apareça apos apertar o botão
        resultado.pack(pady=10)

        moeda_escolhida1= str(combobox1.get())
        moeda_escolhida2= str(combobox2.get())
        quantia = float(valor.get())

        sigla = moeda_escolhida1 [-4:-1]
        sigla2 = moeda_escolhida2 [-4:-1]

        
        url = f"https://economia.awesomeapi.com.br/last/{sigla}-{sigla2}"
        resposta = requests.get(url)
        dados = resposta.json()

        # 4. Extraímos apenas o preço atual ("bid") navegando pelo dicionário
        chave = f"{sigla}{sigla2}"
        preco = float(dados[chave]["bid"])
        valor_final = quantia * preco

        resultado.configure(text=f"{quantia:.2f} {sigla} = {valor_final:.2f} {sigla2}",text_color="black",
        )

    except ValueError:
        resultado.configure(
            text="Por favor, digite um número válido!", text_color="#D50000")


janela = ctk.CTk()
janela.geometry('650x500')
janela.resizable
janela.title('Conversor de Moedas')
janela.iconbitmap('moeda/coins_copy_finance_icon_125514.ico')

titulo = ctk.CTkLabel(janela,
                 text='Sistema de Conversão de Moedas',
                 text_color='#04080f',
                 font=('Arial',27,'bold')
                 )
titulo.pack(pady=20)

combobox1 = ctk.CTkComboBox(janela,
                        values = ["$ Real Brasileiro(BRL)","AED Dirham dos Emirados Árabes Unidos(AED)", "$ Dólar Americano(USD)", "$ Dólar Australiano(AUD)", "$ Dólar Canadense(CAD)", "$ Dólar Neozelandês(NZD)", 
               "€ Euro(EUR)", "CHF Franco Suíço(CHF)", "¥ Iene Japonês(JPY)", "£ Libra Esterlina(GBP)", "₺ Lira Turca(TRY)", 
               "₪ Novo Shekel Israelense(ILS)", "$ Peso Argentino(ARS)", "$ Peso Chileno(CLP)", "$ Peso Colombiano(COP)", "$ Peso Mexicano(MXN)", 
               "$ Peso Uruguaio(UYU)", "R Rand Sul-Africano(ZAR)", "SR Riyal Saudita(SAR)", "₹ Rúpia Indiana(INR)", "¥ Yuan Chinês(CNY)"],
               width=380,
               height=40,
               font=('Arial',12)
               
                        )
combobox1.pack(pady=10)

combobox2 = ctk.CTkComboBox(janela,
                        values = ["AED Dirham dos Emirados Árabes Unidos(AED)", "$ Dólar Americano(USD)", "$ Dólar Australiano(AUD)", "$ Dólar Canadense(CAD)", "$ Dólar Neozelandês(NZD)", 
               "€ Euro(EUR)", "CHF Franco Suíço(CHF)", "¥ Iene Japonês(JPY)", "£ Libra Esterlina(GBP)", "₺ Lira Turca(TRY)", 
               "₪ Novo Shekel Israelense(ILS)", "$ Peso Argentino(ARS)", "$ Peso Chileno(CLP)", "$ Peso Colombiano(COP)", "$ Peso Mexicano(MXN)", 
               "$ Peso Uruguaio(UYU)", "R Rand Sul-Africano(ZAR)","$ Real Brasileiro(BRL)","SR Riyal Saudita(SAR)", "₹ Rúpia Indiana(INR)", "¥ Yuan Chinês(CNY)"],
               width=380,
               height=40,
               font=('Arial',12)
               
                        )
combobox2.pack(pady=10)

valor = ctk.CTkEntry(janela,
                     placeholder_text='Digite o valor a ser convertido',
                     text_color='black',
                     width=380,
                     height=40,
                     )
valor.pack(pady=10)

butao = ctk.CTkButton(janela,
                      text='converter',
                      font = ('arial',15,'bold'),
                      fg_color="#0e6ba8",
                      hover_color="#005672",
                      width=190,
                      height=50,
                      command=converter_moeda
                      )
butao.pack(pady=15)

resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('Verdana',17),
                        corner_radius=10,
                        fg_color="#9EA0A0",
                        border_width=2,
                        border_color='black',
                        width=350,
                        height=120

                         )




janela.mainloop()