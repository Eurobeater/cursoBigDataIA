# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:41:22 2022

@author: ilope
https://player.vimeo.com/video/626484659

pip install programy
pip install Flask==2.1.0


"""


from programy.clients.embed.datafile import EmbeddedDataFileBot
import socket



chatbot = EmbeddedDataFileBot(files={'aiml': ['aiml-source'] }, defaults=True)
print(chatbot.__dir__)

chatbot.ask_question('quiero jugar')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
port = 8000

server.bind((server_ip, port))
server.listen(0)
print(f"Escuchando en {server_ip}:{port}")

while True:
  client_socket, client_address = server.accept()
  print(f"Conexión entrante de {client_address[0]}:{client_address[1]}")
  while True:
    request = client_socket.recv(1024)
    if not request:
      print(f"Conexión cerrada!")
      break;
    request = request.decode("utf-8")  # convert bytes to string
    lineas = request.splitlines()

    # Seleccionamos la última línea
    ultima_linea = lineas[-1] if lineas else ''

    print(ultima_linea)
    if request!="":
      reply="{ \"repuesta\":\""+chatbot.ask_question(ultima_linea)+"\"}\n"
      # if we receive "close" from the client, then we break
      # out of the loop and close the conneciton
      client_socket.send(reply.encode("utf-8"))

