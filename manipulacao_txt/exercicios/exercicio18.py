def gerenciar_notas():
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Ana;8.5;7;9\nBruno;5;6;4.5")

    with open("notas.txt") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            media = sum(map(float, dados[1:])) / 3

            print(dados[0], round(media, 2))

            if media >= 6:
                print("Aprovado")
            else:
                print("Reprovado")


gerenciar_notas()