import json
import os


def coletar_e_criar_arquivo_sensor(login, nome, senha):
    nome = input("Digite o nome do sensor: ")
    temperatura = input("Digite a temperatura do sensor: ")
    energia = input("Digite a energia consumida: ")

    sensor_data = {
        "nome": nome,
        "temperatura": temperatura,
        "energia": energia
    }

    sensor_filename = f"{nome}_sensor.json"

    with open(sensor_filename, 'w') as f:
        json.dump(sensor_data, f, indent=4)

    print(f"Dados do sensor foram registrados com sucesso!")
    main(login, nome, senha)

def exibir_dados_sensores(login, nome, senha):
    for filename in os.listdir('.'):
        if filename.endswith('_sensor.json'):
            with open(filename, 'r') as f:
                sensor_data = json.load(f)
                print(f"Sensor: {sensor_data['nome']}")
                print(f"Temperatura: {sensor_data['temperatura']} °C")
                print(f"Energia Consumida: {sensor_data['energia']} kw")
                print()
    main(login, nome, senha)

def main(login, nome, senha):
    print("""
        Menu
    1 - Cadastrar dados dos sensores
    2 - Exibir dados dos sensores
    3 - Encerrar
    """)

    escolha_usuario = input()

    match escolha_usuario:
        case '1':
            coletar_e_criar_arquivo_sensor(login, nome, senha)
        case '2':
            exibir_dados_sensores(login, nome, senha)
        case '3':
            print(f""""
Dados coletados:
nome - {nome}
login - {login}
senha - {senha}

sensores:""")
            print("1 - Encerrar\n2 - inicar outra operação")
            continuar = input()
            match continuar:
                case '1':
                    exit()
                case '2':
                    print("foi")