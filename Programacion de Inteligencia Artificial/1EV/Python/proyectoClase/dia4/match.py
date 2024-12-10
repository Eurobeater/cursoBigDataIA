serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No reconocido')

# A partir de la versión 3.10 de Python
# se puede usar el operador walrus := para asignar
# un valor a una variable y compararla en la misma línea.

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case'N-03':
        print('Motorola')
    case _:
        print('No reconocido')

cliente = {'nombre': 'Juan',
           'apellido': 'Fuentes',
           'peso': 88,
           'talla': 1.76}
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica':{'director': 'Hermanos Wachowski',
                             'protagonista': 'Keanu Reeves'}}
elementos = [cliente, pelicula, 'libro']

for elemento in elementos:
    match elemento:
        case {'nombre': nombre, 'apellido':apellido}:
            print(f"Cliente: {nombre} {apellido}")
        case {'titulo': titulo, 'ficha_tecnica':{'director':director, 'protagonista':protagonista}}:
            print(f"Pelicula {titulo} dirigada por {director} y protagonizada por {protagonista}")
