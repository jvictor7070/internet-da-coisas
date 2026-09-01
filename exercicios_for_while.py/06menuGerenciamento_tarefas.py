import os
os.system("cls")

lista_tarefas = []

while True:
    print("-------Menu-------\n\n1 - Adicionar tarefa\n2 - Remover tarefa\n3 - Mostrar tarefas\n0 - Sair")
    menu = int(input("Escolha uma das opções acima: "))
    os.system("cls")
    
    if menu == 1:
        tarefa = input("adicione uma tarefa: ")
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif menu == 2:
        tarefa = input("qual tarefa gostaria de excluir: ")
        lista_tarefas.remove(tarefa)
        print("Tarefa removida com sucesso!")
    elif menu == 3:
        print(f"Lista de tarefas:{lista_tarefas}")
    elif menu == 4:
        break
    else:
        print("Número inválido")
    
    