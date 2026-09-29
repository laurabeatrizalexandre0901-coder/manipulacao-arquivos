def buscar_produto():
    with open("produtos.txt", "w") as arquivo:
        arquivo.write("Teclado;120.50;10\nMouse;75.90;15")

    busca = input("Produto: ")

    with open("produtos.txt") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            if nome.lower() == busca.lower():
                print(nome, preco, quantidade)
                return

    print("Produto não encontrado!")


buscar_produto()