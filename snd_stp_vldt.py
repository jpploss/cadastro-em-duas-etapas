import cv2
import face_recognition as fr

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

def DrawInFaces(frame_rgb, frame, face_ref=None):
    faces = fr.face_locations(frame_rgb)
    for face in faces:
        y1, x1, y2, x2 = face[0], face[1], face[2], face[3]

        if face_ref:
            if fr.compare_faces([face_ref], face)[0]:
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
    
    face_has_been_found = False
    valid_face = False

    webcam = cv2.VideoCapture(index_cam) # faz a conexão com a webcam

    if webcam.isOpened(): # verifica se a conexão com a webcam foi bem sucedida
        validation, frame = webcam.read() # le a imagem da webcam

        count = 0
        while validation and count <= 100:
            count += 1
            validation, frame = webcam.read()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            faces_found = get_faces_in_frame(frame_rgb)

            if faces_found:
                frame = DrawInFaces(frame_rgb, frame, face_ref)
                if face_valid(faces_found, face_ref):
                    face_has_been_found = True
                    valid_face = True
                elif count == 10:
                    face_has_been_found = True
                    valid_face = False
            elif count == 10:
                face_has_been_found = False
                valid_face = False

            cv2.imshow("Face validation", frame)
            cv2.waitKey(1)
            
    
    CloseCam(webcam)
    return face_has_been_found, valid_face

