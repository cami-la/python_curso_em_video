from random import randint
from termcolor import cprint
from time import sleep
'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
def play():
  exercise()

  print("-"*30)
  print("      JOGO DA MEGA SENA      ")
  print("-"*30)

  games = []
  list_numbers = []
  total = 0

  draw = int(input("How many games do you want me to draw? "))

  for i in range(draw): 
    while(True):
      number = randint(1,60)
      if number not in list_numbers:
        list_numbers.append(number)
      if len(list_numbers) == 6:
        break
    list_numbers.sort()
    games.append(list_numbers[:])
    list_numbers.clear()   
  print()
  print("-="*3, f" GAME {draw} OF MEGA SENA ", "-="*3)

  for game in range(len(games)):
    sleep(2)    
    print(f"Game {game}: {games[game]}") 
  print()
  print("-="*3, "> GOOD LUCK <", "-="*3)


def exercise():
  cprint("Make a program that helps a MEGA SENA player to create guesses. The program will ask how many games will be generated and will raffle 6 numbers between 1 and 60 for each game, registering everything in a composite list.\n","green", attrs=["blink"])
