def gerenciar_tarefas():
    tarefas = []

    with open("tarefas.txt", "w") as arquivo:
        arquivo.write("Estudar Python\nFazer exercícios")

    while True:
        print("1-Adicionar 2-Listar 3-Remover 4-Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            tarefas.append(input("Tarefa: "))

        elif opcao == "2":
            print(tarefas)

        elif opcao == "3":
            tarefas.remove(input("Tarefa: "))

        elif opcao == "4":
            break


gerenciar_tarefas()