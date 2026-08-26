import os
import time
os.system("cls")

class Quarto_Padrao():
    def __init__(self,hospede,diaria,dias):
        self.hospede = hospede
        self.diaria = diaria * dias
        print(f"Hóspede:{hospede}\nQuarto padrão\nDias reservados:{dias}\nTotal a pagar:{diaria}")
        
class Suite_Presidencial(Quarto_Padrao):
    def __init__(self, hospede, diaria, dias, taxa_mordomo):
        super().__init__(hospede)
        self.diaria = (diaria*dias )+ taxa_mordomo
        

while True:
    print("-------Menu da Recepção-------\n\n1-Reservar Quarto Padrão\n2-Reservar Suíte Presidencial\n3-Ver Histórico de Reservas\n4-Sair")
    try:
        atendimento = int(input("Escolha uma das opções acima: "))
        break
    except ValueError:
        os.system("cls")
        print("Valor inválido, escolha uma das opções cadastradas")
        time.sleep(2)
        
match atendimento:
    case 1:
        nome = input("Nome do cliente: ")
        v_diaria = 250
        q_dias = int(input("Informe quantos dias deseja ficar: "))
        
        quarto_cliente = Quarto_Padrao(nome,v_diaria,q_dias)
        quarto_cliente()