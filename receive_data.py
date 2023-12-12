# Importar o módulo
import json
import cv2
from time import sleep
import os
import cryptocode

def verify_id(id, users):
    for i in range(len(users)):
        if id == users[i]["id"]:
            return False
    return True

def get_id(users):
    id = input("Digite o ID para cadastro: ")
    while True:
        if verify_id(id, users):
            return id
        os.system('cls' if os.name == 'nt' else 'clear')
        id = input(f"O ID {id} já existe.\nDigite outro ID para cadastro: ")

def get_photo(id, img_path):
    print(f"Para completar o cadastro adicione uma foto do seu rosto em '{img_path}'. Lembrando que ela deve ter o mesmo nome do ID fornecido.")
    photo_ext = input("Digite a extensão da foto salva (ex. png, jpeg, jpg): ")
    photo_name = id + '.' + photo_ext

    count = 0
    while True:
        count += 1
        try:
            with open(img_path+photo_name, "r") as f:
                return photo_name
        except FileNotFoundError as e:
            pass

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Não foi possível encontrar o arquivo '{photo_name}' em '{img_path}'.")   
        print(f"Verifique se o nome da foto é '{photo_name}' e está salva em '{img_path}'.")

        if count == 15:
            return None

        sleep(1)

#recebendo dados de cadastro do usuário pelo terminal
def Get_user (img_path, users):
    nome = input("Digite o nome para cadastro: ")
    id = get_id(users)
    password = cryptocode.encrypt(input("Digite a senha para cadastro: ").strip(), "py")
    
    photo_name = get_photo(id, img_path)
    if photo_name == None:
        return None
    
    print("Cadastro feito com sucesso.")
    user = {
        "name": nome,
        "id": id,
        "password": password,
        "photo": photo_name
    }

    return user

#converte o dicionário com os dados do usuário em uma string JSON já identada
def Convert_user_to_JSON (user):
    user_json = json.dumps(user, indent=3)

    return user_json

#adicionar usuário no dataBase,json
def Add_user_data (new_user):
    arq = 'dataBase.json'
    try:
        # Tenta abrir o arquivo no modo de leitura e escrita
        with open(arq, 'r+') as file_json:
            # Tenta carregar o conteúdo do arquivo JSON
            data_base_json = json.load(file_json)

            # Adicionando o novo usuário à lista existente
            data_base_json["users"].append(new_user)

            # Acrescentando uma unidade ao atributo "quantity"
            data_base_json["quantity"] += 1

            # Move o cursor para o início do arquivo antes de escrever
            file_json.seek(0)

            # Escreve de volta ao arquivo JSON
            json.dump(data_base_json, file_json, indent=4)
        
    except FileNotFoundError:
        # Se o arquivo não existe, cria um novo
        with open(arq, 'w') as file_json:
            # Cria um novo dicionário com o novo usuário
            data_base_json = {
                "users": [new_user],
                "quantity": 1
            }

            # Escreve o dicionário no arquivo JSON
            json.dump(data_base_json, file_json, indent=4)

