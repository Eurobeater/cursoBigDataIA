def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return suma - max(num1, num2, num3) - min(num1, num2, num3)

num1 = input("Escribe el numro 1: ")
num2 = input("Escribe el numro 2: ")
num3 = input("Escribe el numro 3: ")

print(devolver_distintos(int(num1), int(num2), int(num3)))