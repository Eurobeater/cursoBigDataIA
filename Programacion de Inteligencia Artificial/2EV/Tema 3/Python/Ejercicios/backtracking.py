W = 10
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
N = len(w)

mejor_valor = 0

def mochila_backtracking(i, peso_actual, valor_actual):
    global mejor_valor
    if i == N:
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
        return
    
    mochila_backtracking(i + 1, peso_actual, valor_actual)
    
    if peso_actual + w[i] <= W:
        mochila_backtracking(i + 1, peso_actual + w[i], valor_actual + v[i])

if __name__ == '__main__':
    mochila_backtracking(0, 0, 0)
    print("El mejor valor obtenido es:", mejor_valor)
