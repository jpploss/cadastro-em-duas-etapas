from frt_stp_vldt import *
from send_email import *
from snd_stp_vldt import *
from receive_data import *

def get_photo_name(id, data_base):    
    for i in range(data_base["quantity"]):
        if data_base["users"][i]["id"] == id:
            return data_base["users"][i]["photo"]

def get_user_name(id, data_base):
    for i in range(data_base["quantity"]):
        if data_base["users"][i]["id"] == id:
            return data_base["users"][i]["name"]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# limpa o terminal, só para melhorar a estética
clear_terminal()

# abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
with open("dataBase.json") as file_json:
    data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

max_attempts, email = sys_config()

while True:
    clear_terminal()
    #lendo o que o usuário deseja fazer
    acao = int(input("01 - Sair.\n02 - Cadastrar novo usuario.\n03 - Acessar sistema.\nDigite um numero: "))

    if acao == 1:
        print("\nSAINDO DO PROGRAMA")
        break
    
    elif acao == 2:
        new_user = Get_user(data_base["images_folder_path"], data_base["users"])
        if new_user:
            Add_user_data(new_user)
            print(f"Usuário de ID '{new_user['id']}' cadastrado.")
        else:
            clear_terminal()
            print("Não foi possível realizar o cadastro.")
            print("Usuário não salvou a foto do rosto conforme solicitado.")
        sleep(2)


    elif acao == 3:

        id = id_password_validation(max_attempts, data_base)
        if id:
            print("Vamos para a segunda etapa")
            img_path = data_base["images_folder_path"] + get_photo_name(id, data_base)
            face_found, face_is_valid = facial_validation(img_path)
            if face_found:
                if face_is_valid:
                    print(f"Bem vindo, {get_user_name(id, data_base)}!")
                else:
                    print("Acesso negado.")
            else:
                print("Face não detectada.")
        else:
            print("Limite de tentivas excedido. Sistema bloqueado.")
            send_alert_email(email, max_attempts)
        sleep(2)
    else:
        print("Opção inválida.")
        sleep(1)