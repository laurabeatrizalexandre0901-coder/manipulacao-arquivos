def buscar_nome():
    with open("nomes.txt", "w") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")
        arquivo.write("Gabriel\n")

    nomes = []

    with open("nomes.txt", "r") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    nome = input("Digite o nome: ")

    if nome in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


buscar_nome()