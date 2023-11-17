# Importar o módulo
import json

#recebendo dados de cadastro do usuário pelo terminal
def Get_user ():
    nome = input("Digite o nome para cadastro: ")
    id = input("Digite o ID para cadastro: ")
    password = input("Digite a senha para cadastro: ")
    photo = input("Digite o nome do arquivo .jpg para cadastro: ")

    user = {
        "name": nome,
        "id": id,
        "password": password,
        "photo": photo
    }

    return user

#converte o dicionário com os dados do usuário em uma string JSON já identada
def Convert_user_to_JSON (user):
    user_json = json.dumps(user, indent=3)

    return user_json

#adicionar usuário no dataBase,json
def Add_user_data (new_user, data_base_json):
    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("dataBase.json", 'r') as file_json:
        data_base_json = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

    # Adicionando o novo usuário à lista existente
    data_base_json["users"].append(new_user)

    # Acrescentando uma unidade ao atributo "quantity"
    data_base_json["quantity"] += 1

    # Escrevendo de volta ao arquivo JSON
    with open("dataBase.json", 'w') as json_file:
        json.dump(data_base_json, json_file, indent=4)
