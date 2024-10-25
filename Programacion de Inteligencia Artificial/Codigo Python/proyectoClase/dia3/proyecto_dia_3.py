texto_usuario =  input().lower()
usuario_pregunta_letra = input().lower()

texto_usuario_cada_palabra = texto_usuario.split()
cuenta_palabras_texto_usuario = len(texto_usuario_cada_palabra)



print(type(texto_usuario))
print(f"Texto escrito: " + texto_usuario)
print(type(usuario_pregunta_letra))
print(f"Palabra que se busca: " + usuario_pregunta_letra)
print(texto_usuario.count(usuario_pregunta_letra))
print(f"Palabras por separado usando split(): " +str(texto_usuario_cada_palabra))
print(f"Número de palabras: " + str(cuenta_palabras_texto_usuario))



