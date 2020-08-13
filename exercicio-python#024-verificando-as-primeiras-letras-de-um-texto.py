from termcolor import colored, cprint
'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

def play():
  exercise()

  name_city = str(input("Type de name of your city: ")).upper().strip()
  position_name_city = name_city.find(" ")

  if (name_city[:position_name_city] == "SANTO"):
    print("This name's city start with SANTO.")
  else:
    print("This name not start with SANTO.")  


def exercise():
  cprint("Create a program to read the name of a city and tell if it begin or not with name 'SANTO'\n","green", attrs=["blink"])
