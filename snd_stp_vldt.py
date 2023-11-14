import cv2
import face_recognition as fr

# def get_encodings_faces(url_img):

#     img = fr.load_image_file(url_img)

#     # faces recebe uma lista com os rostos contidos na imagem
#     faces = fr.face_encodings(img)

#     return faces

# def compare_reference_unknown(url_img_reference, encoding_face_unknown):
#     img_reference = fr.load_image_file(url_img_reference)
#     return fr.compare_faces(img_reference, encoding_face_unknown)

# def facial_validation(url_img_reference):
#     webcam = cv2.VideoCapture(0) # faz a conexão com a webcam

#     ref_img = fr.load_image_file(url_img_reference)

#     if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
#         validacao, frame = webcam.read() # le a imagem da webcam

#         while validacao:
            
#             validacao, frame = webcam.read()
#             cv2.imshow("webcam do joss", frame)
            
#             # result = fr.compare_faces(ref_img, frame)

#             key = cv2.waitKey(3) # retorna um inteiro correpondendo ao código ASCII da tecla apertada
            
#             if key == 27:
#                 break

#     webcam.release() # finaliza a conexão com a webcam
#     cv2.destroyAllWindows() # garante que as janelas criadas serão fechadas ao encerrar o programa


# facial_validation("./images/cr.jpeg")

def get_encoding_face(img_url):
    img = cv2.imread(img_url)
    
    # o cv2 usa o por padrão BGR, para converter em RBG:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # face_encodings retorna uma lista com os rostos contidos na imagem, como o 
    # objetivo é pegar apenas um rosto, basta usar o índice 0 
    face = fr.face_encodings(img)[0]

    return face

def get_faces_in_frame(frame):
    faces = fr.face_encodings(frame)
    return faces

def face_valid(faces, face_ref):
    if faces != None:
        for i in range(len(faces)):
            result = fr.compare_faces([face_ref], faces[i])[0]
            if result:
                return True
    return False

def DrawInFaces(frame_rgb, frame):
    faces = fr.face_locations(frame_rgb)
    for face in faces:
        y1, x1, y2, x2 = face[0], face[1], face[2], face[3]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,0), 2)
    return frame

def CloseCam(cam):
    cam.release() # finaliza a conexão com a webcam
    cv2.destroyAllWindows() # garante que as janelas criadas serão fechadas ao encerrar o programa


# retorna um tupla: [0]: se as faces foram achadas; [1]: se é válida
def facial_validation(imgRef_url):
    face_ref = get_encoding_face(imgRef_url)

    webcam = cv2.VideoCapture(0) # faz a conexão com a webcam

    if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
        validacao, frame = webcam.read() # le a imagem da webcam

        count = 0
        while validacao:
            count += 1
            validacao, frame = webcam.read()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # cv2.imshow("Face validation", frame)

            faces_found = get_faces_in_frame(frame_rgb)

            if faces_found:
                frame = DrawInFaces(frame_rgb, frame)
                if face_valid(faces_found, face_ref):
                    return True, True
                elif count == 10:
                    return True, False
            elif count == 10:
                return False, False

            cv2.imshow("Face validation", frame)
            cv2.waitKey(1) # retorna um inteiro correpondendo ao código ASCII da tecla apertada
            
    
    CloseCam(webcam)

