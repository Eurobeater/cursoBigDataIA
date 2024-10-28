def variables():
    texto_usuario = input()
    texto_usuario_minus = texto_usuario.lower()

    usuario_pregunta_letra_uno = input().lower()
    usuario_pregunta_letra_dos = input().lower()
    usuario_pregunta_letra_tres = input().lower()

    encuentra_python = texto_usuario.find("Python")
    encuentra_python = isPythonThere(encuentra_python)

    texto_usuario_cada_palabra = texto_usuario.split()
    cuenta_palabras_texto_usuario = len(texto_usuario_cada_palabra)
    primera_letra_texto_usuario = texto_usuario[0]
    ultima_letra_texto_usuario = texto_usuario[len(texto_usuario) - 1]

    return texto_usuario, texto_usuario_minus, usuario_pregunta_letra_uno, usuario_pregunta_letra_dos, usuario_pregunta_letra_tres, encuentra_python, texto_usuario_cada_palabra, cuenta_palabras_texto_usuario, primera_letra_texto_usuario, ultima_letra_texto_usuario


def texto_usuario_cada_palabra_reverse(texto_usuario_cada_palabra):
    texto_usuario_cada_palabra.reverse()


def allPrints(texto_usuario, texto_usuario_minus, usuario_pregunta_letra_uno, usuario_pregunta_letra_dos, usuario_pregunta_letra_tres, encuentra_python, texto_usuario_cada_palabra, cuenta_palabras_texto_usuario, primera_letra_texto_usuario, ultima_letra_texto_usuario):
    print(f"Texto escrito: " + texto_usuario)

    print(f"Coinde con " + str(usuario_pregunta_letra_uno) + ": " + str(texto_usuario_minus.count(usuario_pregunta_letra_uno)))
    print(f"Coinde con " + str(usuario_pregunta_letra_dos) + ": " + str(texto_usuario_minus.count(usuario_pregunta_letra_dos)))
    print(f"Coinde con " + str(usuario_pregunta_letra_tres) + ": " + str(texto_usuario_minus.count(usuario_pregunta_letra_tres)))
    print(f"Palabras por separado: " + str(texto_usuario_cada_palabra))
    print(f"Número de palabras: " + str(cuenta_palabras_texto_usuario))
    print(f"Primera letra: " + primera_letra_texto_usuario)
    print(f"Ultima letra: " + ultima_letra_texto_usuario)

    texto_usuario_cada_palabra_reverse(texto_usuario_cada_palabra)
    print(f"Palabras del revés: " + str(texto_usuario_cada_palabra))
    print(f"¿Se encuentra la palabra Python?: " + str(encuentra_python))


def isPythonThere(encuentra_python):
    if encuentra_python == -1:
        encuentra_python = "No"
    else :
        encuentra_python = "Si"

    return encuentra_python


texto_usuario, texto_usuario_minus, usuario_pregunta_letra_uno, usuario_pregunta_letra_dos, usuario_pregunta_letra_tres, encuentra_python, texto_usuario_cada_palabra, cuenta_palabras_texto_usuario, primera_letra_texto_usuario, ultima_letra_texto_usuario = variables()
allPrints(texto_usuario, texto_usuario_minus, usuario_pregunta_letra_uno, usuario_pregunta_letra_dos, usuario_pregunta_letra_tres, encuentra_python, texto_usuario_cada_palabra, cuenta_palabras_texto_usuario, primera_letra_texto_usuario, ultima_letra_texto_usuario)

