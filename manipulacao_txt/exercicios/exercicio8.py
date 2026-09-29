def contar_palavras():
    with open("texto.txt", "w") as arquivo:
        arquivo.write("Python é uma linguagem de programação.\n")
        arquivo.write("Python pode ser utilizada para desenvolvimento web.\n")
        arquivo.write("Python também é muito utilizada em ciência de dados.")

    with open("texto.txt", "r") as arquivo:
        texto = arquivo.read()

    palavras = texto.split()

    print("Quantidade de palavras:", len(palavras))


contar_palavras()