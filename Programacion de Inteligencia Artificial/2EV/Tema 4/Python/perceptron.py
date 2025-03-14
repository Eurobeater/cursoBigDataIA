import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definir nombres de las columnas según el dataset de Iris
columnas = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

df = pd.read_csv(r"C:\Users\USUARIO\Documents\Curso IA y Big Data\Programacion de Inteligencia Artificial\2EV\Tema 4\Python\data\iris.data", names=columnas)

# Seleccionar características (Ejemplo: sepal_length y petal_length)
X = df[["sepal_length", "petal_length"]].values

# Convertir etiquetas (Ejemplo: 'Iris-setosa' → -1, 'Iris-versicolor' → 1)
y = np.where(df["species"] == "Iris-setosa", -1, 1)

class Perceptron(object): 
    """ 
    Parámetros  
    ----------- 
        ratio : float, ratio de aprendizaje (entre 0.0 y 1.0) 
        n_iter: int, Pasadas sobre el dataset de entrenamiento. (también se llaman 
épocas)  
        semilla : int, Semilla para el generador de números aleatorios para 
inicializar el vector de pesos de forma aleatoria 
 
    Atributos  
    ---------- 
        w: 1d-array, Pesos después del entrenamiento.  
        errors: list, Número de clasificaciones erróneas (updates) en cada época 
    """  
     
    def __init__(self, ratio=0.01, n_iter=50, semilla=1): 
        self.ratio = ratio  
        self.n_iter = n_iter  
        self.semilla = semilla  
        rgen = np.random.RandomState(semilla)  
        # self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.w_ = None
        self.errors_ = [] 
 
    def fit(self, X, y): 
        """ entrenar el conjunto de datos.
               Parámetros 
        ---------- 
        X: {array-like}, shape = [n_muestras, n_caracteristicas] 
            Vectores de entrenamiento, donde n_muestras es el número de muestras 
y n_caracteristicas es el número de características. 
        y: array-like, shape = [n_muestras] Valores objetivo (target). 
 
        Devuelve  
        ------ 
            self : object 
        """ 
        rgen = np.random.RandomState(self.semilla)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])  # Ahora X está definido
 
        for _ in range(self.n_iter): 
            errors = 0  
            for xi, target in zip(X, y): 
                update = self.ratio * (target - self.predict(xi))  
                self.w_[1:] += update * xi  
                self.w_[0] += update  
                errors += int(update != 0.0) 
            self.errors_.append(errors) 
        return self 
 
    def net_input(self, X): 
        """Calcula la entrada a la red"""  
        return np.dot(X, self.w_[1:]) + self.w_[0]  
        #+ self.w_[0]*1 en realidad 
 
    def predict(self, X): 
        """Retorna la etiqueta de clase después de un paso""" 
        return np.where(self.net_input(X) >= 0.0, 1, -1) 
    
"""
# **Definir los datos antes de llamar a p.fit(X, y)**
X = np.array([[5.1, 3.5], [4.9, 3.0], [6.2, 2.9], [5.5, 3.8]])
y = np.array([1, -1, 1, -1])
"""""
 
#entrenar el perceptrón 
p=Perceptron(0.1,10,1)  
p.fit(X,y) 
 
plt.plot(range(1, len(p.errors_)+1 ), p.errors_, marker='o')  
plt.xlabel('épocas')  
plt.ylabel('número de actualizaciones')  
plt.show() 
 
#predecir una en concreto  
sepalo=3  
petalo=5  
print("la flor con longitud de sépalo",sepalo,"y longitud de pétalo", petalo, 
       "es",np.where(p.predict([sepalo, petalo])==1,'versicolor','setosa'))