# two-step-validation
## O funcionamento do sistema se deve da seguinte forma:
### 01. Etapa de configuração do sistema:
  - É solicitado um número máximo de tentativas para a primeira etapa (id e senha)
  - É solicitado um email para o envio de uma mensagem de alerta caso as tentativas na primeira etapa tenham excedido o limite fornecido
### 02. Etapa de login:
### - 02.1:
    - É solicitado o id e a senha
    - Verifica a validade do id e senha a partir de uma base de dados em um arquivo .json
### - 02.2:
    - Caso a etapa 02.1 tenha sido bem sucedida, ocorre a segunda etapa (reconhecimento facial)

## Configurações:
- O caminho para a pasta com as imagens deve ser fornecido no campo "images_folder_path" do .json
- O id de um usuário deve ser único
- O campo "quantity" corresponde à quantidade de usuários e deve estar sempre atualizado para o funcionamento correto do programa

## Pré-requisitos:
- pip install opencv-python
- pip install dlib
- pip install face_recognition
