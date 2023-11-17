import cv2
import face_recognition as fr

def get_encoding_face(img_url):

    img = cv2.imread(img_url)

    # caso a img não seja None, o python aponta um erro ao comparar uma matriz com None
    # por isso é preciso colocar o tratamento de erro em um try/except:
    try: 
        if img == None: # se não leu o cv2.imread() retorna None
            print(f"Erro ao ler a imagem 'f{img_url}'.")
            print("Verifique se o nome está correto.")
            exit(1)
    except:
        pass

    # o cv2 usa o por padrão BGR, para converter em RBG:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # face_encodings retorna uma lista com os rostos contidos na imagem, como o 
    # objetivo é pegar apenas um rosto, basta usar o índice 0 
    face = fr.face_encodings(img)[0]

    return face

def get_faces_in_frame(frame):
    faces = fr.face_encodings(frame)
    return faces

def face_is_valid(faces, face_ref):
    if faces != None:
        for i in range(len(faces)):
            result = fr.compare_faces([face_ref], faces[i])[0]
            if result:
                return True
    return False

def DrawInFaces(frame_rgb, faces_found, frame, face_ref=[]):
    faces_loc = fr.face_locations(frame_rgb)

    if len(faces_loc) < 1:
        return frame
    
    for face_loc, face_found in zip(faces_loc, faces_found):
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # se houver alguma face de referência, será desenhado um retangulo verde no rosto
        # correspondente presente no frame
        if len(face_ref) > 0:
            if fr.compare_faces([face_ref], face_found)[0]:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,180,0), 2)
                continue

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,0), 2)

    return frame

def CloseCam(cam):
    cam.release() # finaliza a conexão com a webcam
    cv2.destroyAllWindows() # garante que as janelas criadas serão fechadas ao encerrar o programa


# retorna um tupla: [0]: se as faces foram achadas; [1]: se foi possível detectar alguma face, retorna se foi válida
def facial_validation(imgRef_url, index_cam=0):
    face_ref = get_encoding_face(imgRef_url)
    
    # sobre a classe VideoCapture(): https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    webcam = cv2.VideoCapture(index_cam) # faz a conexão com a webcam

    if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
        
        validation = True
        count = 0 # variável usada para aguardar um determinado tempo até retornar algo

        while validation and count <= 40:
            
            count += 1

            validation, frame = webcam.read() # le imagem da webcam

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converte a imagem para rgb

            faces_found = get_faces_in_frame(frame_rgb)

            if faces_found:
                if count >= 3: # aguarda count chegar a três para desenhar um retângulo verde na face válida, se tiver
                    frame = DrawInFaces(frame_rgb, faces_found, frame, face_ref)
                else:
                    frame = DrawInFaces(frame_rgb, faces_found, frame)
                
                if count >= 5: # a partir de count == 5, começa a poder retornar algo
                    if face_is_valid(faces_found, face_ref):
                        CloseCam(webcam)
                        return True,True
                    elif count >= 10:
                        CloseCam(webcam)
                        return True, False
                
            elif count >= 20:
                CloseCam(webcam)
                return False, False
            
            cv2.waitKey(1)
            cv2.imshow("Face validation", frame)
    else:
        print("Problema na conexão com a webcam.")
        exit(1)

    CloseCam(webcam)        
    return False, False

