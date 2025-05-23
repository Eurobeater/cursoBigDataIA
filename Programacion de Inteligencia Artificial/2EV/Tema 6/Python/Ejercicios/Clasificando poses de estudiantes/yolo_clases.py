from ultralytics import YOLO

# Cargar el modelo preentrenado con https://cocodataset.org/#home
model = YOLO('yolov8n.pt')

# Listar las clases detectadas
class_names = model.names  # Diccionario con ID de clase como clave y nombre como valor

# Imprimir las clases
print("Clases detectadas por YOLOv8:")
for class_id, class_name in class_names.items():
    print(f"{class_id}: {class_name}")
