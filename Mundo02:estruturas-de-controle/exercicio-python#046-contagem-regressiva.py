from termcolor import cprint, colored
from time import sleep
from emoji import emojize
'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

def play():
  exercise()

  for i in range(10,-1,-1):
    print(i)
    sleep(1)
  print(emojize(":star: :star: :star:",use_aliases=True))


def exercise():
  cprint("Make a program that show on the screen a countdown to the burst of fireworks, going from 10 to 0, with a 1 second pause between them.\n","green", attrs=["blink"])


