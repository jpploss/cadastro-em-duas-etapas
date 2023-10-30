import cv2
from deepface import DeepFace
# video util: https://www.youtube.com/watch?v=r8Qg3NfdiHc

webcam = cv2.VideoCapture(0) # faz a conexão com a webcam

if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
    validacao ,frame = webcam.read() # le a imagem da webcam

    while validacao:
        validacao ,frame = webcam.read()
        cv2.imshow("webcam do joss", frame)
        key = cv2.waitKey(3) # retorna um inteiro correpondendo ao código ASCII da tecla apertada

        result = DeepFace.verify(img1_path = "h1.png", img2_path = frame)
        if(result['verified']):
            print("oi hen")
            break
        elif DeepFace.verify(img1_path = "test.png", img2_path = frame)['verified']:
            print("oi jp")
            break
        
        if key == 27:
            break
    
    cv2.imwrite('test2.png', frame) # cria um arquivo com o último frame

webcam.release() # finaliza a conexão com a webcam
cv2.destroyAllWindows() # garante que as janelas criadas serão fechadas ao encerrar o programa
