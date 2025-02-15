# Datos del problema
W = 10                      # Capacidad máxima de la mochila
w = [2, 3, 4, 5]            # Pesos de los objetos
v = [3, 4, 5, 6]            # Valores de los objetos
N = len(w)                  # Número de objetos

# Variable global para almacenar el mejor valor encontrado
mejor_valor = 0

def mochila_backtracking(i, peso_actual, valor_actual):
    global mejor_valor
    # Si se han evaluado todos los objetos
    if i == N:
        # Actualizamos el mejor valor si la solución actual es mejor
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
        return
    
    # Opción 1: No incluir el objeto i
    mochila_backtracking(i + 1, peso_actual, valor_actual)
    
    # Opción 2: Incluir el objeto i (solo si no se excede la capacidad)
    if peso_actual + w[i] <= W:
        mochila_backtracking(i + 1, peso_actual + w[i], valor_actual + v[i])

if __name__ == '__main__':
    mochila_backtracking(0, 0, 0)
    print("El mejor valor obtenido es:", mejor_valor)
