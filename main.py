import json # útil para lidar com a base de usuário (arquivo .json)
import os
from time import sleep



def user_password_validation(max_attempts):

    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("dataBase.json") as file_json:
        data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

    user_list = data_base['users']

    """
    verifica se o nome fornecido está na base de cadastro. Caso estaja,
    verifica se a senha está correta. Se o nome estiver cadastrado e a
    senha estiver correta, retorna True:
    """
    tentativas = 0
    while True:
        tentativas += 1

        # limpa o terminal, só para melhorar a estética
        os.system('cls' if os.name == 'nt' else 'clear')
    
        name = input("Digite o seu nome de usuário: ").strip()
        password = input("Digite sua senha: ").strip()
        for i in range(len(user_list)):
            if name == user_list[i]['name']:
                if password == user_list[i]['password']:
                    return True
        print("Nome de usuário e/ou senha incorretos")

        # se tentou por cinco vezes, retorna False
        if tentativas == max_attempts:
            return False
        
        sleep(2)

logado = user_password_validation(1)

if logado:
    print("Bem vindo")
else:
    print("Sai fora")
