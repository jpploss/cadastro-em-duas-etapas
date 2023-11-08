import json # útil para lidar com a base de usuário (arquivo .json)
import os
from time import sleep

# retorna o id e o password lidos via terminal
def get_id_password():
    id = input("Digite o seu id: ").strip()
    password = input("Digite sua senha: ").strip()
    return id, password

# se o id e o password estão cadastrados: retorna o nome do usuário. Caso contrário, retorna None
def get_user_name(user_list, id, password):
    for i in range(len(user_list)):
        if id == user_list[i]['id']:
            if password == user_list[i]['password']:
                return user_list[i]['name']
    return None

def id_password_validation(max_attempts=1):

    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("dataBase.json") as file_json:
        data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

    user_list = data_base['users']

    tentativas = 0
    while True:
        tentativas += 1

        # limpa o terminal, só para melhorar a estética
        os.system('cls' if os.name == 'nt' else 'clear')
    
        id, password = get_id_password()

        name = get_user_name(user_list, id, password)
        if name:
            return name
        else:
            print("Nome de usuário e/ou senha incorretos")

        # se tentou por cinco vezes, retorna False
        if tentativas == max_attempts:
            return None
        
        sleep(1.8)