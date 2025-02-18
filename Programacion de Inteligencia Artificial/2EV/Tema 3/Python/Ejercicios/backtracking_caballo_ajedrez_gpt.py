def es_valido(x, y, board):
    n = len(board)
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def imprimir_tablero(board):
    for fila in board:
        print(" ".join(str(celda).rjust(2, ' ') for celda in fila))
    print()

def recorrido_caballo(x, y, movei, board, movimientos):
    n = len(board)
    # Si se han llenado todas las casillas, se encontró una solución.
    if movei == n * n:
        return True

    # Probar cada uno de los 8 posibles movimientos del caballo.
    for dx, dy in movimientos:
        next_x, next_y = x + dx, y + dy
        if es_valido(next_x, next_y, board):
            board[next_x][next_y] = movei
            if recorrido_caballo(next_x, next_y, movei + 1, board, movimientos):
                return True
            # Retroceder
            board[next_x][next_y] = -1
    return False

def caballo_tour(n):
    # Inicializar el tablero con -1 indicando casillas sin visitar.
    board = [[-1 for _ in range(n)] for _ in range(n)]
    # Movimientos posibles del caballo.
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                   (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    # El caballo inicia en la posición (0, 0)
    board[0][0] = 0
    if recorrido_caballo(0, 0, 1, board, movimientos):
        print("Recorrido del Caballo en un tablero de", n, "x", n, ":")
        imprimir_tablero(board)
    else:
        print("No se encontró solución para un tablero de", n, "x", n)

if __name__ == '__main__':
    caballo_tour(5)
