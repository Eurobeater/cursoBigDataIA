import cv2.data
import numpy as np


## Aplicar el algoritmo Viola-Jones (cascade-classifier) para detectar caras
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# cap es un objeto que permite extraer frame a frame (cámara web=0)
# Si no se puede acceder a la cámara, sale un mensaje de error y se detiene.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Bucle que captura frames desde la cámara. Si falla (False), se interrumpe.
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("No puedo leer frames de la cámara ...")
        break


    # Se convierte el frame a escala de grises. Detecta las caras con el clasificador Haar.
    # he podido leer un frame
    #proceso
    image_bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # voy a aplicar viola-jones para obtener un array de coordenas (tuplas de 4)
    # donde cada coordenada representa una cara
    faces=faceCascade.detectMultiScale(image_bw, scaleFactor=1.1,
                                 minNeighbors=5,minSize=(30,30))
    
    # Recorre todas las caras detectadas. El rostro se define por un rectangulo con coordenadas.
    # Se extrae luego el área donde se ha detectado la cara
    for (x,y,w,h) in faces:
        # pintar rectángulo alrededor de la cara
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cara=frame[y:y+h,x:x+w]

        #cara=cv2.GaussianBlur(cara,(81,81),30)

        # dentro de la cara, buscar los ojos
        ojos=eyeCascade.detectMultiScale(cara,scaleFactor=1.3,minNeighbors=10,minSize=(5,5))
        for (ox,oy,ow,oh) in ojos:
            ojo=frame[oy+y:oy+oh+y,ox+x:ox+ow+x]
            ojo=cv2.GaussianBlur(ojo,(15,15),10)
            frame[oy+y:oy+oh+y,ox+x:ox+ow+x]=ojo

        #cv2.imshow('caraconojos',cara)

    # Se dibuja un marco azul alrededor de una región del frame.
    # Se añade un texto informativo al frame.
    #pequeña transformación a image_flipped
    cv2.rectangle(frame,(20,20),(620,460),(255,0,0),3)
    cv2.putText(frame,"Imagen procesada por OpenCV",
               (25,75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    #cv2.circle(image_flipped,(320,240),50,(255,0,0),3)
    cv2.imshow('mi camara',frame)



    # Finaliza el progrmaa al presionar la tecla q.
    if cv2.waitKey(33) == ord('q'):
        break

