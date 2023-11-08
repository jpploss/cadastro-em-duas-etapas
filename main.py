from first_step_validation import *
from send_email import *

# limpa o terminal, só para melhorar a estética
os.system('cls' if os.name == 'nt' else 'clear')

max_attempts = int(input("Digite um número máximo de tentativas para o acesso ao sistema via id e senha? "))
email = input("Qual será o email para enviar um alerta sobre um possível ataque ao sistema? ")

name = id_password_validation(max_attempts)
if name:
    print(f"Bem vindo, {name}!")
else:
    print("Limite de tentivas excedido. Sistema bloqueado.")
    send_email(email, max_attempts)