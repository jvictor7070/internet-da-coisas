import customtkinter as ctk 
ctk.set_appearance_mode("dark")

# Funcoes
def calcular():
    dist=float (distancia.get())
    preco=float (preco_combustivel.get())
    cons=float(consumo.get())
    
    formula = (dist / cons) * preco
    
    resultado.configure(text=f'O valor da viagem é de R${formula:.2f} reais')

janela = ctk.CTk()
janela.geometry('500x400')
janela.title('Calculadora de Viagem')
janela.iconbitmap('calculadoraViagem/car_icon-icons.com_54409.ico')


titulo = ctk.CTkLabel(janela,
                             text='APP DE VIAGEM',
                             text_color ="#FF3956",
                             font=('Verdana',40))

titulo.pack(pady=20)



distancia = ctk.CTkEntry(janela,
                         width=400,
                         height=50,
                        border_color="#F40000",
                        placeholder_text="Digite a distância de viagem em KM:")

distancia.pack()



consumo = ctk.CTkEntry(janela,
                         width=400,
                         height=50,
                        border_color="#F40000",
                        placeholder_text="Digite o consumo do seu veículo:")

consumo.pack(pady=20)



preco_combustivel = ctk.CTkEntry(janela,
                         width=400,
                         height=50,
                        border_color="#F40000",
                        placeholder_text="Digite o preço atual do combustível:")

preco_combustivel.pack()

botao =ctk.CTkButton(janela,
                     width=170,
                     height=40,
                     text='calcular gastos',
                     text_color="#FFFFFF",
                     fg_color="#B85656",
                     border_color="#A523BE",
                     cursor='hand2',
                     font=('times new Roman',15,'bold'),
                     command=calcular)

botao.pack(pady=10)


resultado =ctk.CTkLabel(janela,
                        text='',
                        text_color='#FFFFFF',
                        font=('Verdana',20))

resultado.pack(pady=10)





janela.mainloop()