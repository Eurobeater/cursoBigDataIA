import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import cv2


# 1. Los datos de Fashion MNIST están disponibles directamente en la API de conjuntos de datos de tf.keras. Los puedes cargar así:
#
# mnist = tf.keras.datasets.fashion_mnist (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
#
# ¿Qué representan cada una de las variables que devuelve mnist.load_data()? ¿Cuántos elementos y qué forma tiene cada uno de ellos?

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

print("Training images:", training_images.shape)
print("Training labels:", training_labels.shape)
print("Test images:", test_images.shape)
print("Test labels:", test_labels.shape)

# print(mnist.load_data())


# 2. Visualiza el contenido de training_images[0] con un print. ¿Cuál es su forma? ¿Qué tipo de dato contiene? 
# Puedes visualizar una imagen en matplotlib.pyplot con el método imshow, que recibe como parámetro la imagen que quieres mostrar.

print("Contenido:")
print(training_images[0])

print("Forma:", training_images[0].shape)

print("Tipo de dato:", training_images[0].dtype)

plt.imshow(training_images[0], cmap='gray')  # cmap='gray' para imágenes en escala de grises
plt.title("training_images[0]")
plt.show()


# 3. ¿Cuántas clases diferentes de ropa hay? Visualiza en una figura de matplotlib, 10 elementos de cada clase.

nombres_clases = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

numero_clases = len(np.unique(training_labels))
print("Número de clases diferentes:", numero_clases)

# Figura de 10 imágenes por clase
plt.figure(figsize=(15, 15))

imagen = 1

for clase in range(numero_clases):
    contador = 0
    
    for i in range(len(training_labels)):
        if training_labels[i] == clase:
            plt.subplot(numero_clases, 10, imagen)
            plt.imshow(training_images[i], cmap="gray")
            plt.axis("off")
            if contador == 0:
                plt.title(nombres_clases[clase], fontsize=8)
            imagen += 1
            contador += 1
            if contador == 10:
                break

plt.suptitle("10 imágenes por cada clase", fontsize=16)
plt.tight_layout()
plt.show()


# 4. De las etiquetas verdaderas, crea la siguiente lista de clases:
# class_names = ['Camiseta', 'Pantalón', 'Jersey', 'Vestido', 'Abrigo', 'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Bota']
# x,idx = tf.unique(training_labels)
# for i in x:
#     print(class_names[i])

class_names = ['Camiseta', 'Pantalón', 'Jersey', 'Vestido', 'Abrigo', 'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Bota']

x, idx = tf.unique(training_labels)

print("Clases de training_labels:\n")
for i in range(len(class_names)):
    print(class_names[i])


# 5. Cuando trabajamos con imágenes, para pasarlas a una RNA, es mejor escalar los valores de sus píxeles.
# Normalizar es simplemente convertir los valores de los píxeles a un rango 0-1 en lugar
# de un rango 0-255 (valores posibles de un byte). Por tanto, tan sólo tienes que dividir todos los pixeles entre 255.
# Puedes investigar sobre lo que es el MinMaxScaler. Escala los valores de los píxeles de todas las imágenes.

training_images = training_images / 255.0
test_images = test_images / 255.0

# 6. Crea un modelo de keras para que aprenda las diferencias entre las clases de ropa.
# ¿Qué forma tendrá la capa de entrada? Para que la RNA procese mejor la primera capa, hay que
# aplicar una capa llamada Flatten, que “aplana la matriz que representa todos los píxeles de la imagen.
# Por tanto, la primera capa de tu modelo será: 
# define la primera capa, junto con la forma de la entrada
# tf.keras.layers.Flatten(input_shape=(28,28))

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), 
    tf.keras.layers.Dense(128, activation='relu'),  
    tf.keras.layers.Dense(10, activation='softmax') 
])


# 7.Compila el modelo utilizando el método compile con el optimizador Adam,
# función de pérdida sparse_categorical_crossentropy y utilizando como métrica “Accuracy”.

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# 8. Entrena el conjunto training_images durante 5 épocas. ¿Qué resultados obtienes? ¿Te parecen buenos?

model.fit(training_images, training_labels, epochs=5)


# 9. Evalúa el modelo con el conjunto de test y comenta los resultados que has obtenidos

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("Pérdida en test:", test_loss)
print("Precisión en test:", test_accuracy)


# 10. Ejecuta el siguiente código:
#   classifications = model.predict(test_images)
#   print(classifications[0])
# La salida, después de ejecutarla, es una lista de números. ¿Por qué crees que es así y qué representan esos números?
# ¿Qué representa esta lista? Elige la respuesta de entre las siguientes opciones
    # a)	Los 10 valores aleatorios menos significativos
    # b)	Las 10 primeras clasificaciones que hizo la RNA
    # c)    La probabilidad de que el elemento sea de cada una de las 10 clases

classifications = model.predict(test_images)
print(classifications[0])


# 12. Prueba a cargar una imagen que hayas diseñado tú, escribe el código necesario para cargar la imagen y predecir su clase. Puedes utilizar la función imread del paquete cv2 (Computer Vision 2):
    # import cv2
    # mi_imagen=cv2.imread('miImagen.png',cv2.IMREAD_GRAYSCALE)
    # plt.imshow(mi_imagen)
    

# 13. Veamos ahora las capas en tu modelo. Experimenta con diferentes valores para la capa densa con 512 neuronas.
# ¿Qué resultados diferentes obtienes para la pérdida, el tiempo de entrenamiento, etc.? ¿Por qué crees que es así?

# 512 neuronas
print("\n512 neuronas\n")
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)


# 1024 neuronas
print("\n1024 neuronas\n")
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)


# 14. ¿Qué pasaría si eliminas la capa Flatten()? ¿Por qué crees que es así?

## model = tf.keras.Sequential([
##    # tf.keras.layers.Flatten(input_shape=(28, 28)), 
##    tf.keras.layers.Dense(128, activation='relu'),  
##    tf.keras.layers.Dense(10, activation='softmax') 
## ])

## model.compile(
##     optimizer='adam',
##     loss='sparse_categorical_crossentropy',
##    metrics=['accuracy']
## )

# model.fit(training_images, training_labels, epochs=5)


# 15. Considera las capas finales (de salida). ¿Por qué hay 10? ¿Qué pasaría si tuvieras una cantidad diferente a 10? Por ejemplo, intenta entrenar la red con 5

# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(124, activation='relu'),
#     tf.keras.layers.Dense(5, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.fit(training_images, training_labels, epochs=5)


# 16. Considera los efectos de capas adicionales en la red. ¿Qué pasará si agregas otra capa entre la que tiene 512 y la capa final con 10?

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)


# 18. Prueba con 15 épocas: probablemente obtendrás un modelo con una pérdida mucho mayor que el que tiene 5.

print("\n15 épocas:\n")
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=15)


# 19. Prueba 30 épocas: es posible que vea que el valor de pérdida deje de disminuir y, a veces, aumente.
# Este es un efecto secundario de algo llamado "sobreajuste" y es algo que debes tener en cuenta al entrenar redes neuronales.
# No tiene sentido perder el tiempo entrenando si no estás mejorando la pérdida. Es como si la RNA se lo hubiera aprendido de memoria.

print("\n30 épocas:\n")
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=30)

