import os
import json


u = {}
try:
    if os.path.exists('dados.json'):
        with open('dados.json', 'r') as f:
            u = json.load(f)
            print(u)
except FileNotFoundError:
    print("O arquivo json não existe!")

def adicionar_login(login, nome, senha, u):
    u[login] = {"nome": nome, "senha": senha}
    with open('dados.json', 'w') as f:
        json.dump(u, f, indent=4)
    print("Novo usuário adicionado com sucesso!")


