# -*- coding: utf-8 -*-
"""


pip install programy
pip install Flask==2.1.0


"""


from programy.clients.embed.datafile import EmbeddedDataFileBot

chatbot = EmbeddedDataFileBot(files={'aiml': ['aiml-source'] }, defaults=True)
print(chatbot.__dir__)

chatbot.ask_question('quiero jugar')

try:
  while True:
    print(chatbot.ask_question(input('> ')))
except:
  pass
