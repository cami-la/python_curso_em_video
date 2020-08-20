from termcolor import cprint
'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

def play():
  exercise()

  teams = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo",
    "Atlético Mineiro", "Atlético-PR", "Cruzeiro", "Botafogo", "Santos",
    "Bahia", "Corinthians", "Fluminense", "Ceará", "Vasco da Gama", "Sport Recife",
    "América-MG", "Chapecoense", "Vitória", "Paraná")
  
  print("=-"*20)
  print(f"List of brasileirão teams: {teams}")
  print("=-"*20)
  print(f"The first 5 teams: {teams[:5]}")
  print("=-"*20)
  print(f"The last 4 teams: {teams[-4:]}")
  print("=-"*20)
  print(f"Teams in alphabetical order: {sorted(teams)}")
  print("=-"*20)
  print(f"The position of Chapecoense is: {teams.index('Chapecoense')+1}º position")



def exercise():
  cprint("""Create a tuple filled with the top 20 of the Brazilian Football Championship table, in the order of placement. After show:
A) The first 5 teams
B) The last 4 placed
C) Teams in alphabetical order
D) What position is the Chapecoense team in\n""","green", attrs=["blink"])
