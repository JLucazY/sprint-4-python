import json
import os
import re

#Funções usadas no código
def validar_letras(s):
    return bool(re.match(r"^[A-Za-z]+$", s))
def validar_numeros(s):
    return s.isdigit()

#Função que cria o sensor
def coletar_e_criar_arquivo_sensor(login, nome, senha):
    while True:
        nome_sensor = input("Digite o nome do sensor: ")
        if validar_letras(nome_sensor):
            break
        else:
            print("Nome inválido!")
    while True:
        temperatura = input("Digite a temperatura do sensor: ")
        if validar_numeros(temperatura):
            break
        else:
            print("Digite apenas números!")
    while True:
        energia = input("Digite a energia consumida: ")
        if validar_numeros(energia):
            break
        else:
            print("Digite apenas números!")

    sensor_data = {
        "nome": nome_sensor,
        "temperatura": temperatura,
        "energia": energia
    }

    sensor_filename = f"{nome_sensor}_sensor.json"

    with open(sensor_filename, 'w') as f:
        json.dump(sensor_data, f, indent=4)

    print(f"Dados do sensor foram registrados com sucesso!")
    main(login, nome, senha)

#Função que exibe os sensores criados
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

#Função para exibir os sensores quando o código é encerrado
def exibir_sensores_final():
    for filename in os.listdir('.'):
        if filename.endswith('_sensor.json'):
            with open(filename, 'r') as f:
                sensor_data = json.load(f)
                print(f"Sensor: {sensor_data['nome']}")
                print(f"Temperatura: {sensor_data['temperatura']} °C")
                print(f"Energia Consumida: {sensor_data['energia']} kw")

#função que simula o menu
def main(login, nome, senha):
    nome_usuario = nome
    while True:
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
                break
            case '2':
                exibir_dados_sensores(login, nome, senha)
                break
            case '3':
            #Mostra um resumo da operação
                print(f"""
            Dados coletados:
            Nome do usuário - {senha}
            Login - {login}
            Senha - {nome_usuario}
            Informações dos Sensores:
            """)
                exibir_sensores_final()
                print("\nObrigado por usar o programa!\nEncerrando...")
                exit()
            case _:
                print("Digite um número válido!")

