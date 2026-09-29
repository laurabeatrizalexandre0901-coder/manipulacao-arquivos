def classificar_alunos():
    with open("alunos.txt", "w") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")


    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            if nota >= 6:
                situacao = "Aprovado"
            elif nota >= 4:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print(nome, "-", nota, "-", situacao)


classificar_alunos()