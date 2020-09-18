from datetime import date
from termcolor import colored, cprint
'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def play():
  exercise()

  year = int(input("what year were you born? "))
  votain(year)

def exercise():
  cprint("Create a program that has a function called vote () that will take a person's year of birth as a parameter, returning a literal value indicating whether a person has a DENIED, OPTIONAL and MANDATORY vote in the elections.\n","green", attrs=["blink"])  

def votain(year_born):
  actual_age = date.today().year - year_born
  if (actual_age <= 15):
    print(f"With {actual_age}: don't able to vote.")
  elif ((actual_age > 16 and actual_age < 18) or actual_age > 65):
    print(f"With {actual_age}: Optional vote!")
  else:
    print(f"With {actual_age}: Able to vote!")
    
