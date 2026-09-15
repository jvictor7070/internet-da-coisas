import customtkinter as ctk
ctk.set_appearance_mode("#F3B600")

# janela

janela = ctk.CTk()
janela.geometry('500x500')
janela.title('Sistema de acesso - 2026')
janela.iconbitmap('aula7/security-protection-protect-key-password-login_108554.ico')
# ------------------------------------------------------------------------------------------------------------

# corpo da janela---------

titulo = ctk.CTkLabel(janela,
                      text="Sistema de Login",
                      text_color='#157145',
                      font=('Dalton',50))

titulo.pack()
# -------------------------------------------------------------------------------------------------------------


login = ctk.CTkEntry(janela,
                     width=400,
                     height=50,
                     border_color="#F19A3E",
                     placeholder_text="Digite seu login:")

login.pack(pady=20)
# ---------------------------------------------------------------------------------------------------------------


senha = ctk.CTkEntry(janela,
                     width=400,
                     height=50,
                     border_color='#F19A3E',
                     placeholder_text="Digite sua senha:",
                     show = "*")

senha.pack()
# ------------------------------------------------------------------------------------------------------------

botao = ctk.CTkButton(janela,
                      width=400,
                      height=50,
                      text="Acessar",
                      text_color='black',
                      fg_color = ('#49306B'),
                      cursor = 'spider')

botao.pack(pady=35)






janela.mainloop()
