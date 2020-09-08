from termcolor import cprint
from time import sleep
from random import randint
from operator import itemgetter

'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

def play():
  exercise()

  gamers = {"gamer1": randint(1,6),
            "gamer2":randint(1,6),
            "gamer3": randint(1,6),
            "gamer4": randint(1,6)}

  for k, v in gamers.items():
    sleep(1)
    print(f"The {k} hit the number {v}")
      
  ranking = sorted(gamers.items(), key=itemgetter(1), reverse=True)

  print("-=" * 30)
  print("  ==  RANKING OF GAMERS  ==  ")

  for i, v in enumerate(ranking):
      print(f"The {i+1}o. position: {v[0]} with {v[1]}.")
      sleep(i)
  

def exercise():
  cprint("Create a program wich was four gamers play a dice and have random results. Save this results in a dictionary Python. At the end, put in this dictionary in order, knowing that que winner hit the bigger number on the dice.\n","green", attrs=["blink"])
