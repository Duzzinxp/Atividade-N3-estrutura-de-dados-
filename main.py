import json

alunos = []

# Carregar arquivo
try:
    arquivo = open("alunos.json", "r")
    alunos = json.load(arquivo)
    arquivo.close()
except:
    alunos = []


# Salvar arquivo
def salvar():
    arquivo = open("alunos.json", "w")
    json.dump(alunos, arquivo)
    arquivo.close()


# Cadastrar
def cadastrar():
    nome = input("Nome: ")
    matricula = input("Matrícula: ")

    aluno = [nome, matricula]
    alunos.append(aluno)

    salvar()
    print("Aluno cadastrado!")


# Alterar
def alterar():
    matricula = input("Digite a matrícula: ")
    encontrou = False

    for aluno in alunos:
        if aluno[1] == matricula:
            aluno[0] = input("Novo nome: ")
            aluno[1] = input("Nova matrícula: ")
            encontrou = True
            salvar()
            print("Aluno alterado!")

    if encontrou == False:
        print("Aluno não encontrado!")


# Excluir
def excluir():
    matricula = input("Digite a matrícula: ")
    encontrou = False

    for aluno in alunos:
        if aluno[1] == matricula:
            alunos.remove(aluno)
            encontrou = True
            salvar()
            print("Aluno excluído!")
            break

    if encontrou == False:
        print("Aluno não encontrado!")


# Pesquisar
def pesquisar():
    pesquisa = input("Digite o nome ou matrícula: ").lower()
    encontrou = False

    for aluno in alunos:
        if pesquisa in aluno[0].lower() or pesquisa in aluno[1].lower():
            print("Nome:", aluno[0])
            print("Matrícula:", aluno[1])
            encontrou = True

    if encontrou == False:
        print("Aluno não encontrado!")


# Listar por nome
def listar_nome():
    lista = []

    for aluno in alunos:
        lista.append([aluno[0], aluno[1]])

    lista.sort()

    for aluno in lista:
        print(aluno)


# Listar por matrícula
def listar_matricula():
    lista = []

    for aluno in alunos:
        lista.append([aluno[1], aluno[0]])

    lista.sort()

    for aluno in lista:
        print("Matrícula:", aluno[0], "- Nome:", aluno[1])


# Menu principal
while True:
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Pesquisar")
    print("5 - Listar por nome")
    print("6 - Listar por matrícula")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        alterar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        pesquisar()
    elif opcao == "5":
        listar_nome()
    elif opcao == "6":
        listar_matricula()
    elif opcao == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")
