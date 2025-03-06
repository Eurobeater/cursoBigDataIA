def cargar_sudoku(nombre_fichero):
    tablero = []
    with open(nombre_fichero, "r") as f:
        for linea in f:
            linea = linea.strip()
            
            if linea == "":
                continue    
            
            linea_con_split = linea.split(";")
            fila = []
            for numero_str in linea_con_split:
                fila.append(int(numero_str))
            tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        for num in fila:
            print(num, end=" ")   
        print()
    print()

def es_valido(tablero, fila, col, num):
    if num in tablero[fila]:
        return False
    
    for i in range(9):
        if tablero[i][col] == num:
            return False
    
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False
    
    return True

def encontrar_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    
    fila, col = vacio
    
    for num in range(1, 10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            
            if resolver_sudoku(tablero):
                return True
            
            tablero[fila][col] = 0
    
    return False


def main():
    tablero = cargar_sudoku("C:/Users/Eurobeater/OneDrive/Documentos/Curso IA y Big Data Git/Programacion de Inteligencia Artificial/2EV/Tema 3/Python/Ejercicios/Resolucion de Sudokus/matriz.txt")
    print("Sudoku inicial:")
    imprimir_tablero(tablero)
    
    if resolver_sudoku(tablero):
        print("Sudoku resuelto:")
        imprimir_tablero(tablero)
    else:
        print("No se pudo resolver el Sudoku.")

main()