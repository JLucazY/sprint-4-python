import re
import main

#Dados usados para login dos usuários
dados_usuarios = {
    "Joao123": {
        "nome": "João Lucas",
        "senha": "0000"
    },
    "Breno123": {
        "nome": "Breno Silva",
        "senha": "0000"
    }
}

#Funções usadas no código
def validar_login(login):
    return re.match(r'^[a-zA-Z0-9]{6,12}$', login)

def validar_nome(nome):
    return re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome)

def validar_senha(senha):
    return re.match(r'\d{1,5}', senha)

#Função de entrar com usuário e senha
def entrar_com_usuario():
    while True:
        login = input("Digite o login: ")
        #verifica se os dados estão corretos
        if login not in dados_usuarios.keys() or not validar_login(login):
            print("Usuário inválido!")
        else:
            break

    while True:
        senha = input("Digite sua senha: ")
        # verifica se os dados estão corretos
        if senha != dados_usuarios[login]["senha"] or not validar_senha(senha):
            print("Senha inválida!")
        else:
            break

    print("Log in realizado com sucesso!")
    #Chama a função main do menu
    main.main(login, senha, dados_usuarios[login]["nome"])

#Função que cria o usuário, senha e nome
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

    novo_usuario = {
        "nome": nome,
        "senha": senha
    }
    dados_usuarios[login] = novo_usuario
    entrar()

#Função que simula um menu de entrar/criar usuário
def entrar():
    print(dados_usuarios)
    while True:
        print("1 - Entrar\n2 - Criar usuário")
        escolha_usuario = input()

        match escolha_usuario:
            case '1':
                entrar_com_usuario()
                break
            case '2':
                criar_usuario()
                break
            case _:
                print("Digite um número válido!")

# Chama a função entrar para iniciar o programa
entrar()
