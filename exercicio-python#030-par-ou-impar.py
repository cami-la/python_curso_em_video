from termcolor import colored, cprint

'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

def play():
  exercise()

  number = int(input("Type a number: "))

  if (number % 2 == 0): #ou if number // 2 == number % 2
    print(colored(f"This number {number} is EVEN.", "cyan"))
  else:
    print(colored(f"This number {number} is OLD.", "cyan"))

def exercise():
  cprint(colored("Create a program to reads a integer number and show on the screen if it is even or odd.\n","green", attrs=["blink"]))


