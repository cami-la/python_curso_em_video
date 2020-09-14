from termcolor import cprint
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

def play():
  exercise()

  team = []

  player = {}

  while(True):
    player["name"] = str(input("name: "))
    player["gols"] = []
    player["soccer matches"] = int(input("matches: "))
    gols = []

    for i in range(player["soccer matches"]):
      gols.append(int(input(f"    How many goals in the match {i+1}? ")))
      player["gols"] = gols[:]
    gols.clear()

    team.append(player.copy())

    to_continue = str(input("Do you want to continue?" )).upper().strip()
    while(to_continue not in "YN"):
      to_continue = str(input("Invalid Input! Try again [Y/N]: ")).upper().strip()
    if(to_continue == "N"):
      break
  
  print("-"*50)
  print("cod", end=" ")
  for k in player.keys():
    print(f"{k:<15}", end="")
  print()

  print("-"*50)

  for k, v in enumerate(team):
    print(f"{k:>3} ", end="")
    for d in v.values():
      print(f"{str(d):<15}", end="")
    print()
  print("-"*50)    

  while(True):
    search = int(input("How data from which player? (999 exit) ")) 
    if (search == 999):
      break
    if search >= len(team):
      print("Invalid Input! Type again")
    else:
      print(f" ----- PLAYER {team[search]['name']}----- ")
      for i, v in enumerate(team[search]['gols']):
        print(f"In the match {i+1} was {v} gols")
      print("-"*50)
    


def exercise():
  cprint("Create a program that manages the performance of a football player. The program will read the player's name and how many matches he has played. Then you will read the number of goals scored in each match. In the end, all of this will be kept in a dictionary, including the total goals scored during the championship\n","green", attrs=["blink"]) 
