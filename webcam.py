import cv2
import face_recognition as fr

def get_encodings_faces(url_img):

    img = fr.load_image_file(url_img)

    # faces recebe uma lista com os rostos contidos na imagem
    faces = fr.face_encodings(img)

    return faces

def compare_reference_unknown(url_img_reference, encoding_face_unknown):
    img_reference = fr.load_image_file(url_img_reference)
    return fr.compare_faces(img_reference, encoding_face_unknown)

def facial_validation(url_img_reference):
    webcam = cv2.VideoCapture(0) # faz a conexão com a webcam

    ref_img = fr.load_image_file(url_img_reference)

    if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
        validacao, frame = webcam.read() # le a imagem da webcam

        while validacao:
            
            validacao, frame = webcam.read()
            cv2.imshow("webcam do joss", frame)
            
            # result = fr.compare_faces(ref_img, frame)

            key = cv2.waitKey(3) # retorna um inteiro correpondendo ao código ASCII da tecla apertada
            
            if key == 27:
                break

    webcam.release() # finaliza a conexão com a webcam
    cv2.destroyAllWindows() # garante que as janelas criadas serão fechadas ao encerrar o programa


facial_validation("./images/cr.jpeg")

