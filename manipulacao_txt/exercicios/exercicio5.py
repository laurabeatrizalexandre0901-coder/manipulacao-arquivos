def contar_caracteres():
    with open("texto.txt", "r") as arquivo:
        texto = arquivo.read()

    print("Quantidade de caracteres:", len(texto))


contar_caracteres()