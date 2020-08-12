from datetime import date
from termcolor import colored
from time import sleep

'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

def play():
  exercise()

  year = int(input("What do year you want analyse? "))
  print("\nloading...")
  sleep(2)

  if (year == 0):
    year = date.today().year
  
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(colored(f"The year {year} is leap.", "cyan"))
  else:
    print(colored(f"This year {year} isn't lear.", "cyan"))  

def exercise():
  print(colored("Make a program that reads a any year and show if it is leap.\n", "magenta"))
