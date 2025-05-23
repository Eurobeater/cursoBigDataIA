"""
PROMPT CHAT-GPT
dame un trozo de código para capturar la camara con opencv y con yolov8
 detectar personas y telefonos moviles
"""

import cv2
from ultralytics import YOLO

# Cargar el modelo YOLOv8 (por ejemplo, YOLOv8n o YOLOv8s)
model = YOLO('yolov8n.pt')  # Asegúrate de que tienes el archivo del modelo YOLOv8 descargado

# Inicializar la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara principal

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Etiquetas de interés
target_classes = ['person', 'cell phone']

while True:
    # Capturar el frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo capturar el frame.")
        break

    # Realizar la detección
    results = model(frame)

    # Iterar sobre las detecciones
    for result in results:
        boxes = result.boxes  # Coordenadas de las cajas
        for box in boxes:
            # Obtener información de la caja
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Coordenadas (x1, y1) y (x2, y2)
            conf = box.conf[0].cpu().numpy()           # Confianza
            cls = box.cls[0].cpu().numpy()             # Clase detectada
            label = model.names[int(cls)]             # Nombre de la clase

            # Filtrar por clases de interés
            if label in target_classes:
                # Dibujar la caja en el frame
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame con las detecciones
    cv2.imshow("Detección YOLOv8", frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
