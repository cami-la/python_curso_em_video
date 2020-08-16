from termcolor import cprint
from datetime import date

'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

def play():
  exercise()

  adulthood = []
  nonage = []
  
  for i in range(7):
    year_birth = int(input(f"What the year birth of person {i+1}: "))
    
    if (date.today().year - year_birth >= 21):
      adulthood.append(year_birth)
    else:
      nonage.append(year_birth)

  print(f"{len(adulthood)} peoples adulthood and {len(nonage)} peoples nonage.")


def exercise():
  cprint("Create a program to reads the year birth of seven people. At the end, show how many people not yet reached the adulthood and how many already are adulthood.\n","green", attrs=["blink"])  

  
