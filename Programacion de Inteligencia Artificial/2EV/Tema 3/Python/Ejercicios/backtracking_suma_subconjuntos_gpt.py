def subset_sum(conjunto, target, index=0, current=None, current_sum=0):
    if current is None:
        current = []
    
    # Si se alcanza la suma objetivo, se imprime la solución encontrada.
    if current_sum == target:
        print(current)
        # Se retorna aquí para evitar seguir sumando, ya que los números son positivos.
        return
    
    # Si la suma actual supera el objetivo o se han evaluado todos los elementos, se retrocede.
    if current_sum > target or index >= len(conjunto):
        return

    # Opción 1: Incluir el elemento actual y avanzar.
    subset_sum(conjunto, target, index + 1, current + [conjunto[index]], current_sum + conjunto[index])
    
    # Opción 2: No incluir el elemento actual y avanzar.
    subset_sum(conjunto, target, index + 1, current, current_sum)


if __name__ == '__main__':
    conjunto = [3, 34, 4, 12, 5, 2]
    target = 9
    print("Subconjuntos cuya suma es", target, ":")
    subset_sum(conjunto, target)
