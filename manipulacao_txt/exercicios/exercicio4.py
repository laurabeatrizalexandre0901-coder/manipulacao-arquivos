def contar_linhas():
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    print("O arquivo possui", len(linhas), "linhas.")


contar_linhas()