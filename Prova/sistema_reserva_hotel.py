import os
os.system("cls")
import customtkinter as ctk
ctk.set_appearance_mode('dark')

def hospedagem():
    
    try:
        nome_hospede = str(nome.get())
        quant_diaria = int(diarias.get())
        valor = float(valor_diaria.get())
        valor_total = quant_diaria * valor
        
        if (quant_diaria >=5):
            desconto = valor_total * 0.10
            valor_total = valor_total - desconto
            resultado.configure(text=f'Olá, {nome_hospede}\nHospedagem: R${valor:.2f} reais\nDesconto: R${desconto:.2f} reais\nTotal a Pagar: R${valor_total:.2f} reais',text_color = 'green')
        else:
            resultado.configure(text=f'Olá, {nome_hospede}\nValor da Hospedagem: R${valor:.2f}\nQuantidade de Dias: {quant_diaria}\nTotal a Pagar: R${valor_total:.2f}')
    except ValueError:
        resultado.configure(text='Dados inválidos, digite somentes dados válidos!',text_color='red')
            
    

janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False,False)
janela.title('Reserva de Hotel')
janela.iconbitmap('Prova/1497618992-6_85114.ico')

titulo = ctk.CTkLabel(janela,
                 text='Sistema de Reserva de Hotel',
                 text_color='#44FFD2',
                 font=('Arial',25,'bold')
                 )
titulo.pack(pady=10)


nome = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#87F6FF',
                    placeholder_text='Digite o nome do hóspede')
nome.pack(pady=10)

diarias= ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#87F6FF',
                    placeholder_text='Digite a quantidade de dias')
diarias.pack(pady=10)

valor_diaria = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#87F6FF',
                    placeholder_text='Digite o valor da diária')
valor_diaria.pack(pady=10)

butao = ctk.CTkButton(janela,
                      text='Calcular Hospedagem',
                      width=400,
                      height=40,
                      fg_color="#023DC9",
                      text_color='white',
                      font=('Arial',20),
                      hover_color="#2D6CFF",
                      command=hospedagem
                      
                      )
butao.pack(pady=10)

resultado=ctk.CTkLabel(janela,
                        text='',
                        font=('Verdana',17),
                        corner_radius=10,
                        width=350,
                        height=120)

resultado.pack(pady=10)



janela.mainloop()