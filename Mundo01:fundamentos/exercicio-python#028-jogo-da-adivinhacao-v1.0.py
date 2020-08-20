from termcolor import colored, cprint
from random import randint
from time import sleep

'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

def play():
  exercise()

  kick = int(input("Find the number drawn by the computer: "))
  computer = randint(0,5)
  
  print("Loading...")
  sleep(2)

  if (kick == computer):
    print("Congratulations, you got it hit.")
  else:
    print(f"What pity, you missed. The number sort was {computer}." )  

def exercise():
  cprint("Write a program to make the computer 'think' of an integer between 0 and 5 and ask the user to try to find out which number was chosen by the computer. The program must write on the screen whether the user won or lost.\n","green", attrs=["blink"])
