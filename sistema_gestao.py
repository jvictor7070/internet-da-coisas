import os
import time

class Quarto_Padrao:
    def __init__(self, hospede, diaria, dias):
        self.hospede = hospede
        self.dias = dias
        self.diaria = diaria * dias
        self.tipo_quarto = "Quarto Padrão" # Ajuda na hora de salvar

    # Criamos um método específico para salvar e mostrar o recibo
    def confirmar_reserva(self):
        print(f"-----Hóspede cadastrado com sucesso-----")
        print(f"Hóspede: {self.hospede}")
        print(f"Acomodação: {self.tipo_quarto}")
        print(f"Dias reservados: {self.dias}")
        print(f"Total a pagar: R$ {self.diaria:.2f}\n")
        
        with open("Lista_reserva.txt", "a", encoding="utf-8") as arquivo:
            # Usando os atributos do próprio objeto (self)
            arquivo.write(f"Cliente: {self.hospede} - {self.dias} dias - {self.tipo_quarto} - Total: R$ {self.diaria:.2f}\n")

class Suite_Presidencial(Quarto_Padrao):
    def __init__(self, hospede, diaria, dias, taxa_mordomo):
        super().__init__(hospede, diaria, dias) # Puxa atributos da classe mãe
        self.taxa_mordomo = taxa_mordomo
        self.diaria = (diaria * dias) + taxa_mordomo # Atualiza o valor com a taxa
        self.tipo_quarto = "Suíte Presidencial" # Atualiza o nome do quarto


while True:
    os.system("cls")
    print("-------Menu da Recepção-------\n")
    print("1-Reservar Quarto Padrão\n2-Reservar Suíte Presidencial\n3-Ver Histórico de Reservas\n4-Sair\n")
    
    # 1. Proteção do Menu
    try:
        atendimento = int(input("Escolha uma das opções acima: "))
    except ValueError:
        print("\nValor inválido, digite apenas os números do menu!")
        time.sleep(2)
        continue # Faz o laço reiniciar imediatamente, evitando erros no 'match'
        
    match atendimento:
        case 1 | 2: # Podemos juntar o 1 e o 2 já que as perguntas iniciais são iguais!
            nome = input("\nNome do cliente: ")
            
            # 2. Proteção do input de dias (Exigência do Cliente)
            while True:
                dias_input = input("Informe quantos dias deseja ficar: ")
                if dias_input.isdigit(): # Garante que só tem números
                    q_dias = int(dias_input)
                    break
                else:
                    print("Por favor, digite apenas números inteiros para os dias!\n")
            
            os.system("cls")
            
            if atendimento == 1:
                reserva = Quarto_Padrao(nome, 250, q_dias)
            else:
                reserva = Suite_Presidencial(nome, 250, q_dias, 100)
                
            # Agora chamamos a ação apenas uma vez, e o objeto sabe qual é o seu tipo!
            reserva.confirmar_reserva()
            input("Pressione ENTER para voltar ao menu...")
            
        case 3:
            os.system("cls")
            print("-------HISTÓRICO DE RESERVAS-------\n")
            # 3. Tratamento correto para arquivo não encontrado
            try:
                with open("Lista_reserva.txt", "r", encoding="utf-8") as arquivo:
                    print(arquivo.read())
            except FileNotFoundError:
                print("Nenhum hóspede cadastrado ainda no histórico.\n")
                
            input("Pressione ENTER para voltar ao menu...")
            
        case 4:
            print("\nSaindo do programa!!")
            time.sleep(2)
            os.system("cls")
            break
            
        case _:
            print("\nOpção não existe no menu!")
            time.sleep(2)