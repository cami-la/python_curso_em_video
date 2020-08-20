from random import randint
from termcolor import cprint
'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

def play():
  exercise()

  count = 0
  hit = False
  print("=-"*15) 
  print("LET'S TO GAMER EVEN OR ODD")
  print("=-"*15)

  while (not hit):    

    computer = randint(0,10)
    gamer = int(input("Type a number: "))
    choice = str(input("Even or Odd? [E/O] ")).upper().strip()
    add = gamer + computer
    if (add % 2 == 0):
      print("-"*30)
      print(f"You played {gamer} and the computer {computer}. Total {add} EVEN") 
      print("-"*30)
      result = "E"
    else:
      print("-"*30)
      print(f"You played {gamer} and the computer {computer}. Total {add} ODD")
      print("-"*30)
      result = "O"

    if (choice == result):
      count += 1
      print("You won! Let's to play again!")
      print("=-"*15)
    else:
      hit = True
  print(f"Game over! You won {count} times")      


def exercise():
  cprint("Make a program to play even or odd with the computer. The game only should be breaked.\n","green", attrs=["blink"])
