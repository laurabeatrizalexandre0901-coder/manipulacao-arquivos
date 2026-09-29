def menu_arquivo():
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Python")

    while True:
        print("1-Ler  2-Adicionar  3-Sobrescrever  4-Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            with open("notas.txt") as arquivo:
                print(arquivo.read())

        elif opcao == "2":
            with open("notas.txt", "a") as arquivo:
                arquivo.write(input("Texto: ") + "\n")

        elif opcao == "3":
            with open("notas.txt", "w") as arquivo:
                arquivo.write(input("Texto: "))

        elif opcao == "4":
            break


menu_arquivo()