
# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abre para escrita e apaga p conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele ja existir

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # O "open()" função para leitura ou escrita de arquivos
    with open('arquivo.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write('Luara\n')
        arquivo.write('Samara\n')
        arquivo.write('Maria\n')


# criar_arquivo()

def adicionar_alunos(nome):
    with open('arquivo.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write(nome + '\n')


# adicionar_alunos('laura')
# adicionar_alunos('sophia')
# adicionar_alunos('mayara')

def listar_alunos(nome):
    with open('alunos.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteúdo é {conteudo}")


# listar_alunos()

def listar_aluno_individual(nome):
    lista_alunos = []
    with open('alunos.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_alunos.append(linha.strip())

    nomes_alunos = lista_alunos

    print(f'lista de alunos: {nomes_alunos}')


# listar_aluno_individual()

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open('cadastro.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}; {idade}\n")

        print("aluno cadastrado com sucesso")


def listar_cadastro():
    itens_cadastro = []
    with open('cadastro.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(';')

            obj = {
                'nome': nome,
                'idade': idade
            }

            itens_cadastro.append(obj)
            print(f'itens cadastrados: {itens_cadastro}')


cadastrar_aluno()
listar_cadastro()
