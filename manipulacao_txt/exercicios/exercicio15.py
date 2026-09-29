def cadastrar_produtos():
    with open("produtos.txt", "w") as arquivo:
        arquivo.write("Teclado;120.50;10\nMouse;75.90;15")

    produtos = []

    with open("produtos.txt") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produtos.append({
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            })

    print(produtos)


cadastrar_produtos()