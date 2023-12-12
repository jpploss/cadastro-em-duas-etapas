# two-step-validation
## O funcionamento do sistema:
### 01. Etapa de configuração do sistema:
- É solicitado um email para o envio de uma mensagem de alerta caso se detecte um possível ataque
### 02. Etapa de login:
#### 02.1:
- É solicitado o id e a senha
- Verifica a validade do id e senha a partir de uma base de dados em um arquivo .json
#### 02.2:
- Caso a etapa 02.1 tenha sido bem sucedida, ocorre a segunda etapa (reconhecimento facial)

## Configuração:
- O caminho para a pasta com as imagens deve ser fornecido no campo "images_folder_path" do .json

## Pré-requisitos:
- pip install opencv-python
- pip install dlib
- pip install face_recognition
- Colocar os módulos necessários na mesma pasta do arquivo principal

## Limitações reconhecidas:
- O sistema não trata os casos em que se utiliza uma foto da pessoa para acessar o sistema em vez da própria pessoa em si.
- Não há a funcionalidade de excluir alguém previamente cadastrado no sistema.
