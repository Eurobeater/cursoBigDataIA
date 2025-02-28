def cargar_sudoku(nombre_fichero):
    tablero = []
    with open(nombre_fichero, "r") as f:
        for linea in f:
            linea = linea.strip()
            
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

def imprimir_tablero(tablero):
    for fila in tablero:
        # Para cada fila, recorremos cada número y lo imprimimos en la misma línea.
        for num in fila:
            # Imprime el número y un espacio, sin salto de línea
            print(num, end=" ")
        # Salta a la siguiente línea al terminar la fila    
        print()
    # Línea en blanco final para separar la impresión del tablero
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

# Falta encontrar vacio
# Falta resolver sudoku


# Cargar tablero
tablero = cargar_sudoku("C:/Users/Eurobeater/OneDrive/Documentos/Curso IA y Big Data Git/Programacion de Inteligencia Artificial/2EV/Tema 3/Python/Ejercicios/Resolucion de Sudokus/matriz.txt")
imprimir_tablero(tablero)