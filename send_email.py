import smtplib
from email.message import Message 

# retorna uma tupla com a configuração do sistem: limite de tantativas e email para envio de alerta
def sys_config():
    max_attempts = int(input("Digite um número máximo de tentativas para o acesso ao sistema via id e senha? "))
    email = input("Qual será o email para enviar um alerta sobre um possível ataque ao sistema? ")
    return max_attempts, email

def send_alert_email(to, max_attempts):  
    
    # criação de um objeto email.message.Message() para representar o email a ser enviado:
    msg = Message()

    msg['Subject'] = "ALERTA DE SEGURANÇA" # define o assunto do email
    msg['From'] = 'joaopedro.loss@gmail.com' # define o remetente do email
    msg['To'] = to # define o destinatário do email
    password = ''

    msg.add_header('Content-Type', 'text/html') # indica que o conteúdo do email está em HTML
    email_content = f"""
    <p><b>Alerta</b></p>
    <p>Por {max_attempts} vezes alguém tentou acessar o seu sistema!</p>
    """    
    msg.set_payload(email_content) # define o conteúdo como sendo o corpo do email a ser enviado

    # faz a conexão com o servidor do gmail:
    s = smtplib.SMTP('smtp.gmail.com: 587')

    # o TLS é um protocolo de segurança que protege a comunicação entre o cliente (seu código Python) 
    # e o servidor SMTP, garantindo que os dados sejam transmitidos de forma criptografada, tornando
    # a conexão mais segura
    s.starttls()

    # tenta fazer o login:
    try:
        s.login(msg['From'], password)
    except:
        print("Problema no envio de email para alerta.")
        return
    
    # caso o login tenha dado certo, envia o email:
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

