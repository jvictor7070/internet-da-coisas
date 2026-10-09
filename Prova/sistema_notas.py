import tkinter as tk
from tkinter import messagebox

def calcular_resultado():

    try:
        nome = entry_nome.get().strip()
        
        nota1 = float(entry_nota1.get().replace(',', '.'))
        nota2 = float(entry_nota2.get().replace(',', '.'))

       
       
        media = (nota1 + nota2) / 2.0

      
        if media < 5.0:
            situacao = "REPROVADO"
            cor_resultado = "#FF4D4D"  
            situacao = "RECUPERAÇÃO"
            cor_resultado = "#FFC107"  
        else:
            situacao = "APROVADO"
            cor_resultado = "#4CAF50"  

        lbl_media_val.config(text=f"{media:.1f}".replace('.', ','), fg=cor_resultado)
        lbl_situacao_val.config(text=situacao, fg=cor_resultado)

    except ValueError:
        messagebox.showerror("Erro de Validação", "Por favor, insira valores numéricos válidos nas notas.")


janela = tk.Tk()
janela.title("Resultado Académico")
janela.geometry("400x550")
janela.configure(bg="#0F172A")  
janela.resizable(False, False)



BG_COLOR = "#0F172A"
FIELD_BG = "#1E293B"
TEXT_COLOR = "#FFFFFF"
BLUE_BTN = "#2563EB"



tk.Label(janela, text="Nome do Aluno:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11, "bold"), anchor="w").pack(fill="x", padx=25, pady=(20, 5))
entry_nome = tk.Entry(janela, bg=FIELD_BG, fg=TEXT_COLOR, insertbackground="white", font=("Arial", 11), relief="flat", bd=8)
entry_nome.insert(0, "Digite o nome do aluno")
entry_nome.pack(fill="x", padx=25)



tk.Label(janela, text="Nota 1:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11, "bold"), anchor="w").pack(fill="x", padx=25, pady=(15, 5))
entry_nota1 = tk.Entry(janela, bg=FIELD_BG, fg=TEXT_COLOR, insertbackground="white", font=("Arial", 11), relief="flat", bd=8)
entry_nota1.insert(0, "Digite a nota 1")
entry_nota1.pack(fill="x", padx=25)


tk.Label(janela, text="Nota 2:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11, "bold"), anchor="w").pack(fill="x", padx=25, pady=(15, 5))
entry_nota2 = tk.Entry(janela, bg=FIELD_BG, fg=TEXT_COLOR, insertbackground="white", font=("Arial", 11), relief="flat", bd=8)
entry_nota2.insert(0, "Digite a nota 2")
entry_nota2.pack(fill="x", padx=25)



btn_calcular = tk.Button(
    janela, 
    text="CALCULAR RESULTADO", 
    command=calcular_resultado, 
    bg=BLUE_BTN, 
    fg="white", 
    font=("Arial", 11, "bold"), 
    relief="flat", 
    pady=10, 
    cursor="hand2"
)
btn_calcular.pack(fill="x", padx=25, pady=25)



frame_resultado = tk.Frame(janela, bg=FIELD_BG, highlightbackground="#334155", highlightthickness=1, padx=25, pady=20)
frame_resultado.pack(fill="x", padx=25)


frame_resultado.columnconfigure(1, weight=1)


tk.Label(frame_resultado, text="Média:", bg=FIELD_BG, fg=TEXT_COLOR, font=("Arial", 12, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 10))
lbl_media_val = tk.Label(frame_resultado, text="-", bg=FIELD_BG, fg=TEXT_COLOR, font=("Arial", 18, "bold"), anchor="w")
lbl_media_val.grid(row=0, column=1, sticky="w", padx=(30, 0), pady=(0, 10))


tk.Label(frame_resultado, text="Situação:", bg=FIELD_BG, fg=TEXT_COLOR, font=("Arial", 12, "bold"), anchor="w").grid(row=1, column=0, sticky="w")
lbl_situacao_val = tk.Label(frame_resultado, text="-", bg=FIELD_BG, fg=TEXT_COLOR, font=("Arial", 16, "bold"), anchor="w")
lbl_situacao_val.grid(row=1, column=1, sticky="w", padx=(30, 0))


janela.mainloop()