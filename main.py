from deepface import DeepFace # resposável por realizar o validação facial
import cv2 # resposável por realizar a manipulação da webcam
import json # útil para lidar com a base de usuário (arquivo .json)


with open("dataBase.json") as file_json:
    user = json.load(file_json) # ususario recebe um objeto correspondente ao conteúdo do .json


name = input("Digite o seu nome de usuário: ")
password = input("Digite sua senha: ")

user_list = user['users']
logado = False
for i in range(len(user_list)):
    if name == user_list[i]['name']:
        if password == user_list[i]['password']:
            print("Bem vindo")
            logado = True
        else:
            print("Nome de usuário e/ou senha incorretos")
 

if not logado:
    print("Nome de usuário e/ou senha incorretos")
else:
    