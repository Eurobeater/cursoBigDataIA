precios_cafe = [('capuchino', 1.5), ('expresso', 2.1), ('moka', 1.9)]

for elemento in precios_cafe:
    print(elemento)

for elemento in precios_cafe:
    print(f"El precio del {elemento[0]} es {elemento[1]} €")

# ¿Cuál es el café más caro?
# Esto no solucionaría el problema
# print(max(precios_cafe))

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    return (cafe_mas_caro, precio_mayor)        # Entre paréntesis para devolver una lista

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El café más caro es {cafe} y cuesta {precio} €")