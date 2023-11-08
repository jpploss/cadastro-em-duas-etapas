import smtplib
import email.message

def send_email(to, max_attempts):  
    corpo_email = f"""
    <p><b>Alerta</b></p>
    <p>Por {max_attempts} vezes alguém tentou acessar o seu sistema!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "ALERTA DE SEGURANÇA"
    msg['From'] = 'joaopedro.loss@gmail.com'
    msg['To'] = to
    password = 'sewwapmfimdurnzb' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    try:
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    except:
        print("Problema no envio de email para alerta.")
