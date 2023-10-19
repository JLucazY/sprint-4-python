import coletando_json
import re
import main

def validar_login(login):
    return re.match(r'^[a-zA-Z0-9]{6,12}$', login)
def validar_nome(nome):
    return re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome)
def validar_senha(senha):
    return re.match(r'\d{1,5}', senha)

def entrar_com_usuario():
    while True:
        login = input("Digite o login: ")
        if login not in coletando_json.u.keys():
            print("Usuário inválido!")
        else:
            break

    while True:
        senha = input("Digite sua senha: ")
        if senha not in coletando_json.u[login].values():
            print("Senha inválida!")
        else:
            break
    print("Log in realizado com sucesso!")
    main.main()

def criar_usuario():
    while True:
        login = input("Digite o nome de login: ")
        if validar_login(login):
            break
        else:
            print("Nome de login deve conter entre 6 a 12 caracteres!")
    while True:
        nome = input("Digite seu nome: ")
        if validar_nome(nome):
            break
        else:
            print("Nome não pode conter números!")
    while True:
        senha = input("Digite sua senha: ")
        if validar_senha(senha):
            break
        else:
            print("Senha deve conter de 1 a 5 caracteres e somente números!")
    print(f"nome: {nome}\nusuário: {login}\nsenha: {senha}")

def entrar():
    print("1 - Entrar\n2 - Criar usuário")
    escolha_usuario = input()
    match escolha_usuario:
        case '1':
            entrar_com_usuario()
        case '2':
            criar_usuario()

