from termcolor import cprint
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

def play():
  exercise()

  player = {}

  player["name"] = str(input("name: "))
  player["soccer matches"] = int(input("matches: "))
  player["gols"] = []
  
  gols = []
  for i in range(player["soccer matches"]):
    gols.append(int(input(f"    How many goals in the match {i+1}? ")))
    player["gols"] = gols[:]
  gols.clear()

  player["total gols"] = sum(player["gols"])
  print("-="*30)
  print(player)
  print("-="*30)
  
  for k, v in player.items():
    print(f"The {k} field has the value {v}.")
  print("-="*30)

  print(f"  => The player {player['name']} hit {player['soccer matches']} matches:")
  for i, v in enumerate(player["gols"]):
    print(f"The match {i}, hit {v}")
  print(f"    It was a total of {player['total gols']} matches.")



def exercise():
  cprint("Create a program that manages the performance of a football player. The program will read the player's name and how many matches he has played. Then you will read the number of goals scored in each match. In the end, all of this will be kept in a dictionary, including the total goals scored during the championship\n","green", attrs=["blink"]) 
