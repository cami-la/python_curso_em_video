from random import randint
from termcolor import colored, cprint
from time import sleep

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

def play():
  exercise()

  print("""Your options:
  [1] STONE
  [2] PAPER
  [3] SCISSORS
  """)
  gamer = int(input("Choice  one option between 1 and 3: "))
  print("\nJO")
  sleep(1)
  print("KEN")
  sleep(1)
  print("PO\n")
  sleep(1)

  computer = randint(1,3)

  itens = ["stone", "paper", "scissors"]
  '''
  se :
  1 - 1 = 0 (empate)
  1 - 2 = -1 (computador)
  1 - 3 = -2 (jogador)
  2 - 1 = 1 (jogador)
  2 - 2 = 0 (empate)
  2 - 3 = -1 (computador)
  3 - 1 = 2 (computador)
  3 - 2 = 1 (jogador)
  3 - 3 = 0 (empate)
  '''
  
  if (gamer - computer == -1 or gamer - computer == 2):
    print("The computer won!")
  elif (gamer - computer == -2 or gamer - computer == 1):
    print("The gamer won!")  
  else:
    print("Tie in the game") 
  print(f"Gamer {itens[gamer-1]}x{itens[computer-1]} Computer")   

def exercise():
  cprint("Create a program that make the computer to play Jokenpo with you.\n","green", attrs=["blink"])  
