import json # útil para lidar com a base de usuário (arquivo .json)
import os
from time import sleep

def get_user_password():
    name = input("Digite o seu nome de usuário: ").strip()
    password = input("Digite sua senha: ").strip()
    return name, password

def is_valid_input(user_list, name, password):
    for i in range(len(user_list)):
        if name == user_list[i]['name']:
            if password == user_list[i]['password']:
                return True
    return False

def user_password_validation(max_attempts=1):

    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("dataBase.json") as file_json:
        data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

    user_list = data_base['users']

    tentativas = 0
    while True:
        tentativas += 1

        # limpa o terminal, só para melhorar a estética
        os.system('cls' if os.name == 'nt' else 'clear')
    
        name, password = get_user_password()

        if is_valid_input(user_list, name, password):
            return True
        print("Nome de usuário e/ou senha incorretos")

        # se tentou por cinco vezes, retorna False
        if tentativas == max_attempts:
            return False
        
        sleep(2)