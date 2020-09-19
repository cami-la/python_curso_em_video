from termcolor import cprint
'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def play():
  exercise()

  name = str(input("Player's Name: ")).strip()
  gols = input("Numbers of goals: ")

  if (gols.isnumeric()):
    gols = int(goals)
  else:
    gols = 0

  if (name.strip() == ""):
    ficha(goals=gols)
  else:
    ficha(name,gols)


def exercise():
  cprint("Make a program that has a function called token (), that receives two optional parameters: the name of a player and how many goals he scored. The program should be able to display the player's record, even if some data has not been entered correctly.\n","green", attrs=["blink"])

def ficha(player="<unknown>", goals=0):
  print(f"The player {player} scored the goals {goals} in the championship.")
