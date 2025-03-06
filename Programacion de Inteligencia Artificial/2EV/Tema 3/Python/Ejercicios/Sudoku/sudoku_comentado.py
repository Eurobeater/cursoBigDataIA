import os
print(os.getcwd())

# Carga el sudoku dessde un archivo y devuelve una lista de listas (matriz)
def cargar_sudoku(nombre_fichero):
    tablero = []
    
    # Abrir el archivo en modo lectura y cerrarlo automáticamente
    with open(nombre_fichero, "r") as f:
        # Iterar por cada línea del archivo
        for linea in f:
            # Quitar espacios y saltos de líneas
            linea = linea.strip()
            # Ignorar líneas vacías
            if linea == "":
                continue
            
            # Separa la línea por ";"
            linea_con_split = linea.split(";")
            # Inicializa una lista vacía para la fila
            fila = []
            # Para cada cadena en la lista 'partes'
            for numero_str in linea_con_split:
                # Convierte la cadena a entero y añádelo a la lista 'fila'
                fila.append(int(numero_str))
            # Añade la fila completa al tablero
            tablero.append(fila)
    return tablero

# Imprime el tablero de forma legible
def imprimir_tablero(tablero):
    for fila in tablero:
        # Convertir los números a texto y unirlos, separándolos con un espacio.
        print(" ".join(str(num) for num in fila))
    print()

# Comprueba si es válido colocar 'num' en la posición (fila, col) del tablero.
def es_valido(tablero, fila, col, num):
    # Verificar que el número no aparece en la misma fila.
    if num in tablero[fila]:
        return False
    
    # Verificar columna:
    for i in range(9):
        # Acceder a la celda en la fila i y en la columna col.
        if tablero[i][col] == num:
            return False
    
    # Verificar el bloque de 3x3:
    # Calcular el índice de la primera fila del bloque 3x3
    inicio_fila = (fila // 3) * 3
    # Calcular el índice de la primera columna del bloque 3x3
    inicio_col = (col // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False
    
    return True

# Encuentra una celda vacía (con 0). Devuelve (fila, col) o None si no hay.
def encontrar_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

# Resuelve el Sudoku usando backtracking. True si lo ha resuelto, False si no hay solución
def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    # Si no hay vacíos, el Sudoku está completo.
    if not vacio:
        return True
    
    # Obtener la posición de la celda vacía
    fila, col = vacio
    
    # Probar números del 1 al 9 en la celda vacía, intentar rellenar la tabla vacía
    for num in range(1, 10):
        # Verificar si es válido colocar el número
        if es_valido(tablero, fila, col, num):
            # Colocar el número en la celda
            tablero[fila][col] = num
            
            # Llamada recursiva para resolver el tablero. Si con este número se llega a la solución, retorna True.
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

main()
