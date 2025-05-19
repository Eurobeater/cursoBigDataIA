import cv2
import numpy as np
from keras.models import load_model

my_model = load_model('modelos/facialKeyPoints.keras')


# cascade para detectar caras
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Definir filtros
filters = ['images/sunglasses.png', 'images/sunglasses_2.png', 'images/sunglasses_3.jpg', 'images/sunglasses_4.png', 'images/sunglasses_5.jpg', 'images/sunglasses_6.png']
filterIndex = 0

# Cargar cámara
camera = cv2.VideoCapture(0)


while True:

    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame, 1)
    frame2 = np.copy(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detectar caras
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )


    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # Capturar cara
        gray_face = gray[y:y+h, x:x+w]
        color_face = frame[y:y+h, x:x+w]

        # Normalizar
        gray_normalized = gray_face / 255.

        # Redimensionar a 96,96 para hacer la input correcta al modelo
        original_shape = gray_face.shape
        face_resized = cv2.resize(gray_normalized, (96, 96), interpolation = cv2.INTER_AREA)
        face_resized_copy = face_resized.copy()
        face_resized = face_resized.reshape(1, 96, 96, 1)

        # Predecir
        keypoints = my_model.predict(face_resized)

        # Desnormalizar
        keypoints = keypoints *96

        # Mapear los puntos clave a la imagen original
        cara_redim_color = cv2.resize(color_face, (96, 96), interpolation = cv2.INTER_AREA)
        cara_redim_color2 = np.copy(cara_redim_color)

        # Emparejarlos juntos
        points = []
        for i, co in enumerate(keypoints[0][0::2]):
            points.append((co, keypoints[0][1::2][i]))


        # Añadir filtro al frame
        gafas = cv2.imread(filters[filterIndex], cv2.IMREAD_UNCHANGED)
        gafas_ancho = int((points[7][0]-points[9][0])*1.1)
        gafas_alto = int((points[10][1]-points[8][1])/1.1)
        if gafas_ancho >0 and gafas_alto >0:
            gafas_redim = cv2.resize(gafas, (gafas_ancho, gafas_alto), interpolation = cv2.INTER_CUBIC)
            region_no_transparente = gafas_redim[:,:,:3] != 0
            cara_redim_color[int(points[9][1]):int(points[9][1])+gafas_alto, int(points[9][0]):int(points[9][0])+gafas_ancho,:][region_no_transparente] = gafas_redim[:,:,:3][region_no_transparente]

            # Redimensionar cara_redim_color a su forma original
            frame[y:y+h, x:x+w] = cv2.resize(cara_redim_color, original_shape, interpolation = cv2.INTER_CUBIC)

        # Añadir keypoints al frame 2
        contador=0
        for keypoint in points:
            keypoint=(int(keypoint[0]),int(keypoint[1]))
            #cv2.putText(cara_redim_color2,str(contador),keypoint,cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,255,0),1,cv2.LINE_AA)
            cv2.circle(cara_redim_color2, keypoint, 1, (0,255,0), 1)
            contador+=1

        frame2[y:y+h, x:x+w] = cv2.resize(cara_redim_color2, original_shape, interpolation = cv2.INTER_CUBIC)

    # visualizar las dos ventanas
    cv2.imshow("Selfie Filters", frame)
    cv2.imshow("Facial Keypoints", frame2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
