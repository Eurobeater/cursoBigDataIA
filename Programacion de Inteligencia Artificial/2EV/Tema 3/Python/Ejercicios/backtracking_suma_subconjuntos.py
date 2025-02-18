def subset_sum(conjunto, target, index=0, current=None, current_sum=0):
    if current is None:
        current = []
    
    if current_sum == target:
        print(current)
        return
    
    if current_sum > target or index >= len(conjunto):
        return

    subset_sum(conjunto, target, index + 1, current + [conjunto[index]], current_sum + conjunto[index])
    
    subset_sum(conjunto, target, index + 1, current, current_sum)


if __name__ == '__main__':
    conjunto = [3, 34, 4, 12, 5, 2]
    target = 9
    print("Subconjuntos cuya suma es", target, ":")
    subset_sum(conjunto, target)
