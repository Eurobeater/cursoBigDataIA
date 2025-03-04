rdd = sc.parallelize(range(1, 101))

cantidad = rdd.count()

# Calcular la suma total
suma_total = rdd.sum()

# Calcular el promedio
promedio = suma_total / cantidad

# Obtener el valor máximo
valor_maximo = rdd.max()

# Imprimir los resultados
print(f"Cantidad de elementos: {cantidad}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")
print(f"Valor máximo: {valor_maximo}")

#########

# Filtrar los números pares
rdd_pares = rdd.filter(lambda x: x % 2 == 0)

# Mapear cada número par a su cuadrado
rdd_cuadrados = rdd_pares.map(lambda x: x ** 2)

# Obtener los primeros 10 resultados
primeros_10 = rdd_cuadrados.take(10)

# Imprimir los resultados
print("Primeros 10 cuadrados de números pares:", primeros_10)

#######

# Crear tuplas en formato (último dígito del cuadrado, valor del cuadrado)
rdd_tuplas = rdd_cuadrados.map(lambda x: (str(x % 10), x))

# Usar reduceByKey para sumar los valores por cada categoría
rdd_sumado = rdd_tuplas.reduceByKey(lambda x, y: x + y)

# Obtener los resultados
resultado = rdd_sumado.collect()

# Imprimir los resultados por categoría
print("Suma de valores por categoría (último dígito del cuadrado):")
for categoria, suma in sorted(resultado):
    print(f"Dígito {categoria}: {suma}")