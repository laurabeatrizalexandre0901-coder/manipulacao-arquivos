def carregar_nomes():
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

    print(nomes)


carregar_nomes()