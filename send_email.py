import smtplib
from email.message import Message
import datetime

# retorna uma tupla com a configuração do sistem: limite de tantativas e email para envio de alerta
def sys_config():
    email = input("Qual será o email para enviar um alerta sobre um possível ataque ao sistema? ")
    return email

def send_alert_email(to):  
    
    # criação de um objeto email.message.Message() para representar o email a ser enviado:
    msg = Message()

    msg['Subject'] = "ALERTA DE SEGURANÇA" # define o assunto do email
    msg['From'] = 'joaopedro.loss@gmail.com' # define o remetente do email
    msg['To'] = to # define o destinatário do email
    password = 'sbaq trbc wnbt odca'

    time = datetime.datetime.now()
    msg.add_header('Content-Type', 'text/html') # indica que o conteúdo do email está em HTML
    email_content = f"""
    <p><b>Alerta</b></p>
    <p>Possível ataque detectado às {time.hour}:{time.minute}:{time.second}. Sistema temporariamente bloqueado por segurança.</p>
    """    
    msg.set_payload(email_content) # define o conteúdo como sendo o corpo do email a ser enviado

    # faz a conexão com o servidor do gmail:
    s = smtplib.SMTP('smtp.gmail.com: 587')

    # o TLS é um protocolo de segurança que protege a comunicação entre o cliente (seu código Python) 
    # e o servidor SMTP, garantindo que os dados sejam transmitidos de forma criptografada, tornando
    # a conexão mais segura
    s.starttls()

    # tenta fazer o login e enviar o email:
    try:
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    except:
        pass
    
    
    

