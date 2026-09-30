import customtkinter as ctk

ctk.set_appearance_mode("dark")

def calcular_media():
    # O try precisa envolver a leitura/conversao dos dados para capturar o erro
    try:
        n1 = float(nota1.get().replace(",", "."))
        n2 = float(nota2.get().replace(",", "."))
        n3 = float(nota3.get().replace(",", "."))
        
        media = (n1 + n2 + n3) / 3
        
        # Define a situação com base na média
        if media >= 5.0:
            resultado = "Aprovado"
        else:
            resultado = "Recuperação"  # Ajustado conforme enunciado
            
        # Exibe a média e o resultado na interface
        label_resultado.configure(
            text=f"Sua média é: {media:.1f}\nResultado: {resultado}",
            text_color="#FFFFFF"
        )
        
    except ValueError:
        # Exibe a mensagem de erro diretamente na tela para o usuário
        label_resultado.configure(
            text="Erro: Preencha todas as notas apenas com números!",
            text_color="#FF5555"
        )

# Configuração da Janela
janela = ctk.CTk()
janela.geometry('600x550')  # Aumentado para 550 para acomodar melhor os elementos
janela.title('Sistema Escolar - 2026')

# Opcional: try/except no ícone evita erro caso a imagem não exista na pasta
try:
    janela.iconbitmap('aula7/university_cap_icon-icons.com_66109.ico')
except:
    pass

# Corpo da Janela ------------------

titulo = ctk.CTkLabel(
    janela,
    text="Sistema Escolar",
    text_color="#FFFFFF",
    font=('Verdana', 35, 'bold')
)
titulo.pack(pady=20)

nota1 = ctk.CTkEntry(
    janela,
    width=400,
    height=50,
    border_color="#929292",
    placeholder_text="Digite a nota da 1ª unidade:"
)
nota1.pack(pady=10)

nota2 = ctk.CTkEntry(
    janela,
    width=400,
    height=50,
    border_color="#929292",
    placeholder_text="Digite a nota da 2ª unidade:"
)
nota2.pack(pady=10)

nota3 = ctk.CTkEntry(
    janela,
    width=400,
    height=50,
    border_color="#929292",
    placeholder_text="Digite a nota da 3ª unidade:"
)
nota3.pack(pady=10)

# Simplificado sem 'lambda', pois a função não recebe parâmetros
botao = ctk.CTkButton(
    janela,
    width=400,
    height=50,
    text="Calcular Média",
    command=calcular_media
)
botao.pack(pady=20)

label_resultado = ctk.CTkLabel(
    janela,
    text="Média: --",
    font=('Verdana', 14)
)
label_resultado.pack(pady=10)

janela.mainloop()