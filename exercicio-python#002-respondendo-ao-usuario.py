from termcolor import colored, cprint
'''
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''

def play():
  exercise()

  # o comando input pede uma entrada e salva ela em uma variável
  name = input("Type your name: ")
  # "f" na frente da string seguido de {} é a abreviação de .format()
  print(f"Welcome, {name}!")


def exercise():
  cprint("Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.\n","green", attrs=["blink"])
