import os
print(os.getcwd())

def cargar_sudoku(nombre_fichero):
    """
    Carga un sudoku desde un fichero de texto y devuelve una matriz (lista de listas) de enteros.
    Cada línea del fichero tiene los números separados por punto y coma.
    Un 0 indica un hueco.
    """
    tablero = []
    with open(nombre_fichero, "r") as f:
        for linea in f:
            linea = linea.strip()  # quitar espacios y saltos de línea
            if linea == "":
                continue
            # Separa la línea por ";" y convierte cada elemento a entero
            fila = [int(num) for num in linea.split(";")]
            tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    """Imprime el tablero de forma legible."""
    for fila in tablero:
        print(" ".join(str(num) for num in fila))
    print()

def es_valido(tablero, fila, col, num):
    """Comprueba si es válido colocar 'num' en la posición (fila, col) del tablero."""
    # Verificar fila: el número no debe aparecer en la misma fila.
    if num in tablero[fila]:
        return False
    
    # Verificar columna:
    for i in range(9):
        if tablero[i][col] == num:
            return False
    
    # Verificar el bloque de 3x3:
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False
    
    return True

def encontrar_vacio(tablero):
    """Encuentra una celda vacía (con 0). Devuelve (fila, col) o None si no hay."""
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def resolver_sudoku(tablero):
    """
    Función que resuelve el Sudoku usando backtracking.
    Devuelve True si lo ha resuelto, dejando el tablero completo, o False si no hay solución.
    """
    vacio = encontrar_vacio(tablero)
    # Si no hay vacíos, el Sudoku está completo.
    if not vacio:
        return True
    
    fila, col = vacio
    
    # Probar números del 1 al 9 en la celda vacía
    for num in range(1, 10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num  # Colocar el número
            
            # Llamada recursiva: si con este número se llega a la solución, retorna True.
            if resolver_sudoku(tablero):
                return True
            
            # Si no funcionó, se hace backtracking: se reinicia la celda.
            tablero[fila][col] = 0
    
    return False  # Ningún número funcionó en esta celda

def main():
    # Carga el sudoku desde "matriz.txt"
    tablero = cargar_sudoku("C:/Users/Eurobeater/OneDrive/Documentos/Curso IA y Big Data Git/Programacion de Inteligencia Artificial/2EV/Tema 3/Python/Ejercicios/Resolucion de Sudokus/matriz.txt")
    print("Sudoku inicial:")
    imprimir_tablero(tablero)
    
    # Resolver el sudoku con backtracking
    if resolver_sudoku(tablero):
        print("Sudoku resuelto:")
        imprimir_tablero(tablero)
    else:
        print("No se pudo resolver el Sudoku.")

if __name__ == "__main__":
    main()
