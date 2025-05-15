import tensorflow as tf
import os

TRAIN_ROOT_DIR='ruta_al_dataset/train'
rock_dir = os.path.join(TRAIN_ROOT_DIR,'./rock')
paper_dir = os.path.join(TRAIN_ROOT_DIR,'./paper')
scissors_dir = os.path.join(TRAIN_ROOT_DIR,'./scissors')

print('imagenes totales de piedra:', len(os.listdir(rock_dir)))
print('imagenes totales de papel:', len(os.listdir(paper_dir)))
print('imagenes totales de tijera:', len(os.listdir(scissors_dir)))
rock_files = os.listdir(rock_dir)
print(rock_files[:10])

paper_files = os.listdir(paper_dir)
print(paper_files[:10])

scissors_files = os.listdir(scissors_dir)
print(scissors_files[:10])

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pic_index = 2

next_rock = [os.path.join(rock_dir, fname)
                for fname in rock_files[pic_index-2:pic_index]]
next_paper = [os.path.join(paper_dir, fname)
                for fname in paper_files[pic_index-2:pic_index]]
next_scissors = [os.path.join(scissors_dir, fname)
                for fname in scissors_files[pic_index-2:pic_index]]
fig,axs=plt.subplots(3, 2)
for i, img_path in enumerate(next_rock+next_paper+next_scissors):
  img = mpimg.imread(img_path)
  print(img_path)
  subfigura=axs[i//2][i%2]
  subfigura.imshow(img)
  subfigura.axis('Off')
  subfigura.set_title(img_path.split('/')[-2:],fontsize=8)
plt.show()

# con el método tf.keras.preprocessing.image_dataset_from_directory,
# carga el dataset:


# crea un modelo secuencial para aumentación de datos
# utiliza las capas Rescaling, RandomFlip, RandomRotation,RandomZoom

# Crear un modelo de keras incluyendo:
# la capa de aumentación
# dos convoluciones con su cala de pooling Max
# una capa densa con activación softmax

# imprime el resumen del modelo



# compila


# entrena

# evalua sobre el conjunto de test


# prueba algún ejemplo


