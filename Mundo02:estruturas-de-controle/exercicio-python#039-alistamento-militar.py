from datetime import date
from termcolor import colored, cprint
'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
def play():
  exercise()

  year_birth = int(input("Type your year birth: "))
  actual_year = date.today().year
  age_young_person = actual_year - year_birth
  enlist_age = 18

  if (age_young_person == enlist_age):
    print(f"Your age is {age_young_person}. You are able to enlist.")
  elif (age_young_person < enlist_age):
    print(f"Your age is {age_young_person}. Your aren't able to enlist. You are {enlist_age - age_young_person} years younger than allowed to enlist. You return in {year_birth + enlist_age}." )
  else:
    print(f"Your age is {age_young_person}. Your aren't able to enlist. You are {age_young_person - enlist_age} years older than allowed to enlist. You should have enlisted in {year_birth + enlist_age}")    

def exercise():
  cprint("Make a program that reads the year of birth of a young person and informs, according to his age, if he is still going to enlist in the military, if it is an exact time to enlist, or if he alredy past enlistment time. Your program should also show how much time is left or past the deadline.\n","green", attrs=["blink"])
