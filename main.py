from frt_stp_vldt import *
from send_email import *
from snd_stp_vldt import *

def get_photo_name(id, data_base):    
    for i in range(data_base["quantity"]):
        if data_base["users"][i]["id"] == id:
            return data_base["users"][i]["photo"]

# limpa o terminal, só para melhorar a estética
os.system('cls' if os.name == 'nt' else 'clear')

# abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
with open("dataBase.json") as file_json:
    data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json

max_attempts = int(input("Digite um número máximo de tentativas para o acesso ao sistema via id e senha? "))
email = input("Qual será o email para enviar um alerta sobre um possível ataque ao sistema? ")

id = id_password_validation(max_attempts, data_base)
if id:
    print("Vamos para a segunda etapa")
    img_path = data_base["images_folder_path"] + get_photo_name(id, data_base)
    face_found, face_is_valid = facial_validation(img_path)
    if face_found:
        if face_is_valid:
            print(f"Bem vindo, {name}!")
        else:
            print("Acesso negado.")
    else:
        print("Face não detectada.")
else:
    print("Limite de tentivas excedido. Sistema bloqueado.")
    send_alert_email(email, max_attempts)