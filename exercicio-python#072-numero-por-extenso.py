from termcolor import cprint
'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

def play():
  exercise()

  numbers_in_full = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")

  number = int(input("Type a number between 1 and 20: "))

  while (number not in range(1,20)):
    number = int(input("Try again! Type a number between 1 and 20: "))

  print(f"You typed {numbers_in_full[number-1]}")  

  

def exercise():
  cprint("Create a program that has a tuple fully populated with a full count, from zero to twenty. Your program should reads a number by keyboard (between 0 e 20) and show it in full.\n","green", attrs=["blink"])
