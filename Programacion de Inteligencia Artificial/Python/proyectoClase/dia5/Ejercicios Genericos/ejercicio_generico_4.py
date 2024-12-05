def contar_primos(num):
    primos = []
    for i in range(2, num + 1):
        limite = int(i ** 0.5)
        for j in range(2, limite + 1):
            if i % j == 0:
                break
            else:
                primos.append(i)
        print(primos)
        return len(primos)

print(contar_primos())