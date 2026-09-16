import customtkinter as ctk 
ctk.set_appearance_mode("dark")

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
                     cursor='spider')

botao.pack(pady=35)







janela.mainloop()