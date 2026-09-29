def calcular_estoque():
    with open("produtos.txt", "w") as arquivo:
        arquivo.write("Teclado;120.50;10\nMouse;75.90;15")

    total = 0

    with open("produtos.txt") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")
            total += float(preco) * int(quantidade)

    print("Total: R$", total)


calcular_estoque()