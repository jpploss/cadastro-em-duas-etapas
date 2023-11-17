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

