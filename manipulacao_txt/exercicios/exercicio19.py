def gerar_relatorio():
    with open("vendas.txt", "w") as arquivo:
        arquivo.write("Ana;Notebook;3500\nBruno;Mouse;80\nAna;Monitor;900")

    total = 0

    with open("vendas.txt") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")
            print(vendedor, produto, valor)
            total += float(valor)

    print("Total:", total)


gerar_relatorio()